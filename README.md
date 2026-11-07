# Distro Reader for Hermes Agent

Read independent news and content from [Distro](https://distro.media) publications directly in Hermes Agent. The plugin connects Hermes to Distro's public Reader MCP server and bundles workflow guidance for discovery, article and book reading, archive research, news digests, visual reader rendering, premium access, and publisher tips.

## What it adds

- **Eight MCP tools** for feeds, search, articles, books, podcasts/video series, Distro's visual reader, payment information, and tips.
- **`distro-reader` skill** for reliable source routing, full-text reading, visual rendering, books, premium access, and payment safety.
- **`distro-news-digest` skill** for date-filtered daily/weekly briefings with deduplication and canonical links.
- **`distro-archive-research` skill** for evidence-linked archive analysis, counterarguments, and carefully framed trading hypotheses.
- **No account or API key required** for public discovery and free stories.

Examples:

- “What are the latest stories from DeAI News?”
- “Search Distro for reporting about decentralized AI.”
- “Read and summarize this Distro story.”
- “Open this story in the visual reader.”
- “Give me some trading ideas based on the DeAI News archive.”
- “Build a briefing from this week's Distro headlines.”

## Install

After the catalog entry is merged:

```bash
hermes plugins install distro-reader
hermes plugins enable distro-reader
```

To test the repository directly:

```bash
hermes plugins install https://github.com/Distro-Media/hermes-plugin-distro-reader
hermes plugins enable distro-reader
```

Start a new Hermes session, or reload MCP connections if your client exposes that action.

## Package layout

This is a portable [Agent Plugins v1](https://agent-plugins.org) package:

```text
plugin.json
mcp.json
skills/
├── distro-archive-research/
│   └── SKILL.md
├── distro-reader/
│   ├── SKILL.md
│   └── references/
│       ├── premium-access.md
│       └── tool-workflows.md
└── distro-news-digest/
    └── SKILL.md
```

`mcp.json` registers the Streamable HTTP endpoint:

```text
https://reader.distro.media/mcp/reader/stream
```

The package does not modify the user's `config.yaml` and contains no credentials.

## Tools

| Tool | Purpose |
|---|---|
| `distro_feed_latest` | Browse recent Distro stories, optionally by publication |
| `distro_search` | Search stories, topics, people, and publications |
| `distro_story_read` | Read a free story or retrieve premium-access instructions |
| `distro_media_series` | Discover podcast/video series and episodes |
| `distro_story_render_hud` | Render a story in Distro's visual reader |
| `distro_book_render_hud` | Render a book, table of contents, and available chapters |
| `distro_payment_info` | Inspect price and supported payment rails without paying |
| `distro_tip` | Retrieve tip options or initiate a user-approved tip |

## Safety and privacy

- The plugin makes network requests only to Distro's public Reader MCP endpoint and URLs returned by that endpoint when the user requests reading or payment-related actions.
- The package declares the MCP server **untrusted**. Hermes can run tools annotated read-only without a prompt, while write-capable tools such as `distro_tip` go through Hermes's approval gate.
- Public discovery and free-story reading need no credentials.
- Premium stories use Distro's x402 flow. The bundled skill requires explicit approval of the exact amount, asset, network, and resource before payment.
- No telemetry, background process, shell command, credential-file access, or self-updater is included.
- Premium content remains subject to the license returned by Distro; the skill forbids redistribution of paid bodies.

## Validate

```bash
hermes plugins validate . --install-deps
python3 scripts/smoke_test.py
```

The smoke test uses only Python's standard library. It verifies the MCP handshake and checks that the expected tool contract is present; it does not read premium content or perform a payment.

## License

MIT © 2026 Distro Media
