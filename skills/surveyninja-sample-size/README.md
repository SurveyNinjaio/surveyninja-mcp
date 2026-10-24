<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Understand results</sub>

# How many responses you need

**Tells you whether what you have is enough and how many more responses you need before conclusions hold**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-sample-size` | 1.1.1 | 3 | [ZIP](https://surveyninja.io/skills/sample-size.zip) | [surveyninja.io](https://surveyninja.io/skills/sample-size) |

## What it does

1. **Asks about the decision, not the percentage.** Getting a feel for the mood and choosing between two options need different precision, and that sets the sample size.
2. **Counts by segment, not in total.** Splitting by city or segment multiplies the requirement: every group needs its own volume, and one overall figure is not enough.
3. **Gives honest rules of thumb.** 30–50 responses for the general mood, around 400 for five-percent precision. These are conversation benchmarks, and the assistant calls them that.
4. **Can say “that is enough”.** When there is enough data, the assistant says so instead of advising you to keep collecting just in case.

## What you get

| Collected | Overall picture | Precision now | For ±5% |
|:-:|:-:|:-:|:-:|
| **318** | **enough** | **±5.5%** | **+80** |
| <sub>completed</sub> | <sub>about 100 needed</sub> |  | <sub>about 400 in total</sub> |

| | | |
|---|---|---|
| **London** | 142 responses, enough |  |
| **Manchester** | 96 responses, almost there |  |
| **Leeds** | 44 responses, too few |  |
| **Other cities** | 36 responses combined, too few |  |

> **National conclusions hold, city ones do not yet**  
> The most common situation. The overall picture can be shown today. Comparing Leeds with London on 44 responses cannot: the gap will swing with every dozen new responses.

<sub>The numbers are an example. The estimate is made for your survey and your segments.</sub>

## How to ask

> Can we draw conclusions yet or should we keep collecting?

> How many responses do I need to compare two cities?

> Is there enough data to make a decision from this survey?

## What not to do

- Do not demand representativeness
- Do not stay silent about a small sample
- Do not count abandoned responses
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `generate_filtered_report` | Filtered report | write |
| `get_quiz_report` | Quiz report | read |
| `get_quiz_summary` | Quiz summary | read |

## Questions

<details>
<summary><b>What will the skill ask me?</b></summary>

Three things: how large the audience is, what you will decide from the results, and whether you need conclusions per group, such as per city or segment.

</details>

<details>
<summary><b>How many responses do I need?</b></summary>

About 30–50 to get a sense of the mood, around 100 to state shares to about 10%, and roughly 400 for about 5%. To compare two groups, 100 or more in each; for five segments, 100 per segment, so 500 or more.

</details>

<details>
<summary><b>Is this an exact calculation?</b></summary>

No, these are benchmarks for the conversation. If you need a formal estimate, the assistant says the numbers are approximate, explains what they depend on and points you to the free sample size and margin of error calculators on the SurveyNinja site.

</details>

<details>
<summary><b>What if there is enough overall but not per group?</b></summary>

That is the most common case. The assistant tells you which conclusions already hold and which could still reverse.

</details>

<details>
<summary><b>Are incomplete responses counted?</b></summary>

No, only completed responses count toward what has been collected. The skill reads the survey summary and report and changes nothing.

</details>

<details>
<summary><b>What do I need to use it?</b></summary>

A SurveyNinja account and an assistant that supports MCP and loads skills from a folder, such as Claude Code, Codex, Cursor or Gemini CLI. The assistant connects with your own API key or through “Allow access”. The skill is a plain text file and runs nothing by itself.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
