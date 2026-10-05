#!/usr/bin/env python3
"""Validate the repository's portable Agent Skills without external packages."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "instagram-stories-scraper",
    "instagram-followers-scraper",
    "instagram-following-scraper",
    "instagram-highlights-scraper",
    "instagram-campaign-monitor",
}
REQUIRED_MARKERS = (
    "APIFY_TOKEN",
    "maxTotalChargeUsd",
    "skillName",
    "skillVersion",
    "paid external service",
)


def main() -> None:
    found = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
    if found != EXPECTED:
        raise SystemExit(f"Unexpected skill set: expected {sorted(EXPECTED)}, got {sorted(found)}")

    errors: list[str] = []
    for name in sorted(EXPECTED):
        path = ROOT / "skills" / name / "SKILL.md"
        text = path.read_text(encoding="utf-8")
        frontmatter = text.split("---", 2)
        if len(frontmatter) < 3:
            errors.append(f"{name}: missing YAML frontmatter")
            continue

        header = frontmatter[1]
        declared_name = re.search(r"^name:\s*([^\n]+)$", header, re.MULTILINE)
        description = re.search(r"^description:\s*(.+)$", header, re.MULTILINE)

        if not declared_name or declared_name.group(1).strip() != name:
            errors.append(f"{name}: frontmatter name must match the directory")
        if not description or len(description.group(1).strip()) < 40:
            errors.append(f"{name}: description is missing or too vague")
        for marker in REQUIRED_MARKERS:
            if marker not in text:
                errors.append(f"{name}: missing required marker {marker!r}")

        if "apify_api_" in text:
            errors.append(f"{name}: possible Apify token committed")

    if errors:
        raise SystemExit("\n".join(errors))

    print(f"Validated {len(EXPECTED)} skills.")


if __name__ == "__main__":
    main()
