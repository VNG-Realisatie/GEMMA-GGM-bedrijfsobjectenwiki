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
├── Sources/               # ruwe bronnen, NIET aanpassen
│   ├── Onderwerpen VNG/   # VNG-publicaties en beleidsdocumenten per domein
│   │   ├── Arbeidszaken/
│   │   ├── Asiel en Integratie/
│   │   ├── Belastingen/
│   │   ├── Bestuur/
│   │   ├── Cultuur/
│   │   ├── Dienstverlening/
│   │   ├── Economie/
│   │   ├── Energie en Klimaat/
│   │   ├── Europa en Internationaal/
│   │   ├── Financien/
│   │   ├── Informatiesamenleving/
│   │   ├── Maatschappelijke Ondersteuning/
│   │   ├── Milieu/
│   │   ├── Omgevingswet/
│   │   ├── Onderwijs/
│   │   ├── Openbare Gezondheid/
│   │   ├── Openbare Orde en Veiligheid/
│   │   ├── Recht/
│   │   ├── Risicobeheer/
│   │   ├── Ruimte Wonen en Mobiliteit/
│   │   ├── Schulden en Armoede/
│   │   ├── Sociaal Domein/
│   │   ├── Werk en Inkomen/
│   │   └── {domein}/
│   ├── GGM/        # leesbare representatie van het Gemeentelijk Gegevensmodel
│   │   ├── structuur-ggm.md       # taakvelden en beleidsdomeinen met definities
│   │   ├── 3-economie/            # taakveld 3 Economie
│   │   │   └── economie.md
│   │   ├── 5-sport-cultuur-en-recreatie/  # taakveld 5
│   │   │   └── sport-cultuur-en-recreatie.md
│   │   ├── 6-sociaal-domein/      # taakveld 6 Sociaal Domein
│   │   │   ├── index.md           # overzicht met links naar beleidsdomeinen
│   │   │   ├── generiek-jeugd-en-wmo.md
│   │   │   ├── inburgering.md
│   │   │   ├── inkomen.md
│   │   │   ├── schulden.md
│   │   │   ├── terug-en-invordering.md
│   │   │   ├── werk.md
│   │   │   ├── sociaal-domein-generiek.md
│   │   │   └── sociaal-domein-overig.md
│   │   ├── 9-interne-organisatie/ # taakveld 9
│   │   │   └── financien.md
│   │   └── 99-kern/               # taakveld 99 Kern
│   │       ├── rsgb.md
│   │       └── rgbz.md
│   └── {domein}/          # nieuwe domeinen als subdirectory
├── Wiki/
│   ├── index.md           # inhoudelijk overzicht van alle wiki-pagina's
│   ├── log.md             # chronologisch logboek van ingest/query/lint acties
│   ├── Domeinen/          # domeinoverzichten met begrippentabellen
│   ├── Bedrijfsobjecten/  # bedrijfsobjectpagina's, georganiseerd per GGM-beleidsdomein
│   │   ├── 6-sociaal-domein/
│   │   │   ├── inburgering/
│   │   │   └── terug-en-invordering/
│   │   ├── 9-interne-organisatie/
│   │   │   └── financien/
│   │   ├── 99-kern/
│   │   └── {taakveld}/{beleidsdomein}/
│   ├── Bronsamenvattingen/# samenvattingen per bron, georganiseerd per domein
│   │   ├── Belastingen/
│   │   ├── Economie/
│   │   └── {domein}/
│   └── Analyses/          # query-resultaten, vergelijkingen, syntheses
└── llm-wiki.md            # Karpathy's originele ideebestand (referentie)
```

## Bronnen (Sources)

- **Immutabel** — de LLM leest bronnen maar wijzigt ze nooit.
- Bronnen zijn gemeentelijke beleidsdocumenten, VNG-publicaties, proposities, toelichtingen, verordeningen.
- Georganiseerd per gemeentelijk domein als subdirectory onder `Sources/`.
- Bronnen kunnen YAML-frontmatter bevatten (title, source, created, description, tags).
- **GGM-pagina's zijn bronnen, geen wiki.** De bestanden in `Sources/GGM/` zijn een leesbare conversie van het XMI-bestand (de bron van waarheid). Ze bevatten letterlijke definities uit het model, zonder synthese of interpretatie. De LLM leest ze als referentie bij het mappen van begrippen en bedrijfsobjecten, maar wijzigt ze niet.

### Bronnen toevoegen

Er zijn twee manieren om bronnen toe te voegen. Beide resulteren in een bestand in `Sources/{domein}/`.

#### Via URL (LLM fetcht)

Wanneer de gebruiker een URL aanwijst:

1. **Ophalen** — fetch de pagina en converteer naar markdown. Behoud de originele tekst; ruim alleen opmaakruis op (navigatie, footers, ads). Herschrijf geen inhoud.
2. **Domein bepalen** — kies de juiste subdirectory onder `Sources/`. Controleer bestaande subdirectories eerst; hergebruik als het domein past. Maak alleen een nieuwe subdirectory aan voor een echt nieuw domein.
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

Web Clipper slaat pagina's op in `Clippings/` met dezelfde frontmatter-structuur (title, source, created, etc.). Deze directory is een landingszone — clippings worden niet direct als bron gebruikt.

Wanneer de gebruiker vraagt om een clipping te verwerken, of bij een ingest die naar een clipping verwijst:

1. **Lees** het bestand in `Clippings/`.
2. **Verplaats** het naar `Sources/{domein}/{beschrijvende-slug}.md` — zelfde regels als bij URL-ophalen voor domeinkeuze en naamgeving.
3. **Frontmatter aanvullen** als velden ontbreken (description, tags).
4. Ga verder met de reguliere ingest-workflow.

### GGM-bronbestandformaat

Alle GGM-bronbestanden volgen een uniform formaat — ongeacht de omvang van het taakveld of beleidsdomein. Dit formaat bevat de informatie die nodig is om (1) te matchen op begrippen, (2) te bepalen of een entiteit een bedrijfsobject is, en (3) het bedrijfsobject te definiëren.

#### Granulariteit

- Per **beleidsdomein** als het beleidsdomein ≤ ~80 entiteiten bevat.
- Grote taakvelden (zoals Sociaal Domein) worden opgesplitst in meerdere bestanden per beleidsdomein of logische groep.

#### Frontmatter

```yaml
---
type: ggm-beleidsdomein | ggm-taakveld
naam: {naam}
taakveld: "{nr} {taakveldnaam}"
definitie: "{korte definitie}"
aantal_entiteiten: {n}
# alleen bij taakveld-niveau:
beleidsdomeinen: [{lijst}]
---
```

#### Verplichte secties per entiteitsgroep

**1. Entiteitstabel** met de volgende kolommen:

| Kolom | Verplicht | Toelichting |
|---|---|---|
| Entiteit | Ja | Naam van de entiteit |
| Definitie | Ja | Letterlijke definitie uit het GGM |
| Attributen | Ja | Alle attributen van de entiteit |
| Abstract | Ja | `Ja` als de entiteit abstract is (geen bedrijfsobject; alleen de concrete specialisaties worden BO's) |
| Herkomst | Ja | Basisregistratie of standaard waaruit de entiteit afkomstig is (BRP, BRK, BRWOZ, BAG, BGT/IMGeo, NHR, iWmo, iJw, StUF, KING, etc.) |

**2. Overervingshiërarchie** — als er abstracte entiteiten zijn, expliciet de hiërarchie noteren:

```
Overervingshiërarchie: Ouder → Kind1; Ouder → Kind2.
```

**3. Relatiediagrammen** — de belangrijkste relaties tussen entiteiten als ASCII-diagram:

```
Entiteit_A [1] ──── Entiteit_B [1..*]
    │
    ├── Entiteit_C [0..*]
    └── Entiteit_D [1]
```

Multipliciteiten noteren waar bekend. Diagram hoeft niet elke relatie te bevatten — focus op de relaties die relevant zijn voor het begrijpen van de procescontext.

**4. Observaties** — feitelijke constateringen over het model:

- Wat valt op aan de structuur of omvang?
- Welke entiteiten overspannen meerdere packages of beleidsdomeinen?
- Waar zitten mogelijke hiaten of modelleringskeuzes die de wiki-mapping beïnvloeden?

**5. Relevantie-sectie** — per relevant domeinperspectief:

- Welke entiteiten zijn relevant voor welk gemeentelijk domein (belastingen, sociaal domein, ruimtelijk, etc.)?
- Wat ontbreekt er vanuit dat domeinperspectief?
- Verwijzingen naar relevante analyse-pagina's in de wiki.

#### Waarom elk element nodig is

| Element | Nodig voor | Reden |
|---|---|---|
| Definitie | Begrip-matching | Koppelt GGM-entiteit aan beleidsbegrip |
| Attributen | BO-definitie | Bepaalt de scope en inhoud van het bedrijfsobject |
| Abstract-vlag | BO-bepaling | Abstracte entiteiten worden geen BO; hun specialisaties wel |
| Overerving | BO-bepaling | Voorkomt dubbele BO's (ouder + kind) |
| Relatiediagram | BO-relaties, procescontext | Laat zien welke BO's samenwerken in processen en functies |
| Herkomst | BO-definitie, herleidbaarheid | Vertelt welke basisregistratie de bron van waarheid is |
| Relevantie | BO-bepaling, hiaten | Signaleert wat er is en wat er ontbreekt per domein |

## Wiki-pagina's

### Paginatypen en frontmatter

Elke wiki-pagina heeft YAML-frontmatter. De velden per type:

#### Bedrijfsobject (`Wiki/Bedrijfsobjecten/`)

```yaml
---
type: bedrijfsobject
naam: {naam}
domein: [{domein(en)}]
archimate_type: {business-object | contract | product}
grondslag: {ggm-entiteit | ggm-afgeleid | procesobject | governance-object}

# GGM-velden — uit het XMI, beheerd door de GGM-community
ggm_entiteit: {naam van GGM-entiteit, leeg als niet van toepassing}
ggm_guid: {EA GUID van de GGM-entiteit, bijv. EAID_F9B2A863_...}
ggm_uml_type: {Class | Enumeration}
ggm_beleidsdomein: {GGM beleidsdomein}
ggm_taakveld: {GGM taakveld, bijv. "6 Sociaal Domein"}
ggm_diagram: [{namen van GGM-diagrammen waarop deze entiteit staat}]
ggm_diagram_ids: [{EA GUIDs van die diagrammen}]
ggm_definitie: {letterlijke GGM-definitie uit het XMI}
ggm_toelichting: {GGM-toelichting uit XMI-tag}
ggm_synoniemen: {GGM-synoniemen uit XMI-tag}
ggm_herkomst: {basisregistratie/standaard waaruit de entiteit afkomstig is}

# GEMMA-waarden zoals gevonden in het GGM XMI — referentie van eerdere import-cycli
ggm_gemma_naam: {GEMMA-naam in het GGM}
ggm_gemma_guid: {GEMMA-guid in het GGM}
ggm_gemma_definitie: {GEMMA-definitie in het GGM}
ggm_gemma_toelichting: {GEMMA-toelichting in het GGM}
ggm_gemma_synoniemen: {GEMMA-synoniemen in het GGM}
ggm_gemma_type: {GEMMA ArchiMate-type in het GGM, altijd "business-object"}
ggm_gemma_url: {GEMMA Online URL in het GGM}
ggm_gemma_bron: {GEMMA-bron in het GGM}
ggm_gemma_alternate_name: {GEMMA alternate name in het GGM}

# GEMMA-velden — beheerd door het GEMMA-team via deze wiki
gemma_definitie: {GEMMA-definitie op bedrijfsniveau, of "gelijk aan GGM" als er geen afwijking is}
bronnen: [{paden naar bronsamenvattingen die dit BO onderbouwen}]
relaties:
  - type: {associatie | compositie | generalisatie}
    bedrijfsobject: {naam van gerelateerd BO}
    richting: {van-dit-BO | naar-dit-BO | bidirectioneel}
    kardinaliteit: {bijv. "1..*"}
    beschrijving: {korte omschrijving van de relatie}
bedrijfsprocessen: [{bedrijfsprocessen die dit object gebruiken/produceren}]
bedrijfsfuncties: [{bedrijfsfuncties}]
---
```

**Drie naamvelden** — elk veld bestaat in een GGM-, GGM-GEMMA- en GEMMA-variant:

| Veld | GGM (XMI-bron) | GGM-GEMMA (referentie) | GEMMA (wiki/export) |
|---|---|---|---|
| naam | `ggm_entiteit` | `ggm_gemma_naam` | `naam` |
| definitie | `ggm_definitie` | `ggm_gemma_definitie` | `gemma_definitie` |
| toelichting | `ggm_toelichting` | `ggm_gemma_toelichting` | *(toekomstig)* |
| synoniemen | `ggm_synoniemen` | `ggm_gemma_synoniemen` | *(toekomstig)* |

Bij een nieuwe GGM-release worden de `ggm_*` velden bijgewerkt uit het nieuwe XMI en de `ggm_gemma_*` velden uit de GEMMA-tags in dat XMI. De wiki `gemma_*` velden worden alleen gewijzigd als het team besluit dat de nieuwe GGM-waarden een update rechtvaardigen.

**Status**: BO-pagina's hebben geen apart goedkeuringsmoment. Als het proces is doorlopen en de onderbouwing klopt, is het BO vastgesteld. Markeer alleen als `ter discussie` in de body wanneer een specifieke keuze (bijv. generalisatieniveau, GGM-afwijking) niet eenduidig is en teambespreking vereist.

**Grondslag** geeft aan waarop het bedrijfsobject is gebaseerd. Dit is structureel: het GGM modelleert data-objecten maar niet processen of governance (zie [[ggm-dekkingspatroon]]). Er zal daarom altijd een klasse bedrijfsobjecten zijn zonder GGM-grondslag.

| Grondslag | Betekenis | GGM-relatie | Voorbeeld |
|---|---|---|---|
| **ggm-entiteit** | 1:1 of n:1 mapping op een GGM-entiteit | Directe match; definitie en attributen uit GGM | WOZ-object, Begroting, Debiteur |
| **ggm-afgeleid** | Afleidbaar uit bestaande GGM-objecten | Geen eigen entiteit, wel berekbaar | *(toekomstig: solvabiliteitsratio als BO)* |
| **procesobject** | Artefact dat in een proces ontstaat, niet in GGM gemodelleerd | Structureel hiaat — GGM dekt processen niet | *(toekomstig: belastingaanslag, kadernota)* |
| **governance-object** | Juridisch of beleidsmatig kader dat processen aanstuurt | Structureel hiaat — GGM dekt governance niet | *(toekomstig: belastingverordening)* |

De BO-pagina is een **beslisdocument**: het onderbouwt waarom dit een bedrijfsobject is, hoe het zich verhoudt tot het GGM, en welke metadata naar het ArchiMate-model gaat.

Body bevat:
- **BO-criteria toetsing**: welke criteria zijn van toepassing, waarom is dit een BO
- **Beschrijving**: het bedrijfsobject op het niveau waarop er in de gemeente over wordt gepraat
- **GGM-bron** (bij grondslag `ggm-entiteit`): letterlijke GGM-definitie als blockquote, entiteitnaam, beleidsdomein, attributen, matchsterkte
- **BO-definitie**: alleen als de eigen definitie afwijkt van de GGM-definitie — beide opnemen zodat het verschil terugkoppelbaar is
- **Afleiding** (bij grondslag `ggm-afgeleid`): welke GGM-objecten, welke berekening/aggregatie
- **Procesbron** (bij grondslag `procesobject`): uit welk proces, welke beleidsbron beschrijft dit
- **Juridische bron** (bij grondslag `governance-object`): welke wet/verordening, welke beleidsbron
- **Relaties**: afgeleid van GGM-associaties (bij GGM-grondslag) of uit beleidsbronnen (bij overige grondslagen), vereenvoudigd naar bedrijfsniveau. Noteer de bron van elke relatie.
- **Bedrijfsprocessen**: welke processen dit object gebruiken of produceren
- **Bedrijfsfuncties**: welke functies dit object raken
- **Terugmelding GGM** (indien van toepassing): correcties, ontbrekende entiteiten, afwijkende definities

### BO-criteria

Een begrip is een bedrijfsobject als het aan de **meeste** van deze criteria voldoet:

- Heeft betekenis binnen het domein
- Is herkenbaar voor domeinexperts
- Heeft een eigen bestaan binnen het domein
- Kan in meervoud bestaan (er zijn meerdere exemplaren)
- Heeft een eigen levenscyclus
- Heeft relaties met andere concepten

**Vuistregel:** een begrip is meestal een BO als je er natuurlijk over kunt spreken als "deze ...", "die ...", "een nieuwe ...", "deze heeft kenmerken en relaties".

**Geen BO** als het slechts een eigenschap, status, activiteit, regel of classificatie van iets anders is.

### Afleidingsregels voor bedrijfsobjecten

#### Grondslag bepalen

Bepaal eerst de grondslag van het bedrijfsobject:

1. **Zoek een GGM-entiteit.** Is er een directe match → grondslag `ggm-entiteit`.
2. **Geen entiteit, wel afleidbaar?** Kan het BO berekend/geaggregeerd worden uit bestaande GGM-objecten → grondslag `ggm-afgeleid`.
3. **Geen GGM-basis, wel een proces?** Is het een artefact dat ontstaat in een gemeentelijk proces (aanslag, beschikking, nota) → grondslag `procesobject`.
4. **Geen GGM-basis, juridisch/beleidsmatig kader?** Is het een verordening, regeling of bevoegdheid die processen aanstuurt → grondslag `governance-object`.

Het ontbreken van een GGM-grondslag is voor procesobjecten en governance-objecten **structureel**, niet incidenteel — het GGM modelleert data, niet processen of governance (zie [[ggm-dekkingspatroon]]).

#### GGM-matchsterkte

Bij elke GGM-match wordt de sterkte beoordeeld:

| Matchsterkte | Betekenis | Actie |
|---|---|---|
| **exact** | GGM-entiteit en BO zijn hetzelfde concept, definitie klopt | Overnemen, definitie uit GGM |
| **sterk** | Zelfde concept, maar definitie of scope wijkt licht af | Overnemen, afwijking documenteren en terugmelden |
| **partieel** | GGM-entiteit dekt een deel van het BO, of BO is aggregatie van meerdere entiteiten | Overnemen met toelichting, overweeg terugmelding |
| **zwak** | Verwant concept maar wezenlijk andere scope of granulariteit | Relatie noteren, niet als grondslag gebruiken |

#### Mapping van GGM-entiteit naar bedrijfsobject (grondslag `ggm-entiteit`)

- Bij voorkeur 1-op-1 mapping van GGM-entiteit naar bedrijfsobject (beheerbaarheid, herkenbaarheid).
- Aggregatie toegestaan als het GGM te granulair is — noteer welke GGM-entiteiten zijn samengevoegd.
- Als een GGM-entiteit in meerdere beleidsdomeinen voorkomt: maak één bedrijfsobject met alle GGM-bronnen.

#### Generalisaties (overerving)

Bij een generalisatiehiërarchie in het GGM moet expliciet worden besloten op welk niveau het bedrijfsobject wordt gedefinieerd. De keuze hangt af van het bedrijfsperspectief, niet van het informatiemodel:

| Situatie | BO-keuze | Voorbeeld |
|---|---|---|
| Specialisaties zijn herkenbaar op bedrijfsniveau en hebben eigen processen/relaties | Elke specialisatie wordt een BO; het abstracte niveau wordt geen BO | Rechtspersoon (abstract) → NatuurlijkPersoon (BO), NietNatuurlijkPersoon (BO) |
| Specialisaties zijn uitwisselbaar op bedrijfsniveau; het onderscheid is alleen technisch | Het abstracte niveau wordt het BO; specialisaties worden geen apart BO | KadastraleOnroerendeZaak (BO) — perceel vs. appartementsrecht is voor de meeste bedrijfsprocessen niet relevant |
| Zowel het abstracte niveau als specialisaties zijn herkenbaar op bedrijfsniveau | Beide worden BO; de generalisatierelatie wordt vastgelegd | *(beoordeel per geval)* |

Beslisregel: **praat de gemeente erover als aparte dingen?** Zo ja → aparte BO's. Zo nee → één BO op het herkende niveau.

Noteer de beslissing en de motivatie in de body van het bedrijfsobject. Markeer als `⚠️ ter discussie` in de body als de keuze niet eenduidig is en teambespreking vereist.

#### Relaties tussen bedrijfsobjecten

BO-relaties worden afgeleid van GGM-associaties maar vereenvoudigd naar bedrijfsniveau:

- **Overnemen**: GGM-relaties die herkenbaar zijn in de bedrijfspraktijk worden 1-op-1 overgenomen.
- **Inkorten**: als een GGM-relatie via een tussenliggende entiteit loopt die geen BO wordt, wordt de relatie ingekort tot een directe BO-relatie. Noteer de tussenliggende GGM-entiteit.
- **Samenvoegen**: meerdere GGM-associaties tussen dezelfde entiteiten worden samengevoegd als ze op bedrijfsniveau niet onderscheidbaar zijn.
- **Weglaten**: GGM-relaties die puur technisch zijn (referentietabellen, enumeraties) worden niet als BO-relatie opgenomen.
- **Toevoegen**: als een relatie op bedrijfsniveau bestaat maar niet in het GGM is gemodelleerd, wordt deze toegevoegd als hiaat-relatie.

Elke BO-relatie vermeldt de GGM-bron (welke associatie/generalisatie) en eventuele afwijkingen.

### Blik op bronnen: objecten, relaties en generalisaties

Bij het lezen van **alle bronnen** — zowel GGM als VNG-beleidsdocumenten, proposities, verordeningen — wordt dezelfde blik gehanteerd:

1. **Objecten identificeren**: welke dingen worden benoemd die in processen worden gebruikt, geproduceerd of geregistreerd?
2. **Relaties herkennen**: welke objecten worden in samenhang genoemd? Welk object "hoort bij", "bestaat uit", of "is onderdeel van" een ander?
3. **Generalisaties expliciteren**: worden er overkoepelende termen gebruikt die meerdere specifiekere dingen omvatten? Is het overkoepelende niveau het herkende bedrijfsobject, of de specifiekere dingen, of beide?
4. **Granulariteit beoordelen**: wordt er in de bron gesproken op een grover of fijner niveau dan het GGM modelleert?

Bij GGM-bronnen levert dit de formele entiteiten, associaties en generalisaties op. Bij VNG-bronnen levert het begrippen en impliciete bedrijfsobjecten op die al dan niet matchen met het GGM — en juist de mismatches (hiaten, aggregaties, andere granulariteit) zijn waardevolle bevindingen voor de wiki.

#### GGM-terminologie

Het GGM is hiërarchisch opgebouwd: **taakvelden** (afgeleid van IV3) bevatten **beleidsdomeinen**. Gebruik de juiste terminologie:

- Taakveld = het bovenste niveau (bijv. "5 Sport, Cultuur en Recreatie", "9 Interne Organisatie")
- Beleidsdomein = het niveau daaronder (bijv. "Financien" onder taakveld 9, "Schulden" onder taakveld 6)
- Zie `Sources/GGM/structuur-ggm.md` voor het volledige overzicht met definities

De GGM-pagina's in `Sources/GGM/` zijn georganiseerd per taakveld als subfolder (bijv. `6-sociaal-domein/`). Elk taakveld met meerdere beleidsdomeinen heeft een `index.md`. Bestanden bevatten de entiteiten per beleidsdomein met letterlijke definities en attributen uit het model. Deze zijn referentie — de wiki verwijst ernaar maar wijzigt ze niet.

#### Domeinoverzicht (`Wiki/Domeinen/`)

```yaml
---
type: domein
naam: {domeinnaam}
status: {afgerond | in-behandeling | niet-gestart}
verwerkingsdatum: {datum laatste verwerking}
bronnen_count: {aantal verwerkte bronnen}
begrippen_count: {aantal geidentificeerde begrippen}
bo_count: {aantal bedrijfsobjecten}
---
```

Het domeinoverzicht is de **centrale werkpagina** per domein. Het bevat alle begrippen als tabel — geen aparte begrippenpagina's. Een domein wordt altijd afgetekend na verwerking — ook als de uitkomst 0 BO's is.

Body bevat:
- Korte beschrijving van het gemeentelijk domein
- **Begrippentabel** — het hart van de pagina:

```markdown
| Begrip | Type | Omschrijving | BO? | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|
| [[woz-object]] | object | Onroerende zaak voor WOZ-waardering | ✅ | 6/6 criteria, exact match | Woning, kantoor | ja |
| belastingaanslag | object | Individuele vaststelling belastingbedrag | ✅ | 6/6 criteria, GGM-hiaat | OZB-aanslag 2025 | nee |
| heffingsmaatstaf | object | Maatstaf voor belastingschuld | ❌ | Eigenschap van verordening | WOZ-waarde | nee |
| belastingmix | thema | Gekozen combinatie belastingen | ❌ | Beleidsmatig, geen object | — | nee |
```

  - **Begrip**: `[[link]]` naar BO-pagina als het een BO is, anders platte tekst
  - **Type**: begripstype (object/instrument/actor/doelgroep/thema/doel/waarde)
  - **Omschrijving**: identiek aan de BO-definitie als het een BO is
  - **BO?**: ✅ of ❌
  - **Reden**: korte samenvatting waarom wel/niet (volledige onderbouwing staat in de BO-pagina)
  - **Voorbeelden**: concrete instanties
  - **GGM**: ja/nee — heeft dit begrip een GGM-entiteit

- **GGM-dekkingsanalyse**: welke GGM-entiteiten zijn BO, welke niet, welke ontbreken
- **Verwerkte bronnen**: lijst met links naar bronsamenvattingen
- **Nog te verwerken bronnen**: lijst met links naar Sources/
- **Openstaande vragen of hiaten**
- **Terugmeldingen richting GGM**

#### Bronsamenvatting (`Wiki/Bronsamenvattingen/`)

```yaml
---
type: bronsamenvatting
bron: "Sources/{domein}/{bestand}.md"
titel: {titel van het document}
domein: [{domein(en)}]
datum_ingest: {datum van verwerking}
---
```

Body bevat:
- Samenvatting van de bron (max 500 woorden)
- Kernbegrippen met korte toelichting
- Relevantie voor bedrijfsarchitectuur
- Citaten die begrippen of objecten definiëren

De bronsamenvatting is het **schakelstuk** in de herleidbaarheidsketen: het verwijst naar het bronbestand (Sources/) en wordt verwezen door de BO-pagina (via `bronnen` in frontmatter).

#### Analyse (`Wiki/Analyses/`)

```yaml
---
type: analyse
titel: {titel}
datum: {datum}
aanleiding: {query of vraag die tot deze analyse leidde}
---
```

Vrij format — vergelijkingen, syntheses, mappingtabellen, bevindingen.

### Begripstypen en abstractieniveaus

Begrippen in de domeinoverzichttabel hebben twee onafhankelijke classificaties: **begripstype** (kolom "Type") en **abstractieniveau** (impliciet in de beoordeling). Samen bepalen ze of een begrip een BO-kandidaat is en of een GGM-match verwacht wordt.

#### Begripstypen (gemapt op ArchiMate)

Elk begripstype correspondeert met een ArchiMate-elementtype. Dit geeft direct de architectuurlaag aan.

| Begripstype | Omschrijving | ArchiMate-elementtype | BO-kandidaat? | GGM-match? |
|---|---|---|---|---|
| **object** | Concreet ding dat in processen wordt gebruikt/geproduceerd/geregistreerd | Business Object | Ja | Verwacht |
| **instrument** | Regeling, programma, wet, maatregel, verordening | Contract / Product | Ja | Nee (governance-hiaat GGM) |
| **actor** | Rol, organisatie, samenwerkingsverband | Business Actor / Role | Mogelijk | Deels (RSGB) |
| **doelgroep** | Groep waarop beleid of uitvoering gericht is | Business Actor (als rol) | Mogelijk | Deels (RSGB) |
| **thema** | Werkgebied dat doelen, actoren en instrumenten bundelt | Grouping | Nee | Nee |
| **doel** | Nagestreefde situatie of uitkomst | Goal / Outcome | Nee | Nee |
| **waarde** | Maatschappelijk ideaal, richtinggevend principe | Driver / Principle | Nee | Nee |

**BO-filterlogica:**
- **object** en **instrument** → BO-kandidaten (passive structure)
- **actor** en **doelgroep** → mogelijk BO (active structure)
- **thema**, **doel**, **waarde** → geen BO, wel context voor onderbouwing

**GGM-terugmeldlogica:**
- GGM-match verwacht maar afwezig → hiaat, terugmelden aan GGM
- GGM-match niet verwacht → structureel buiten GGM-scope, geen terugmelding

#### Abstractieniveaus

| Niveau | Kernvraag |
|---|---|
| **operationeel** | Wordt dit concreet gebruikt/geregistreerd in processen? |
| **beleidsmatig** | Is dit richtinggevend/strategisch? |

De twee dimensies versterken elkaar:
- `object` + `operationeel` → sterke BO-kandidaat, GGM-match verwacht
- `instrument` + `operationeel` → BO-kandidaat (governance-object), GGM-hiaat verwacht
- `object` + `beleidsmatig` → ongewone combinatie, nader bekijken
- `doel` + `beleidsmatig` → verwacht, geen BO

### Conventies voor wiki-pagina's

- **Taal**: Nederlands, tenzij het een gevestigde Engelse term betreft (ArchiMate, business object).
- **Bestandsnamen**: lowercase, woorden gescheiden door koppeltekens. Voorbeeld: `onroerende-zaak.md`, `gemeentelijk-belastinggebied.md`.
- **Cross-references**: gebruik Obsidian `[[wiki-links]]` voor alle verwijzingen tussen pagina's.
- **Citaten uit bronnen**: gebruik blockquotes (`>`) met bronvermelding.
- **Mappingtabellen**: gebruik markdown-tabellen voor begrip → GGM → dataobject → bedrijfsobject mappings.

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

Python-scripts in `tools/` voor XMI-verwerking. Worden aangeroepen door skills of handmatig.

| Tool | Functie |
|---|---|
| `parse_ggm_xmi.py` | Parse GGM XMI → JSON met entiteiten, relaties, packages, diagrammen |
| `enrich_bo_frontmatter.py` | Verrijk BO-frontmatter met GGM-velden uit geparsed XMI-JSON |
| `export_ggm_csv.py` | Genereer 5 CSV-bestanden uit geparsed XMI-JSON + wiki BO-pagina's |

## index.md format

```markdown
# Wiki Index

## Domeinen
- [[belastingen]] — Gemeentelijke belastingen, heffingen en retributies (23 begrippen, 10 BO's)
- ...

## Bedrijfsobjecten
- [[woz-object]] — Onroerende zaak voor WOZ-waardering (Domein: Belastingen)
- ...

## Bronsamenvattingen
- [[belastingtypen]] — VNG: drie typen gemeentelijke belastingen
- ...

## Analyses
- ...
```

## log.md format

```markdown
# Wiki Log

## [2026-06-17] ingest | Belastingtypen
- Bron: Sources/Belastingen/Belastingtypen.md
- Bronsamenvatting: Bronsamenvattingen/Belastingen/belastingtypen.md
- Domeinoverzicht bijgewerkt: 4 begrippen toegevoegd
- BO's aangemaakt: —
```

## Belangrijke regels

1. **Wijzig nooit bestanden in `Sources/`** — deze zijn immutabel.
2. **Alle wiki-output gaat naar `Wiki/`** — houd de scheiding strikt.
3. **Bespreek eerst, schrijf dan** — bij ingest altijd eerst de kernpunten bespreken met de gebruiker voordat pagina's worden aangemaakt.
4. **Herleidbaarheid** — elk bedrijfsobject moet traceerbaar zijn naar bronsamenvattingen via het `bronnen`-veld in de frontmatter. De keten is: Sources/ → Bronsamenvattingen/ → Bedrijfsobjecten/.
5. **Geen fantasie** — als een mapping naar het GGM onzeker is, markeer het als `ter discussie` in plaats van te gokken.
6. **Incrementeel** — update bestaande pagina's in plaats van duplicaten te maken.
7. **Update index en log** — na elke ingest of significante wijziging.
8. **Gemeentelijk perspectief** — de wiki beschrijft wat de gemeente ziet, doet en registreert in de keten. Actoren en processen buiten de gemeentelijke scope (bijv. IND-procedures, COA-interne processen) worden benoemd als context maar niet als eigen begrip of bedrijfsobject uitgewerkt.
