.PHONY: draft generate schedule analytics weekly-review leads help

help: ## Show available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

draft: ## Create a new draft (usage: make draft slug=my-post-title)
	@if [ -z "$(slug)" ]; then echo "Usage: make draft slug=my-post-title"; exit 1; fi
	@DATE=$$(date +%Y-%m-%d); \
	cp content/posts/templates/linkedin-post.md "content/posts/drafts/$${DATE}-$(slug).md"; \
	sed -i "s/YYYY-MM-DD/$${DATE}/" "content/posts/drafts/$${DATE}-$(slug).md"; \
	echo "Created: content/posts/drafts/$${DATE}-$(slug).md"

generate: ## AI-generate content from bullet points (usage: make generate file=path/to/draft.md type=post)
	python scripts/content_gen.py $(file) --type $(or $(type),post)

generate-dry: ## Preview AI-generated content without writing (usage: make generate-dry file=path/to/draft.md)
	python scripts/content_gen.py $(file) --type $(or $(type),post) --dry-run

weekly-review: ## Run weekly KPI and content calendar review
	python pipelines/weekly_review.py

weekly-review-save: ## Save weekly review to file
	@DATE=$$(date +%Y-%m-%d); \
	python pipelines/weekly_review.py --output "data/analytics/weekly_$${DATE}.md"; \

leads: ## Show all leads
	python scripts/lead_tracker.py list

leads-active: ## Show active leads only
	python scripts/lead_tracker.py list --status active

lead-add: ## Add a lead (usage: make lead-add name="Jane" org="UNICEF" source="linkedin")
	python scripts/lead_tracker.py add --name "$(name)" --org "$(org)" --source "$(source)" --notes "$(notes)"

case-study: ## Generate case study from project materials (usage: make case-study slug=my-project source=path/to/sow.pdf)
	python scripts/generate_case_study.py --slug "$(slug)" $(if $(source),--source "$(source)") $(if $(repo),--repo "$(repo)") $(if $(notes),--notes "$(notes)")

case-study-dry: ## Preview case study without writing (usage: make case-study-dry slug=my-project source=path/to/sow.pdf)
	python scripts/generate_case_study.py --slug "$(slug)" $(if $(source),--source "$(source)") $(if $(repo),--repo "$(repo)") $(if $(notes),--notes "$(notes)") --dry-run

calendar: ## Show content calendar
	@cat config/content_calendar.yaml
