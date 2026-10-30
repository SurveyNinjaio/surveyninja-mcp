---
name: surveyninja-open-answers
description: "Analyses free-text answers from a SurveyNinja survey: groups them into
  themes, counts how often each theme comes up and picks representative quotes. Use
  when someone asks to read the comments, understand what respondents write about,
  summarise open answers, or find the most common complaints and suggestions in
  text answers."
---

# Analysing free-text answers

Open questions give the most valuable material and the least convenient one: a
hundred lines of text that appear in the report as a plain list. The job is to turn
them into a few themes with numbers.

Reply to the person in the language they write in. Keep quotes in the language the
respondent wrote them in.

## Collect

1. `get_quiz_structure` — find the open questions with their `widget_id` and
   `widget_hash`.
2. `get_quiz_report` — gives the `report_uuid`.
3. `get_quiz_report_inputs` with those three — the text answers for one question,
   50 at a time: page with `offset` until nothing is left. If several questions
   collect text, take them one at a time: mixing answers to different questions
   produces mush.

The texts follow the report's saved filters (by default, completed responses
only); no call parameter narrows them. To analyze only part of the respondents
(one segment, one period), the saved report filters have to change: read them
with `get_quiz_report_filters`, and before `save_quiz_report_filters` ask the
person, because the same filters apply to the report screen, the public link and
the PDF that others see. Restore them afterwards if asked. If report filters are
not available on the person's plan, say so as a fact and analyze all answers.

## Analyze

1. **Extract themes** by meaning, not by wording: "waited long", "waited forty
   minutes" and "the queue" are one theme.
2. **Count.** How many answers per theme and what share of those who answered.
3. **Separate the empty ones.** "No", "all fine", "-" form a "no content" group:
   do not theme them, and do not hide them either, because the size of the group
   says something.
4. **Pick quotes.** One or two per theme, verbatim, the most characteristic.
5. **Note sentiment** where it is distinguishable: one theme can carry different
   attitudes.

## How to present

Themes by descending frequency. For each: a theme name in your own words, the
count, the share, one quote.

At the end: the two or three themes that recur most, which is what is worth acting
on.

## Honesty rules

- **Do not invent themes.** If the answers do not group, say so.
- **Do not bend results to expectations.** If they expected price complaints and
  people write about deadlines, report deadlines.
- **Quote verbatim**, typos included: a tidied quote stops being evidence.
- **Do not conclude from five answers.** Say the data is thin.

## What not to do

- **Do not mix answers to different questions** in one analysis.
- **Do not surface quotes containing personal data.** Strip phone numbers, email
  addresses and names out of the quote.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.
