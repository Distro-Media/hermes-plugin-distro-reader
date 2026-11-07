#!/usr/bin/env python3
"""Smoke-test the public Distro Reader MCP contract with stdlib only."""

from __future__ import annotations

import json
import sys
import urllib.request

ENDPOINT = "https://reader.distro.media/mcp/reader/stream"
EXPECTED_TOOLS = {
    "distro_feed_latest",
    "distro_story_read",
    "distro_search",
    "distro_media_series",
    "distro_story_render_hud",
    "distro_book_render_hud",
    "distro_payment_info",
    "distro_tip",
}


def rpc(method: str, params: dict | None = None) -> dict:
    payload = json.dumps(
        {"jsonrpc": "2.0", "id": 1, "method": method, "params": params or {}}
    ).encode()
    request = urllib.request.Request(
        ENDPOINT,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "MCP-Protocol-Version": "2025-06-18",
            "User-Agent": "hermes-plugin-distro-reader-smoke-test/1.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def main() -> int:
    initialized = rpc(
        "initialize",
        {
            "protocolVersion": "2025-06-18",
            "capabilities": {},
            "clientInfo": {"name": "distro-reader-smoke-test", "version": "1.0.0"},
        },
    )
    server = initialized.get("result", {}).get("serverInfo", {})
    if server.get("name") != "distro-reader":
        raise AssertionError(f"Unexpected server info: {server!r}")

    listed = rpc("tools/list")
    tools = {tool["name"] for tool in listed.get("result", {}).get("tools", [])}
    missing = EXPECTED_TOOLS - tools
    if missing:
        raise AssertionError(f"Missing tools: {sorted(missing)}")

    print(f"OK: {server['name']} {server.get('version', '')}; {len(tools)} tools")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise
