---
name: surveyninja-data-quality
description: "Checks the quality of responses collected in SurveyNinja: too-fast
  submissions, flat-lined answers, duplicates by contact, junk text,
  contradictions and bursts in time, and works out whether removing them changes
  the conclusions. Use when someone doubts the data, suspects cheating or bots,
  ran a survey for a reward or through an open link, or is preparing results to
  present."
---

# Can this data be trusted

Before building conclusions it is worth looking at what they are made of,
especially if the survey was distributed for a reward or through an open link.

Reply to the person in the language they write in.

## What to check

**Too fast.** Completed in less time than it takes to read the questionnaire.
Rule of thumb: at least five seconds per question; for ten questions, anything
under a minute is suspicious. The average time from `get_quiz_summary` helps set
the bar for this survey.

**Flat-lined.** The first option everywhere, one rating throughout, a whole
matrix column.

**Duplicates by contact.** The same phone or email several times. Sometimes
honest, a double submission by mistake, but in a rewarded survey it is cheating.

**Junk text.** "Aaa", "123", random letters in a required open field.

**Contradictions.** "Never used the service" followed by a detailed rating of it.
Usually this means the display logic is wrong, not that the person lied.

**Time spikes.** Twenty submissions in a minute with an identical answer pattern.

## How to collect

- `get_quiz_summary`: how many completed, how many were screened out, the average
  time to complete.
- `get_quiz_answers` with `is_complete` true, paged with `limit` and `offset`:
  the submissions themselves with their start and end times and contacts, one
  trait at a time. Screened-out and hidden responses are not returned by default,
  which is right for this check.
- `get_quiz_report` for the distributions, and `get_quiz_report_inputs` for the
  texts of one open question in the junk check.

## How to present

Per trait: how many submissions match and what share of the total. Separately:
how many submissions remain if all of it is removed, and how the key numbers
change.

That last part matters most: if the conclusions hold after cleaning, there is no
need to clean.

## What to do with findings

Propose, do not act:

1. Tag them with `tag_answer`. The data stays, the doubtful ones are marked.
   The tool replaces the tags of a response, so keep the tags it already has.
2. Hide them from reports with `toggle_answer_visibility`. The response stays in
   the list and can be brought back.
3. Delete them with `delete_quiz_answers` only on an explicit request and after
   confirmation. Moving to the trash can be undone; permanent deletion cannot.

Start with the first. For the next wave, the survey settings can limit one
response per person and add a captcha or a password; mention it, do not change
the settings without being asked.

## What not to do

- **Do not call low ratings and harsh comments junk.** An unhappy respondent is
  not cheating.
- **Do not delete anything yourself** off the back of this check.
- **Do not trim the sample** toward a desired result.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit or a
  feature is not on the plan, state the fact and stop.
