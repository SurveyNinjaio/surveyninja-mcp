#!/usr/bin/env python3
"""Builds the ChatGPT plugin package: dist/surveyninja-openai.zip with plugin.json, mcp.json, skills and the logo.

Run: python3 scripts/openai_package.py --video <URL of the demo recording>. Python 3.11+, standard library only.
Upload the ZIP at https://platform.openai.com/plugins (Upload new or existing plugin).
"""
import argparse
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
- Every tool is marked as read-only or as changing data. Tools that delete or overwrite data, such as deleting responses, are marked destructive, so ChatGPT asks before it calls them.
- Ready-made skills for common jobs: a survey from a brief, a check before launch, open-answer analysis, sample size, A/B checks, results digests and sharing results.

Who it is for: marketers, product and research teams, HR and anyone who runs surveys in SurveyNinja.

Limitations:
- You need a SurveyNinja account. You sign in with SurveyNinja and choose one workspace; ChatGPT gets the same rights you have there and nothing more, and loses access when you leave the workspace or disconnect.
- Some features, such as the AI report, depend on the workspace plan.
- Up to 180 requests per minute per user. Links to exported files work for one hour.
- Webhooks and new email recipients are created in the SurveyNinja app, so ChatGPT never sends responses to a new outside address on its own. Once they exist, ChatGPT can check them and switch them on."""

POSITIVE = [
    {
        "description": "Lists the account's surveys with response counts.",
        "prompt": "Show my SurveyNinja surveys and how many responses each has.",
        "tools_triggered": ["get_quiz_list"],
        "expected_behavior": "A list of the six sample surveys (Customer satisfaction, Employee engagement, Product feedback, Event registration, Survey basics quiz, Website feedback draft) with their response counts.",
    },
    {
        "description": "Reads a survey's totals and summarizes the complaints in its open answers.",
        "prompt": "How is the Customer satisfaction survey performing? Show views, completed responses and completion rate, and summarize what customers complain about in their open answers.",
        "tools_triggered": ["get_quiz_list", "get_quiz_summary", "get_quiz_report"],
        "expected_behavior": "181 views, 169 completed responses, 11 started but not finished, a 93% completion rate and an average time of about 2:51, plus a short summary of the complaints in the open answers, such as slow support replies and the mobile app.",
    },
    {
        "description": "Explains a draft survey's logic without changing it.",
        "prompt": "Explain the logic of the Website feedback draft in SurveyNinja: where does each answer to the first question lead? Don't publish it.",
        "tools_triggered": ["get_quiz_list", "get_quiz_structure"],
        "expected_behavior": "The draft has four questions. \"Yes\" to \"Did you find what you were looking for?\" jumps to the website rating, \"No\" goes on to \"What were you looking for?\" first. The draft stays unpublished and unchanged.",
    },
    {
        "description": "Creates a short survey and publishes it after confirmation.",
        "prompt": "Create a two-question feedback survey for a café in SurveyNinja and publish it.",
        "tools_triggered": ["create_quiz", "update_quiz_widgets", "publish_quiz"],
        "expected_behavior": "A new survey with two questions; ChatGPT may also build it with generate_ai_quiz. ChatGPT asks for confirmation before publishing, then returns the public link for respondents.",
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


def plugin_manifest(version, video=None):
    manifest = {
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
    if video:
        manifest["extensions"]["com.openai"]["review"]["demo_recording_url"] = video
    return manifest


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


def main(argv=None):
    parser = argparse.ArgumentParser(description="Build the ChatGPT plugin package.")
    parser.add_argument("--video", help="HTTPS link to the demo recording of the review cases, required for the review")
    args = parser.parse_args(argv)
    if args.video and not args.video.startswith("https://"):
        parser.error("--video must be an https:// link")

    version = json.loads((ROOT / "plugin/.claude-plugin/plugin.json").read_text(encoding="utf-8"))["version"]
    shutil.rmtree(BUILD, ignore_errors=True)
    (BUILD / "assets").mkdir(parents=True)
    (BUILD / "plugin.json").write_text(json.dumps(plugin_manifest(version, args.video), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (BUILD / "mcp.json").write_text(json.dumps(mcp_config(), indent=2) + "\n", encoding="utf-8")
    # The plugin icon is the 1024 px logo; assets/logo.png at the root is 500 px
    shutil.copy(ROOT / "plugin/.claude-plugin/icon.png", BUILD / "assets/logo.png")

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
    if not args.video:
        print("no demo recording: the review needs one, build again with --video <URL> before uploading")


if __name__ == "__main__":
    main()
