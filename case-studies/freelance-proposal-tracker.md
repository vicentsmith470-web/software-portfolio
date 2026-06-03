# Freelance Proposal Tracker

## Problem

Small freelance accounts need a simple way to track proposals without paying for a CRM. The useful fields are usually client, platform, title, value, status, due date, link, and notes.

## Solution

This portfolio includes a dependency-free Python CLI that reads and writes a JSON proposal store. It can add proposals, list them in a compact table, and print a summary grouped by status with total estimated value.

## Validation

- Reads sample proposal data from `examples/proposals.sample.json`.
- Prints deterministic summary output.
- Validates Python syntax with `python -m py_compile`.
- Uses only the Python standard library.

## Sample Command

```bash
python tools/proposal_tracker.py --store examples/proposals.sample.json summary
```

