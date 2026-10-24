<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Build and share</sub>

# Launch kit

**Puts the whole launch together at once: labeled links, announcement copy for each channel and a QR code**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-launch-kit` | 1.1.1 | 9 | [ZIP](https://surveyninja.io/skills/launch-kit.zip) | [surveyninja.io](https://surveyninja.io/skills/launch-kit) |

## What it does

1. **Starts from the channels.** Email, website, social posts, WhatsApp or Telegram, print. Each gets its own labeled link, otherwise there is no way to tell later what worked.
2. **Writes copy for each channel.** An email subject that does not open with the word "survey", one or two sentences for a post, a short message for a chat and five words for a banner. One rule for all: why it matters and how long it takes.
3. **Does not oversell.** No "takes a minute" for a fifteen-question survey and no invented figures in the announcement.
4. **Checks where responses land.** Before the send-out, not after. If notifications are not set up, the assistant offers to set them up while the link is still unsent.

## What you get for the launch

**Launch kit, 4 channels**

| | | |
|---|---|---|
| **"Three questions about your visit"** | newsletter · subject, two lines and a button | email-oct |
| **"Were you with us this week? Tell us how it went, it takes 2 minutes"** | WhatsApp group · one line and the link | whatsapp-group |
| **"How was your visit?"** | website banner · five words | site-banner |
| **QR code for the counter** | print · PNG 600 px | plain link |

> **Before you send: nobody is notified yet**  
> Responses are saved in the account, but the survey has no email notification and no integrations. Worth setting up now, otherwise the first responses arrive without anyone noticing.

<sub>The copy and labels above are an example. Announcements are written for your audience and your channels.</sub>

## How to ask

> Prepare everything for the launch: links, copy and a QR code

> Write the survey announcement for our newsletter and for WhatsApp

> We are launching in three channels, make a labeled link for each

## What not to do

- Do not send anything yourself
- Do not publish the survey unasked
- Do not invent figures
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_email_settings` | Quiz email settings | read |
| `get_quiz_integrations` | Quiz integration state | read |
| `get_quiz_variables` | Quiz variables | read |
| `get_quiz_versions` | Quiz publication history | read |
| `get_quiz_webhooks` | Quiz webhooks | read |
| `manage_quiz_analytics` | Analytics counters and pixels | write |
| `manage_quiz_messenger` | Telegram notifications | destructive |
| `manage_quiz_qr_code` | Quiz QR code | write |
| `set_quiz_link` | Quiz link address | write |

## Questions

<details>
<summary><b>What will the skill prepare?</b></summary>

A labeled link for each channel, announcement copy for email, social posts, WhatsApp or Telegram messages and a website banner, and a QR code for print, which is worth checking before a print run.

</details>

<details>
<summary><b>Why a separate link for each channel?</b></summary>

So you can tell later what worked. The label travels in the link and is saved with each response, so responses can be counted by channel. Splitting the report itself by label in Results uses report filters, which depend on the plan. The QR code always carries the plain survey link, without a label.

</details>

<details>
<summary><b>What will the announcement say?</b></summary>

Each channel gets its own text, all built on one rule: why it matters to the reader, how long it takes and what happens next. A banner gets five words at most.

</details>

<details>
<summary><b>Will it write "takes a minute" to get more responses?</b></summary>

No. For a fifteen-question survey that only leads to incomplete responses. It also does not promise rewards that do not exist or invent figures.

</details>

<details>
<summary><b>Will the skill send the announcement for me?</b></summary>

No. It prepares the material and you do the sending. It does not publish the survey without asking either.

</details>

<details>
<summary><b>What do I need for this skill to work?</b></summary>

A SurveyNinja account on any plan, including Free, a survey ready to launch, and an AI assistant that supports MCP and loads skills from a folder, such as Claude Code, Codex, Cursor or Gemini CLI. The skill is a plain text file; the assistant works through your API key or the access you allow when connecting.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
