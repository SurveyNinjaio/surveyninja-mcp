<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Understand results</sub>

# Survey results summary

**Answers "so what did the survey say" with figures and a conclusion instead of a raw export**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-results-digest` | 1.1.1 | 9 | [ZIP](https://surveyninja.io/skills/results-digest.zip) | [surveyninja.io](https://surveyninja.io/skills/results-digest) |

## What it does

1. **Starts from the summary and the report.** Distributions are already calculated in SurveyNinja. Raw completions are needed only for a specific person or to quote wording.
2. **Checks whether the data is complete.** If many completions were abandoned, they are counted separately instead of being folded into one number with the finished ones.
3. **Slices when a condition is named.** "September only", "only people who picked the premium option", "only from the link I emailed". The skill filters by dates, answers, tags or link sets instead of counting by eye.
4. **Leads with the conclusion.** You read "two thirds are unhappy with turnaround" first, and then the base that percentage is taken from.

## What the digest looks like

**Survey results, September**

| Started | Finished | Average score | Left a contact |
|:-:|:-:|:-:|:-:|
| **412** | **318** | **4.1** | **186** |
|  | <sub>77%</sub> | <sub>out of 5</sub> | <sub>45% of those who started</sub> |

| | | |
|---|---|---|
| Very satisfied | `████░░░░░░` | 134 (42%) |
| Somewhat satisfied | `███░░░░░░░` | 92 (29%) |
| Neutral | `██░░░░░░░░` | 48 (15%) |
| Somewhat dissatisfied | `█░░░░░░░░░` | 29 (9%) |
| Very dissatisfied | `░░░░░░░░░░` | 15 (5%) |

> **The headline is turnaround, not price**  
> In the open answers 41 of 96 respondents mention waiting time and 12 mention price. The percentages above are taken from 318 finished completions; abandoned ones are excluded.

<sub>The numbers above are an example. The digest is built from your real responses.</sub>

## How to ask

> What did the survey show? Give me the short version

> Show results for September only, and only for people who came from the link I emailed

> Summarize the survey and tell me what deserves attention

## What not to do

- Do not export a file unasked
- Do not recompute by hand
- Do not mix completed and abandoned
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `export_answers_xlsx` | Export answers to Excel | read |
| `generate_filtered_report` | Filtered report | write |
| `get_quiz_answers` | Quiz answers | read |
| `get_quiz_report` | Quiz report | read |
| `get_quiz_report_inputs` | Text answers of a question | read |
| `get_quiz_structure` | Quiz structure | read |
| `get_quiz_summary` | Quiz summary | read |
| `get_workspace_list` | Workspace list | read |
| `get_workspace_tariff` | Workspace plan | read |

## Questions

<details>
<summary><b>Where does the skill start?</b></summary>

With the survey summary and the per-question report, where distributions and percentages are already calculated. It reads individual responses only when you ask about a specific one or it needs a quote.

</details>

<details>
<summary><b>Can I get results only for September or for one channel?</b></summary>

Yes. Name the condition and the skill builds a slice by dates, by answers to a question, by tags or by a set of unique links. Date, answer and tag slices are not on every plan. To separate channels, each one needs its own set of unique links; a label in the link is counted from the responses that carry it.

</details>

<details>
<summary><b>How does it handle incomplete responses?</b></summary>

Separately. It first checks how many people finished, and if many dropped out it says so. Finished and abandoned are never mixed in one figure without a note.

</details>

<details>
<summary><b>What about open-ended answers?</b></summary>

The skill does not retell them one by one. It groups them into themes and gives a couple of typical quotes.

</details>

<details>
<summary><b>Will I get conclusions even with few responses?</b></summary>

Not as facts. With around ten responses the skill says plainly that the data is too thin to conclude anything.

</details>

<details>
<summary><b>Does the skill change anything in my survey?</b></summary>

No. It only reads the summary, the report and the responses, and it makes an export file only if you ask for one. The download link works for one hour.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
