<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Keep the account tidy</sub>

# Tidying up the account

**Sorts, archives, copies and cleans, and knows which of those cannot be undone**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-workspace-housekeeping` | 1.0.2 | 16 | [ZIP](https://surveyninja.io/skills/workspace-housekeeping.zip) | [surveyninja.io](https://surveyninja.io/skills/workspace-housekeeping) |

## What it does

1. **List first, actions second.** When you say "tidy up", the assistant does not start deleting. It shows what it proposes for each survey and waits for your agreement.
2. **Tells archive, trash and permanent apart.** A finished survey with responses goes to the archive, where everything is kept. Drafts go to the trash and can be restored. Deleting a full workspace or files is final and needs a separate yes.
3. **Makes a new wave as a copy.** Last time's survey is copied under a new name instead of being edited, so the previous wave stays comparable. A recurring survey becomes a template.
4. **Leaves live surveys alone.** Before archiving it checks for recent responses: an archived survey stops accepting them.

## What is proposed

**Tidy-up plan, 34 surveys in the account**

| Archive | Trash | Template | Permanent |
|:-:|:-:|:-:|:-:|
| **6** | **12** | **1** | **0** |
| <sub>reversible</sub> | <sub>restorable</sub> |  | <sub>not confirmed yet</sub> |

| | | |
|---|---|---|
| **"Delivery feedback, spring" and 5 more** | no responses since April, responses are kept | archive |
| **11 drafts without a single question** | last edited in February | to the trash |
| **"Survey (copy) (copy)"** | duplicate of a live survey, no responses | to the trash |
| **"Service quality"** | runs every quarter | template |
| **3.4 GB of respondent files in archived surveys** | frees space, cannot be undone | ask |

> **Nothing has been done yet, this is a plan for approval**  
> Archive and trash can be undone, so they can start right after your "yes". Respondent files are deleted for good, so they need a separate answer.

<sub>The list above is an example. The real plan is built from your account.</sub>

## How to ask

> Tidy up my account: sort surveys into workspaces and archive the old ones

> Copy the customer survey for the autumn wave into the "2026" workspace

> Make a template from the quality survey, we run it every quarter

## What not to do

- Do not delete permanently without explicit agreement
- Do not archive a survey that is still collecting responses
- Do not rename or move other people's surveys
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `archive_quiz` | Archive quiz | write |
| `create_folder` | Create folder | write |
| `delete_quiz` | Delete quiz | destructive |
| `duplicate_quiz` | Duplicate quiz | write |
| `get_folder_list` | Folder list | read |
| `get_quiz_list` | Quiz list | read |
| `get_quiz_summary` | Quiz summary | read |
| `get_workspace_list` | Workspace list | read |
| `get_workspace_templates` | Workspace templates | read |
| `make_quiz_template` | Make quiz a template | write |
| `manage_workspace_files` | Workspace files | destructive |
| `manage_workspace_folder` | Manage folder | destructive |
| `move_quiz` | Move quiz to a folder | write |
| `rename_quiz` | Rename quiz | write |
| `restore_quiz` | Restore quiz from trash | write |
| `update_quiz_note` | Quiz note | write |

## Questions

<details>
<summary><b>What can the skill tidy up?</b></summary>

It sorts surveys into workspaces, renames them, moves them to the archive or the trash, makes copies and templates, and cleans up account files. Finding what is abandoned and where storage runs out is the job of the Workspace audit skill.

</details>

<details>
<summary><b>What is the difference between the archive and the trash?</b></summary>

An archived survey stops accepting responses but keeps everything, and it does not count against the survey limit. That is for finished surveys. A survey in the trash can be restored with its questions, logic and responses. That is for drafts and duplicates.

</details>

<details>
<summary><b>Can anything be lost for good?</b></summary>

Yes, in two cases: deleting a workspace that still has surveys in it, which removes them with their responses, and deleting files. Both happen only at your direct request and only for a list you have seen. Respondent files cannot be recovered.

</details>

<details>
<summary><b>How do I start a new wave of a survey?</b></summary>

With a copy. The skill copies the survey into the right workspace under a new name, and the previous wave's responses stay untouched and comparable. If you run it regularly, it can become a template.

</details>

<details>
<summary><b>Will it rename my colleagues' surveys?</b></summary>

Not without asking. In a shared workspace colleagues look for surveys by their old names and in their old workspaces.

</details>

<details>
<summary><b>What do I need to use it?</b></summary>

A SurveyNinja account and an assistant that supports MCP and loads skills from a folder, such as Claude Code, Codex, Cursor or Gemini CLI. The MCP server works on every plan, the free one included. You connect with "Allow access" in the assistant or with your own API key.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
