---
name: surveyninja-workspace-housekeeping
description: "Tidies up a SurveyNinja account: sorts surveys into workspaces
  (folders), renames them, archives finished ones, moves drafts to the trash and
  restores from it, copies a survey for a new wave, turns a recurring survey into
  a template, and cleans up files that take up storage. Use when someone asks to
  tidy up or organize their surveys, remove old ones, free up space, copy a
  survey, or save one as a template."
---

# Tidying up the account

Accounts get overgrown: a hundred surveys in one workspace, finished ones next to
live ones, year-old drafts. Most of the tidying can be undone. A few steps cannot,
and those have to be known in advance.

Reply to the person in the language they write in.

The tools and the app name things differently. What the tools call a workspace is
the **account** in the app; what they call folders are **workspaces** in the app.
Talk to the person in the app's words.

## Picture first, actions second

`get_workspace_list` gives the account's `workspace_id` that almost every tool
below needs. `get_folder_list` and `get_quiz_list` show what is where. If the
person asks to "tidy up" in general, first show the list of what is proposed for
each survey and get agreement. A health check (what is abandoned, where storage is running out) is
a separate skill; this one does the work.

## What does what

| Task | Tool | Reversible? |
|---|---|---|
| New workspace | `create_folder` | yes |
| Rename a workspace, delete it, change the order | `manage_workspace_folder` | delete: no |
| Move a survey to another workspace | `move_quiz` | yes |
| Rename a survey | `rename_quiz` | yes |
| Internal note on a survey | `update_quiz_note` | yes |
| Archive and bring back | `archive_quiz` | yes |
| Copy a survey | `duplicate_quiz` | yes |
| Make a template | `make_quiz_template` | no undo through these tools |
| The account's own templates | `get_workspace_templates` | read only |
| Move to the trash | `delete_quiz` | can be restored |
| Restore from the trash | `restore_quiz` | yes |
| Account files: overview, list, delete | `manage_workspace_files` | delete: no |

## Three levels of "remove"

1. **Archive.** The survey stops accepting responses, leaves the main list, and
   its public report links stop opening, but everything is kept. Archived surveys
   do not count against the survey limit. For finished surveys this is the right
   answer.
2. **Trash.** The survey is removed; `restore_quiz` brings it back with its
   questions, logic and responses. For drafts and duplicates. A restored survey
   takes a slot in the survey limit again.
3. **Permanent.** Deleting a workspace that has surveys in it deletes every survey
   inside together with its responses, and deleting files cannot be undone. Both
   need a separate confirmation flag. Offer them last.

A finished survey with responses goes to the archive, not the trash: the
responses will be useful for comparing with the next wave.

## A new wave of a survey

Do not edit last time's survey. Copy it with `duplicate_quiz` into the right
workspace under a new name, so the previous wave's responses stay untouched and
comparable. If the survey runs regularly, `make_quiz_template` turns it into a
template for the next waves; ask first, because the template cannot be removed
through these tools.

## Workspaces and colleagues

A new workspace is open only to the account owner and to the person who created
it. If colleagues need it, say so and hand over to access management; do not leave
them looking at a list without the moved surveys. Two workspaces cannot share a
name, and the main workspace cannot be deleted.

## Files

`manage_workspace_files` with `overview` shows how much is used and by which
surveys; `list` shows the files themselves, filtered by survey and type. Delete
only on a direct request and only what was shown to the person as a list: a
respondent's file is attached to their response and cannot be recovered.

## What not to do

- **Do not delete permanently without explicit agreement** on a specific list.
- **Do not archive a survey that is still collecting responses**: it will stop
  accepting them. Check recent responses in `get_quiz_summary` first.
- **Do not rename or move other people's surveys** in a shared workspace without
  asking: colleagues look for them by the old names and in the old workspaces.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.
