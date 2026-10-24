---
name: surveyninja-survey-logic
description: "Configures question display logic in a SurveyNinja survey: branching,
  showing and hiding questions, skipping blocks, screening out unsuitable
  respondents and quotas. Use when someone wants different questions shown to
  different people, or reports that the survey sends respondents to the wrong
  place or into a dead end."
---

# Branching and routing

Logic is where surveys break silently: a condition references a question by
identifier, and a branch built blind leads the respondent into a dead end with no
way out.

Reply to the person in the language they write in.

## The order is strict

1. `get_quiz_structure`: read the current state and the question identifiers.
2. Build the change against what actually exists.
3. `update_quiz_logic`: write.
4. The edit lands in the draft. Respondents get it only after `publish_quiz`,
   and publishing waits for the person's go-ahead.

The first step cannot be skipped. Identifiers cannot be guessed, and logic that
points at a question that does not exist is rejected on save (`widget_missing`
and similar errors).

## What can be built

- **Branch on an answer.** "Rated below four: ask why."
- **Show or hide a question.** "Ask about delivery only if they ordered online."
- **Skip a block.** "Did not use the service: do not ask about its quality."
- **Screen out.** A respondent who does not fit belongs on a `screenout` screen,
  not driven to the end and cleaned up afterwards.
- **Quotas.** Once a group is full, stop admitting it.
- **Branch on a link label.** A value passed in the survey link (a hidden variable)
  can drive a condition. Hidden variables are not on every plan: if they are not
  available, say so and stop.

## Rules people trip over

- **Every branch needs an exit**, to the next block or to the end of the survey.
- **A condition on "Other"** matches the option, not the text typed into it.
- **The operator must fit the question type.** Greater and less than are for
  numbers and scales, not for text or choices.
- **Order matters**: conditions are checked top to bottom and the first match wins.
- **A branch must not lead back** to an already answered question, or the
  respondent ends up in a loop.

## After the edit

Walk the route by eye: from the first question along every branch to the end. If
there are more than three or four branches, describe the map in words: who ends up
where. Then ask whether to publish: until then respondents still follow the old
route.

## What not to do

- **Do not write logic without reading the structure.**
- **Do not change the question set in the same edit.** When something breaks, it
  becomes unclear which change caused it.
- **Do not build branching where one question with options is enough.**
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.
