<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Deliver responses</sub>

# Lead quality

**Counts the people who left a contact you can actually use**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-lead-quality` | 1.1.1 | 8 | [ZIP](https://surveyninja.io/skills/lead-quality.zip) | [surveyninja.io](https://surveyninja.io/skills/lead-quality) |

## What it does

1. **Puts the right number first.** The share of people who left a usable contact, out of everyone who started. Completion can be high while leads are almost absent.
2. **Finds where people changed their mind.** It compares the question before the contact with the contact itself. The gap shows how many got that far and still closed the tab.
3. **Filters out what you cannot use.** Broken emails, test@test.com, phone numbers with too few or too many digits, one-letter names and duplicates are counted apart. A lead you cannot reach does not go into the total.
4. **Splits leads by channel.** If the link carried source labels, you see where leads are more numerous and where they are better. Quite often those are different channels.

## What the lead breakdown looks like

**Lead quality, last 30 days**

| Started | Reached the contact | Left a contact | Usable |
|:-:|:-:|:-:|:-:|
| **512** | **243** | **186** | **164** |
|  | <sub>47%</sub> |  | <sub>32% of those who started</sub> |

| | | |
|---|---|---|
| Newsletter | `████░░░░░░` | 38% usable |
| LinkedIn post | `███░░░░░░░` | 31% |
| Website banner | `██░░░░░░░░` | 19% |
| No label | `██░░░░░░░░` | 24% |

> **Leads are lost at the moment you ask for the contact**  
> 57 people reached the email field and left it empty. One line explaining why you need the address usually lifts that share more than any design change.

<sub>The numbers above are an example. The real count runs on your responses and your link labels.</sub>

## How to ask

> How many usable leads did this survey collect?

> Check the quality of our leads and tell me where we lose them

> Which channel brings better leads?

## What not to do

- Do not count a submission without a contact as a lead
- Do not paste contacts into the chat
- Do not advise removing every required field
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_answers` | Quiz answers | read |
| `get_quiz_report` | Quiz report | read |
| `get_quiz_report_inputs` | Text answers of a question | read |
| `get_quiz_structure` | Quiz structure | read |
| `get_quiz_summary` | Quiz summary | read |
| `get_quiz_variables` | Quiz variables | read |
| `get_workspace_list` | Workspace list | read |
| `get_workspace_tariff` | Workspace plan | read |

## Questions

<details>
<summary><b>What does the skill count as a lead?</b></summary>

A submission with a usable contact. A submission without a contact is not a lead, and neither is one with a broken email or a phone number that cannot exist.

</details>

<details>
<summary><b>Why not the completion rate?</b></summary>

When a survey works as a lead form, what matters is how many people you can contact afterwards. The headline number is the share with a usable contact out of everyone who started.

</details>

<details>
<summary><b>What counts as an unusable contact?</b></summary>

Emails with a broken format, placeholder addresses such as test@test.com, typos like gmial.com, phone numbers with fewer than 7 or more than 15 digits, one-letter names. The skill counts them separately and merges duplicates.

</details>

<details>
<summary><b>Can I compare channels?</b></summary>

Yes, if the link was shared with labels such as utm_source. Each response carries its labels, so the skill splits leads by label and says where they are better in substance, not only in number.

</details>

<details>
<summary><b>Will it change my survey or show contacts in the chat?</b></summary>

No. The skill only reads the survey and its responses. It suggests changes, such as asking for the contact later or opening the phone question to every country, and contacts stay in your exports and integrations.

</details>

<details>
<summary><b>What do I need to use it?</b></summary>

A SurveyNinja account and an assistant that supports MCP and loads skills from a folder, such as Claude Code, Codex, Cursor or Gemini CLI. The MCP server works on every plan, the free one included. You connect with "Allow access" in the assistant or with your own API key.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
