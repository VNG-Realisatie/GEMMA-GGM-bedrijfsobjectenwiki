---
type: bronsamenvatting
bron: "[Sources/evenementen/locatiebeleid-evenementen-2024-2030.md](locatiebeleid-evenementen-2024-2030.md)"
titel: Beleidsnota Locatiebeleid evenementen — Passende ruimte voor evenementen 2024-2030
domein:
  - evenementen
datum_ingest: 2026-06-20
---

## Samenvatting

De Beleidsnota Locatiebeleid evenementen (gemeente Utrecht, juni 2024) is het centrale beleidsdocument voor buitenevenementen in de stad. Het vervangt de Evenementennota uit 2009 en vormt een thematisch onderdeel van de Omgevingsvisie Utrecht en de Ruimtelijke Strategie Utrecht 2040.

De nota definieert **buitenevenementen** als alle activiteiten met publiek ter gelegenheid van een bijzondere gebeurtenis, besloten of openbaar. Manifestaties, betogingen en weekmarkten vallen er niet onder.

Het beleid rust op drie doelstellingen:

1. **Duidelijkheid en spreiding** — werken met locatieprofielen voor tien evenementenlocaties, met kaders voor aantal evenementendagen, omvang, duur, geluidsniveau en rustperiodes.
2. **Kwaliteit en diversiteit** — kwalitatieve verdelingssystematiek op basis van vier beoordelingscriteria: maatschappelijke waarde, pluriform aanbod, inclusiviteit en duurzaamheid.
3. **Blijvend passende ruimte** — vaste plekken voor zeven stads- en volksfeesten, verbetering bestaande locaties, onderzoek naar nieuwe locaties voor grote evenementen, en mogelijkheid van meerjarige vergunningen.

De gemeente hanteert een **reserveringskalender**: organisatoren melden hun evenement jaarlijks in augustus aan. Bij overaanmelding beoordeelt de gemeente op basis van de vier criteria. De burgemeester stelt de kalender vast. Een plek op de kalender garandeert geen vergunning.

De locatieprofielen zijn vastgelegd in de APV (Algemene Plaatselijke Verordening) en worden op termijn overgeheveld naar het Omgevingsplan.

## Kernbegrippen

- **[[Evenement]]** — buitenactiviteit met publiek, kern van het beleid. Eigen levenscyclus (aanmelding → beoordeling → reservering → vergunning → uitvoering → evaluatie).
- **[[Evenementenlocatie]]** — fysieke locatie met eigen kenmerken (omvang, functie, type ondergrond, maximale bezoekers). Tien locaties met locatieprofielen.
- **[[Evenementenvergunning]]** — vergunning die organisatoren aanvragen na plaatsing op de reserveringskalender. Combinatie van evenementenvergunning en omgevingsvergunning.
- **Locatieprofiel** — set van regels per locatie: evenementendagen, omvang, duur, geluidsnormen, rustperiodes. Governance-instrument, geen BO.
- **Reserveringskalender** — jaarlijkse kalender met toegewezen evenementen per locatie en datum. Planningsinstrument, geen BO.
- **Beoordelingscriteria** — vier criteria voor verdeling bij overaanmelding (maatschappelijke waarde, pluriform aanbod, inclusiviteit, duurzaamheid). Beleidsregels, geen BO.
- **Stads- en volksfeest** — evenementen onlosmakelijk verbonden met de stad (Koningsdag, Bevrijdingsdag, Keti Koti, Canal Pride, Sint Maarten, Sinterklaas, Dodenherdenking). Classificatie van evenement.
- **Rustperiode** — verplichte pauze tussen evenementen: 12 dagen op verharde locaties, 18 dagen op onverharde. Regel.
- **Winterbeperking** — extra herstelperiode 1 november–31 maart in parken (vanaf 2027). Regel.

## Relevantie voor bedrijfsarchitectuur

De nota beschrijft een gemeentelijk domein met duidelijke registratieobjecten: evenementen worden aangemeld, beoordeeld, vergund en gemonitord. Evenementenlocaties hebben eigen profielen en kenmerken. Het vergunningenproces is formeel vastgelegd in de APV. Dit levert drie BO-kandidaten op: [[Evenement]], [[Evenementenlocatie]] en [[Evenementenvergunning]].

Het GGM kent de entiteit `OpenbareActiviteit` (VTH, taakveld 1) met attributen `evenmentnaam`, `datumStart`, `datumEinde`, `locatieOmschrijving`, `status` — een dunne entiteit zonder relaties of diagrammen die slechts een deel van het evenementenbegrip dekt.

> "Deze Beleidsnota gaat over buitenevenementen in Utrecht. Daarmee bedoelen we alle activiteiten met publiek ter gelegenheid van een bijzondere gebeurtenis."

> "Als er meer aanmeldingen zijn dan dat er plek is, gaan we met organisatoren in gesprek om te kijken of een evenement kan verplaatsen. Als dit niet mogelijk is maakt de gemeente een inhoudelijke afweging op basis van kwaliteit en de in deze nota beschreven criteria."

> "De locatieprofielen zijn vastgesteld in de APV om de komende beleidscyclus ervaring op te doen met het werken met locatieprofielen, voor de nieuwe regelgeving definitief vast te leggen in het Omgevingsplan."
