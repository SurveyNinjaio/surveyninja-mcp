---
name: surveyninja-prelaunch-check
description: "Checks a SurveyNinja survey before launch and finds what will break on
  live respondents: dead ends in the logic, unreachable questions, empty texts,
  responses that reach nobody, limits that are about to run out. Use when someone
  is about to publish a survey, send out the link or put a survey on their site,
  or asks whether everything is ready."
---

# Checking a survey before launch

Survey mistakes surface after the link goes out, when part of the responses are
already collected through a broken questionnaire and cannot be compared with
anything.

Reply to the person in the language they write in.

## Order

Read `get_quiz_structure` (questions, their logic, and the headings and texts of
the welcome and thank-you screens), `get_quiz_texts` (interface and button labels)
and `get_quiz_list` (the survey type, whether it is published and at what
address), then walk the list below. Fix nothing silently: show the findings first,
then ask what to repair.

## What to check

**Branching**

- Dead ends: a branch with no way forward and no way to finish.
- Unreachable questions: nothing routes to them.
- Conditions pointing at deleted or renamed questions.
- An operator that does not fit the question type, such as "greater than" on a
  text field.

**Questions**

- A choice question with no options.
- Required questions that do not need to be required: each one costs responses.
- Open text where a count is needed: a rating typed as text never reaches the
  charts in the report.
- Excessive length: if there are more than fifteen questions, say so plainly.

**Texts**

- Empty headings, default button labels, an empty text on a thank-you screen
  that exists.
- No `finish` screen is not a defect: the respondent then sees the standard
  completion screen, and the Thank You screen depends on the plan. Mention it only
  if the survey needs its own final message, such as a promised next step.

**Where the answers will go**

- `get_quiz_email_settings`: are notifications on, are recipients set, and **are
  their addresses confirmed** (the `checked` field). An unconfirmed address looks
  configured but receives nothing.
- `get_quiz_integrations`: is Telegram, Zapier or Google Sheets connected, is
  sending on, and does the plan allow it.
- `get_quiz_webhooks`: if there are webhooks, are they on, and was one switched
  off automatically after failed deliveries.
- A survey with no notifications and no integrations collects responses in
  silence. That can be fine if the person reads the report, but say it.

**Plan and access**

- `get_workspace_tariff`: how many responses, surveys and storage remain, and
  whether the features the survey relies on are included.
- A regular survey: is it published and reachable by its link.
- An on-site survey (type `micro`) has no link of its own: `get_quiz_summary`
  shows `is_connected`. If it is false, the survey is not on any site yet and
  nobody will see it.

## What not to do

- **Do not fix silently.** List the findings and let the person decide.
- **Do not publish on your own initiative.**
- **Do not rewrite question wording.** That is separate work.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit or a
  feature is not on the plan, state the fact and stop.

## What to say at the end

Findings ordered by weight: what will break collection, what will degrade data
quality, what is merely worth improving. If everything is clean, say so and do
not invent remarks.
