#!/usr/bin/env python3
"""
Build a search index for the CS 5520 site.

Reads every markdown file in ../lessons/, chunks each file by H2 section,
and writes ../search-index.json.

This is a pure static-site build step — run it locally whenever you edit
lessons, then redeploy. No server search, no backend required.

Usage:
    python3 scripts/build-search-index.py
"""

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE_ROOT = HERE.parent
LESSONS_DIR = SITE_ROOT / "lessons"
OUT_FILE = SITE_ROOT / "search-index.json"

# file → (url slug, friendly label)
FILE_TO_WEEK = {
    "Topic_01_Intro_Kotlin_Basics_I.md":             ("01", "Topic 01 — Introduction & Kotlin Basics I"),
    "Topic_02_Kotlin_Basics_II.md":                  ("02", "Topic 02 — Kotlin Basics II"),
    "Topic_03_Activity_and_Debugging.md":            ("03", "Topic 03 — Activity and Debugging"),
    "Topic_04_Compose_Basics.md":                    ("04", "Topic 04 — Compose Basics"),
    "Topic_05_Layouts_Dialogs_Navigation.md":        ("05", "Topic 05 — Layouts, Dialogs, Navigation"),
    "Topic_06_ViewModel_StateFlow_Notifications.md": ("06", "Topic 06 — ViewModel, StateFlow & Notifications"),
    "Topic_07_Lists_LazyColumn.md":                  ("07", "Topic 07 — Lists with LazyColumn"),
    "Topic_08_Gradle_Retrofit_Networking.md":        ("08", "Topic 08 — Gradle, Retrofit & Networking"),
    "Topic_09_JSON_Robust_APIs.md":                  ("09", "Topic 09 — JSON & Robust APIs"),
    "Topic_10_Firebase_Auth_Firestore.md":           ("10", "Topic 10 — Firebase Auth & Firestore"),
    "Topic_11_Storage_Room_DataStore.md":            ("11", "Topic 11 — Storage, Room & DataStore"),
    "Topic_12_Location_Maps.md":                     ("12", "Topic 12 — Location & Maps"),
    "Topic_13_CameraX_Animations.md":                ("13", "Topic 13 — CameraX & Animations"),
    "Topic_14_Project_Work_KMP_Kickoff.md":          ("14", "Topic 14 — Project Work & KMP Kickoff"),
    "Topic_15_Project_Work_Polish_Testing.md":       ("15", "Topic 15 — Polish & Testing"),
    "KMP_Optional_Module.md":                       ("kmp", "Optional — Kotlin Multiplatform"),
    "Cloud_AI_Optional_Module.md":                  ("cloud_ai", "Optional — Cloud AI"),
    "AI_Optional_Module.md":                        ("ai", "Optional — On-Device AI"),
}


def strip_markdown(text: str) -> str:
    """Collapse markdown into indexable plain text, preserving code tokens."""
    # Strip code-fence markers but KEEP the code itself — students search for API names
    text = re.sub(r"```[a-zA-Z]*\n", "", text)
    text = text.replace("```", "")
    # Inline code ticks → just keep the content
    text = re.sub(r"`([^`]+)`", r"\1", text)
    # Links [label](url) → label
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # Bold / italic markers
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"\1", text)
    text = re.sub(r"__([^_]+)__", r"\1", text)
    # Headings — drop the hashes but keep the text
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    # HTML tags
    text = re.sub(r"<[^>]+>", " ", text)
    # Collapse whitespace
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def chunk_by_section(md: str):
    """
    Split a lesson into chunks at each H2 heading.
    Returns a list of (section_title, section_body) tuples.
    The preamble before the first H2 is returned with title 'Overview'.
    """
    lines = md.split("\n")
    chunks = []
    current_title = "Overview"
    current_body: list[str] = []

    for line in lines:
        h2 = re.match(r"^##\s+(.+?)\s*$", line)
        if h2:
            if current_body:
                chunks.append((current_title, "\n".join(current_body)))
            current_title = h2.group(1).strip()
            current_body = []
        else:
            current_body.append(line)

    if current_body:
        chunks.append((current_title, "\n".join(current_body)))

    return chunks


def build_index():
    if not LESSONS_DIR.is_dir():
        raise SystemExit(f"lessons/ directory not found at {LESSONS_DIR}")

    entries = []
    for filename, (slug, label) in FILE_TO_WEEK.items():
        path = LESSONS_DIR / filename
        if not path.exists():
            print(f"  skip {filename}: file missing")
            continue

        md = path.read_text(encoding="utf-8")
        for section_title, section_body in chunk_by_section(md):
            body_plain = strip_markdown(section_body)
            if not body_plain:
                continue
            entries.append({
                "w": slug,
                "topic_label": label,
                "section": section_title,
                "body": body_plain,
                "url": f"/week.html?w={slug}",
            })

    OUT_FILE.write_text(
        json.dumps(entries, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    print(f"Wrote {OUT_FILE} ({len(entries)} sections across {len(FILE_TO_WEEK)} lessons)")


if __name__ == "__main__":
    build_index()
