---
name: surveyninja-survey-copy
description: "Rewrites the copy of a SurveyNinja survey so that people finish it:
  question wording, button labels, welcome and thank-you screens. Use when someone
  asks to improve a survey, make it clearer or friendlier, or complains that people
  start it and do not complete it."
---

# Rewriting so people finish

People rarely abandon a survey because it is long. They abandon it at the question
where they stop seeing what is in it for them. Fixing the copy often helps more
than cutting questions.

Reply to the person in the language they write in. Write the survey copy in the
language of its audience.

## Start from data, not taste

`get_quiz_answers` with `is_complete` set to false lists unfinished responses,
up to 100 per page (page with `offset`): note the last question each one answered
and find where most of them stop. The report does not show this: it holds
completed responses only. Fix those questions first, not the ones that merely
look wrong.

Incomplete responses are not saved on every plan, and then the same call quietly
returns completed ones: check `is_complete` on each response. If there are no
unfinished ones, say why: either there are no responses yet or the plan does not
keep unfinished ones. Then edit by general rules and suggest looking at behavior
once responses come in.

Question wording, the welcome and thank-you screens are widget fields: read them
with `get_quiz_structure`, write them with `update_quiz_widgets`. Button labels
and other interface strings come from `get_quiz_texts` and are saved by their
`code` with `update_quiz_texts`.

## What to fix

| Problem | How it looks | Better |
|---|---|---|
| Formal, bureaucratic tone | "Please rate your level of satisfaction with the services rendered" | "How happy are you with the work?" |
| Double question | "Were the price and the timing right?" | two separate questions |
| Double negative | "Do you disagree that we should not…" | a direct question |
| Internal jargon | "Rate the front office" | "Rate the staff at the front desk" |
| Leading question | "How much did you enjoy our excellent service?" | "How was our service?" |
| Question without bounds | "How often do you visit?" as open text | options: weekly, monthly, less often |

## The first screen

This is where most people are lost. It needs three things: **what is being asked**,
**how long it takes**, and **why the person should care**. The last one is usually
missing, and it is the one that decides.

"Customer satisfaction survey" is weak. "Three questions about your visit. Your
answers help us cut waiting times" works.

## Buttons and thank-you

Default labels work, but a human label on the last step helps completion. The
thank-you screen is the place to say what happens next ("We read every answer this
week").

## Order of work

1. Show the proposed edits: before and after, question by question.
2. Wait for agreement.
3. Write.
4. Widget edits land in the draft: respondents see them only after
   `publish_quiz`. Ask before publishing. Interface strings saved with
   `update_quiz_texts` reach the live survey at once.

Do not rewrite everything silently: copy is often agreed with a client or a legal
team.

## What not to do

- **Do not change the meaning of a question** for the sake of nicer wording:
  comparability with earlier responses breaks.
- **Do not edit copy of a survey already collecting responses without warning**:
  answers before and after the edit stop being comparable.
- **Do not add or remove questions.** That is different work.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.
