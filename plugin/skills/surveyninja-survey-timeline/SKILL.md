---
name: surveyninja-survey-timeline
description: "Shows the history of a SurveyNinja survey over time: when it was
  published, how responses came in, where the spikes and drops are. Use when
  someone asks why responses stopped or dropped, what changed in the survey and
  when, or how collection went over a period."
---

# Survey timeline

"Why did responses stop" is answered by lining up two things: how responses came in
and what was done to the survey.

Reply to the person in the language they write in.

## Two lines

**Responses over time:** `get_quiz_summary` gives responses per day (completed,
unfinished and screened out) and visits per day. Group them by week if collection
ran long. Unfinished ones are there only if the plan keeps them.

**Edit history:** `get_quiz_versions`. Every publication leaves a snapshot, so it is
visible when the survey changed and which version was live at each moment.

## Line them up

Find matches by date:

- **A drop right after a publication:** something was broken by an edit, such as a
  logic branch, a required field or the link address.
- **A drop with no edits:** an outside cause. The email campaign or ad ended, the
  banner came down, the event finished.
- **A spike** is also useful: understand what worked and repeat it.
- **A steady decline** is normal decay: the audience the link reached ran out.

## Check separately

If the drop is sharp and goes to zero, check whether the survey was unpublished or
closed. An unpublished or closed survey stops accepting responses immediately,
which from the outside looks exactly like people no longer answering.

Check whether the account has reached its monthly response limit with
`get_workspace_tariff` (the `workspace_id` comes from `get_workspace_list`). Past
the limit, new responses are still saved but hidden: they do not appear in the
summary, the report or the responses and are not sent to integrations, so it
looks as if people stopped answering. If so, state that as a fact and stop there.

If the person watches responses somewhere else (Google Sheets, a webhook,
Telegram) and those stopped, check `get_quiz_integrations` as well: a broken
connection looks the same from outside while responses keep arriving in
SurveyNinja.

## How to present

Briefly and by date: period, what happened, what it lines up with. A few anchor
points instead of a forty-row table.

One sentence of conclusion: "responses stopped on this date, apparently because of
that". If no link is found, say so rather than inventing one.

## What not to do

- **Do not pass a date coincidence off as a cause** when the edit could not have
  affected it.
- **Do not compare weekdays with weekends** without noting it: most surveys have a
  weekly rhythm.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.
