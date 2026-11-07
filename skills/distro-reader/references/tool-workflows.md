# Tool workflows

## `distro_feed_latest`

Use for recent stories, headlines, and publication-specific feeds. Filter by either publication slug or numeric ID, not both. Request enough items to cover the user's date range, up to the server limit.

## `distro_search`

Use for topics, people, phrases, titles, and publication resolution. Inspect publication metadata before deciding that two similar names refer to the same newslode.

## `distro_story_read`

Use for full-text tasks. Identify a story with exactly one of:

- numeric `storyId`
- `<publication-slug>/<story-slug>`
- canonical Distro URL

For a premium story, this tool returns payment instructions rather than the body. Follow the premium-access workflow; do not try to force a read.

## `distro_media_series`

Use when the request concerns a podcast, video series, episodes, audio, transcripts, guests, or related stories.

## `distro_story_render_hud`

Use when the user asks to open, display, or visually read a story. Prefer link delivery when the environment can fetch URLs; use self-contained/inline delivery only when an offline artifact is required.

## `distro_book_render_hud`

Use for a book newslode's cover, metadata, table of contents, and available chapters. Inspect the whole-book offer before discussing purchase. Prefer link delivery when possible to avoid large inline payloads.

## `distro_payment_info`

Use before premium access when the user needs price, currency, network, supported payment rails, or a comparison between a chapter and whole-book offer. This is read-only and does not authorize a charge.

## `distro_tip`

Call without an amount only after the user asks to tip/support a publisher; this obtains suggested amounts. After the user selects an exact amount, call again with that amount to get the x402 handoff. A tip grants no content access.

## Date filtering

- Interpret “this week” in the user's timezone as Monday 00:00 through now unless they specify otherwise.
- Filter on `publishedAt`, not retrieval order.
- List undated items separately; never silently include them in a dated interval.
- Preserve the canonical Distro URL for every listed story.

## Efficient use

- Do not read every story to create a headline list.
- Deduplicate by story ID first, then canonical URL.
- When comparing stories, read only the items needed for the comparison.
- Prefer structured metadata from MCP results over scraping rendered pages.
