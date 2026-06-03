# Rule-Based File Organizer

## Problem

Manual file cleanup is repetitive when files need to be moved or copied from watched folders into target folders by extension, name pattern, or date-based conventions.

## Solution

This portfolio includes a dependency-free Python CLI that reads JSON rules and previews matching file operations. It supports move or copy actions, optional recursive matching, and a safe default dry-run mode before applying changes.

## Validation

- Reads rules from `examples/file_rules.sample.json`.
- Finds matching files in `examples/inbox`.
- Prints deterministic JSON output in dry-run mode.
- Uses only the Python standard library.

## Sample Command

```bash
python tools/file_rule_mover.py examples/file_rules.sample.json
```

