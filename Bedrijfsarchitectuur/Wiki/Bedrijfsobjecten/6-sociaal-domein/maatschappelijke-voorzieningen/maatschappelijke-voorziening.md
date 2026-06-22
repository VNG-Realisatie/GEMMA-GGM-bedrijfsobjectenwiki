---
type: bedrijfsobject
naam: Maatschappelijke voorziening
domein: [Sociaal Domein]
archimate_type: business-object
grondslag: ggm-afgeleid

# GGM-velden — geen directe entiteit; afgeleid van meerdere GGM-entiteiten
ggm_entiteit:
ggm_guid:
ggm_uml_type:
ggm_beleidsdomein:
ggm_taakveld:
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie:
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

# GEMMA-waarden — geen bestaande GEMMA-entry
ggm_gemma_naam:
ggm_gemma_guid:
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type:
ggm_gemma_url:
ggm_gemma_bron:
ggm_gemma_alternate_name:

# GEMMA-velden
gemma_definitie: "Plek die ruimte biedt aan activiteiten met primair een maatschappelijk doel op het gebied van zorg, welzijn, cultuur, sport of onderwijs."
gemma_subtypes:
  - naam: "Buurtcentrum"
    omschrijving: Welzijnsvoorziening met minimaal drie activiteitenruimten voor ontmoeting en bewonersactiviteiten
  - naam: "Buurtkamer"
    omschrijving: "Kleinschalige ontmoetingsplek (1-2 ruimten, ~200 m²), aanvullend op buurtcentrum"
  - naam: "Jongerenhuiskamer"
    omschrijving: "Laagdrempelige ruimte voor jongeren (~150 m²), 1 per wijk"
  - naam: "Gezondheidscentrum"
    omschrijving: "Clustering van eerstelijns zorg (~800-1200 m²)"
  - naam: "Sporthal"
    omschrijving: Binnensportaccommodatie voor training en competitie
    ggm_entiteit: Binnenlocatie
    ggm_guid: EAID_6508657D_7C3F_4261_B647_5D3B077A20F9
    ggm_attribuut: sporthal
  - naam: "Sportpark"
    omschrijving: "Geheel van terreinen, gebouwen en voorzieningen voor buitensporten"
    ggm_entiteit: Sportpark
    ggm_guid: EAID_FE1A2EF2_44FA_46fa_A583_7BAB858E17FD
    ggm_attribuut: sportpark
  - naam: "Zwembad"
    omschrijving: "Overdekt of openlucht zwembad voor leszwemmen, recreatief zwemmen en zwemsporten"
  - naam: "Beheerde speeltuin"
    omschrijving: Beheerde speelvoorziening (~5000 m²) als aanvulling op openbare speelplekken
  - naam: "Speelplek"
    omschrijving: Formele speelruimte in de openbare ruimte met speeltoestellen of sporttoestellen
  - naam: "Wijkcultuurhuis"
    omschrijving: Laagdrempelige culturele plek op wijkniveau voor kunst en cultuur
  - naam: "School"
    omschrijving: Gebouw in gebruik voor primair of voortgezet onderwijs
    ggm_entiteit: School
    ggm_guid: EAID_32DFC5DD_79D9_45d5_8F9D_7D5125961817
    ggm_attribuut: school
  - naam: "Volkstuinpark"
    omschrijving: Groene maatschappelijke voorziening voor tuinieren en ontmoeting
  - naam: "Scoutingaccommodatie"
    omschrijving: "Accommodatie in zelfbeheer voor jeugdactiviteiten (300-600 m²)"
  - naam: "Dagbestedingslocatie"
    omschrijving: Locatie voor activering en zinvolle dagbesteding vanuit de Wmo
  - naam: "Gezinshuis"
    omschrijving: "Kleinschalige woonzorgvorm voor jeugdhulp met verblijf (4-6 kamers)"
  - naam: "Maatschappelijke opvang"
    omschrijving: Tijdelijke opvang met zorg en ondersteuning voor daklozen
bronnen: [Wiki/Bronsamenvattingen/Sociaal Domein/leefbare-stad-en-maatschappelijke-voorzieningen]
relaties:
  - type: associatie
    bedrijfsobject: "[[Wijk]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: "Maatschappelijke voorzieningen zijn verspreid over wijken; spreiding en bereikbaarheid zijn beleidsuitgangspunten"
bedrijfsprocessen:
  - Gebiedsontwikkeling
  - Programmering maatschappelijke voorzieningen
  - Vastgoedbeheer
bedrijfsfuncties:
  - Maatschappelijke ontwikkeling
  - Ruimtelijke ordening
  - Vastgoedmanagement
---

## BO-criteria toetsing

| Criterium | Toepassing |
|---|---|
| 1. Betekenis in domein | ✅ Centraal begrip in gemeentelijk beleid voor leefbaarheid en gebiedsontwikkeling |
| 2. Herkenbaar voor experts | ✅ Beleidsmedewerkers, gebiedsontwikkelaars en vastgoedbeheerders werken dagelijks met dit concept |
| 3. Eigen bestaan | ✅ Een maatschappelijke voorziening is een herkenbare fysieke plek |
| 4. Meervoud | ✅ Een gemeente heeft tientallen tot honderden maatschappelijke voorzieningen |
| 5. Eigen levenscyclus | ✅ Wordt geprogrammeerd, gerealiseerd, beheerd, gerenoveerd, herbestemd of afgestoten |
| 6. Relaties | ✅ Relaties met wijk, gebiedsontwikkeling, doelgroep, vastgoedobject |

Score: 6/6.

## Beschrijving

Een maatschappelijke voorziening is een plek die ruimte biedt aan activiteiten met primair een maatschappelijk doel. Het gaat om activiteiten op het gebied van zorg, welzijn, cultuur, sport en onderwijs. De gemeente heeft hierin verschillende rollen: partner, regisseur, facilitator en eigenaar/beheerder.

Bij gebiedsontwikkeling zijn maatschappelijke voorzieningen een structurele opgave naast groen, mobiliteit, gezondheid en duurzaamheid. De gemeente hanteert zeven uitgangspunten (participatie, ontmoeting, open wijken, toegankelijkheid, slim ruimtegebruik, flexibel bouwen, thuis voor iedereen) en acht richtlijnen voor de programmering ervan.

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| Buurtcentrum | Welzijnsvoorziening met minimaal drie activiteitenruimten; normen gedifferentieerd naar wijksterkte (0,05–0,1 m² per inwoner) | — |
| Buurtkamer | Kleinschalige ontmoetingsplek (1-2 ruimten, ~200 m²), aanvullend op buurtcentrum | — |
| Jongerenhuiskamer | Laagdrempelige ruimte voor jongeren (~150 m²), 1 per wijk | — |
| Gezondheidscentrum | Clustering eerstelijns zorg (~800-1200 m²), norm: 1100 m² per 6500 inwoners | — |
| Sporthal | Binnensportaccommodatie, norm: 1 per 17.500 inwoners | [Binnenlocatie](Sources/GGM/5-sport-cultuur-en-recreatie/sport.md) → sporthal |
| Sportpark | Geheel van terreinen, gebouwen en voorzieningen voor buitensporten | [Sportpark](Sources/GGM/5-sport-cultuur-en-recreatie/sport.md) |
| Zwembad | Overdekt of openlucht zwembad | — |
| Beheerde speeltuin | Beheerde speelvoorziening (~5000 m²) | — |
| Speelplek | Formele speelruimte in openbare ruimte | — |
| Wijkcultuurhuis | Laagdrempelige culturele plek op wijkniveau, norm: 0,25 m² BVO per woning | — |
| School | Gebouw voor primair of voortgezet onderwijs, norm PO: 1 per 2000 woningen | [School](Sources/GGM/4-onderwijs/onderwijs.md) |
| Volkstuinpark | Groene voorziening voor tuinieren en ontmoeting (15 in Utrecht) | — |
| Scoutingaccommodatie | Accommodatie in zelfbeheer (300-600 m², buitenterrein 2200-3000 m²) | — |
| Dagbestedingslocatie | Locatie voor activering en dagbesteding vanuit de Wmo | — |
| Gezinshuis | Kleinschalige woonzorgvorm voor jeugdhulp met verblijf (4-6 kamers) | — |
| Maatschappelijke opvang | Tijdelijke opvang met zorg voor daklozen, transitie naar kleinschalig | — |

## Afleiding

Dit BO is afgeleid van meerdere GGM-entiteiten uit verschillende taakvelden:

- **Sportlocatie** (abstract, taakveld 5) met subtypes Binnenlocatie en Sportpark — dekt de sportvoorzieningen
- **School** (taakveld 4) — dekt onderwijshuisvesting
- **Vastgoedobject** (taakveld 9) — dekt het vastgoedaspect van gemeentelijke voorzieningen

Het GGM modelleert deze typen per taakveld apart zonder overkoepelende generalisatie. De welzijns-, zorg-, en cultuurvoorzieningen (buurtcentrum, gezondheidscentrum, wijkcultuurhuis, etc.) hebben geen GGM-entiteit.

## BO-definitie

> Plek die ruimte biedt aan activiteiten met primair een maatschappelijk doel op het gebied van zorg, welzijn, cultuur, sport of onderwijs.

Afgeleid uit de bronformulering:

> "Maatschappelijke voorzieningen zijn plekken die ruimte bieden aan activiteiten die primair een maatschappelijk doel dienen."

## Relaties

| Gerelateerd BO | Type | Richting | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wijk]] | associatie | bidirectioneel | Voorzieningen zijn verspreid over wijken; spreiding is beleidsuitgangspunt | Beleidsbron |

## Bedrijfsprocessen

- **Gebiedsontwikkeling** — programmering van voorzieningen bij nieuwe wijken
- **Vastgoedbeheer** — beheer en onderhoud van gemeentelijk maatschappelijk vastgoed
- **Programmering maatschappelijke voorzieningen** — afstemming aanbod op vraag per wijk

## Bedrijfsfuncties

- **Maatschappelijke ontwikkeling** — beleid en regie op voorzieningenniveau
- **Ruimtelijke ordening** — inpassing in omgevingsvisie en gebiedsplannen
- **Vastgoedmanagement** — eigenaar/beheerder van gemeentelijk vastgoed

## Terugmelding GGM

Het GGM mist een overkoepelend concept voor maatschappelijke voorzieningen. De welzijns-, zorg- en cultuursubtypen (buurtcentrum, buurtkamer, jongerenhuiskamer, gezondheidscentrum, wijkcultuurhuis, dagbestedingslocatie, gezinshuis, maatschappelijke opvang) hebben geen GGM-entiteit. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
