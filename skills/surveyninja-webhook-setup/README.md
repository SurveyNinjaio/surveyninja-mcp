<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Deliver responses</sub>

# Webhook setup

**Sends survey responses to your own address and checks that the receiver accepted them**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-webhook-setup` | 1.1.0 | 9 | [ZIP](https://surveyninja.io/skills/webhook-setup.zip) | [surveyninja.io](https://surveyninja.io/skills/webhook-setup) |

## What it does

1. **Looks at what is already set up.** A second webhook to the same address is almost always a mistake. The assistant checks the list before creating anything.
2. **Asks the four things nothing works without.** The address, the method, which fields to send and what to call them. Field names match your system through renaming.
3. **Careful with incomplete responses.** If you want incomplete responses too, they go out with a delay. Otherwise a person who comes back to finish arrives twice.
4. **Reads the delivery log.** 200 means it works, 4xx means the receiver rejected the request, 5xx is an error on their side. Nothing is resent while the receiver keeps failing.

## What you get

| Fields | Unfinished | Deliveries | Errors |
|:-:|:-:|:-:|:-:|
| **3** | **no** | **47** | **0** |
| <sub>of nine questions</sub> |  | <sub>this week</sub> |  |

| | | |
|---|---|---|
| **https://crm.example.com/hooks/survey** | post, finished responses, switched on |  |
| **phone ← Your phone** | field renamed |  |
| **rating ← How happy are you?** | field renamed |  |
| **Authorization: ***** | header, value hidden |  |
| **Last delivery** | 30 September 14:02, receiver answered 200 |  |

> **The receiver accepted the first response with code 200**  
> The webhook works. If the receiver starts answering 4xx, the assistant will not resend blindly. The cause gets fixed first, and the resend comes after.

<sub>The address and fields above are an example. The setup is built for your system.</sub>

## How to ask

> Set up a webhook to send responses to our server

> Send the phone from the survey to our CRM as a field called phone

> Check whether responses are arriving through the webhook

## What not to do

- Do not create a second webhook to the same address
- Do not send every question
- Do not ask the person to dictate access keys into the chat
- Do not enable a webhook that was disabled on purpose
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `delete_quiz_webhook` | Delete webhook | destructive |
| `get_quiz_structure` | Quiz structure | read |
| `get_quiz_webhook_logs` | Webhook delivery log | read |
| `get_quiz_webhooks` | Quiz webhooks | read |
| `get_workspace_list` | Workspace list | read |
| `get_workspace_tariff` | Workspace plan | read |
| `manage_quiz_zapier` | Sending to Zapier | write |
| `resend_quiz_webhook_log` | Resend webhook | write |
| `toggle_quiz_webhook` | Webhook on and off | write |

## Questions

<details>
<summary><b>Are webhooks available on my plan?</b></summary>

The skill checks this first, because webhooks are not on every plan. If they are not available, it tells you right away and stops.

</details>

<details>
<summary><b>What do I need to tell it, and who creates the webhook?</b></summary>

Four things: the address (a public http or https one), the method (almost always POST), which fields to send and what your system calls them. Connected by API key, the assistant creates the webhook. In Claude, ChatGPT and other assistant apps connected with Allow access, you create it in the app from the values the skill prepares, and the skill takes it from there.

</details>

<details>
<summary><b>Can fields be named the way my system expects?</b></summary>

Yes. If your system expects phone and the question is called Your phone, the skill renames the field in the payload. The question in the survey stays as it is.

</details>

<details>
<summary><b>Will incomplete responses be sent?</b></summary>

By default only finished ones are sent. If you want abandoned ones too, the skill sends them with a delay of 1, 6, 12 or 24 hours, so a person who comes back to finish does not arrive twice.

</details>

<details>
<summary><b>How do I know the webhook works?</b></summary>

A new webhook starts switched off, and the skill turns it on when you confirm the receiver is ready. After the first response it reads the delivery log: 200 means it works, 4xx means the receiver rejected the request, 5xx is an error on their side. An empty log means there were no responses yet.

</details>

<details>
<summary><b>How do I pass an access key for my system?</b></summary>

Do not paste it into the chat. Put keys into the webhook headers in the app. The assistant only sees header values hidden behind asterisks.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
