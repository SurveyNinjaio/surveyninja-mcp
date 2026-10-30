---
name: surveyninja-account-audit
description: "Reviews the state of a SurveyNinja account in one read-only report:
  surveys collecting responses that nobody receives, abandoned surveys and drafts,
  broken notifications and webhooks, limits that are hit or close, storage and
  hidden files, pending invitations and over-wide access. Use when someone asks to
  check or tidy up their account, understand what is going on in it, or find out
  why responses or notifications stopped arriving."
---

# The account in one report

Accounts silt up: surveys collecting responses nobody reads, year-old drafts,
storage running out, a webhook that switched itself off months ago. The job is to
show all of it at once and change nothing.

Reply to the person in the language they write in.

## What to gather

Start with `get_workspace_list` to get the account's `workspace_id`: most tools
below need it. In the SurveyNinja interface the survey folders are called
"Workspaces" and the whole account is the "account": use those words with the
person.

| What | Tool |
|---|---|
| Surveys and workspaces (folders) | `get_quiz_list`, `get_folder_list` |
| Account and the key owner's permissions | `get_workspace_details` |
| Plan, limits and what remains | `get_workspace_tariff` |
| Storage and files hidden over the quota | `get_workspace_storage_usage`, `get_workspace_hidden_files` |
| Members and invitations | `get_workspace_members` |
| What one member can actually do | `get_workspace_member_access` |
| Recent activity of a survey | `get_quiz_summary` |
| Where responses go | `get_quiz_email_settings`, `get_quiz_integrations`, `get_quiz_webhooks` |

There may be many surveys. Check where responses go for the ones with recent
responses, not for all of them. Archived surveys are not in the regular
`get_quiz_list` output; ask for the archive separately if it matters.

## What to look for

**Responses piling up unseen.** A published survey with recent responses, no
email notification to the author, no enabled integration and no working webhook.
The most valuable finding of an audit.

**Notifications that only look set up.** A recipient address that was never
confirmed with the code from the letter receives nothing. A webhook that was switched
off automatically after a run of failed deliveries. An integration that is
connected but no longer allowed by the plan.

**Ghost surveys.** Published, but no responses for a long time: the link is no
longer shared, or it is broken somewhere.

**Drafts.** Created and abandoned. They count against the survey limit; archived
surveys do not.

**Storage.** How much is used and by which surveys, and whether files have started
to be hidden over the quota. Hidden files look to the author like attachments that
disappeared from responses.

**Plan limits.** What is already hit or close: surveys, responses, members, disk
space, email recipients.

**Access.** Invitations that were never accepted, members whose email is not
confirmed, members with wider access than their work needs. For a member who
looks over-privileged, `get_workspace_member_access` shows the effective
permissions, per-workspace overrides included; "Own only" in the interface means
the action works only on what that person created.

## How to present

In sections, by weight: first what is losing data right now, then what is merely
worth tidying.

For each finding: how many objects, which ones, and what specifically to do.
Avoid a vague "clean it up". If the person wants the tidy-up done, that is a
separate step with its own confirmation.

## What not to do

- **Delete and change nothing during the audit.** It is a report, not a cleanup.
- **Do not call a survey abandoned** when it may simply be seasonal: ask.
- **Do not show respondents' personal data** in the report: counts and survey
  names are enough.
- **Do not suggest a plan upgrade or lead to payment.** When a limit is hit or
  files are hidden over the quota, state the fact and stop.
