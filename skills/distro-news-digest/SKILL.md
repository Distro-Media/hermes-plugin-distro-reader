---
name: distro-news-digest
description: Use when creating a daily, weekly, topic, or publication briefing from Distro headlines, with date filtering, deduplication, and links.
---

# Distro News Digest

Build concise briefings from Distro without reading or paying for content unnecessarily.

## Workflow

1. Resolve named publications or topics with `distro_search`.
2. Fetch enough candidates with `distro_feed_latest` to cover the requested window.
3. Filter by `publishedAt` in the user's timezone.
4. Deduplicate by story ID, then canonical URL.
5. Rank by relevance to the user's requested publications/topics; do not invent importance from engagement metrics the tool did not return.
6. Use titles, previews, author/publication metadata, and canonical links for a headline digest.
7. Read selected free stories with `distro_story_read` only when the user asks for summaries or analysis that previews cannot support.
8. For premium stories, include the title, preview, publication, price when available, and link. Do not initiate payment during digest creation.

## Default format

For each item include:

- **Title** — linked to the canonical Distro URL
- publication and author when present
- publication time in the user's timezone
- one-sentence preview-derived takeaway
- `Premium — <price>` when applicable

End with a short “What stands out” section only when there is enough evidence across multiple items. Distinguish preview-based observations from conclusions based on full story text.

## Date rules

- “Today”: local midnight through now.
- “This week”: Monday 00:00 through now unless the user specifies a different week.
- “Last 24 hours”: rolling 24-hour interval.
- Undated stories: list separately; do not silently include in a dated range.
- State the interval used when the user's wording is relative.

## Source discipline

Distro is authoritative for Distro publication metadata and story links. If Distro is unavailable, label any web-based fallback and do not imply it is complete.
