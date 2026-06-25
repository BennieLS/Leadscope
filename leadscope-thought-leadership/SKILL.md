---
name: leadscope-thought-leadership
description: Schrijf een thought-leadership LinkedIn-post in de stem van Marten Dames (Leadscope), op basis van een idee, ervaring of brokje bronmateriaal. Gebruik deze skill altijd wanneer de gebruiker vraagt om een LinkedIn-post, thought-leadership-content, een "TL-post", een opiniestuk, een post voor Marten, of een inhoudelijke LinkedIn-update voor Leadscope te schrijven — ook als ze alleen een ruw onderwerp of een losse gedachte aanleveren en niet letterlijk "schrijf een post" zeggen. Trigger ook bij vragen als "maak hier een post van", "kun je dit als LinkedIn-post schrijven", of "ik heb een idee voor LinkedIn".
---

# Leadscope — Thought-leadership posts (stem: Marten Dames)

Deze skill schrijft één sterke LinkedIn-post in de stem van **Marten Dames**, gefundeerd op de **merkstrategie van Leadscope**. De post draagt een inhoudelijke stelling of inzicht (de ruggengraat), maar klinkt warm, nuchter en menselijk — niet stijf of verkoperig.

## Het idee in één zin

Inhoud uit de merkstrategie + één van de archetypes als vorm + de stem van Marten = een post die opvalt omdat hij iets *vindt*, niet omdat hij hard roept.

## Workflow

Doorloop deze stappen. Lees de referentiebestanden waar aangegeven — sla dat niet over, daar zit de kwaliteit.

### Stap 1 — Vang de input (het "zaadje")

De gebruiker levert minimaal een onderwerp of losse gedachte. Optioneel ook:
- **bronmateriaal**: een klantsituatie, een datapunt/cijfer, een eigen ervaring of fout, een artikel/post om op te reageren, een eigen observatie;
- **gewenste invalshoek/archetype** (zie `references/archetypes.md`);
- **must-haves**: punten die er per se in moeten, of dingen die juist niet.

Als het zaadje te dun is om iets scherps te maken, stel **maximaal 2** verhelderende vragen — bijvoorbeeld: "Wat is de concrete aanleiding?" of "Heb je hier een eigen ervaring of cijfer bij?". Stel geen vragen als je het redelijk zelf kunt invullen; ga dan door en benoem je aanname kort.

### Stap 2 — Verbind met het fundament

Lees `references/brand-foundation.md`. Bepaal:
- Welke **content-pijler** raakt dit? (demand gen vs lead gen · fundament vóór campagnes · GTM als missing link · grip & voorspelbaarheid · RevOps/HubSpot · marketing-sales-alignment · 95% out-of-market)
- Wat is de **stelling**? Een TL-post heeft één duidelijk standpunt. Geen standpunt = geen post.
- Klopt het met de merkwaarheden? Check vooral de **rode lijnen** (nooit valse beloftes, kanaal-agnostisch waar relevant, geen kostenpost-vs-profitcenter-framing).

### Stap 2b — Raadpleeg je eigen prestaties (LinkedIn-database)

In de hoofdmap van dit project staat een lokale database met Martens eigen postresultaten (zie `CLAUDE.md`). Gebruik die om je keuze van **pijler / archetype / hook** te onderbouwen — maar **alleen voor zover er genoeg data is**. Eén virale post mag de richting niet bepalen.

Haal status én patronen op met:

```
./.venv/bin/python -c "import database as db, json; print(json.dumps(db.inzichten_voor_skills(), default=str, ensure_ascii=False, indent=2))"
```

(Bestaat `.venv` niet of werk je buiten dit project, gebruik dan `python3`. Geeft het commando een fout of leegte? Ga gewoon door zonder eigen-data-laag.)

Pas je gedrag aan op het veld `status.fase`:
- **`loggen`** — negeer de data volledig als sturing. Kies pijler/archetype puur op merkstrategie en de input.
- **`zachte_signalen`** — gebruik de patronen alleen als lichte tiebreaker bij twijfel, en benoem ze als voorlopig ("voorlopig signaal, nog weinig data"). Maak er geen regel van.
- **`sturen`** — laat de best presterende pijlers/hooks (`patronen.per_pijler`, `patronen.per_hook`, `patronen.beste_posts`) meewegen. Let op: `engagement_ratio` is een fractie (0.05 = 5%). Alleen segmenten met genoeg posts staan erin.

Harde regel: forceer nooit een onderwerp of vorm die niet bij de input past, alleen omdat een pijler/hook goed scoort. De data **informeert**; de input en de merkstrategie blijven leidend.

### Stap 3 — Kies het archetype

Lees `references/archetypes.md`. Kies het archetype dat bij de input past, of adviseer er één en zeg waarom. Elk archetype heeft een eigen structuur en hookpatroon.

### Stap 4 — Schrijf in de stem van Marten

Lees `references/voice-marten.md`. Schrijf de post volgens het stemprofiel: warm, nuchter, je-vorm, korte zinnen, lichte woordspeling waar het natuurlijk valt, genereus, spaarzaam `:)`/`;)` (geen moderne emoji), uitroeptekens alleen voor echte energie. De inhoud is scherp; de toon is toegankelijk.

### Stap 5 — Lever in het vaste outputformat

Lever **altijd** in dit format:

```
## Post

[De volledige post, klaar om te plaatsen. Korte alinea's, witregels, scanbaar.
Hook in regel 1-2 (vóór de "…meer"-afkap). Eén idee. Zachte afsluiter/CTA.]

## Alternatieve hooks

1. [hook-variant]
2. [hook-variant]
3. [hook-variant]

## Toelichting (kort)

- Archetype: [welke + waarom]
- Pijler: [welke content-pijler]
- Zachte CTA: [welke richting — volgen / reageren / keynote/blog]
```

De **zachte CTA** sluit aan op de "volg ons / lees de keynote"-richting uit de strategie. Nooit een harde salespitch ("plan een strategiegesprek") in een TL-post. Goede zachte CTA's: een open vraag aan de lezer, uitnodigen te volgen, of verwijzen naar de keynote/blog als die er is. Soms is geen expliciete CTA het sterkst — laat de afsluiter dan het werk doen.

### Stap 6 — Kwaliteitscheck

Lees `references/quality-checklist.md` en loop de post er langs vóór je 'm oplevert. Belangrijkste: de hook-test, de stelling-test, de stem-test, en de **anti-AI-stijl-pass**. Voer die laatste uit met de `vermijd-ai-schrijfstijl`-skill (Nederlandse AI-tells), of pas de principes daaruit toe als de skill niet beschikbaar is.

## Wat deze skill niet doet

- Geen valse resultaatbeloftes, geen "wij maken je marktleider".
- Geen generieke "5 tips voor B2B-marketing"-lijstjes zonder standpunt.
- Geen engagement-bait ("Mee eens? 👇", "Typ JA in de comments").
- Geen hashtag-spam (0-3 relevante hashtags, of geen).
- Geen corporate jargon of buzzwords als vulling.
