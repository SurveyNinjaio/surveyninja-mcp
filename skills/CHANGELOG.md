# AI skills changelog

People download a skill as a file and keep it. A file downloaded a month ago does not say whether it is
out of date, so versions and dates live here. A skill's version is also on its page at surveyninja.io/skills.

- **Third number**: wording, a typo, a clarification. No need to download again.
- **Second number**: a new step, rule or reference. Worth updating.
- **First number**: the skill was rewritten or renamed. Remove the old file.

## 2026-10-24

Every skill's `description` in the `SKILL.md` header is now in double quotes. In 20 skills it held a colon
followed by a space, which strict YAML parsers reject, so an assistant with such a parser could skip the
skill. The text of the skills did not change. If your assistant did not pick a skill up, download it again.

| Version | Skills |
|---|---|
| 1.1.1 | `ab-significance`, `benchmark`, `launch-kit`, `lead-quality`, `open-answers`, `response-funnel`, `results-digest`, `sample-size`, `source-dashboard`, `survey-copy`, `survey-timeline` |
| 1.0.2 | `account-audit`, `integration-triage`, `prelaunch-check`, `results-sharing`, `survey-distribution`, `survey-from-brief`, `survey-logic`, `webhook-setup`, `workspace-access`, `workspace-housekeeping` |
| 1.0.1 | `answer-notifications`, `answers-cleanup`, `data-quality`, `report-appearance` |

## 2026-10-21

Fixes after a check of every skill against the MCP server code.

| Version | Skills | What changed |
|---|---|---|
| 1.1.0 | `ab-significance`, `response-funnel`, `lead-quality`, `benchmark`, `survey-timeline`, `sample-size` | The report holds completed responses only: completion, drop-off and contact gaps now come from unfinished responses (`get_quiz_answers`) and the summary's daily counts; report dates and slices need the results filter on the plan |
| 1.1.0 | `source-dashboard`, `results-digest`, `open-answers` | Link labels come from survey variables and each response's `extra_fields`; no tool slices the report by a label. Open answers need the report id and the question hash, come 50 at a time and follow the saved filters |
| 1.1.0 | `launch-kit`, `survey-copy` | The QR code carries the plain published link. Copy edits: widget texts are a draft until published, interface strings go live at once |
| 1.0.1 | `prelaunch-check`, `survey-logic`, `survey-from-brief`, `survey-distribution`, `results-sharing`, `integration-triage`, `webhook-setup`, `account-audit`, `workspace-access`, `workspace-housekeeping` | No finish screen means the standard completion, not a blank page; a public results link cannot be turned off; Telegram connects from chat; webhooks accept http; the app's words for workspaces and access |

## 2026-10-20

First release: 25 skills, checked against the SurveyNinja MCP server.

| Group | Skills, all 1.0.0 |
|---|---|
| Build and share | `survey-from-brief`, `survey-copy`, `survey-logic`, `launch-kit`, `survey-distribution` |
| Check before launch | `prelaunch-check`, `data-quality` |
| Understand results | `results-digest`, `ab-significance`, `benchmark`, `open-answers`, `response-funnel`, `sample-size`, `survey-timeline`, `source-dashboard`, `results-sharing`, `report-appearance` |
| Deliver responses | `answer-notifications`, `webhook-setup`, `integration-triage`, `lead-quality` |
| Keep the account tidy | `account-audit`, `answers-cleanup`, `workspace-housekeeping`, `workspace-access` |

Every name starts with `surveyninja-`.
