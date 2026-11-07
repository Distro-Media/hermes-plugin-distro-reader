# Premium access and tipping

## Before a purchase

1. Call `distro_payment_info` or inspect the paywall returned by `distro_story_read`.
2. For a book chapter, compare the chapter price with the whole-book offer.
3. Tell the user the exact amount, token/currency, network, resource, and access scope.
4. Ask for explicit approval. Approval for one resource or amount does not cover another.

## x402 settlement

Follow the canonical resource and payment instructions returned by Distro. The purchase succeeds only when settlement evidence reports `settled` and includes a `PAYMENT-RESPONSE` receipt. Save the receipt and access grant in protected client state when the host supports it; never paste them into chat.

A generic HTTP 200 is not payment evidence. If settlement reports `skipped_already_owned`, tell the user the wallet already owned the resource and **no new charge occurred**.

## Reusing access

Use an unexpired `X-Distro-Access-Token` for the same resource instead of paying again. A whole-book token covers all chapters in that book. When a token expires, ownership remains permanent; use the advertised wallet-recovery challenge with the original wallet.

Never put an access token, challenge, signature, nonce, or payment payload in a URL. The only exception is Distro's short-lived, single-use `webHandoff.url`, which is specifically minted for opening the purchased article on the Distro website.

## Licensing

Premium bodies are licensed to the purchasing wallet for personal use. The agent may read, transform, or summarize them for that user, but must not republish, redistribute, cache for other users, or re-serve the complete body.

## Tips

A tip is separate from content access and grants no token. Only begin when the user asks to tip or support the publisher:

1. Call `distro_tip` without an amount to retrieve suggested options.
2. Obtain explicit approval for the exact amount.
3. Call `distro_tip` with that amount and complete the returned payment handoff.
4. Confirm only from a decoded settlement receipt. Never retry automatically after an ambiguous outcome.
