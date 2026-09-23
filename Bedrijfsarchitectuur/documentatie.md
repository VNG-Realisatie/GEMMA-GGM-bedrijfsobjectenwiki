# Documentatie — GEMMA Bedrijfsobjectenwiki

Uitleg van de werkwijze, het proces en de rol van het GGM. Voor regels, structuur, skills en tools: zie [CLAUDE.md](CLAUDE.md).

## Kernidee: LLM-wiki (Karpathy)

Generiek voor alle wiki's in deze repo, zie [agent/documentatie.md](../agent/documentatie.md) §Kernidee.

## Doel

De gebruiker is het GEMMA-team bij VNG. De wiki is een professioneel werkinstrument voor standaardontwikkeling — fundament voor onderhoud en doorontwikkeling van de GEMMA bedrijfsobjecten — geen persoonlijk naslagwerk. Kwaliteit en onderbouwing zijn cruciaal: de wiki voedt een landelijke standaard.

Het bestaande GEMMA bedrijfsobjectenmodel is een ongefiltreerde kopie van het GGM. Deze wiki bouwt het opnieuw op met onderbouwing:

1. **Bronnen lezen en samenvatten** — VNG-beleidsdocumenten, proposities, verordeningen → bronsamenvattingen
2. **Onderwerpoverzicht opbouwen** — begrippen identificeren, typeren en beoordelen als BO-kandidaat
3. **BO's afleiden** — per BO-kandidaat: criteria toetsen, BO-pagina aanmaken met onderbouwing
4. **Hiaten signaleren** — GGM-entiteiten zonder BO, BO's zonder GGM-grondslag, correcties terugkoppelen

Het resultaat per onderwerp: BO-beslisdocumenten met metadata die als properties naar het GEMMA ArchiMate-model gaan.

De herleidbaarheidsketen is: `Sources/ → Bronsamenvattingen/ → Bedrijfsobjecten/`. Het onderwerpoverzicht organiseert de begrippen en hun BO-beoordeling.

**BO-afleiding staat op zichzelf.** Een begrip wordt BO op basis van de BO-criteria — dat kan zonder GGM. GGM-matching is aanvullende verrijking en verificatie, geen voorwaarde voor BO-status.

## Bottom-up proces: Bronnen → Bedrijfsobjecten

Per onderwerp wordt het volgende proces doorlopen:

1. **Bronnen ophalen** — beleidsdocumenten, proposities en verordeningen worden opgehaald, naar Markdown geconverteerd en opgeslagen in `Sources/` (immutabel)
2. **Bronsamenvattingen maken** — kernpunten uit de documenten worden geëxtraheerd en vastgelegd in `Wiki/Bronsamenvattingen/`
3. **Onderwerpoverzicht opbouwen** — begrippen uit de samenvattingen worden geïdentificeerd, getypeerd als ArchiMate-concepten en vastgelegd in een overzichtstabel
4. **BO-beoordeling** — elk begrip wordt getoetst aan expliciete criteria, zoals herkenbaarheid, eigen bestaan, levenscyclus en relaties; dit bepaalt de BO-kandidaten
5. **GGM-matching** — BO-kandidaten worden gematcht met bestaande GGM-entiteiten
6. **Hiaten signaleren** — GGM-entiteiten zonder BO-grondslag en BO-kandidaten zonder GGM-entiteit worden gesignaleerd richting het GGM-team

Het resultaat per onderwerp bestaat uit **BO-pagina's met volledige onderbouwing** (bron → begrip → criteria → GGM-match). De vastgestelde eigenschappen worden vervolgens opgenomen in het GEMMA ArchiMate-model.

### Werkwijze in de praktijk

De wiki wordt **onderwerp voor onderwerp** opgebouwd. Per onderwerp wordt het volledige proces doorlopen (bronnen → samenvattingen → onderwerpoverzicht → BO's) voordat het volgende onderwerp wordt opgepakt.

GGM-dekkingsanalyse gebeurt centraal via `/entiteitendekking` en werkt vanuit GGM-beleidsdomeinen (niet per wiki-onderwerp), omdat wiki-onderwerpen en GGM-beleidsdomeinen niet 1-op-1 overlappen. Het doel: inzicht welke beleidsdomeinen bronnen hebben vs. waar nog documenten gezocht moeten worden.

### Workflows

**Ingest** — wanneer de gebruiker een bron of onderwerp aanwijst om te verwerken:

1. Lees de volledige bron
2. Bespreek de kernpunten met de gebruiker voordat je schrijft
3. Maak een bronsamenvatting aan (zie `templates/bronsamenvatting.md`)
4. Maak of update het onderwerpoverzicht met nieuwe begrippen (zie `templates/onderwerpoverzicht.md`)
5. Maak BO-pagina's aan voor begrippen die de BO-criteria doorstaan, via `/element-pipeline` (zie `templates/element.md`)
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

## GGM als bron en validatie

Het GGM vervult zowel de rol van invoerbron als validatiekader:

* **Invoer** — het GGM definieert beleidsdomeinen en bevat kandidaat-bedrijfsobjecten
* **Validatie** — voor elk in een bron geïdentificeerd BO wordt gecontroleerd of dit voorkomt in het GGM; ontbrekende entiteiten worden teruggekoppeld. Het GGM is de primaire bron maar kan zelf fouten bevatten — ook correcties op bestaande GGM-entiteiten worden teruggekoppeld, niet alleen ontbrekende
* **Dekking** — met de skill `/entiteitendekking` wordt per GGM-beleidsdomein geanalyseerd welke entiteiten in een bron zijn aangetroffen en welke nog ontbreken

Hiermee ontstaat een gesloten feedbackloop tussen gemeentelijke bronnen, het GGM en het GEMMA-bedrijfsobjectenmodel.

## Bronnen

Bronnen zijn gemeentelijke beleidsdocumenten, VNG-publicaties, proposities, toelichtingen, verordeningen. Ze zijn georganiseerd per gemeentelijk onderwerp als subdirectory onder `Sources/`. Bronnen kunnen YAML-frontmatter bevatten (title, source, created, description, tags).

**GGM-pagina's zijn gegenereerde brondata, geen handmatige wiki-content.** De bestanden in `Wiki/GGM/` zijn een leesbare conversie van het XMI-bestand (de bron van waarheid), gegenereerd door `/generate-ggm`. Ze bevatten letterlijke definities uit het model, zonder synthese of interpretatie, en worden nooit handmatig bewerkt.

**Sources/GEMMA/** en **Sources/Standaarden/** bevatten aanvullende referentiebronnen: GEMMA-VNG-afspraken resp. basisregistratie-catalogi (BAG, BRK, BRO, NHR, RGBZ, RSGB, ZTC, BRP).

## GGM-terminologie

Het GGM is hiërarchisch opgebouwd: **taakvelden** (afgeleid van IV3) bevatten **beleidsdomeinen**.

- Taakveld = het bovenste niveau (bijv. "5 Sport, Cultuur en Recreatie", "9 Interne Organisatie")
- Beleidsdomein = het niveau daaronder (bijv. "Financien" onder taakveld 9, "Schulden" onder taakveld 6)
- Zie `Wiki/GGM/structuur-ggm.md` voor het volledige overzicht met definities

## Skills

Wiki-specifieke skills. Generieke skills (`crawl`, `setup-omgeving`) staan in [agent/documentatie.md](../agent/documentatie.md) §Skills.

Waar van toepassing staat de aangeroepen **Tool** (Python-script uit `tools/` — zie §"Tools" voor details) als tweede regel onder de Functie. Waar de skill zelf een pagina schrijft staat het gebruikte **template** uit `templates/` direct achter dat bestand, tussen haakjes. Elk output-bestand/-locatie staat op een eigen regel. "chat" bij Uit = geen bestand, alleen een antwoord/rapportage.

| Skill | Functie | In | Uit |
|---|---|---|---|
| **ingest**<br>`/ingest {bron\|onderwerp}` | Orchestrator: bron(nen) verwerken tot bronsamenvattingen en onderwerpoverzicht | bron/onderwerp | `Wiki/Bronsamenvattingen/` (template: `bronsamenvatting.md`)<br>`Wiki/Onderwerpoverzichten/` (template: `onderwerpoverzicht.md`)<br>`Wiki/index.md` (template: `index.md`)<br>`Wiki/log.md` (template: `log.md`)<br>Delegeert BO-beoordeling en -aanmaak naar element-pipeline |
| **element-pipeline**<br>`/element-pipeline {begrip}` | Orchestrator: begrip beoordelen via assess-element en, bij een positieve beoordeling, vastleggen via write-element | begrip (of lijst/onderwerp), nog niet beoordeeld | BO-/actor-/rol-pagina bij een positieve beoordeling, anders afwijzing met reden (chat) — delegeert naar assess-element en write-element |
| **assess-element**<br>`/assess-element {begrip}` | Begrip volledig beoordelen: classificatie, criteria, data-object, hiaat | begrip (uit onderwerpoverzicht/GGM) | beoordeling — geen bestand, invoer voor element-pipeline |
| **write-element**<br>`/write-element {element}` | Element vastleggen: GGM-match, frontmatter, pagina aanmaken<br>Tool: `parse_ggm_xmi.py` (optioneel, bij nieuwe GGM-release) | beoordeeld element + `ggm_parsed.json` | `Wiki/Bedrijfsobjecten/` (template: `element.md`)<br>of `Wiki/Actoren/` (template: `element.md`)<br>of `Wiki/Rollen/` (template: `element.md`)<br>Bij afwijking/hiaat: regel toegevoegd aan `Wiki/Analyses/ggm-terugmeldingen.md` (template: `ggm-terugmelding.md`) |
| **entiteitendekking**<br>`/entiteitendekking [taakveld]` | Uniforme GGM-analyse per taakveld/beleidsdomein: BO-matches, classificatie, relaties, hiaten<br>Tool: `entiteitendekking.py`, `entiteitendekking_sync_bo.py` | `ggm_parsed.json` + `Wiki/Bedrijfsobjecten/` | `Wiki/Analyses/entiteitendekking/` (eigen rapportformat, geen template)<br>teruggeschreven `analyse_ggm_dekking` in BO-frontmatter |
| **domain-status**<br>`/domain-status {onderwerp}` | Read-only voortgangsrapportage | `Wiki/` voor onderwerp | chat |
| **lint**<br>`/lint [onderwerp]` | Volledig mechanisch/technisch: deterministisch script (exacte telling), dan modelbeoordeling van wat nog niet gescript is<br>Tool: `lint_checks.py` (stap 1, altijd), `migrate_frontmatter_style.py` (bij fix) | hele wiki of onderwerp | chat |
| **audit-element**<br>`/audit-element {modus} [scope]` | Volledig inhoudelijk, alle elementtypen (BO/actor/rol): drie modi — `definities` (afwijkingen van GGM/bronnen), `duplicaten` (naamconflicten), `werkvoorraad` (ontbrekende actor-/rolpagina's) | `Wiki/Bedrijfsobjecten/` + `Wiki/Actoren/` + `Wiki/Rollen/` + `ggm_parsed.json` | chat; modus `definities` kan direct `bo_definitie`/`bo_toelichting` herschrijven; modus `werkvoorraad` levert een werkvoorraadlijst (vervolg via element-pipeline) |
| **fetch**<br>`/fetch {URL}` | URL ophalen als bronbestand in `Sources/` | URL | `Sources/{onderwerp}/*.md` |
| **clip**<br>`/clip {bestand}` | Clipping uit `Clippings/` verplaatsen naar `Sources/`<br>Roept: `/convert_pdf` (indien pdf) | `Clippings/*.md` | `Sources/{onderwerp}/*.md` |
| **convert_pdf**<br>`/convert_pdf {bestand}` | PDF converteren naar markdown voor `Sources/`<br>Tool: `convert_pdf.py` | PDF | markdown naast origineel |
| **export-ggm**<br>`/export-ggm` | Genereer 5 CSV's (objecten, relaties, diagrammen, beleidsdomeinen, diagram-mapping) uit XMI + wiki<br>Tool: `export_ggm_csv.py` | `ggm_parsed.json` + `Wiki/Bedrijfsobjecten/` | `exports/*.csv` (5 bestanden) |
| **generate-ggm**<br>`/generate-ggm` | Volledige pipeline: XMI → parsed JSON → Wiki/GGM markdown (herhaalbaar, telt alleen Objecttypen)<br>Tool: `parse_ggm_xmi.py`, `generate_ggm_wiki.py`, `generate_ggm_enrich_bo.py` | XMI-bestand | `Sources/GGM-repository/ggm_parsed.json`<br>`Wiki/GGM/**` |

**Model voorkeur:** staat per skill in de eigen frontmatter (`model: haiku`) als die afwijkt van het standaard project-model. Alleen `/lint` heeft deze pin (read-only analyse, geen reasoning); `/audit-element` doet inhoudelijke beoordeling en draait op het standaardmodel.

## Tools

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
