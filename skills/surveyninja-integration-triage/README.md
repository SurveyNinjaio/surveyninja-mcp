<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Deliver responses</sub>

# Why responses are not delivered

**Finds why responses never reach your Telegram, Google Sheet, Zapier or webhook, and what to do about it**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-integration-triage` | 1.0.2 | 15 | [ZIP](https://surveyninja.io/skills/integration-triage.zip) | [surveyninja.io](https://surveyninja.io/skills/integration-triage) |

## What it does

1. **Goes from cheap to expensive.** It reads the integration state first, which covers most cases and costs nothing. Logs come next, and only if the reason is still unknown.
2. **Pulls the actual reason.** The bot was removed from the group, Google access was revoked, the zap was turned off, the receiver answers 500. The assistant names the cause in plain words.
3. **Tells a delay from a breakdown.** A Google Sheet set to refresh once a day is not broken. The assistant explains the refresh mode before anyone starts fixing things.
4. **Resends only after the fix.** A retry against a live failure repeats the same rejection and fills the log with noise. The cause gets fixed first, and the resend comes after.

## What you get

| Waiting to resend | Causes found | Fixed by you | Will resend |
|:-:|:-:|:-:|:-:|
| **148** | **3** | **2** | **148** |
| <sub>piled up over 6 days</sub> |  | <sub>need a sign-in</sub> | <sub>once the cause is gone</sub> |

| | | |
|---|---|---|
| **Telegram** | bot removed from the Leads group on 23 September |  |
| **Google Sheets** | access to the Google account revoked |  |
| **Zapier** | sending on, one zap subscribed |  |
| **Website webhook** | receiver answers 500 |  |
| **Email notifications** | recipient confirmed, delivery running |  |

> **The main cause: the bot was removed from the group**  
> Add the bot back to the Leads chat and the 148 waiting messages go out in one resend. Resending while the bot is outside the group just repeats the same rejection.

<sub>The states above are an example. The assistant checks the integrations of your own survey.</sub>

## How to ask

> Responses stopped arriving in our Google Sheet. Find out why

> Telegram notifications stopped coming. What happened?

> Check every integration on this survey and resend what piled up

## What not to do

- Do not suggest a plan upgrade or lead to payment
- Do not enable sending yourself
- Do not resend "just in case"
- Do not delete an integration to "reset" it

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `confirm_quiz_email_recipient` | Confirm recipient address | write |
| `get_integration_logs` | Messenger delivery log | read |
| `get_quiz_email_settings` | Quiz email settings | read |
| `get_quiz_integrations` | Quiz integration state | read |
| `get_quiz_list` | Quiz list | read |
| `get_quiz_webhook_logs` | Webhook delivery log | read |
| `get_quiz_webhooks` | Quiz webhooks | read |
| `manage_quiz_google_sheets` | Google Sheets export | destructive |
| `manage_quiz_messenger` | Telegram notifications | destructive |
| `manage_quiz_zapier` | Sending to Zapier | write |
| `resend_integration_logs` | Resend to messenger | write |
| `resend_quiz_webhook_log` | Resend webhook | write |
| `toggle_quiz_email` | Quiz emails on and off | write |
| `toggle_quiz_email_recipient` | Recipient on and off | write |
| `toggle_quiz_webhook` | Webhook on and off | write |

## Questions

<details>
<summary><b>Which channels does the skill check?</b></summary>

Email notifications, Telegram, Google Sheets, Zapier and webhooks.

</details>

<details>
<summary><b>Where does it start?</b></summary>

With the integration state of the survey. It already has a ready reason: not on the plan, not connected, or switched off. That covers most cases and costs nothing.

</details>

<details>
<summary><b>Where does it see the reason for a failure?</b></summary>

For Telegram, in the delivery log with Telegram's own refusal text. For webhooks, in the receiver's status code. For Google Sheets, in the table's state: whether access is alive and how often it refreshes. For Zapier, in whether sending is on and how many zaps are subscribed.

</details>

<details>
<summary><b>Will the responses that piled up be lost?</b></summary>

For Telegram and webhooks, no: once the cause is fixed, the skill resends them. A Google Sheet catches up with one sync. Resending earlier is pointless, because the same refusal repeats.

</details>

<details>
<summary><b>Will the skill connect or switch on an integration by itself?</b></summary>

Telegram it can connect from the chat if you agree: it returns a bot link, and you add the bot to your chat. Google Sheets and Zapier are connected in the app or in Zapier, and the assistant gives you the steps. Sending that was switched off it turns on only with your consent, because people often switch it off on purpose.

</details>

<details>
<summary><b>Will it ask for my system's keys?</b></summary>

No. Webhook header values are hidden behind asterisks, and the skill neither asks you to read them out nor offers to rewrite them as a test.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`references/reasons.md`](references/reasons.md): reference the skill reads when it needs it
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
