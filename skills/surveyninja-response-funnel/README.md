<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Understand results</sub>

# Completion funnel

**Shows which question makes people close the tab, and why**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-response-funnel` | 1.1.1 | 5 | [ZIP](https://surveyninja.io/skills/response-funnel.zip) | [surveyninja.io](https://surveyninja.io/skills/response-funnel) |

## What it does

1. **Finds the drop-off.** Counts how many people answered each question. Where the count falls is where the problem is.
2. **Explains the reason.** Open text, a required contact field, a ten-row matrix: each question type is abandoned for its own reasons.
3. **Separates normal from broken.** Losing a couple of percent at every step always happens. A cliff at one question does not.
4. **Suggests specific edits.** Instead of “make the survey shorter”, it names the question to make optional and the one to move closer to the end.

## What you get

| Opened | Started | Finished | Drop-off |
|:-:|:-:|:-:|:-:|
| **1,284** | **912** | **318** | **question 5** |
|  | <sub>71% of those who opened</sub> | <sub>35% of those who started</sub> | <sub>41% lost in one step</sub> |

| | | |
|---|---|---|
| 1. Welcome | `██████████` | 912 (100%) |
| 2. How happy are you? | `██████████` | 874 (96%) |
| 3. Was it finished on time? | `█████████░` | 831 (91%) |
| 4. What could be better? (open text) | `███████░░░` | 602 (66%) |
| 5. Your phone number (required) | `████░░░░░░` | 355 (39%) |
| 6. Thank you | `████░░░░░░` | 318 (35%) |

> **The main loss is the required phone number at step five**  
> Many of the people who get there walk away. Move the contact field to the end and explain in one line why it is needed.

<sub>The numbers are an example. In your account the funnel is built from real responses.</sub>

## How to ask

> Why does this survey get so few responses? Find where people quit

> How many people finish the survey and where do they drop off?

> Break down the completion funnel and suggest what to fix

## What not to do

- Do not compute conversion over all responses
- Do not draw conclusions from twenty responses
- Do not edit the survey yourself
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_answers` | Quiz answers | read |
| `get_quiz_structure` | Quiz structure | read |
| `get_quiz_summary` | Quiz summary | read |
| `get_workspace_list` | Workspace list | read |
| `get_workspace_tariff` | Workspace plan | read |

## Questions

<details>
<summary><b>How does the skill find where people quit?</b></summary>

It computes the share who finished, then reads the unfinished responses and finds the last question each person answered: where most of them stop is the drop. Then it ties that question's position to its content and type.

</details>

<details>
<summary><b>What counts as normal?</b></summary>

A steady decline of a couple of percent from question to question: some people always leave. The problem is a cliff at one specific question.

</details>

<details>
<summary><b>Why do people leave on the first screen or the last one?</b></summary>

On the first screen the issue is the promise: it is unclear what the survey is for, or it looks long. On the last one it is almost always contacts, asked for before the person understands why to give them.

</details>

<details>
<summary><b>What if my plan does not keep incomplete responses?</b></summary>

Incomplete responses are not on every plan, and the skill checks that. If they are unavailable, there is nothing to compute the drop-off from: the assistant gives the completion share and a review of the survey itself, and says that this is weaker than a measurement.

</details>

<details>
<summary><b>Will the skill change my survey?</b></summary>

No. It only reads the summary, the incomplete responses and the survey structure. It shows what it found and proposes specific edits, and you decide.

</details>

<details>
<summary><b>What do I need to use it?</b></summary>

A SurveyNinja account and an assistant that supports MCP and loads skills from a folder, such as Claude Code, Codex, Cursor or Gemini CLI. The assistant connects with your own API key or through “Allow access”. The skill is a plain text file and runs nothing by itself.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
