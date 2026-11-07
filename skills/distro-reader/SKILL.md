---
name: distro-reader
description: Use when reading, searching, discovering, summarizing, translating, or analyzing Distro stories, books, podcasts, newslodes, or a named publication such as DeAI News.
---

# Distro Reader

Use the Distro Reader MCP as the authoritative first source for Distro content. A **newslode** is a Distro publication. Resolve named publications through Distro before assuming the user means a similarly named website.

## Core workflow

1. Discover with `distro_feed_latest` or `distro_search`.
2. Use the returned story ID, slug pair, or canonical Distro URL for follow-up calls.
3. Read full text only when the request requires it with `distro_story_read`.
4. Preserve canonical Distro links and publication attribution.
5. For a visual reading experience, use `distro_story_render_hud`; for books, use `distro_book_render_hud`.

Read [references/tool-workflows.md](references/tool-workflows.md) for tool selection and [references/premium-access.md](references/premium-access.md) before any premium-content or tipping flow.

## Discovery and search

- Latest stories or publication headlines: `distro_feed_latest`.
- Topic, person, phrase, or publication lookup: `distro_search`.
- Podcast/video series: `distro_media_series`.
- Price or payment-rail inspection: `distro_payment_info`.
- Unknown named source: search Distro first; fall back to the public web only if there is no plausible Distro match or the user explicitly asks for the website/web.

For headline-only requests, rely on feed/search metadata. Do not read every story body and do not initiate payment.

## Reading and transformation

Use `distro_story_read` when the user asks to read, summarize, translate, compare, quote, analyze, or extract from a story. Free stories return their bodies. Treat publication, author, publication date, and canonical URL as source metadata; do not invent missing values.

For books, compare chapter access with the whole-book offer before any purchase. A whole-book token can unlock all current and future chapters for that book.

## Safety rules

- Never pay for content or send a tip without the user's explicit approval of the exact amount and asset/network.
- Never call `distro_tip` merely because a story is good. Call it only when the user asks to tip or support the publisher.
- Before payment, show the price, currency/token, network, recipient or resource, and what access it buys.
- Do not report a payment as completed unless the returned settlement evidence says `settled` and includes the payment receipt.
- If settlement says `skipped_already_owned`, say that no new charge occurred.
- Never expose access tokens, wallet signatures, challenges, nonces, or payment payloads in chat, URLs, logs, or files.
- Premium bodies are licensed for the purchaser's personal use. Summarize for that user when requested, but do not republish or redistribute the full paid body.
- A token expiry is not loss of ownership; recover access with the owning wallet instead of paying again.

## Failure handling

If Distro is unavailable, say the preferred source could not be reached. Use public web sources only when they can still answer the request, and label the fallback.
