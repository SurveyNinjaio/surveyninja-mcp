<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Understand results</sub>

# Analyze open-ended answers

**Turns a hundred lines of free text into a handful of themes with numbers and quotes**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-open-answers` | 1.1.1 | 5 | [ZIP](https://surveyninja.io/skills/open-answers.zip) | [surveyninja.io](https://surveyninja.io/skills/open-answers) |

## What it does

1. **Groups answers by meaning.** “Waited too long”, “waited forty minutes” and “the queue” are one theme. The words do not have to match.
2. **Counts the shares.** For each theme: how many answers and what share of everyone who wrote something. A theme without a number decides nothing.
3. **Sets aside the empty ones.** “No”, “all fine” and “-” go into their own group. They are not themed and not hidden either, because the size of that group says something too.
4. **Quotes verbatim.** One or two characteristic quotes per theme, typos and all, with no polishing. Personal details are stripped out of the quote.

## What you get

| | | |
|---|---|---|
| Long wait | `████░░░░░░` | 41 (43%) |
| Unclear what the price includes | `██░░░░░░░░` | 18 (19%) |
| Nobody called back | `█░░░░░░░░░` | 12 (13%) |
| Praise for the technician | `█░░░░░░░░░` | 9 (9%) |
| No content | `██░░░░░░░░` | 16 (17%) |

> **“waited almost an hour even though I booked for 10:00”**  
> Waiting is both the largest theme and the most consistent one: people name a specific time instead of complaining in general. That is something you can measure and fix.

<sub>The themes and the quote are an example. The analysis runs on your own text answers.</sub>

## How to ask

> Group the free-text answers into themes and show what comes up most

> What are people writing in the “what could be better” question?

> Pull themes out of the open answers with quotes

## What not to do

- Do not mix answers to different questions
- Do not surface quotes containing personal data
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_report` | Quiz report | read |
| `get_quiz_report_filters` | Saved report filters | read |
| `get_quiz_report_inputs` | Text answers of a question | read |
| `get_quiz_structure` | Quiz structure | read |
| `save_quiz_report_filters` | Save report filters | write |

## Questions

<details>
<summary><b>How does the skill find themes?</b></summary>

By meaning rather than wording: “waited too long”, “waited forty minutes” and “the queue” are one theme. Each theme gets the number of answers and its share of everyone who wrote something.

</details>

<details>
<summary><b>What happens to answers like “no” or “all fine”?</b></summary>

They go into a separate “no content” group. It is not split into themes and not hidden either, because its size says something too.

</details>

<details>
<summary><b>Can it analyze several questions at once?</b></summary>

One at a time. Mixing answers to different questions produces mush, so the questions are analysed one after another.

</details>

<details>
<summary><b>Can I analyze the answers of only some respondents?</b></summary>

Yes, if report filters are available on your plan. The texts follow the report's saved filters, so the assistant sets them to your condition, but asks you first: the same filters apply to the report others see.

</details>

<details>
<summary><b>What about personal data in the answers?</b></summary>

Phone numbers, email addresses and names are removed from the quotes. The skill only reads answers and changes nothing in the survey.

</details>

<details>
<summary><b>What do I need to use it?</b></summary>

A SurveyNinja survey with open questions and an assistant that supports MCP and loads skills from a folder, such as Claude Code, Codex, Cursor or Gemini CLI. The assistant connects with your own API key or through “Allow access”. The skill is a plain text file and runs nothing by itself.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
