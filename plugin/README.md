# SurveyNinja plugin for Claude Code

Build surveys, read responses and make reports in [SurveyNinja](https://surveyninja.io) from Claude Code. The plugin
adds two things: the SurveyNinja MCP server and 25 ready-made skills, from a survey brief to a report you can send.

## Install

```text
/plugin marketplace add surveyninjaio/surveyninja-mcp
/plugin install surveyninja@surveyninja
```

Then type `/mcp`, select the SurveyNinja server and sign in: SurveyNinja opens in the browser, you choose a
workspace and click **Allow access**. The plugin needs no key. A SurveyNinja account is required; the server works
on every plan, Free included.

## What is inside

- **The MCP server** `https://mcp.surveyninja.io/mcp/v1` (Streamable HTTP, OAuth): more than 160 tools for surveys,
  logic, design, publishing, responses, reports, exports and sharing. Every tool is marked as read-only or as
  changing data, and the ones that delete or overwrite data are marked destructive, so Claude asks before it calls
  them.
- **The skills** in [`skills/`](skills/): step-by-step instructions for jobs such as writing a survey from a brief,
  checking it before launch, reading open answers, comparing A/B variants or setting up notifications. Each skill
  has a "What not to do" section.

The full list of skills and tools, configs for other assistants and the changelog are in the
[repository](https://github.com/surveyninjaio/surveyninja-mcp).

## Privacy

The plugin and the skills run nothing on your computer: the skills are text instructions, and the plugin only adds
the server address to Claude Code. The one connection is to `https://mcp.surveyninja.io/mcp/v1` over HTTPS, and it
carries what your assistant asks for: your surveys, responses and reports in your SurveyNinja account. SurveyNinja
stores that data on a server in the EU behind Cloudflare and handles it under the
[privacy policy](https://surveyninja.io/privacy).

## License

MIT, see [LICENSE](LICENSE). Questions: team@surveyninja.io.
