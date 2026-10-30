---
name: surveyninja-benchmark
description: "Compares SurveyNinja survey results against each other: one
  questionnaire across periods (waves), or different surveys in the account on
  shared metrics such as completion rate and time to complete. Use when someone
  asks whether things improved, how ratings changed since the last measurement,
  or which survey performs better."
---

# Comparing with your past self

A single number means almost nothing: is 4.2 good or bad? Meaning appears only
against a previous measurement.

Reply to the person in the language they write in.

## Two kinds of comparison

**One survey across periods**, in waves. The most reliable: same questionnaire,
same audience, only time differs.

**Different surveys in the account** are comparable only on general metrics such
as completion rate and time to complete. Substantive answers cannot be compared
when the questions differ.

## How to collect

For waves: `get_quiz_report` with `date_from` and `date_to`, once per period. The
dates work only when the plan has results filters (`result_filters` in
`get_workspace_tariff`, with the `workspace_id` from `get_workspace_list`);
otherwise the report silently covers all time, and two periods give identical
numbers. Without the filters, read the completed responses with
`get_quiz_answers` (`is_complete` true, paged with `limit` and `offset`) and split
them by their end date, or say that waves cannot be compared here. The report
holds only completed responses either way; completion per period comes from the
daily counts in `get_quiz_summary` (`number_answer_by_day`; the unfinished ones
appear only when the plan keeps them).

For different surveys: `get_quiz_list`, then `get_quiz_summary` for each. The
summary gives visits, completed and abandoned responses, completion rate and
average time.

**Check `get_quiz_versions` before comparing waves.** Every publication leaves a
snapshot with its date. If the survey was republished between the waves and the
wording or options changed, the numbers are not comparable, and that must be said
plainly rather than shown as a trend. If the snapshots do not make clear what
changed, ask the person.

## What to compare

| Metric | What a change means |
|---|---|
| Average rating | a shift in audience sentiment |
| Distribution across options | more precise than the average: shows where the shift came from |
| Completion share | a change in the questionnaire or in audience quality |
| Number of responses | distribution activity, not product quality |

Look at the distribution, not only the average: the average can hold steady while
half the satisfied move to dissatisfied and the other half the other way.

## How to answer

- **State direction and size.** "The average rose from 4.0 to 4.3", and how many
  responses each is based on.
- **Say whether it is meaningful.** On small samples, tenths mean nothing.
- **Do not explain a cause that is not in the data.** A guess can be offered, but
  labeled as a guess.

## What not to do

- **Do not compare periods of different length** without normalising.
- **Do not compare waves with an edited questionnaire** in between without saying
  so.
- **Do not compare seasonal periods head-on.** December and July behave
  differently.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit or a
  feature is not on the plan, state the fact and stop.
