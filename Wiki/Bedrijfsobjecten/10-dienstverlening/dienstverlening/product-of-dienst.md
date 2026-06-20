---
type: bedrijfsobject
naam: Product of dienst
domein: [Dienstverlening]
archimate_type: product
grondslag: "ggm-entiteit"
ggm_entiteit: "ProductOfDienst"
ggm_guid: EAID_4B871112_CB41_4bfb_BD43_117C63D31BB4
ggm_uml_type: Class
ggm_beleidsdomein: "10 Dienstverlening"
ggm_taakveld: "10 Dienstverlening"
ggm_diagram: [Entiteiten Dienstverlening, Afspraken en Klantcontacten, Entiteiten Klantcontact, Klantbeoordelingen]
ggm_diagram_ids: [EAID_48B6C3F9_CCF1_4794_8252_FC6543409B78, EAID_282A4979_0BBC_4448_B71C_0CE64829083B, EAID_5901286A_E9EF_4360_9CE6_32B6FDE1C970, EAID_AE8DC6AF_062B_4111_BAB4_D58F21FDDDF1]
ggm_definitie: "Bron: QP_CALENDAR.CFM_SERVICES"
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "ProductOfDienst"
ggm_gemma_guid: "724f019e-158f-4404-8b57-3e1eae109fec"
ggm_gemma_definitie: "Bron: QP_CALENDAR.CFM_SERVICES"
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-724f019e-158f-4404-8b57-3e1eae109fec"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "Een door de gemeente aangeboden dienst of product waarvoor inwoners, ondernemers of organisaties een aanvraag kunnen indienen of een afspraak kunnen maken."
bedrijfsprocessen: [Productcatalogusbeheer, Dienstverlening]
bedrijfsfuncties: [Dienstverlening, Productmanagement]
relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/balieafspraak|balieafspraak]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: balieafspraak betreft dit product of dienst
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding|aanvraag-of-melding]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: aanvraag betreft (indirect via klantcontact)
---

## BO-criteria toetsing

| Criterium | Toepassing |
|---|---|
| Betekenis binnen domein | ✅ Definiëert wat de gemeente aanbiedt |
| Herkenbaar voor experts | ✅ Elke gemeente heeft een producten- en dienstencatalogus (PDC) |
| Eigen bestaan | ✅ Bestaat onafhankelijk van individuele aanvragen |
| Meervoud | ✅ Gemeenten bieden honderden producten en diensten aan |
| Levenscyclus | ✅ Ingesteld → in gebruik → uitgefaseerd |
| Relaties | ✅ Met balieafspraak, klantcontact, klantbeoordeling, zaaktype |

Score: 6/6 — duidelijk een bedrijfsobject.

## Beschrijving

Een product of dienst is wat de gemeente aanbiedt aan haar inwoners, ondernemers en organisaties. Gemeenten beheren hun aanbod in een producten- en dienstencatalogus (PDC). Voorbeelden: paspoort aanvragen, rijbewijs verlengen, bijstandsuitkering aanvragen, melding openbare ruimte doen.

Het product of dienst vormt de schakel tussen de dienstverleningslaag (wat bied je aan?) en de zaaklaag (hoe handel je het af?). Via de ZTC2 wordt elk product gekoppeld aan één of meer zaaktypen die de afhandeling configureren.

## GGM-bron

> "Bron: QP_CALENDAR.CFM_SERVICES" (GGM definitie)

- **Entiteit:** ProductOfDienst
- **Beleidsdomein:** Model Dienstverlening (taakveld 10)
- **Matchsterkte:** sterk
- **Attributen:** naam, afhandeltijd, ingebruik

De GGM-definitie is een systeemreferentie naar het bronsysteem, niet een inhoudelijke definitie. De GEMMA-definitie is daarom afwijkend geformuleerd.

## BO-definitie

> **Een door de gemeente aangeboden dienst of product waarvoor inwoners, ondernemers of organisaties een aanvraag kunnen indienen of een afspraak kunnen maken.**

## Relaties

| Gerelateerd BO | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/balieafspraak|balieafspraak]] | ← | 0..* | afspraak betreft dit product/dienst | GGM: Balieafspraak → ProductOfDienst |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding|aanvraag-of-melding]] | ← | 0..* | aanvraag betreft (via klantcontact) | GGM: Klantcontact → ProductOfDienst |
| zaaktypecatalogus | → | 0..* | gekoppeld aan zaaktype(n) via ZTC | Standaard ZTC2 |

## Terugmelding GGM

De definitie "Bron: QP_CALENDAR.CFM_SERVICES" is een systeemreferentie, geen inhoudelijke definitie. Suggestie: vervang door een beschrijvende definitie.
