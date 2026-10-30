# Changelog

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions of each skill and what
changed in them are in [`skills/CHANGELOG.md`](skills/CHANGELOG.md).

## [1.1.0] - 2026-10-30

### Changed

- The Claude Code plugin is now the `plugin/` folder: the server, a copy of the skills, its README and the license.
  Installing it no longer copies the repository's scripts, tests and workflows. The install commands stay the same.
- Codex signs in with Allow access (`codex mcp login surveyninja`) instead of an API key from the environment.
- Three skills say what to do on an Allow access connection, where creating or changing a webhook and confirming a
  new email recipient are not offered: `webhook-setup`, `answer-notifications`, `integration-triage`.
- The tool reference lists 173 tools and marks the 7 that work only with an API key.

### Added

- `scripts/openai_package.py` builds the ChatGPT plugin package.

## [1.0.0] - 2026-10-24

### Added

- Connecting to the MCP server `https://mcp.surveyninja.io/mcp/v1` with Allow access (OAuth) or an API key, with
  steps for Claude, ChatGPT, Claude Code, Cursor, VS Code, Gemini CLI and Codex, and ready-made configs.
- The SurveyNinja skills, the same as in the catalog at [surveyninja.io/skills](https://surveyninja.io/skills).
- A Claude Code plugin and a Gemini CLI extension: the server and the skills in one install.
- The tool reference and starter phrases.
- Metadata for the official MCP Registry (`server.json`).
