<sub><a href="../README.md">SurveyNinja MCP</a> › Configs</sub>

# Ready-made configs

Copy the file you need, or its contents, into your client's settings. With these configs the client opens
SurveyNinja for you to sign in and click **Allow access**: no key goes into the file.

| File | Where it goes | Sign-in |
|---|---|---|
| [`cursor.json`](cursor.json) | `~/.cursor/mcp.json`, or `.cursor/mcp.json` in a project | Allow access |
| [`vscode.json`](vscode.json) | `.vscode/mcp.json` in a project | Allow access |
| [`gemini.json`](gemini.json) | `~/.gemini/settings.json` | Allow access |
| [`codex.toml`](codex.toml) | `~/.codex/config.toml` | Allow access, after `codex mcp login surveyninja` |
| [`api-key.json`](api-key.json) | any client that takes `mcpServers` with headers | API key: replace `YOUR_API_KEY` |

Claude Code takes one command, or the plugin with the skills:

```bash
claude mcp add --transport http surveyninja https://mcp.surveyninja.io/mcp/v1
```

Claude and ChatGPT connect in their settings, no file needed. Every step is in [`../docs/connect.md`](../docs/connect.md).
