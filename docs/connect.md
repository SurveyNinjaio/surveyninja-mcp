<sub><a href="../README.md">SurveyNinja MCP</a> › Connecting</sub>

# Connecting to the SurveyNinja MCP server

| | |
|---|---|
| Server | `https://mcp.surveyninja.io/mcp/v1` |
| Transport | Streamable HTTP |
| Sign-in | Allow access (OAuth), or an API key in the `Authorization: Bearer <key>` header |
| Plans | Every plan, Free included |

## Two ways to connect

| | Allow access | API key |
|---|---|---|
| What you need | Only the server address | A key from **Settings → API / MCP** |
| Workspaces the assistant sees | The one workspace you choose | Every workspace where you are the owner or a member |
| How long access lasts | The assistant renews it by itself | Until you delete the key |
| How to turn it off | Remove the connector in the assistant | Delete the key, and access stops at once |

Use **Allow access** when your assistant supports it. Use a key for clients that cannot sign in, or when one
assistant should work across several workspaces.

### Getting an API key

1. Sign in to SurveyNinja.
2. Open **Settings → [API / MCP](https://app.surveyninja.io/account/api)**.
3. Click **Create API key** and copy it right away: the key is shown only once.

The key acts on your behalf with your permissions. Delete it on the same page to cut access off.

## Your assistant

### Claude

1. In Claude on the web or in the desktop app, open **Settings → Connectors** and click **Add custom connector**.
2. Enter a name, for example SurveyNinja, and the server address.
3. Click **Add**, then **Connect**, and allow access in SurveyNinja.

On Claude Team and Enterprise an organization owner adds the connector first, then each member connects it.

### ChatGPT

1. Turn on developer mode in the ChatGPT settings. It is available on some ChatGPT plans.
2. Create a connector with the server address and OAuth authentication.
3. Allow access in SurveyNinja.

### Claude Code

With the skills, as a plugin:

```text
/plugin marketplace add surveyninjaio/surveyninja-mcp
/plugin install surveyninja@surveyninja
```

Only the server:

```bash
claude mcp add --transport http surveyninja https://mcp.surveyninja.io/mcp/v1
```

Then type `/mcp` in Claude Code, select the SurveyNinja server and sign in.

### Cursor

Add [`clients/cursor.json`](../clients/cursor.json) to `~/.cursor/mcp.json` for all projects, or to
`.cursor/mcp.json` for one project. Open the MCP section in the Cursor settings and sign in to the `surveyninja`
server.

### VS Code

Put [`clients/vscode.json`](../clients/vscode.json) into your project as `.vscode/mcp.json`. Start the server from
the file and sign in when VS Code asks. The server works in GitHub Copilot Chat in agent mode.

### Gemini CLI

With the skills, as an extension:

```bash
gemini extensions install https://github.com/surveyninjaio/surveyninja-mcp
```

Only the server: add [`clients/gemini.json`](../clients/gemini.json) to `~/.gemini/settings.json`. If Gemini CLI
does not offer to sign in by itself, run `/mcp auth surveyninja`.

### Codex

Add [`clients/codex.toml`](../clients/codex.toml) to `~/.codex/config.toml`, then sign in:

```bash
codex mcp login surveyninja
```

SurveyNinja opens in the browser; choose the workspace and click **Allow access**. In the Codex app, add the server
under **Settings → MCP servers** as Streamable HTTP and select **Authenticate**.

### Other clients

Any client that connects to remote MCP servers over Streamable HTTP can use the same address. With MCP sign-in
(OAuth) it opens SurveyNinja for you to allow access. Without it, send the header
`Authorization: Bearer <key>`, as in [`clients/api-key.json`](../clients/api-key.json).

## First request

“Show my surveys and how many responses came in this week.” The assistant lists your surveys with their response
counts. More ideas in [prompts.md](prompts.md).

## Troubleshooting

| What you see | What to do |
|---|---|
| The server answers `401` | The assistant is not signed in, or the key is missing or deleted. Connect again, or check the header: `Authorization: Bearer <key>`, with a space |
| The assistant does not see a survey | With Allow access it sees only the workspace you chose. Connect again and choose the other one, or use a key |
| A refusal about permissions | Your role in the workspace does not allow the action. The workspace owner can change it |
| A refusal that mentions the plan | The feature is not in the workspace plan. AI reports, for example, need Premium or Enterprise |
| The assistant hit the request limit | The limit is 180 requests per minute per user. Wait a minute |
| A link to an exported file does not open | Links to exported files work for one hour. Ask for a new export |
