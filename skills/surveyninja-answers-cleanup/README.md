<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Keep the account tidy</sub>

# Cleaning up responses

**Removes test runs and duplicates from your results and shows you the list before anything goes**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-answers-cleanup` | 1.0.1 | 10 | [ZIP](https://surveyninja.io/skills/answers-cleanup.zip) | [surveyninja.io](https://surveyninja.io/skills/answers-cleanup) |

## What it does

1. **Shows first, acts second.** The list to clean comes with counts, the period and the signal it was selected by. Nothing happens until you have seen it.
2. **Builds groups by signal.** Test runs before the survey was shared, too-fast completions, straight-lining and duplicate contacts come as separate groups with numbers.
3. **Moves from reversible to final.** Hiding from reports comes first and can be undone. Then the trash, which can be restored. Permanent deletion happens only when you ask for it directly.
4. **Offers a tag instead of deletion.** A tagged response stays in the statistics and stands out. "Call back", "complaint" and "duplicate" are easier to work with than a spreadsheet export.

## What would be cleaned

**Selection before cleaning, 412 responses**

| Selected | Hide | Trash | For good |
|:-:|:-:|:-:|:-:|
| **64** | **undoable** | **restorable** | **on request** |
|  | <sub>stays in the list</sub> | <sub>if you change your mind</sub> | <sub>only when you ask</sub> |

| | | |
|---|---|---|
| **Test runs before the survey was shared, 3 to 6 September** | the author's own runs while building | 18 |
| **Faster than one minute** | a nine-question survey | 23 |
| **Same option in every question** | straight-lining | 14 |
| **Duplicate email addresses** | one address twice or more | 9 |

> **Nothing has been deleted yet**  
> This is a list for your approval. Hiding from reports is the suggested start: the numbers update right away, and the responses stay in place if you need to undo it.

<sub>The groups above are an example. The selection rules are chosen for your survey.</sub>

## How to ask

> Remove the test runs from this survey's statistics

> Find duplicate email addresses and show them before deleting anything

> Tag everyone who left a phone number and a complaint as "call back"

## What not to do

- Do not delete permanently without explicit consent
- Do not clean "outliers" by answer value
- Do not delete responses to improve the numbers
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `create_answer_tag` | Create answer tag | write |
| `delete_answer_tag` | Delete answer tag | destructive |
| `delete_quiz_answers` | Delete answers | destructive |
| `get_answer_tags` | Account answer tags | read |
| `get_quiz_answers` | Quiz answers | read |
| `get_workspace_list` | Workspace list | read |
| `set_answer_note` | Answer note | write |
| `set_answers_order_mode` | Question order in an answer | write |
| `tag_answer` | Tags on an answer | write |
| `toggle_answer_visibility` | Hide an answer from reports | write |

## Questions

<details>
<summary><b>What junk does the skill look for?</b></summary>

Test runs made while building the survey, completions too fast to read the questions, straight-lining with the same option everywhere, and duplicates by email or phone.

</details>

<details>
<summary><b>Will it delete anything right away?</b></summary>

No. First it shows groups with the number of responses, the period and the selection signal. Cleaning starts only after you agree.

</details>

<details>
<summary><b>What is the difference between hiding and deleting?</b></summary>

A hidden response stays in the list but is left out of reports and the summary, and you can bring it back. A response in the trash can be restored. A permanently deleted response is gone, together with the files the respondent uploaded.

</details>

<details>
<summary><b>Will it remove low ratings?</b></summary>

No. A low rating is a real answer. The skill does not clean outliers by value and does not delete responses to make the numbers look better.

</details>

<details>
<summary><b>Why tags if I can delete?</b></summary>

A tagged response stays in the statistics and is marked: "call back", "complaint", "needs work". The skill reuses the tags you already have, so the same tag does not appear under three spellings.

</details>

<details>
<summary><b>What do I need to use it?</b></summary>

A SurveyNinja account and an assistant that supports MCP and loads skills from a folder, such as Claude Code, Codex, Cursor or Gemini CLI. The MCP server works on every plan, the free one included. You connect with "Allow access" in the assistant or with your own API key.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
