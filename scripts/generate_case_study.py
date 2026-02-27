"""
generate_case_study.py — Draft a case study from existing project materials.

Reads a scope of work, README, or any project doc and generates a structured
case study draft using Claude. Outputs to content/case-studies/.

Usage:
    # From a scope of work document
    python scripts/generate_case_study.py --source docs/sow_wfp_pipeline.pdf --slug wfp-pipeline

    # From a GitHub repo README (fetches raw README)
    python scripts/generate_case_study.py --repo https://github.com/username/project --slug project-name

    # From a local file (markdown, text, or PDF)
    python scripts/generate_case_study.py --source path/to/file.md --slug project-name

    # From multiple sources combined
    python scripts/generate_case_study.py --source sow.pdf --repo https://github.com/user/repo --slug project-name

    # Add extra context via notes
    python scripts/generate_case_study.py --source sow.pdf --slug project-name --notes "Client was very happy. Reduced reporting time from 2 weeks to 2 days."

    # Dry run (print to stdout, don't write file)
    python scripts/generate_case_study.py --source sow.pdf --slug project-name --dry-run
"""

import argparse
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import anthropic
import yaml


ROOT = Path(__file__).parent.parent
CONFIG_PATH = ROOT / "config" / "config.yaml"
BRAND_VOICE_PATH = ROOT / "config" / "brand_voice.md"
CASE_STUDY_DIR = ROOT / "content" / "case-studies"


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        print("ERROR: config/config.yaml not found. Copy from config.example.yaml and add your keys.")
        sys.exit(1)
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def load_brand_voice() -> str:
    with open(BRAND_VOICE_PATH) as f:
        return f.read()


def read_source_file(path: str) -> str:
    """Read a local file. Supports .md, .txt, .pdf (via pdftotext)."""
    p = Path(path)
    if not p.exists():
        print(f"ERROR: Source file not found: {path}")
        sys.exit(1)

    if p.suffix.lower() == ".pdf":
        try:
            result = subprocess.run(
                ["pdftotext", str(p), "-"],
                capture_output=True, text=True, check=True,
            )
            return result.stdout
        except FileNotFoundError:
            print("ERROR: pdftotext not found. Install poppler-utils: sudo apt install poppler-utils")
            sys.exit(1)
    else:
        return p.read_text()


def fetch_repo_readme(repo_url: str) -> str:
    """Fetch README from a GitHub repo URL."""
    # Normalise URL to raw README
    repo_url = repo_url.rstrip("/")
    if "github.com" in repo_url:
        parts = repo_url.replace("https://github.com/", "").split("/")
        if len(parts) >= 2:
            owner, repo = parts[0], parts[1]
            # Try common README filenames
            for filename in ["README.md", "readme.md", "README.rst", "README.txt", "README"]:
                raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{filename}"
                try:
                    result = subprocess.run(
                        ["curl", "-sf", raw_url],
                        capture_output=True, text=True, timeout=15,
                    )
                    if result.returncode == 0 and result.stdout.strip():
                        return result.stdout
                except subprocess.TimeoutExpired:
                    continue

            # Try 'master' branch as fallback
            for filename in ["README.md", "readme.md"]:
                raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/master/{filename}"
                try:
                    result = subprocess.run(
                        ["curl", "-sf", raw_url],
                        capture_output=True, text=True, timeout=15,
                    )
                    if result.returncode == 0 and result.stdout.strip():
                        return result.stdout
                except subprocess.TimeoutExpired:
                    continue

    print(f"WARNING: Could not fetch README from {repo_url}. Continuing without it.")
    return ""


def generate_case_study(materials: str, brand_voice: str, config: dict) -> str:
    """Send project materials to Claude and get back a structured case study draft."""
    client = anthropic.Anthropic(api_key=config["anthropic"]["api_key"])

    system_prompt = f"""You are writing a case study for A3DI, a data consultancy for humanitarian
and development organisations. Follow these brand voice guidelines:

{brand_voice}

TASK: Generate a case study from the project materials provided. The materials may include
scopes of work, README files, project notes, or a combination.

OUTPUT FORMAT (use exactly this structure):

## Challenge
[2-3 sentences describing the client's problem. Focus on the organisational pain point,
not the technical details.]

## Approach
[3-5 sentences on what A3DI did. Be specific about methods, tools, and process.
Mention technologies used (Python, Tableau, etc.) where relevant.]

## Result
[2-3 sentences on outcomes. Quantify where possible (time saved, coverage improved,
reports automated, etc.). If you can't quantify from the materials, use [PLACEHOLDER]
and note what metric would go there.]

## Key Takeaway
[1 sentence — the generalizable lesson from this project.]

## Services Used
[Comma-separated list from: Survey Design, Data Analysis, Data Pipelines,
Visualisation & Dashboards, Training & Capacity Building]

RULES:
- Anonymise by default: use descriptions like "a UN agency" or "an international NGO"
  instead of specific org names, unless the materials suggest the work is already public.
- Do NOT fabricate details. If the materials don't contain enough info for a section,
  write what you can and add [NEEDS INPUT: describe what's missing] placeholders.
- Keep the total length to 200-300 words.
- Write for a non-technical audience (M&E officers, programme managers) —
  mention tools but explain what they achieved, not how they work internally.
- Use British English spelling (organisation, programme, etc.)."""

    message = client.messages.create(
        model=config["anthropic"]["model"],
        max_tokens=2048,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": f"Here are the project materials. Draft a case study from them:\n\n{materials}",
            }
        ],
    )
    return message.content[0].text


def build_frontmatter(slug: str) -> str:
    """Generate YAML frontmatter for the case study file."""
    frontmatter = {
        "title": "",
        "slug": slug,
        "client_type": "",
        "sector": "",
        "region": "",
        "services_used": [],
        "status": "draft",
        "date_created": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "date_completed": "",
        "publish_to": ["website", "linkedin", "pdf"],
    }
    return yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)


def main():
    parser = argparse.ArgumentParser(
        description="Generate a case study draft from project materials"
    )
    parser.add_argument("--source", type=str, help="Path to a scope of work or project doc (.md, .txt, .pdf)")
    parser.add_argument("--repo", type=str, help="GitHub repo URL (will fetch README)")
    parser.add_argument("--slug", type=str, required=True, help="Short name for the file (e.g., 'wfp-pipeline')")
    parser.add_argument("--notes", type=str, default="", help="Additional context or notes to include")
    parser.add_argument("--dry-run", action="store_true", help="Print output without writing to file")
    args = parser.parse_args()

    if not args.source and not args.repo:
        print("ERROR: Provide at least one of --source or --repo")
        sys.exit(1)

    # Gather materials
    materials_parts = []

    if args.source:
        print(f"Reading source: {args.source}")
        content = read_source_file(args.source)
        materials_parts.append(f"=== SCOPE OF WORK / PROJECT DOCUMENT ===\n{content}")

    if args.repo:
        print(f"Fetching README from: {args.repo}")
        readme = fetch_repo_readme(args.repo)
        if readme:
            materials_parts.append(f"=== GITHUB README ===\n{readme}")

    if args.notes:
        materials_parts.append(f"=== ADDITIONAL NOTES ===\n{args.notes}")

    materials = "\n\n".join(materials_parts)

    if len(materials.strip()) < 50:
        print("ERROR: Not enough material to generate a case study. Check your inputs.")
        sys.exit(1)

    # Truncate if very long (API context limits)
    max_chars = 30000
    if len(materials) > max_chars:
        print(f"WARNING: Materials truncated from {len(materials)} to {max_chars} chars")
        materials = materials[:max_chars]

    # Generate
    config = load_config()
    brand_voice = load_brand_voice()

    print("Generating case study draft...")
    body = generate_case_study(materials, brand_voice, config)

    if args.dry_run:
        print("\n--- Generated Case Study ---\n")
        print(body)
        return

    # Write to file
    frontmatter = build_frontmatter(args.slug)
    output_path = CASE_STUDY_DIR / f"{args.slug}.md"
    output_path.write_text(f"---\n{frontmatter}---\n\n# {args.slug.replace('-', ' ').title()}\n\n{body}\n")
    print(f"Case study draft written to: {output_path}")
    print(f"Next steps:")
    print(f"  1. Review and fill in any [PLACEHOLDER] or [NEEDS INPUT] markers")
    print(f"  2. Update the frontmatter (title, client_type, sector, region)")
    print(f"  3. When ready, change status to 'ready'")


if __name__ == "__main__":
    main()
