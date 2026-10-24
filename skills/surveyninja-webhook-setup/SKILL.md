---
name: surveyninja-webhook-setup
description: "Sets up delivery of SurveyNinja survey responses to an external URL via
  webhook: address, method, which fields and under which names, headers, whether
  to send unfinished responses and with what delay. Use when someone asks to send
  responses to their own server, app or CRM, to Make or n8n, to rename or change
  webhook fields, to check whether a webhook delivers, or to turn a webhook on or
  off."
---

# Webhook: responses to your own address

A webhook is the most direct way to get responses into your own system: every
response goes out as an HTTP request to the given address. It is quick to set up and
quiet when it breaks, so order matters more than speed here.

Reply to the person in the language they write in.

## 1. Check that webhooks are available

`get_workspace_tariff` (the `workspace_id` comes from `get_workspace_list`):
webhooks are not part of every plan. If they are not available, say so right away
and stop. Creating and switching on a webhook check the plan too, but collecting
the address, method, fields and headers only to hit a refusal at the last step
wastes the conversation.

If the target is Zapier, a webhook is not needed: SurveyNinja has a Zapier
integration. The zap is built in Zapier, and `manage_quiz_zapier` shows whether
sending is on and switches it.

## 2. See what already exists

`get_quiz_webhooks` lists the survey's webhooks, whether each is on, and whether one
switched itself off after a run of failed deliveries. A second webhook to the same
address is almost always a mistake, not a wish: check before creating.

## 3. Find out four things

Nothing can be created without them:

| What | Why |
|---|---|
| **Address** | where to send; a public `http` or `https` address (internal addresses are rejected), and the receiver must answer 2xx |
| **Method** | `post` almost always; `get`, `put`, `patch` if the receiver demands it |
| **Which fields** | a contact and two or three key answers beat the whole questionnaire and are easier for the receiver |
| **Field names** | if the system expects `phone` and the question is "Your phone", rename it with `body_naming` |

Question names and identifiers come from `get_quiz_structure`.

## 4. Create and switch on

`create_quiz_webhook`: a title (for the person, to tell webhooks apart), address,
method, fields (`body`), renaming (`body_naming`) and headers (`headers`, where the
receiver's access keys go).

**Unfinished responses**: `incomplete` and `hours`. By default only finished ones
are sent. If abandoned ones are wanted too, send them with a delay of 1, 6, 12 or 24
hours; otherwise a person who comes back to finish arrives twice.

**A new webhook is created switched off.** Tell the person, and once they confirm
the receiver is ready, turn it on with `toggle_quiz_webhook`.

## 5. Verify delivery

After the first response, read `get_quiz_webhook_logs`: the receiver's response code
and body. `200` means it works. `4xx` means the receiver rejected it, usually because
of the address, the method or the body format. `5xx` is an error on their side. An
empty log means no responses yet, which is not an error.

Do not resend with `resend_quiz_webhook_log` while the receiver answers with an
error: the same thing will happen again. Once it is fixed, resend one entry by
`log_id` or every entry over a period.

## Change, disable, delete

- Fix the address or fields with `update_quiz_webhook`. Fields you do not pass keep
  their values, so send only what changes. **`headers` is replaced as a whole
  list**, and header values come back masked: to change one header, ask the person
  for the others again, or leave `headers` out entirely.
- A webhook that switched itself off after failures comes back on with
  `toggle_quiz_webhook`, once the receiver is fixed.
- To pause while they fix their side, switch it off with `toggle_quiz_webhook`
  rather than deleting it.
- Delete with `delete_quiz_webhook` only on a direct request: the settings, headers
  and delivery log are gone for good.

## What not to do

- **Do not create a second webhook to the same address** without asking.
- **Do not send every question** when there are many. The receiver needs the right
  fields.
- **Do not ask the person to dictate access keys into the chat.** Ask them to put
  the keys into the webhook headers in the app, or insert only what they sent
  themselves.
- **Do not enable a webhook that was disabled on purpose.**
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.
