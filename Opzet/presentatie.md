# Onderbouwd werken aan het GEMMA-bedrijfsobjectenmodel

**Een LLM-wiki als werkinstrument**

Kennissessie GEMMA-team · slides gescheiden door `---` (bruikbaar in Marp, Obsidian Slides, reveal.js e.d.)

---

## Waar dit over gaat

- Hoe we het GEMMA-bedrijfsobjectenmodel opnieuw onderbouwen
- Hoe een LLM daarbij helpt — als eerste filter, niet als orakel
- Hoe de werkwijze onafhankelijk is van één AI-leverancier
- Hoe je zelf kunt meewerken

---

## Het probleem

- Het huidige GEMMA-bedrijfsobjectenmodel is een **gefilterde kopie van het GGM**
- Maar: die filtering gebeurde **zonder expliciete criteria**
- Waarom is entiteit X wél een bedrijfsobject en Y niet? Niemand kan het nazoeken
- Nieuwe GGM-releases en nieuwe beleidsthema's maken dit elke keer pijnlijker

---

## Wat we willen

- Elke keuze **onderbouwd**: vaste criteria, expliciet toegepast
- Elke bewering **herleidbaar**: terug te volgen tot een beleidsbron
- Het resultaat **onderhoudbaar**: herhaalbaar bij nieuwe releases en onderwerpen
- En: een **feedbackloop** naar het GGM-team (hiaten, duplicaten, definitieverschillen)

---

## Het kernidee: een LLM-wiki

Naar het patroon van Karpathy:

- Kennis wordt niet telkens opnieuw verzameld, maar **stapsgewijs opgebouwd** in een wiki
- Elke nieuwe bron wordt gelezen, samengevat en **verwerkt in bestaande pagina's**
- Verbanden en tegenstrijdigheden worden expliciet gemaakt
- De wiki wordt gaandeweg rijker én consistenter

---

## Rolverdeling mens ↔ LLM

| Mens (GEMMA-team) | LLM |
|---|---|
| Selecteert bronnen | Leest en vat samen |
| Beslist twijfelgevallen | Beoordeelt tegen vaste criteria |
| Stelt vast | Structureert en legt vast |
| Bewaakt de lijn | Signaleert hiaten en conflicten |

De LLM is het **eerste filter** — de mens blijft het besliskader.

---

## Getrapte autonomie

1. **Bronniveau** — de LLM bespreekt eerst de kernpunten, schrijft dan pas
2. **Eenduidige begrippen** — voldoen ze aan strikte voorwaarden (type, 5+ criteria, sterke GGM-match), dan handelt de LLM ze zelfstandig af
3. **Twijfelgevallen** — per stuk voorgelegd aan het team

Zo blijft het snel én controleerbaar.

---

## De structuur in één beeld

```
Sources/                    Wiki/
(immutabel)                 (afgeleid, door LLM onderhouden)

beleidsdocumenten   ──►   Bronsamenvattingen/
GGM (XMI)           ──►   Onderwerpoverzichten/  ──►  Bedrijfsobjecten/
                          Actoren/ · Rollen/           Analyses/
```

---

## De herleidbaarheidsketen

```
Sources/  →  Bronsamenvattingen/  →  Bedrijfsobjecten/
(exacte kopie)   (schakelstuk)        (beslisdocument)
```

- Elke BO-pagina verwijst naar bronsamenvattingen
- Elke bronsamenvatting verwijst naar het bronbestand
- Elke claim heeft een citaat of bron

**Niets in de wiki zweeft.**

---

## Sources: de spelregels

- **Inhoud is immutabel** — nooit herschrijven, vertalen of samenvatten; ordenen mag
- Exacte kopieën van beleidsdocumenten, verordeningen, VNG-publicaties
- Gemeentelijke onderwerpen onder `Sources/Onderwerpen/{onderwerp}/`
- Bronnen uit meerdere gemeenten zijn juist goed: dat maakt BO's generiek

---

## Het GGM: bron én validatiekader

- **Bron:** het GGM levert beleidsdomeinen en kandidaat-entiteiten
- **Validatie:** elk uit bronnen afgeleid BO wordt getoetst tegen het GGM
- Het XMI-bestand is de bron van waarheid; een parser maakt er leesbare pagina's en doorzoekbare data van
- Structuur: **taakvelden** (IV3) → **beleidsdomeinen** → entiteiten

---

## De wiki: paginatypes

| Pagina | Functie |
|---|---|
| Bronsamenvatting | Kernpunten van één bron |
| Onderwerpoverzicht | Alle begrippen van een onderwerp in één tabel |
| Element (BO / actor / rol) | Het beslisdocument met onderbouwing |
| Analyse | Dekkingsrapporten, syntheses, terugmeldingen |

Plus: `index.md` (overzicht) en `log.md` (logboek van alle acties).

---

## De werkwijze: onderwerp voor onderwerp

Per onderwerp het volledige proces afronden:

```
bronnen ophalen → samenvatten → begrippen beoordelen
    → elementen vastleggen → hiaten signaleren → aftekenen
```

Ruim 30 onderwerpen verwerkt: van belastingen en financiën tot milieu, mobiliteit en werk & inkomen.

---

## Stap 1-2: bron ophalen en bespreken

- Bron binnenhalen als **exacte kopie** (URL-fetch, webclipper of PDF-conversie)
- LLM leest de volledige bron en bespreekt de kernpunten met het team
- Welke bestanden zijn rijk? Welke begrippen springen eruit?
- **Er wordt nog niets geschreven**

---

## Stap 3-4: samenvatten en beoordelen

- Per bron een **bronsamenvatting** met kernbegrippen en citaten
- Per begrip een volledige beoordeling:
  - **Begripstype** — object, governance-instrument, actor, rol, doelgroep, thema, doel of waarde
  - **Structuuranalyse** — subtypes, specialisaties, generalisaties
  - **De 6 BO-criteria**

---

## De 6 BO-criteria

1. Heeft betekenis binnen het onderwerp
2. Is herkenbaar voor domeinexperts
3. Heeft een eigen bestaan
4. Kan in meervoud bestaan
5. Heeft een eigen levenscyclus
6. Heeft relaties met andere concepten

**5+ = bedrijfsobject.** En dit is de éérste en enige toets — "wordt het geregistreerd" of "van wie is het" telt niet mee.

---

## Stap 5: vastleggen als element

- **Grondslag:** ggm-entiteit · ggm-afgeleid · procesobject · governance-object
- **GGM-match** met matchsterkte (exact / sterk / partieel / zwak)
- Definitie volgens vaste regels: GGM overnemen als die klopt, anders eigen definitie mét documentatie van de afwijking
- Duplicaten en homoniemen expliciet gedocumenteerd
- Volledige frontmatter → wordt straks properties in het ArchiMate-model

---

## Actoren en rollen

- Ook actoren (wie handelt) en rollen (in welke verantwoordelijkheid) krijgen eigen pagina's
- **Twee-pagina-patroon:** een begrip kan actor/rol zijn én bedrijfsobject (er worden gegevens over vastgelegd) — dan twee gekoppelde pagina's
- Externe actoren (ketenpartners) kunnen een actor-/rolpagina krijgen; het gemeentelijk perspectief begrenst alleen de **BO-scope**

---

## Stap 6: hiaten en terugmeldingen

- Data-objecten zonder GGM-entiteit → **potentieel GGM-hiaat**
- Processen en governance zijn structureel buiten GGM-scope — geen hiaat
- Duplicaten (zelfde concept, twee GUIDs) → advies samenvoegen
- Homoniemen (zelfde naam, ander concept) → hernoemadvies
- Alles landt in één terugmeldingenregister voor het GGM-team

---

## Kwaliteit bewaken: de dekkingsanalyse

- Script berekent per taakveld/beleidsdomein: welke GGM-entiteiten zijn gedekt, waardoor, en wat niet
- Ambigue gevallen (`ter discussie`) kiest **een mens**, en die keuze overleeft her-runs
- Dekkingspercentages met eerlijke noemer (niet-toepasbare entiteiten tellen niet mee)
- Omgekeerde index per BO: welke GGM-entiteiten dekt dit BO?

---

## Kwaliteit bewaken: lint en audits

- **Lint** — consistentiecheck: herleidbaarheid, frontmatter, links, symmetrie van relaties
- **Audit definities** — kloppen definities met GGM en bronnen?
- **Audit duplicaten** — ongedocumenteerde naamconflicten
- **Audit actoren** — ontbrekende actor-/rolpagina's in bestaande content
- Alles rapporteert eerst; herstellen gebeurt na beoordeling

---

## De uitkomst per onderwerp

- Begrippentabel met álle begrippen — ook de afgewezen (met reden)
- Elementpagina's met volledige onderbouwing
- Terugmeldingen richting GGM
- Export naar CSV's voor de GGM-GEMMA-uitwisseling en het ArchiMate-model

---

## Waarom vendor-neutraal?

- De werkwijze zat vast aan één tool (Claude Code): specifieke commandobestanden, één monolitisch instructiebestand
- LLM-tooling verandert snel; het team gebruikt verschillende tools
- **De kennis en werkwijze zijn van het team, niet van de tool**

---

## De nieuwe opzet: drie lagen

```
Opzet/
├── AGENTS.md        ← entrypoint: kerninstructies (open standaard)
├── context/         ← KENNIS: project, regels, conventies (8 kleine bestanden)
├── workflows/       ← PROCES: ingest, vragen, lint, onderhoud
├── prompts/         ← TAKEN: 15 uitvoerbare prompts met {{parameters}}
├── templates/       ← paginasjablonen
├── adapters/        ← per tool: zo laad je dit
└── tools/           ← catalogus van de Python-scripts
```

---

## Werkt met elke tool

| Tool | Hoe |
|---|---|
| Claude Code, Codex, Cursor, Aider | Lezen AGENTS.md (vrijwel) automatisch |
| ChatGPT, Gemini, Open WebUI | AGENTS.md als systeeminstructie, context als projectkennis |
| OpenAI API, OpenRouter | System prompt samenstellen uit de context-bestanden |
| Ollama, LM Studio | Modelfile/preset met AGENTS.md; lichte taken lokaal |

Eén bron van waarheid, dunne adapters per tool.

---

## Wat een prompt is

Elke taak is een markdown-bestand met een vast formaat:

- **Doel** · **Aanbevolen model** (standaard/licht) · **Parameters** (`{{onderwerp}}`)
- **Benodigde context** — welke bestanden de LLM moet kunnen lezen
- **Verwachte uitvoer** — wat er aan het eind bestaat
- Het **promptblok** zelf + een voorbeeld

Geen slash-commands nodig: invullen en plakken werkt overal.

---

## De spelregels blijven overal gelden

Waar de LLM ook draait:

1. Sources-inhoud is onaantastbaar
2. Alles herleidbaar — geen fantasie, onzeker = `ter discussie`
3. Bespreken vóór schrijven (op bronniveau)
4. Incrementeel — bestaande pagina's bijwerken
5. Index en log altijd actueel
6. Bij twijfel: vragen, per geval

---

## Wat dit oplevert

- **Uitlegbaarheid** — elk BO-besluit is na te lezen, tot de bron
- **Consistentie** — vaste criteria, vaste templates, geautomatiseerde checks
- **Onderhoudbaarheid** — nieuwe GGM-release? Pipeline draaien, verschillen beoordelen
- **Toolvrijheid** — vandaag Claude, morgen iets anders: de werkwijze blijft

---

## Zelf aan de slag (1): meelezen

1. Open de wiki (Obsidian of VS Code)
2. Start bij `Wiki/index.md` — het overzicht van alle onderwerpen en elementen
3. Volg de keten van een BO terug: pagina → bronsamenvatting → bron
4. `Wiki/log.md` toont wat er wanneer is gebeurd, en waarom

---

## Zelf aan de slag (2): meewerken

1. Kies je tool en volg de adapter in `Opzet/adapters/`
2. Nieuwe bron? → prompt `fetch` of `clip`, daarna `ingest`
3. Vraag over een onderwerp? → gewoon stellen; goede antwoorden gaan de wiki in
4. Voortgang zien? → prompt `domain-status`

---

## Samengevat

- Een wiki die kennis **opbouwt** in plaats van telkens opnieuw verzamelt
- Een LLM als **eerste filter**, de mens als besliskader
- Elke keuze **onderbouwd en herleidbaar**
- Werkwijze **onafhankelijk van de tool**

**Vragen?**
