# assess-element

**Doel:** een begrip volledig beoordelen: classificatie, structuuranalyse, BO-criteria, data-objectclassificatie en hiaatbeoordeling.
**Aanbevolen model:** standaard
**Parameters:** {{begrip}} — begripsnaam uit een onderwerpoverzicht, een GGM-entiteit, of "onderwerp X" voor alle onbeoordeelde begrippen van dat onderwerp. Verplicht.
**Benodigde context:** [../context/regels.md](../context/regels.md), [../context/ai-richtlijnen.md](../context/ai-richtlijnen.md), het onderwerpoverzicht, `Wiki/GGM/` van het relevante taakveld, `Wiki/GEMMA/actoren-en-rollen.md`.
**Verwachte uitvoer:** per begrip een beoordeling (criteria-score, voorstel, data-object, naamconflict, argument) en een bijgewerkte begrippentabel.

## Prompt

Toets de elementcriteria voor: {{begrip}}

### FASE A — CLASSIFICATIE

**Stap 1: Domeinbepaling.** Bij welk gemeentelijk onderwerp hoort dit begrip? Lees het onderwerpoverzicht en/of de GGM-entiteit(en). Verhuisregel: een begrip verhuist als het primair in een ander onderwerp thuishoort. Bij twijfel: vastleggen waar het gevonden is, met verwijzing naar het mogelijk betere onderwerp.

**Stap 2: Begripstype bepalen.**

| Begripstype | Omschrijving | ArchiMate-type | Element-kandidaat? | GGM-match verwacht? |
|---|---|---|---|---|
| object | Concreet ding dat in processen wordt gebruikt/geproduceerd | Business Object | Ja (BO) | Ja |
| governance-instrument | Regeling, programma, wet, maatregel, verordening | Contract / Product | Ja (BO) | Nee (governance-hiaat) |
| actor | Persoon of organisatie(-eenheid) die kan handelen | Business Actor | Ja (actorpagina) | Deels (RSGB) |
| rol | Verantwoordelijkheid voor specifiek gedrag | Business Role | Ja (rolpagina) | Deels (RSGB) |
| doelgroep | Groep waarop beleid of uitvoering is gericht | Business Object (classificatie) | Ja (BO) | Deels (RSGB) |
| thema | Werkgebied dat doelen, actoren en instrumenten bundelt | Grouping | Nee | Nee |
| doel | Nagestreefde situatie of uitkomst | Goal / Outcome | Nee | Nee |
| waarde | Maatschappelijk ideaal, richtinggevend principe | Driver / Principle | Nee | Nee |

Stop-regel: thema/doel/waarde = geen kandidaat → vastleggen in de begrippentabel met BO? = ❌, geen verdere beoordeling.
Actor/rol-onderscheid: gaat het over *wie* iets doet (actor) of *in welke verantwoordelijkheid* (rol)? Een doelgroep is geen actor of rol maar een classificatie — behandel als gewoon BO.
Let op: begripstypen classificeren begrippen uit bronnen (*wat is het?*); de dekkingsanalyse gebruikt een apart systeem van entiteitstypen voor GGM-entiteiten (*waarom wel/geen BO?*).

**Stap 2b: Actor/rol-toets** (alleen bij begripstype actor of rol). Toets tegen de diagnostische vragen in `Wiki/GEMMA/actoren-en-rollen.md` (6 vragen per type; 4+ maal ja = kwalificeert, krijgt een pagina in `Wiki/Actoren/` of `Wiki/Rollen/` — ongeacht of er gegevens over worden vastgelegd). Toets daarnaast onafhankelijk de 6 BO-criteria (stap 7): slagen die ook, dan komt er óók een BO-pagina — het twee-pagina-patroon, gekoppeld via `element_tegenhangers` (zie template). Externe actoren kunnen een actor-/rolpagina krijgen; het gemeentelijk perspectief begrenst alleen de BO-scope.

**Stap 3: Abstractieniveau.** Operationeel (wordt concreet gebruikt in processen) of beleidsmatig (richtinggevend)? Combinaties: object+operationeel = sterke BO-kandidaat; governance-instrument+operationeel = BO-kandidaat met verwacht GGM-hiaat; object+beleidsmatig = ongewoon, nader bekijken.

**Stap 3b: Duplicaat/homoniem-signaal.** Check vóór de structuuranalyse of het begrip een naam deelt met een bestaand element (`Wiki/Bedrijfsobjecten/`, `Wiki/Actoren/`, `Wiki/Rollen/`) of een GGM-entiteit in een ander domein. Classificeer: duplicaat (zelfde concept → verwijs naar het bestaande BO, maak geen nieuw), homoniem (ander concept → markeer; bij vastlegging is een disambiguerende naam nodig), of geen conflict. Dit is een signaal, geen beslissing — meld het en ga door; de definitieve keuze valt bij `write-element`. Een actor/rol-pagina en BO-pagina met dezelfde naam zijn géén conflict (twee-pagina-patroon).

### FASE B — STRUCTUURANALYSE

**Stap 4: Specialisaties en generalisaties.** Analyseer twee onafhankelijke bronnen: (a) beleidsbronnen — welke overkoepelende termen en subtypes noemen ze; (b) GGM — welke generalisatierelaties bestaan er. Vergelijk; afwijkingen zijn waardevolle bevindingen. Beslisregel: *praat de gemeente erover als aparte dingen?*

| Situatie | Keuze |
|---|---|
| Specialisaties herkenbaar, eigen processen/relaties | Elke specialisatie een eigen BO; het abstracte niveau wordt óók BO als het zelf de 6 criteria haalt |
| Specialisaties uitwisselbaar, onderscheid alleen technisch | Abstract niveau wordt het BO; specialisaties als subtypes |
| BO's delen structuur in een hiërarchie | Elk niveau een eigen BO met generalisatie-sectie |

**Leg elk generalisatiegeval individueel voor aan de gebruiker** — ook als een eerder vergelijkbaar geval al is beslist. Markeer niet-eenduidige keuzes als `⚠️ ter discussie`.

**Stap 5: Attributen-check.** Komt het concept in de GGM-bronpagina's voor als attribuut of classificatie van een andere entiteit? Dan geen BO maar een eigenschap of subtype van het parent-BO.

**Stap 6: Relatie-check.** Heeft het concept in het GGM een `[0..*]`-relatie naar een grotere entiteit en geen eigen bestaan? Dan mogelijk deel van een groter BO.

### FASE C — BO-CRITERIA

**Stap 7: De 6 BO-criteria** (elk ja/nee):

1. Heeft betekenis binnen het onderwerp.
2. Is herkenbaar voor domeinexperts.
3. Heeft een eigen bestaan binnen het onderwerp.
4. Kan in meervoud bestaan.
5. Heeft een eigen levenscyclus (ontstaat, wijzigt, eindigt).
6. Heeft relaties met andere concepten.

Drempel: 5+ = BO. Negatieve toets: geen BO als het slechts een eigenschap, status, activiteit, regel of classificatie van iets anders is.

**Stap 7b: Anti-patronen.** Gebruik NOOIT als criterium of motivatie: registreerbaarheid ("wat gemeenten registreren"), eigendom, systeembeheer, regie, extern systeem. De 6 criteria zijn de enige toets; vermijd het woord "registr\*" in de motivatie.

**Stap 8: Hiërarchie borgen.** Subtypes, generieke begrippen en begrippen uit andere onderwerpen niet weglaten maar vastleggen bij het relevante BO: subtypes (children geen apart BO) / specialisaties (children wél apart BO) / generalisatie (hiërarchie van gelijkwaardige BO's) — conform stap 4.

### FASE D — DATA-OBJECT EN AFRONDEN

**Stap 9: Data-objectclassificatie** (apart van de BO-beoordeling): wordt dit begrip als zelfstandige entiteit met eigen attributen vastgelegd in een informatiesysteem? Vastleggen in de kolom "Data-object" (ja/nee). Alle combinaties komen voor; data-objecten zonder GGM-match zijn de sterkste hiaatkandidaten.

**Stap 10: GGM-hiaatbeoordeling** (alleen bij data-object zonder GGM-match). Processen en governance-instrumenten zijn structureel buiten GGM-scope — geen hiaat. Bij een potentieel hiaat, motiveer: waar worden deze gegevens vastgelegd, welke attributen zijn relevant, in welk beleidsdomein zou het passen. Formuleer als terugmelding. Conservatief: twijfel = niet rapporteren.

**Stap 11: Autonomieregels.** Zelfstandig afhandelen wanneer alle drie gelden: (1) begripstype object/actor/rol/doelgroep én operationeel; (2) 5+ van de 6 criteria; (3) matchsterkte exact of sterk. Voorleggen bij: governance-instrument (altijd), <5 criteria, matchsterkte partieel/zwak, generalisatiekeuzes, elke terugmelding.

**Stap 12: Presentatie.** Per begrip: criteria-score (bijv. 5/6), voorstel (BO / geen BO / subtype van parent), data-object ja/nee, naamconflict, argument in 1-2 zinnen. Twijfelgevallen per begrip voorleggen, niet in batch. Werk de begrippentabel bij (BO?, Data-object, Reden). Bij een goedgekeurd element: ga door met de prompt `write-element`.

## Voorbeeld

> Toets de elementcriteria voor: belastingaanslag (onderwerp belastingen)
