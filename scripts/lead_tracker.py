"""
lead_tracker.py — Simple CLI-based lead tracking.

Usage:
    python scripts/lead_tracker.py add --name "Jane Doe" --org "UNICEF" --source linkedin
    python scripts/lead_tracker.py list
    python scripts/lead_tracker.py list --status active
    python scripts/lead_tracker.py update --id 3 --status converted --notes "Signed for Q3 survey project"
"""

import argparse
import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

LEADS_FILE = Path(__file__).parent.parent / "data" / "leads" / "leads.csv"
FIELDNAMES = ["id", "date_added", "name", "org", "source", "status", "notes", "last_contact"]


def ensure_file():
    LEADS_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not LEADS_FILE.exists():
        with open(LEADS_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()


def read_leads() -> list[dict]:
    ensure_file()
    with open(LEADS_FILE, newline="") as f:
        return list(csv.DictReader(f))


def write_leads(leads: list[dict]):
    with open(LEADS_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(leads)


def add_lead(args):
    leads = read_leads()
    next_id = max((int(l["id"]) for l in leads), default=0) + 1
    new_lead = {
        "id": next_id,
        "date_added": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "name": args.name,
        "org": args.org or "",
        "source": args.source or "",
        "status": "active",
        "notes": args.notes or "",
        "last_contact": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }
    leads.append(new_lead)
    write_leads(leads)
    print(f"Added lead #{next_id}: {args.name} ({args.org})")


def list_leads(args):
    leads = read_leads()
    if args.status:
        leads = [l for l in leads if l["status"] == args.status]
    if not leads:
        print("No leads found.")
        return
    print(f"\n{'ID':<4} {'Date':<12} {'Name':<25} {'Org':<20} {'Source':<12} {'Status':<12}")
    print("-" * 85)
    for l in leads:
        print(f"{l['id']:<4} {l['date_added']:<12} {l['name']:<25} {l['org']:<20} {l['source']:<12} {l['status']:<12}")
    print(f"\nTotal: {len(leads)} lead(s)")


def update_lead(args):
    leads = read_leads()
    for lead in leads:
        if int(lead["id"]) == args.id:
            if args.status:
                lead["status"] = args.status
            if args.notes:
                lead["notes"] = args.notes
            lead["last_contact"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            write_leads(leads)
            print(f"Updated lead #{args.id}: {lead['name']}")
            return
    print(f"Lead #{args.id} not found.")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="A3DI Lead Tracker")
    sub = parser.add_subparsers(dest="command", required=True)

    add_parser = sub.add_parser("add")
    add_parser.add_argument("--name", required=True)
    add_parser.add_argument("--org", default="")
    add_parser.add_argument("--source", default="", help="e.g., linkedin, conference, referral, webinar")
    add_parser.add_argument("--notes", default="")

    list_parser = sub.add_parser("list")
    list_parser.add_argument("--status", help="Filter by status: active, contacted, proposal, converted, lost")

    update_parser = sub.add_parser("update")
    update_parser.add_argument("--id", type=int, required=True)
    update_parser.add_argument("--status")
    update_parser.add_argument("--notes")

    args = parser.parse_args()
    {"add": add_lead, "list": list_leads, "update": update_lead}[args.command](args)


if __name__ == "__main__":
    main()
