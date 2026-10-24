<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Keep the account tidy</sub>

# Members and access

**Finds out why a colleague cannot see the surveys and grants exactly the rights they need**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-workspace-access` | 1.0.2 | 13 | [ZIP](https://surveyninja.io/skills/workspace-access.zip) | [surveyninja.io](https://surveyninja.io/skills/workspace-access) |

## What it does

1. **Shows the current picture first.** Who is in the account, with which role, and what each person can really do. "Give Peter access" without that picture usually leaves Peter with too much.
2. **Knows why "they see nothing".** An invitation never accepted, an email never confirmed, a role without workspaces, a workspace created after the invitation. Each one leaves a member looking at an empty list.
3. **Asks about the job, not the role.** Viewing results, building surveys and setting up integrations need different rights. Full access is only for people who run the account.
4. **Never revokes on its own.** Removing a member can only be undone with a new invitation and new workspace access, so it happens only when you ask.

## What the access review looks like

**Account members, 6 people**

| Members | Not accepted | Missing a workspace | Too much access |
|:-:|:-:|:-:|:-:|
| **6** | **1** | **1** | **1** |
|  | <sub>listed but cannot work</sub> | <sub>has a role, misses surveys</sub> |  |

| | | |
|---|---|---|
| **Anna** | administrator, all workspaces | working |
| **Peter** | invited on 4 September, never accepted | no access |
| **Maria** | "Analyst" role, the new "2026" workspace is not open to her | empty workspace |
| **James** | full access, only needs to view results | too much access |
| **Olga** | views results in 2 workspaces | working |

> **Both "I added them and they see nothing" cases come from here**  
> Peter has an unaccepted invitation that needs resending. Maria has a role, but the "2026" workspace was created after she joined and is open only to the owner and its creator.

<sub>The members above are an example. The real review is built from your account.</sub>

## How to ask

> Invite a colleague who can only see the results

> Why can this member not see the surveys?

> Show me who has which rights in the account

## What not to do

- Do not remove a member without an explicit request
- Do not grant full access "to be safe"
- Do not edit a shared role to fix one person
- Do not delete a role in use
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `delete_workspace_role` | Delete member role | destructive |
| `get_folder_list` | Folder list | read |
| `get_workspace_list` | Workspace list | read |
| `get_workspace_member_access` | Member access | read |
| `get_workspace_members` | Workspace members | read |
| `get_workspace_roles` | Member roles | read |
| `invite_workspace_member` | Invite member | write |
| `manage_folder_access` | Folder access | destructive |
| `remove_workspace_member` | Remove member | destructive |
| `resend_workspace_member_invite` | Resend member invite | write |
| `save_workspace_role` | Member role | write |
| `set_workspace_member_folders` | Folders available to a member | write |
| `set_workspace_member_role` | Change member role | write |

## Questions

<details>
<summary><b>Why can a member not see the surveys?</b></summary>

Most often the invitation was not accepted, the email was not confirmed, or the member has a role but no workspaces. A workspace created later is open only to the owner and the person who created it, so others need it granted.

</details>

<details>
<summary><b>How do I give access to results only?</b></summary>

With a role that allows viewing results and forbids editing, plus the workspaces that person needs. The skill asks what your colleague has to do and picks the rights for that.

</details>

<details>
<summary><b>Can a member see only their own surveys?</b></summary>

Yes. Each permission can be allowed, forbidden, or set to Own only, which limits it to the surveys the member created.

</details>

<details>
<summary><b>Why can a member not see the integrations?</b></summary>

Setting up integrations is a separate permission. Without it a member does not even see where responses are sent.

</details>

<details>
<summary><b>Can the skill remove a member?</b></summary>

Only at your direct request. Access then comes back only through a new invitation, and the surveys they created stay in the account. Before deleting a role, the skill checks who is on it, because those members move to the default role.

</details>

<details>
<summary><b>What do I need to use it?</b></summary>

A SurveyNinja account and an assistant that supports MCP and loads skills from a folder, such as Claude Code, Codex, Cursor or Gemini CLI. The MCP server works on every plan, the free one included. You connect with "Allow access" in the assistant or with your own API key.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
