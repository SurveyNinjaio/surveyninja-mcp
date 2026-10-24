<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Understand results</sub>

# A/B variant analysis

**Tells you whether the difference between variants is real or just noise**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-ab-significance` | 1.1.1 | 9 | [ZIP](https://surveyninja.io/skills/ab-significance.zip) | [surveyninja.io](https://surveyninja.io/skills/ab-significance) |

## What it does

1. **Counts from the base.** "42 of 180 against 34 of 179" shows what the conclusion rests on. Bare percentages such as "23% against 19%" hide it.
2. **Checks there is enough data.** On fifty responses a ten point gap appears by itself. The skill says when it is too early to call.
3. **Verifies the comparison is fair.** Different periods, different traffic sources or wording edited mid-test break the comparison. That is checked before a winner is named.
4. **Is willing to say "no difference".** That is a result too: it means the variant can be chosen on other grounds.

## What the answer looks like

**A/B test, first question wording**

| Variant A | Variant B | Difference | Data |
|:-:|:-:|:-:|:-:|
| **23.3%** | **19.0%** | **4.3 pp** | **thin** |
| <sub>42 of 180 left a contact</sub> | <sub>34 of 179</sub> | <sub>in favor of A</sub> | <sub>400+ per group needed</sub> |

| | | |
|---|---|---|
| Variant A: "Three questions about your visit" | `██░░░░░░░░` | 23.3% |
| Variant B: "Service quality survey" | `██░░░░░░░░` | 19.0% |

> **Too early to declare a winner**  
> A 4.3 point gap on groups of 180 is within the margin of error. To say that A is better you need around 400 completions in each group.

<sub>The numbers above are an example. The skill works from your real variants and picks whichever of the three verdicts is honest.</sub>

## How to ask

> Compare the A/B variants in this survey. Which one is better?

> Can we pick a winner yet, or is the data too thin?

> Check whether the difference between the two question wordings is significant

## What not to do

- Do not declare a winner on a couple of points
- Do not compare variants from different periods
- Do not peek and stop the test
- Do not call a difference significant because it is badly wanted
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `export_answers_csv` | Export answers to CSV | read |
| `generate_filtered_report` | Filtered report | write |
| `get_quiz_answers` | Quiz answers | read |
| `get_quiz_report` | Quiz report | read |
| `get_quiz_structure` | Quiz structure | read |
| `get_quiz_summary` | Quiz summary | read |
| `get_quiz_versions` | Quiz publication history | read |
| `get_workspace_list` | Workspace list | read |
| `get_workspace_tariff` | Workspace plan | read |

## Questions

<details>
<summary><b>What can the skill compare?</b></summary>

The built-in SurveyNinja A/B test, where a question shows different versions of its title and description, and also two surveys or two sets of links that you ran as variants.

</details>

<details>
<summary><b>What counts as success?</b></summary>

Whatever you name: the share who finished, the share who left a contact, the average rating. If you have not said, the assistant asks first, because without a goal there is nothing to compare.

</details>

<details>
<summary><b>How many responses do I need?</b></summary>

It depends on the gap. A five point difference needs hundreds of responses in each group, a twenty point one needs dozens. With fewer than a hundred per group a difference is almost never proven.

</details>

<details>
<summary><b>What answer will I get?</b></summary>

One of three: there is a difference, with its size and what it means in practice; there is no difference, so choose on other grounds; or there is not enough data yet, with how much more to collect.

</details>

<details>
<summary><b>Can I stop the test as soon as one variant pulls ahead?</b></summary>

The skill will not advise that, since pulling ahead by chance is common. Decide once you have the volume you need.

</details>

<details>
<summary><b>Does the skill change anything in my survey?</b></summary>

No. It only reads the structure, the report and the responses.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
