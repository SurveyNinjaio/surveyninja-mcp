<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Understand results</sub>

# Comparing traffic sources

**Shows which channel brought the right people and which only brought numbers**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-source-dashboard` | 1.1.1 | 5 | [ZIP](https://surveyninja.io/skills/source-dashboard.zip) | [surveyninja.io](https://surveyninja.io/skills/source-dashboard) |

## What it does

1. **Checks the labels exist first.** Without source labels on the links a channel breakdown is impossible, and labels cannot be added afterwards. The assistant says so instead of inventing a split.
2. **Counts three things per channel.** How many arrived, how many finished, and the metric that matters to you, such as contacts or average rating.
3. **Separates volume from quality.** A thousand people at five percent completion is worse than a hundred with half finishing. The table shows it; a single total does not.
4. **Keeps unlabelled responses visible.** They get their own row instead of an “other” bucket: usually direct visits, or a label lost when the link was forwarded.

## What you get

| | | |
|---|---|---|
| **Email to customers** | 168 arrived, 119 finished, 62 contacts |  |
| **Instagram** | 94 arrived, 60 finished, 38 contacts |  |
| **No label** | 82 arrived, 48 finished, 27 contacts |  |
| **Website banner** | 68 arrived, 15 finished, 9 contacts |  |

| | | |
|---|---|---|
| Email to customers, 168 people | `███████░░░` | 71% finished |
| Instagram, 94 | `██████░░░░` | 64% |
| No label, 82 | `██████░░░░` | 59% |
| Website banner, 68 | `██░░░░░░░░` | 22% |

> **The banner brings people, just not the right ones**  
> It delivers decent traffic, but only about one in five finishes. Usually the promise on the banner is the cause rather than the channel itself. One run is not enough to switch it off.

<sub>The channels are an example. The split is built from your own source labels.</sub>

## How to ask

> Where did respondents come from and which channel worked best?

> Compare the email campaign and Instagram by response quality

> Split the responses by source label

## What not to do

- Do not infer the channel from arrival time
- Do not advise switching a channel off
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `generate_filtered_report` | Filtered report | write |
| `get_answer_extra_field_values` | Link label values | read |
| `get_quiz_answers` | Quiz answers | read |
| `get_quiz_variables` | Quiz variables | read |
| `manage_quiz_unique_links` | Unique quiz links | destructive |

## Questions

<details>
<summary><b>Can I compare channels without labels?</b></summary>

No. Labels cannot be added afterwards, and the assistant will not guess the channel from arrival time. It suggests giving each channel its own labeled link, so the next run splits by channel.

</details>

<details>
<summary><b>What does the skill count for each channel?</b></summary>

Three things: how many arrived, how many finished, and your target metric, such as contacts or average rating. Both unique links and source labels are counted from the responses themselves.

</details>

<details>
<summary><b>Is the best channel the one with the most responses?</b></summary>

Not necessarily. A channel that brought a thousand people with five percent finishing is worse than one that brought a hundred with half finishing.

</details>

<details>
<summary><b>Does it use Google Analytics or Meta Pixel data?</b></summary>

No. Visits counted by Google Analytics or Meta Pixel stay in those services. The breakdown comes only from the source labels saved with the responses.

</details>

<details>
<summary><b>Will it advise switching off a weak channel?</b></summary>

Not after a single run. It shows how each channel performed, notes when a channel is too small to compare, and leaves the decision to you.

</details>

<details>
<summary><b>What do I need to use it?</b></summary>

A SurveyNinja account and an assistant that supports MCP and loads skills from a folder, such as Claude Code, Codex, Cursor or Gemini CLI. The assistant connects with your own API key or through “Allow access”. The skill only reads responses, reports and label values; it is a plain text file and runs nothing by itself.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
