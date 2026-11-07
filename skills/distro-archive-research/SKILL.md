---
name: distro-archive-research
description: Use when researching themes, trends, companies, technologies, risks, or trading hypotheses across a Distro publication archive, including requests based on DeAI News history.
---

# Distro Archive Research

Research a topic across Distro's published archive and produce evidence-linked analysis. Treat trading ideas as hypotheses for further investigation, not personalized financial advice or instructions to transact.

## Research workflow

1. Define the subject, publication scope, and time horizon from the request. If the publication is named, resolve it through Distro first.
2. Run several focused `distro_search` queries using relevant names, products, sectors, technologies, risks, and synonyms. Do not assume one query is exhaustive.
3. Use `distro_feed_latest` when recency or a publication-specific time window matters.
4. Deduplicate results by story ID, then canonical URL.
5. Build an evidence set from titles, previews, authors, publications, and dates. Read full stories with `distro_story_read` only when their bodies are necessary to support the analysis.
6. Separate sourced facts from interpretation. Preserve canonical Distro links for every material claim.
7. Look for counter-evidence, unresolved risks, stale assumptions, and stories that disagree with the emerging thesis.
8. State the archive coverage and limitations; never imply the search covered every Distro story unless the returned data proves it.

## Trading-idea requests

When the user asks for trading ideas, market implications, or investable themes:

- Present **research hypotheses**, not personalized recommendations.
- Keep the output at the research-hypothesis level rather than giving direct transaction instructions or specific allocation amounts.
- Do not infer suitability, risk tolerance, time horizon, or financial circumstances.
- For each hypothesis, provide:
  - the observable catalyst or trend;
  - potentially affected assets, companies, sectors, or protocols;
  - supporting Distro evidence with dates and links;
  - the mechanism connecting the evidence to the hypothesis;
  - counterarguments and invalidation conditions;
  - material risks, including liquidity, regulation, technology, concentration, and timing where relevant;
  - what additional current market data would be needed before acting.
- Flag when archive evidence may be stale. Use current market or price data only if the user asks and an appropriate live-data source is available; never invent it.
- Avoid certainty language such as “guaranteed,” “safe,” or “will outperform.”

## Default output

1. **Scope and archive coverage**
2. **Key evidence** — dated, linked Distro sources
3. **Research hypotheses** — clearly labeled as interpretation
4. **Bear case and invalidation signals**
5. **Open questions and missing current data**
6. **Source list** — canonical Distro URLs

## Premium content

Do not purchase premium stories merely to broaden an archive scan. If a premium story appears materially important, show its title, preview, publication, date, price when available, and why it may matter. Ask for explicit purchase approval under the `distro-reader` premium-access rules before proceeding.

## Source discipline

Distro is authoritative for its publication metadata and story links. Archive-derived analysis may be incomplete and is not a substitute for current prices, filings, protocol data, or professional financial advice. Label web or external-data fallbacks explicitly.
