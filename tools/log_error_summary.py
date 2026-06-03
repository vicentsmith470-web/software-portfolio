#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


LEVEL_RE = re.compile(r"\b(INFO|WARN|WARNING|ERROR|DEBUG)\b[:\]\s-]*(.*)", re.IGNORECASE)


def normalize_level(level: str) -> str:
    level = level.upper()
    return "WARN" if level == "WARNING" else level


def summarize_log(path: Path, limit: int) -> int:
    levels: Counter[str] = Counter()
    important_messages: Counter[str] = Counter()

    for raw_line in path.read_text(encoding="utf8").splitlines():
        match = LEVEL_RE.search(raw_line)
        if not match:
            continue
        level = normalize_level(match.group(1))
        message = match.group(2).strip() or raw_line.strip()
        levels[level] += 1
        if level in {"WARN", "ERROR"}:
            important_messages[f"{level}: {message}"] += 1

    print(f"Log file: {path}")
    print("Levels:")
    for level, count in sorted(levels.items()):
        print(f"- {level}: {count}")

    print("Top warnings/errors:")
    if not important_messages:
        print("- None")
    else:
        for message, count in important_messages.most_common(limit):
            print(f"- {count}x {message}")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize warning and error messages in a log file.")
    parser.add_argument("log_file", help="Path to the log file.")
    parser.add_argument("--limit", type=int, default=5, help="Number of repeated messages to show.")
    args = parser.parse_args()
    return summarize_log(Path(args.log_file), args.limit)


if __name__ == "__main__":
    raise SystemExit(main())

