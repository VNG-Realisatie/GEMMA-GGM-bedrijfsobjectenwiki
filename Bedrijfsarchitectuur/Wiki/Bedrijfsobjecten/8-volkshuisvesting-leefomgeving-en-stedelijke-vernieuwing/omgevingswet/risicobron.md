---
type: element
naam: Risicobron
onderwerp: [gevaarlijke-stoffen]
archimate_type: "business-object"
grondslag: ggm-afgeleid

# GGM-velden — geen directe entiteit; afgeleid via generalisatie van GGM-entiteit Activiteit
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

analyse_ggm_dekking: |
  Dit BO heeft geen directe GGM-entiteit; het is een specialisatie van GGM-entiteit **Activiteit**, vastgelegd als generalisatie-relatie naar [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/activiteit|Activiteit]].
bo_definitie: "Een bedrijf, buisleiding of transportroute waar gevaarlijke stoffen worden verwerkt, opgeslagen of vervoerd."
bo_toelichting:
bedrijfsprocessen: []
bedrijfsfuncties: []
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/activiteit|Activiteit]]"
    richting: naar-dit-BO
    kardinaliteit:
    beschrijving: "Risicobron is een specialisatie van Activiteit (een activiteit met externe veiligheidsrisico's)"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/gebiedsaanwijzing|Gebiedsaanwijzing]]"
    richting: "van-dit-BO"
    kardinaliteit: "1..*"
    beschrijving: "Een risicobron heeft een of meer aandachtsgebieden (subtype van Gebiedsaanwijzing/Beperkingsgebied: brand, explosie, gifwolk)"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/gebiedsaanwijzing|Gebiedsaanwijzing]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Rond een risicobron kan een voorschriftengebied worden aangewezen (subtype van Gebiedsaanwijzing/Beperkingsgebied)"
---

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Centraal concept in het omgevingsveiligheidsbeleid |
| Is herkenbaar voor domeinexperts | ✅ | Standaardterm in de Omgevingswet en het Bkl |
| Heeft een eigen bestaan | ✅ | Fysieke locatie/installatie met eigen kenmerken |
| Kan in meervoud bestaan | ✅ | Meerdere risicobronnen per gemeente |
| Heeft een eigen levenscyclus | ✅ | Ontstaat (vestiging), wijzigt (uitbreiding), verdwijnt (sanering) |
| Heeft relaties met andere concepten | ✅ | Aandachtsgebieden, voorschriftengebieden, kwetsbare gebouwen |

## Beschrijving

Een risicobron is een bedrijf, buisleiding of transportroute waar gevaarlijke stoffen worden verwerkt, opgeslagen of vervoerd. De gemeente maakt per type risicobron beleidskeuzes over plaatsgebonden risico, groepsrisico, voorschriftengebieden en het toelaten van zeer kwetsbare gebouwen.

In Utrecht zijn de belangrijkste risicobronnen:
- **Bedrijven**: LPG-tankstations, multifuel-tankstations op bedrijventerreinen Lage Weide, Overvecht en Oudenrijn
- **Buisleidingen**: hogedruk aardgastransportleidingen (alleen aardgas, geen waterstof)
- **Transportroutes**: A2, A12, A27, A28 (weg), spoor Breukelen–Utrecht–Lunetten, Amsterdam-Rijnkanaal (water)

### Specialisaties

| Specialisatie | Omschrijving | GGM-attribuut |
|---|---|---|
| Risicovol bedrijf | Bedrijf waar met gevaarlijke stoffen wordt gewerkt | — |
| Risicovolle buisleiding | Buisleiding voor transport van gevaarlijke stoffen | — |
| Risicovolle transportroute | Weg, spoor of vaarweg waarover gevaarlijke stoffen worden vervoerd | — |

## Generalisatie

Risicobron heeft geen eigen GGM-entiteit. Het is een specialisatie van GGM-entiteit **Activiteit** (Omgevingswet) — zie [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/activiteit|Activiteit]] voor de GGM-bron en matchsterkte. Activiteit is een generiek Omgevingswet-concept dat alle activiteiten in de leefomgeving omvat; een risicobron is een specifiek type activiteit — namelijk een activiteit met externe veiligheidsrisico's. Het GGM kent geen apart objecttype voor risicobronnen.

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/gebiedsaanwijzing\|Gebiedsaanwijzing]] (subtype Aandachtsgebied) | associatie | → | 1..* | Een risicobron heeft aandachtsgebieden voor brand, explosie en/of gifwolk | Beleidsnota §2.4 |
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/gebiedsaanwijzing\|Gebiedsaanwijzing]] (subtype Voorschriftengebied) | associatie | → | 0..* | Rond een risicobron kan een voorschriftengebied worden aangewezen | Beleidsnota §2.4.4 |

## Bedrijfsprocessen

- **Advisering ruimtelijke ontwikkelingen** — bij elk nieuw bouwplan voert de gemeente het gesprek over omgevingsveiligheid in relatie tot nabije risicobronnen.
- **Opstellen omgevingsplan** — risicobronnen en hun aandachtsgebieden worden ruimtelijk vertaald in het omgevingsplan.


## Bronnen

- [[Wiki/Bronsamenvattingen/gevaarlijke-stoffen/beleidsnota-omgevingsveiligheid]]

## Terugmelding GGM

Het GGM kent geen specifiek objecttype voor risicobronnen. De generieke Activiteit dekt het concept partieel. Overweeg bij een toekomstige GGM-release of een specialisatie "Activiteit met externe veiligheidsrisico's" zinvol is. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
