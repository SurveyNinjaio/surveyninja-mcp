#!/usr/bin/env python3
"""Checks the repository before a commit and in CI: skill headers, tools, manifests, stray secrets.

Run: python3 scripts/check.py. Python 3.11+, standard library only.
"""
import json
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SERVER = "https://mcp.surveyninja.io/mcp/v1"
errors = []


def front_matter(text):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not m:
        return None
    fm, key = {}, None
    for line in m.group(1).splitlines():
        km = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if km:
            key = km.group(1)
            fm[key] = km.group(2).strip()
        elif key and line.startswith("  "):
            fm[key] += " " + line.strip()
    return fm


known_tools = set(re.findall(r"^\| `([a-z0-9_]+)` \|", (ROOT / "docs/tools.md").read_text(encoding="utf-8"), re.M))
if len(known_tools) < 100:
    errors.append(f"docs/tools.md lists only {len(known_tools)} tools")

skills = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
for d in skills:
    skill = d / "SKILL.md"
    if not skill.exists():
        errors.append(f"skills/{d.name}: no SKILL.md")
        continue
    fm = front_matter(skill.read_text(encoding="utf-8"))
    if fm is None:
        errors.append(f"skills/{d.name}: no front matter")
        continue
    extra = set(fm) - {"name", "description"}
    if extra:
        errors.append(f"skills/{d.name}: extra keys in front matter: {', '.join(sorted(extra))}")
    name, desc = fm.get("name", ""), fm.get("description", "")
    if not re.fullmatch(r'"[^"\\]+"', desc):
        errors.append(f"skills/{d.name}: the description must be in double quotes, with no \" or \\ inside")
    desc = desc.strip('"')
    if name != d.name:
        errors.append(f"skills/{d.name}: name {name!r} differs from the folder")
    if not re.fullmatch(r"surveyninja-[a-z0-9-]{1,52}", name):
        errors.append(f"skills/{d.name}: the name must be surveyninja- plus lowercase letters, digits and hyphens")
    if not 40 <= len(desc) <= 1024:
        errors.append(f"skills/{d.name}: the description must be 40 to 1024 characters, it is {len(desc)}")
    if not (d / "README.md").exists():
        errors.append(f"skills/{d.name}: no README.md, run scripts/sync.py")
    if (d / "skill.json").exists():
        errors.append(f"skills/{d.name}: skill.json belongs to the site, run scripts/sync.py")
    yaml = d / "agents/openai.yaml"
    if yaml.exists():
        for tool in re.findall(r'value:\s*"([a-z0-9_]+)"', yaml.read_text(encoding="utf-8")):
            if tool not in known_tools:
                errors.append(f"skills/{d.name}: tool {tool} is not in docs/tools.md")

if len(skills) < 1:
    errors.append("skills/ is empty, run scripts/sync.py")

for f in [ROOT / ".claude-plugin/marketplace.json", ROOT / ".claude-plugin/plugin.json", ROOT / "server.json",
          ROOT / "gemini-extension.json", *sorted((ROOT / "clients").glob("*.json"))]:
    try:
        data = json.loads(f.read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"{f.relative_to(ROOT)}: {e}")
        continue
    if SERVER not in json.dumps(data) and f.name != "marketplace.json":
        errors.append(f"{f.relative_to(ROOT)}: no {SERVER}")

try:
    tomllib.loads((ROOT / "clients/codex.toml").read_text(encoding="utf-8"))
except Exception as e:
    errors.append(f"clients/codex.toml: {e}")

versions = {json.loads((ROOT / p).read_text(encoding="utf-8"))["version"]
            for p in (".claude-plugin/plugin.json", "gemini-extension.json", "server.json")}
if len(versions) != 1:
    errors.append(f"plugin.json, gemini-extension.json and server.json have different versions: {sorted(versions)}")

for f in sorted(ROOT.rglob("*")):
    if not f.is_file() or ".git" in f.parts or f.suffix not in {".md", ".json", ".toml", ".yaml", ".yml", ".py"}:
        continue
    text = f.read_text(encoding="utf-8")
    if re.search(r"[\u0400-\u04FF]", text):
        errors.append(f"{f.relative_to(ROOT)}: has Cyrillic text")
    if re.search(r"(?<![A-Z_])(sk|pk)_live_|Bearer [0-9]+\|[A-Za-z0-9]{20,}", text):
        errors.append(f"{f.relative_to(ROOT)}: looks like a real key")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
for region in ("badges", "glance", "skills"):
    m = re.search(r"<!-- generated:" + region + r" -->\n(.*?)<!-- /generated:" + region + r" -->", readme, re.S)
    if not m or not m.group(1).strip():
        errors.append(f"README.md: the generated:{region} region is empty, run scripts/sync.py")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"ok: {len(skills)} skills, {len(known_tools)} tools, manifests read")
