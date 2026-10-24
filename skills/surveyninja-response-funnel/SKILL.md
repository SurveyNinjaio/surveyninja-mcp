---
name: surveyninja-response-funnel
description: "Works out where respondents abandon a SurveyNinja survey and explains
  why. Use when someone complains about few responses, low completion, many
  incomplete responses, asks why people do not finish the survey, or wants to know
  which question makes respondents leave."
---

# Where the survey is abandoned

"Few responses" rarely means few people arrived. Usually one specific question is
where people close the tab.

Reply to the person in the language they write in.

## Build the picture

1. `get_quiz_summary` — how many finished (`filled_completely`) and how many
   started but left (`started_not_finished`).
2. `get_quiz_answers` with `is_complete` false — the unfinished responses, paged
   with `limit` and `offset`. Each lists every question in order; the last one
   with an answer is where that person stopped. The report will not do: it holds
   only completed responses.
3. `get_quiz_structure` — question order and types, to tie a position to content.

Compute the completion share and, from the unfinished responses, how many people
stopped at each question: the question where most of them stop is where the drop
happens.

**If unfinished responses are not kept.** They are not part of every plan:
`incomplete_answers` in `get_workspace_tariff` (it needs the `workspace_id` from
`get_workspace_list`) tells whether they are. Without them `is_complete` false
returns completed responses instead, so check the `is_complete` field of what
comes back. When they are not available, say so plainly: there is nothing to
compute the drop-off point from. What is left is the completion share from
`get_quiz_summary` and a reading of the survey itself: length, order, required
questions. That is weaker, and the person should be told, not handed a guess
dressed up as a measurement.

## Reading it

- **A steady decline of a few percent** from question to question is normal.
- **A cliff at one question** is the problem. Look at it closely.
- **A cliff on the first screen** is about the promise, not the question: people
  did not understand what the survey is for, or saw that it is long.
- **A cliff at the last step** is almost always contacts: they were asked for
  before the person understood why to give them.

## Common causes by type

| Question | Why people leave |
|---|---|
| Open text | typing is effort, especially on a phone |
| Required contact | unclear why, and not trusted |
| A ten-row matrix | looks like work |
| A long option list | nobody wants to read it |
| File upload | awkward on a phone |
| A personal question with no explanation | feels intrusive |

## What to propose

Specific edits instead of "shorten the survey": make this one optional, move that
one later, split this matrix, add one line explaining why you ask.

Ask for contacts at the end, after the person has already invested effort.

## What not to do

- **Do not compute conversion over all responses** if some are your own test
  runs. Cut them off by date first.
- **Do not draw conclusions from twenty responses.**
- **Do not edit the survey yourself.** Present the findings and propose changes.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.
