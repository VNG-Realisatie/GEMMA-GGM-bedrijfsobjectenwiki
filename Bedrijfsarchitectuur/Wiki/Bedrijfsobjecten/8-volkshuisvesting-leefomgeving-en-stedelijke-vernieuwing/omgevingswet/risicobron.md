---
type: bedrijfsobject
naam: Risicobron
domein: [gevaarlijke-stoffen]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Activiteit"
ggm_guid: EAID_8BE600D0_EBF4_475b_8801_F387A5D39009
ggm_uml_type: Class
ggm_beleidsdomein: "Omgevingswet"
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram: [Omgevingswet Toepasbare Regels, Omgevingswet Verzoek Activiteit op Locatie, Omgevingswet Juridische Regels (CIMOW)]
ggm_diagram_ids: [EAID_B9209AD2_0648_4482_BB24_135F27C2FECC, EAID_30B09C29_F649_4248_97FC_35A5F9331BBF, EAID_0AC65EDC_5C77_4fd6_8548_98FCF09F72D0]
ggm_definitie: "Ieder menselijk handelen waarbij, of ieder menselijk nalaten waardoor een verandering of effect in de (fysieke) leefomgeving wordt of kan worden bewerkstelligd. "
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Activiteit"
ggm_gemma_guid: "8deec5da-a06a-4159-9b20-e9f9ff24674e"
ggm_gemma_definitie: "Ieder menselijk handelen waarbij, of ieder menselijk nalaten waardoor een verandering of effect in de (fysieke) leefomgeving wordt of kan worden bewerkstelligd."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-8deec5da-a06a-4159-9b20-e9f9ff24674e"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: "Activiteit (Omgevingswet)"

ggm_duplicaat_entiteiten:
  - "EAID_A1C60F39_3074_4d1c_A37D_5F431F54DF92"

bo_definitie: "Ieder menselijk handelen waarbij, of ieder menselijk nalaten waardoor een verandering of effect in de (fysieke) leefomgeving wordt of kan worden bewerkstelligd."
bo_toelichting: ''
bedrijfsprocessen: ""
bedrijfsfuncties: ""
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Aandachtsgebied]]"
    richting: "van-dit-BO"
    kardinaliteit: "1..*"
    beschrijving: "Een risicobron heeft een of meer aandachtsgebieden (brand, explosie, gifwolk)"
  - type: associatie
    bedrijfsobject: "[[Voorschriftengebied]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Rond een risicobron kan een voorschriftengebied worden aangewezen
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

| Subtype | Omschrijving | GGM-attribuut |
|---|---|---|
| Risicovol bedrijf | Bedrijf waar met gevaarlijke stoffen wordt gewerkt | — |
| Risicovolle buisleiding | Buisleiding voor transport van gevaarlijke stoffen | — |
| Risicovolle transportroute | Weg, spoor of vaarweg waarover gevaarlijke stoffen worden vervoerd | — |

## GGM-bron

> "Ieder menselijk handelen waarbij, of ieder menselijk nalaten waardoor een verandering of effect in de (fysieke) leefomgeving wordt of kan worden bewerkstelligd."
> — GGM, Activiteit (EAID_8BE600D0), beleidsdomein Omgevingswet

**Matchsterkte: partieel.** Activiteit is een generiek Omgevingswet-concept dat alle activiteiten in de leefomgeving omvat. Een risicobron is een specifiek type activiteit — namelijk een activiteit met externe veiligheidsrisico's. De GGM-entiteit is breder; het BO is een specialisatie. Het GGM kent geen apart objecttype voor risicobronnen.

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|---|
| [[Aandachtsgebied]] | associatie | → | 1..* | Een risicobron heeft aandachtsgebieden voor brand, explosie en/of gifwolk | Beleidsnota §2.4 |
| [[Voorschriftengebied]] | associatie | → | 0..* | Rond een risicobron kan een voorschriftengebied worden aangewezen | Beleidsnota §2.4.4 |

## Bedrijfsprocessen

- **Advisering ruimtelijke ontwikkelingen** — bij elk nieuw bouwplan voert de gemeente het gesprek over omgevingsveiligheid in relatie tot nabije risicobronnen.
- **Opstellen omgevingsplan** — risicobronnen en hun aandachtsgebieden worden ruimtelijk vertaald in het omgevingsplan.


## Bronnen

- [[Wiki/Bronsamenvattingen/gevaarlijke-stoffen/beleidsnota-omgevingsveiligheid]]

## Terugmelding GGM

Het GGM kent geen specifiek objecttype voor risicobronnen. De generieke Activiteit dekt het concept partieel. Overweeg bij een toekomstige GGM-release of een specialisatie "Activiteit met externe veiligheidsrisico's" zinvol is. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
