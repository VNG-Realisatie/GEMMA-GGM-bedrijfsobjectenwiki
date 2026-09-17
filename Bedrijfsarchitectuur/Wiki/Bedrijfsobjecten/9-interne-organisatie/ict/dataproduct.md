---
type: element
naam: Dataproduct
onderwerp: [Informatiesamenleving]
archimate_type: business-object
grondslag: procesobject

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

ggm_gemma_naam:
ggm_gemma_guid:
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type:
ggm_gemma_url:
ggm_gemma_bron:
ggm_gemma_alternate_name:

ggm_duplicaat_entiteiten: []

bo_definitie: "Concreet resultaat van datagedreven werken — een dashboard, rapportage of analyse die inzicht geeft voor beleid of sturing."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie|Applicatie]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Dataproduct put gegevens uit applicaties (databronnen)"
bedrijfsprocessen: [Datagedreven werken, Beleidsondersteuning, Managementinformatie]
bedrijfsfuncties: [Informatievoorziening, Beleid en Strategie]
---

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Betekenis | Concreet resultaat van datagedreven werken: dashboard, rapportage, analyse |
| Herkenbaarheid | Beleidsmedewerkers kennen "het armoede-dashboard", "de wijkmonitor", "de GMSD" |
| Eigen bestaan | Heeft eigen naam, eigenaar, doel, databronnen, publicatiekanaal |
| Meervoud | Gemeente heeft tientallen dashboards, rapportages en analyses |
| Levenscyclus | Ontwerpen → bouwen → publiceren → onderhouden → uitfaseren |
| Relaties | Applicatie (databron), beleidsdomein (opgave), dataset |

Resultaat: 6/6 — BO.

## Beschrijving

Een dataproduct is een concreet resultaat van datagedreven werken: een dashboard, rapportage, analyse of datavisualisatie die inzicht geeft voor beleid, sturing of verantwoording. Gemeenten produceren tientallen dataproducten, van de Gemeentelijke Monitor Sociaal Domein (GMSD) en armoedekaarten tot verkeersdashboards en begrotingsrapportages.

Een dataproduct heeft een eigenaar (opdrachtgever vanuit de lijn), één of meer databronnen (applicaties, basisregistraties, externe datasets), en een publicatiekanaal (intern dashboard, dataportaal, open data). Het Datalab of BI-team bouwt en onderhoudt dataproducten op basis van opgavegerichte vragen.

De datastrategie beschrijft de kaders waarbinnen dataproducten worden ontwikkeld: opgavegericht (vanuit de vraag, niet het aanbod), ethisch (publieke waarden, AVG) en kwalitatief (actuele en authentieke gegevens uit basisregistraties).

## Procesbron

Dataproducten ontstaan in het proces van datagedreven werken. Nunspeet beschrijft het Datalab als aanspreekpunt voor vragen, ideeën en verzoeken, en het bouwen van nieuwe dataproducten.

Zie [[Wiki/Bronsamenvattingen/Informatiesamenleving/informatiebeleidsplan-nunspeet|Informatiebeleidsplan 2024-2028 Gemeente Nunspeet]] voor de concrete beschrijving van opgavegericht datagedreven werken.

## Subtypes

Herkende specialisaties van Dataproduct. Gevonden in bronnen. Geen apart BO.

- **Dashboard** — interactieve visualisatie voor monitoring en sturing (bijv. armoede-dashboard, verkeersdashboard)
- **Rapportage** — periodiek document met analyse en conclusies (bijv. begrotingsrapportage, sociaal domein monitor)
- **Datavisualisatie** — kaart of grafiek voor inzicht in ruimtelijke of kwantitatieve data (bijv. armoedekaart, wijkprofiel)
- **Open dataset** — publiek beschikbaar gemaakte dataset via dataportaal of data.overheid.nl

## Relaties

| Relatie | Richting | Beschrijving |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | naar-dit-BO | Dataproduct put gegevens uit applicaties (databronnen) |

## Bedrijfsprocessen

- **Datagedreven werken** — ontwerpen en bouwen van dataproducten in het Datalab
- **Beleidsondersteuning** — inzicht voor beleidsvorming en -evaluatie
- **Managementinformatie** — dashboards voor sturing en verantwoording

## Bedrijfsfuncties

- **Informatievoorziening** — datastrategie en datamanagement
- **Beleid en Strategie** — opgavegericht gebruik van dataproducten

## Bronnen

- [[Wiki/Bronsamenvattingen/Informatiesamenleving/informatiebeleidsplan-nunspeet]]
- [[Wiki/Bronsamenvattingen/Informatiesamenleving/beleid-informatie-ict-bel-combinatie]]

## Terugmelding GGM

Dataproduct ontbreekt als entiteit in het GGM. Het GGM ICT-domein modelleert applicaties, databases en gegevens, maar niet de producten die uit data worden afgeleid. Zou passen in beleidsdomein ICT als sibling van Applicatie, of in een nieuw beleidsdomein Data/BI.

Teruggemeld als #83 in [[Wiki/Analyses/ggm-terugmeldingen]].
