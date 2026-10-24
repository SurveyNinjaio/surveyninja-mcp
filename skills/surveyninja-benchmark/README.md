<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Understand results</sub>

# Comparing with past results

**Compares a survey with its own past, because one figure means little and a change says a lot**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-benchmark` | 1.1.1 | 7 | [ZIP](https://surveyninja.io/skills/benchmark.zip) | [surveyninja.io](https://surveyninja.io/skills/benchmark) |

## What it does

1. **Checks comparability first.** If the wording or answer options changed between waves, the numbers are not comparable. The skill says so plainly instead of showing a "trend".
2. **Looks at the distribution as well as the average.** The average can stay flat while half the satisfied moved to dissatisfied and the other half moved the other way.
3. **Separates the two kinds of comparison.** One survey across periods is reliable. Different surveys can only be compared on shared metrics such as completion rate and time to complete.
4. **Says whether the change matters.** On small samples a tenth of a point means nothing, and the skill says so instead of calling it growth.

## What a wave comparison looks like

**Spring against autumn, same survey**

| Spring | Autumn | Change | Survey |
|:-:|:-:|:-:|:-:|
| **4.0** | **4.3** | **+0.3** | **unchanged** |
| <sub>286 responses</sub> | <sub>318 responses</sub> |  | <sub>no edits between waves</sub> |

| | | |
|---|---|---|
| Very satisfied, spring | `███░░░░░░░` | 31% |
| Very satisfied, autumn | `████░░░░░░` | 42% |
| Very dissatisfied, spring | `█░░░░░░░░░` | 11% |
| Very dissatisfied, autumn | `░░░░░░░░░░` | 5% |

> **The gain is real, and it sits at the edges**  
> The average moved three tenths, but the interesting part is elsewhere: the very dissatisfied group halved and the very satisfied group grew noticeably. The middle barely moved.

<sub>The numbers above are an example. The skill compares your own periods and surveys.</sub>

## How to ask

> Compare the autumn wave of the survey with the spring one

> Did things get better or worse since the last measurement?

> Compare completion rates across two surveys in my account

## What not to do

- Do not compare periods of different length
- Do not compare waves with an edited questionnaire
- Do not compare seasonal periods head-on
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_answers` | Quiz answers | read |
| `get_quiz_list` | Quiz list | read |
| `get_quiz_report` | Quiz report | read |
| `get_quiz_summary` | Quiz summary | read |
| `get_quiz_versions` | Quiz publication history | read |
| `get_workspace_list` | Workspace list | read |
| `get_workspace_tariff` | Workspace plan | read |

## Questions

<details>
<summary><b>What can I compare?</b></summary>

One survey across periods, in waves, which is the most reliable. Or different surveys in your account, but only on shared metrics: completion rate and time to complete.

</details>

<details>
<summary><b>What does the skill check before comparing?</b></summary>

The publication history: if the wording or answer options changed between waves, the numbers are not comparable and the skill says so. It also checks that the periods are the same length.

</details>

<details>
<summary><b>Why is the average not enough?</b></summary>

The average can stay the same while half the satisfied respondents became dissatisfied and the other half went the other way. The distribution across options shows where a shift came from.

</details>

<details>
<summary><b>How will I know whether things improved?</b></summary>

From the direction and size of the change, such as "the average rose from 4.0 to 4.3", with how many responses each figure rests on, and whether the difference matters on samples of that size.

</details>

<details>
<summary><b>Will it explain why the numbers changed?</b></summary>

Only if the reason is visible in the data. Otherwise it offers a guess and labels it as one.

</details>

<details>
<summary><b>Does the skill change anything in my surveys?</b></summary>

No. It only reads the survey list, the summary, the report, the responses and the publication history.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
