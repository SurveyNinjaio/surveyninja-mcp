<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Check before launch</sub>

# Pre-launch check

**Finds what will break on real respondents while the link is still unsent**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-prelaunch-check` | 1.0.2 | 8 | [ZIP](https://surveyninja.io/skills/prelaunch-check.zip) | [surveyninja.io](https://surveyninja.io/skills/prelaunch-check) |

## What it does

1. **Reads the whole survey first.** Questions, logic, texts and publication state. Before judging anything, the assistant looks at what is actually in the survey.
2. **Walks every route to the end.** Dead ends, unreachable questions, conditions on deleted questions, a "greater than" on a text field. These are the things that surface on live respondents.
3. **Checks where the responses will land.** Email recipients and whether their addresses are confirmed, Telegram, Zapier, Google Sheets and webhooks. An unconfirmed address looks configured but never receives mail.
4. **Hands over a list and waits.** Nothing is fixed quietly. Findings come sorted by severity, and you decide what to fix.

## What a pre-launch check finds

**Survey check, 12 points**

| Breaks collection | Hurts data | Minor | Clean |
|:-:|:-:|:-:|:-:|
| **2** | **3** | **4** | **3** |
| <sub>fix before sending</sub> |  |  | <sub>checked, nothing to report</sub> |

| | | |
|---|---|---|
| **The "never used the service" branch leads nowhere** | logic, question 6 | critical |
| **No email recipients and no integrations** | where responses land | critical |
| **Recipient address is not confirmed** | email, marketing@… | important |
| **Phone is required at question three of nine** | questions | important |
| **The finish screen has no text** | texts, finish | important |
| **Button labels are still the defaults** | texts | minor |

> **Not ready to publish yet**  
> Two findings will lose responses outright: the dead end in the logic and leads that nobody receives. The rest can wait until after launch.

<sub>The findings above are an example. In your account the check runs against your own survey.</sub>

## How to ask

> Check my survey before launch. Is everything ready?

> I am about to send the link. Did I forget anything?

> Find logic and text problems before I publish

## What not to do

- Do not fix silently
- Do not publish on your own initiative
- Do not rewrite question wording
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_email_settings` | Quiz email settings | read |
| `get_quiz_integrations` | Quiz integration state | read |
| `get_quiz_list` | Quiz list | read |
| `get_quiz_structure` | Quiz structure | read |
| `get_quiz_summary` | Quiz summary | read |
| `get_quiz_texts` | Quiz default texts | read |
| `get_quiz_webhooks` | Quiz webhooks | read |
| `get_workspace_tariff` | Workspace plan | read |

## Questions

<details>
<summary><b>What does the skill check?</b></summary>

The branching logic, the questions, the texts and the finish screen, where the responses will go, the limits left on your plan, and whether the survey is published and reachable. For a survey on your website it checks that the survey is attached to a site.

</details>

<details>
<summary><b>Which logic errors does it look for?</b></summary>

Dead ends with no way forward, questions that no route leads to, conditions on deleted questions, and operators that do not fit the question, such as "greater than" on a text field.

</details>

<details>
<summary><b>Will it check that I actually receive the responses?</b></summary>

Yes. It looks at email notifications and whether the recipient addresses are confirmed, at Telegram, Zapier and Google Sheets, and at webhooks, including one that was switched off after failed deliveries.

</details>

<details>
<summary><b>Will the skill fix what it finds?</b></summary>

No. It lists the findings and you decide what to repair. It will not publish the survey on its own or rewrite your questions.

</details>

<details>
<summary><b>What do I get at the end?</b></summary>

A list sorted by weight: what will break collection, what will hurt data quality, and what is just worth improving. If everything is clean, it says so without inventing remarks.

</details>

<details>
<summary><b>What do I need to use it?</b></summary>

A SurveyNinja account and an assistant that connects to MCP and loads skills from a folder, such as Claude Code, Codex, Cursor or Gemini CLI. Access goes through your own API key or "Allow access" in the assistant. The skill is plain text that runs nothing itself: your assistant does the work through the MCP server, with your permissions.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
