<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Build and share</sub>

# Skip logic and branching

**Sets up survey logic so that no respondent ever hits a dead end**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-survey-logic` | 1.0.2 | 3 | [ZIP](https://surveyninja.io/skills/survey-logic.zip) | [surveyninja.io](https://surveyninja.io/skills/survey-logic) |

## What it does

1. **Reads the structure first.** The skill reads the question IDs first, so every condition points at a real question.
2. **Builds the right kind of rule.** A branch on an answer, a question shown or hidden, a skipped block, a screenout for people who do not qualify or a quota per group, chosen to fit the task.
3. **Knows the usual traps.** "Other" fires on the option, not on the text typed into it. "Greater than" does not work on text. Conditions are checked in order and the first match wins.
4. **Walks the route after the edit.** From the first question along every branch to the end. With more than three or four branches, the assistant describes the map in words.

## What the routing looks like

**Survey logic, 4 rules**

| Branches | Dead ends | Unreachable | Loops |
|:-:|:-:|:-:|:-:|
| **4** | **0** | **0** | **0** |
|  | <sub>each route walked</sub> |  | <sub>no jumps backwards</sub> |

| | | |
|---|---|---|
| **Rating below 4 → "What went wrong?"** | branch on answer · question 2 | has an exit |
| **Rating 4 or higher → skip question 3** | skipped block | has an exit |
| **"Never used the service" → screenout** | screenout · question 4 | end |
| **200 responses in the group → stop admitting** | quota | end |

> **"Other" fires on the option, not on the text**  
> A common mistake is expecting a jump to react to the words typed into the "Other" field. The condition reacts to the option being chosen; the text plays no part.

<sub>The rules above are an example. Logic is built from your questions and their identifiers.</sub>

## How to ask

> If someone rates us below four, ask them why

> Skip the quality questions for people who never used the service

> Check the survey logic for dead ends

## What not to do

- Do not write logic without reading the structure
- Do not change the question set in the same edit
- Do not build branching where one question with options is enough
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_structure` | Quiz structure | read |
| `publish_quiz` | Publish quiz | write |
| `update_quiz_logic` | Quiz branching logic | write |

## Questions

<details>
<summary><b>What can be set up?</b></summary>

A branch on an answer ("rated below four, ask why"), showing or hiding a question, skipping a block, screening out people who do not qualify, and quotas per group.

</details>

<details>
<summary><b>Why does the skill read the survey first?</b></summary>

Conditions point at questions by their IDs. The skill reads those IDs first, so every condition points at a real question.

</details>

<details>
<summary><b>How does it avoid dead ends?</b></summary>

Every branch must have an exit, to the next block or to the end, and no branch may lead back to a question already answered.

</details>

<details>
<summary><b>Will a condition react to the text typed into "Other"?</b></summary>

No. The condition reacts to the "Other" option being chosen, not to what the respondent typed.

</details>

<details>
<summary><b>Will the skill change my questions as well?</b></summary>

No. Questions and logic are separate edits. If both change at once and something breaks, it is unclear which change caused it.

</details>

<details>
<summary><b>What do I need for this skill to work?</b></summary>

A SurveyNinja account on any plan, including Free, and an AI assistant that supports MCP and loads skills from a folder, such as Claude Code, Codex, Cursor or Gemini CLI. The skill is a plain text file; the assistant works through your API key or the access you allow when connecting.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
