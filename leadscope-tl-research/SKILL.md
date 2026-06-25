---
name: leadscope-tl-research
description: Haal verse, Europese B2B-onderwerpen op die geschikt zijn als startpunt ("zaadje") voor een thought-leadership-post van Leadscope/Marten Dames, en lever ze als een shortlist gekoppeld aan een content-pijler en een archetype. Gebruik deze skill altijd wanneer de gebruiker vraagt om onderwerp-ideeën, content-inspiratie of "waar zal ik over posten", bijvoorbeeld bij "vind recente onderwerpen", "haal topics op voor LinkedIn", "wat speelt er waar ik iets over kan zeggen", "vul de contentkalender", "geef me wat zaadjes", "research voor een TL-post", of "ik weet niet waarover ik moet schrijven". Trigger ook als de gebruiker losjes vraagt wat er recent gebeurd is in B2B-marketing, demand gen, RevOps of GTM dat de moeite waard is om op te reageren. Dit is de voorkant van de TL-pijplijn en schrijft GEEN posts, maar levert de onderwerpen waaruit de leadscope-thought-leadership-skill vervolgens put.
---

# Leadscope — TL-research (zaadjes voor thought leadership)

Deze skill levert **8 onderwerp-zaadjes**: verse, Europese B2B-ontwikkelingen die de moeite waard zijn om als Leadscope/Marten op te reageren. Elk zaadje is al voorgekauwd — gekoppeld aan een content-pijler, een archetype en een mogelijke hook — zodat "waar schrijf ik over" een kwestie van scannen en kiezen wordt.

## Het idee in één zin

Verse, Europese B2B-ontwikkelingen → streng gefilterd op recentheid én op of de tactiek naar een NL/EU MKB-bedrijf vertaalt → gekoppeld aan een Leadscope-pijler en een archetype = 8 zaadjes om uit te kiezen.

## Plek in de pijplijn

Dit is de **voorkant** van de thought-leadership-pijplijn, vergelijkbaar met hoe `strategy-1-research` de strategy-pijplijn opent.

```
[deze skill: tl-research]  →  kies 1 zaadje  →  [leadscope-thought-leadership: schrijft de post]
```

Deze skill schrijft dus **nooit zelf een post**. Hij levert brandstof. Na de shortlist nodig je de gebruiker uit om een zaadje te kiezen, dat je daarna in de `leadscope-thought-leadership`-skill voert.

Waarom dit ertoe doet: Leadscope heeft (nog) geen low-ticket offer of lead magnet. De thought-leadership-stroom op LinkedIn is op dit moment de feitelijke **transitionele CTA** — de lage-drempelmanier waarop prospects bij Leadscope binnenkomen ("volg ons"). Verse, rake zaadjes voeden dus niet zomaar wat content; ze voeden het enige lage-drempelkanaal dat er nu is.

## Vaste instellingen (afgesproken met Leadscope)

- **Tijdvenster: 180 dagen**, altijd teruggerekend vanaf de dag van uitvoeren. Bereken de drempeldatum live — gebruik nooit een hardcoded datum.
- **Geografie: Nederland + Europa.** Amerikaanse bronnen tellen alleen mee voor *cijfers/onderzoek*, en dan nog alleen als de onderliggende les naar de Europese markt vertaalt. Reden: VS-bedrijven zijn vaak zó groot dat hun tactieken bij een NL/EU MKB-bedrijf (zakelijke dienstverlening of maakindustrie, MKB-voorkeur) niet werken. Dit is het belangrijkste kwaliteitsfilter — zie `references/vertaalcheck.md`.
- **Aantal: 8 zaadjes per run**, gespreid over meerdere pijlers (niet 8 keer dezelfde invalshoek).

Als de gebruiker bij het aanroepen een afwijkende wens noemt (korter venster, één specifieke pijler, meer/minder zaadjes), volg die — anders gelden bovenstaande standaarden.

## Workflow

Doorloop deze stappen op volgorde. Lees de reference-bestanden waar aangegeven; daar zit de kwaliteit — sla dat niet over.

### Stap 1 — Bepaal venster en focus

- Bereken de drempeldatum: vandaag minus 180 dagen. Noteer 'm; alles ouder valt straks af.
- Vraag jezelf af of de gebruiker een focus gaf (bv. "alleen RevOps", "iets over AI in sales"). Zo ja: zoek gerichter. Zo nee: dek de pijlers breed af zodat de shortlist gevarieerd wordt.

### Stap 1b — Weeg mee wat bij Marten al werkt (LinkedIn-database)

In de hoofdmap van dit project staat een lokale database met Martens eigen postresultaten (zie `CLAUDE.md`). Gebruik die om de **spreiding van je 8 zaadjes** bij te sturen — maar **alleen voor zover er genoeg data is**.

Haal status én patronen op met:

```
./.venv/bin/python -c "import database as db, json; print(json.dumps(db.inzichten_voor_skills(), default=str, ensure_ascii=False, indent=2))"
```

(Bestaat `.venv` niet of werk je buiten dit project, gebruik dan `python3`. Geeft het commando een fout of leegte? Ga gewoon door zonder eigen-data-laag.)

Pas je gedrag aan op `status.fase`:
- **`loggen`** — negeer de data; zorg simpelweg voor brede spreiding over de pijlers.
- **`zachte_signalen`** — laat best presterende pijlers iets zwaarder meewegen in de spreiding, maar blijf breed; benoem het als voorlopig.
- **`sturen`** — geef pijlers/hooks die aantoonbaar goed presteren (`patronen.per_pijler`, `patronen.per_hook`) wat meer gewicht in de shortlist, zónder de variatie te verliezen.

Harde regel: de recentheids- en NL/EU-vertaalcheck wegen altijd zwaarder dan de eigen-data-voorkeur. Een goed scorende pijler is nooit een excuus voor een oud of niet-vertaalbaar zaadje.

### Stap 2 — Zoek per pijler

Lees `references/bronnen.md`. Dat bevat de Europees-gewogen bronlijst en concrete zoek-patronen (Nederlands én Engels, met het juiste jaartal).

- Zoek **per content-pijler** apart — één brede zoekopdracht levert oppervlakkige resultaten voor alles. Combineer ze niet.
- Gebruik het huidige jaartal in queries, niet een oud jaar.
- Verzamel ruim: mik op 20–30 kandidaten zodat je na het filteren nog 8 sterke overhoudt.

### Stap 3 — Verifieer recentheid — niet overslaan

Lees `references/recency-regels.md`. Dit is het stuk waar een naïeve aanpak stukloopt: **zoekrelevantie is niet hetzelfde als recentheid.** SEO-sterke evergreen-artikelen ranken bovenaan, ongeacht leeftijd. Verifieer daarom de publicatiedatum aan de bron (pagina-metadata via web_fetch), niet uit het zoeksnippet. Gooi alles weg dat ouder is dan de drempeldatum of geen verifieerbare datum heeft.

### Stap 4 — Screen op NL/EU-relevantie

Lees `references/vertaalcheck.md`. Loop elke overgebleven kandidaat langs de vertaalcheck: schaalt dit naar een ambitieus NL/EU MKB-bedrijf, of is het een enterprise/VS-speeltje (negenkoppige teams, budgetten die hier niet bestaan, tools/kanalen die hier niet relevant zijn)? Bij twijfel: eruit. Liever 8 scherpe dan 12 halve.

### Stap 5 — Koppel aan pijler + archetype

Lees `references/zaadje-format.md` voor de mapping. Koppel elk zaadje aan de content-pijler die het raakt en aan het archetype dat er het beste bij past. Let op: research voedt vooral de archetypes **contraire stelling, mythe ontkrachten, scherp inzicht uit data en voorspelling/trendduiding**. De archetypes *eigen fout, geanonimiseerd klantverhaal en event/keynote* komen uit Martens eigen leven, niet uit research — bied die alleen aan als een zaadje er natuurlijk een herinnering aan oproept ("dit deed me denken aan…"), niet als hoofdvorm.

### Stap 6 — Lever 8 zaadjes in het vaste format

Lees `references/zaadje-format.md` en lever exact in dat format. Sorteer op sterkte (sterkste zaadje bovenaan) en zorg voor spreiding over pijlers.

### Stap 7 — Bied de overdracht aan

Sluit af met een korte, niet-pusherige uitnodiging om één zaadje te kiezen, met de toezegging dat je het dan via de `leadscope-thought-leadership`-skill tot een post uitwerkt. Dwing niets af; de gebruiker mag ook gewoon de lijst meenemen.

## Wat deze skill niet doet

- **Geen posts schrijven.** Dat is de TL-skill. Lever zaadjes, geen kant-en-klare content.
- **Geen VS-enterprise-tactieken** presenteren als inspiratie. De vertaalcheck is hard.
- **Geen oude of ongedateerde content.** Buiten 180 dagen of geen verifieerbare datum = niet meenemen.
- **Geen pure tool-promo** ("tool X heeft feature Y gelanceerd") tenzij er een inhoudelijke stelling of inzicht aan vastzit dat bij een pijler past.
- **Geen ranking-gokwerk.** Een hoge zoekpositie is geen bewijs van recentheid of relevantie; altijd verifiëren.
