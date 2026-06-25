Toets BO-criteria voor: $ARGUMENTS

Input: begripsnaam uit onderwerpoverzicht, GGM-entiteit, of "onderwerp X" voor alle onbeoordeelde begrippen.

## FASE A — CLASSIFICATIE

### Stap 1: Domeinbepaling

Welk gemeentelijk onderwerp hoort dit begrip bij?

1. Lees het onderwerpoverzicht en/of de GGM-entiteit(en).
2. Check: bestaat het onderwerpoverzicht al? Staat het begrip al in een ander onderwerp?
3. **Verhuisregel:** begrip verhuist als het primair in een ander onderwerp thuishoort (bijv. "horecavergunning" hoort bij horeca, niet bij vergunningen generiek).
4. Bij twijfel: vastleggen in het onderwerp waar het is gevonden, met verwijzing naar het onderwerp waar het mogelijk beter past.

### Stap 2: Begripstype bepalen

Classificeer het begrip als een van deze typen:

| Begripstype | Omschrijving | ArchiMate-elementtype | BO-kandidaat? | GGM-match verwacht? |
|---|---|---|---|---|
| **object** | Concreet ding dat in processen wordt gebruikt/geproduceerd | Business Object | Ja | Ja |
| **instrument** | Regeling, programma, wet, maatregel, verordening | Contract / Product | Ja | Nee (governance-hiaat GGM) |
| **actor** | Rol, organisatie, samenwerkingsverband | Business Actor / Role | Ja | Deels (RSGB) |
| **doelgroep** | Groep waarop beleid of uitvoering gericht is | Business Actor (als rol) | Ja | Deels (RSGB) |
| **thema** | Werkgebied dat doelen, actoren en instrumenten bundelt | Grouping | Nee | Nee |
| **doel** | Nagestreefde situatie of uitkomst | Goal / Outcome | Nee | Nee |
| **waarde** | Maatschappelijk ideaal, richtinggevend principe | Driver / Principle | Nee | Nee |

**Stop-regel:** thema / doel / waarde = geen BO-kandidaat → vastleggen in begrippentabel met BO?=❌, geen verdere beoordeling.

### Stap 3: Abstractieniveau bepalen

| Niveau | Kernvraag |
|---|---|
| **operationeel** | Wordt dit concreet gebruikt in processen? |
| **beleidsmatig** | Is dit richtinggevend/strategisch? |

Combinatieregels:

| Type × Niveau | Betekenis |
|---|---|
| object + operationeel | Sterke BO-kandidaat, GGM-match verwacht |
| object + beleidsmatig | Ongewone combinatie, nader bekijken |
| instrument + operationeel | BO-kandidaat (governance-object), GGM-hiaat verwacht |
| actor/doelgroep + operationeel | BO-kandidaat (actor-object), in GEMMA als Business Actor |

## FASE B — STRUCTUURANALYSE (vóór BO-criteria)

### Stap 4: Specialisaties en generalisaties afleiden

Twee onafhankelijke bronnen analyseren:

**a) Uit beleidsbronnen (eigenstandige analyse):**
- Welke overkoepelende termen of subtypes noemen de bronnen?
- Welke begrippen zijn specialisaties van bredere concepten?

**b) Uit GGM (generalisatierelaties):**
- Welke generalisatie-relaties bestaan er in het GGM voor dit begrip of verwante entiteiten?
- Zoek in source/GGM naar overerving, specialisaties en generalisaties

**Vergelijk a) en b):** komen ze overeen? Waar wijkt de bronnenanalyse af van het GGM? Afwijkingen zijn waardevolle bevindingen.

**Beslisregel:** praat de gemeente erover als aparte dingen?

| Situatie | BO-keuze | Body-sectie |
|---|---|---|
| Specialisaties zijn herkenbaar en hebben eigen processen/relaties | Elke specialisatie wordt een BO; abstract niveau wordt ook BO als het zelf de 6 criteria haalt | Parent-BO: `## Specialisaties` (tabel met links). Child-BO's: `generalisatie`-relatie in frontmatter |
| Specialisaties zijn uitwisselbaar; onderscheid is alleen technisch | Abstract niveau wordt het BO; specialisaties geen apart BO | `## Subtypes` (lijst met vetgedrukte namen) |
| BO's delen dezelfde structuur in een hiërarchie (bijv. gebiedsindelingen) | Elk niveau wordt een apart BO | Elk BO: `## Generalisatie` (beschrijft positie in hiërarchie) |

Noteer de beslissing en motivatie. Markeer als `⚠️ ter discussie` als de keuze niet eenduidig is.

### Stap 5: Attributen-check

Zoek in de GGM-bronpagina's of het concept als **attribuut of classificatie** voorkomt in andere entiteiten.

Als het begrip slechts een attribuut, status, of enumeratiewaarde is van een andere entiteit → **geen BO** maar een eigenschap. Vastleggen als subtype of eigenschap bij het parent-BO.

### Stap 6: Relatie-check

Bekijk of het concept in het GGM een `[0..*]` relatie heeft naar een grotere entiteit.

Afhankelijk ding zonder eigen bestaan → mogelijk deel van een groter BO, niet een zelfstandig BO.

## FASE C — BO-CRITERIA

### Stap 7: De 6 BO-criteria toetsen

Scoor elk criterium met ja/nee:

1. **Heeft betekenis binnen het onderwerp** — is dit een herkenbaar concept in het vakgebied?
2. **Is herkenbaar voor domeinexperts** — weten beleidsmedewerkers/uitvoerders wat dit is?
3. **Heeft een eigen bestaan binnen het onderwerp** — bestaat het onafhankelijk van andere objecten?
4. **Kan in meervoud bestaan** — zijn er meerdere exemplaren van?
5. **Heeft een eigen levenscyclus** — wordt het aangemaakt, gewijzigd, beëindigd?
6. **Heeft relaties met andere concepten** — relateert het aan andere BO's of concepten?

**Drempel:** meeste (5+) = BO.

**Negatieve toets:** geen BO als het slechts een eigenschap, status, activiteit, regel of classificatie van iets anders is.

### Stap 7b: Anti-patronen

**NOOIT als BO-criterium of motivatie gebruiken:**
- registreerbaar / registratieobject / "wat gemeenten registreren"
- eigendom ("eigendom ligt bij Eneco")
- systeembeheer ("gemeente registreert dit niet")
- regie ("regie, niet registratie")
- extern systeem

**De enige toets zijn de 6 criteria hierboven.** Gebruik het woord "registr*" niet in de motivatie.

### Stap 8: Hiërarchie vastleggen

Begrippen die een subtype zijn van een breder concept, die generiek zijn, of die in een ander onderwerp thuishoren: **niet weglaten** maar vastleggen als subtype bij het relevante BO. Een verwijzing naar het andere onderwerp/BO is voldoende.

Gebruik het resultaat van stap 4 om de eigenstandig afgeleide specialisaties en generalisaties hier te borgen. Kies het juiste patroon:

| Patroon | Wanneer | Vastleggen als |
|---|---|---|
| **Subtypes** | Children zijn geen apart BO (uitwisselbaar) | `## Subtypes` + `gemma_subtypes` frontmatter bij parent-BO |
| **Specialisaties** | Children zijn wél apart BO (eigen processen) | `## Specialisaties` bij parent-BO + `generalisatie`-relatie bij child-BO's |
| **Generalisatie** | BO's delen structuur in een hiërarchie | `## Generalisatie` bij elk niveau-BO |

## FASE D — DATA-OBJECT CLASSIFICATIE EN AFRONDEN

### Stap 9: Data-object classificatie

Is dit begrip een data-object? Een data-object is een zelfstandige entiteit die in een informatiesysteem wordt vastgelegd en eigen attributen heeft.

Dit is een **aparte classificatie** naast de BO-beoordeling:

| Combinatie | Voorbeeld | Gevolg |
|---|---|---|
| BO + data-object | WOZ-object, Begroting | Meest voorkomend |
| BO + geen data-object | Governance-objecten, procesobjecten | Structureel geen GGM-match verwacht |
| Subtype + data-object | Type monument (geregistreerd) | Vastleggen als subtype met GGM-link |
| Geen BO + data-object | Te granulair voor BO, wél geregistreerd | Potentieel GGM-entiteit zonder BO; vastleggen in begrippentabel |

Vastleggen in de kolom **"Data-object"** in de begrippentabel (ja/nee).

Data-objecten zonder GGM-match zijn de sterkste hiaat-kandidaten (→ stap 10).

### Stap 10: GGM-hiaatbeoordeling

Alleen bij data-objecten zonder GGM-match.

| Type begrip | GGM-scope? | Rapporteren als hiaat? |
|---|---|---|
| Data-object | In scope | Ja (potentieel hiaat) |
| Proces | Uit scope | Nee (structureel out-of-scope) |
| Governance-instrument | Uit scope | Nee (structureel out-of-scope) |

Bij potentieel hiaat, motiveer:
- Waar worden deze gegevens in de gemeente vastgelegd/beheerd?
- Welke attributen zijn relevant?
- Past het in een bestaand GGM-beleidsdomein?

Formuleer als terugmelding:
> **[Object]** — [Omschrijving als data-object] [waarom relevant] [waar zou passen in GGM]

**Conservatief: twijfel = niet rapporteren.**

### Stap 11: LLM-autonomieregels

**Zelfstandig afhandelen** wanneer ALLE drie voorwaarden waar zijn:
1. Begripstype is `object`, `actor` of `doelgroep`, en abstractieniveau is `operationeel`
2. Minstens 5 van de 6 BO-criteria zijn van toepassing
3. GGM-matchsterkte is `exact` of `sterk`

**Voorleggen aan het team** bij:
- Begripstype `instrument` (altijd)
- Minder dan 5 BO-criteria van toepassing
- GGM-matchsterkte `partieel` of `zwak`
- Generalisatiekeuzes (welk niveau wordt het BO?)
- Elke voorgestelde GGM-terugmelding

### Stap 12: Presentatie

Per begrip presenteren:
- **Criteria-score** (bijv. 5/6)
- **Voorstel:** BO / geen BO / subtype van [parent]
- **Data-object:** ja / nee
- **Argument:** 1-2 zinnen

Vragen per begrip, niet in batch.

Update de begrippentabel in het onderwerpoverzicht:
- **BO?** kolom: ✅ of ❌
- **Data-object** kolom: ja of nee
- **Reden** kolom: korte samenvatting

Bij BO → trigger `/write-bo` voor GGM-matching en pagina-aanmaak.
