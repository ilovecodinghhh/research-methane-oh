#!/usr/bin/env python3
"""
Process all PDFs in papers/ using MinerU cloud API.
1. Build raw GitHub URLs for each PDF
2. Submit batch tasks to MinerU API
3. Poll for completion
4. Download and extract markdown results
"""

import os
import sys
import json
import time
import zipfile
import io
import glob
import urllib.parse
import requests

API_KEY = os.environ.get("MINERU_API_KEY", "")
GITHUB_REPO = "Ilovecodinghhh/research-methane-OH"
GITHUB_BRANCH = "master"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS_DIR = os.path.join(BASE_DIR, "papers")
OUTPUT_DIR = os.path.join(BASE_DIR, "papers_md")
TASKS_FILE = os.path.join(BASE_DIR, "scripts", "mineru_tasks.json")

API_BASE = "https://mineru.net/api/v4"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}


def get_raw_github_url(filepath):
    """Build raw GitHub URL for a file in the repo.
    The repo has a nested research-methane-OH/ directory at root."""
    # filepath is relative to local repo root, e.g. papers/Zhao_2019_ACP_13701.pdf
    # but in GitHub the path is research-methane-OH/papers/...
    encoded = urllib.parse.quote(f"research-methane-OH/{filepath}", safe="/")
    return f"https://raw.githubusercontent.com/{GITHUB_REPO}/{GITHUB_BRANCH}/{encoded}"


def list_pdfs():
    """List all PDFs in papers/."""
    pdfs = sorted(glob.glob(os.path.join(PAPERS_DIR, "*.pdf")))
    return pdfs


def submit_task(url, filename):
    """Submit a single extraction task."""
    r = requests.post(
        f"{API_BASE}/extract/task",
        headers=HEADERS,
        json={"url": url, "is_ocr": False, "enable_formula": True},
        timeout=30,
    )
    data = r.json()
    if data.get("code") == 0:
        return data["data"]["task_id"]
    else:
        print(f"  ERROR submitting {filename}: {data.get('msg', 'unknown error')}")
        return None


def check_task(task_id):
    """Check task status."""
    r = requests.get(
        f"{API_BASE}/extract/task/{task_id}",
        headers={"Authorization": f"Bearer {API_KEY}"},
        timeout=30,
    )
    return r.json().get("data", {})


def download_and_extract(zip_url, pdf_name):
    """Download zip result and extract markdown."""
    r = requests.get(zip_url, timeout=120)
    if r.status_code != 200:
        print(f"  Failed to download {zip_url}: {r.status_code}")
        return None

    md_content = None
    with zipfile.ZipFile(io.BytesIO(r.content)) as zf:
        for name in zf.namelist():
            if name.endswith(".md"):
                md_content = zf.read(name).decode("utf-8", errors="replace")
                break

    if md_content:
        stem = os.path.splitext(pdf_name)[0]
        out_path = os.path.join(OUTPUT_DIR, f"{stem}.md")
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        return out_path
    return None


def main():
    if not API_KEY:
        print("ERROR: MINERU_API_KEY not set")
        sys.exit(1)

    pdfs = list_pdfs()
    print(f"Found {len(pdfs)} PDFs to process")

    # Load existing tasks if resuming
    tasks = {}
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE) as f:
            tasks = json.load(f)

    # Submit tasks for PDFs not yet submitted
    for pdf_path in pdfs:
        pdf_name = os.path.basename(pdf_path)
        if pdf_name in tasks and tasks[pdf_name].get("task_id"):
            print(f"  Already submitted: {pdf_name}")
            continue

        rel_path = f"papers/{pdf_name}"
        url = get_raw_github_url(rel_path)
        print(f"  Submitting: {pdf_name}")
        task_id = submit_task(url, pdf_name)

        if task_id:
            tasks[pdf_name] = {"task_id": task_id, "state": "pending", "url": url}
        else:
            tasks[pdf_name] = {"task_id": None, "state": "error", "url": url}

        # Save after each submission
        with open(TASKS_FILE, "w") as f:
            json.dump(tasks, f, indent=2)

        # Rate limit: small delay between submissions
        time.sleep(1)

    print(f"\nAll {len(tasks)} tasks submitted. Polling for results...")

    # Poll for completion
    max_wait = 600  # 10 minutes max
    start = time.time()
    while time.time() - start < max_wait:
        pending = [
            name
            for name, t in tasks.items()
            if t.get("task_id") and t.get("state") not in ("done", "error", "failed")
        ]
        if not pending:
            break

        print(f"\n  {len(pending)} tasks still pending... checking")
        for pdf_name in pending:
            task_id = tasks[pdf_name]["task_id"]
            result = check_task(task_id)
            state = result.get("state", "unknown")
            tasks[pdf_name]["state"] = state

            if state == "done":
                zip_url = result.get("full_zip_url", "")
                tasks[pdf_name]["zip_url"] = zip_url
                if zip_url:
                    out = download_and_extract(zip_url, pdf_name)
                    if out:
                        tasks[pdf_name]["md_path"] = out
                        print(f"    ✅ {pdf_name} → {os.path.basename(out)}")
                    else:
                        print(f"    ⚠️  {pdf_name}: no markdown in zip")
                else:
                    print(f"    ⚠️  {pdf_name}: done but no zip URL")
            elif state in ("error", "failed"):
                err = result.get("err_msg", "")
                tasks[pdf_name]["error"] = err
                print(f"    ❌ {pdf_name}: {err}")

        # Save progress
        with open(TASKS_FILE, "w") as f:
            json.dump(tasks, f, indent=2)

        # Wait before next poll
        time.sleep(15)

    # Final summary
    done = sum(1 for t in tasks.values() if t.get("state") == "done")
    failed = sum(1 for t in tasks.values() if t.get("state") in ("error", "failed"))
    pending = sum(
        1
        for t in tasks.values()
        if t.get("state") not in ("done", "error", "failed", None)
    )
    print(f"\n{'='*60}")
    print(f"SUMMARY: {done} done, {failed} failed, {pending} still pending")
    print(f"Markdown files saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
