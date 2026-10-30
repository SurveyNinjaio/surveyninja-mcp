---
name: surveyninja-lead-quality
description: "Analyses the quality of leads collected by a SurveyNinja survey: how
  many respondents reached the contact question, how many left a usable email or
  phone number, where people drop off before the contact, and how leads differ by
  channel. Use when a survey works as a lead form, quote request or sign-up form
  and someone asks how many leads it brought, whether the contacts are any good,
  where leads are lost, or which channel brings better leads."
---

# Counting usable leads

When a survey works as a lead form, the completion rate says little. What matters
is how many people left a contact the team can actually reach.

Reply to the person in the language they write in.

## Collect

`get_quiz_structure`: find the contact questions (types `phone`, `email`, and
`fio` for the name) and the question right before the first of them.

`get_quiz_summary`: how many finished (`filled_completely`) and how many started
but left (`started_not_finished`). `get_quiz_report` counts the answers to each
question, but only among completed responses.

`get_quiz_answers` with `is_complete` false: the unfinished responses, paged with
`limit` and `offset`. They show who reached the contact question and left without
filling it. They are not kept on every plan (`incomplete_answers` in
`get_workspace_tariff`, with the `workspace_id` from `get_workspace_list`), and
without them `is_complete` false returns completed responses instead: check the
`is_complete` field. Then say that the drop-off before the contact cannot be
measured.

`get_quiz_report_inputs`: the values entered in the contact questions, to check
whether they are usable. It needs `report_uuid` from `get_quiz_report` and the
question's `widget_id` and `widget_hash` from `get_quiz_structure`, and returns 50
rows at a time: page with `offset`. Reading the completed responses with
`get_quiz_answers` page by page works too.

Link labels such as `utm_source`, if the link was shared per channel: each
response from `get_quiz_answers` carries them in `extra_fields`, and
`get_quiz_variables` lists the label names set up for the survey. Count leads per
label from the responses.

## Compute

1. **Share with a usable contact** out of everyone who started. This is the
   headline number. Completion can be high while leads are few.
2. **Where people drop off.** Among the unfinished responses, count those that
   answered the question before the contact but not the contact itself. They are
   the people who got there and changed their mind.
3. **Contact usability.** Count separately:
   - emails with a broken format, placeholder addresses (`test@test.com`,
     `a@a.com`, anything at `example.com`) and typos in big mail domains
     (`gmial.com`, `hotmial.com`);
   - phone numbers that cannot exist: fewer than 7 or more than 15 digits (the
     international maximum), one digit repeated, runs like `123456789`;
   - one-letter names and keyboard mash.

   A lead with a dead email or phone does not count as a lead.
4. **Duplicates.** The same email or phone several times is one lead.
5. **By channel**, if labels exist: leads and the usable share per label.

## What usually gets in the way

- **The contact is asked too early**, before the person sees what they get.
  Move it closer to the end.
- **Too much is asked.** Email, phone and city at once: every extra field costs
  leads. Ask for the one channel the team really uses.
- **No reason given.** One line such as "we will call to agree on a time" usually
  lifts the share more than any design change.
- **A phone question locked to one country.** When respondents come from several
  countries, a single default country with the selector hidden turns the others
  away. Suggest country auto-detection or showing the selector in the phone
  question settings.
- **A required contact in an otherwise optional survey**: people leave without
  answering anything.

## How to present

Numbers first: started, reached the contact question, left a contact, usable, and
usable as a share of those who started. Then where people drop off and what to
change, ordered by payoff.

With channels, a table plus a conclusion about which channel brings better leads
in substance, since the biggest channel is often not the best one.

## What not to do

- **Do not count a submission without a contact as a lead.**
- **Do not paste contacts into the chat**: they belong in an export or in the
  connected Google Sheets, Zapier or webhook.
- **Do not advise removing every required field**: a lead without a contact is
  useless.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.
