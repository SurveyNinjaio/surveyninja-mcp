# Security

## Reporting a problem

Found a vulnerability in the SurveyNinja MCP server or in the skills of this repository? Report it privately:
use **Report a vulnerability** on the [Security tab](https://github.com/surveyninjaio/surveyninja-mcp/security) of
this repository, or write to team@surveyninja.io. Please keep the details out of public issues until the problem is
fixed.

## How access works

An assistant connects to the server in one of two ways:

- **Allow access** (OAuth): you sign in to SurveyNinja and choose one workspace. Access works in that workspace
  only, the assistant renews it by itself, and it ends when you leave the workspace or remove the connector.
- **API key** from **Settings → API / MCP**: the key acts with its owner's permissions in every workspace where they are
  the owner or a member. Deleting the key cuts access off at once.

Either way the server checks the same permissions as the app: the member's role and the workspace plan. Tools
that cannot be undone carry the `destructiveHint` annotation.

## Secrets in this repository

There are none, and there should be none. Configs in `clients/` use `YOUR_API_KEY` as a placeholder or no key at
all. If you see something that looks like a real key or personal data here, report it as above.
