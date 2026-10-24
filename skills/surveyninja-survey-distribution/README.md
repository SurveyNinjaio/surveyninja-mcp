<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Build and share</sub>

# Distribute the survey

**Gets the survey ready to hand out so you can still tell which channel each response came from**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-survey-distribution` | 1.0.2 | 10 | [ZIP](https://surveyninja.io/skills/survey-distribution.zip) | [surveyninja.io](https://surveyninja.io/skills/survey-distribution) |

## What it does

1. **Starts with channel labels.** One survey, several places. Without labels the responses merge into one pile, so the labels are agreed before the send-out, not after.
2. **Gives one link per channel.** Newsletter, social posts, WhatsApp group, website banner: each gets its own link with a readable label instead of utm1 and utm2 that nobody can decode a month later.
3. **Covers print.** A QR code in PNG, SVG or EPS with your colors for a sticker, a slide or a flyer, checked before the print run. A printable version in PDF or Word when the survey is filled in on paper.
4. **Restricts access when needed.** Passwords in batches of up to fifty, different ones for different groups, or a separate link for each branch or partner.

## What you get

**Distribution, 4 channels**

| Address | Labels | Passwords | Print |
|:-:|:-:|:-:|:-:|
| **custom** | **4** | **20** | **PDF** |
| <sub>short and readable</sub> | <sub>one per channel</sub> | <sub>if the survey is private</sub> | <sub>also Word, HTML, text</sub> |

| | | |
|---|---|---|
| **Newsletter** | label newsletter | link |
| **WhatsApp group** | label whatsapp | link |
| **Website banner** | label site-banner | link |
| **Counter in the store** | label print-qr · QR 600 px | QR code |

> **The address of a survey already sent out stays put**  
> SurveyNinja redirects an old address to the new one, but printed codes and sent links then rely on that redirect. If the address really has to change, the assistant warns you before touching it.

<sub>The labels and numbers above are an example. Names are chosen to match your channels.</sub>

## How to ask

> How do I send this survey to several channels and tell them apart later?

> Make a QR code for the survey to put on the counter

> I need a private survey with passwords for twenty people

## What not to do

- Do not publish the survey unasked
- Do not change the address of a survey already sent out
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `create_quiz_variable` | Create quiz variable | write |
| `export_quiz_print` | Quiz print version | read |
| `get_quiz_answers` | Quiz answers | read |
| `get_quiz_variables` | Quiz variables | read |
| `get_quiz_versions` | Quiz publication history | read |
| `manage_quiz_passwords` | Passwords for a closed quiz | destructive |
| `manage_quiz_qr_code` | Quiz QR code | write |
| `manage_quiz_unique_links` | Unique quiz links | destructive |
| `set_quiz_link` | Quiz link address | write |
| `update_quiz_settings` | Quiz settings | write |

## Questions

<details>
<summary><b>How will I know where the responses came from?</b></summary>

From channel labels. Each channel gets a link with its own label, the label is saved with every answer, and the responses can be split by it later. Labels are saved on any plan.

</details>

<details>
<summary><b>Can labels be added after the send-out?</b></summary>

Not to responses that already came in. That is why the skill suggests labels up front, for the channels you name.

</details>

<details>
<summary><b>Can I change the survey address?</b></summary>

Yes, where your plan allows a custom address. SurveyNinja redirects the old address to the new one until another survey takes it. For a survey already sent out, the skill warns you before the change.

</details>

<details>
<summary><b>What kind of QR code can I get?</b></summary>

A code for a sticker, a slide or a flyer in PNG, SVG or EPS, with your choice of size, color and background. A logo in the centre is uploaded in the app. The code leads to the plain survey address, without a channel label. Check where it leads before a print run.

</details>

<details>
<summary><b>How do I make a survey private?</b></summary>

The skill adds passwords in batches of up to fifty, different ones for different groups, and gives you the list right away because passwords cannot be read back later. Another option is a separate link for each branch or partner, where your plan allows it.

</details>

<details>
<summary><b>What do I need for this skill to work?</b></summary>

A SurveyNinja account on any plan, including Free, and an AI assistant that supports MCP and loads skills from a folder, such as Claude Code, Codex, Cursor or Gemini CLI. The skill is a plain text file; the assistant works through your API key or the access you allow when connecting.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
