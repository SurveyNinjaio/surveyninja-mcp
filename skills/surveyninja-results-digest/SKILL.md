---
name: surveyninja-results-digest
description: "Explains what a SurveyNinja survey showed: pulls the summary, the
  per-question report, filtered slices and open answers, and turns them into a
  few conclusions with numbers. Use when someone asks about survey results, wants
  results for a period, a channel or a group of respondents, needs figures for a
  report, or asks what the open answers say."
---

# What the survey showed

The answer is a few numbers with an explanation of what they mean. A dump of raw
responses is not an answer.

Reply to the person in the language they write in.

## Which tool for what

This is where the wrong tool gets picked most often:

| What you need | Tool | What it returns |
|---|---|---|
| The funnel | `get_quiz_summary` | visits, completed, abandoned, completion rate, screened out, average time, by day, devices, countries |
| Answers per question | `get_quiz_report` | distributions for every question, completed responses only |
| A slice by answers, tags or a set of unique links | `generate_filtered_report` | the same report over the selected responses |
| Individual submissions | `get_quiz_answers` | raw responses one by one |
| Free text of one question | `get_quiz_report_inputs` | text answers, 50 per page |
| A file for a human | `export_answers_xlsx` and the other `export_*` tools | a download link |

**Start with the summary and the report, not with raw answers.** Raw answers are
for a specific submission or for quoting examples.

## Order

1. `get_quiz_summary`: how many visited, how many finished, how many abandoned.
   If many abandoned, say so and treat them separately.
2. `get_quiz_report`: the distributions. It counts completed responses only,
   whatever `is_complete` says. Unfinished ones are read one by one with
   `get_quiz_answers` with `is_complete` false, if the plan keeps them; if it
   does not, that call quietly returns completed ones, so check `is_complete` on
   each response.
3. If a condition was named, such as "September only" or "only people who chose
   the premium option", build a slice: dates in `get_quiz_report`, answers and
   tags in `generate_filtered_report`. Dates, answers and tags apply only when
   the plan includes results filters; otherwise the report covers everything and
   does not say so. Check `get_workspace_tariff` (the `workspace_id` comes from
   `get_workspace_list`) or compare the totals with the summary. For "only from
   the link I sent by email", check how that link was marked: a set of unique
   links filters directly, on any plan. A link label such as `utm_source` is in
   the `extra_fields` of each response from `get_quiz_answers`: count the
   responses with that value there. No tool builds the whole report for one label
   value; in the app that is the Hidden Variables filter in Results.
4. Open answers: `get_quiz_report_inputs` with the `report_uuid` from the report
   and the question's `widget_id` and `widget_hash` from `get_quiz_structure`.
   It returns 50 answers per page: page with `offset` to read them all. The texts
   follow the report filters saved in the app, not the slice built here.
5. Export a file only if a file was asked for. The link lives for one hour.

## How to answer

- **Conclusion first, numbers second.** Not "question 3 has this distribution"
  but "two thirds are unhappy with turnaround times, here is the breakdown".
- **Always name the base** for a percentage: all submissions or completed ones.
- **Do not present conclusions from ten responses as fact.**
- **Do not retell free text one by one.** Group it into themes with a couple of
  representative quotes.

## What not to do

- **Do not export a file unasked.** Chat needs numbers, not a download link.
- **Do not recompute by hand** what the summary or the report already provides.
- **Do not mix completed and abandoned** in one figure without saying so.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit or a
  feature is not on the plan, state the fact and stop.
