#!/usr/bin/env python3
"""Rename all PDF and MD files to standardized convention: LeadAuthorYearJournal"""

import os
import shutil

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_DIR = os.path.join(BASE, "papers")
MD_DIR = os.path.join(BASE, "papers_md")

# Mapping: old_name_stem -> new_name_stem
# Convention: LeadAuthorSurnameYearJournalAbbrev
RENAME_MAP = {
    "Acquah_2025_ACP_13665":        "Acquah2025ACP",
    "Anderson_2021_ACP":            "Anderson2021ACP",
    "Anderson_2023_ACP_6319":       "Anderson2023ACP",
    "Bousquet_2005_ACP_2635":       "Bousquet2005ACP",
    "Duncan_2024_ACP_13001":        "Duncan2024ACP",
    "Fiore (2024)":                 "Fiore2024AREPS",
    "He et al.2026":                "He2026Science",
    "He, J. et al.2021":            "He2021GRL",
    "Holmes_2013_ACP_285":          "Holmes2013ACP",
    "John_2012_ACP_12021":          "John2012ACP",
    "Lawrence_2001_ACP_37":         "Lawrence2001ACP",
    "Lelieveld_2016_ACP":           "Lelieveld2016ACP",
    "McNorton_2016_ACP_7943":       "McNorton2016ACP",
    "Mertens_2024_ACP":             "Mertens2024ACP",
    "Montzka, S.A. et al.2011":     "Montzka2011Science",
    "Murray_2014_ACP_3589":         "Murray2014ACP",
    "Naik_2013_ACP_5277":           "Naik2013ACP",
    "Naus_2019_ACP_407":            "Naus2019ACP",
    "Naus_2021_ACP_4809":           "Naus2021ACP",
    "Nguyen, N.H. et al.2020":      "Nguyen2020GRL",
    "Nicely_2020_ACP_1341":         "Nicely2020ACP",
    "Nicely, J.M. et al.2018":      "Nicely2018JGR",
    "Patra (2014) Nature,":         "Patra2014Nature",
    "Patra (2021) JGR":             "Patra2021JGR",
    "Prather (2012)":               "Prather2012GRL",
    "Prather, M.J. & Zhu, X.2024":  "Prather2024JAMES",
    "Prather & Zhu (2024) Science": "Prather2024Science",
    "Prinn (2001)":                 "Prinn2001Science",
    "Prinn (2005)":                 "Prinn2005GRL",
    "Rigby, M. et al.2017":         None,  # DUPLICATE of McNorton2016ACP
    "Rowlinson_2019_ACP_8669":      "Rowlinson2019ACP",
    "Saunois_2017_ACP_11135":       "Saunois2017ACP",
    "Saunois_2020_ESSD_1561":       "Saunois2020ESSD",
    "Saunois_2025_ESSD_1873":       "Saunois2025ESSD",
    "Souri_2024_ACP_8677":          "Souri2024ACP",
    "Stevenson_2020_ACP_12905":     "Stevenson2020ACP",
    "Turner, A.J. et al.2017":      "Turner2017PNAS",
    "turner-et-al-2017":            None,  # DUPLICATE of Turner2017PNAS
    "Voulgarakis et al.2013_ACP":   "Voulgarakis2013ACP",
    "Wild_2020_ACP_4047":           "Wild2020ACP",
    "Zhao_2020_ACP_13011":          "Zhao2020aACP",
    "Zhao_2020_ACP_9525":           "Zhao2020bACP",
    "Zhao et al.2019":              "Zhao2019ACP",
    "Zhao et al.2023":              "Zhao2023ACP",
    "Zhu et al.2025":               "Zhu2026JAMES",
}

DUPLICATES_TO_REMOVE = []

def rename_in_dir(directory, ext):
    for old_stem, new_stem in RENAME_MAP.items():
        old_path = os.path.join(directory, f"{old_stem}{ext}")
        if not os.path.exists(old_path):
            continue
        if new_stem is None:
            DUPLICATES_TO_REMOVE.append(old_path)
            print(f"  DUPLICATE (will remove): {old_path}")
            continue
        new_path = os.path.join(directory, f"{new_stem}{ext}")
        if old_path == new_path:
            continue
        if os.path.exists(new_path):
            print(f"  WARNING: target exists, skipping: {new_path}")
            continue
        os.rename(old_path, new_path)
        print(f"  {os.path.basename(old_path)} -> {os.path.basename(new_path)}")


print("=== Renaming PDFs ===")
rename_in_dir(PDF_DIR, ".pdf")
print("\n=== Renaming MDs ===")
rename_in_dir(MD_DIR, ".md")

print(f"\n=== Removing {len(DUPLICATES_TO_REMOVE)} duplicates ===")
for dup in DUPLICATES_TO_REMOVE:
    os.remove(dup)
    print(f"  Removed: {dup}")

# Verify
print("\n=== Final PDF list ===")
for f in sorted(os.listdir(PDF_DIR)):
    if f.endswith(".pdf"):
        print(f"  {f}")
print(f"\n=== Final MD list ===")
for f in sorted(os.listdir(MD_DIR)):
    if f.endswith(".md"):
        print(f"  {f}")
