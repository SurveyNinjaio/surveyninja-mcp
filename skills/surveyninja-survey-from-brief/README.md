<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Build and share</sub>

# Build a survey from a brief

**Describe what you need in plain words, and the assistant builds the survey in your SurveyNinja account as a draft**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-survey-from-brief` | 1.0.2 | 13 | [ZIP](https://surveyninja.io/skills/survey-from-brief.zip) | [surveyninja.io](https://surveyninja.io/skills/survey-from-brief) |

## What it does

1. **Asks only what is missing.** Who is being asked, what the results will decide and where the link will live. Three questions at most; everything else is faster to fix on a draft.
2. **Picks the right question types.** A rating becomes a scale, a recommendation question becomes NPS, phone and email become fields with format checks. Whether the results can be summarized later depends on this.
3. **Wires up the branching.** Unhappy respondents get asked why, and people who never used the service skip that block. Logic is built from the survey structure, so no route ends in a dead end.
4. **Publishes only when you say so.** Until then the survey does not open by its link, so there is time to read the draft and change it.

## What one sentence turns into

**Repair shop customer survey**

| Questions | Required | Branches | Length |
|:-:|:-:|:-:|:-:|
| **7** | **2** | **2** | **~2 min** |
| <sub>plus welcome and thank-you</sub> | <sub>contact details only</sub> | <sub>by rating and service</sub> | <sub>to complete</sub> |

| | | |
|---|---|---|
| **How happy are you with the work?** | Star rating, 5 stars | — |
| **What could we have done better?** | Text answer, shown when the rating is below 4 | branch |
| **Was it finished on time?** | Yes or no | — |
| **Rate the front desk, the work and the price** | Matrix, 3 rows | — |
| **What is the best email to reach you?** | Email, format checked | required |

> **Ready to launch, not yet published**  
> The assistant hands over a draft you can review in the builder. Publishing is a separate step and happens only on your word.

<sub>The survey above is an example of how the phrase "rate the work and collect contacts for a follow-up visit" can be read. Your survey is built from your brief.</sub>

## How to ask

> Build a survey for our repair shop customers: rate the work and collect contacts for a follow-up visit

> I need a short satisfaction survey after delivery: three questions and an email

> Create a consultation request form with name, phone, preferred time and the customer's question

## What not to do

- Do not publish unasked
- Do not invent filler questions
- Do not make everything required
- Do not suggest a plan upgrade or lead to payment
- Do not delete or rewrite existing surveys

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `apply_quiz_theme` | Apply theme to quiz | write |
| `create_quiz` | Create quiz | write |
| `create_quiz_from_template` | Create quiz from template | write |
| `generate_ai_quiz` | Build quiz from description | write |
| `get_folder_list` | Folder list | read |
| `get_quiz_structure` | Quiz structure | read |
| `get_quiz_texts` | Quiz default texts | read |
| `get_theme_list` | Theme list | read |
| `publish_quiz` | Publish quiz | write |
| `search_quiz_templates` | Search ready-made quizzes | read |
| `update_quiz_logic` | Quiz branching logic | write |
| `update_quiz_texts` | Edit default texts | write |
| `update_quiz_widgets` | Quiz questions and structure | write |

## Questions

<details>
<summary><b>How many questions will the assistant ask me?</b></summary>

Three at most, and only if you did not say it already: who is being asked, what the results will decide and where the link will live. The rest is quicker to fix on the draft.

</details>

<details>
<summary><b>How does it choose question types?</b></summary>

By what you need to learn. A rating gets a scale or stars, likelihood to recommend gets NPS, phone and email get fields with format checks, a date gets a date field. The type decides whether the answers can be summarized.

</details>

<details>
<summary><b>What if there is a ready-made template for my topic?</b></summary>

The assistant offers to start from it, because that is faster and usually better than building from scratch. You decide.

</details>

<details>
<summary><b>Which questions will be required?</b></summary>

Only the contact details the survey exists for. Every extra required question costs responses.

</details>

<details>
<summary><b>Will respondents see the survey right away?</b></summary>

No. Until it is published it does not open by its link. The assistant publishes only when you say so, then sends the link and a short summary of what was built.

</details>

<details>
<summary><b>What do I need for this skill to work?</b></summary>

A SurveyNinja account on any plan, including Free, and an AI assistant that supports MCP and loads skills from a folder, such as Claude Code, Codex, Cursor or Gemini CLI. The skill is a plain text file; the assistant works through your API key or the access you allow when connecting.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`references/widget-types.md`](references/widget-types.md): reference the skill reads when it needs it
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
