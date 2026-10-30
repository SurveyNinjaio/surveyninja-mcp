"""scripts/sync.py: its helpers, and a full run from a small site repository into a copy of this one."""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import sync  # noqa: E402

CONFIG = """<?php
return [
    'groups' => ['build', 'read'],
    'default_group' => 'read',
    'order' => [
        'second', 'first',
    ],
];
"""

LANG = """<?php
return [
    'groups' => [
        'build' => 'Build and share',
        'read' => 'Understand results',
    ],
];
"""

TOOLS = {
    "tools": {
        "get_quiz_list": {"title": "List surveys", "read_only": True},
        "create_quiz": {"title": "Create a survey"},
        "delete_quiz": {"title": "Delete a survey", "destructive": True},
        "hidden_tool": {"title": "Not in any section", "read_only": True},
    }
}

SKILL = """---
name: surveyninja-{slug}
description: "A test skill that does one {slug} job with the SurveyNinja MCP tools."
---

# Test

## What not to do

- **Never delete a survey without asking.** The user decides.
- **Never invent numbers**
"""


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def make_skill(site, slug, group, tools):
    d = site / f"resources/skills/en/surveyninja-{slug}"
    write(d / "SKILL.md", SKILL.format(slug=slug))
    write(d / "skill.json", json.dumps({
        "version": "1.2.0",
        "group": group,
        "site": {"en": {
            "title": f"Skill {slug}",
            "tagline": f"Does the {slug} job | fast",
            "highlights": [["One thing", "it does."], ["Another thing?", "It does too."]],
            "prompts": [f"Run the {slug} job"],
            "faq": [["Is it free?", "Yes."]],
        }},
    }))
    write(d / "references/notes.md", "Notes.\n")
    if tools:
        write(d / "agents/openai.yaml", "dependencies:\n  tools:\n" + "".join(
            f'    - type: "mcp"\n      value: "{t}"\n' for t in tools))


def git(site, *args):
    subprocess.run(["git", "-C", str(site), "-c", "user.name=test", "-c", "user.email=test@example.com", *args],
                   check=True, capture_output=True)


class HelpersTest(unittest.TestCase):
    def test_php_list_and_map(self):
        self.assertEqual(["build", "read"], sync.php_list(CONFIG, "groups"))
        self.assertEqual(["second", "first"], sync.php_list(CONFIG, "order"))
        self.assertEqual({"build": "Build and share", "read": "Understand results"}, sync.php_map(LANG, "groups"))

    def test_php_list_stops_on_a_missing_key(self):
        with self.assertRaises(SystemExit):
            sync.php_list(CONFIG, "missing")

    def test_never_rules(self):
        body = SKILL.format(slug="x") + "\n## Next\n\n- **Not a rule.**\n"
        self.assertEqual(["Never delete a survey without asking", "Never invent numbers"], sync.never_rules(body))
        self.assertEqual([], sync.never_rules("# No such section\n"))

    def test_kind(self):
        self.assertEqual("destructive", sync.kind({"destructive": True, "read_only": True}))
        self.assertEqual("read", sync.kind({"read_only": True}))
        self.assertEqual("write", sync.kind({}))

    def test_cell_escapes_pipes_and_newlines(self):
        self.assertEqual("a \\| b c", sync.cell("a | b\nc"))

    def test_bar_is_clamped_to_ten(self):
        self.assertEqual("█████░░░░░", sync.bar(50))
        self.assertEqual("░" * 10, sync.bar(-5))
        self.assertEqual("█" * 10, sync.bar(140))

    def test_replace_region(self):
        text = "a\n<!-- generated:x -->\nold\n<!-- /generated:x -->\nb\n"
        self.assertEqual("a\n<!-- generated:x -->\nnew\n<!-- /generated:x -->\nb\n", sync.replace_region(text, "x", "new\n"))
        with self.assertRaises(SystemExit):
            sync.replace_region(text, "y", "new\n")

    def test_tools_doc_skips_unknown_tools_and_empty_sections(self):
        tools = {k: v for k, v in TOOLS["tools"].items() if k != "hidden_tool"}
        doc = sync.tools_doc(tools, {"Surveys": ["get_quiz_list", "create_quiz", "gone_tool"], "Empty": ["gone_tool"],
                                     "Danger zone": ["delete_quiz"]})
        self.assertIn("3 tools by section. 1 only read. 1 delete or overwrite", doc)
        self.assertIn("| `delete_quiz` | Delete a survey | destructive |", doc)
        self.assertIn("[Danger zone](#danger-zone) <sub>1</sub>", doc)
        self.assertNotIn("gone_tool", doc)
        self.assertNotIn("## Empty", doc)
        self.assertNotIn("API key only", doc)

    def test_tools_doc_marks_api_key_only_tools(self):
        tools = {"get_quiz_list": {"title": "List surveys", "read_only": True},
                 "create_quiz_webhook": {"title": "Create webhook", "api_key_only": True}}
        doc = sync.tools_doc(tools, {"Webhooks": ["get_quiz_list", "create_quiz_webhook"]})
        self.assertIn("1 tool works only when you connect with an API key", doc)
        self.assertIn("| `create_quiz_webhook` | Create webhook | write, *API key only* |", doc)
        self.assertIn("| `get_quiz_list` | List surveys | read |", doc)


class RunTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.repo = self.tmp / "repo"
        shutil.copytree(ROOT, self.repo, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        write(self.repo / "scripts/tool-sections.json", json.dumps({
            "Surveys": ["get_quiz_list", "create_quiz"],
            "Danger zone": ["delete_quiz"],
        }))
        write(self.repo / "skills/surveyninja-removed/SKILL.md", "old\n")

        self.site = self.tmp / "site"
        write(self.site / "config/skills.php", CONFIG)
        write(self.site / "resources/lang/en/skills.php", LANG)
        write(self.site / "resources/skills/tools.json", json.dumps(TOOLS))
        write(self.site / "resources/skills/CHANGELOG.md", "# Skills changelog\n")
        make_skill(self.site, "first", "build", ["get_quiz_list"])
        make_skill(self.site, "second", "build", ["create_quiz", "delete_quiz"])
        make_skill(self.site, "third", "read", [])
        git(self.site, "init", "-q")
        git(self.site, "add", ".")
        git(self.site, "commit", "-q", "-m", "skills")

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def run_sync(self, *args):
        return subprocess.run([sys.executable, str(self.repo / "scripts/sync.py"), "--from", str(self.site), *args],
                              capture_output=True, text=True)

    def read(self, path):
        return (self.repo / path).read_text(encoding="utf-8")

    def test_it_writes_the_skills_and_the_docs(self):
        result = self.run_sync()
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("synced 3 skills and 3 tools", result.stdout)
        self.assertIn("left out of the docs: hidden_tool", result.stdout)

        skills = sorted(p.name for p in (self.repo / "skills").iterdir() if p.is_dir())
        self.assertEqual(["surveyninja-first", "surveyninja-second", "surveyninja-third"], skills)
        second = self.repo / "skills/surveyninja-second"
        self.assertFalse((second / "skill.json").exists())
        self.assertTrue((second / "references/notes.md").exists())
        self.assertEqual("# Skills changelog\n", self.read("skills/CHANGELOG.md"))

        plugin = sorted(p.name for p in (self.repo / "plugin/skills").iterdir())
        self.assertEqual(["surveyninja-first", "surveyninja-second", "surveyninja-third"], plugin, "stale skills are gone")
        self.assertTrue((self.repo / "plugin/skills/surveyninja-second/references/notes.md").exists())
        self.assertEqual([], list((self.repo / "plugin/skills").rglob("README.md")), "the plugin copy has no READMEs")
        self.assertEqual(self.read("LICENSE"), self.read("plugin/LICENSE"))

        readme = self.read("skills/surveyninja-second/README.md")
        self.assertIn("# Skill second", readme)
        self.assertIn("| `surveyninja-second` | 1.2.0 | 2 | [ZIP](https://surveyninja.io/skills/second.zip) |", readme)
        self.assertIn("1. **One thing.** it does.", readme)
        self.assertIn("2. **Another thing?** It does too.", readme)
        self.assertIn("- Never delete a survey without asking", readme)
        self.assertIn("| `delete_quiz` | Delete a survey | destructive |", readme)
        self.assertIn("<summary><b>Is it free?</b></summary>", readme)
        self.assertIn("- [`agents/openai.yaml`](agents/openai.yaml)", readme)
        self.assertNotIn("Tools it calls", self.read("skills/surveyninja-third/README.md"))

        index = self.read("skills/README.md")
        self.assertIn("3 skills.", index)
        # The site's order puts second before first inside a group
        self.assertLess(index.index("Skill second"), index.index("Skill first"))
        self.assertIn("Does the first job \\| fast", index)

        tools = self.read("docs/tools.md")
        self.assertIn("3 tools by section.", tools)
        self.assertNotIn("hidden_tool", tools)
        self.assertIn("- “Run the third job”", self.read("docs/prompts.md"))

        root = self.read("README.md")
        self.assertIn("badge/skills-3-", root)
        self.assertIn("badge/tools-3%2B-", root)
        self.assertIn("| **Tools** | 3+: 1 only read, 1 delete or overwrite data", root)
        self.assertIn("| [Skill third](skills/surveyninja-third/) |", root)

    def test_it_refuses_uncommitted_skills(self):
        write(self.site / "resources/skills/en/surveyninja-first/SKILL.md", "edited\n")
        result = self.run_sync()
        self.assertNotEqual(0, result.returncode)
        self.assertIn("uncommitted edits", result.stderr)
        self.assertTrue((self.repo / "skills/surveyninja-removed").exists(), "nothing is written")

        result = self.run_sync("--allow-dirty")
        self.assertEqual(0, result.returncode, result.stderr)

    def test_it_refuses_a_skill_that_uses_a_tool_without_a_section(self):
        make_skill(self.site, "fourth", "read", ["hidden_tool"])
        git(self.site, "add", ".")
        git(self.site, "commit", "-q", "-m", "fourth")
        result = self.run_sync()
        self.assertNotEqual(0, result.returncode)
        self.assertIn("surveyninja-fourth uses tools that are not in scripts/tool-sections.json: hidden_tool", result.stderr)

    def test_it_refuses_a_folder_without_skills(self):
        result = subprocess.run([sys.executable, str(self.repo / "scripts/sync.py"), "--from", str(self.tmp)],
                                capture_output=True, text=True)
        self.assertNotEqual(0, result.returncode)
        self.assertIn("has no resources/skills/en", result.stderr)


if __name__ == "__main__":
    unittest.main()
