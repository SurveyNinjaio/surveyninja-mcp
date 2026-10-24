<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Build and share</sub>

# Rewrite survey copy

**Rewrites your questions so people finish the survey, starting from the data rather than taste**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-survey-copy` | 1.1.1 | 6 | [ZIP](https://surveyninja.io/skills/survey-copy.zip) | [surveyninja.io](https://surveyninja.io/skills/survey-copy) |

## What it does

1. **Looks at where people quit.** The questions people abandon get fixed first, not the ones that merely look wrong. If there are no responses to learn from yet, the assistant says so.
2. **Fixes the usual problems.** Bureaucratic tone, double questions, double negatives, internal jargon, leading questions and questions with no bounds. Each edit comes as a before and after.
3. **Works hardest on the first screen.** That is where most people leave. It has to say what is being asked, how long it takes and why it matters to the reader. The last part is usually missing.
4. **Writes only with your consent.** You get the list of edits first and the changes second. Survey copy is often approved by a client or a legal team.

## What the edits look like

**Before and after, 5 questions**

| | | |
|---|---|---|
| **How happy are you with the work?** | was: Please rate your level of satisfaction with the services rendered | too formal |
| **Was it on time? / Was the price fair?** | was: Were you happy with the timing and the price? | double question |
| **Rate the staff at the front desk** | was: Rate the performance of the front office | internal term |
| **How was our service?** | was: How much did you enjoy our excellent service? | leading |
| **Weekly, monthly or less often** | was: How often do you visit us? (open text) | no bounds |

> **The first screen is rewritten in full**  
> "Service quality survey" becomes "Three questions about your visit. Your answers help us cut waiting times." The meaning stays, and now the reader knows why it matters.

<sub>The wording above is an example. Edits are proposed for your survey and your audience.</sub>

## How to ask

> Rewrite the questions in this survey in plain language

> People quit at question three, look at the wording

> Make the first screen of the survey worth reading

## What not to do

- Do not change the meaning of a question
- Do not edit copy of a survey already collecting responses without warning
- Do not add or remove questions
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_answers` | Quiz answers | read |
| `get_quiz_structure` | Quiz structure | read |
| `get_quiz_texts` | Quiz default texts | read |
| `publish_quiz` | Publish quiz | write |
| `update_quiz_texts` | Edit default texts | write |
| `update_quiz_widgets` | Quiz questions and structure | write |

## Questions

<details>
<summary><b>Which questions does the skill fix first?</b></summary>

The ones people quit on, taken from the incomplete responses. If there are none yet, it edits by general rules and says so.

</details>

<details>
<summary><b>What does it fix in the wording?</b></summary>

Bureaucratic tone, double questions, double negatives, internal jargon, leading questions and questions without bounds, such as "how often do you visit us?" asked as open text.

</details>

<details>
<summary><b>What should the first screen say?</b></summary>

What is being asked, how long it takes and why it matters to the reader. The last part is the one most often missing, and it is the one that decides.

</details>

<details>
<summary><b>Will it rewrite everything at once?</b></summary>

No. It first shows a before and after for each question and writes only after you agree, because survey copy is often approved by a client or a legal team.

</details>

<details>
<summary><b>Can it edit a survey that is already collecting responses?</b></summary>

Only after a warning: answers given before and after the edit will no longer be comparable. The assistant tells you before it changes anything.

</details>

<details>
<summary><b>What do I need for this skill to work?</b></summary>

A SurveyNinja account on any plan, including Free, and an AI assistant that supports MCP and loads skills from a folder, such as Claude Code, Codex, Cursor or Gemini CLI. The skill is a plain text file; the assistant works through your API key or the access you allow when connecting.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
