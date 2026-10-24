---
name: surveyninja-answers-cleanup
description: "Puts collected SurveyNinja responses in order: finds test runs,
  too-fast and straight-lined submissions and duplicates, hides them from reports,
  moves them to the trash or restores them, and marks responses with notes and
  tags. Use when someone asks to clean up responses, remove test submissions,
  mark or tag some responses, restore accidentally deleted ones, or complains
  about junk in the results."
---

# Cleaning up responses

Test runs, random clicks and duplicates distort the statistics. Cleaning brings
the reports back to what respondents really said, but part of it cannot be undone,
and that is the main thing to keep in mind.

Reply to the person in the language they write in.

## Look first, act second

`get_quiz_answers` with filters (date, completion, sort by start or end time):
show exactly what would be affected, meaning how many submissions, over what
period, and selected by which signal. Act only after the person agrees.

Hidden responses and those screened out by the survey logic are not in the default
output; ask for them with the matching filter when they matter.

## What does what

| Task | Tool |
|---|---|
| Hide a response from reports and the summary without deleting it | `toggle_answer_visibility` |
| A short note on a response (up to 100 characters) | `set_answer_note` |
| Tags on a response | `tag_answer` |
| Workspace tag list | `get_answer_tags`, `create_answer_tag`, `delete_answer_tag` |
| Move to trash, restore, delete for good | `delete_quiz_answers` |
| Question order inside a response card | `set_answers_order_mode` |

## Three levels of removal

1. **Hide.** The response stays in the list but leaves reports and the summary.
   Reversible. The right choice when unsure.
2. **Trash.** The response leaves the list and the report but can be restored.
3. **Permanent.** Nothing to recover, and the files the respondent uploaded go
   with it. It needs an explicit confirmation flag, and that confirmation must come
   from the person in words for the specific volume.

Start at level one. Offer level three only when permanent deletion is explicitly
requested. Hidden responses are skipped by trash and permanent deletion: bring a
response back into reports first if it really has to go.

## What people usually look for

- **Test submissions**: the author's own runs while building, usually the
  earliest ones, before the survey was shared.
- **Too fast**: completed quicker than the questions can be read.
- **Straight-lining**: the first option everywhere, or one rating throughout.
- **Duplicates by contact**: the same email or phone number several times.

Show them as separate groups with counts, not one long list.

## Tags and notes

The tag list belongs to the workspace, not to the survey, so the tag tools need
the workspace id: take it from `get_workspace_list`.

Tags beat deletion: the response stays in the statistics but is marked. "Call
back", "complaint", "needs work" are easier to work with than an exported sheet.

Read `get_answer_tags` first and reuse an existing tag. Create a new one only if
nothing suitable exists, otherwise the workspace ends up with three spellings of
the same thing. `tag_answer` replaces the tags of a response, so pass the ones it
already has together with the new one.

`set_answers_order_mode` also changes the public link to responses and the Word
export, so mention that before switching it.

## What not to do

- **Do not delete permanently without explicit consent** for the specific volume.
- **Do not clean "outliers" by answer value**: a low rating is a real answer.
- **Do not delete responses to improve the numbers.**
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.
