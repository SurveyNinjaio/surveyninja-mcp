---
name: surveyninja-survey-from-brief
description: "Builds a ready-to-use survey in SurveyNinja from a plain-language brief.
  Use when someone asks for a survey, questionnaire, feedback form, lead form, test
  or quiz and describes in words what they need to learn and from whom, rather than
  listing specific questions."
---

# Building a survey from a brief

Someone describes the job in words: "I need a survey for our repair shop customers,
to rate the work and collect contacts for a follow-up visit". Turn that into a
working survey in their account, not a list of questions in chat.

Reply to the person in the language they write in. Write the survey texts in the
language of their audience, not the language of this instruction.

## 1. Ask three things if they were not given

Who is being asked, what decision the results serve, where the link will live. No
more than three questions: everything else is faster to show as a draft and fix
from feedback.

Do not ask about question types, styling or order. Choosing them is the
assistant's job.

## 2. Check for something ready-made

`search_quiz_templates` by topic. The catalog has English templates but no
Spanish or Portuguese ones: for those audiences search with `lang` set to `en`
and translate. If a suitable template exists, offer to start
from it with `create_quiz_from_template` and edit from there: it is faster and
usually better than building from scratch. The choice stays with the person.

## 3. Create the survey and build the questions

`create_quiz`, then `update_quiz_widgets`.

A survey is created inside a folder, so start with `get_folder_list` and pick the
one to use. If there are several and the person did not say which, ask instead of
choosing for them.

Choosing types is the core of the work and where mistakes happen:

| What you need | Type | Why not otherwise |
|---|---|---|
| Quality rating | `rating` or `scale` | not `input` with a number: free text cannot be summarized |
| Likelihood to recommend | `nps` | its own 0–10 scale and its own analytics |
| One choice from a short list | `choice` | not `input`: free text cannot be grouped in a report |
| Several choices | `choice` with multiple selection | |
| One choice from a long list | `dropdown` | a long list of buttons is hard to scan |
| Name | `fio` | its own fields; switch the middle-name field off for most audiences |
| Phone, email | `phone`, `email` | format checks; otherwise half the contacts are unusable |
| Date and time | `datetime` | not text: otherwise it cannot be filtered or sorted |
| Several ratings on one set of criteria | `matrix` | instead of ten separate questions |
| File or photo | `file` | |
| Numeric answer | `number` | |
| Yes or no | `yesno` | |
| Put in order | `ranking` | |

Start the survey with a `welcome` screen. The last widget is always `submit`; add a
`finish` thank-you screen before it so the respondent sees what happens next
instead of a bare confirmation.

Make required only the contacts the survey exists for. Every extra required
question costs responses.

Set the phone question's default country to the audience's country, not a guess.

The full list of types and their fields is in `references/widget-types.md`.

## 4. Texts and styling

Headings and the thank-you text are fields of the `welcome` and `finish`
widgets: write them with `update_quiz_widgets`. Button labels and other interface
strings go through `update_quiz_texts`, by their `code` from `get_quiz_texts`.
Write in the plain language of the audience.

`get_theme_list` and `apply_quiz_theme`: take an existing theme. Create a new one
only if brand colors are explicitly requested.

## 5. Branching

`update_quiz_logic`, if the brief implies branches: "unhappy customers get a why
question", "did not use the service, so skip the quality block".

The order is strict: `get_quiz_structure` first, then edit, then write. Conditions
reference questions by identifier, and logic built blind leads respondents into a
dead end.

## 6. Show the draft, then publish

`publish_quiz` **only after the person agrees**. Until it is published the survey
does not open by its link, and that is the right state for review.

After publishing, hand over the link and briefly list what came out: how many
questions, which are required, whether there is branching.

## What not to do

- **Do not publish unasked.** A published survey can already be taken, and edits
  after the first responses break comparability.
- **Do not invent filler questions.** Long surveys are abandoned.
- **Do not make everything required.**
- **Do not suggest a plan upgrade or lead to payment.** If a limit is reached or a
  question type is not on the plan, state the fact and stop.
- **Do not delete or rewrite existing surveys** when asked to make a new one.

## If the brief is large

For long briefs there is `generate_ai_quiz`: the whole build runs in the
background. It returns the id of a survey that stays empty until the build is
done, not a finished survey. Call `generate_ai_quiz` again with that `quiz_id` to
see whether it is pending or ready, show the result, then edit with the usual
tools.
