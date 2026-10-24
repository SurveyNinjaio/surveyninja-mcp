---
name: surveyninja-integration-triage
description: "Finds why responses to a SurveyNinja survey do not reach an external
  system, and fixes it. Use when someone reports that responses or leads are not
  arriving in Telegram, rows are not added to a Google Sheet, a Zap in Zapier does
  not trigger, a webhook to their CRM or app does not fire, or email notifications
  stopped, and when they ask to check every integration of a survey and resend what
  piled up."
---

# Why responses are not leaving the survey

A silent integration has several different causes, each with a different fix. Work
strictly in order: every next step costs more than the previous one.

Reply to the person in the language they write in.

Reasons and log messages are collected in [references/reasons.md](references/reasons.md).

## 1. Get the survey id

Nothing can be done without it. If the survey was named in words, find it with
`get_quiz_list` and confirm it is the right one before changing anything.

## 2. Read the state: `get_quiz_integrations`

It returns Telegram, Zapier and Google Sheets with a ready-made reason in the
`blocked` field. This covers most requests and costs nothing. The response also
lists channels SurveyNinja does not offer; ignore them.

| Reason | Meaning | What to do |
|---|---|---|
| `blocked_by_tariff` | not included in the plan | state it plainly and stop, see the rule below |
| `not_connected` | no connection at all | Telegram: offer `manage_quiz_messenger` `activate`, which returns the bot link the person adds to their chat; Google Sheets and Zapier connect in the app: give the steps |
| `disabled` | connected, sending switched off | ask whether that was deliberate; enable only with consent |
| empty | settings are fine | go to step 3 |

Email notifications and webhooks are not in this response. They have their own
checks, see steps 5 and 6.

## 3. Find the refusal

Each channel shows its cause in a different place.

**Telegram**: `get_integration_logs` with `integration` telegram. The refusal text
is there (bot removed from the group, chat deleted, topic closed), and the unsent
counter shows how much is waiting.

**Google Sheets**: `manage_quiz_google_sheets` with the `show` action. It shows
whether access to the Google account is alive, the refresh mode and when the last
export happened. Two common causes:

- access to the Google account was revoked, or the table was deleted: the person
  reconnects the table in the app, because that needs a Google sign-in;
- nothing is broken, the refresh mode is `scheduled` (once a day) or `manual`, so
  rows appear later or only on command. Explain it and ask whether to switch to
  `realtime` with "set_sync_mode".

**Zapier**: `manage_quiz_zapier` with the `show` action. It shows whether sending is
on and how many zaps are subscribed. Zero zaps means the zap was deleted or turned
off on the Zapier side. SurveyNinja keeps no log of what Zapier did next: the run
history is in the person's Zapier account, under the zap's history.

## 4. Resend only after the cause is fixed

- Telegram: `resend_integration_logs`, one entry by `log_id` or every failure over a
  period.
- Google Sheets: `manage_quiz_google_sheets` with `sync_now` pushes what piled up.
  "export_all" re-exports every answer; ask where to (a new file, a new sheet, or
  `replace`, which overwrites the current sheet) before running it.
- Zapier: once the zap is back on in Zapier, new responses flow again. There is no
  resend from the survey side.

Resending while the cause is alive is pointless: the same refusal repeats and the
log fills with noise. The person fixes their side first: returns the bot to the
group, restores access to the table, turns the zap back on.

## 5. Email notifications

`get_quiz_email_settings`: is the notification on, is each address confirmed (the
`checked` field) and switched on. An address that was added but never confirmed
receives nothing, while the settings look complete. That is the most common cause:
ask the person for the code from the letter and confirm it with
`confirm_quiz_email_recipient`. A recipient or the whole notification switched off
is turned back on with `toggle_quiz_email_recipient` or `toggle_quiz_email`, after
asking. If everything is confirmed and on, ask the person to check their spam
folder.

## 6. Webhooks separately

`get_quiz_webhooks` lists the webhooks, whether each is on, and whether one switched
itself off after a run of failed deliveries. `get_quiz_webhook_logs` is the delivery
log with the receiver's response code. `resend_quiz_webhook_log` resends after the
receiver is fixed, and `toggle_quiz_webhook` turns a self-disabled webhook back on.

Header values in responses are masked: they hold access keys to someone else's
system. Do not ask the person to read them out, and do not offer to rewrite headers
"to test": passing `headers` to an update replaces the whole list.

## What to say at the end

Three things: which channel is silent, for what exact reason, and what the person
needs to do. If the cause was fixed and the backlog resent, say how many went out.

## What not to do

- **Do not suggest a plan upgrade or lead to payment.** When the plan blocks a
  channel, name the reason and stop.
- **Do not enable sending yourself.** A disabled integration is often disabled on
  purpose.
- **Do not resend "just in case".** See step 4.
- **Do not delete an integration to "reset" it.** Deleting Zapier removes its
  subscriptions, and the zap has to be rebuilt in Zapier; deleting a webhook loses
  its headers and log.
