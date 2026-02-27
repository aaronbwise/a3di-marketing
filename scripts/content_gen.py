"""
content_gen.py — Generate marketing content from bullet points using Claude API.

Usage:
    python scripts/content_gen.py content/posts/drafts/2026-03-01-survey-tips.md
    python scripts/content_gen.py content/posts/drafts/2026-03-01-survey-tips.md --type carousel
    python scripts/content_gen.py content/case-studies/pipeline-project.md --type case-study

The script reads a markdown file with YAML frontmatter and bullet points in the body,
sends them to Claude with the brand voice guidelines, and writes the generated content
back into the file.
"""

import argparse
import sys
from pathlib import Path

import anthropic
import yaml


def load_config() -> dict:
    config_path = Path(__file__).parent.parent / "config" / "config.yaml"
    if not config_path.exists():
        print("ERROR: config/config.yaml not found. Copy from config.example.yaml and add your keys.")
        sys.exit(1)
    with open(config_path) as f:
        return yaml.safe_load(f)


def load_brand_voice() -> str:
    voice_path = Path(__file__).parent.parent / "config" / "brand_voice.md"
    with open(voice_path) as f:
        return f.read()


def parse_content_file(filepath: Path) -> tuple[dict, str]:
    """Parse a markdown file with YAML frontmatter. Returns (frontmatter, body)."""
    text = filepath.read_text()
    if text.startswith("---"):
        parts = text.split("---", 2)
        frontmatter = yaml.safe_load(parts[1]) or {}
        body = parts[2].strip()
    else:
        frontmatter = {}
        body = text.strip()
    return frontmatter, body


def generate_linkedin_post(bullets: str, brand_voice: str, config: dict) -> str:
    client = anthropic.Anthropic(api_key=config["anthropic"]["api_key"])

    message = client.messages.create(
        model=config["anthropic"]["model"],
        max_tokens=1024,
        system=f"""You are a content writer for A3DI, a data consultancy for humanitarian
and development organisations. Follow these brand voice guidelines exactly:

{brand_voice}

Generate a LinkedIn post from the bullet points provided. Output ONLY the post text,
no frontmatter, no meta-commentary. Keep it to 150-300 words.""",
        messages=[
            {"role": "user", "content": f"Turn these bullet points into a LinkedIn post:\n\n{bullets}"}
        ],
    )
    return message.content[0].text


def generate_carousel(bullets: str, brand_voice: str, config: dict) -> str:
    client = anthropic.Anthropic(api_key=config["anthropic"]["api_key"])

    message = client.messages.create(
        model=config["anthropic"]["model"],
        max_tokens=2048,
        system=f"""You are a content writer for A3DI. Follow these brand voice guidelines:

{brand_voice}

Generate a LinkedIn carousel outline (5-7 slides) from the bullet points provided.
Format as:

## Slide 1: [Title]
[Content for slide — 1-3 sentences max]

## Slide 2: [Title]
...

Keep each slide concise. The first slide is the hook/title, the last is a CTA.""",
        messages=[
            {"role": "user", "content": f"Create a carousel outline from these notes:\n\n{bullets}"}
        ],
    )
    return message.content[0].text


def generate_case_study(bullets: str, brand_voice: str, config: dict) -> str:
    client = anthropic.Anthropic(api_key=config["anthropic"]["api_key"])

    message = client.messages.create(
        model=config["anthropic"]["model"],
        max_tokens=2048,
        system=f"""You are a content writer for A3DI. Follow these brand voice guidelines:

{brand_voice}

Generate a case study from the notes provided. Follow the structure:
## Challenge (2-3 sentences)
## Approach (3-5 sentences)
## Result (2-3 sentences)
## Key Takeaway (1 sentence)

Keep it factual and specific. Use [PLACEHOLDER] for any details you're unsure about.
Do not fabricate project specifics.""",
        messages=[
            {"role": "user", "content": f"Write a case study from these project notes:\n\n{bullets}"}
        ],
    )
    return message.content[0].text


GENERATORS = {
    "post": generate_linkedin_post,
    "carousel": generate_carousel,
    "case-study": generate_case_study,
}


def main():
    parser = argparse.ArgumentParser(description="Generate marketing content from bullet points")
    parser.add_argument("file", type=Path, help="Path to the markdown file with bullet points")
    parser.add_argument("--type", choices=GENERATORS.keys(), default="post", help="Content type to generate")
    parser.add_argument("--dry-run", action="store_true", help="Print output without writing to file")
    args = parser.parse_args()

    if not args.file.exists():
        print(f"ERROR: File not found: {args.file}")
        sys.exit(1)

    config = load_config()
    brand_voice = load_brand_voice()
    frontmatter, bullets = parse_content_file(args.file)

    if not bullets or bullets.isspace():
        print("ERROR: No bullet points found in the file body. Add your notes below the frontmatter.")
        sys.exit(1)

    print(f"Generating {args.type} from: {args.file}")
    generated = GENERATORS[args.type](bullets, brand_voice, config)

    if args.dry_run:
        print("\n--- Generated Content ---\n")
        print(generated)
        return

    # Write back: preserve frontmatter, replace body
    frontmatter["status"] = "draft"
    output = f"---\n{yaml.dump(frontmatter, default_flow_style=False)}---\n\n{generated}\n"
    args.file.write_text(output)
    print(f"Content written to: {args.file}")


if __name__ == "__main__":
    main()
