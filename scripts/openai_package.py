#!/usr/bin/env python3
"""Builds the ChatGPT plugin package: dist/surveyninja-openai.zip with plugin.json, mcp.json, skills and the logo.

Run: python3 scripts/openai_package.py. Python 3.11+, standard library only.
Upload the ZIP at https://platform.openai.com/plugins (Create plugin, With MCP).
"""
import json
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
BUILD = DIST / "openai"
ZIP = DIST / "surveyninja-openai.zip"
SERVER = "https://mcp.surveyninja.io/mcp/v1"

LONG_DESCRIPTION = """SurveyNinja is an online survey builder. This plugin connects ChatGPT to your SurveyNinja account: build a survey from a short description, a template or from scratch, check it before launch, publish it, then read the responses and reports and export them.

Things to ask:
- Build a customer satisfaction survey with an NPS question and a follow-up question for low scores.
- Check my draft for broken logic and unclear questions before I publish it.
- How many responses came in this week, and what do people write in the open answers?
- Export the responses to Excel and the report to PDF.
- Tag the responses that mention pricing.

What it can do:
- More than 160 tools: surveys, questions and logic, design and settings, publishing, responses, the summary, reports with filters, exports to CSV, Excel, Word, SPSS and PDF, public report links, tags, notifications and workspace members.
- Every tool is marked as read-only or as changing data. Tools that cannot be undone, such as deleting a survey or responses, are marked destructive, so ChatGPT asks before it calls them.
- Ready-made skills for common jobs: a survey from a brief, a check before launch, open-answer analysis, sample size, A/B checks, results digests and sharing results.

Who it is for: marketers, product and research teams, HR and anyone who runs surveys in SurveyNinja.

Limitations:
- You need a SurveyNinja account. You sign in with SurveyNinja and choose one workspace; ChatGPT gets the same rights you have there and nothing more, and loses access when you leave the workspace or disconnect.
- Some features, such as the AI report, depend on the workspace plan.
- Up to 180 requests per minute per user. Links to exported files work for one hour.
- Webhooks and new email recipients are set up in the SurveyNinja app: on this connection ChatGPT does not send responses to a new outside address. It then checks them and switches them on."""

POSITIVE = [
    {
        "description": "Lists the account's surveys with response counts.",
        "prompt": "Show my SurveyNinja surveys and how many responses each has.",
        "tools_triggered": ["get_quiz_list"],
        "expected_behavior": "A list of the six sample surveys (Customer satisfaction, Employee engagement, Product feedback, Event registration, Survey basics quiz, Website feedback draft) with their response counts.",
    },
    {
        "description": "Reads the NPS and summarizes why detractors give low scores.",
        "prompt": "What is the NPS of the Customer satisfaction survey, and why do detractors give low scores?",
        "tools_triggered": ["get_quiz_list", "get_quiz_summary", "get_quiz_answers"],
        "expected_behavior": "The NPS of the survey (24) with the share of promoters, passives and detractors, and a short summary of the reasons in the detractors' open answers.",
    },
    {
        "description": "Checks a draft survey before launch without changing it.",
        "prompt": "Check the Website feedback draft in SurveyNinja for broken logic and unclear questions before I publish it.",
        "tools_triggered": ["get_quiz_list", "get_quiz_structure"],
        "expected_behavior": "A list of findings about the draft's questions and logic. The draft stays unpublished and unchanged.",
    },
    {
        "description": "Creates a short survey and publishes it after confirmation.",
        "prompt": "Create a two-question feedback survey for a café in SurveyNinja and publish it.",
        "tools_triggered": ["create_quiz", "update_quiz_widgets", "publish_quiz"],
        "expected_behavior": "A new survey with two questions. ChatGPT asks for confirmation before publishing, then returns the public link for respondents.",
    },
    {
        "description": "Exports responses to an Excel file.",
        "prompt": "Export the responses of the Product feedback survey to Excel.",
        "tools_triggered": ["get_quiz_list", "export_answers_xlsx"],
        "expected_behavior": "A download link to an .xlsx file with the survey's responses; the link works for one hour.",
    },
]

NEGATIVE = [
    {"description": "A weather question is unrelated to surveys; the plugin is not called.", "prompt": "What's the weather in Berlin today?"},
    {"description": "Creative writing is unrelated to surveys; the plugin is not called.", "prompt": "Write a short poem about autumn."},
    {"description": "A translation request does not need survey data; the plugin is not called.", "prompt": "Translate \"Thank you for your feedback\" into Spanish."},
]


def plugin_manifest(version):
    return {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "name": "surveyninja",
        "version": version,
        "description": "Build surveys, read responses and make reports in SurveyNinja: the MCP server and ready-made skills.",
        "author": {"name": "SurveyNinja", "email": "team@surveyninja.io", "url": "https://surveyninja.io"},
        "homepage": "https://surveyninja.io/features/mcp-server",
        "repository": "https://github.com/surveyninjaio/surveyninja-mcp",
        "license": "MIT",
        "keywords": ["surveys", "forms", "quiz", "polls", "feedback", "nps"],
        "extensions": {
            "com.openai": {
                "interface": {
                    "displayName": "SurveyNinja",
                    "shortDescription": "Build surveys, read results",
                    "longDescription": LONG_DESCRIPTION,
                    "developerName": "SurveyNinja",
                    "category": "Productivity",
                    "websiteURL": "https://surveyninja.io",
                    "supportURL": "https://surveyninja.io/support",
                    "privacyPolicyURL": "https://surveyninja.io/privacy",
                    "termsOfServiceURL": "https://surveyninja.io/agreement",
                    "defaultPrompt": [
                        "Build an NPS survey for my customers with a follow-up question for low scores.",
                        "How many responses did my surveys get this week?",
                        "Summarize the open answers of my latest survey.",
                    ],
                    "logo": "./assets/logo.png",
                    "composerIcon": "./assets/logo.png",
                },
                "review": {"test_cases": {"positive": POSITIVE, "negative": NEGATIVE}},
                "publication": {"release_notes": "Initial release: build and check surveys, read responses and reports, export results."},
            }
        },
    }


def mcp_config():
    return {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json",
        "mcpServers": {
            "surveyninja": {
                "type": "streamable-http",
                "url": SERVER,
                "extensions": {"com.openai": {"auth": {"type": "oauth", "client": {"mode": "dcr"}}}},
            }
        },
    }


def main():
    version = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))["version"]
    shutil.rmtree(BUILD, ignore_errors=True)
    (BUILD / "assets").mkdir(parents=True)
    (BUILD / "plugin.json").write_text(json.dumps(plugin_manifest(version), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (BUILD / "mcp.json").write_text(json.dumps(mcp_config(), indent=2) + "\n", encoding="utf-8")
    shutil.copy(ROOT / "assets/logo.png", BUILD / "assets/logo.png")

    skills = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
    for d in skills:
        # README.md is the human install page of a skill; the package needs only what the model reads.
        shutil.copytree(d, BUILD / "skills" / d.name, ignore=shutil.ignore_patterns("README.md"))

    ZIP.unlink(missing_ok=True)
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(BUILD.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(BUILD))
    print(f"{ZIP}: {len(skills)} skills, version {version}")


if __name__ == "__main__":
    main()
