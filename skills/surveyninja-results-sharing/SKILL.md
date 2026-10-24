---
name: surveyninja-results-sharing
description: "Prepares SurveyNinja survey results for handing to someone else: a
  public link to the summary, report or responses, a PDF or Word file, or an AI
  report with conclusions. Use when someone asks to send results to a client,
  share a report with a colleague or manager, export the outcome as a file, or
  build a report with findings and hand it over as a link or PDF."
---

# Handing over results

Survey results are read by more people than those who built the survey. A client, a
manager or a colleague does not need access to the account. They need a finished
thing: a link or a file.

Reply to the person in the language they write in.

## Ask what exactly is needed first

These are four different things, and mixing them up is expensive:

| What they ask for | What to hand over | Tool |
|---|---|---|
| "Show me the results", figures per question | the summary | `share_summary_link`, `export_summary_pdf` |
| A report with breakdowns, by period or filter | the report | `share_report_link`, `export_filtered_report_pdf`, `export_filtered_report_word` |
| Individual completions, who answered what | the responses | `share_answers_link`, `export_answers_xlsx` |
| Text with conclusions rather than tables | the AI report | `get_ai_report`, `generate_ai_report`, `share_ai_report` |

If the request does not make it clear, ask one question. If the survey is named in
words, find it with `get_quiz_list` and confirm it is the right one.

## Link or file

**A link** always shows fresh data. It cannot be turned off and has no expiry: it
stops opening only if the survey is archived or deleted. It suits a survey that is
still collecting and a client who will come back more than once.

**A file** freezes the state at export time. It suits a report "as of a date" or a
recipient who must not see what arrives later. Download links live for an hour: say
so.

## Check before handing anything outside

1. **Are there contacts in the survey?** Call `get_quiz_structure`. If there is a
   phone, email or name question, a public link to the *responses* shows them to
   anyone who has the link. Offer the summary or the report instead; if responses
   are really needed, ask whether they should leave the team at all.
2. **Period and scope.** The summary and responses links take a date range and
   the completion status (`is_complete`); the report link keeps the report
   filters saved in the app. Ask whether abandoned completions are wanted: for a
   client, usually not.
3. **Saved filter.** If the report already has a configured slice
   (`get_quiz_report_filters`), hand that over instead of building a new one.

## The AI report

In the app it is called Smart Analytics. Read what already exists with `get_ai_report` first. It returns the report the
author sees in the results section, with the state of each of its three sections:
text analysis, comparative and quantitative. Building a report for a new survey
counts against a plan limit, and rebuilding an existing one does not.

If there is no report yet, `generate_ai_report` builds all three sections or one
`section`, in the language given by `locale`. It is not instant: warn first, then
fetch the result with `get_ai_report`. Hand it out with `share_ai_report` as a public
link or as a PDF. The survey must be published, because the report page lives at its
address.

Do not build an AI report on a handful of answers. The tool refuses below its
minimum, and a dozen answers give conclusions that sound confident and rest on
nothing. Say the data is thin.

If Smart Analytics is not on the person's plan, the tool says so. State it and
offer the summary, the report or the responses instead.

## What to say at the end

What exactly was handed over (summary, report, responses, AI report), for which
period, with which filters, and whether it is a link that stays open or a file whose
download link lives an hour. If a link was handed over, remind them it is public
and cannot be revoked: only archiving or deleting the survey closes it. That
matters most when the responses hold contacts.

## What not to do

- **Do not share responses with contacts via a public link** without asking directly.
- **Do not export a file when a link was asked for**, or the other way round. They
  are different things.
- **Do not build an AI report silently.** It takes a while and counts against the
  plan limit, so warn first and read the existing report before building a new one.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.
