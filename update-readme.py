#!/usr/bin/env python3
"""Werkt de skill-overzichtstabel in README.md bij op basis van de SKILL.md-bestanden.

Gebruik: zet dit bestand in de root van je repo en draai `python3 update-readme.py`.
Zorg dat je README.md ergens deze twee regels bevat (de tabel komt ertussen):

    <!-- SKILLS:START -->
    <!-- SKILLS:END -->
"""
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
README = os.path.join(ROOT, "README.md")
START = "<!-- SKILLS:START -->"
END = "<!-- SKILLS:END -->"


def parse_frontmatter(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return None
    data, key = {}, None
    for line in m.group(1).splitlines():
        km = re.match(r"^(\w[\w-]*):\s*(.*)$", line)
        if km:
            key = km.group(1)
            data[key] = km.group(2).strip()
        elif key:  # vervolgregel van een lange description
            data[key] += " " + line.strip()
    return data


def short(desc):
    """Maak een nette eenregelige samenvatting voor de tabel."""
    desc = desc.strip().strip('"\'')
    m = re.search(r"^(.*?\.)(\s|$)", desc)   # eerste zin
    s = m.group(1) if m else desc
    if len(s) > 140:
        s = s[:137].rstrip() + "..."
    return s.replace("|", r"\|")             # pipes escapen voor de tabel


def main():
    rows = []
    for name in sorted(os.listdir(ROOT)):
        skill_md = os.path.join(ROOT, name, "SKILL.md")
        if os.path.isfile(skill_md):
            fm = parse_frontmatter(skill_md)
            if not fm:
                continue
            rows.append((fm.get("name", name), short(fm.get("description", ""))))

    table = ["| Skill | Wat doet het |", "|---|---|"]
    table += [f"| {n} | {d} |" for n, d in rows]
    block = f"{START}\n" + "\n".join(table) + f"\n{END}"

    with open(README, encoding="utf-8") as f:
        content = f.read()

    if START in content and END in content:
        before = content[: content.index(START)]
        after = content[content.index(END) + len(END):]
        content = before + block + after
    else:
        content = content.rstrip() + "\n\n## Beschikbare skills\n\n" + block + "\n"

    with open(README, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"README.md bijgewerkt: {len(rows)} skill(s) gevonden.")


if __name__ == "__main__":
    main()
