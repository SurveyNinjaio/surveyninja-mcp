---
name: surveyninja-workspace-access
description: "Manages SurveyNinja account members and their permissions:
  invitations, roles, access to workspaces (folders), per-workspace overrides. Use
  when someone wants to invite a colleague, give access to results only, restrict
  or revoke access, set up roles, or work out why a member cannot see the surveys
  or actions they need."
---

# People and access

Permission mistakes are quiet: a member simply does not see part of the surveys and
assumes they do not exist, or sees things not meant for them.

Reply to the person in the language they write in.

The tools and the app name things differently. What the tools call a workspace is
the **account** in the app; what they call folders are **workspaces** in the app
(the role editor still says folders). Talk to the person in the app's words.

## See the current picture first

Start with `get_workspace_list` to get the account's `workspace_id`: every tool
below asks for it. Workspaces, if needed, come from `get_folder_list`.

- `get_workspace_members`: who is in the account, with which role, whether the
  invitation was accepted, which workspaces they have.
- `get_workspace_member_access`: what one member can actually do, the same check
  the system runs when it refuses an action. It shows the role, the workspaces,
  per-workspace overrides, and a `blocked` reason when the member cannot work at
  all.
- `get_workspace_roles`: which roles exist, what each allows, and how many members
  are on each.

Start here. "Give Peter access" without the current picture usually gives Peter
more than intended.

## Invite and configure

| Task | Tool |
|---|---|
| Invite | `invite_workspace_member` |
| Resend the invitation | `resend_workspace_member_invite` |
| Change a member's role | `set_workspace_member_role` |
| Set the whole workspace list of one member | `set_workspace_member_folders` |
| Grant or revoke one workspace for one member | `manage_folder_access` |
| Remove a member | `remove_workspace_member` |
| Create or edit a role, delete a role | `save_workspace_role`, `delete_workspace_role` |

`set_workspace_member_folders` replaces the whole list: pass three workspaces and
the member sees exactly those. For a single change use `manage_folder_access`. An
empty list in either the invitation or the workspace list opens every workspace.

## Why "I added them and they see nothing"

1. **The invitation was not accepted.** Until the link from the letter is opened,
   the person is listed but has no access. `resend_workspace_member_invite` helps
   when the letter was lost or the link expired.
2. **The email is not confirmed.** The member joined but never confirmed their
   address, so every action is refused. Only they can fix it, from their own
   letter.
3. **No workspaces.** Access to surveys rests on workspaces: a member without
   workspaces sees an empty survey list.
4. **A new workspace.** A workspace created later is open only to the account
   owner and the person who created it. Other members need it granted.
5. **A per-workspace override.** The role allows something in general, but
   inside one workspace it is forbidden.

`get_workspace_member_access` shows which of these it is.

## Choosing permissions

Ask what the person needs to do, not which role to give:

- View results only: a role that allows viewing reports and forbids editing,
  plus the relevant workspaces.
- Build surveys: add editing, not necessarily deletion of surveys or responses.
- Configure integrations: a separate permission. Without it they do not see where
  responses are sent.
- Full access: only for people who actually administer the account.

A permission can be Allowed, Forbidden or Own only (`partially` in the tools),
which limits the member to the surveys, workspaces or themes they created
themselves.

A change to a role applies at once to every member on it. To change one person,
move them to another role instead of editing a shared one. Role setup and the
number of members depend on the plan: if a tool refuses, say so.

## What not to do

- **Do not remove a member without an explicit request**: access comes back only
  through a new invitation, and workspaces have to be assigned again. Their
  surveys stay in the account.
- **Do not grant full access "to be safe"**: the most common way to over-share.
- **Do not edit a shared role to fix one person**: everyone on that role changes
  too.
- **Do not delete a role in use** without checking who is on it: its members move
  to the default role and their permissions change.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.
