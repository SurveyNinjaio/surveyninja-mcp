<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Deliver responses</sub>

# New response notifications

**Sets up where new responses are announced, by email or in Telegram, and fixes it when they stop arriving**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-answer-notifications` | 1.1.0 | 11 | [ZIP](https://surveyninja.io/skills/answer-notifications.zip) | [surveyninja.io](https://surveyninja.io/skills/answer-notifications) |

## What it does

1. **Looks at what is already set.** Whether emails are on, who receives them, whether each address is confirmed and whether Telegram is connected. It checks before changing anything.
2. **Remembers address confirmation.** The most common cause of "we set it up and nothing arrives" is an address that was added but never confirmed. The setup looks complete either way.
3. **Keeps the message short.** A contact and two or three key answers beat the full questionnaire. Nobody reads a twenty-question email.
4. **Verifies with a test message.** Telegram can be checked right away instead of waiting for a live respondent. Adding the bot to your chat is one tap on a link, and the assistant gives you that link.

## What you get

| In the message | Recipients | Channels | Check |
|:-:|:-:|:-:|:-:|
| **3** | **2** | **2** | **test** |
| <sub>questions out of nine</sub> | <sub>one actually receives</sub> | <sub>email and Telegram</sub> | <sub>no waiting for a respondent</sub> |

| | | |
|---|---|---|
| **sales@example.com** | email, address confirmed, on |  |
| **marketing@example.com** | email, code sent but not confirmed |  |
| **Telegram, Leads group** | test message delivered |  |
| **Copy to the respondent** | off, as you asked |  |

> **The second address looks set up but receives nothing**  
> Until the address is confirmed with the code from the letter, nothing is sent to it. This is the most common reason notifications do not arrive.

<sub>The setup above is an example. The assistant reports the state of your own survey.</sub>

## How to ask

> Send me an email for every new response to this survey

> Send new responses to our Telegram group

> Notifications stopped arriving. Why?

## What not to do

- Do not enable notifications the person switched off deliberately
- Do not resend before the cause is fixed
- Do not add your own or a guessed address
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `add_quiz_email_recipient` | Add answer copy recipient | write |
| `delete_quiz_email_recipient` | Delete answer copy recipient | destructive |
| `get_integration_logs` | Messenger delivery log | read |
| `get_quiz_email_settings` | Quiz email settings | read |
| `get_quiz_integrations` | Quiz integration state | read |
| `manage_quiz_messenger` | Telegram notifications | destructive |
| `resend_integration_logs` | Resend to messenger | write |
| `save_quiz_email_template` | Quiz email template | write |
| `set_quiz_email_questions` | Questions included in the email | write |
| `toggle_quiz_email` | Quiz emails on and off | write |
| `toggle_quiz_email_recipient` | Recipient on and off | write |

## Questions

<details>
<summary><b>Where can I get notifications?</b></summary>

By email, as a letter with the response, and in a Telegram chat or group. The respondent can also get a copy of their answers by email.

</details>

<details>
<summary><b>Why do emails not arrive when everything looks set up?</b></summary>

Most often the address was never confirmed. A letter with a code goes to it, and nothing is sent until it is confirmed, even though the setting looks complete. The skill checks this first. Connected by API key, the assistant enters the code you give it. In assistant apps connected with Allow access, you enter it in the app: the survey's Notifications tab, click the address shown in red.

</details>

<details>
<summary><b>What goes into the message?</b></summary>

Not the whole questionnaire: a contact and two or three key answers are more useful. You decide which questions to include, and the skill sets the content and the subject.

</details>

<details>
<summary><b>How do I check without waiting for a response?</b></summary>

For Telegram, with a test message: the skill sends one to the chat right away.

</details>

<details>
<summary><b>Will the skill connect the bot to my chat?</b></summary>

It switches sending on and gives you a link. You open it and add the bot to your chat or group, which takes a tap and needs no tokens.

</details>

<details>
<summary><b>Notifications stopped. What happens next?</b></summary>

The skill checks whether sending was switched off or is not on your plan, reads the Telegram delivery log and finds the cause. Once the cause is fixed, it resends what piled up. It never turns notifications back on without asking you.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
