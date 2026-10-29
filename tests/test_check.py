"""scripts/check.py on a copy of the repository: it passes as committed and catches each kind of breakage."""
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class CheckTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.repo = self.tmp / "repo"
        shutil.copytree(ROOT, self.repo, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        self.skill = sorted(p for p in (self.repo / "skills").iterdir() if p.is_dir())[0]

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def run_check(self):
        return subprocess.run([sys.executable, str(self.repo / "scripts/check.py")], capture_output=True, text=True)

    def edit(self, path, old, new):
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def assert_fails_with(self, message):
        result = self.run_check()
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn(message, result.stdout)

    def test_the_repository_passes(self):
        result = self.run_check()
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertRegex(result.stdout, r"^ok: \d+ skills, \d+ tools")

    def test_an_unquoted_description_fails(self):
        self.edit(self.skill / "SKILL.md", 'description: "', "description: ")
        self.assert_fails_with(f"skills/{self.skill.name}: the description must be in double quotes")

    def test_a_name_that_differs_from_the_folder_fails(self):
        self.edit(self.skill / "SKILL.md", f"name: {self.skill.name}", "name: surveyninja-other")
        self.assert_fails_with("differs from the folder")

    def test_an_extra_front_matter_key_fails(self):
        self.edit(self.skill / "SKILL.md", f"name: {self.skill.name}\n", f"name: {self.skill.name}\nversion: 1.0.0\n")
        self.assert_fails_with("extra keys in front matter: version")

    def test_a_tool_missing_from_the_docs_fails(self):
        yaml = next(p / "agents/openai.yaml" for p in sorted((self.repo / "skills").iterdir()) if (p / "agents/openai.yaml").exists())
        tool = re.search(r'value:\s*"([a-z0-9_]+)"', yaml.read_text(encoding="utf-8")).group(1)
        self.edit(yaml, f'"{tool}"', '"no_such_tool"')
        self.assert_fails_with("tool no_such_tool is not in docs/tools.md")

    def test_the_site_skill_json_must_not_be_copied(self):
        (self.skill / "skill.json").write_text("{}", encoding="utf-8")
        self.assert_fails_with("skill.json belongs to the site")

    def test_manifest_versions_must_match(self):
        path = self.repo / "server.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["version"] = "0.0.1"
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assert_fails_with("have different versions")

    def test_a_manifest_without_the_server_url_fails(self):
        self.edit(self.repo / "gemini-extension.json", "https://mcp.surveyninja.io/mcp/v1", "https://example.com/mcp")
        self.assert_fails_with("gemini-extension.json: no https://mcp.surveyninja.io/mcp/v1")

    def test_broken_json_fails(self):
        (self.repo / "clients/broken.json").write_text("{", encoding="utf-8")
        self.assert_fails_with("clients/broken.json:")

    def test_cyrillic_text_fails(self):
        (self.repo / "docs/note.md").write_text("Survey " + "".join(map(chr, (0x043E, 0x043F, 0x0440))) + "\n", encoding="utf-8")
        self.assert_fails_with("docs/note.md: has Cyrillic text")

    def test_something_like_a_real_key_fails(self):
        (self.repo / "docs/live.md").write_text("key: " + "sk" + "_live_abc\n", encoding="utf-8")
        (self.repo / "docs/bearer.md").write_text("Authorization: Bearer " + "12|" + "a" * 40 + "\n", encoding="utf-8")
        result = self.run_check()
        self.assertEqual(1, result.returncode)
        self.assertIn("docs/live.md: looks like a real key", result.stdout)
        self.assertIn("docs/bearer.md: looks like a real key", result.stdout)

    def test_an_empty_generated_region_fails(self):
        readme = self.repo / "README.md"
        text = readme.read_text(encoding="utf-8")
        text = re.sub(r"(<!-- generated:glance -->\n).*?(<!-- /generated:glance -->)", r"\1\2", text, flags=re.S)
        readme.write_text(text, encoding="utf-8")
        self.assert_fails_with("the generated:glance region is empty")


if __name__ == "__main__":
    unittest.main()
