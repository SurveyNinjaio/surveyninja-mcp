---
name: surveyninja-ab-significance
description: "Compares A/B variants in SurveyNinja and checks whether the
  difference is real or within noise: the built-in A/B test of a question's
  wording, or two surveys or two sets of links run as variants. Use when someone
  asks which variant or wording performs better, whether a test can be stopped,
  or is about to make a decision based on a test."
---

# Comparing A/B variants

The main A/B mistake is deciding on random noise. On fifty responses a ten point
difference appears by itself, for no reason at all.

Reply to the person in the language they write in.

## Find out what is being compared

- **The built-in A/B test.** In SurveyNinja a question, a message or an HTML block
  can show two or more versions of its title and description; the answer options
  stay the same. `get_quiz_structure` shows which questions have variants and
  their wording.
- **Two surveys, or two sets of links to one survey**, run side by side. Then the
  variants are compared like any two groups of respondents.

Ask first what counts as success: completion share, share leaving a contact,
average rating, the share choosing a given option. Without that there is nothing
to compare.

## Collect

For the built-in test, `get_quiz_report`: the question's `abTest` block lists the
variants. The report holds only completed responses, so there `shown_count` is the
number of completed responses that saw each variant, and `completion_count`
repeats it: the completion percentages are always near 100% and say nothing.

Completion share by variant cannot be read through the tools: the responses from
`get_quiz_answers` do not say which variant the respondent saw. Ask the person to
open Results → Reports in the app, choose All above the report and read each
variant's Impressions and Finished. All is there only when the plan keeps
unfinished responses (`incomplete_answers` in `get_workspace_tariff`; it needs the
`workspace_id` from `get_workspace_list`); without it, say that this metric is not
available and compare what the completed responses allow.

For any other metric (a contact left, a rating, an option chosen) the report does
not split answers by variant. The answer export (`export_answers_csv`) has a
column with the variant each respondent saw: use it if you can open the file, or
ask the person to apply the A/B test section of Filter in Results and read the
numbers per variant. Export and filters depend on the plan.

For two surveys: `get_quiz_summary` for each gives the completed
(`filled_completely`) and unfinished (`started_not_finished`) counts. For two sets
of unique links: `get_quiz_answers` with `unique_link_group_id`, `is_complete` true
and then false, paged with `limit` and `offset`; count the responses returned, as
`answer_total_count` is the whole survey's total. Without unfinished responses on
the plan, `is_complete` false returns completed ones: check each response's
`is_complete` field. Answers per set: `generate_filtered_report` with
`unique_link_group_id` (completed responses only).

The SurveyNinja report may mark a leading variant. That mark starts at 80%
confidence, a lower bar than a decision needs, so treat it as a hint.

## Compute

1. The metric per variant with its base: "42 of 180" beats "23%".
2. The difference in percentage points, not percent of a percent.
3. Whether there is enough data. Rule of thumb: a five point difference needs
   hundreds per group, a twenty point one needs dozens. Below a hundred per group
   a difference can rarely be called proven. When in doubt, run a two-proportion
   test and give the result in plain words.
4. That the groups are comparable: same period, same traffic source. If the
   shares or the wording changed during the test (`get_quiz_versions`), say so.

## How to answer

Three possible conclusions; pick one honestly:

- **There is a difference.** State its size and what it means in practice.
- **There is no difference.** The variants perform the same, which is also a
  result: choose either on other grounds.
- **Not enough data.** Say how much more is needed and give no recommendation.

The third is the most common and the least popular, and giving it honestly
matters more than guessing.

## What not to do

- **Do not declare a winner on a couple of points** on a small sample.
- **Do not compare variants from different periods.** Seasonality breaks it.
- **Do not peek and stop the test** the moment the preferred variant pulls ahead.
- **Do not call a difference significant because it is badly wanted.**
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit or a
  feature is not on the plan, state the fact and stop.
