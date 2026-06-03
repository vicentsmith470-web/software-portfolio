#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def load_proposals(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf8"))


def save_proposals(path: Path, proposals: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(proposals, indent=2) + "\n", encoding="utf8")


def parse_value(raw: str) -> float:
    value = float(raw)
    if value < 0:
        raise argparse.ArgumentTypeError("value must be zero or greater")
    return value


def add_proposal(args: argparse.Namespace) -> int:
    path = Path(args.store)
    proposals = load_proposals(path)
    proposals.append(
        {
            "client": args.client,
            "platform": args.platform,
            "title": args.title,
            "value": args.value,
            "status": args.status,
            "due_date": args.due_date,
            "link": args.link,
            "notes": args.notes,
        }
    )
    save_proposals(path, proposals)
    print(f"Added proposal #{len(proposals)} to {path}")
    return 0


def list_proposals(args: argparse.Namespace) -> int:
    proposals = load_proposals(Path(args.store))
    if not proposals:
        print("No proposals found.")
        return 0

    for index, proposal in enumerate(proposals, start=1):
        value = float(proposal.get("value") or 0)
        print(
            f"{index:02d} | {proposal.get('status', ''):<10} | "
            f"${value:,.2f} | {proposal.get('platform', '')} | "
            f"{proposal.get('title', '')}"
        )
    return 0


def summarize_proposals(args: argparse.Namespace) -> int:
    proposals = load_proposals(Path(args.store))
    statuses = Counter(str(proposal.get("status", "unknown")) for proposal in proposals)
    total_value = sum(float(proposal.get("value") or 0) for proposal in proposals)

    print(f"Total proposals: {len(proposals)}")
    print(f"Estimated value: ${total_value:,.2f}")
    for status, count in sorted(statuses.items()):
        print(f"{status}: {count}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Track freelance proposals in a JSON file.")
    parser.add_argument("--store", default="proposals.json", help="Path to the proposal JSON store.")

    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a proposal.")
    add_parser.add_argument("--client", required=True)
    add_parser.add_argument("--platform", required=True)
    add_parser.add_argument("--title", required=True)
    add_parser.add_argument("--value", type=parse_value, required=True)
    add_parser.add_argument("--status", default="draft")
    add_parser.add_argument("--due-date", default="")
    add_parser.add_argument("--link", default="")
    add_parser.add_argument("--notes", default="")
    add_parser.set_defaults(func=add_proposal)

    list_parser = subparsers.add_parser("list", help="List proposals.")
    list_parser.set_defaults(func=list_proposals)

    summary_parser = subparsers.add_parser("summary", help="Summarize proposals.")
    summary_parser.set_defaults(func=summarize_proposals)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

