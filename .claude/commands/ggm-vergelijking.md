Vergelijk GGM-entiteiten met bronbegrippen voor onderwerp: $ARGUMENTS

Doel: leg voor een wiki-onderwerp de GGM-entiteiten en de in de bronnen gevonden begrippen/BO's naast elkaar in een gestructureerde vergelijking. Maak zichtbaar waar het GGM en de bronnen overeenkomen, waar ze afwijken, en wat de hiaten zijn.

## Bronnen die geraadpleegd worden

De analyse combineert drie perspectieven:

| Perspectief | Bron | Locatie | Wat het levert |
|---|---|---|---|
| **GGM** | GGM-beleidsdomeinpagina's | `Wiki/GGM/{taakveld}/{beleidsdomein}.md` | Entiteiten, definities, attributen, relaties, overervingshiërarchie |
| **Bronnen** | Onderwerpoverzicht + begrippentabel | `Wiki/Onderwerpoverzichten/{onderwerp}.md` | Begrippen, BO-beoordelingen, typeringen, GGM-matches |
| **BO's** | BO-pagina's | `Wiki/Bedrijfsobjecten/{taakveld}/{beleidsdomein}/` | Vastgelegde BO's met GGM-grondslag, matchsterkte, relaties |

## Entiteitstype-classificatie

Elke GGM-entiteit krijgt een **entiteitstype** dat beschrijft wat voor soort entiteit het is en hoe het zich verhoudt tot de BO-laag. Deze classificatie wordt in alle tabellen gebruikt.

### Detail vs. attribuut

Of iets een aparte entiteit of een attribuut is, hangt af van de **normaliseringsgraad** van het model. Het GGM is sterk genormaliseerd: wat in een minder genormaliseerd model een attribuut zou zijn (bijv. een score bij een leefgebied, een tarief bij een voorziening), is in het GGM uitgemodelleerd als aparte entiteit met eigen attributen en relaties. Conceptueel is er geen verschil — een `Tarief` is een detailgegeven van een `Voorziening`, ongeacht of het als attribuut of als entiteit is gemodelleerd. Het entiteitstype **detail** vangt beide situaties: het is een gegeven dat conceptueel bij een grotere entiteit hoort en geen zelfstandig bestaansrecht heeft op BO-niveau.

### Entiteitstypen

| Entiteitstype | Omschrijving | Voorbeeld |
|---|---|---|
| **classificatie** | Typering/soort van een andere entiteit; geen eigen bestaansrecht | Voorzieningsoort, Beschikkingsoort, Leveringsvorm |
| **detail** | *Beschrijft* of *meet* iets aan een grotere entiteit. Zou in een minder genormaliseerd model een attribuut zijn. Zonder het parent-object geen betekenis — "welk tarief?" is geen zinnige vraag zonder voorziening | Score, Beperkingscore, Tarief, Budgetuitputting |
| **component** | *Maakt deel uit van* een groter BO. Herkenbaar als eigen ding maar bestaat niet los van het parent. Zou ook in een platter model een aparte regel of deelrecord blijven | Declaratieregel, Melding Eigen bijdrage, Beschikte Voorziening |
| **proces** | Proces of processtap; beschrijft een activiteit of handeling, geen object. In de toelichting aangeven of het een heel proces is of een stap daarin | Caseaanmelding (processtap), Informering (processtap) |
| **actor** | Organisatie, afdeling of samenwerkingsverband (ArchiMate: Business Actor) | Team |
| **rol** | Functie of verantwoordelijkheid die een actor vervult (ArchiMate: Business Role) | Clientbegeleider |
| **meetinstrument** | Beoordelings- of meetinstrument; niet te verwarren met assess-bo's begripstype governance-instrument (regeling, verordening) | Zelfredzaamheidmatrix |
| **cross-cutting** | Concept dat in een ander domein/onderwerp al als BO is afgedekt | AOMMeldingWmoJeugd → generiek Aanvraag of Melding |
| **homoniem** | GGM-entiteit en BO delen dezelfde naam maar verschillen in scope of betekenis; BO is hernoemd ter disambiguatie | Declaratie (GGM) → Zorgdeclaratie (BO, vanwege HR-declaratie) |
| **synoniem** | GGM-entiteit en bronbegrip gebruiken verschillende namen voor hetzelfde concept | — |

**Entiteitstype vs. begripstype:** dit zijn entiteitstypen — ze classificeren GGM-entiteiten (*waarom is dit wel/geen BO?*). De `/assess-bo` skill gebruikt een apart classificatiesysteem, begripstypen, dat begrippen uit bronnen classificeert (*wat is het?*). Beide systemen gebruiken "actor" en "rol", maar de populatie is anders: assess-bo classificeert bronbegrippen, deze skill classificeert GGM-entiteiten.

**Deze lijst is niet uitputtend.** Als bij een analyse een GGM-entiteit niet in een bestaand entiteitstype past, leg dan een voorstel voor uitbreiding van de typelijst voor aan de gebruiker voordat je verdergaat.

## Uitvoering

### Stap 1: Scope bepalen

1. Lees het onderwerpoverzicht (`Wiki/Onderwerpoverzichten/{onderwerp}.md`).
2. Bepaal welke GGM-beleidsdomeinen dit onderwerp raakt:
   - Kijk naar de `GGM`-kolom in de begrippentabel — welke GGM-entiteiten worden genoemd?
   - Kijk naar de BO-pagina's — in welke `{taakveld}/{beleidsdomein}/` staan ze?
   - Kijk naar de bronsamenvattingen — welke GGM-domeinen raken ze inhoudelijk?
3. Lees alle relevante GGM-beleidsdomeinpagina's.
4. Lees alle BO-pagina's in de relevante beleidsdomeinen.
5. Noteer de scope: welke beleidsdomeinen, hoeveel GGM-entiteiten, hoeveel bronbegrippen.

### Stap 2: Matchen

Per GGM-entiteit in de relevante beleidsdomeinen:

1. Zoek in de begrippentabel of deze entiteit voorkomt (naam of synoniem).
2. Zoek in de BO-pagina's of er een BO met `ggm_entiteit` match bestaat.
3. Classificeer het entiteitstype (zie entiteitstype-classificatie hierboven).
4. **Dekking bepalen** (alleen voor detail, component, classificatie): volg de GGM-relaties omhoog tot je een BO bereikt. Noteer de keten als leesbare relatiebeschrijving (bijv. "onderdeel van X, dat beschrijft [[BO]]"). Als er geen BO bereikt wordt, markeer als **BO-hiaat** — een concept dat BO zou moeten zijn maar waarvoor nog geen onderbouwing uit bronnen is.

Per begrip in de begrippentabel dat BO is (✅):

1. Zoek of er een GGM-entiteit voor bestaat.
2. Classificeer:

| Situatie | Criterium |
|---|---|
| **GGM-match** | BO heeft een gematchte GGM-entiteit |
| **GGM-hiaat** | BO bestaat maar GGM heeft geen entiteit (terugmelding) |

### Stap 3: Analyse-pagina genereren

Maak de analyse-pagina aan als `Wiki/Analyses/ggm-vergelijking/ggm-vergelijking-{onderwerp}.md` met dit format:

```yaml
---
type: analyse
titel: "GGM-vergelijking {Onderwerp}"
datum: {datum}
aanleiding: "Vergelijking GGM-entiteiten met bronbegrippen voor {onderwerp}"
scope_beleidsdomeinen:
  - {beleidsdomein 1}
  - {beleidsdomein 2}
ggm_entiteiten_count: {aantal}
bronbegrippen_count: {aantal}
bo_count: {aantal}
hiaten_count: {aantal}
---
```

#### Body-structuur

**Inleiding**: Eén alinea die de scope beschrijft (welke beleidsdomeinen, bronnen, en de herleidbaarheidsketen).

**Tabel 1: GGM-entiteiten met match in de bronnen**

| GGM-entiteit | GGM-beleidsdomein | Bronbegrip / BO | Entiteitstype | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/.../{entiteit}\|{naam}]] | {beleidsdomein} | [[Wiki/Bedrijfsobjecten/.../{bo}\|{BO-naam}]] ✅ BO | — | {1-regel toelichting} |
| [[Wiki/GGM/.../{entiteit}\|{naam}]] | {beleidsdomein} | [[Wiki/Bedrijfsobjecten/.../{bo}\|{BO-naam}]] ✅ BO | homoniem | {hernoemd vanwege naamconflict} |
| [[Wiki/GGM/.../{entiteit}\|{naam}]] | {beleidsdomein} | {begrip} ❌ | component | {onderdeel van [[BO]]} |

- GGM-entiteiten linken naar hun GGM-domeinpagina: `[[Wiki/GGM/{taakveld}/{beleidsdomein}\|{entiteitnaam}]]`
- BO's linken naar hun BO-pagina: `[[Wiki/Bedrijfsobjecten/{taakveld}/{beleidsdomein}/{bo}\|{BO-naam}]]`
- Entiteitstype is `—` bij een rechttoe-rechtaan match; bij niet-BO's of bijzondere matches: het entiteitstype uit de classificatie
- Sorteer op GGM-beleidsdomein, dan op naam

**Tabel 2: GGM-entiteiten zonder match in de bronnen**

| GGM-entiteit | GGM-beleidsdomein | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/{taakveld}/{beleidsdomein}\|{naam}]] | {beleidsdomein} | {entiteitstype} | {dekkingsketen} | {1-regel waarom geen BO} |

Dekkingswaarden — leesbare relatiebeschrijvingen:
- `beschrijft [[BO]]` of `item van [[BO]]` — direct parent is een BO
- `onderdeel van X, dat beschrijft [[BO]]` — via tussenentiteit(en) naar BO
- `⚠️ BO-hiaat: {concept}` — geen parent-BO bereikbaar; benoem het ontbrekende concept
- `n.v.t.` — voor rollen, actoren, processen, meetinstrumenten

Sorteer op GGM-beleidsdomein, dan op entiteitstype, dan op naam.

**Tabel 3: Bronbegrippen zonder GGM-equivalent (hiaten)**

| Begrip uit bronnen | BO-status | Grondslag | GGM-hiaat? |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/.../{bo}\|{naam}]] | ✅ BO | {wettelijke grondslag} | **Ja** — {wat ontbreekt in GGM} |

Alleen begrippen die BO zijn én geen GGM-match hebben.

**Beoordeling**: Vrije tekst met:
- Samenvatting van de dekking (X van Y BO's hebben GGM-match)
- Structurele patronen (welke typen entiteiten worden geen BO en waarom)
- Analyse van de hiaten (hoe ernstig, is het een lacune of een modelleerkeuze)
- **BO-hiaten**: welke concepten ontbreken als BO om de dekking van alle detail/component-entiteiten compleet te maken. Per BO-hiaat: suggesties voor bronnen (type document, vindplaats) die het concept kunnen onderbouwen tot begrip of BO
- Naamverschillen en hun motivatie (homoniemen, synoniemen)
- Bewuste abstractiekeuzes (bijv. domeinspecifiek → generiek)

### Stap 4: Cross-check en afronden

1. **Verificatie**: tel de aantallen in de tabellen en vergelijk met frontmatter-counts.
2. **Consistentie**: check of elke BO uit het onderwerpoverzicht in precies één tabel voorkomt.
3. **Hiaten**: check of alle terugmeldingen uit het onderwerpoverzicht terug te vinden zijn in tabel 3.
4. Update `Wiki/index.md` met de nieuwe analyse-pagina.
5. Voeg entry toe aan `Wiki/log.md`.

### Stap 5: Totaaloverzicht bijwerken

Update `Wiki/Analyses/ggm-vergelijkingen.md` — het centrale overzicht van alle GGM-vergelijkingen.

De tabel bevat een regel per onderwerp uit `Wiki/Onderwerpoverzichten/`. Onderwerpen waarvoor nog geen vergelijking is gedraaid staan met lege waarden als signaal.

| Onderwerp | Vergelijking | GGM-entiteiten | BO's | Entiteit-hiaten | BO-hiaten | Structurele dekking | Functionele dekking |
|---|---|---|---|---|---|---|---|

Kolommen:
- **Onderwerp**: link naar het onderwerpoverzicht
- **Vergelijking**: link naar de analyse-pagina, leeg als niet gedraaid
- **GGM-entiteiten**: aantal GGM-entiteiten in scope
- **BO's**: aantal BO's
- **Entiteit-hiaten**: aantal BO's zonder GGM-entiteit (tabel 3)
- **BO-hiaten**: aantal ontbrekende parent-BO's voor detail/component-entiteiten (uit dekking-kolom tabel 2)
- **Structurele dekking**: hebben alle detail/component-entiteiten een parent-BO? Bijv. "compleet" of "incompleet (1 BO-hiaat: Grootboek)"
- **Functionele dekking**: dekt het GGM het domein inhoudelijk? Bijv. "compleet" of "incompleet — balans/verantwoording ontbreekt"

## Relatie met andere skills

| Skill | Relatie |
|---|---|
| `/coverage` | Coverage telt per beleidsdomein; deze skill vergelijkt per wiki-onderwerp |
| `/bo-coverage` | Bo-coverage beoordeelt structureel per entiteit; deze skill toont de match met bronnen |
| `/assess-bo` | Assess-bo levert de BO-beoordelingen; deze skill visualiseert het resultaat |
| `/domain-status` | Domain-status rapporteert voortgang; deze skill analyseert de GGM-aansluiting |
| `/ingest` | Ingest genereert de input (begrippentabel, BO's); deze skill maakt de vergelijking achteraf |
