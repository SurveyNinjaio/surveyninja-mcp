# SurveyNinja question types and their fields

Reference for the `surveyninja-survey-from-brief` skill. Open it when the type you
need is not in the selection table inside `SKILL.md`, or when a question needs finer
configuration.

Only the fields that actually change behavior are listed. The full schema comes
with `update_quiz_widgets`, and `get_quiz_structure` returns a live example for an
existing survey: if unsure about a field name, look there.

Some types are not available on every plan. If the tool refuses a type for that
reason, tell the person which question could not be added and why, and stop.

## Text and numbers

| Type | What it is | Main fields |
|---|---|---|
| `input` | single or multi-line answer | `inputPlaceholder`, `inputIsTextarea`, `inputLimitMin`, `inputLimitMax` |
| `number` | a number | `numberMin`, `numberMax`, `inputPlaceholder` |
| `fio` | a name in separate fields | `fioWithPatronymic`, `fioNamePlaceholder`, `fioSurnamePlaceholder` |
| `email` | email with format checking | `emailPlaceholder` |
| `phone` | phone with country selection | `phoneDefaultCountry`, `phoneAutoDetectCountry`, `phoneStrictValidation` |
| `datetime` | date, time or both | `dateTimeType`, `dateTimeFormatOfDate`, `dateTimeFormatOfTime` |

`fio` shows a middle-name (patronymic) field by default. Most audiences do not use
one: set `fioWithPatronymic` to false unless the person asks for it.

Set `phoneDefaultCountry` to the audience's country (two-letter code such as `US`,
`MX`, `BR`, `ES`).

## Choice

| Type | What it is | Main fields |
|---|---|---|
| `choice` | single or multiple choice, as text or pictures | `choiceType`, `choiceMultiple`, `choiceRandomize`, `choiceTextOther`, `choiceTextIds`, `choiceTextEntities` |
| `dropdown` | choice from a long list | `dropdownMultiple`, `dropdownOther`, `dropdownRandomize`, `dropdownIds`, `dropdownEntities` |
| `yesno` | yes or no | `yesNoTextIds`, `yesNoTextEntities` |
| `ranking` | put items in order | options in `choiceTextIds` and `choiceTextEntities`, as in `choice` |
| `pair` | pairwise comparison | `pairItemIds`, `pairItemEntities`, `pairShowImages`, `pairStepByStep` |

"Other", "Hard to answer" and "None of the above" are switched on with their flags
(`choiceTextOther` or `dropdownOther`, `hardToAnswer`, `noneOfAbove`). Never add them
as ordinary options: they lose the input field and their own line in the report.

Option identifiers must be freshly generated UUIDs. Names like `q2_1` save but the
survey then fails to publish.

## Ratings and scales

| Type | What it is | Main fields |
|---|---|---|
| `rating` | stars, hearts, thumbs, smileys | `ratingCount`, `ratingFigure`, `ratingScores` |
| `smile-rating` | a row of faces | see the schema in `update_quiz_widgets` |
| `scale` | numeric scale with edge labels | `scaleCount`, `scaleStartValue`, `scaleLabelLeftValue`, `scaleLabelRightValue` |
| `nps` | likelihood-to-recommend scale, fixed 0–10 | same fields as `scale` |
| `slider` | slider | `sliderMin`, `sliderMax`, `sliderStep` |
| `matrix` | a set of ratings over one list of criteria | `matrixChoiceType`, `matrixRowIds`, `matrixColIds`, `matrixIsAllRequired` |
| `semantic_differential` | a scale between two opposite words | see the schema in `update_quiz_widgets` |

`nps` is not the same as a ten-point `scale`: it has its own analytics in reports.
For "how likely are you to recommend", use `nps`.

## Images, files, map, embedded

| Type | What it is | Main fields |
|---|---|---|
| `file` | file or photo upload | common fields only |
| `click_test` | clicks on an image, shown as a heatmap | `imageSelectionImageUrl`, `clickTestMinClicks`, `clickTestMaxClicks` |
| `area_select` | choosing marked areas on an image | `imageSelectionImageUrl`, `areaSelectIds`, `areaSelectEntities` |
| `map` | a pin on a map | `mapCenterLat`, `mapCenterLng`, `mapZoom`, `mapMinMarks`, `mapMaxMarks` |
| `html` | custom markup block | `htmlCode`, `htmlIsEmbedded` |
| `booking` | appointment booking against a schedule | `bookingSchedulerId`, `bookingNameWidgetId`, `bookingEmailWidgetId` |

`booking` needs a schedule (`get_schedulers`). Without one the question shows no
free time: warn the person rather than adding it silently.

## Screens without a question

| Type | What it is | Main fields |
|---|---|---|
| `welcome` | welcome screen, always first | `welcomeLabel`, `welcomeWithQuestionCount`, `welcomeWithResponseTime` |
| `message` | a text screen between questions | `messageLabel`, `messageWithButton` |
| `inline_group` | several questions on one screen | `groupWidgets` with its own `ids` and `entities` |
| `submit` | the submit step, always last, with optional consent | `submitLabel`, `submitTerms`, `submitTermsText` |
| `finish` | thank-you screen, added before `submit` | `finishLabel`, `finishActiveType`, `finishNextUrl` |
| `screenout` | end of the road for unsuitable respondents | the jump to it is set in `update_quiz_logic` |

A survey has no `finish` screen until you add one. Editing `submit` does not create
it.

## Commonly confused

- **Ratings are not collected as text.** An `input` asking for "a score from 1 to
  5" destroys the analytics.
- **Option lists are not collected as text.** Free answers cannot be grouped.
- **Phone and email have their own types.** Contacts collected through `input` are
  half unusable.
- **Ten similar ratings are a `matrix`,** not ten `rating` questions in a row.
