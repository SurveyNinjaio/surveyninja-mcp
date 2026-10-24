<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Understand results</sub>

# Results for the client

**Turns survey results into something you can send: a link, a file or a report with conclusions**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-results-sharing` | 1.0.2 | 13 | [ZIP](https://surveyninja.io/skills/results-sharing.zip) | [surveyninja.io](https://surveyninja.io/skills/results-sharing) |

## What it does

1. **Works out what is needed first.** A summary, a report with breakdowns, individual responses and a text with conclusions are four different things. The assistant asks one clarifying question instead of guessing.
2. **Picks a link or a file for the job.** A link shows fresh data and cannot be revoked later. A file freezes the state on a date. Download links live an hour, and the assistant says so up front.
3. **Checks what goes outside.** If the survey asks for phones or emails, a public link to responses shows them to anyone. The assistant warns you and offers the summary instead.
4. **Hands over the AI report.** It reads the report you already have before building a new one, and says honestly when there are too few answers for conclusions.

## What you get

| Responses | Period | Format | Contacts |
|:-:|:-:|:-:|:-:|
| **318** | **Sept** | **link** | **hidden** |
| <sub>finished only</sub> |  | <sub>plus a dated PDF</sub> | <sub>not in the report</sub> |

| | | |
|---|---|---|
| **Public report link** | September, finished responses, stays open |  |
| **Summary as PDF** | snapshot as of 30 September, download link lives an hour |  |
| **AI report** | three sections, building now |  |
| **Link to responses** | the survey has a phone field, waiting for your OK |  |

> **Responses with phone numbers stayed inside**  
> The survey has a phone field, and a public link to responses would show it to anyone holding the link. The client got the report and the summary. The responses wait for your explicit confirmation.

<sub>The numbers above are an example. The assistant builds what you ask for from your own survey.</sub>

## How to ask

> Send the client the survey results for September

> Make a report link I can show my manager

> Build a report with conclusions and share it as a link

## What not to do

- Do not share responses with contacts via a public link
- Do not export a file when a link was asked for
- Do not build an AI report silently
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `export_answers_xlsx` | Export answers to Excel | read |
| `export_filtered_report_pdf` | Export report to PDF | read |
| `export_filtered_report_word` | Export report to Word | read |
| `export_summary_pdf` | Export summary to PDF | read |
| `generate_ai_report` | AI report | write |
| `get_ai_report` | Ready AI report | read |
| `get_quiz_list` | Quiz list | read |
| `get_quiz_report_filters` | Saved report filters | read |
| `get_quiz_structure` | Quiz structure | read |
| `share_ai_report` | Public link to an AI report | write |
| `share_answers_link` | Public link to answers | write |
| `share_report_link` | Public link to a report | write |
| `share_summary_link` | Public link to a summary | write |

## Questions

<details>
<summary><b>What can I hand to a client?</b></summary>

The summary with totals per question, the report with breakdowns by period or filter, the responses showing who answered what, or the AI report with written conclusions instead of tables.

</details>

<details>
<summary><b>Should I send a link or a file?</b></summary>

A link always shows fresh data and suits a survey that is still collecting. A file keeps the state at the moment of export, which is what you want for a report as of a date.

</details>

<details>
<summary><b>How long does a link work?</b></summary>

A public link has no expiry and cannot be turned off: it stops opening only if the survey is archived or deleted. A download link for a file lives one hour, and the skill tells you so.

</details>

<details>
<summary><b>Will respondents' contacts leak?</b></summary>

The skill checks whether the survey has a phone, email or name question. If it does, it offers the summary or the report, and shares responses outside only after you confirm directly.

</details>

<details>
<summary><b>Can it hand over the AI report?</b></summary>

Yes. It reads the report you already have first, builds a new one only after warning you, and will not build one on a handful of answers. Sharing it as a link needs the survey to be published. The AI report, called Smart Analytics in the app, is not on every plan; where it is missing, the assistant says so and hands over the summary or the report instead.

</details>

<details>
<summary><b>What do I need for this to work?</b></summary>

A SurveyNinja account and an assistant that connects to MCP servers and loads skills from a folder, such as Claude Code, Codex, Cursor or Gemini CLI. Access goes through your own API key or the Allow access button. The skill itself is a plain text file and runs nothing.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
