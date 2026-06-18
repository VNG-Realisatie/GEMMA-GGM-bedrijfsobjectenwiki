---
type: ggm-structuur
naam: Structuur Gemeentelijk Gegevensmodel
bron: GGM v2.5.1, Gemeente Delft
---

# Structuur Gemeentelijk Gegevensmodel

Het GGM is hiërarchisch opgebouwd in drie niveaus: **taakvelden**, **beleidsdomeinen** en **diagramgroepen**. De taakvelden zijn afgeleid van de IV3-indeling (Informatie voor Derden), de landelijke standaard voor financiële verantwoording door gemeenten. Onder elk taakveld vallen een of meer beleidsdomeinen die de inhoudelijke informatiegebieden afbakenen.

```
Taakveld (IV3-indeling)
  └── Beleidsdomein (inhoudelijk domein)
        └── Diagramgroep (thematische clustering van entiteiten)
              └── Entiteit (objecttype)
```

### Diagramgroepen

Binnen elk beleidsdomein zijn entiteiten geclusterd in **diagramgroepen**. Deze groepen komen uit de EA-diagrammen (Enterprise Architect) waarin de modelleurs de entiteiten visueel hebben georganiseerd op thema. Ze vormen het tussenniveau tussen beleidsdomein en individuele entiteit.

In de GGM-bronbestanden zijn diagramgroepen opgenomen als `###`-secties onder de `## Entiteiten`-kop. Elk beleidsdomein heeft minimaal één diagramgroep; grote beleidsdomeinen (zoals RSGBPlus met 135 entiteiten) hebben er 10–15. Entiteiten die niet op een diagram voorkomen staan in de groep "Overig".

Voorbeelden:
- **RSGBPlus**: Detaillering subjecten, Detaillering adressen/gebouwen/terreinen, Detaillering Kadastrale Onroerende Zaken, Detaillering WOZ-objecttypen, Overige geo-objecten
- **Financien**: Verwerken Mutaties, Personen, Verplichtingen en Facturen, Begroting en Budgetverantwoordelijkheid
- **Omgevingswet**: Verzoeken (IMAM), Omgevingsplan, Toepasbare Regels, Juridische Regels

## Taakvelden

| Nr | Taakveld | Definitie |
|---|---|---|
| **0** | **Bestuur, Politiek en Ondersteuning** | Domein dat gegevens bevat die worden vastgelegd bij en voortkomen uit bestuurlijke en politieke processen en  beleidsvorming en gegevens die in het kader van de gemeentelijke taak rond burgerzaklen worden vastgelegd. |
| **1** | **Veiligheid en Vergunningen** | Het informatiedomein dat gegevens omvat over het waarborgen van veiligheid, handhaving van regels en crisisbeheersing. |
| **2** | **Verkeer, Vervoer en Waterstaat** | Het informatiedomein dat gegevens omvat over infrastructuur, mobiliteit en waterbeheer ter ondersteuning van bereikbaarheid en transportefficiëntie. |
| **3** | **Economie** | Het informatiedomein dat gegevens omvat over economische ontwikkeling, bedrijvigheid en innovatie. |
| **4** | **Onderwijs** | Het informatiedomein dat gegevens omvat over onderwijsvoorzieningen, leerlingenstromen, taken in het onderwijsveld  en educatieve ondersteuning. |
| **5** | **Sport, Cultuur en Recreatie** | Het informatiedomein dat gegevens omvat over taken in het kader van erfgoed, sportieve activiteiten, culturele voorzieningen en recreatieve mogelijkheden. |
| **6** | **Sociaal Domein** | Het informatiedomein dat gegevens omvat over zorg en ondersteuning welzijn en maatschappelijke participatie ter ondersteuning van individuen of groepen. |
| **7** | **Volksgezondheid en Milieu** | Het informatiedomein dat gegevens omvat over volksgezondheid, afvalbeheer en milieubescherming. |
| **8** | **Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing** | Het informatiedomein dat gegevens omvat over huisvesting, ruimtelijke inrichting en verbetering van de leefomgeving in stedelijke of landelijke gebieden. |
| **9** | **Interne Organisatie** | Het informatiedomein dat gegevens omvat over de interne processen en ondersteunende functies die bijdragen aan het functioneren van de interne organisatie. |
| **10** | **Dienstverlening** | Het informatiedomein dat gegevens omvat over meldingen, aanvragen, baliecontacten, telefonische afhandeling en digitale interacties die faciliterend zijn voor andere domeinen. |
| **99** | **Kern** | Het informatiedomein dat de fundamentele gegevensstructuren en -definities bevat, gebaseerd op de Nederlandse basisregistraties, en dat dient als fundament voor alle overige informatiedomeinen. |

## Beleidsdomeinen per taakveld

### 0 Bestuur, Politiek en Ondersteuning

| Beleidsdomein | Definitie |
|---|---|
| **Burgerzaken** | Het informatiedomein dat gegevens omvat over de registratie en dienstverlening met betrekking tot de persoonlijke levenssfeer van inwoners, gericht op het vastleggen en verstrekken van officiële documenten en informatie. |
| **Griffie** | Het informatiedomein dat gegevens omvat over de ondersteuning van de gemeenteraad en de organisatie van raadsprocessen, gericht op het faciliteren van besluitvorming en democratische controle. |
| **Politiek** | Het informatiesubdomein dat gegevens omvat over de politieke organen van de gemeente, hun activiteiten en de ondersteuning daarvan. |

### 1 Veiligheid en Vergunningen

| Beleidsdomein | Definitie |
|---|---|
| **Model VTH** | Alle objecttypen uit het domein VTH (Vergunningverlening Toezicht en Handhaving) |

### 2 Verkeer, Vervoer en Waterstaat

| Beleidsdomein | Definitie |
|---|---|
| **Mobiliteit** | Het informatiedomein dat de structuur, definities en relaties van gegevens omvat met betrekking tot verkeer en vervoer van personen en goederen, gericht op het faciliteren van efficiënte en duurzame mobiliteit. |
| **Parkeren** | Het informatiedomein dat gegevens omvat over het stilstaan van voertuigen op een daarvoor bestemde plaats, met als doel het reguleren van parkeerruimte en het bevorderen van leefbaarheid, bereikbaarheid en mobiliteit binnen de gemeente. |

### 3 Economie

| Beleidsdomein | Definitie |
|---|---|
| **Model Economie** | Het informatiedomein dat gegevens omvat over economische ontwikkeling, bedrijvigheid en innovatie. |

### 4 Onderwijs

| Beleidsdomein | Definitie |
|---|---|
| **Leerplicht en Leerlingenvervoer** | Het informatiedomein dat gegevens omvat over de naleving van de leerplichtwet en de organisatie van leerlingenvervoer, gericht op het waarborgen van toegang tot onderwijs voor alle kinderen en jongeren. |
| **Onderwijs** | Het informatiedomein dat gegevens omvat over het funderend onderwijs, gericht op het waarborgen van toegang tot en kwaliteit van primair en voortgezet onderwijs voor kinderen en jongeren. |

### 5 Sport, Cultuur en Recreatie

| Beleidsdomein | Definitie |
|---|---|
| **Erfgoed** | *(geen definitie in GGM)* |
| — Archeologie | Het informatiedomein dat gegevens omvat over archeologische opgravingen, onderzoeken en besluitvorming, gericht op het behoud, de bescherming en de ontsluiting van archeologisch erfgoed binnen de kaders van de Erfgoedwet. |
| — Archief | Het informatiedomein dat gegevens omvat over de vorming, het beheer, de toegankelijkheid en de duurzame bewaring van archieven, inclusief documenten en collecties van cultuurhistorische waarde. |
| — Generieke Entiteiten Erfgoed | Alle generieke objecttypen die gebruikt worden door de verschillende erfgoeddomeinen |
| — Monumenten | Het informatiedomein dat gegevens omvat over de aanwijzing, bescherming en instandhouding van monumenten, inclusief gebouwen, objecten en landschappen, die van cultuurhistorische, wetenschappelijke of esthetische waarde zijn. |
| **Musea** | Het informatiedomein dat gegevens omvat over de verwerving, het beheer, het onderzoek en de presentatie van museale collecties en tentoonstellingen binnen een overheidsorganisatie. |
| **Sport** | Dit informatiedomein bevat data over collectiebeheer, tentoonstellingen, bezoekersaantallen en educatieve activiteiten van musea die onderdeel zijn van een overheidsorganisatie. Het ondersteunt de uitvoering van de museale functie conform de Erfgoedwet, inclusief het beheer van eventuele rijkscollecties. De gegevens worden gebruikt voor beleidsontwikkeling, verantwoording en publieksbereik van het cultureel erfgoed. |

### 6 Sociaal Domein

| Beleidsdomein | Definitie |
|---|---|
| **Dak- en thuislozen** | Het informatiedomein dat gegevens omvat over mensen zonder vaste woon- of verblijfplaats, gericht op het in kaart brengen van de omvang, kenmerken en ondersteuningsbehoeften van deze doelgroep. |
| **Gemeentebegrafenissen** | Het informatiedomein dat gegevens omvat over gemeentelijke uitvaarten, uitgevoerd wanneer niemand anders in de lijkbezorging voorziet, zoals vastgelegd in de Wet op de lijkbezorging. |
| **Generiek Jeugd en Wmo** | Alle generieke objecttypen die zowel voor de Wmo als voor uitvoering van de jeugdwet worden gebruikt |
| **Inburgering** | Het informatiedomein dat gegevens omvat over de uitvoering van de Wet inburgering, gericht op het ondersteunen van inburgeraars bij hun integratie en participatie in de Nederlandse samenleving. |
| **Inkomen** | Het informatiedomein dat gegevens omvat over inkomensvoorzieningen, -regelingen en financiële ondersteuning voor inwoners, gericht op het waarborgen van bestaanszekerheid en participatie in de samenleving. |
| — Diensten | Het Dienstenmodel biedt een gestructureerde weergave van de processen en objecttypen die betrokken zijn bij het leveren van diensten binnen het sociaal domein. Het model richt zich op de relaties tussen aanvragen, besluiten, rechten en voorwaarden die de basis vormen voor het verstrekken van voorzieningen. |
| — Normafwijking | Het onderdeel Normafwijking bricht zich op de registratie en afhandeling van situaties waarin een afwijking van de gestelde normen wordt geconstateerd bij inkomensvoorzieningen. |
| — Reden aanvraag | Het onderdeel Reden aanvraag richt zich op de registratie en categorisatie van redenen waarom een cliënt een inkomensvoorziening aanvraagt. Dit model biedt een overzicht van de verschillende soorten redenen en hun onderlinge relaties, waardoor gemeenten deze informatie gestructureerd kunnen vastleggen en verwerken. |
| — Terug- en invordering | Het onderdeel Terug- en Invordering richt zich op de processen en gegevens rondom het terugvorderen en invorderen van onterecht verstrekte inkomensvoorzieningen. Dit model biedt een gestructureerde weergave van de objecttypen en hun onderlinge relaties die nodig zijn om deze financiële processen effectief te beheren. |
| **Jeugd** | Het informatiedomein dat gegevens omvat over de ondersteuning, hulp en bescherming van jeugdigen en hun gezinnen, gebaseerd op de Jeugdwet. |
| **Jeugdbescherming en reclassering** | Het informatiedomein dat gegevens omvat over de uitvoering van kinderbeschermingsmaatregelen, gericht op het waarborgen van een veilige ontwikkeling van kinderen en jongeren. |
| **Schulden** | Het informatiedomein dat gegevens omvat over de ondersteuning en begeleiding van inwoners met problematische schulden, gericht op het bevorderen van financiële stabiliteit en maatschappelijke participatie. |
| — Schuldhulpverlening | Alle objecten die in het kader van schuldhulpverlening worden toegepast. Dit model is opgesteld in het kader van het programma DDAS (Data Delen Armoede en Schulden) |
| — Vroegsignalering | *(geen definitie in GGM)* |
| **Sociaal Domein Generiek** | Het domein met de generieke objecttypen die door de deeldomeinen van het sociaal domein gebruikt worden. |
| **Sociale Teams** | Het informatiedomein dat gegevens omvat over de integrale ondersteuning en hulpverlening die sociale teams bieden aan inwoners, gericht op het bevorderen van zelfredzaamheid, participatie en het oplossen van complexe problemen. |
| **Werk** | Het informatiedomein dat gegevens omvat over de ondersteuning van mensen bij het vinden en behouden van werk, gebaseerd op de Participatiewet en gericht op het bevorderen van arbeidsparticipatie. |
| **Wmo** | Het informatiedomein dat gegevens omvat over de ondersteuning en zorg die gemeenten bieden aan burgers om hun zelfredzaamheid en participatie in de maatschappij te bevorderen in het kader van de WMO, met als doel mensen zo lang mogelijk zelfstandig thuis te laten wonen. |

### 7 Volksgezondheid en Milieu

| Beleidsdomein | Definitie |
|---|---|
| **Afval** | Het informatiedomein dat gegevens bevat over de gemeentelijke taken ten aanzien van inzameling en verwerking van bedrijfs- en huishoudelijk afval |

### 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing

| Beleidsdomein | Definitie |
|---|---|
| **Beheer Openbare Ruimte** | "Het informatiedomein dat gegevens omvat over: 1. De fysieke objecten in de publieke buitenruimte, inclusief hun kenmerken, locatie en conditie. 2. De processen en activiteiten gericht op het onderhouden, inrichten en beheren van deze objecten." |
| **Bouwen en Wonen** | Het informatiedomein dat gegevens omvat over de planning, ontwikkeling en uitvoering van woningbouwprojecten, gericht op het realiseren van voldoende, betaalbare en duurzame woningen. |
| **Meldingen Openbare Ruimte** | Het informatiedomein dat gegevens omvat over meldingen van inwoners of organisaties betreffende zaken die niet in orde zijn in de openbare ruimte, gericht op het in stand houden van een schone, hele en veilige leefomgeving. |
| **Omgevingswet** | Het informatiedomein dat gegevens omvat over de uitvoering van de Omgevingswet, gericht op het integraal beheren en ontwikkelen van de fysieke leefomgeving. |

### 9 Interne Organisatie

| Beleidsdomein | Definitie |
|---|---|
| **Financien** | Het informatiesubdomein dat gegevens omvat over de financiële processen, planning en control, en het financieel beheer van de organisatie. |
| **HR** | Het informatiesubdomein dat gegevens omvat over het beheer en de ontwikkeling van personeel, gericht op het ondersteunen van de organisatie en haar medewerkers. |
| **ICT** | Het informatiesubdomein dat gegevens omvat over de informatietechnologie en communicatiesystemen die de interne processen en informatievoorziening van een organisatie ondersteunen. |
| **Inkoop** | Het informatiesubdomein dat gegevens omvat over het proces van het verwerven van goederen, diensten en werken door een organisatie. |
| **Organisatie-indeling** | Het informatiedomein dat gegevens omvat over de structuur en indeling van een organisatie, inclusief de inrichting en uitvoering van programma's en projecten. |
| **Subsidies** | Het informatiedomein dat gegevens omvat over het proces van aanvragen, beoordelen, verstrekken, beheren en verantwoorden van subsidies door de organisatie, zowel in de rol van subsidieverstrekker als subsidieontvanger. |
| **Vastgoed** | Het informatiedomein dat gegevens omvat over het beheer, onderhoud en de exploitatie van gebouwen en terreinen in eigendom van de organisatie. |

### 10 Dienstverlening

| Beleidsdomein | Definitie |
|---|---|
| **Model Dienstverlening** | Het informatiedomein dat gegevens omvat over meldingen, aanvragen, baliecontacten, telefonische afhandeling en digitale interacties die faciliterend zijn voor andere domeinen. |

### 99 Kern

| Beleidsdomein | Definitie |
|---|---|
| **BAG** | Het subdomein dat gegevens omvat over adressen en gebouwen in Nederland, gebaseerd op het Informatiemodel BAG (IMBAG), waarbij uitsluitend die elementen zijn opgenomen die relevant zijn voor gemeenten en andere lagere overheden. |
| **Dimensies** | *(geen definitie in GGM)* |
| **Generiek** | *(geen definitie in GGM)* |
| **RGBZPlus** | Het subdomein dat gegevens omvat over gemeentelijke zaakgerichtheid, gebaseerd op RGBZ 1.0, met uitbreidingen voor specifieke toepassingen zoals leges en precario. |
| **RSGBPlus** | Het subdomein dat gegevens omvat over gemeentelijke basisgegevens, gebaseerd op het Referentiemodel Stelsel van Gemeentelijke Basisgegevens (RSGB) v2.0.2, aangevuld met specifieke uitbreidingen voor lokaal gebruik en aanvullingen uit RSGB v3.0. |
