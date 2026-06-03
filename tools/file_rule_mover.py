#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


def resolve_path(base_dir: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else base_dir / path


def unique_target(path: Path) -> Path:
    if not path.exists():
        return path

    counter = 1
    while True:
        candidate = path.with_name(f"{path.stem}_{counter}{path.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def matching_files(source: Path, patterns: list[str], recursive: bool) -> list[Path]:
    matches: list[Path] = []
    for pattern in patterns:
        iterator = source.rglob(pattern) if recursive else source.glob(pattern)
        matches.extend(path for path in iterator if path.is_file())
    return sorted(set(matches))


def apply_rule(base_dir: Path, rule: dict[str, object], apply_changes: bool) -> list[dict[str, object]]:
    source = resolve_path(base_dir, str(rule["source"]))
    target = resolve_path(base_dir, str(rule["target"]))
    patterns = [str(pattern) for pattern in rule.get("patterns", ["*"])]
    action = str(rule.get("action", "copy")).lower()
    recursive = bool(rule.get("recursive", False))

    if action not in {"copy", "move"}:
        raise ValueError(f"Unsupported action: {action}")

    results: list[dict[str, object]] = []
    for source_file in matching_files(source, patterns, recursive):
        target_file = unique_target(target / source_file.name)
        result = {
            "rule": rule.get("name", ""),
            "action": action,
            "source": str(source_file),
            "target": str(target_file),
            "applied": apply_changes,
        }

        if apply_changes:
            target_file.parent.mkdir(parents=True, exist_ok=True)
            if action == "copy":
                shutil.copy2(source_file, target_file)
            else:
                shutil.move(str(source_file), str(target_file))

        results.append(result)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Preview or apply file move/copy rules.")
    parser.add_argument("rules_file", help="JSON file containing file organization rules.")
    parser.add_argument("--apply", action="store_true", help="Apply changes. Defaults to dry-run preview.")
    args = parser.parse_args()

    rules_path = Path(args.rules_file)
    base_dir = rules_path.parent
    rules = json.loads(rules_path.read_text(encoding="utf8"))

    results: list[dict[str, object]] = []
    for rule in rules:
        results.extend(apply_rule(base_dir, rule, args.apply))

    print(json.dumps(results, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

