<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Understand results</sub>

# Survey timeline

**Answers “why did responses stop” by lining up collection against the edit history**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-survey-timeline` | 1.1.1 | 5 | [ZIP](https://surveyninja.io/skills/survey-timeline.zip) | [surveyninja.io](https://surveyninja.io/skills/survey-timeline) |

## What it does

1. **Builds two lines.** Responses by day or week, and the publication history. Each explains little alone; together they explain almost everything.
2. **Looks for date matches.** A drop right after a publication means an edit broke something. A drop with no edits points outside: the email campaign ended, the banner came down, the event passed.
3. **Checks the obvious separately.** A sharp drop to zero is a reason to see whether the survey was unpublished or closed, or the monthly response limit was reached. From outside it looks like people simply stopped answering.
4. **Does not pass coincidence off as cause.** If an edit could not have affected collection, the assistant says so. An invented link is worse than an honest “nothing found”.

## What you get

| | | |
|---|---|---|
| 4–10 Aug | `██████████` | 96 |
| 11–17 Aug | `█████████░` | 88 |
| 18–24 Aug, published on the 19th | `███░░░░░░░` | 31 |
| 25–31 Aug | `███░░░░░░░` | 27 |
| 1–7 Sep, logic fixed on the 1st | `███████░░░` | 74 |
| 8–14 Sep | `████████░░` | 81 |

> **The drop starts on the publication date, 19 August**  
> That version added a condition that sent part of the audience into a branch with no exit. After the fix on 1 September collection returned to its earlier level, so the link shows from both sides.

<sub>The dates are an example. The lines are built from your survey and its versions.</sub>

## How to ask

> Why did the survey stop collecting responses?

> Show how responses came in and when we edited the survey

> There was a drop in late August. Work out what it was tied to

## What not to do

- Do not pass a date coincidence off as a cause
- Do not compare weekdays with weekends
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_integrations` | Quiz integration state | read |
| `get_quiz_summary` | Quiz summary | read |
| `get_quiz_versions` | Quiz publication history | read |
| `get_workspace_list` | Workspace list | read |
| `get_workspace_tariff` | Workspace plan | read |

## Questions

<details>
<summary><b>How does the skill look for the cause?</b></summary>

It compares two lines: how responses came in, by day or by week, and when the survey was edited and published. Then it looks for matching dates.

</details>

<details>
<summary><b>What does a drop right after a publication mean?</b></summary>

Most likely an edit broke something: a logic branch, a required field or the link address.

</details>

<details>
<summary><b>And if nobody touched the survey?</b></summary>

Then the cause is outside: an email campaign or ad ended, a banner came down, an event finished. A steady decline is normal decay, because the audience the link reached has run out.

</details>

<details>
<summary><b>Responses dropped to zero. What gets checked?</b></summary>

Whether the survey was unpublished or closed and whether the account reached its monthly response limit; past it, new responses are saved but hidden. If you follow responses in Google Sheets, a webhook or Telegram, the integrations are checked too: a broken connection looks the same from outside.

</details>

<details>
<summary><b>Why not compare weekdays with weekends?</b></summary>

Most surveys have a weekly rhythm. Without noting it, such a comparison shows a drop where there is none.

</details>

<details>
<summary><b>What do I need to use it?</b></summary>

A SurveyNinja account and an assistant that supports MCP and loads skills from a folder, such as Claude Code, Codex, Cursor or Gemini CLI. The assistant connects with your own API key or through “Allow access”. The skill only reads the summary, the publication history, the plan and the integrations; it is a plain text file and runs nothing by itself.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
