<sub><a href="../README.md">SurveyNinja MCP</a> › Skills</sub>

# SurveyNinja skills

25 skills. A skill is a folder with a `SKILL.md` file: plain-language instructions that tell the
assistant how to do one job with the SurveyNinja MCP tools. The assistant picks a skill up by itself when your
request fits, so there is no need to name it.

Skills contain no code and run nothing. All they need is the [MCP server](../README.md#quick-start) connected
to your SurveyNinja account. Versions and changes are in [CHANGELOG.md](CHANGELOG.md).

### Build and share

| Skill | What you get | Download |
|---|---|:-:|
| [Build a survey from a brief](surveyninja-survey-from-brief/) | Describe what you need in plain words, and the assistant builds the survey in your SurveyNinja account as a draft | [ZIP](https://surveyninja.io/skills/survey-from-brief.zip) |
| [Skip logic and branching](surveyninja-survey-logic/) | Sets up survey logic so that no respondent ever hits a dead end | [ZIP](https://surveyninja.io/skills/survey-logic.zip) |
| [Rewrite survey copy](surveyninja-survey-copy/) | Rewrites your questions so people finish the survey, starting from the data rather than taste | [ZIP](https://surveyninja.io/skills/survey-copy.zip) |
| [Distribute the survey](surveyninja-survey-distribution/) | Gets the survey ready to hand out so you can still tell which channel each response came from | [ZIP](https://surveyninja.io/skills/survey-distribution.zip) |
| [Launch kit](surveyninja-launch-kit/) | Puts the whole launch together at once: labeled links, announcement copy for each channel and a QR code | [ZIP](https://surveyninja.io/skills/launch-kit.zip) |

### Check before launch

| Skill | What you get | Download |
|---|---|:-:|
| [Pre-launch check](surveyninja-prelaunch-check/) | Finds what will break on real respondents while the link is still unsent | [ZIP](https://surveyninja.io/skills/prelaunch-check.zip) |
| [Data quality check](surveyninja-data-quality/) | Tells you whether the responses can be trusted before anyone builds conclusions on them | [ZIP](https://surveyninja.io/skills/data-quality.zip) |

### Understand results

| Skill | What you get | Download |
|---|---|:-:|
| [Survey results summary](surveyninja-results-digest/) | Answers "so what did the survey say" with figures and a conclusion instead of a raw export | [ZIP](https://surveyninja.io/skills/results-digest.zip) |
| [Analyze open-ended answers](surveyninja-open-answers/) | Turns a hundred lines of free text into a handful of themes with numbers and quotes | [ZIP](https://surveyninja.io/skills/open-answers.zip) |
| [Completion funnel](surveyninja-response-funnel/) | Shows which question makes people close the tab, and why | [ZIP](https://surveyninja.io/skills/response-funnel.zip) |
| [A/B variant analysis](surveyninja-ab-significance/) | Tells you whether the difference between variants is real or just noise | [ZIP](https://surveyninja.io/skills/ab-significance.zip) |
| [Comparing with past results](surveyninja-benchmark/) | Compares a survey with its own past, because one figure means little and a change says a lot | [ZIP](https://surveyninja.io/skills/benchmark.zip) |
| [How many responses you need](surveyninja-sample-size/) | Tells you whether what you have is enough and how many more responses you need before conclusions hold | [ZIP](https://surveyninja.io/skills/sample-size.zip) |
| [Survey timeline](surveyninja-survey-timeline/) | Answers “why did responses stop” by lining up collection against the edit history | [ZIP](https://surveyninja.io/skills/survey-timeline.zip) |
| [Comparing traffic sources](surveyninja-source-dashboard/) | Shows which channel brought the right people and which only brought numbers | [ZIP](https://surveyninja.io/skills/source-dashboard.zip) |
| [Results for the client](surveyninja-results-sharing/) | Turns survey results into something you can send: a link, a file or a report with conclusions | [ZIP](https://surveyninja.io/skills/results-sharing.zip) |
| [Report and survey styling](surveyninja-report-appearance/) | Tidies up what people see from outside: the survey theme, the report colors and the logo | [ZIP](https://surveyninja.io/skills/report-appearance.zip) |

### Deliver responses

| Skill | What you get | Download |
|---|---|:-:|
| [New response notifications](surveyninja-answer-notifications/) | Sets up where new responses are announced, by email or in Telegram, and fixes it when they stop arriving | [ZIP](https://surveyninja.io/skills/answer-notifications.zip) |
| [Webhook setup](surveyninja-webhook-setup/) | Sends survey responses to your own address and checks that the receiver accepted them | [ZIP](https://surveyninja.io/skills/webhook-setup.zip) |
| [Why responses are not delivered](surveyninja-integration-triage/) | Finds why responses never reach your Telegram, Google Sheet, Zapier or webhook, and what to do about it | [ZIP](https://surveyninja.io/skills/integration-triage.zip) |
| [Lead quality](surveyninja-lead-quality/) | Counts the people who left a contact you can actually use | [ZIP](https://surveyninja.io/skills/lead-quality.zip) |

### Keep the account tidy

| Skill | What you get | Download |
|---|---|:-:|
| [Workspace audit](surveyninja-account-audit/) | Shows in one report where your workspace is losing responses, storage and attention | [ZIP](https://surveyninja.io/skills/account-audit.zip) |
| [Tidying up the account](surveyninja-workspace-housekeeping/) | Sorts, archives, copies and cleans, and knows which of those cannot be undone | [ZIP](https://surveyninja.io/skills/workspace-housekeeping.zip) |
| [Members and access](surveyninja-workspace-access/) | Finds out why a colleague cannot see the surveys and grants exactly the rights they need | [ZIP](https://surveyninja.io/skills/workspace-access.zip) |
| [Cleaning up responses](surveyninja-answers-cleanup/) | Removes test runs and duplicates from your results and shows you the list before anything goes | [ZIP](https://surveyninja.io/skills/answers-cleanup.zip) |

All skills in one archive: [all.zip](https://surveyninja.io/skills/all.zip).

## Installing

**Claude Code, as a plugin.** Installs the skills and the MCP server at once:

```text
/plugin marketplace add surveyninjaio/surveyninja-mcp
/plugin install surveyninja@surveyninja
```

**Any assistant, one command.** [skills](https://skills.sh) finds the agents you have installed and asks where
to put the skills:

```bash
npx skills add surveyninjaio/surveyninja-mcp
```

**Any assistant, from an archive.** Download a skill's ZIP from the table above or all of them at once, unzip it
into the folder your assistant reads skills from and restart the assistant:

| Assistant | Folder in your project |
|---|---|
| Claude Code | `.claude/skills/` |
| Codex, Cursor | `.agents/skills/` |
| Gemini CLI | `.gemini/skills/` |

Your assistant is not in the table? Try `.agents/skills/`, most clients read it.
