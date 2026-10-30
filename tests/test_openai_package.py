"""scripts/openai_package.py: listing limits and review cases of the ChatGPT package, and a build into a temporary folder."""
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import openai_package  # noqa: E402


class ManifestTest(unittest.TestCase):
    def setUp(self):
        self.ext = openai_package.plugin_manifest("1.0.0")["extensions"]["com.openai"]
        self.interface = self.ext["interface"]

    def test_listing_fits_the_limits(self):
        self.assertLessEqual(len(self.interface["displayName"]), 30)
        self.assertLessEqual(len(self.interface["shortDescription"]), 30)
        self.assertLessEqual(len(self.interface["longDescription"]), 4000)
        self.assertLessEqual(len(self.interface["developerName"]), 80)
        self.assertLessEqual(len(self.interface["defaultPrompt"]), 3)
        for prompt in self.interface["defaultPrompt"]:
            self.assertLessEqual(len(prompt), 128)

    def test_listing_urls_are_https(self):
        for key in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
            self.assertTrue(self.interface[key].startswith("https://"), key)

    def test_review_has_five_positive_and_three_negative_cases(self):
        cases = self.ext["review"]["test_cases"]
        self.assertEqual(len(cases["positive"]), 5)
        self.assertEqual(len(cases["negative"]), 3)
        for case in cases["positive"]:
            self.assertTrue(case["prompt"] and case["tools_triggered"] and case["expected_behavior"])

    def test_package_carries_no_reviewer_credentials(self):
        self.assertNotIn("test_credentials", self.ext["review"])
        self.assertNotIn("reviewer_instructions", self.ext["review"])

    def test_server_uses_oauth_with_dynamic_registration(self):
        server = openai_package.mcp_config()["mcpServers"]["surveyninja"]
        self.assertEqual(server["url"], openai_package.SERVER)
        self.assertEqual(server["extensions"]["com.openai"]["auth"], {"type": "oauth", "client": {"mode": "dcr"}})


class BuildTest(unittest.TestCase):
    def test_build_writes_the_zip_with_every_skill_and_no_readmes(self):
        with tempfile.TemporaryDirectory() as tmp:
            dist = Path(tmp)
            with mock.patch.multiple(openai_package, DIST=dist, BUILD=dist / "openai", ZIP=dist / "p.zip"):
                openai_package.main()
            names = zipfile.ZipFile(dist / "p.zip").namelist()
        self.assertIn("plugin.json", names)
        self.assertIn("mcp.json", names)
        self.assertIn("assets/logo.png", names)
        self.assertFalse(any(n.endswith("README.md") for n in names))
        skills = {n.split("/")[1] for n in names if n.startswith("skills/")}
        self.assertEqual(skills, {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()})
        for skill in skills:
            self.assertIn(f"skills/{skill}/SKILL.md", names)


if __name__ == "__main__":
    unittest.main()
