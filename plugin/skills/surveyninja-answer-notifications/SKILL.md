---
name: surveyninja-answer-notifications
description: "Sets up and repairs notifications about new responses to a SurveyNinja
  survey: emails to the team, a copy of the answers to the respondent, and messages
  in a Telegram chat or group. Use when someone wants new responses delivered to
  their inbox or Telegram, wants to add or remove a recipient, change what the
  notification contains, or asks why notifications stopped arriving."
---

# Where new responses are announced

The most common setting in a survey and the most common cause of "responses are
coming in and nobody knows".

Reply to the person in the language they write in; write email subjects and texts
in the language of the people who will read them.

## 1. See what is already set

`get_quiz_email_settings` shows whether survey emails are on, who receives them,
whether each address is confirmed (the `checked` field) and the letter templates.

`get_quiz_integrations` shows whether Telegram is connected, switched on and
allowed by the plan. The response also lists channels SurveyNinja does not offer;
ignore them.

## 2. Email

- Turn the team notification on with `toggle_quiz_email` (`type` owner). The copy
  of the answers to the respondent is `type` client; it is not available on every
  plan, and the respondent's address comes from an email question or a variable
  set as `client_source` in `save_quiz_email_template`.
- Add a recipient with `add_quiz_email_recipient`. The number of addresses depends
  on the plan.
- **The address must be confirmed.** A letter with a 4-digit code goes to it, and
  until it is confirmed nothing is delivered there, while the setting still looks
  complete. This is the single most common cause of "we set it up and get nothing".
  You cannot read that mailbox. An address already confirmed in another survey of
  the workspace needs no code.
  - Connected by API key: ask the person for the code and confirm with
    `confirm_quiz_email_recipient`; its "resend_code" action sends a new one.
  - Connected with "Allow access" (the sign-in Claude, ChatGPT and other assistant
    apps use), that tool is not offered, so that text in a respondent's answer
    cannot add someone else's address as a recipient. The person enters the code in
    the app: the survey's Notifications tab, Added addresses, click the address
    shown in red. A new code is there too, under "get the code again". Do not ask
    for the code in the chat then: you have nowhere to enter it.
- Switch one address on or off with `toggle_quiz_email_recipient`; remove one with
  `delete_quiz_email_recipient`.
- What goes into the letter: `set_quiz_email_questions` lists the questions to
  leave out (the full list each time; an empty list brings every question back),
  and `save_quiz_email_template` sets the subject and text.

Do not put every question into the email when there are many: the contact and two
or three key answers are more useful than the whole questionnaire.

## 3. Telegram

`manage_quiz_messenger` with `messenger` telegram. `show` lists the chats and
people the messages go to, the subject and the excluded questions.

- `activate` switches sending on and returns a bot link. The person opens it and
  adds the bot to their chat or group; you cannot do that step for them, so give
  the link and the steps. No tokens are needed.
- "save_widgets" sets the subject and the questions to leave out of the message.
- `test` sends a test message. It is the best way to verify the setup without
  waiting for a live respondent.
- "remove_recipient" removes one chat; `deactivate` stops sending; `delete` removes
  the integration.

If Telegram is not on the person's plan, the tool says so: state it and stop.

## If it stopped working

1. `get_quiz_integrations`: is Telegram switched off, not connected, or blocked by
   the plan?
2. For Telegram, `get_integration_logs` with `integration` telegram. The rejection
   text is there (bot removed from the group, chat deleted) together with the count
   of unsent messages.
3. For email, check that the address is confirmed and switched on in
   `get_quiz_email_settings`, and ask the person to look in their spam folder.
4. Once the cause is fixed, `resend_integration_logs` sends the Telegram backlog:
   one entry by `log_id`, or every failed one over a period. Resending earlier is
   pointless: the same rejection repeats.

## What not to do

- **Do not enable notifications the person switched off deliberately.** Ask first.
- **Do not resend before the cause is fixed.**
- **Do not add your own or a guessed address.** Only the one the person gave.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.
