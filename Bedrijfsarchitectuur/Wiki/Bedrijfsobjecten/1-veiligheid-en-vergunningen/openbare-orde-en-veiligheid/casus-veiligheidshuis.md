---
type: element
naam: Casus (Veiligheidshuis)
onderwerp: [Openbare Orde en Veiligheid]
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

bo_definitie: "Complexe persoons-, systeem- of gebiedsgerichte problematiek die door partners bij het Zorg- en Veiligheidshuis is aangedragen, geaccepteerd na screening en triage, en ketenoverstijgend behandeld via een integraal plan van aanpak."
bo_toelichting: "Homoniem-waarschuwing: \"casus\" is een generieke term die ook elders in de wiki voorkomt (bijv. sociaal domein, VTH). Deze pagina betreft specifiek de casus zoals behandeld binnen het Veiligheidshuis-netwerk — vandaar de disambiguerende naam \"Casus (Veiligheidshuis)\"."
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Actoren/zorg-en-veiligheidshuis|Zorg- en Veiligheidshuis]]"
    richting: naar-dit-BO
    kardinaliteit: "0..* → 1"
    beschrijving: "Het Veiligheidshuis behandelt de casus"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/brp/natuurlijk-persoon|Natuurlijk Persoon]]"
    richting: van-dit-BO
    kardinaliteit: "0..* → 1..*"
    beschrijving: "De persoon/personen op wie de casus betrekking heeft (persoons-, systeem- of gezinsgericht)"
bedrijfsprocessen: []
bedrijfsfuncties: [Openbare orde en veiligheid]
---

# Casus (Veiligheidshuis)

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Identificeerbaar | Ja — elke casus heeft een eigen aanleiding, betrokken persoon/systeem/gebied en dossier |
| Eigen attributen | Ja — aandragende partner, criteria complexe problematiek, betrokken partners, casusregisseur, plan van aanpak, status |
| Levenscyclus | Ja — aandragen door een partner → screening en triage tegen criteria complexe problematiek → acceptatie (of doorverwijzing naar ketenoverleg) → behandeling (casusoverleg) → integraal plan van aanpak → uitvoering en monitoring → afsluiting |
| Gemeentelijk eigendom | Deels — de gemeente voert sinds 2013 de regie op de samenwerking, maar de casusregie ligt bij de partner met de meeste expertise op de casus |
| Wettelijke grondslag | Nee — geen eigen wettelijke grondslag; berust op het Landelijk Kader Veiligheidshuizen (2013) en de eigen wettelijke bevoegdheden van de deelnemende partners |
| Registratieverplichting | Ja — casusoverleggen, afspraken en het plan van aanpak worden vastgelegd, met privacyregels (Avg/Wpg) |

Score: 5/6 criteria (geen eigen wettelijke grondslag — het Landelijk Kader is een bestuurlijk afgesproken kader, geen wet).

## Beschrijving

Een casus komt bij het [[Wiki/Actoren/zorg-en-veiligheidshuis|Zorg- en Veiligheidshuis]] terecht wanneer een partner (politie, OM, gemeente, zorgpartij) een zaak aandraagt die voldoet aan de criteria voor "complexe problematiek": er is sprake van meerdere, onderling samenhangende problemen (multiprobleem) op meer dan één leefgebied die kunnen leiden tot crimineel of overlastgevend gedrag; samenwerking tussen meerdere ketens is nodig omdat één partner het niet effectief alleen kan aanpakken; de problematiek beïnvloedt en wordt beïnvloed door het gezinssysteem of de directe sociale leefomgeving; óf er is sprake van ernstige, lokale gebiedsgebonden veiligheidsproblematiek die een ketenoverstijgende aanpak vraagt.

Instroom kan op verschillende manieren plaatsvinden: via de ZSM-afdoeningstafel bij de start van een strafrechtelijk traject, vanuit een lopend straf- of zorgtraject dat wordt opgeschaald, of preventief wanneer gezinsleden dreigen af te glijden. Elke partner selecteert eerst zelf op basis van de criteria voordat een zaak wordt ingebracht — een goede selectie is bepalend voor de effectiviteit van het Veiligheidshuis.

Binnen het Veiligheidshuis wordt onderscheid gemaakt tussen procesregie (bij het Veiligheidshuispersoneel, gericht op het faciliteren van de samenwerking) en casusregie (bij de partner met het zwaartepunt van de expertise op de specifieke casus). De casusregisseur is verantwoordelijk voor het integrale plan van aanpak: concrete, onderling afgestemde afspraken over interventies op verschillende leefgebieden, vervolgstappen en monitoring — met als uitgangspunt "één gezin, één plan, één regisseur".

## Procesbron

De casus ontstaat in het proces van complexe-problematiekbehandeling binnen het Veiligheidshuis, zoals beschreven in het Landelijk Kader Veiligheidshuizen (Ministerie van Veiligheid en Justitie, 2013). Zie [[Wiki/Bronsamenvattingen/Openbare Orde en Veiligheid/landelijk-kader-veiligheidshuizen|Landelijk Kader Veiligheidshuizen]], hoofdstuk 4 (Focus en scope) en 5.4-5.5 (sturing, regie en samenwerking).

## Relaties

| Relatie | Bedrijfsobject | Richting | Beschrijving |
|---|---|---|---|
| associatie | [[Wiki/Actoren/zorg-en-veiligheidshuis\|Zorg- en Veiligheidshuis]] | ← | Behandelt de casus |
| associatie | [[Wiki/Bedrijfsobjecten/99-kern/brp/natuurlijk-persoon\|Natuurlijk Persoon]] | → | Betrokken persoon/personen (persoons-, systeem- of gezinsgericht) |

## Bronnen
- [[Wiki/Bronsamenvattingen/Openbare Orde en Veiligheid/landelijk-kader-veiligheidshuizen]]

## Terugmelding GGM

GGM-hiaat: geen GGM-entiteit voor de casus, het casusoverleg of het plan van aanpak binnen de Veiligheidshuis-context. Geen wettelijke grondslag (bestuurlijk landelijk kader, geen wet), dus conservatief gerapporteerd — twijfelgeval tussen procesobject en governance-gedreven samenwerkingsproces.
