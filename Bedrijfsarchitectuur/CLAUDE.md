# GEMMA Bedrijfsobjecten Wiki

Werkinstrument van het GEMMA-team voor het onderbouwd opbouwen, onderhouden en doorontwikkelen van GEMMA bedrijfsobjecten. Werkwijze, proces en de rol van het GGM: zie [documentatie.md](documentatie.md).

## 1. Ad-hoc vragen

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

## 2. Bronnen toevoegen

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

## 3. Wiki-pagina's

Elke wiki-pagina heeft YAML-frontmatter. Templates per paginatype staan in `templates/`:

| Paginatype | Template | Locatie |
|---|---|---|
| Element (bedrijfsobject) | `templates/element.md` | `Wiki/Bedrijfsobjecten/{taakveld}/{beleidsdomein}/` |
| Element (actor) | `templates/element.md` | `Wiki/Actoren/` (plat) |
| Element (rol) | `templates/element.md` | `Wiki/Rollen/` (plat) |
| Element (bedrijfsfunctie) | `templates/element.md` | `Wiki/Bedrijfsfuncties/{taakveld}/{beleidsdomein}/` |
| Element (bedrijfsproces) | `templates/element.md` | `Wiki/Bedrijfsprocessen/{taakveld}/{beleidsdomein}/` |
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

## 4. BO-criteria & beoordeling

BO-afleiding staat los van GGM (zie [documentatie.md](documentatie.md)) — een begrip wordt beoordeeld op zijn eigen merites.

Alle beoordelingslogica staat in de skills, niet in dit bestand:
- **Elementbeoordeling:** `/assess-element` — domeinbepaling, begripstype, criteria (zie `templates/elementtype-criteria.md` voor de volledige begripstype-tabel en de criteria per elementtype), subtypes, data-object classificatie, autonomieregels

## 5. GGM-matching & hiaten

GGM-matching gebeurt **nadat** een begrip al op eigen kracht als BO is beoordeeld (zie §4) — het verrijkt en verifieert, het bepaalt niet.

- **Element vastleggen:** `/write-element` — grondslag, GGM-match, matchsterkte, duplicaten- en homoniemdetectie, hiërarchie, relaties, frontmatter, pagina, terugmelding
- **Grondslag zonder GGM:** `/write-element` stap 10 — het mechanisme achter het principe uit §4: een BO zonder GGM-grondslag krijgt lege `ggm_*`-velden en in plaats daarvan een Procesbron- of Juridische bron-sectie
- **Hiaat:** twee richtingen — GGM-entiteiten zonder BO, en BO's zonder GGM-grondslag; zie `/assess-element` voor hiaat-bepaling
- **Onzekere matches:** zie [IH6]
- **Entiteitendekking:** `/entiteitendekking` — analyseert dit systematisch per taakveld/beleidsdomein (zie §7)

## 6. Regels

Schrijfwijze: `- [ID] **kernonderwerp** — normatieve tekst`. Keywords: `ALTIJD` (verplicht), `NOOIT` (verboden), `ALS ... →` (conditioneel), `ALLEEN`/`ALLEEN ALS` (exclusieve beperking), `UITZONDERING:` (afwijking op een ALTIJD/NOOIT), `STANDAARD:` (default-gedrag). Sequentiële procedures (§1, §2) zijn geen losse regels en krijgen geen ID.

### Procesregels (PR) — hoe te werken

- [PR1] **Sources/ is read-only** — NOOIT bestanden in `Sources/` wijzigen; deze zijn immutabel (Bronnen zijn read-only).
- [PR2] **Wiki-output alleen naar Wiki/** — ALTIJD wiki-output naar `Wiki/`; houd de scheiding strikt tussen bronnen en wiki.
- [PR3] **Eerst bespreken, dan schrijven** — ALTIJD bij ingest eerst de kernpunten bespreken met de gebruiker, pas daarna schrijven.
- [PR4] **Incrementeel werken** — ALTIJD bestaande pagina's updaten in plaats van dupliceren; consolideer vergelijkbare concepten.
- [PR5] **Index en log actueel houden** — ALTIJD `Wiki/index.md` en `Wiki/log.md` bijwerken na elke ingest of significante wijziging.
- [PR6] **Bij onzekerheid navragen** — ALS onduidelijk is hoe iets gecategoriseerd of behandeld moet worden → vraag het de gebruiker; NOOIT gokken.
- [PR7] **Geen retroactieve aannames** — ALS een pagina al bestaat → update deze in plaats van te gokken wat erin zou moeten staan; vraag eerst.

### Inhoudsregels (IH) — herleidbaarheid & kwaliteit

Elke factische claim moet traceerbaar zijn naar zijn bron:

- [IH1] **Refereer altijd naar bronbestanden** — ALTIJD verwijzen naar bronbestanden; GEEN ononderbouwde claims.
- [IH2] **Verwijsformat naar bronnen** — Verwijs naar `[[Wiki/Bronsamenvattingen/{onderwerp}/{slug}]]` voor VNG-bronnen, of citeer direct: `> [citaat] (bron: bestandsnaam)`.
- [IH3] **Bij tegenspraak beide documenteren** — ALS twee bronnen het oneens zijn → documenteer beide en markeer als `⚠️ Tegenspraak` in de BO-pagina.
- [IH4] **Zonder bron markeren** — ALS een claim geen bron heeft → markeer als `🔍 Verificatie nodig` en voeg toe aan openstaande vragen.
- [IH5] **BO-grondslag via Bronnen-sectie** — Elke BO moet via de `## Bronnen`-sectie in de body traceerbaar zijn naar bronsamenvattingen.
- [IH6] **Onzekere GGM-matching/mapping als ter discussie** — Bij onzekere matches of mapping: markeer als `ter discussie`; NOOIT gokken; documenteer elke aanname.

Dit zorgt voor **herleidbaarheid**: elke bewering kan teruggevoerd worden naar originele bronnen.

### Scope- & vormregels (VR)

- [VR1] **Bestandsnamen: lowercase met koppeltekens** — Bestandsnamen ALTIJD lowercase met koppeltekens (bijv. `machine-learning.md`, `verkiezing.md`); GEEN spaties of CAPITALS.
- [VR2] **Begrijpelijk Nederlands** — Schrijf begrijpelijk Nederlands; geen technische jargon tenzij nodig; elk concept moet voor domeinexperts herkenbaar zijn.
- [VR3] **`bo_definitie`-vormcriteria** — Geldt voor `bo_definitie` op elk elementtype (bedrijfsobject, actor, rol): kort, bij voorkeur 1 zin, ≤160 tekens. Langer mag alleen als de tekst letterlijk uit GGM of bron is overgenomen. ALTIJD een zelfstandige tekst; NOOIT "gelijk aan GGM" of een vergelijkbare verwijzing als definitie.

### Bedrijfsobjecten (BO)

Regels die één skill uitvoert staan in die skill: `/assess-element` (6 criteria, abstract niveau, GGM-hiaten), `/write-element` (duplicaten/homoniemen, definities), `/audit-element` (modus `duplicaten`), `/ingest` (bronselectie, GGM-dekking). Hieronder alleen skill-overstijgende regels.

**Anti-patronen registr\***

- [BO1] **Anti-patroon "registr\*" als BO-afwijsgrond** — De 6 BO-criteria zijn de ENIGE toets (`/assess-element` Stap 7). NOOIT "registr*" (registreerbaar, registreren, registratieobject) gebruiken als filter, criterium of motivatie bij BO-beoordeling, begrippentabellen, GGM-hiaat-beoordelingen of inleidende analyses. Ook niet impliciet of als synoniem. UITZONDERING: de typering van data-objecten in `/assess-element` Stap 9–10; die bepaalt NOOIT BO-status.
- [BO2] **Vervangingen voor registr\*-taal** — Vervang: "registreerbaar object" → "zelfstandig object"; "wat gemeenten registreren" → "wat de gemeente herkent als zelfstandig ding"; "geen registratieobject" → afwijzen via de 6 criteria.
- [BO3] **Irrelevante afwijsgronden** — Irrelevant als afwijsgrond: "eigendom ligt bij X", "systeembeheer", "regie, niet registratie", "extern systeem".

**BO-naam bij GGM-generalisatie**

Scope: BO matcht een GGM-entiteit via generalisatie/specialisatie, matchsterkte "sterk"/"partieel", GGM-entiteit is breder.

- [BO4] **BO-naam blijft het beleidsbegrip** — STANDAARD: BO-naam blijft het gemeentelijke beleidsbegrip. NIET hernoemen naar de abstractere GGM-entiteitnaam.
- [BO5] **Afwijking vastleggen in GGM-bron, niet in Naamkeuze** — Leg de afwijking vast in de bestaande `## GGM-bron`/matchsterkte-toelichting. NOOIT in `## Naamkeuze` (uitsluitend voor naamcollisie-disambiguatie; zie `/write-element` Stap 0 en `templates/element.md`).
- [BO6] **Uitzondering: hernoemen naar de GGM-naam** — UITZONDERING (zeldzaam, per geval): hernoemen naar de GGM-naam ALLEEN ALS de term geen eigen identiteit heeft: er is in de gemeentelijke bronnen geen ander gebruik van de GGM-entiteit dan deze ene toepassing én de term is geen zelfstandig gedragen beleidsbegrip.
- [BO7] **Toets voor de BO6-uitzondering** — Toets voor [BO6]: zou een domeinexpert dit begrip ooit anders noemen, of gebruiken voor iets anders dan deze ene GGM-toepassing? ALS ja → niet hernoemen.
- [BO8] **Subtype of Specialisatie bij hernoeming** — Bij hernoeming wordt de specifieke term binnen de hernoemde BO een Subtype (geen eigen pagina) OF een Specialisatie (eigen pagina; ALLEEN ALS de term zelf de 6 criteria haalt).
- [BO9] **Geen bulk-hernoeming** — NOOIT in bulk doorvoeren op basis van één eerder akkoord. Bij twijfel of meerdere vergelijkbare gevallen: expliciet per geval voorleggen. Een generiek "ja, overal" is geen akkoord voor bulk.
- [BO10] **Wiki-links bijwerken na hernoeming** — Bij hernoeming of nieuwe generieke pagina: ALLE wiki-links bijwerken: bare `[[Naam]]`-links in Bronsamenvattingen, `bo_relaties` in andere BO's, onderwerpoverzicht-rijen, `Wiki/index.md`.
- [BO11] **Dekkingsrapport regenereren na hernoeming** — Daarna `entiteitendekking.py --all` regenereren en controleren volgens `/entiteitendekking` Stap 1 (controle na de run).

**Wiki-velden**

- [BO12] **BO-veldnamen en prefixen** — Veldnamen: `bo_definitie`, `bo_toelichting`, `bo_relaties`, `bo_synoniemen` (andere namen voor hetzelfde concept), `bo_homoniemen` (andere concepten met dezelfde GGM-naam). `bo_subtypes`: zie [BO15]. `bedrijfsprocessen` en `bedrijfsfuncties` behouden hun naam; sinds besluit 2026-09-23 zijn dit wiki-links naar eigen elementpagina's in `Wiki/Bedrijfsprocessen/`/`Wiki/Bedrijfsfuncties/` (zie §7, `templates/element.md`), geen vrije tekst meer — vrije-tekstvermeldingen van vóór dit besluit zijn migratie-achterstand, gesignaleerd door `/lint`. Prefix `bo_` = wiki-eigen BO-model; `ggm_*` = GGM-bron; `ggm_gemma_*` = GGM-GEMMA-referentie. De export leest de `bo_`-velden.
- [BO13] **Herkomst gemma_\*-velden** — `gemma_*`-waarden komen uit het GGM (dat een `gemma.csv` importeert). In `ggm_parsed.json` staan ze als `gemma_tags`; in BO-frontmatter als `ggm_gemma_*`.
- [BO14] **Geen wiki-beoordeling in gemma_\*-velden** — NOOIT `gemma_*`/`ggm_gemma_*` vullen vanuit wiki-beoordeling; wiki-eigen inhoud gaat naar `bo_*`.
- [BO15] **bo_subtypes blijft in gebruik** — `bo_subtypes` is in gebruik (NIET deprecated): per item `naam`, `omschrijving`, `ggm_entiteit`, `ggm_guid`, `ggm_attribuut`. `tools/entiteitendekking.py` leest de items met `ggm_attribuut: generalisatie` voor de dekking van GGM-specialisaties; lint, export en enrichment gebruiken het ook. NIET verwijderen.

Notes: precedent [BO6]: Woonboot → Vaartuig hernoemd (2026-07-09; Woonboot is de enige toepassing van GGM-entiteit Vaartuig). NIET hernoemd: Evenement, Woning, Rioolleiding (zelfstandige beleidsbegrippen). Rioolleiding = twee pagina's: Leiding (generieke GGM-match) + Rioolleiding (Specialisatie met generalisatie-relatie terug).

### Bronnen (SRC) — GGM en Sources/

Paden relatief aan `Bedrijfsarchitectuur/`.

**GGM-bronnen**

- [SRC1] **XMI is bron van waarheid, niet direct lezen** — `Sources/GGM-repository/Gemeentelijk Gegevensmodel XMI2.1.xml` is de bron van waarheid voor het GGM. NOOIT direct lezen; ALLEEN via de parser.
- [SRC2] **Nieuwe GGM-release omzetten** — ALS er een nieuwe GGM-release is → zet het XMI om in `Sources/GGM-repository/ggm_parsed.json` met `tools/parse_ggm_xmi.py` (via `/generate-ggm`). Beide bestanden staan in `Sources/GGM-repository/`.
- [SRC3] **Geen afgeleide GGM-bronnen** — NOOIT CSV-bestanden (~/Downloads) of andere locaties als GGM-bron gebruiken (afgeleiden; verouderd of incompleet).
- [SRC4] **Altijd zoeken in ggm_parsed.json** — ALTIJD zoeken en matchen in `Sources/GGM-repository/ggm_parsed.json` (structurele query, bv. Python/jq): entiteiten (incl. enumeraties) over alle beleidsdomeinen, namen en synoniemen, relaties, generalisaties (`uml_type: Generalization`), attributen, GUIDs, GEMMA-tags, diagram-IDs.
- [SRC5] **Wiki/GGM/ alleen voor leesbaar doorlopen** — `Wiki/GGM/{taakveld}/` ALLEEN gebruiken om een beleidsdomein leesbaar door te lopen (definities, attributen). Het bevat alleen Objecttypen en geen relaties, generalisaties, enumeraties, GUIDs of tags.

**Bestanden in Sources/**

- [SRC6] **Sources/ ook niet vertalen of uitbreiden** — Naast [PR1] (algemeen read-only): NOOIT vertalen of herschrijven, NOOIT per ongeluk uitbreiden.
- [SRC7] **Nederlandse bronnen letterlijk bewaren** — Nederlandse bronnen: originele Nederlandse tekst letterlijk bewaren. Ophalen: `/fetch` (curl, NOOIT WebFetch).
- [SRC8] **Alleen selectief kopiëren** — ALLEEN selectief kopiëren toegestaan: neem de beschrijvingen over; laat ruis weg (navigatie, nieuwslijsten, agenda's, gerelateerde links).
- [SRC9] **Geen wiki-links in Sources/** — NOOIT `[[wiki-links]]` in `Sources/`. ALTIJD platte bestandsreferentie: GGM-bronbestand → `bestandsnaam.md`; wiki-pagina → volledig pad, bv. `Wiki/Analyses/bestandsnaam.md`.

Notes: regels voor bronselectie staan in `/ingest`, voor PDF-conversie in `/convert_pdf` en `/fetch`, voor utrecht.bestuurlijkeinformatie.nl in `/fetch`.

### Wiki-conventies (WC)

**Links**

- [WC1] **Altijd wiki-links, geen platte tekst** — ALTIJD `[[wiki-links]]` voor verwijzingen naar wiki-pagina's en BO's in `Wiki/`-bestanden. NOOIT platte tekst.
- [WC2] **Toepassing per maptype** — Toepassing:
  - `Wiki/Bronsamenvattingen/`: links naar BO's, andere bronsamenvattingen, analyses.
  - `Wiki/Bedrijfsobjecten/`: links naar bronsamenvattingen (veld `bronnen`), gerelateerde BO's (sectie `relaties`), analyses.
  - `Wiki/Onderwerpoverzichten/`: links naar BO's (begrippentabel), bronsamenvattingen ("Verwerkte bronnen").
  - `index.md`, `log.md`: alle verwijzingen zijn wiki-links.
- [WC3] **Uitzondering: Sources-frontmatter als markdown-link** — UITZONDERING: frontmatter-velden die naar Sources wijzen (bv. `bron:` in een bronsamenvatting) → markdown-link `[text](path)`. In `Sources/` zelf: [SRC9].

**Scope**

- [WC4] **Gemeentelijk perspectief als scope** — ALTIJD gemeentelijk perspectief als scope: wat de gemeente ziet, doet, registreert en beslist.
- [WC5] **Ketenpartners alleen als context** — Ketenpartners (COA, IND, DT&V, UWV e.d.) en externe actoren/processen: ALLEEN als context of afbakening ("buiten scope") noemen. NOOIT een eigen begrips- of BO-pagina; NOOIT hun interne processen uitwerken. Geldt voor alle domeinen.
- [WC6] **Domein altijd afsluiten, ook bij 0 BO's** — Een domein dat geen BO's oplevert → afsluiten met een conclusie waarom. Ingest sluit een domein ALTIJD af, ook bij 0 BO's.

**Inhoud van wiki-pagina's**

- [WC7] **Geen verwijzingen naar technische bestanden** — NOOIT vanuit wiki-content (BO-pagina's, begrippen, analyses, bronsamenvattingen) verwijzen naar of citeren uit `CLAUDE.md`, `templates/`, `tools/` of skills (`.claude/commands/`). Onderbouwing staat op eigen kracht in de inhoud.
- [WC8] **Geen absolute taal zonder onderbouwing** — NOOIT absolute taal ("structureel buiten scope", "per definitie", "GGM modelleert nooit X") zonder domeinspecifieke onderbouwing.
- [WC9] **Herformuleer generieke "GGM doet dit niet"** — ALS een generieke "GGM doet dit niet"-bewering geen specifieke reden heeft → herformuleer naar "in het GGM niet compleet gedekt". Specifieke reden = ontbrekend beleidsdomein, specifieke wetsverwijzing of attribuutvergelijking.
- [WC10] **Concrete reden: niet aanpassen** — ALS een bewering een concrete, specifieke reden geeft (bv. "dit beleidsdomein begint pas bij X", "GGM heeft wel BAG-locaties maar niet dit type locatie") → NIET aanpassen, ook niet als het woord "structureel" erin staat.
- [WC11] **Per geval beoordelen bij opschoning** — Bij opschoning van deze framing: per geval beoordelen. NOOIT blind alle "structureel"/"buiten scope" vervangen.

**Gegenereerde bestanden en subagent-runs**

- [WC12] **Wiki/GGM/ nooit handmatig bewerken** — `Wiki/GGM/` NOOIT handmatig bewerken (gegenereerd). Wijzig ALLEEN door te regenereren via `/generate-ggm`. Herstel een ongewenste externe wijziging met `git checkout -- <bestand>`.
- [WC13] **Checklist na elke subagent-run** — Checklist na elke subagent-run (zie [W4]):
  1. `Wiki/Analyses/ggm-terugmeldingen.md`: nieuwe hiaten/correcties uit de BO-pagina's toegevoegd?
  2. `Wiki/index.md`: alle nieuwe BO's en bronsamenvattingen opgenomen?
  3. `Wiki/log.md`: entry klopt met werkelijke aantallen?
  4. `Wiki/Onderwerpoverzichten/{onderwerp}.md`: `bo_count` en `begrippen_count` actueel?
  5. Forward references in BO-pagina's: verwijzen ze naar bestaande bestanden?

Notes:
- `templates/element.md` verwijst naar [WC7].
- Precedent [WC9]: GGM-beleidsdomein Normafwijking (Participatiewet-ingest, 2026-09-18) modelleert Maatregel en Boete; dit weerlegde "GGM modelleert nooit processen/governance".

## 7. Skills & tools

### Directorystructuur

```
Bedrijfsarchitectuur/
├── CLAUDE.md              # dit bestand — regels en conventies
├── documentatie.md        # werkwijze, proces en de rol van het GGM
├── .claude/commands/      # skills (`/command`), projectlokaal — zie documentatie.md §"Skills"
├── templates/             # paginatemplates en referentietabellen (o.a. elementtype-criteria.md)
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
│   ├── Bedrijfsfuncties/  # Business Function-pagina's, per {taakveld}/{beleidsdomein}/
│   ├── Bedrijfsprocessen/ # Business Process-pagina's, per {taakveld}/{beleidsdomein}/
│   ├── Bronsamenvattingen/# samenvattingen per bron, georganiseerd per {onderwerp}/
│   ├── Analyses/          # per-taakveld dekkingsrapporten, hiaten, terugmeldingen
│   ├── Vragen/            # ad-hoc vraag-antwoord-pagina's (zie §1)
│   └── GGM/               # gegenereerde leesbare GGM-representatie, niet handmatig bewerken
│       ├── structuur-ggm.md
│       └── {taakveld}/    # per taakveld, met index.md en bestanden per beleidsdomein
├── Clippings/             # landingszone voor webclippings (Web Clipper uitvoer)
├── ToDo/                  # taken en agenda
├── exports/               # gegenereerde CSV's (nieuwste versie alleen)
├── tools/                 # Python-scripts voor XMI-verwerking
└── .trash/                # verwijderde items (archief)
```

Onderwerpen en taakvelden worden **niet** vooraf benoemd in de structuur — ze ontstaan bij het verwerken van bronnen. Controleer bestaande subdirectories voordat je een nieuwe aanmaakt.

Skills zijn project-lokaal: `.claude/commands/` (binnen `Bedrijfsarchitectuur/`), zelfde niveau als `tools/` (Python-scripts). Skills die wiki-pagina's wijzigen updaten altijd `Wiki/index.md` en voegen een entry toe aan `Wiki/log.md`. Elke skill is zelfvoorzienend (Input/Output/aangeroepen tool staan in de skill zelf). Functie-overzicht per skill en tool: zie [documentatie.md](documentatie.md).

## 8. Gedragsprincipes

- Don't assume. Don't hide confusion. Surface tradeoffs.
- Minimum code that solves the problem. Nothing speculative.
- Touch only what you must. Clean up only your own mess.
- Define success criteria. Loop until verified.
