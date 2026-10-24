<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › Understand results</sub>

# Report and survey styling

**Tidies up what people see from outside: the survey theme, the report colors and the logo**

| Skill | Version | Tools | Download | Page |
|---|---|:-:|:-:|:-:|
| `surveyninja-report-appearance` | 1.0.1 | 15 | [ZIP](https://surveyninja.io/skills/report-appearance.zip) | [surveyninja.io](https://surveyninja.io/skills/report-appearance) |

## What it does

1. **Looks at existing themes first.** A suitable theme usually exists in the account already. Creating another one just adds something nobody maintains.
2. **Asks concrete questions.** Instead of asking about your brand style, it asks for the main button color, the background and whether there is a logo. Two or three colors are plenty.
3. **Keeps one report separate from the rest.** A new look for one client's report goes into that survey's own settings. The shared palette changes only when you ask, and every report that follows it changes too.
4. **Advises on substance.** Contrast beats beauty: light grey on white is unreadable on a phone, and chart colors have to survive black-and-white printing.

## What you get

| Theme | Colors | Presets | Reports changed |
|:-:|:-:|:-:|:-:|
| **existing** | **2** | **3** | **1** |
| <sub>no new one created</sub> | <sub>button and background</sub> | <sub>one per client</sub> | <sub>of 14</sub> |

| | | |
|---|---|---|
| **Survey theme** | an existing account theme, applied to this survey |  |
| **This survey's report** | own palette and font, shared palette untouched |  |
| **Preset for Client A** | saved for the next reports |  |
| **Logo** | account-wide, shows in every survey and PDF |  |

> **Only one report changed**  
> You asked for new colors in one client's report, so they went into that survey's settings. The other 13 reports keep the shared palette.

<sub>The numbers above are an example. Settings apply to your own account and survey.</sub>

## How to ask

> Give the survey a theme in our brand colors

> Change the chart colors in this survey's report

> Put the company logo on our surveys and reports

## What not to do

- Do not change the shared account palette for one report
- Do not create a new theme when a suitable one exists
- Do not suggest a plan upgrade or lead to payment

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `apply_quiz_theme` | Apply theme to quiz | write |
| `create_report_appearance_preset` | Create report appearance preset | write |
| `create_theme` | Create theme | write |
| `delete_report_appearance_preset` | Delete report appearance preset | destructive |
| `delete_workspace_logo` | Delete workspace logo | destructive |
| `get_theme_details` | Theme details | read |
| `get_theme_list` | Theme list | read |
| `get_workspace_list` | Workspace list | read |
| `get_workspace_report_appearance` | Workspace report appearance | read |
| `manage_theme` | Manage themes | destructive |
| `update_quiz_settings` | Quiz settings | write |
| `update_theme` | Update theme | write |
| `update_workspace_branding` | Workspace logo and copyright | write |
| `update_workspace_report_palette` | Workspace report palette | write |
| `upload_workspace_logo` | Upload workspace logo | write |

## Questions

<details>
<summary><b>What can the skill style?</b></summary>

The survey theme, the chart colors and font in reports, saved report presets for different clients, and the account logo with the SurveyNinja branding line.

</details>

<details>
<summary><b>Will it create a new theme?</b></summary>

Only if nothing suitable exists. It checks the account's themes first and can copy one instead of starting from scratch.

</details>

<details>
<summary><b>What will it ask about my brand?</b></summary>

Concrete things: the main button color, the background and whether you have a logo. A survey rarely needs more than two or three colors.

</details>

<details>
<summary><b>Can I change colors in just one report?</b></summary>

Yes. The skill gives that survey its own report palette and font, and the other reports stay as they are. The shared account palette changes only when you ask for it, after a warning.

</details>

<details>
<summary><b>Will the logo appear in every survey?</b></summary>

Yes. The logo is an account setting, so it shows in every survey, report and PDF of the account. A custom logo and hiding the SurveyNinja branding are not available on every plan, and the skill says so plainly.

</details>

<details>
<summary><b>What do I need for this to work?</b></summary>

A SurveyNinja account and an assistant that connects to MCP servers and loads skills from a folder, such as Claude Code, Codex, Cursor or Gemini CLI. Access goes through your own API key or the Allow access button. The skill itself is a plain text file and runs nothing.

</details>

## Files

- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on
