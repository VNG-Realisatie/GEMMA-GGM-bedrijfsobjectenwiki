# GEMMA Bedrijfsobjecten Wiki

Werkinstrument van het GEMMA-team voor het onderbouwd opbouwen, onderhouden en doorontwikkelen van GEMMA bedrijfsobjecten. De wiki wordt onderwerp voor onderwerp opgebouwd vanuit gemeentelijke beleidsdocumenten en het GGM, en vormt het besliskader voor welke entiteiten bedrijfsobjecten worden.

## 1. Doel & werkwijze

Het bestaande GEMMA bedrijfsobjectenmodel is een ongefiltreerde kopie van het GGM. Deze wiki bouwt het opnieuw op met onderbouwing:

1. **Bronnen lezen en samenvatten** — VNG-beleidsdocumenten, proposities, verordeningen → bronsamenvattingen
2. **Onderwerpoverzicht opbouwen** — begrippen identificeren, typeren en beoordelen als BO-kandidaat
3. **BO's afleiden** — per BO-kandidaat: criteria toetsen, BO-pagina aanmaken met onderbouwing
4. **Hiaten signaleren** — GGM-entiteiten zonder BO, BO's zonder GGM-grondslag, correcties terugkoppelen

Het resultaat per onderwerp: BO-beslisdocumenten met metadata die als properties naar het GEMMA ArchiMate-model gaan.

De herleidbaarheidsketen is: `Sources/ → Bronsamenvattingen/ → Bedrijfsobjecten/`. Het onderwerpoverzicht organiseert de begrippen en hun BO-beoordeling.

**BO-afleiding staat op zichzelf.** Een begrip wordt BO op basis van de BO-criteria (zie §5) — dat kan zonder GGM. GGM-matching (zie §6) is aanvullende verrijking en verificatie, geen voorwaarde voor BO-status.

### Werkwijze

De wiki wordt **onderwerp voor onderwerp** opgebouwd. Per onderwerp wordt het volledige proces doorlopen (bronnen → samenvattingen → onderwerpoverzicht → BO's) voordat het volgende onderwerp wordt opgepakt.

GGM-dekkingsanalyse gebeurt centraal via `/entiteitendekking` en werkt vanuit GGM-beleidsdomeinen (niet per wiki-onderwerp), omdat wiki-onderwerpen en GGM-beleidsdomeinen niet 1-op-1 overlappen. Het doel: inzicht welke beleidsdomeinen bronnen hebben vs. waar nog documenten gezocht moeten worden.

### Workflows

**Ingest** — wanneer de gebruiker een bron of onderwerp aanwijst om te verwerken:

1. Lees de volledige bron
2. Bespreek de kernpunten met de gebruiker voordat je schrijft
3. Maak een bronsamenvatting aan (zie `templates/bronsamenvatting.md`)
4. Maak of update het onderwerpoverzicht met nieuwe begrippen (zie `templates/onderwerpoverzicht.md`)
5. Maak BO-pagina's aan voor begrippen die de BO-criteria doorstaan (zie `templates/element.md`)
6. Update `Wiki/index.md` met nieuwe pagina's en one-line beschrijvingen
7. Voeg een entry toe aan `Wiki/log.md` met datum, bron en wat is gewijzigd

Een enkele bron kan 10-15 wiki-pagina's raken. Dat is normaal.

**Lint** — bij een lint- of auditverzoek:

1. **Contradities opsporen** — twee pagina's die elkaar tegenspreken; mark beide pagina's met `⚠️ Tegenspraak met [[andere-pagina]]`
2. **Wees-pagina's vinden** — pagina's zonder inbound links van andere pagina's; controleren of ze werkelijk orphan zijn of moeten gelinkt worden
3. **Concepten zonder pagina** — concepten/BO's die meerdere keren genoemd worden maar geen eigen pagina hebben; voeg toe aan openstaande taken
4. **Verouderde claims** — claims die op basis van nieuwere bronnen mogelijk outdated zijn; flag met `🔍 Verificatie nodig` en citeer nieuwere bron
5. **Template-naleving** — controleren of alle pagina's de juiste frontmatter, secties en formattering hebben (zie templates/)
6. **Herleidbaarheid** — BO-pagina's moeten een `## Bronnen`-sectie in de body hebben; claims moeten citaten hebben

Rapportage: bevindingen als **genummerde lijst met voorgestelde fixes** per categorie (contradities, orphans, verouderd, etc.).

### Onderhoudscyclus

Na de initiële opbouw wordt het model onderhouden bij:
- Nieuwe GGM-releases (entiteiten hertoetsen)
- Nieuwe gemeentelijke onderwerpen (bronnen toevoegen, onderwerpoverzicht uitbreiden, BO's afleiden)

### LLM-rol & autonomie

De LLM fungeert als **eerste filter**. Autonomieregels staan in `/assess-element` stap 11.

## 2. Ad-hoc vragen

Dit is geen skill-getriggerde workflow (geen `/command`) maar het gedrag dat geldt bij elke vraag die de gebruiker stelt, buiten de reguliere ingest/lint-flows om.

1. **Lees eerst `Wiki/index.md`** om relevante pagina's te localiseren
2. **Lees die pagina's en synthetiseer** een antwoord gebaseerd op wat er al in de wiki staat
3. **Citeer specifieke wiki-pagina's** in je antwoord — verwijs naar [[pagina-naam]] waar relevant
4. **Als het antwoord niet in de wiki staat**, zeg dat duidelijk en bied aan het toe te voegen
5. **Als het antwoord waardevol is**, bied aan het op te slaan als vraag-antwoord-pagina in `Wiki/Vragen/` (zie `templates/vraag-antwoord.md`, bijv. [[Wiki/Vragen/nieuwe-vraag]])

**Principe:** Goede antwoorden worden teruggeschreven naar de wiki zodat kennis zich opbouwt. Na elke substantiële vraag controleren: zou dit als vraag-antwoord, begrip of BO-pagina moeten bestaan?

Format bij antwoord:
- Citeer relevant: `Zie [[Wiki/Onderwerpoverzichten/bestuur]] voor...`
- Verwijs naar relaties: `Dit BO relateert aan [[Verkiezing]]`
- Verwijs naar analyses: `Context via [[Wiki/Analyses/entiteitendekking/totaaloverzicht]]` of andere relevante analyses

## 3. Bronnen (Sources)

- **Immutabel** — de LLM leest bronnen maar wijzigt ze nooit.
- Bronnen zijn gemeentelijke beleidsdocumenten, VNG-publicaties, proposities, toelichtingen, verordeningen.
- Georganiseerd per gemeentelijk onderwerp als subdirectory onder `Sources/`.
- Bronnen kunnen YAML-frontmatter bevatten (title, source, created, description, tags).
- **GGM-pagina's zijn gegenereerde brondata, geen handmatige wiki-content.** De bestanden in `Wiki/GGM/` zijn een leesbare conversie van het XMI-bestand (de bron van waarheid), gegenereerd door `/generate-ggm`. Ze bevatten letterlijke definities uit het model, zonder synthese of interpretatie, en worden nooit handmatig bewerkt.
- **Sources/GEMMA/** en **Sources/Standaarden/** bevatten aanvullende referentiebronnen: GEMMA-VNG-afspraken resp. basisregistratie-catalogi (BAG, BRK, BRO, NHR, RGBZ, RSGB, ZTC, BRP).

### Bronnen toevoegen

Er zijn twee manieren om bronnen toe te voegen. Beide resulteren in een bestand in `Sources/{onderwerp}/`.

#### Via URL (LLM fetcht)

1. **Ophalen** — fetch de pagina en converteer naar markdown. Behoud de originele tekst; ruim alleen opmaakruis op (navigatie, footers, ads). Herschrijf geen inhoud.
2. **Onderwerp bepalen** — kies de juiste subdirectory onder `Sources/`. Controleer bestaande subdirectories eerst; maak alleen een nieuwe aan voor een echt nieuw onderwerp.
3. **Opslaan** als `Sources/{onderwerp}/{beschrijvende-slug}.md` (lowercase, kebab-case, max 60 tekens).
4. **Frontmatter** toevoegen:
   ```yaml
   ---
   title: "{titel van de pagina}"
   source: "{originele URL}"
   author: "{auteur of organisatie, leeg als onbekend}"
   published: {publicatiedatum, leeg als onbekend}
   created: {datum van ophalen}
   description: "{korte beschrijving, max 1 zin}"
   tags:
     - "{onderwerp}"
   ---
   ```
5. Als een bestand met dezelfde naam al bestaat, voeg een numeriek suffix toe (bijv. `-2.md`).
6. Na opslaan: meld de gebruiker welk bestand is aangemaakt en stel voor om een ingest te starten.

#### Via Obsidian Web Clipper (gebruiker clipt)

Web Clipper slaat pagina's op in `Clippings/` — een landingszone, geen bron.

1. **Lees** het bestand in `Clippings/`.
2. **Verplaats** naar `Sources/{onderwerp}/{beschrijvende-slug}.md` — zelfde regels als bij URL-ophalen.
3. **Frontmatter aanvullen** als velden ontbreken (description, tags).
4. Ga verder met de reguliere ingest-workflow.

### GGM-terminologie

Het GGM is hiërarchisch opgebouwd: **taakvelden** (afgeleid van IV3) bevatten **beleidsdomeinen**.

- Taakveld = het bovenste niveau (bijv. "5 Sport, Cultuur en Recreatie", "9 Interne Organisatie")
- Beleidsdomein = het niveau daaronder (bijv. "Financien" onder taakveld 9, "Schulden" onder taakveld 6)
- Zie `Wiki/GGM/structuur-ggm.md` voor het volledige overzicht met definities

## 4. Wiki-pagina's

Elke wiki-pagina heeft YAML-frontmatter. Templates per paginatype staan in `templates/`:

| Paginatype | Template | Locatie |
|---|---|---|
| Element (bedrijfsobject) | `templates/element.md` | `Wiki/Bedrijfsobjecten/{taakveld}/{beleidsdomein}/` |
| Element (actor) | `templates/element.md` | `Wiki/Actoren/` (plat) |
| Element (rol) | `templates/element.md` | `Wiki/Rollen/` (plat) |
| Onderwerpoverzicht | `templates/onderwerpoverzicht.md` | `Wiki/Onderwerpoverzichten/` |
| Bronsamenvatting | `templates/bronsamenvatting.md` | `Wiki/Bronsamenvattingen/{onderwerp}/` |
| GGM-terugmelding | `templates/ggm-terugmelding.md` | `Wiki/Analyses/ggm-terugmeldingen.md` (één doorlopend bestand) |
| Vraag-antwoord | `templates/vraag-antwoord.md` | `Wiki/Vragen/` |
| Wiki Index | `templates/index.md` | `Wiki/index.md` |
| Wiki Log | `templates/log.md` | `Wiki/log.md` |

### Conventies

- **Taal**: Nederlands, tenzij gevestigde Engelse term (ArchiMate, business object).
- **Bestandsnamen**: lowercase, koppeltekens. Voorbeeld: `onroerende-zaak.md`.
- **Cross-references**: Obsidian `[[wiki-links]]` voor alle verwijzingen tussen wiki-pagina's.
- **Wiki-links met alias**: alle `[[Wiki/...]]` links moeten een alias hebben zodat de lezer een leesbare naam ziet, niet een pad. In tabellen: `[[pad\|alias]]` (escaped pipe). Buiten tabellen: `[[pad|alias]]` (gewone pipe). Alias is de leesbare naam (bijv. `[[Wiki/Bedrijfsobjecten/.../boom\|Boom]]` in tabel, `[[Wiki/Bronsamenvattingen/.../nota|Nota Dierenwelzijn]]` in proza). Korte links zonder pad (bijv. `[[Stembureau]]`) hoeven geen alias.
- **Citaten uit bronnen**: blockquotes (`>`) met bronvermelding.

## 5. BO-criteria & beoordeling

BO-afleiding staat los van GGM (zie §1) — een begrip wordt beoordeeld op zijn eigen merites.

Alle beoordelingslogica staat in de skills, niet in dit bestand:
- **Elementbeoordeling:** `/assess-element` — domeinbepaling, begripstype, criteria (incl. actor/rol-criteria, zie `Wiki/GEMMA/actoren-en-rollen.md`), subtypes, data-object classificatie, autonomieregels

## 6. GGM-matching & hiaten

GGM-matching gebeurt **nadat** een begrip al op eigen kracht als BO is beoordeeld (zie §5) — het verrijkt en verifieert, het bepaalt niet.

- **Element vastleggen:** `/write-element` — grondslag, GGM-match, matchsterkte, duplicaten- en homoniemdetectie, hiërarchie, relaties, frontmatter, pagina, terugmelding
- **Grondslag zonder GGM:** `/write-element` stap 10 — het mechanisme achter het principe uit §1: een BO zonder GGM-grondslag krijgt lege `ggm_*`-velden en in plaats daarvan een Procesbron- of Juridische bron-sectie
- **Hiaat:** twee richtingen — GGM-entiteiten zonder BO, en BO's zonder GGM-grondslag; zie `/assess-element` voor hiaat-bepaling
- **Onzekere matches:** markeer als `ter discussie`, niet gokken
- **Entiteitendekking:** `/entiteitendekking` — analyseert dit systematisch per taakveld/beleidsdomein (zie §8)

## 7. Regels

### Procesregels — hoe te werken

1. **Wijzig nooit bestanden in `Sources/`** — deze zijn immutabel. (Bronnen zijn read-only.)
2. **Alle wiki-output gaat naar `Wiki/`** — houd de scheiding strikt tussen bronnen en wiki.
3. **Bespreek eerst, schrijf dan** — bij ingest altijd eerst de kernpunten bespreken met de gebruiker.
4. **Incrementeel** — update bestaande pagina's, geen duplicaten; consolideer vergelijkbare concepten.
5. **Update index en log** — na elke ingest of significante wijziging; zorg dat Wiki/index.md en Wiki/log.md actueel zijn.
6. **Bij onzekerheid** — vraag aan de gebruiker hoe iets moet worden gecategoriseerd of behandeld; gok niet.
7. **Geen retroactieve aannames** — als een pagina al bestaat, update deze in plaats van te gokken wat erin zou moeten staan; vraag eerst.

### Inhoudsregels — herleidbaarheid & kwaliteit

Elke factische claim moet traceerbaar zijn naar zijn bron:

1. **Refereer altijd naar bronbestanden** — geen ononderbouwde claims
2. **Format:** Verwijs naar `[[Wiki/Bronsamenvattingen/{onderwerp}/{slug}]]` voor VNG-bronnen, of citeer direct: `> [citaat] (bron: bestandsnaam)`
3. **Bij tegenspraak:** Als twee bronnen het oneens zijn, documenteer beide en mark als `⚠️ Tegenspraak` in de BO-pagina
4. **Zonder bron:** Mark als `🔍 Verificatie nodig` en voeg toe aan openstaande vragen
5. **BO-grondslag:** Elke BO moet via de `## Bronnen`-sectie in de body traceerbaar zijn naar bronsamenvattingen
6. **GGM-matching:** Bij onzekere matches: mark als `ter discussie`, niet gokken
7. **Geen fantasie:** onzekere GGM-mapping markeren als `ter discussie`, niet gokken; elke aanname documenteren

Dit zorgt voor **herleidbaarheid**: elke bewering kan teruggevoerd worden naar originele bronnen.

### Scope- & vormregels

1. **Bestandsnamen** — lowercase met koppeltekens (bijv. `machine-learning.md`, `verkiezing.md`); geen spaties of CAPITALS.
2. **Duidelijke taal** — schrijf begrijpelijk Nederlands; geen technische jargon tenzij nodig; elk concept moet voor domeinexperts herkenbaar zijn.

## 8. Skills & tools

### Directorystructuur

```
Bedrijfsarchitectuur/
├── CLAUDE.md              # dit bestand — schema en conventies
├── .claude/commands/      # skills (`/command`), projectlokaal — zie §"Skills"
├── templates/             # paginatemplates en referentietabellen
├── Sources/               # ruwe bronnen, NIET aanpassen
│   ├── Onderwerpen/       # beleidsdocumenten per onderwerp
│   │   └── {onderwerp}/
│   ├── GEMMA/             # GEMMA-VNG-afspraken (o.a. GEMMA/GGM-relatie)
│   ├── Standaarden/       # basisregistratie-catalogi (BAG, BRK, BRO, NHR, RGBZ, RSGB, ZTC, BRP)
│   └── GGM-repository/    # GGM-bronbestanden en geparsede data
│       ├── Gemeentelijk Gegevensmodel XMI2.1.xml  # XMI-bron (alleen bij nieuwe release)
│       └── ggm_parsed.json   # geparsed XMI — gebruik dit voor GUIDs, GEMMA-tags, relaties
├── Wiki/
│   ├── index.md           # inhoudelijk overzicht van alle wiki-pagina's
│   ├── log.md             # chronologisch logboek van alle acties
│   ├── Onderwerpoverzichten/ # onderwerpoverzichten met begrippentabellen
│   ├── Bedrijfsobjecten/  # BO-pagina's, georganiseerd per {taakveld}/{beleidsdomein}/
│   ├── Actoren/           # Business Actor-pagina's (plat)
│   ├── Rollen/            # Business Role-pagina's (plat)
│   ├── Bronsamenvattingen/# samenvattingen per bron, georganiseerd per {onderwerp}/
│   ├── Analyses/          # per-taakveld dekkingsrapporten, hiaten, terugmeldingen
│   ├── Vragen/            # ad-hoc vraag-antwoord-pagina's (zie §2)
│   ├── GEMMA/             # duiding GEMMA-GGM-samenhang, actoren/rollen-criteria
│   └── GGM/               # gegenereerde leesbare GGM-representatie (zie §3), niet handmatig bewerken
│       ├── structuur-ggm.md
│       └── {taakveld}/    # per taakveld, met index.md en bestanden per beleidsdomein
├── Clippings/             # landingszone voor webclippings (Web Clipper uitvoer)
├── ToDo/                  # taken en agenda
├── exports/               # gegenereerde CSV's (nieuwste versie alleen)
├── tools/                 # Python-scripts voor XMI-verwerking
└── .trash/                # verwijderde items (archief)
```

Onderwerpen en taakvelden worden **niet** vooraf benoemd in de structuur — ze ontstaan bij het verwerken van bronnen. Controleer bestaande subdirectories voordat je een nieuwe aanmaakt.

### Skills

Skills zijn project-lokaal: `.claude/commands/` (binnen `Bedrijfsarchitectuur/`), zelfde niveau als `tools/`. Skills die wiki-pagina's wijzigen updaten altijd `Wiki/index.md` en voegen een entry toe aan `Wiki/log.md`.

Waar van toepassing staat de aangeroepen **Tool** (Python-script uit `tools/` — zie §"Tools" voor details) als tweede regel onder de Functie. Waar de skill zelf een pagina schrijft staat het gebruikte **template** uit `templates/` direct achter dat bestand, tussen haakjes. Elk output-bestand/-locatie staat op een eigen regel. "chat" bij Uit = geen bestand, alleen een antwoord/rapportage.

| Skill | Functie | In | Uit |
|---|---|---|---|
| **ingest**<br>`/ingest {bron\|onderwerp}` | Orchestrator: bron(nen) verwerken via assess-element en write-element | bron/onderwerp | `Wiki/Bronsamenvattingen/` (template: `bronsamenvatting.md`)<br>`Wiki/Onderwerpoverzichten/` (template: `onderwerpoverzicht.md`)<br>`Wiki/index.md` (template: `index.md`)<br>`Wiki/log.md` (template: `log.md`)<br>Delegeert BO-beoordeling en -aanmaak naar assess-element/write-element |
| **assess-element**<br>`/assess-element {begrip}` | Begrip volledig beoordelen: classificatie, criteria, data-object, hiaat | begrip (uit onderwerpoverzicht/GGM) | beoordeling — geen bestand, invoer voor write-element |
| **write-element**<br>`/write-element {element}` | Element vastleggen: GGM-match, frontmatter, pagina aanmaken<br>Tool: `parse_ggm_xmi.py` (optioneel, bij nieuwe GGM-release) | beoordeeld element + `ggm_parsed.json` | `Wiki/Bedrijfsobjecten/` (template: `element.md`)<br>of `Wiki/Actoren/` (template: `element.md`)<br>of `Wiki/Rollen/` (template: `element.md`)<br>Bij afwijking/hiaat: regel toegevoegd aan `Wiki/Analyses/ggm-terugmeldingen.md` (template: `ggm-terugmelding.md`) |
| **entiteitendekking**<br>`/entiteitendekking [taakveld]` | Uniforme GGM-analyse per taakveld/beleidsdomein: BO-matches, classificatie, relaties, hiaten<br>Tool: `entiteitendekking.py`, `entiteitendekking_sync_bo.py` | `Wiki/GGM/` + `Wiki/Bedrijfsobjecten/` | `Wiki/Analyses/entiteitendekking/` (eigen rapportformat, geen template)<br>teruggeschreven `analyse_ggm_dekking` in BO-frontmatter |
| **domain-status**<br>`/domain-status {onderwerp}` | Read-only voortgangsrapportage | `Wiki/` voor onderwerp | chat |
| **lint**<br>`/lint [onderwerp]` | Twee stappen: deterministisch script (exacte telling), dan modelbeoordeling van wat overblijft<br>Tool: `lint_checks.py` (stap 1, altijd), `migrate_frontmatter_style.py` (bij fix) | hele wiki of onderwerp | chat |
| **audit-duplicaten**<br>`/audit-duplicaten` | Systematische scan op naamconflicten (duplicaten/homoniemen) in alle BO's | `Wiki/Bedrijfsobjecten/` | chat, voorstellen (geen automatische fix) |
| **audit-actoren**<br>`/audit-actoren` | Controleer Business Actors op consistentie en volledigheid | `Wiki/Bedrijfsobjecten/` + `Wiki/Bronsamenvattingen/` | werkvoorraadlijst (chat) — vervolg via assess-element/write-element |
| **audit-definities**<br>`/audit-definities` | Controleer BO-definities op afwijkingen van GGM | `Wiki/Bedrijfsobjecten/` + `Wiki/GGM/` | chat, optioneel direct herschreven `bo_definitie`/`bo_toelichting` |
| **fetch**<br>`/fetch {URL}` | URL ophalen als bronbestand in `Sources/` | URL | `Sources/{onderwerp}/*.md` |
| **clip**<br>`/clip {bestand}` | Clipping uit `Clippings/` verplaatsen naar `Sources/`<br>Roept: `/convert_pdf` (indien pdf) | `Clippings/*.md` | `Sources/{onderwerp}/*.md` |
| **convert_pdf**<br>`/convert_pdf {bestand}` | PDF converteren naar markdown voor `Sources/`<br>Tool: `convert_pdf.py` | PDF | markdown naast origineel |
| **crawl**<br>`/crawl {URL}` | Spidering/scraping van website voor bronverzameling | URL(s) | chat (optioneel `Sources/`-bestand op verzoek) |
| **export-ggm**<br>`/export-ggm` | Genereer 5 CSV's (objecten, relaties, diagrammen, beleidsdomeinen, diagram-mapping) uit XMI + wiki<br>Tool: `export_ggm_csv.py` | `ggm_parsed.json` + `Wiki/Bedrijfsobjecten/` | `exports/*.csv` (5 bestanden) |
| **generate-ggm**<br>`/generate-ggm` | Volledige pipeline: XMI → parsed JSON → Wiki/GGM markdown (herhaalbaar, telt alleen Objecttypen)<br>Tool: `parse_ggm_xmi.py`, `generate_ggm_wiki.py`, `generate_ggm_enrich_bo.py` | XMI-bestand | `Sources/GGM-repository/ggm_parsed.json`<br>`Wiki/GGM/**` |

**Model voorkeur:** `/lint` en `/audit-duplicaten` draaien op **Haiku** (read-only analyse, geen reasoning). Andere skills draaien op het standaard project-model.

### Tools

Python-scripts in `tools/`, projectlokaal naast de skills die ze aanroepen.

| Tool | Functie | Skill |
|---|---|---|
| `parse_ggm_xmi.py` | Parse GGM XMI → JSON; schrijft naar `Sources/GGM-repository/ggm_parsed.json`. Alleen draaien bij nieuwe GGM-release. | `/generate-ggm` Stap 1, `/write-element` (optioneel) |
| `generate_ggm_wiki.py` | Genereer Wiki/GGM markdown uit parsed JSON. Telt alleen Objecttypen. `--dry-run` voor preview. | `/generate-ggm` Stap 2 |
| `generate_ggm_enrich_bo.py` | Verrijk BO-frontmatter met `ggm_*`/`ggm_gemma_*`-velden uit geparsed JSON. Herschrijft alleen die velden; alle overige frontmatter (incl. `bo_*`, `ggm_duplicaat_entiteiten`, `analyse_ggm_dekking`) blijft ongewijzigd. | `/generate-ggm` Stap 3 |
| `export_ggm_csv.py` | Genereer 5 CSV-bestanden uit geparsed JSON + wiki BO-pagina's | `/export-ggm` |
| `entiteitendekking.py` | Uniforme GGM-analyse: match, classificeer, traceer relaties, genereer per-taakveld rapporten + totaaloverzicht | `/entiteitendekking` Stap 1 |
| `entiteitendekking_sync_bo.py` | Schrijft `analyse_ggm_dekking` (reverse-index: welke GGM-entiteiten dekt dit BO) terug naar BO-pagina's, chirurgisch — raakt geen andere velden. `--dry-run` voor preview. | `/entiteitendekking` Stap 5 |
| `convert_pdf.py` | Converteert PDF naar markdown | `/convert_pdf` |
| `migrate_frontmatter_style.py` | Fixt frontmatter-stijlfouten (quotes, lege waarden, veldnamen, incl. geneste velden onder `bo_subtypes`/`bo_homoniemen`) | `/lint` (fix-suggestie) |
| `lint_checks.py` | Deterministische consistentiechecks (frontmatter-compleetheid, enum-validatie, Bronnen-secties, dode Sources-links, wees-BO's, wiki-link-aliassen, subtypes/duplicaten/homoniemen-schema) — geen model nodig, exacte telling. `--fix` past de mechanisch veilige subset direct toe (Bronnen-aliassen, dode links, duplicaten-schema, homoniemen-ggm-backfill) | `/lint` Stap 1 (altijd eerst) |

## 9. Gedragsprincipes

- Don't assume. Don't hide confusion. Surface tradeoffs.
- Minimum code that solves the problem. Nothing speculative.
- Touch only what you must. Clean up only your own mess.
- Define success criteria. Loop until verified.

@.claude/projectcontext.md
