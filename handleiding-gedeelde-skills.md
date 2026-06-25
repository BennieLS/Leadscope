# Gedeelde Claude Code skills — handleiding

Dit is onze gezamenlijke verzameling Claude Code skills. De **GitHub-repo is de bron**: je kloont 'm één keer naar je eigen computer, en houdt 'm actueel met `git pull`. Voeg je zelf een skill toe, dan push je die terug zodat het hele team 'm krijgt.

---

## Vooraf (eenmalig regelen)

- Een (gratis) **GitHub-account**, en je hebt de uitnodiging voor de repo geaccepteerd (check je mail of github.com/notifications).
- **VS Code** met **Claude Code** werkend.
- **Git** geïnstalleerd. Check in de Terminal met `git --version`. Geen versie? Op Mac installeer je 't met `xcode-select --install`.

---

## Stap 1 — Repo klonen (eenmalig)

We klonen de repo naar `~/.claude/skills`. Dat is de map waar Claude Code automatisch naar skills kijkt, dus daarna zijn de skills in **al je projecten** beschikbaar.

1. Open de **Terminal**.

2. Kijk of je daar al skills hebt staan:
   ```bash
   ls ~/.claude/skills
   ```
   - "No such file or directory" → mooi, ga door naar stap 3.
   - Staat er al iets → zet het eerst veilig (anders weigert git te klonen):
     ```bash
     mv ~/.claude/skills ~/.claude/skills-backup
     ```

3. Kloon de repo naar die plek:
   ```bash
   git clone https://github.com/BennieLS/Leadscope.git ~/.claude/skills
   ```
   De eerste keer vraagt GitHub om in te loggen (er opent meestal een browservenster). Daarna onthoudt hij dat.

4. Controleer:
   ```bash
   ls ~/.claude/skills
   ```
   Je ziet nu de skill-mappen. Open Claude Code en typ `/skills` om te bevestigen dat ze actief zijn.

> **Windows:** doe dit in **Git Bash**, dan werkt `~/.claude/skills` net zo.

---

## Stap 2 — Updaten (de nieuwste skills ophalen)

Doe dit aan het begin van je dag, of als iemand laat weten dat er iets nieuws is gepusht:

```bash
cd ~/.claude/skills
git pull
```

Of gebruik de **Sync**-knop linksonder in VS Code.

> Wijzigingen aan bestaande skills pakt Claude Code meteen op. Een **gloednieuwe** skill-map wordt soms pas zichtbaar na een herstart van Claude Code.

---

## Stap 3 — Een nieuwe skill toevoegen en pushen

1. Ga in de repo-map staan en haal eerst de laatste versie op:
   ```bash
   cd ~/.claude/skills
   git pull
   ```

2. Maak een nieuwe map met daarin een `SKILL.md` (kleine letters, koppeltekens, geen spaties):
   ```bash
   mkdir mijn-nieuwe-skill
   touch mijn-nieuwe-skill/SKILL.md
   ```
   Vul `SKILL.md` met de YAML-frontmatter (`name` en `description`) en de instructies.
   > Heb je de skill ergens anders gemaakt (bijv. in een klantproject)? Kopieer dan de hele skill-map naar `~/.claude/skills`.

3. Werk de README-tabel bij met het script:
   ```bash
   python3 update-readme.py
   ```

4. Commit en push:
   ```bash
   git add .
   git commit -m "nieuwe skill: mijn-nieuwe-skill"
   git push
   ```

5. Geef het team een seintje dat ze even `git pull` moeten doen.

---

## Als `git push` wordt afgewezen

Bij samenwerken kan het gebeuren dat iemand anders net iets heeft gepusht. Git weigert dan je push. Oplossing: eerst ophalen, dan opnieuw pushen.
```bash
git pull
git push
```

---

## Spiekbriefje

| Wat | Command |
|---|---|
| Laatste skills ophalen | `cd ~/.claude/skills && git pull` |
| Bekijken wat je hebt gewijzigd | `git status` |
| README-tabel bijwerken | `python3 update-readme.py` |
| Wijzigingen pushen | `git add . && git commit -m "..." && git push` |
| Actieve skills bekijken in Claude Code | `/skills` |
