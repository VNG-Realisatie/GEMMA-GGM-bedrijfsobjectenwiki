# GEMMA Bedrijfsobjecten Wiki

Werkinstrument van het GEMMA-team voor het onderbouwd opbouwen, onderhouden en doorontwikkelen van GEMMA bedrijfsobjecten. De wiki wordt domein voor domein opgebouwd vanuit gemeentelijke beleidsdocumenten en het GGM, en vormt het besliskader voor welke entiteiten bedrijfsobjecten worden.

## Doel

Het bestaande GEMMA bedrijfsobjectenmodel is een ongefiltreerde kopie van het GGM. Deze wiki bouwt het opnieuw op met onderbouwing:

1. **Bronnen lezen en samenvatten** — VNG-beleidsdocumenten, proposities, verordeningen → bronsamenvattingen
2. **Domeinoverzicht opbouwen** — begrippen identificeren, typeren en beoordelen als BO-kandidaat
3. **BO's afleiden** — per BO-kandidaat: GGM matchen, BO-pagina aanmaken met onderbouwing
4. **Hiaten signaleren** — GGM-entiteiten zonder BO, BO's zonder GGM-grondslag, correcties terugkoppelen

Het resultaat per domein: BO-beslisdocumenten met metadata die als properties naar het GEMMA ArchiMate-model gaan.

De herleidbaarheidsketen is: `Sources/ → Bronsamenvattingen/ → Bedrijfsobjecten/`. Het domeinoverzicht organiseert de begrippen en hun BO-beoordeling.

### Werkwijze

De wiki wordt **domein voor domein** opgebouwd. Per domein wordt het volledige proces doorlopen (bronnen → samenvattingen → domeinoverzicht → BO's) voordat het volgende domein wordt opgepakt.

GGM-dekkingsanalyse gebeurt centraal via `/coverage` en werkt vanuit GGM-beleidsdomeinen (niet per wiki-domein), omdat wiki-domeinen en GGM-beleidsdomeinen niet 1-op-1 overlappen. Het doel: inzicht welke beleidsdomeinen bronnen hebben vs. waar nog documenten gezocht moeten worden.

### Onderhoudscyclus

Na de initiële opbouw wordt het model onderhouden bij:
- Nieuwe GGM-releases (entiteiten hertoetsen)
- Nieuwe gemeentelijke onderwerpen (bronnen toevoegen, domeinoverzicht uitbreiden, BO's afleiden)

### LLM-rol

De LLM fungeert als **eerste filter**. Autonomieregels staan in `/assess-bo` stap 11.

## Directorystructuur

```
Bedrijfsarchitectuur/
├── CLAUDE.md              # dit bestand — schema en conventies
├── templates/             # paginatemplates en referentietabellen
├── Sources/               # ruwe bronnen, NIET aanpassen
│   ├── Onderwerpen/       # beleidsdocumenten per domein
│   │   └── {domein}/
│   ├── GGM/               # leesbare representatie van het Gemeentelijk Gegevensmodel
│   │   ├── structuur-ggm.md
│   │   └── {taakveld}/    # per taakveld, evt. met index.md en bestanden per beleidsdomein
│   ├── GGM-repository/    # GGM-bronbestanden en geparsede data
│   │   ├── Gemeentelijk Gegevensmodel XMI2.1.xml  # XMI-bron (alleen bij nieuwe release)
│   │   └── ggm_parsed.json   # geparsed XMI — gebruik dit voor GUIDs, GEMMA-tags, relaties
│   └── {domein}/          # overige bronnen per domein
├── Wiki/
│   ├── index.md           # inhoudelijk overzicht van alle wiki-pagina's
│   ├── log.md             # chronologisch logboek van alle acties
│   ├── Domeinen/          # domeinoverzichten met begrippentabellen
│   ├── Bedrijfsobjecten/  # BO-pagina's, georganiseerd per {taakveld}/{beleidsdomein}/
│   ├── Bronsamenvattingen/# samenvattingen per bron, georganiseerd per {domein}/
│   └── Analyses/          # query-resultaten, vergelijkingen, syntheses
└── tools/                 # Python-scripts voor XMI-verwerking
```

Domeinen en taakvelden worden **niet** vooraf benoemd in de structuur — ze ontstaan bij het verwerken van bronnen. Controleer bestaande subdirectories voordat je een nieuwe aanmaakt.

## Bronnen (Sources)

- **Immutabel** — de LLM leest bronnen maar wijzigt ze nooit.
- Bronnen zijn gemeentelijke beleidsdocumenten, VNG-publicaties, proposities, toelichtingen, verordeningen.
- Georganiseerd per gemeentelijk domein als subdirectory onder `Sources/`.
- Bronnen kunnen YAML-frontmatter bevatten (title, source, created, description, tags).
- **GGM-pagina's zijn bronnen, geen wiki.** De bestanden in `Sources/GGM/` zijn een leesbare conversie van het XMI-bestand (de bron van waarheid). Ze bevatten letterlijke definities uit het model, zonder synthese of interpretatie.

### Bronnen toevoegen

Er zijn twee manieren om bronnen toe te voegen. Beide resulteren in een bestand in `Sources/{domein}/`.

#### Via URL (LLM fetcht)

1. **Ophalen** — fetch de pagina en converteer naar markdown. Behoud de originele tekst; ruim alleen opmaakruis op (navigatie, footers, ads). Herschrijf geen inhoud.
2. **Domein bepalen** — kies de juiste subdirectory onder `Sources/`. Controleer bestaande subdirectories eerst; maak alleen een nieuwe aan voor een echt nieuw domein.
3. **Opslaan** als `Sources/{domein}/{beschrijvende-slug}.md` (lowercase, kebab-case, max 60 tekens).
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
     - "{domein}"
   ---
   ```
5. Als een bestand met dezelfde naam al bestaat, voeg een numeriek suffix toe (bijv. `-2.md`).
6. Na opslaan: meld de gebruiker welk bestand is aangemaakt en stel voor om een ingest te starten.

#### Via Obsidian Web Clipper (gebruiker clipt)

Web Clipper slaat pagina's op in `Clippings/` — een landingszone, geen bron.

1. **Lees** het bestand in `Clippings/`.
2. **Verplaats** naar `Sources/{domein}/{beschrijvende-slug}.md` — zelfde regels als bij URL-ophalen.
3. **Frontmatter aanvullen** als velden ontbreken (description, tags).
4. Ga verder met de reguliere ingest-workflow.

### GGM-bronbestandformaat

Zie `templates/ggm-bron.md` voor het volledige format inclusief verplichte secties en verantwoording.

#### GGM-terminologie

Het GGM is hiërarchisch opgebouwd: **taakvelden** (afgeleid van IV3) bevatten **beleidsdomeinen**.

- Taakveld = het bovenste niveau (bijv. "5 Sport, Cultuur en Recreatie", "9 Interne Organisatie")
- Beleidsdomein = het niveau daaronder (bijv. "Financien" onder taakveld 9, "Schulden" onder taakveld 6)
- Zie `Sources/GGM/structuur-ggm.md` voor het volledige overzicht met definities

## Wiki-pagina's

Elke wiki-pagina heeft YAML-frontmatter. Templates per paginatype staan in `templates/`:

| Paginatype | Template | Locatie |
|---|---|---|
| Bedrijfsobject | `templates/bedrijfsobject.md` | `Wiki/Bedrijfsobjecten/{taakveld}/{beleidsdomein}/` |
| Domeinoverzicht | `templates/domeinoverzicht.md` | `Wiki/Domeinen/` |
| Bronsamenvatting | `templates/bronsamenvatting.md` | `Wiki/Bronsamenvattingen/{domein}/` |
| Analyse | `templates/analyse.md` | `Wiki/Analyses/` |

Formats voor `index.md` en `log.md`: zie `templates/index-log.md`.

### Beoordelingslogica

Alle beoordelingslogica staat in de skills, niet in dit bestand:
- **BO-beoordeling:** `/assess-bo` — domeinbepaling, begripstype, criteria, subtypes, data-object classificatie, hiaat, autonomieregels
- **BO vastleggen:** `/write-bo` — grondslag, matchsterkte, frontmatter, relaties, pagina, terugmelding
- **GGM-dekking:** `/coverage` — batch GGM→wiki dekkingssweep per beleidsdomein

### Conventies

- **Taal**: Nederlands, tenzij gevestigde Engelse term (ArchiMate, business object).
- **Bestandsnamen**: lowercase, koppeltekens. Voorbeeld: `onroerende-zaak.md`.
- **Cross-references**: Obsidian `[[wiki-links]]` voor alle verwijzingen tussen wiki-pagina's.
- **Wiki-links met alias**: alle `[[Wiki/...]]` links moeten een alias hebben zodat de lezer een leesbare naam ziet, niet een pad. In tabellen: `[[pad\|alias]]` (escaped pipe). Buiten tabellen: `[[pad|alias]]` (gewone pipe). Alias is de leesbare naam (bijv. `[[Wiki/Bedrijfsobjecten/.../boom\|Boom]]` in tabel, `[[Wiki/Bronsamenvattingen/.../nota|Nota Dierenwelzijn]]` in proza). Korte links zonder pad (bijv. `[[Stembureau]]`) hoeven geen alias.
- **Citaten uit bronnen**: blockquotes (`>`) met bronvermelding.

## Ingest workflow

Wanneer de gebruiker een bron of domein aanwijst om te verwerken:

1. Lees de volledige bron
2. Bespreek de kernpunten met de gebruiker voordat je schrijft
3. Maak een bronsamenvatting aan (zie `templates/bronsamenvatting.md`)
4. Maak of update het domeinoverzicht met nieuwe begrippen (zie `templates/domeinoverzicht.md`)
5. Maak BO-pagina's aan voor begrippen die de BO-criteria doorstaan (zie `templates/bedrijfsobject.md`)
6. Update `Wiki/index.md` met nieuwe pagina's en one-line beschrijvingen
7. Voeg een entry toe aan `Wiki/log.md` met datum, bron en wat is gewijzigd

Een enkele bron kan 10-15 wiki-pagina's raken. Dat is normaal.

## Vragen beantwoorden

Wanneer de gebruiker een vraag stelt:

1. **Lees eerst `Wiki/index.md`** om relevante pagina's te localiseren
2. **Lees die pagina's en synthetiseer** een antwoord gebaseerd op wat er al in de wiki staat
3. **Citeer specifieke wiki-pagina's** in je antwoord — verwijs naar [[pagina-naam]] waar relevant
4. **Als het antwoord niet in de wiki staat**, zeg dat duidelijk en bied aan het toe te voegen
5. **Als het antwoord waardevol is**, bied aan het als nieuwe analyse-pagina op te slaan (bijv. [[Wiki/Analyses/nieuwe-analyse]])

**Principe:** Goede antwoorden worden teruggeschreven naar de wiki zodat kennis zich opbouwt. Na elke substantiële vraag controleren: zou dit als analyse, begrip of BO-pagina moeten bestaan?

**Format bij antwoord:**
- Citeer relevant: `Zie [[Wiki/Domeinen/bestuur]] voor...`
- Verwijs naar relaties: `Dit BO relateert aan [[Verkiezing]]`
- Verwijs naar analyses: `Context via [[Wiki/Analyses/ggm-dekkingspatroon]]`

## Lint

Bij een lint- of auditverzoek:

1. **Contradities opsporen** — twee pagina's die elkaar tegenspreken; mark beide pagina's met `⚠️ Tegenspraak met [[andere-pagina]]`
2. **Wees-pagina's vinden** — pagina's zonder inbound links van andere pagina's; controleren of ze werkelijk orphan zijn of moeten gelinkt worden
3. **Concepten zonder pagina** — concepten/BO's die meerdere keren genoemd worden maar geen eigen pagina hebben; voeg toe aan openstaande taken
4. **Verouderde claims** — claims die op basis van nieuwere bronnen mogelijk outdated zijn; flag met `🔍 Verificatie nodig` en citeer nieuwere bron
5. **Template-naleving** — controleren of alle pagina's de juiste frontmatter, secties en formattering hebben (zie templates/)
6. **Herleidbaarheid** — BO-pagina's moeten een `## Bronnen`-sectie in de body hebben; claims moeten citaten hebben

**Rapportage:** Bevindingen als **genummerde lijst met voorgestelde fixes** per categorie (contradities, orphans, verouderd, etc.).

## Skills

Beschikbaar als `/command` (gedefinieerd in `.claude/commands/`). Skills die wiki-pagina's wijzigen updaten altijd `Wiki/index.md` en voegen een entry toe aan `Wiki/log.md`.

| Skill | Aanroep | Functie |
|---|---|---|
| **ingest** | `/ingest {bron\|domein}` | Orchestrator: bron(nen) verwerken via assess-bo en write-bo |
| **assess-bo** | `/assess-bo {begrip}` | Begrip volledig beoordelen: classificatie, criteria, data-object, hiaat |
| **write-bo** | `/write-bo {BO}` | BO vastleggen: GGM-match, frontmatter, pagina aanmaken |
| **coverage** | `/coverage dekking` | GGM-dekkingsanalyse: centrale pagina per beleidsdomein, telt entiteiten/BO's, signaleert welke beleidsdomeinen bronnen hebben |
| **domain-status** | `/domain-status {domein}` | Read-only voortgangsrapportage |
| **lint** | `/lint [domein]` | Consistentiechecks op wiki tegen templates en skills |
| **fetch** | `/fetch {URL}` | URL ophalen als bronbestand in `Sources/` |
| **clip** | `/clip {bestand}` | Clipping uit `Clippings/` verplaatsen naar `Sources/` |
| **export-ggm** | `/export-ggm` | Genereer 5 CSV's (objecten, relaties, diagrammen, beleidsdomeinen, diagram-mapping) uit XMI + wiki |

## Tools

Python-scripts in `tools/` voor XMI-verwerking.

| Tool | Functie |
|---|---|
| `parse_ggm_xmi.py` | Parse GGM XMI → JSON; schrijft naar `Sources/GGM-repository/ggm_parsed.json`. Alleen draaien bij nieuwe GGM-release. |
| `enrich_bo_frontmatter.py` | Verrijk BO-frontmatter met GGM-velden uit geparsed JSON |
| `export_ggm_csv.py` | Genereer 5 CSV-bestanden uit geparsed JSON + wiki BO-pagina's |

### GGM-data gebruiken

- **Voor domeinbegrip** (entiteiten, definities, relaties): lees `Sources/GGM/{taakveld}/`
- **Voor technische metadata** (GUIDs, GEMMA-tags, diagram-IDs): lees `Sources/GGM-repository/ggm_parsed.json`
- **XMI niet direct lezen** — alleen via de parser bij een nieuwe GGM-release

## Citation & verification rules

Elke factische claim moet traceerbaar zijn naar zijn bron:

1. **Refereer altijd naar bronbestanden** — geen ononderbouwde claims
2. **Format:** Verwijs naar `[[Wiki/Bronsamenvattingen/{domein}/{slug}]]` voor VNG-bronnen, of citeer direct: `> [citaat] (bron: bestandsnaam)`
3. **Bij tegenspraak:** Als twee bronnen het oneens zijn, documenteer beide en mark als `⚠️ Tegenspraak` in de BO-pagina
4. **Zonder bron:** Mark als `🔍 Verificatie nodig` en voeg toe aan openstaande vragen
5. **BO-grondslag:** Elke BO moet via de `## Bronnen`-sectie in de body traceerbaar zijn naar bronsamenvattingen
6. **GGM-matching:** Bij onzekere matches: mark als `ter discussie`, niet gokken

Dit zorgt voor **herleidbaarheid**: elke bewering kan teruggevoerd worden naar originele bronnen.

## Regels

1. **Wijzig nooit bestanden in `Sources/`** — deze zijn immutabel. (Bronnen zijn read-only.)
2. **Alle wiki-output gaat naar `Wiki/`** — houd de scheiding strikt tussen bronnen en wiki.
3. **Bespreek eerst, schrijf dan** — bij ingest altijd eerst de kernpunten bespreken met de gebruiker.
4. **Herleidbaarheid** (zie Citation & verification rules) — elk BO traceerbaar naar bronsamenvattingen, elke factische claim naar bron.
5. **Geen fantasie** — onzekere GGM-mapping markeren als `ter discussie`, niet gokken; elke aanname documenteren.
6. **Incrementeel** — update bestaande pagina's, geen duplicaten; consolideer vergelijkbare concepten.
7. **Update index en log** — na elke ingest of significante wijziging; zorg dat Wiki/index.md en Wiki/log.md actueel zijn.
8. **Gemeentelijk perspectief** — de wiki beschrijft wat de gemeente ziet, doet en registreert. Externe actoren en processen zijn context, geen eigen begrip of BO.
9. **Bestandsnamen** — lowercase met koppeltekens (bijv. `machine-learning.md`, `verkiezing.md`); geen spaties of CAPITALS.
10. **Duidelijke taal** — schrijf begrijpelijk Nederlands; geen technische jargon tenzij nodig; elk concept moet voor domeinexperts herkenbaar zijn.
11. **Bij onzekerheid** — vraag aan de gebruiker hoe iets moet worden gecategoriseerd of behandeld; gok niet.
12. **Geen retroactieve aannames** — als een pagina al bestaat, update deze in plaats van te gokken wat erin zou moeten staan; vraag eerst.
