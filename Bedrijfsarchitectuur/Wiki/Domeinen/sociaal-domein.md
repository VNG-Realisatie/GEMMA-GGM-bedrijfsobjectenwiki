---
type: domein
naam: Sociaal Domein
status: in-behandeling
verwerkingsdatum: 2026-06-21
bronnen_count: 1
begrippen_count: 17
bo_count: 1
---

# Sociaal Domein

Het sociaal domein omvat de gemeentelijke verantwoordelijkheid voor zorg, welzijn, onderwijs, sport, cultuur en maatschappelijke ondersteuning. Binnen deze wiki richt de eerste ingest zich op **maatschappelijke voorzieningen**: de fysieke plekken waar deze activiteiten plaatsvinden.

## Begrippentabel

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/maatschappelijke-voorzieningen/maatschappelijke-voorziening\|Maatschappelijke voorziening]] | object | Plek voor activiteiten met maatschappelijk doel (zorg, welzijn, cultuur, sport, onderwijs) | ✅ | ja | 6/6 criteria; overkoepelend concept met 16 subtypes | Buurtcentrum Zuilen, Sporthal Olympos | afgeleid |
| Buurtcentrum | object | Welzijnsvoorziening met minimaal drie activiteitenruimten | subtype | ja | Subtype van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/maatschappelijke-voorzieningen/maatschappelijke-voorziening\|Maatschappelijke voorziening]] | Buurthuis de Musketon | nee |
| Buurtkamer | object | Kleinschalige ontmoetingsplek (1-2 ruimten, ~200 m²) | subtype | ja | Subtype van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/maatschappelijke-voorzieningen/maatschappelijke-voorziening\|Maatschappelijke voorziening]] | — | nee |
| Jongerenhuiskamer | object | Laagdrempelige ruimte voor jongeren (~150 m²) | subtype | ja | Subtype van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/maatschappelijke-voorzieningen/maatschappelijke-voorziening\|Maatschappelijke voorziening]] | — | nee |
| Gezondheidscentrum | object | Clustering eerstelijns zorg (~800-1200 m²) | subtype | ja | Subtype van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/maatschappelijke-voorzieningen/maatschappelijke-voorziening\|Maatschappelijke voorziening]] | — | nee |
| Sporthal | object | Binnensportaccommodatie voor training en competitie | subtype | ja | Subtype van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/maatschappelijke-voorzieningen/maatschappelijke-voorziening\|Maatschappelijke voorziening]]; GGM: Binnenlocatie | Sporthal Lunetten | ja |
| Sportpark | object | Geheel van terreinen en voorzieningen voor buitensporten | subtype | ja | Subtype van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/maatschappelijke-voorzieningen/maatschappelijke-voorziening\|Maatschappelijke voorziening]]; GGM: Sportpark | Sportpark Zoudenbalch | ja |
| Zwembad | object | Overdekt of openlucht zwembad | subtype | ja | Subtype van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/maatschappelijke-voorzieningen/maatschappelijke-voorziening\|Maatschappelijke voorziening]] | De Kwakel | nee |
| Beheerde speeltuin | object | Beheerde speelvoorziening (~5000 m²) | subtype | ja | Subtype van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/maatschappelijke-voorzieningen/maatschappelijke-voorziening\|Maatschappelijke voorziening]] | — | nee |
| Speelplek | object | Formele speelruimte in openbare ruimte | subtype | ja | Subtype van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/maatschappelijke-voorzieningen/maatschappelijke-voorziening\|Maatschappelijke voorziening]] | — | nee |
| Wijkcultuurhuis | object | Laagdrempelige culturele plek op wijkniveau | subtype | ja | Subtype van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/maatschappelijke-voorzieningen/maatschappelijke-voorziening\|Maatschappelijke voorziening]] | UCK | nee |
| School | object | Gebouw voor primair of voortgezet onderwijs | subtype | ja | Subtype van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/maatschappelijke-voorzieningen/maatschappelijke-voorziening\|Maatschappelijke voorziening]]; GGM: School | Prinses Margrietschool | ja |
| Volkstuinpark | object | Groene voorziening voor tuinieren en ontmoeting | subtype | ja | Subtype van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/maatschappelijke-voorzieningen/maatschappelijke-voorziening\|Maatschappelijke voorziening]] | — | nee |
| Scoutingaccommodatie | object | Accommodatie in zelfbeheer voor jeugdactiviteiten | subtype | ja | Subtype van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/maatschappelijke-voorzieningen/maatschappelijke-voorziening\|Maatschappelijke voorziening]] | — | nee |
| Dagbestedingslocatie | object | Locatie voor activering en dagbesteding vanuit Wmo | subtype | ja | Subtype van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/maatschappelijke-voorzieningen/maatschappelijke-voorziening\|Maatschappelijke voorziening]] | — | nee |
| Gezinshuis | object | Kleinschalige woonzorgvorm voor jeugdhulp met verblijf | subtype | ja | Subtype van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/maatschappelijke-voorzieningen/maatschappelijke-voorziening\|Maatschappelijke voorziening]] | — | nee |
| Maatschappelijke opvang | object | Tijdelijke opvang met zorg voor daklozen | subtype | ja | Subtype van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/maatschappelijke-voorzieningen/maatschappelijke-voorziening\|Maatschappelijke voorziening]] | — | nee |

## GGM-entiteitendekking

Het koersdocument raakt meerdere GGM-taakvelden. De dekking per relevant beleidsdomein:

| GGM-beleidsdomein | Taakveld | Entiteiten | BO | Niet-BO | Niet beoordeeld | Reden niet beoordeeld |
|---|---|---|---|---|---|---|
| Sport | 5 | 13 | 2 (Binnenlocatie, Sportpark als subtypes) | 0 | 11 | Sportbeleid nog niet als eigen bron verwerkt |
| Onderwijs | 4 | 12 | 1 (School als subtype) | 0 | 11 | Onderwijsbeleid nog niet als eigen bron verwerkt |
| Generiek Jeugd en Wmo | 6 | 27 | 0 | 0 | 27 | Wmo/Jeugd-beleid nog niet als eigen bron verwerkt |
| Sociale Teams | 6 | 9 | 0 | 0 | 9 | Buurtteams nog niet als eigen bron verwerkt |
| Dak- en thuislozen | 6 | 1 | 0 | 0 | 1 | Opvangbeleid nog niet als eigen bron verwerkt |

### GGM-dekkingsanalyse

Het koersdocument is een overkoepelende ruimtelijke bron die alle typen voorzieningen benoemt maar geen van de specifieke beleidsdomeinen diepgaand behandelt. De GGM-dekking voor dit domein is daardoor gering:

- **Sport** (taakveld 5): Binnenlocatie en Sportpark zijn als subtype gekoppeld. De overige 11 entiteiten (Sportvereniging, Veld, Belijning, etc.) zijn niet beoordeeld — daarvoor is een sportnota nodig.
- **Onderwijs** (taakveld 4): School is als subtype gekoppeld. Leerling, Inschrijving, etc. vallen buiten scope van dit koersdocument.
- **Sociaal Domein** (taakveld 6): GGM-entiteit Voorziening (Wmo/Jeugd) is een ander concept (dienst, niet fysieke plek). De welzijns- en zorgvoorzieningen uit het koersdocument (buurtcentrum, gezondheidscentrum, etc.) ontbreken volledig in het GGM.

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/Sociaal Domein/leefbare-stad-en-maatschappelijke-voorzieningen|Leefbare stad en maatschappelijke voorzieningen]] — Gemeente Utrecht, koersdocument maart 2020

## Nog te verwerken bronnen

Geen. De 11 overige bronnen in Sources/Onderwerpen/Sociaal Domein/ waren dunne VNG-portaalpagina's zonder BO-kandidaten en zijn verplaatst naar Niet-relevant/.

Voor verdere verdieping van dit domein zijn inhoudelijke beleidsdocumenten nodig, bijvoorbeeld:
- Sportnota (voor sportaccommodaties)
- Wmo-beleidsplan (voor welzijns- en zorgvoorzieningen)
- Cultuurvisie (voor cultuurvoorzieningen)
- Onderwijsagenda (voor onderwijshuisvesting)

## Openstaande vragen

- De subtypes zijn nu allemaal onder één overkoepelend BO geplaatst. Bij verwerking van domeinspecifieke bronnen (sportnota, Wmo-beleid, cultuurvisie) kan besloten worden om subtypes te promoveren tot zelfstandige BO's.
- De relatie met [[Wijk]] is de enige vastgelegde BO-relatie. Bij verdere ingest ontstaan relaties met vastgoed, gebiedsontwikkeling, etc.

## Terugmeldingen richting GGM

Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]] #44: overkoepelend concept maatschappelijke voorziening en welzijns-/zorg-/cultuursubtypen ontbreken in het GGM.
