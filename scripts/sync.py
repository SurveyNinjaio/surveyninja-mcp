#!/usr/bin/env python3
"""Rebuild the skills and the generated docs from the SurveyNinja site repository.

The skills live in the site repository (resources/skills), where `php artisan skills` checks them
against the MCP server. This script copies them here and writes everything derived from them:

- skills/<name>/      the skill files, without the site's skill.json, plus a README.md
- skills/README.md    the catalog by group
- skills/CHANGELOG.md the skills' changelog
- docs/tools.md       the MCP tools by section: only the tools listed in scripts/tool-sections.json
- docs/prompts.md     starter phrases from the skills
- README.md           the parts between <!-- generated:NAME --> and <!-- /generated:NAME -->

Run: python3 scripts/sync.py --from ../../ninja-land, then python3 scripts/check.py.
The site's skills must be committed: --allow-dirty syncs uncommitted edits too. Python 3.11+, standard library only.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/surveyninjaio/surveyninja-mcp"
SITE = "https://surveyninja.io"
SERVER = "https://mcp.surveyninja.io/mcp/v1"
PREFIX = "surveyninja-"


def php_list(text, key):
    """Quoted strings of a flat PHP array: 'key' => ['a', 'b', ...]."""
    m = re.search(r"'" + re.escape(key) + r"'\s*=>\s*\[(.*?)\]", text, re.S)
    if not m:
        sys.exit(f"cannot find '{key}' in the PHP file")
    return re.findall(r"'([a-z0-9-]+)'", m.group(1))


def php_map(text, key):
    """A flat PHP map of strings: 'key' => ['a' => 'A', ...]."""
    m = re.search(r"'" + re.escape(key) + r"'\s*=>\s*\[(.*?)\]", text, re.S)
    if not m:
        sys.exit(f"cannot find '{key}' in the PHP file")
    return dict(re.findall(r"'([a-z0-9-]+)'\s*=>\s*'([^']*)'", m.group(1)))


def never_rules(body):
    """The bold rule of each item in "## What not to do", as the site shows them."""
    m = re.search(r"^## What not to do\s*\n(.*?)(?=^## |\Z)", body, re.M | re.S)
    if not m:
        return []
    return [r.strip().rstrip(".") for r in re.findall(r"^- \*\*(.+?)\*\*", m.group(1), re.M)]


def kind(tool):
    if tool.get("destructive"):
        return "destructive"
    return "read" if tool.get("read_only") else "write"


def cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def zip_url(slug):
    return f"{SITE}/skills/{slug}.zip"


def page_url(slug):
    return f"{SITE}/skills/{slug}"


def bar(percent):
    filled = max(0, min(10, round(float(percent) / 10)))
    return "█" * filled + "░" * (10 - filled)


def load(source):
    skills_root = source / "resources/skills/en"
    tools = json.loads((source / "resources/skills/tools.json").read_text(encoding="utf-8"))["tools"]
    config = (source / "config/skills.php").read_text(encoding="utf-8")
    groups = php_list(config, "groups")
    order = php_list(config, "order")
    labels = php_map((source / "resources/lang/en/skills.php").read_text(encoding="utf-8"), "groups")

    skills = []
    for d in sorted(p for p in skills_root.iterdir() if (p / "SKILL.md").is_file()):
        body = (d / "SKILL.md").read_text(encoding="utf-8")
        meta = json.loads((d / "skill.json").read_text(encoding="utf-8"))
        slug = d.name[len(PREFIX):]
        yaml = d / "agents/openai.yaml"
        deps = re.findall(r'value:\s*"([a-z0-9_]+)"', yaml.read_text(encoding="utf-8")) if yaml.exists() else []
        skills.append({
            "dir": d,
            "name": d.name,
            "slug": slug,
            "version": meta["version"],
            "group": meta["group"],
            "card": meta["site"]["en"],
            "never": never_rules(body),
            "tools": sorted(deps),
        })

    rank = {slug: i for i, slug in enumerate(order)}
    skills.sort(key=lambda s: (groups.index(s["group"]), rank.get(s["slug"], len(rank)), s["slug"]))
    return skills, tools, groups, labels


def skill_readme(s, tools, label):
    c = s["card"]
    out = [
        f'<sub><a href="../../README.md">SurveyNinja MCP</a> › <a href="../README.md">Skills</a> › {label}</sub>',
        "",
        f"# {c['title']}",
        "",
        f"**{c['tagline']}**",
        "",
        "| Skill | Version | Tools | Download | Page |",
        "|---|---|:-:|:-:|:-:|",
        f"| `{s['name']}` | {s['version']} | {len(s['tools'])} | [ZIP]({zip_url(s['slug'])}) | [surveyninja.io]({page_url(s['slug'])}) |",
        "",
        "## What it does",
        "",
    ]
    for i, (head, text) in enumerate(c.get("highlights", []), 1):
        out.append(f"{i}. **{head}.** {text}" if not head.endswith((".", "?", "!")) else f"{i}. **{head}** {text}")
    out.append("")

    p = c.get("preview") or {}
    if p:
        out += [f"## {p.get('title') or 'What you get'}", ""]
        if p.get("head"):
            out += [f"**{p['head']}**", ""]
        tiles = p.get("tiles") or []
        if tiles:
            out.append("| " + " | ".join(cell(t["label"]) for t in tiles) + " |")
            out.append("|" + ":-:|" * len(tiles))
            out.append("| " + " | ".join(f"**{cell(t['value'])}**" for t in tiles) + " |")
            if any(t.get("hint") for t in tiles):
                out.append("| " + " | ".join(f"<sub>{cell(t['hint'])}</sub>" if t.get("hint") else "" for t in tiles) + " |")
            out.append("")
        rows = p.get("rows") or []
        if rows:
            out += ["| | | |", "|---|---|---|"]
            for r in rows:
                out.append(f"| **{cell(r['title'])}** | {cell(r['meta'])} | {cell(r.get('value') or '')} |")
            out.append("")
        bars = p.get("bars") or []
        if bars:
            out += ["| | | |", "|---|---|---|"]
            for b in bars:
                out.append(f"| {cell(b['label'])} | `{bar(b['percent'])}` | {cell(b['value'])} |")
            out.append("")
        if p.get("callout"):
            out += [f"> **{p['callout']['title']}**  ", f"> {p['callout']['text']}", ""]
        if p.get("note"):
            out += [f"<sub>{p['note']}</sub>", ""]

    out += ["## How to ask", ""]
    for prompt in c.get("prompts", []):
        out += [f"> {prompt}", ""]

    if s["never"]:
        out += ["## What not to do", ""]
        out += [f"- {rule}" for rule in s["never"]]
        out.append("")

    if s["tools"]:
        out += ["## Tools it calls", "", "| Tool | What it does | Kind |", "|---|---|---|"]
        for t in s["tools"]:
            out.append(f"| `{t}` | {cell(tools[t]['title'])} | {kind(tools[t])} |")
        out.append("")

    if c.get("faq"):
        out += ["## Questions", ""]
        for q, a in c["faq"]:
            out += ["<details>", f"<summary><b>{q}</b></summary>", "", a, "", "</details>", ""]

    out += ["## Files", "", "- [`SKILL.md`](SKILL.md): the skill itself, instructions for the assistant"]
    refs = s["dir"] / "references"
    if refs.is_dir():
        for f in sorted(refs.iterdir()):
            out.append(f"- [`references/{f.name}`](references/{f.name}): reference the skill reads when it needs it")
    if (s["dir"] / "agents/openai.yaml").exists():
        out.append("- [`agents/openai.yaml`](agents/openai.yaml): the MCP tools the skill depends on")
    return "\n".join(out) + "\n"


def catalog_tables(skills, groups, labels, link_prefix):
    out = []
    for g in groups:
        members = [s for s in skills if s["group"] == g]
        if not members:
            continue
        out += [f"### {labels.get(g, g)}", "", "| Skill | What you get | Download |", "|---|---|:-:|"]
        for s in members:
            out.append(f"| [{s['card']['title']}]({link_prefix}{s['name']}/) | {cell(s['card']['tagline'])} | [ZIP]({zip_url(s['slug'])}) |")
        out.append("")
    return out


def skills_index(skills, groups, labels):
    out = [
        '<sub><a href="../README.md">SurveyNinja MCP</a> › Skills</sub>',
        "",
        "# SurveyNinja skills",
        "",
        f"{len(skills)} skills. A skill is a folder with a `SKILL.md` file: plain-language instructions that tell the",
        "assistant how to do one job with the SurveyNinja MCP tools. The assistant picks a skill up by itself when your",
        "request fits, so there is no need to name it.",
        "",
        "Skills contain no code and run nothing. All they need is the [MCP server](../README.md#quick-start) connected",
        "to your SurveyNinja account. Versions and changes are in [CHANGELOG.md](CHANGELOG.md).",
        "",
    ]
    out += catalog_tables(skills, groups, labels, "")
    out += [
        f"All skills in one archive: [all.zip]({SITE}/skills/all.zip).",
        "",
        "## Installing",
        "",
        "**Claude Code, as a plugin.** Installs the skills and the MCP server at once:",
        "",
        "```text",
        "/plugin marketplace add surveyninjaio/surveyninja-mcp",
        "/plugin install surveyninja@surveyninja",
        "```",
        "",
        "**Any assistant, one command.** [skills](https://skills.sh) finds the agents you have installed and asks where",
        "to put the skills:",
        "",
        "```bash",
        "npx skills add surveyninjaio/surveyninja-mcp",
        "```",
        "",
        "**Any assistant, from an archive.** Download a skill's ZIP from the table above or all of them at once, unzip it",
        "into the folder your assistant reads skills from and restart the assistant:",
        "",
        "| Assistant | Folder in your project |",
        "|---|---|",
        "| Claude Code | `.claude/skills/` |",
        "| Codex, Cursor | `.agents/skills/` |",
        "| Gemini CLI | `.gemini/skills/` |",
        "",
        "Your assistant is not in the table? Try `.agents/skills/`, most clients read it.",
    ]
    return "\n".join(out) + "\n"


def tools_doc(tools, sections):
    reads = sum(1 for t in tools.values() if t.get("read_only"))
    destructive = sum(1 for t in tools.values() if t.get("destructive"))
    sections = {name: [t for t in names if t in tools] for name, names in sections.items()}
    sections = {name: names for name, names in sections.items() if names}
    out = [
        '<sub><a href="../README.md">SurveyNinja MCP</a> › Tools</sub>',
        "",
        "# SurveyNinja MCP tools",
        "",
        f"{len(tools)} tools by section. {reads} only read. {destructive} delete or overwrite data and carry the",
        "`destructiveHint` annotation, so your client can ask before it calls them. The rest create or change data, and",
        "some act at once: publishing a survey or inviting a member, for example.",
        "",
        "Your client gets the server's own list with `tools/list` when it connects. Tool names say `quiz` where the app",
        "says survey: they mean the same thing.",
        "",
        " &nbsp;|&nbsp; ".join(f"[{name}](#{re.sub(r'[^a-z0-9 -]', '', name.lower()).replace(' ', '-')}) <sub>{len(names)}</sub>"
                 for name, names in sections.items()),
        "",
    ]
    for name, names in sections.items():
        out += [f"## {name}", "", "| Tool | What it does | Kind |", "|---|---|---|"]
        out += [f"| `{t}` | {cell(tools[t]['title'])} | {kind(tools[t])} |" for t in names]
        out.append("")
    return "\n".join(out)


def prompts_doc(skills, groups, labels):
    out = [
        '<sub><a href="../README.md">SurveyNinja MCP</a> › What to ask</sub>',
        "",
        "# What to ask",
        "",
        "Starter phrases from the skills. A skill starts by itself when the request fits, so there is no need to name it.",
        "",
    ]
    for g in groups:
        members = [s for s in skills if s["group"] == g]
        if not members:
            continue
        out += [f"## {labels.get(g, g)}", ""]
        for s in members:
            out += [f"**[{s['card']['title']}](../skills/{s['name']}/)**", ""]
            out += [f"- “{p}”" for p in s["card"].get("prompts", [])]
            out.append("")
    return "\n".join(out)


def replace_region(text, name, content):
    pattern = re.compile(r"(<!-- generated:" + name + r" -->\n).*?(<!-- /generated:" + name + r" -->)", re.S)
    if not pattern.search(text):
        sys.exit(f"README.md has no generated:{name} region")
    return pattern.sub(lambda m: m.group(1) + content + m.group(2), text)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--from", dest="source", default=str(ROOT.parent.parent / "ninja-land"),
                        help="path to the SurveyNinja site repository")
    parser.add_argument("--allow-dirty", action="store_true", help="sync uncommitted edits of the site's skills too")
    args = parser.parse_args()
    source = Path(args.source).resolve()
    if not (source / "resources/skills/en").is_dir():
        sys.exit(f"{source} has no resources/skills/en")
    dirty = subprocess.run(["git", "-C", str(source), "status", "--porcelain", "--", "resources/skills", "config/skills.php"],
                           capture_output=True, text=True).stdout.strip()
    if dirty and not args.allow_dirty:
        sys.exit("the site's skills have uncommitted edits; commit them first, or pass --allow-dirty\n" + dirty)

    skills, tools, groups, labels = load(source)
    sections = json.loads((ROOT / "scripts/tool-sections.json").read_text(encoding="utf-8"))
    # Only the tools placed in a section are documented; a new server tool waits until it gets one
    listed = {t for names in sections.values() for t in names}
    left_out = sorted(set(tools) - listed)
    tools = {name: t for name, t in tools.items() if name in listed}
    for s in skills:
        missing = [t for t in s["tools"] if t not in tools]
        if missing:
            sys.exit(f"{s['name']} uses tools that are not in scripts/tool-sections.json: {', '.join(missing)}")

    target = ROOT / "skills"
    target.mkdir(exist_ok=True)
    names = {s["name"] for s in skills}
    for old in target.iterdir():
        if old.is_dir() and old.name not in names:
            shutil.rmtree(old)
    for s in skills:
        dest = target / s["name"]
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(s["dir"], dest, ignore=shutil.ignore_patterns("skill.json", ".DS_Store"))
        (dest / "README.md").write_text(skill_readme(s, tools, labels.get(s["group"], s["group"])), encoding="utf-8")

    (target / "README.md").write_text(skills_index(skills, groups, labels), encoding="utf-8")
    shutil.copyfile(source / "resources/skills/CHANGELOG.md", target / "CHANGELOG.md")
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "docs/tools.md").write_text(tools_doc(tools, sections), encoding="utf-8")
    (ROOT / "docs/prompts.md").write_text(prompts_doc(skills, groups, labels), encoding="utf-8")

    reads = sum(1 for t in tools.values() if t.get("read_only"))
    destructive = sum(1 for t in tools.values() if t.get("destructive"))
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    readme = replace_region(readme, "skills", "\n".join(catalog_tables(skills, groups, labels, "skills/")))
    readme = replace_region(readme, "glance", "\n".join([
        "| | |",
        "|---|---|",
        f"| **Server** | `{SERVER}`, Streamable HTTP, nothing to deploy on your side |",
        "| **Sign-in** | **Allow access** (OAuth): one workspace you choose, the assistant renews access by itself. "
        "Or an **API key** from **Settings → API / MCP**: every workspace where you are the owner or a member |",
        f"| **Tools** | {len(tools)}+: {reads} only read, {destructive} delete or overwrite data and are marked. [Full list](docs/tools.md) |",
        "| **Permissions** | Yours: the assistant can do what your role and your plan allow, nothing more |",
        "| **Plans** | Every plan, Free included |",
        "| **Limits** | 180 requests per minute per user; links to exported files work for one hour |",
    ]) + "\n")
    readme = replace_region(readme, "badges", (
        f'  <a href="skills/"><img alt="Skills: {len(skills)}" src="https://img.shields.io/badge/skills-{len(skills)}-8b5cf6?style=flat-square"></a>\n'
        f'  <a href="docs/tools.md"><img alt="Tools: {len(tools)}+" src="https://img.shields.io/badge/tools-{len(tools)}%2B-8b5cf6?style=flat-square"></a>\n'
    ))
    (ROOT / "README.md").write_text(readme, encoding="utf-8")

    print(f"synced {len(skills)} skills and {len(tools)} tools from {source}")
    if left_out:
        print(f"not in scripts/tool-sections.json, left out of the docs: {', '.join(left_out)}")


if __name__ == "__main__":
    main()
