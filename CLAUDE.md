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

De wiki wordt **domein voor domein** opgebouwd. Per domein wordt het volledige proces doorlopen (bronnen → samenvattingen → domeinoverzicht → BO's → dekkingsanalyse) voordat het volgende domein wordt opgepakt.

### Onderhoudscyclus

Na de initiële opbouw wordt het model onderhouden bij:
- Nieuwe GGM-releases (entiteiten hertoetsen)
- Nieuwe gemeentelijke onderwerpen (bronnen toevoegen, domeinoverzicht uitbreiden, BO's afleiden)

### LLM-rol

De LLM fungeert als **eerste filter**:

**Zelfstandig afhandelen** wanneer alle drie voorwaarden waar zijn:
1. Begripstype is `object` en abstractieniveau is `operationeel`
2. Minstens 5 van de 6 BO-criteria zijn van toepassing
3. GGM-matchsterkte is `exact` of `sterk`

**Voorleggen aan het team** bij:
- Begripstype `instrument`, `actor` of `doelgroep` (altijd)
- Minder dan 5 BO-criteria van toepassing
- GGM-matchsterkte `partieel` of `zwak`
- Generalisatiekeuzes (welk niveau wordt het BO?)
- Elke voorgestelde GGM-terugmelding

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

### BO-criteria

Een begrip is een bedrijfsobject als het aan de **meeste** van deze criteria voldoet:

- Heeft betekenis binnen het domein
- Is herkenbaar voor domeinexperts
- Heeft een eigen bestaan binnen het domein
- Kan in meervoud bestaan (er zijn meerdere exemplaren)
- Heeft een eigen levenscyclus
- Heeft relaties met andere concepten

**Geen BO** als het slechts een eigenschap, status, activiteit, regel of classificatie van iets anders is.

**Registratie in een informatiesysteem is geen BO-criterium.** Alleen de 6 criteria hierboven zijn leidend. Gebruik ook niet als afwijsgrond: eigendom ("eigendom ligt bij Eneco"), systeembeheer ("gemeente registreert dit niet"), of regietype ("regie, niet registratie"). De enige vraag is: herkent de gemeente dit als een zelfstandig ding waar beleid op gemaakt wordt?

### Begripstypen en abstractieniveaus

Zie `templates/begripstypen.md` voor de volledige classificatietabel en filterlogica.

### Afleidingsregels voor bedrijfsobjecten

#### Grondslag bepalen

1. **Zoek een GGM-entiteit.** Is er een directe match → grondslag `ggm-entiteit`.
2. **Geen entiteit, wel afleidbaar?** Kan het BO berekend/geaggregeerd worden uit bestaande GGM-objecten → grondslag `ggm-afgeleid`.
3. **Geen GGM-basis, wel een proces?** Artefact dat ontstaat in een gemeentelijk proces → grondslag `procesobject`.
4. **Geen GGM-basis, juridisch/beleidsmatig kader?** Verordening, regeling of bevoegdheid → grondslag `governance-object`.

Het ontbreken van een GGM-grondslag is voor procesobjecten en governance-objecten **structureel**, niet incidenteel — het GGM modelleert data, niet processen of governance (zie [[ggm-dekkingspatroon]]).

#### GGM-matchsterkte

| Matchsterkte | Betekenis | Actie |
|---|---|---|
| **exact** | GGM-entiteit en BO zijn hetzelfde concept, definitie klopt | Overnemen, definitie uit GGM |
| **sterk** | Zelfde concept, maar definitie of scope wijkt licht af | Overnemen, afwijking documenteren en terugmelden |
| **partieel** | GGM-entiteit dekt een deel van het BO, of BO is aggregatie van meerdere entiteiten | Overnemen met toelichting, overweeg terugmelding |
| **zwak** | Verwant concept maar wezenlijk andere scope of granulariteit | Relatie noteren, niet als grondslag gebruiken |

#### Mapping van GGM-entiteit naar bedrijfsobject

- Bij voorkeur 1-op-1 mapping (beheerbaarheid, herkenbaarheid).
- Aggregatie toegestaan als het GGM te granulair is — noteer welke GGM-entiteiten zijn samengevoegd.
- Als een GGM-entiteit in meerdere beleidsdomeinen voorkomt: maak één bedrijfsobject met alle GGM-bronnen.

#### Generalisaties (overerving)

Bij een generalisatiehiërarchie moet expliciet worden besloten op welk niveau het BO wordt gedefinieerd. Beslisregel: **praat de gemeente erover als aparte dingen?** Zo ja → aparte BO's. Zo nee → één BO op het herkende niveau.

| Situatie | BO-keuze |
|---|---|
| Specialisaties zijn herkenbaar en hebben eigen processen/relaties | Elke specialisatie wordt een BO; abstract niveau wordt geen BO |
| Specialisaties zijn uitwisselbaar; onderscheid is alleen technisch | Abstract niveau wordt het BO; specialisaties geen apart BO |
| Zowel abstract als specialisaties zijn herkenbaar | Beide worden BO; generalisatierelatie vastleggen |

Noteer de beslissing en motivatie in de body. Markeer als `⚠️ ter discussie` als de keuze niet eenduidig is.

#### Specialisaties (subtypes)

Wanneer een BO herkende subtypes heeft die **geen apart BO** zijn (ze zijn uitwisselbaar, vallen onder hetzelfde register en dezelfde processen), leg ze vast als `gemma_subtypes` in de frontmatter en een **Specialisaties**-tabel in de body. Dit voorkomt dat elk subtype een apart begrip of BO wordt en houdt de begrippentabel in het domeinoverzicht schoon.

Subtypes zijn typisch attribuutwaarden (bijv. GGM-enumeratie `TypeMonument`) of categorieën uit beleidsbronnen. In de GEMMA-export komen ze in de kolom `GEMMA-subtypes`.

**Regel: GGM-link verplicht.** Elk subtype dat overeenkomt met een GGM data-object (Class of Enumeration) moet gelinkt zijn:
- **Frontmatter**: `ggm_entiteit`, `ggm_guid` en `ggm_attribuut` per subtype (voor export en traceerbaarheid). Link naar de GGM-entiteit die het attribuut draagt, niet naar enumeraties die niet in de bronbestanden staan.
- **Body-tabel**: kolommen Subtype, Omschrijving, GGM-attribuut. GGM-attribuut bevat een markdown-link naar de GGM-entiteit in het bronbestand gevolgd door `→ attribuutnaam`, bijv. `[Beschermde Status](Sources/GGM/.../monumenten.md) → type`. Geen GUID in de tabel — die staat in de frontmatter.

Als er geen GGM-match is, laat de velden leeg.

Voorbeeld: Monument heeft subtypes kerkgebouw, synagoge, klooster, beschermd stadsgezicht — alle vallen onder GGM-enumeratie TypeMonument.

#### Relaties tussen bedrijfsobjecten

BO-relaties worden afgeleid van GGM-associaties maar vereenvoudigd naar bedrijfsniveau:

- **Overnemen**: herkenbaar in de bedrijfspraktijk → 1-op-1 overnemen
- **Inkorten**: GGM-relatie via tussenliggende entiteit die geen BO wordt → directe BO-relatie
- **Samenvoegen**: meerdere GGM-associaties op bedrijfsniveau niet onderscheidbaar → samenvoegen
- **Weglaten**: puur technische relaties (referentietabellen, enumeraties)
- **Toevoegen**: relatie bestaat op bedrijfsniveau maar niet in GGM → hiaat-relatie

### GGM-hiaten beoordelen

Voordat een BO als "hiaat" in het GGM wordt gemeld, doorloop deze checklist:

**Stap 1: Bepaal wat het BO is**
- Is het een **dataobject** (wat gemeenten registreren in informatiesystemen)?
- Of is het een **proces** (hoe werk verloopt: processen, cycli, stappen)?
- Of is het een **governance-instrument** (wetten, verordeningen, bevoegdheden)?

**Stap 2: Controleer GGM-scope**
Het GGM modelleert **dataobjecten**. Dus:
- **Dataobjecten** die geen GGM-entiteit hebben → potentiële hiaat (rapporteren)
- **Processen** die geen GGM-entiteit hebben → structureel buiten scope (niet rapporteren)
- **Governance-instrumenten** die geen GGM-entiteit hebben → structureel buiten scope (niet rapporteren)

**Stap 3: Motiveer de melding**

Als het een dataobject is, motiveer waarom het in het GGM past:
- Waar worden deze gegevens in de gemeente geregistreerd/beheerd?
- Welke attributen/eigenschappen zijn registreerbaar?
- Pakt het in een bestaand GGM-beleidsdomein (bijv. registratie, boekhoudkunde, proces-output)?
- Voorbeelden: BAG-locatie (registratie), Begroting (boekhoudkunde), Stembureau (registratieobject)

**Stap 4: Formuleer als terugmelding**

Voorbeeld goed:
> **Stembureau** — Registratieobject voor fysieke locaties waar stemmingen plaatsvinden (adres, capaciteit, toegankelijkheid). Dataobject vergelijkbaar met BAG-locatie maar met verkiezings-specifieke properties. Zou onder Bestuur (taakveld 0) kunnen.

Voorbeeld fout:
> **Verkiezing** — Ontbreekt in GGM. [FOUT: dit is een proces, geen dataobject]

**Regel: Wees conservatief met hiaten.** Alleen dataobjecten die gemeenten daadwerkelijk registreren rapporteren. Geen processen, geen governance.

### Blik op bronnen

Bij het lezen van **alle bronnen** — zowel GGM als VNG-beleidsdocumenten — dezelfde blik:

1. **Objecten identificeren**: welke dingen worden benoemd die in processen worden gebruikt, geproduceerd of geregistreerd?
2. **Relaties herkennen**: welke objecten worden in samenhang genoemd?
3. **Generalisaties expliciteren**: overkoepelende termen die meerdere specifiekere dingen omvatten?
4. **Granulariteit beoordelen**: grover of fijner dan het GGM modelleert?

Bij VNG-bronnen zijn juist de mismatches met het GGM (hiaten, aggregaties, andere granulariteit) waardevolle bevindingen — **maar alleen voor dataobjecten** (zie "GGM-hiaten beoordelen").

### Conventies

- **Taal**: Nederlands, tenzij gevestigde Engelse term (ArchiMate, business object).
- **Bestandsnamen**: lowercase, koppeltekens. Voorbeeld: `onroerende-zaak.md`.
- **Cross-references**: Obsidian `[[wiki-links]]` voor alle verwijzingen tussen wiki-pagina's.
- **Wiki-links in tabellen**: gebruik `[[pad/naar/pagina]]` zonder alias — de `|` in `[[pad|alias]]` breekt markdown-tabellen. Buiten tabellen mag alias-syntax wel.
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
6. **Herleidbaarheid** — BO-pagina's moeten `bronnen` in frontmatter hebben; claims moeten citaten hebben

**Rapportage:** Bevindingen als **genummerde lijst met voorgestelde fixes** per categorie (contradities, orphans, verouderd, etc.).

## Skills

Beschikbaar als `/command` (gedefinieerd in `.claude/commands/`). Skills die wiki-pagina's wijzigen updaten altijd `Wiki/index.md` en voegen een entry toe aan `Wiki/log.md`.

| Skill | Aanroep | Functie |
|---|---|---|
| **ingest** | `/ingest {bron\|domein}` | Bron(nen) verwerken: samenvatting → domeinoverzicht bijwerken → BO's afleiden |
| **fetch** | `/fetch {URL}` | URL ophalen als bronbestand in `Sources/` |
| **clip** | `/clip {bestand}` | Clipping uit `Clippings/` verplaatsen naar `Sources/` |
| **lint** | `/lint [domein]` | Consistentiechecks op wiki (frontmatter, herleidbaarheid, hiaten) |
| **coverage** | `/coverage {domein}` | GGM-dekkingsanalyse: welke entiteiten zijn/worden BO |
| **domain-status** | `/domain-status {domein}` | Voortgangsoverzicht (bronnen, begrippen, BO's, dekking) |
| **test-bo** | `/test-bo {begrip}` | Begrip tegen BO-criteria toetsen |
| **match-ggm** | `/match-ggm {BO}` | BO matchen op GGM-entiteit met matchsterkte |
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
5. **BO-grondslag:** Elke BO moet via `bronnen` in frontmatter traceerbaar zijn naar bronsamenvattingen
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
