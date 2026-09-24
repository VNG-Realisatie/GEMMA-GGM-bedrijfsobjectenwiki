---
type: element
naam: Risico
onderwerp: [Risicobeheer, Financien]
archimate_type: business-object
grondslag: governance-object

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

bo_definitie: "De kans op een gebeurtenis die de gemeente belemmert in het behalen van haar doelstellingen, met een mogelijk financieel gevolg."
bo_toelichting: "Voor het weerstandsvermogen zijn specifiek de financiële risico's relevant: de kans op een gebeurtenis die leidt tot een directe financiële tegenvaller van materiële betekenis, die niet is afgedekt in de begroting. Risico's kunnen structureel of incidenteel zijn, intern of extern, beïnvloedbaar of niet, en in geld te kwantificeren of niet."
bo_subtypes:
  - naam: "Afgedekt risico"
    omschrijving: "Risico waarvoor een specifieke maatregel is getroffen: een reserve, een voorziening of een verzekering. Telt niet mee in de risico-inventarisatie voor het weerstandsvermogen."
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: "Niet-afgedekt risico"
    omschrijving: "Risico zonder specifieke beheersmaatregel, relevant voor de risico-inventarisatie en de berekening van het weerstandsvermogen."
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/weerstandsvermogen-en-risicobeheersing|Weerstandsvermogen en risicobeheersing]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: Niet-afgedekte risico's worden opgenomen in de risico-inventarisatie
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/reserve|Reserve]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: Een reserve kan een risico afdekken
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/financiele-voorziening|Financiële Voorziening]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: Een voorziening kan een risico afdekken
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/verzekering|Verzekering]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: Een verzekering kan een risico afdekken
bedrijfsprocessen: [Risicomanagement]
bedrijfsfuncties: [Risicobeheer, Financieel beheer]
---

# Risico

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Identificeerbaar | Ja — elk risico is een afzonderlijke inventarisatiepost met eigen omschrijving |
| Eigen attributen | Ja — omschrijving, kans, financieel gevolg, aard (structureel/incidenteel, intern/extern), eventuele beheersmaatregel |
| Levenscyclus | Ja — identificeren → kwantificeren → (evt.) afdekken via reserve/voorziening/verzekering → periodiek herzien |
| Gemeentelijk eigendom | Ja — de gemeente identificeert en beheert haar eigen risico's |
| Wettelijke grondslag | Ja — onderdeel van de wettelijk verplichte risico-inventarisatie (art. 11 lid 2 sub b BBV) |
| Registratieverplichting | Ja — verplicht opgenomen in de risico-inventarisatie van de paragraaf Weerstandsvermogen en Risicobeheersing |

Score: 6/6 criteria.

## Beschrijving

Een risico is de kans op een gebeurtenis die de gemeente belemmert in het behalen van haar doelstellingen. Risico's zijn niet per definitie negatief — beleid maken en uitvoeren gaat vrijwel altijd gepaard met risico's — maar voor het weerstandsvermogen zijn specifiek de risico's relevant die een financieel gevolg kunnen hebben en niet al zijn afgedekt.

Gemeenten onderscheiden risico's op basis van meerdere kenmerken: afkomstig van binnen of buiten de eigen organisatie, wel of niet beïnvloedbaar, terugkerend (structureel) of eenmalig (incidenteel), en wel of niet in geld te kwantificeren. Voorbeelden van risicogebieden: het bedrijfs- en operationele proces, aansprakelijkheid, verbonden partijen (gemeenschappelijke regelingen, publiek-private samenwerking), subsidierelaties, gebiedsuitbreiding, open-einderegelingen en grondexploitaties.

Een deel van de risico's wordt afgedekt door specifieke maatregelen: het vormen van een reserve of voorziening, het afsluiten van een verzekering, of het inrichten van interne controle. Alleen de risico's die niet op een andere manier zijn ondervangen — en die van materiële betekenis kunnen zijn — worden meegenomen in de risico-inventarisatie die de basis vormt voor de berekening van het weerstandsvermogen.

## Specialisaties

Herkende specialisaties van Risico. Geen apart BO.

- **Afgedekt risico** — risico met een getroffen beheersmaatregel (reserve, voorziening of verzekering); buiten de risico-inventarisatie voor het weerstandsvermogen
- **Niet-afgedekt risico** — risico zonder beheersmaatregel; telt mee in de risico-inventarisatie en de benodigde weerstandscapaciteit

## Procesbron

Het risico ontstaat in het proces van risico-identificatie, onderdeel van het gemeentelijke risicomanagement. Zie [[Wiki/Bronsamenvattingen/Risicobeheer/nota-weerstandsvermogen-risicobeheersing-waadhoeke|Nota Weerstandsvermogen en Risicobeheersing (Gemeente Waadhoeke)]], hoofdstuk 3 en 5.

## Relaties

| Relatie | Bedrijfsobject | Richting | Beschrijving |
|---|---|---|---|
| associatie | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/weerstandsvermogen-en-risicobeheersing\|Weerstandsvermogen en risicobeheersing]] | → | Niet-afgedekte risico's in de risico-inventarisatie |
| associatie | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/reserve\|Reserve]] | ← | Kan het risico afdekken |
| associatie | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/financiele-voorziening\|Financiële Voorziening]] | ← | Kan het risico afdekken |
| associatie | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/verzekering\|Verzekering]] | ← | Kan het risico afdekken |

## Bedrijfsprocessen

- **Risicomanagement** — identificeren, kwantificeren, beheersen en periodiek herzien van risico's

## Bronnen
- [[Wiki/Bronsamenvattingen/Risicobeheer/nota-weerstandsvermogen-risicobeheersing-waadhoeke]]

## Terugmelding GGM

GGM-hiaat: geen entiteit voor het individuele risico als registratiepost. Vergelijkbaar met de eveneens ontbrekende [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/weerstandsvermogen-en-risicobeheersing|Weerstandsvermogen en risicobeheersing]] waarvan het onderdeel is.
