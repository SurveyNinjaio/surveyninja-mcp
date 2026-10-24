<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Check before launch</sub>

# Data quality check

**Tells you whether the responses can be trusted before anyone builds conclusions on them**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-data-quality` | 1.0.1 | 7 | [ZIP](https://surveyninja.io/skills/data-quality.zip) | [surveyninja.io](https://surveyninja.io/skills/data-quality) |

## What it does

1. **Checks signal by signal.** Suspiciously fast completions, flat-lining, duplicate contacts, junk in text fields, contradictions and bursts in time. Each signal is counted on its own.
2. **Shows the share as well as the count.** For every signal you see how many completions match and what part of the total they are. A count without a share says little.
3. **Works out whether the conclusions move.** The most useful part of the check: if the key figures stay the same after cleaning, there is no reason to clean.
4. **Leaves low scores alone.** An unhappy respondent is not cheating. Harsh comments and one-star ratings are not treated as junk.

## What the check looks like

**Data quality, 412 completions**

| Questionable | Would remain | Average now | Average after |
|:-:|:-:|:-:|:-:|
| **54** | **358** | **4.1** | **4.2** |
| <sub>13% of the total</sub> |  |  | <sub>difference within noise</sub> |

| | | |
|---|---|---|
| **Under a minute for nine questions** | speed | 23 (6%) |
| **Same option everywhere** | flat-lining | 14 (3%) |
| **One phone number twice or more** | duplicate contacts | 9 (2%) |
| **"aaa", "123", random letters** | junk in text | 11 (3%) |
| **"Never used it" followed by a service rating** | contradiction, likely a logic error | 7 (2%) |

> **Cleaning would not change the conclusions**  
> The average moves by a tenth and the order of the options stays the same. Tag the questionable completions if you like, but deleting them is not worth it for these numbers.

<sub>The numbers above are an example. The check runs on the responses you collected.</sub>

## How to ask

> Can I trust these responses? Check the data quality

> This survey looks gamed. Take a look at the data

> Find suspicious completions and tell me if they change the conclusions

## What not to do

- Do not call low ratings and harsh comments junk
- Do not delete anything yourself
- Do not trim the sample
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `delete_quiz_answers` | Delete answers | destructive |
| `get_quiz_answers` | Quiz answers | read |
| `get_quiz_report` | Quiz report | read |
| `get_quiz_report_inputs` | Text answers of a question | read |
| `get_quiz_summary` | Quiz summary | read |
| `tag_answer` | Tags on an answer | write |
| `toggle_answer_visibility` | Hide an answer from reports | write |

## Questions

<details>
<summary><b>What does the skill treat as suspicious?</b></summary>

Completions that are too fast, the same answer everywhere, duplicates by phone or email, junk in text fields, contradictions, and bursts such as twenty completions in a minute with identical answers.

</details>

<details>
<summary><b>How fast is too fast?</b></summary>

A rough guide is at least five seconds per question. For a ten-question survey, anything under a minute is suspicious. The skill also looks at the average time for your survey.

</details>

<details>
<summary><b>Are contradictory answers a sign of cheating?</b></summary>

Usually not. "Never used the service" followed by a rating of it more often means the display logic is set up wrong.

</details>

<details>
<summary><b>What do I get in the end?</b></summary>

For each signal, how many completions match and what share of the total they are. Most importantly, whether the key figures change once everything doubtful is set aside. If they do not, the skill says there is no need to clean.

</details>

<details>
<summary><b>Will the skill delete suspicious responses?</b></summary>

No. It only reads. It suggests what to do: tag the responses, hide them from reports, which can be undone, or delete them if you ask directly and confirm.

</details>

<details>
<summary><b>What do I need to use it?</b></summary>

A SurveyNinja account and an assistant that connects to MCP and loads skills from a folder, such as Claude Code, Codex, Cursor or Gemini CLI. Access goes through your own API key or "Allow access" in the assistant. The skill is plain text that runs nothing itself: your assistant does the work through the MCP server, with your permissions.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
