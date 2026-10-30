# Integration failure reasons

Reference for the `surveyninja-integration-triage` skill.

## The `blocked` field in `get_quiz_integrations`

Given for Telegram, Zapier and Google Sheets. Entries for channels SurveyNinja does
not offer are ignored.

| Code | Meaning | Who fixes it |
|---|---|---|
| `blocked_by_tariff` | not included in the current plan | nobody from chat: state it and stop |
| `not_connected` | the survey has no connection to this channel | Telegram: from chat, `manage_quiz_messenger` `activate` gives the bot link for the person to add; Google Sheets and Zapier: the person, in the app |
| `disabled` | connected, sending switched off | can be switched on from chat, with consent |
| empty | settings are fine, look in the log | — |

## Telegram

The log from `get_integration_logs` (`integration` telegram) carries the refusal text
from Telegram.

| In the log | What happened | What to do |
|---|---|---|
| bot was blocked, bot is not a member | the bot was removed from the group or blocked in a private chat | add the bot back through the link from `manage_quiz_messenger` `activate`, then resend |
| user is deactivated | the person's Telegram account is gone | remove that recipient with "remove_recipient" |
| chat not found | the chat was deleted or turned into another one | add the bot to the new chat, remove the old recipient |
| message thread not found, topic closed | the forum topic in the group was closed or deleted | reopen the topic or pick another chat |
| not enough rights | the bot is in the group but is not allowed to post | the group admin gives the bot permission to send messages |
| too many requests, timeout, 5xx | a temporary failure on Telegram's side | nothing: these are retried automatically |

The last case matters: it is **not** a failure that needs work. The message is
retried on its own.

Resend with `resend_integration_logs` only after the cause is fixed.

## Google Sheets

`manage_quiz_google_sheets` with `show` gives the state.

| What `show` says | What happened | What to do |
|---|---|---|
| access is not alive | access to the Google account was revoked, or the table was deleted | the person reconnects the table in the app (it needs a Google sign-in), then `sync_now` |
| refresh mode `scheduled` | rows arrive once a day at the set time | explain; switch to `realtime` with "set_sync_mode" if the person wants |
| refresh mode `manual` | rows arrive only on command | explain; push with `sync_now` or switch the mode |
| a question is missing from the table | it is in the excluded list | "save_widgets" with the full list of exclusions |

"export_all" re-exports every answer into a new file, a new sheet, or over the
current sheet (`replace`). Ask which before running it.

## Zapier

`manage_quiz_zapier` with `show` gives the state and the number of subscribed zaps.

| What you see | What happened | What to do |
|---|---|---|
| sending off | switched off on the survey side | ask whether it was deliberate; `activate` with consent |
| zero zaps | the zap was deleted or turned off in Zapier | the person turns it on or rebuilds it in Zapier |
| sending on, zaps present, nothing arrives | the zap fails at a later step | the person opens the zap's run history in Zapier |

SurveyNinja keeps no Zapier delivery log, and there is no resend from the survey
side. Deleting the Zapier integration removes its subscriptions: never do it as a
"reset".

## Email notifications

| What `get_quiz_email_settings` shows | What happened | What to do |
|---|---|---|
| address not `checked` | the address was added but never confirmed | by API key: ask for the code from the letter, `confirm_quiz_email_recipient`, "resend_code" if it is lost; on "Allow access": the person clicks the red address on the survey's Notifications tab and enters the code there |
| address switched off | the recipient was turned off | ask, then `toggle_quiz_email_recipient` |
| owner letter off | notifications are switched off for the survey | ask, then `toggle_quiz_email` |
| everything on and confirmed | delivery works on our side | the person checks spam and mail filters |

## Webhooks

The cause shows in the receiver's response code in `get_quiz_webhook_logs`:

| Code | Meaning |
|---|---|
| 401, 403 | the receiver rejected authorisation: the key in the header changed |
| 404 | the address no longer exists |
| 5xx | a failure on the receiving side, worth resending after it is fixed |
| no response | the address is unreachable or too slow |

After a run of failures a webhook switches itself off; `get_quiz_webhooks` shows it.
Once the receiver is fixed, turn it back on with `toggle_quiz_webhook` and resend
with `resend_quiz_webhook_log`.
