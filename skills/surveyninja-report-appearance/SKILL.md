---
name: surveyninja-report-appearance
description: "Configures how a SurveyNinja survey and its reports look: the survey
  theme, the report palette and font, saved report presets, the account logo and
  the SurveyNinja branding line. Use when someone asks to match their brand style,
  change survey or chart colors, put a logo on surveys and reports, or prepare a
  report to show a client."
---

# Styling the survey and the reports

The survey and the report are what outsiders see: the respondent and the client.
These settings are cheap and change the impression a great deal.

Reply to the person in the language they write in.

## Survey theme

Branding and the shared report palette live at account level, and most tools below
need the account id: take it from `get_workspace_list`.

`get_theme_list` shows what already exists in the account, and `get_theme_details`
shows the colors of one theme. **Look at existing themes first**: usually a
suitable one is already there.

`apply_quiz_theme` applies a theme to a survey. `create_theme` and `update_theme`
are for custom colors. `manage_theme` copies a theme (quicker than starting from
scratch), deletes one or restores a deleted one; surveys that used a deleted theme
move to the default one.

Ask about brand colors concretely: the main button color, the background, whether
there is a logo. More than two or three colors in a survey is too many.

## Report styling

`get_workspace_report_appearance` shows the shared account palette, the saved
presets and the allowed values for every field.

There are two levels, and the difference matters:

- **The shared palette**, `update_workspace_report_palette`, repaints every survey
  that follows it. Surveys with their own colors keep them.
- **One survey's report**, `update_quiz_settings` with `results_appearance`, gives
  that survey its own palette, bar colouring, font, value labels and grid lines.
  It stops following the shared palette, and nothing else changes.

If the person wants a new look for a single report, use the survey level. If they
ask to change the shared palette, say first that every report following it changes
too.

`create_report_appearance_preset` saves a set of settings under a name, useful when
reports go to different clients; `delete_report_appearance_preset` removes one.
A preset is a template: to use it on a survey, pass its settings as
`results_appearance`. Deleting or editing a preset does not touch surveys it was
used on.

The PDF of the AI report is printed from the public report page, so it carries the
same palette and font.

## Logo and branding

`upload_workspace_logo` (a public URL or a file, up to 1 MB), `delete_workspace_logo`,
and `update_workspace_branding` to show or hide the logo and the SurveyNinja
branding line.

These are account-wide, not per survey: the logo appears in every survey, report
and PDF of the account. A custom logo and hiding the SurveyNinja branding are not
available on every plan. If the plan does not allow it, the tool says so: state it
plainly and stop.

## Advice worth giving

- **Contrast beats beauty.** Light grey on white is unreadable on a phone, and
  most surveys are taken on phones.
- **Chart palettes must survive black-and-white printing**, because reports get
  printed. The `contrast` and `mono` palettes are safe choices.
- **A logo on the survey is fine; on every question it is not.**

## What not to do

- **Do not change the shared account palette for one report** without warning.
  Use the survey's own report appearance instead.
- **Do not create a new theme when a suitable one exists.**
- **Do not suggest a plan upgrade or lead to payment.** If the plan does not allow
  a custom logo or hiding the branding, state the fact and stop.
