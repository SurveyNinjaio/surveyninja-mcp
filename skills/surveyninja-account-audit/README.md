<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Keep the account tidy</sub>

# Workspace audit

**Shows in one report where your workspace is losing responses, storage and attention**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-account-audit` | 1.0.2 | 13 | [ZIP](https://surveyninja.io/skills/account-audit.zip) | [surveyninja.io](https://surveyninja.io/skills/account-audit) |

## What it does

1. **Finds surveys collecting into silence.** Published, fresh responses, but no email notification, no integration and no working webhook. Data piles up and nobody knows.
2. **Checks that notifications really work.** An address that never confirmed the letter, a webhook switched off after failed deliveries, an integration the plan no longer allows. Each looks set up and delivers nothing.
3. **Separates ghosts from drafts.** A published survey with no responses for months and a draft abandoned after the first question are different stories. Drafts also count against the survey limit.
4. **Counts storage, limits and access.** How much space is used and by what, which files are over the quota, which limits are close, and who still has an unaccepted invitation.

## What the workspace report looks like

**Workspace health, 34 surveys**

| Surveys | Drafts | Storage | Findings |
|:-:|:-:|:-:|:-:|
| **34** | **11** | **82%** | **6** |
| <sub>12 published</sub> | <sub>untouched for six months</sub> | <sub>of the plan's disk space</sub> |  |

| | | |
|---|---|---|
| **"Delivery feedback" collects into silence** | 47 responses this month, no notifications or integrations | losing data |
| **Webhook to the order system is off** | switched off automatically after failed deliveries | losing data |
| **Two published surveys with no responses since April** | the link is no longer shared, or it is broken | check |
| **11 drafts count against the limit** | last edited in April or earlier | tidy up |
| **One invitation is still not accepted** | sent in July | resend |

> **Start with the first two items**  
> They are the only findings losing data right now: 47 responses nobody has read, and a webhook that stopped sending. The rest can wait for a calm afternoon.

<sub>The findings above are an example. The real report is built from your workspace, and the audit changes nothing.</sub>

## How to ask

> Audit my workspace: what is abandoned and where is storage running out?

> Are there surveys collecting responses that nobody receives?

> Run a workspace audit and tell me where to start cleaning up

## What not to do

- Delete and change nothing during the audit
- Do not call a survey abandoned
- Do not show respondents' personal data
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_folder_list` | Folder list | read |
| `get_quiz_email_settings` | Quiz email settings | read |
| `get_quiz_integrations` | Quiz integration state | read |
| `get_quiz_list` | Quiz list | read |
| `get_quiz_summary` | Quiz summary | read |
| `get_quiz_webhooks` | Quiz webhooks | read |
| `get_workspace_details` | Workspace details | read |
| `get_workspace_hidden_files` | Files hidden over quota | read |
| `get_workspace_list` | Workspace list | read |
| `get_workspace_member_access` | Member access | read |
| `get_workspace_members` | Workspace members | read |
| `get_workspace_storage_usage` | Storage usage | read |
| `get_workspace_tariff` | Workspace plan | read |

## Questions

<details>
<summary><b>What does the skill check?</b></summary>

Surveys and folders, plan limits, storage and hidden files, members and invitations, and for surveys with fresh responses, where those responses go: email, integrations and webhooks.

</details>

<details>
<summary><b>What is the most useful thing it finds?</b></summary>

A published survey with fresh responses and no notification, integration or working webhook. Responses pile up and nobody knows about them.

</details>

<details>
<summary><b>How is a ghost survey different from a draft?</b></summary>

A ghost is published but has had no responses for a long time, so the link is no longer shared or is broken somewhere. A draft was created and abandoned, and it still counts against the survey limit.

</details>

<details>
<summary><b>Will the skill delete or change anything?</b></summary>

No. Every tool it uses only reads. What to tidy up is your decision, and a cleanup is a separate step with its own confirmation.

</details>

<details>
<summary><b>Will it list a seasonal survey as abandoned?</b></summary>

No. If a survey looks seasonal, the assistant asks instead of calling it abandoned.

</details>

<details>
<summary><b>What do I need to use it?</b></summary>

A SurveyNinja account and an assistant that supports MCP and loads skills from a folder, such as Claude Code, Codex, Cursor or Gemini CLI. The MCP server works on every plan, the free one included. You connect with "Allow access" in the assistant or with your own API key.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
