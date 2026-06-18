# Gemeentelijke Bedrijfsarchitectuur Wiki

Dit is een LLM-onderhouden wiki voor het identificeren en structureren van begrippen en bedrijfsobjecten in het gemeentelijk domein. De wiki wordt incrementeel opgebouwd uit gemeentelijke beleidsdocumenten en vormt een brug tussen beleidstaal en architectuurmodellen.

## Doel

Uit gemeentelijke bronnen (beleidsdocumenten, proposities, toelichtingen) begrippen en bedrijfsobjecten extraheren en deze mappen op:

1. **Begrippen** — termen en definities zoals gebruikt in beleidsdocumenten
2. **GGM-entiteiten** — objecttypen uit het Gemeentelijk Gegevensmodel (conceptueel informatiemodel)
3. **ArchiMate dataobjecten** — vertaling van GGM-entiteiten naar ArchiMate-laag
4. **Bedrijfsobjecten** — afgeleide ArchiMate business objects op het niveau van de bedrijfsarchitectuur

## Directorystructuur

```
Bedrijfsarchitectuur/
├── CLAUDE.md              # dit bestand — schema en conventies
├── Sources/               # ruwe bronnen, NIET aanpassen
│   ├── Onderwerpen VNG/   # VNG-publicaties en beleidsdocumenten per domein
│   │   ├── Belastingen/
│   │   ├── Cultuur/
│   │   ├── Dienstverlening/
│   │   ├── Economie/
│   │   ├── Inburgering/
│   │   ├── Ondersteuning/
│   │   ├── Schuldhulpverlening/
│   │   └── {domein}/
│   ├── GGM/               # leesbare representatie van het Gemeentelijk Gegevensmodel
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
│   ├── Domeinen/          # overzichtspagina's per gemeentelijk domein
│   ├── Begrippen/         # individuele begrippenpagina's
│   ├── Bedrijfsobjecten/  # bedrijfsobjectpagina's, georganiseerd per domein
│   │   ├── Financien/
│   │   ├── Terug-en-invordering/
│   │   └── {domein}/
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

#### Begrip (`Wiki/Begrippen/`)

```yaml
---
type: begrip
naam: {begrip in lowercase}
definitie: {korte definitie}
begripstype: waarde | doel | thema | instrument | actor | doelgroep | object
abstractieniveau: normatief | strategisch | tactisch | operationeel
domein: [{domein(en)}]
synoniemen: [{alternatieve termen}]
bronnen: ["[[Sources/...]]"]  # wiki-links naar bronbestanden
ggm_entiteit: {link naar GGM-entiteit als die bestaat}
status: concept | vastgesteld | ter discussie
---
```

**Begripstype en abstractieniveau** zijn twee onafhankelijke dimensies die samen beschrijven wat voor soort begrip het is en op welk niveau het functioneert. Zie de sectie "Begripstypen en abstractieniveaus" verderop voor het volledige kader en de toelichting.

Body bevat:
- Uitgebreide definitie en toelichting
- Context: hoe het begrip in beleidsdocumenten wordt gebruikt (met citaten)
- Relaties met andere begrippen via `[[wiki-links]]`
- Afbakening: wat het begrip NIET is, verwarring met verwante termen

#### Bedrijfsobject (`Wiki/Bedrijfsobjecten/`)

```yaml
---
type: bedrijfsobject
naam: {naam}
domein: [{domein(en)}]
archimate_type: business-object
grondslag: {ggm-entiteit | ggm-afgeleid | procesobject | governance-object}
ggm_entiteit: {naam van GGM-entiteit, leeg als niet van toepassing}
ggm_beleidsdomein: {GGM beleidsdomein, leeg als niet van toepassing}
definitie: {korte definitie — bij voorkeur gelijk aan GGM als grondslag ggm-entiteit}
gerelateerde_begrippen: [{links naar begrippenpagina's}]
relaties:
  - type: {associatie | compositie | generalisatie}
    bedrijfsobject: {naam van gerelateerd BO}
    richting: {van-dit-BO | naar-dit-BO | bidirectioneel}
    kardinaliteit: {bijv. "1..*"}
    beschrijving: {korte omschrijving van de relatie}
bedrijfsprocessen: [{bedrijfsprocessen die dit object gebruiken/produceren}]
bedrijfsfuncties: [{bedrijfsfuncties}]
status: concept | vastgesteld | ter discussie
---
```

**Grondslag** geeft aan waarop het bedrijfsobject is gebaseerd. Dit is structureel: het GGM modelleert data-objecten maar niet processen of governance (zie [[ggm-dekkingspatroon]]). Er zal daarom altijd een klasse bedrijfsobjecten zijn zonder GGM-grondslag.

| Grondslag | Betekenis | GGM-relatie | Voorbeeld |
|---|---|---|---|
| **ggm-entiteit** | 1:1 of n:1 mapping op een GGM-entiteit | Directe match; definitie en attributen uit GGM | WOZ-object, Begroting, Debiteur |
| **ggm-afgeleid** | Afleidbaar uit bestaande GGM-objecten | Geen eigen entiteit, wel berekbaar | *(toekomstig: solvabiliteitsratio als BO)* |
| **procesobject** | Artefact dat in een proces ontstaat, niet in GGM gemodelleerd | Structureel hiaat — GGM dekt processen niet | *(toekomstig: belastingaanslag, kadernota)* |
| **governance-object** | Juridisch of beleidsmatig kader dat processen aanstuurt | Structureel hiaat — GGM dekt governance niet | *(toekomstig: belastingverordening)* |

Body bevat:
- Beschrijving van het bedrijfsobject op het niveau waarop er in de gemeente over wordt gepraat
- **GGM-bron** (bij grondslag `ggm-entiteit`): letterlijke GGM-definitie als blockquote, entiteitnaam, beleidsdomein, attributen
- **Bo-definitie**: alleen als de eigen definitie afwijkt van de GGM-definitie — beide opnemen zodat het verschil terugkoppelbaar is
- **Afleiding** (bij grondslag `ggm-afgeleid`): welke GGM-objecten, welke berekening/aggregatie
- **Procesbron** (bij grondslag `procesobject`): uit welk proces, welke beleidsbron beschrijft dit
- **Juridische bron** (bij grondslag `governance-object`): welke wet/verordening, welke beleidsbron
- **Relaties**: afgeleid van GGM-associaties (bij GGM-grondslag) of uit beleidsbronnen (bij overige grondslagen), vereenvoudigd naar bedrijfsniveau. Noteer de bron van elke relatie.
- **Bedrijfsprocessen**: welke processen dit object gebruiken of produceren
- **Bedrijfsfuncties**: welke functies dit object raken

### Afleidingsregels voor bedrijfsobjecten

#### Grondslag bepalen

Bepaal eerst de grondslag van het bedrijfsobject:

1. **Zoek een GGM-entiteit.** Is er een directe match → grondslag `ggm-entiteit`.
2. **Geen entiteit, wel afleidbaar?** Kan het BO berekend/geaggregeerd worden uit bestaande GGM-objecten → grondslag `ggm-afgeleid`.
3. **Geen GGM-basis, wel een proces?** Is het een artefact dat ontstaat in een gemeentelijk proces (aanslag, beschikking, nota) → grondslag `procesobject`.
4. **Geen GGM-basis, juridisch/beleidsmatig kader?** Is het een verordening, regeling of bevoegdheid die processen aanstuurt → grondslag `governance-object`.

Het ontbreken van een GGM-grondslag is voor procesobjecten en governance-objecten **structureel**, niet incidenteel — het GGM modelleert data, niet processen of governance (zie [[ggm-dekkingspatroon]]).

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

Noteer de beslissing en de motivatie in de body van het bedrijfsobject. Markeer als `status: ter discussie` als de keuze niet eenduidig is.

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
bronnen_count: {aantal verwerkte bronnen}
begrippen_count: {aantal geidentificeerde begrippen}
---
```

Body bevat:
- Overzicht van het gemeentelijk domein
- Lijst van begrippen in dit domein (links)
- Lijst van bedrijfsobjecten in dit domein (links)
- Relevante GGM-entiteiten
- Samenvatting van verwerkte bronnen
- Openstaande vragen of hiaten

#### Bronsamenvatting (`Wiki/Bronsamenvattingen/`)

```yaml
---
type: bronsamenvatting
bron: "[[Sources/...]]"  # wiki-link naar bronbestand
titel: {titel van het document}
domein: [{domein(en)}]
datum_ingest: {datum van verwerking}
begrippen_geextraheerd: [{lijst van geextraheerde begrippen}]
---
```

Body bevat:
- Samenvatting van de bron (max 500 woorden)
- Kernbegrippen met korte toelichting
- Relevantie voor bedrijfsarchitectuur
- Citaten die begrippen of objecten definiëren

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

Begrippen in de wiki hebben twee onafhankelijke dimensies: **begripstype** (wat voor soort ding het aanduidt) en **abstractieniveau** (op welk niveau het functioneert). Dit onderscheid is nodig omdat VNG-beleidsdocumenten en het GGM een fundamenteel andere taal spreken:

- **VNG-bronnen** leveren vooral begrippen op normatief, strategisch en tactisch niveau — beleidstaal.
- **GGM** levert begrippen op operationeel niveau — wat informatiesystemen vastleggen.
- **De wiki** maakt de brug zichtbaar: welke beleidsdoelen worden (niet) ondersteund door welke operationele objecten.

#### Begripstypen

| Begripstype | Omschrijving | Voorbeeld |
|---|---|---|
| **waarde** | Maatschappelijk ideaal, richtinggevend principe | brede welvaart, draagkrachtbeginsel |
| **doel** | Nagestreefde situatie of uitkomst | versterking vestigingsklimaat, optimale belastingmix |
| **thema** | Werkgebied dat doelen, actoren en instrumenten bundelt | arbeidsmarkt, ondernemersdienstverlening, kwijtschelding |
| **instrument** | Regeling, programma, wet, maatregel | belastingverordening, actieagenda mkb-dienstverlening |
| **actor** | Rol, organisatie, samenwerkingsverband | heffingsambtenaar, economische regio |
| **doelgroep** | Groep waarop beleid of uitvoering gericht is | midden- en kleinbedrijf, belastingplichtige |
| **object** | Concreet ding dat in processen wordt gebruikt, geproduceerd of geregistreerd | belastingaanslag, werklocatie, vestiging |

#### Abstractieniveaus

| Niveau | Kernvraag | Typische bron |
|---|---|---|
| **normatief** | Wat vinden we belangrijk? | Coalitieakkoord, politieke agenda |
| **strategisch** | Wat willen we bereiken? | VNG-speerpunten, beleidsplannen |
| **tactisch** | Hoe organiseren we dat? | Programma's, regelingen, samenwerkingsverbanden |
| **operationeel** | Wat doen/registreren we concreet? | Procesbeschrijvingen, informatiemodellen |

#### GGM-match: begripstype is de primaire voorspeller

De GGM-match wordt niet primair bepaald door het abstractieniveau maar door het **begripstype**. Het GGM modelleert data-objecten — de staat van informatiesystemen — niet processen, governance of beleidsinstrumenten (zie [[ggm-dekkingspatroon]]). Daardoor voorspelt het begripstype veel beter of een GGM-entiteit bestaat:

| Begripstype | GGM-match | Reden |
|---|---|---|
| **object** | Vaak | Het GGM modelleert data-objecten |
| **doelgroep** | Deels | Personen via RSGB, maar niet als rol |
| **actor** | Zelden | GGM kent geen rollen/bevoegdheden |
| **instrument** | Nee | Verordeningen, regelingen, procedures vallen buiten GGM |
| **thema** | Nee | Werkgebieden zijn geen data |
| **doel** | Nee | Verwacht — buiten GGM-scope |
| **waarde** | Nee | Verwacht — buiten GGM-scope |

Dit betekent dat ook operationele begrippen zonder GGM-match kunnen zijn als hun type geen "object" is. Drie voorbeelden op hetzelfde abstractieniveau:
- WOZ-waarde (object, operationeel) → **directe GGM-match**
- begrotingscyclus (thema, operationeel) → **geen match** — het is een proces
- heffingsambtenaar (actor, operationeel) → **geen match** — het is een rol

Het abstractieniveau bepaalt wel of een GGM-match *überhaupt verwacht kan worden*: op normatief/strategisch niveau is afwezigheid altijd logisch. Maar binnen het tactische en operationele niveau is begripstype bepalend.

#### Combinaties

Niet elke combinatie van type en niveau komt voor. De gangbare combinaties:

| | normatief | strategisch | tactisch | operationeel |
|---|---|---|---|---|
| **waarde** | x | | | |
| **doel** | | x | x | |
| **thema** | | x | x | |
| **instrument** | | | x | x |
| **actor** | | | x | x |
| **doelgroep** | | | x | x |
| **object** | | | | x |

Een begrip kan bedrijfsobject worden (wiki-paginatype `bedrijfsobject`), ongeacht het begripstype. Een doelgroep als "werkzoekende" is als begrip een doelgroep, maar kan in de architectuur een bedrijfsobject zijn.

### Conventies voor wiki-pagina's

- **Taal**: Nederlands, tenzij het een gevestigde Engelse term betreft (ArchiMate, business object).
- **Bestandsnamen**: lowercase, woorden gescheiden door koppeltekens. Voorbeeld: `onroerende-zaak.md`, `gemeentelijk-belastinggebied.md`.
- **Cross-references**: gebruik Obsidian `[[wiki-links]]` voor alle verwijzingen tussen pagina's.
- **Citaten uit bronnen**: gebruik blockquotes (`>`) met bronvermelding.
- **Mappingtabellen**: gebruik markdown-tabellen voor begrip → GGM → dataobject → bedrijfsobject mappings.

## Workflows

### 1. Ingest (bron verwerken)

Wanneer de gebruiker een nieuwe bron toevoegt of vraagt een bestaande bron te verwerken:

1. Lees de bron volledig.
2. Bespreek de kernpunten met de gebruiker — welke begrippen en objecten springen eruit?
3. Maak een bronsamenvatting aan in `Wiki/Bronsamenvattingen/`.
4. Voor elk geïdentificeerd begrip:
   - Bestaat er al een begrippenpagina? → **update** met nieuwe context en bronvermelding.
   - Nieuw begrip? → maak een nieuwe pagina in `Wiki/Begrippen/`.
5. Identificeer potentiële bedrijfsobjecten en maak of update pagina's in `Wiki/Bedrijfsobjecten/`.
6. Als GGM-mappings mogelijk zijn, raadpleeg de GGM-bronpagina's in `Sources/GGM/` en leg mappings vast in begrippen-/bedrijfsobjectpagina's of analysepagina's.
7. Update de domeinoverzichtspagina in `Wiki/Domeinen/`.
8. Update `Wiki/index.md` met nieuwe pagina's.
9. Voeg een entry toe aan `Wiki/log.md`.

### 2. Query (vraag beantwoorden)

1. Lees `Wiki/index.md` om relevante pagina's te vinden.
2. Lees de relevante wiki-pagina's.
3. Synthetiseer een antwoord met verwijzingen naar wiki-pagina's en bronnen.
4. Als het antwoord waardevolle nieuwe inzichten bevat → sla op als analysepagina in `Wiki/Analyses/`.
5. Voeg een entry toe aan `Wiki/log.md`.

### 3. Map (GGM-mapping)

Wanneer de gebruiker vraagt om begrippen/objecten te mappen op het GGM:

1. Lees de relevante begrippen- en bedrijfsobjectpagina's.
2. Raadpleeg de GGM-bronpagina's in `Sources/GGM/` voor entiteiten en definities.
4. Beschrijf de afleiding: begrip → GGM-entiteit → ArchiMate dataobject → bedrijfsobject.
5. Markeer onzekere of ontbrekende mappings met `status: ter discussie`.

### 4. Lint (wiki-onderhoud)

Periodiek of op verzoek:

- Zoek naar begrippen die in bronsamenvattingen worden genoemd maar geen eigen pagina hebben.
- Zoek naar wees-pagina's zonder inkomende links.
- Controleer of alle begrippenpagina's een `domein` hebben.
- Controleer of bedrijfsobjecten gekoppeld zijn aan ten minste één begrip.
- Signaleer tegenstrijdigheden tussen pagina's.
- Stel ontbrekende GGM-mappings voor.

## index.md format

```markdown
# Wiki Index

## Domeinen
- [[belastingen]] — Gemeentelijke belastingen, heffingen en retributies
- ...

## Begrippen
- [[onroerende-zaak]] — Object van OZB-heffing (Domein: Belastingen)
- ...

## Bedrijfsobjecten
- [[belastingaanslag]] — Aanslag opgelegd aan belastingplichtige (Domein: Belastingen)
- ...

## Bronsamenvattingen
- [[samenvatting-belastingtypen]] — VNG-artikel over de drie typen gemeentelijke belastingen
- ...

## Analyses
- ...
```

## log.md format

```markdown
# Wiki Log

## [2026-06-17] ingest | Belastingtypen
- Bron: Sources/Belastingen/Belastingtypen.md
- Begrippen geëxtraheerd: algemene belasting, bestemmingsbelasting, retributie, leges
- Pagina's aangemaakt: 4 begrippen, 1 bronsamenvatting
- Pagina's bijgewerkt: domeinoverzicht belastingen
```

## Belangrijke regels

1. **Wijzig nooit bestanden in `Sources/`** — deze zijn immutabel.
2. **Alle wiki-output gaat naar `Wiki/`** — houd de scheiding strikt.
3. **Bespreek eerst, schrijf dan** — bij ingest altijd eerst de kernpunten bespreken met de gebruiker voordat pagina's worden aangemaakt.
4. **Herleidbaarheid** — elk begrip en bedrijfsobject moet traceerbaar zijn naar ten minste één bron.
5. **Geen fantasie** — als een mapping naar het GGM onzeker is, markeer het als `ter discussie` in plaats van te gokken.
6. **Incrementeel** — update bestaande pagina's in plaats van duplicaten te maken.
7. **Update index en log** — na elke ingest of significante wijziging.
8. **Gemeentelijk perspectief** — de wiki beschrijft wat de gemeente ziet, doet en registreert in de keten. Actoren en processen buiten de gemeentelijke scope (bijv. IND-procedures, COA-interne processen) worden benoemd als context maar niet als eigen begrip of bedrijfsobject uitgewerkt.
