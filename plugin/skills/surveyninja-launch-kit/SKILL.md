---
name: surveyninja-launch-kit
description: "Prepares launch material for a SurveyNinja survey: announcement copy
  for email, social posts, WhatsApp or Telegram messages and a website banner, one
  labeled link per channel, and a QR code for print. Use when someone is about to
  send out a survey and asks how to present it, what to write, or how to tell later
  which channel brought the responses."
---

# Launch material

The survey is ready but still has to reach people. That is usually done by hand in
several places at once. Prepare it all in one go.

Reply to the person in the language they write in. Write the announcement copy in
the language of the survey's audience.

## 1. Establish the channels

Ask where it goes: an email list, the website, social posts, WhatsApp or Telegram
chats and groups, print. Each channel gets its own labeled link, otherwise there
is no way to tell what worked.

## 2. Links with labels

Check the survey is published (`get_quiz_versions` shows the publication history).
An unpublished survey does not open by its link, and the send-out goes nowhere.

A label is a parameter added to the survey link, for example
`?source=email-oct` or `?source=whatsapp`. SurveyNinja saves the link's
parameters with each response (its hidden values in Results), so responses can
later be counted per channel. Splitting the report by label in Results uses the
report filters, which depend on the plan; without them the count per label is
still taken from the responses.

Name labels readably: `email-oct`, `instagram`, `whatsapp-group`, `site-banner`,
not `utm1` and `utm2`. Nobody remembers what those meant a month later. If the
person already uses `utm_source` and `utm_campaign`, keep their convention;
`get_quiz_variables` shows the names already set up for the survey.

`set_quiz_link` changes the address itself to something short and readable. It is
optional and not on every plan.

For the website, the embed code (frame, pop-up, side widget or button) is copied
from the survey's share section in SurveyNinja. There is no tool for it: tell the
person where to find it and which label to put in the link.

## 3. Announcement copy

One per channel, all following one rule: **why it matters to the reader, how long
it takes, what happens next**.

- **Email.** A subject line that does not start with the word "survey", such as
  "Three questions about your visit". Two or three lines and a button in the body.
- **Social posts.** One or two sentences and the link. Reader benefit first.
- **WhatsApp or Telegram message.** One short line that reads like a person wrote
  it, and the link.
- **Website banner.** Five words at most.

Do not promise a reward that does not exist, and do not understate the time:
"takes a minute" for a fifteen-question survey buys abandonment and irritation.

## 4. Print

`manage_quiz_qr_code` builds a code from the published survey link. It always
encodes that plain link and takes no parameters, so the code cannot carry a label
and responses from print arrive unlabeled: say so. Verify the code opens the
right page before printing a run. A logo in the centre is uploaded in the app; an
already uploaded one is included.

## 5. Tracking, if they use it

If the person tracks campaigns in Google Analytics or runs Meta ads,
`manage_quiz_analytics` connects a Google Analytics counter or a Meta Pixel to the
survey. Only offer it when they mention it.

## 6. Last thing to say

Where the responses will land: are notifications set up? Check with
`get_quiz_email_settings`, `get_quiz_integrations` and `get_quiz_webhooks`. If
nothing is set up, offer to do it before the send-out, not after: an email
notification, or a Telegram message with `manage_quiz_messenger`.

## What not to do

- **Do not send anything yourself.** This prepares material; the person launches.
- **Do not publish the survey unasked.**
- **Do not invent figures** for the announcement.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.
