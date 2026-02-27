"""
weekly_review.py — Weekly marketing KPI snapshot and content calendar check.

Usage:
    python pipelines/weekly_review.py
    python pipelines/weekly_review.py --output data/analytics/weekly_2026-03-01.md

Checks:
- Upcoming content due in the next 14 days
- Overdue drafts (past due date, not published)
- Lead pipeline summary
- Post-publish stats (when analytics integration is live)
"""

import argparse
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
CALENDAR_PATH = ROOT / "config" / "content_calendar.yaml"
LEADS_PATH = ROOT / "data" / "leads" / "leads.csv"


def load_calendar() -> list[dict]:
    """Flatten the content calendar into a list of items."""
    with open(CALENDAR_PATH) as f:
        cal = yaml.safe_load(f) or {}
    items = []
    for year, quarters in cal.items():
        for quarter, entries in (quarters or {}).items():
            for entry in (entries or []):
                entry["quarter"] = f"{year} {quarter}"
                items.append(entry)
    return items


def check_upcoming(items: list[dict], days: int = 14) -> list[dict]:
    today = datetime.now(timezone.utc).date()
    cutoff = today + timedelta(days=days)
    upcoming = []
    for item in items:
        try:
            d = datetime.strptime(item["date"], "%Y-%m-%d").date()
        except (ValueError, TypeError):
            continue
        if today <= d <= cutoff and item.get("status") != "published":
            upcoming.append(item)
    return sorted(upcoming, key=lambda x: x["date"])


def check_overdue(items: list[dict]) -> list[dict]:
    today = datetime.now(timezone.utc).date()
    overdue = []
    for item in items:
        try:
            d = datetime.strptime(item["date"], "%Y-%m-%d").date()
        except (ValueError, TypeError):
            continue
        if d < today and item.get("status") not in ("published", "scheduled"):
            overdue.append(item)
    return sorted(overdue, key=lambda x: x["date"])


def load_lead_summary() -> dict:
    import csv
    if not LEADS_PATH.exists():
        return {"total": 0, "active": 0, "contacted": 0, "proposal": 0, "converted": 0}
    with open(LEADS_PATH) as f:
        leads = list(csv.DictReader(f))
    summary = {"total": len(leads), "active": 0, "contacted": 0, "proposal": 0, "converted": 0}
    for lead in leads:
        status = lead.get("status", "active")
        if status in summary:
            summary[status] += 1
    return summary


def generate_report() -> str:
    items = load_calendar()
    upcoming = check_upcoming(items)
    overdue = check_overdue(items)
    leads = load_lead_summary()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    lines = [
        f"# A3DI Weekly Marketing Review — {today}",
        "",
        "## Content Pipeline",
        "",
    ]

    if upcoming:
        lines.append(f"### Upcoming (next 14 days): {len(upcoming)} items")
        for item in upcoming:
            lines.append(f"- **{item['date']}** | {item['type']} | {item['topic']} [{item['status']}]")
    else:
        lines.append("### Upcoming: Nothing due in the next 14 days")

    lines.append("")

    if overdue:
        lines.append(f"### Overdue: {len(overdue)} items")
        for item in overdue:
            lines.append(f"- **{item['date']}** | {item['type']} | {item['topic']} [{item['status']}]")
    else:
        lines.append("### Overdue: None — you're on track!")

    lines.extend([
        "",
        "## Lead Pipeline",
        "",
        f"- Total leads: {leads['total']}",
        f"- Active: {leads['active']}",
        f"- Contacted: {leads['contacted']}",
        f"- Proposal stage: {leads['proposal']}",
        f"- Converted: {leads['converted']}",
        "",
        "---",
        f"*Generated {today} by weekly_review.py*",
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Weekly marketing review")
    parser.add_argument("--output", type=Path, help="Save report to file (default: print to stdout)")
    args = parser.parse_args()

    report = generate_report()

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report)
        print(f"Report saved to: {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
