---
type: element
naam: Weerstandsvermogen en risicobeheersing
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

bo_definitie: "De relatie tussen de weerstandscapaciteit (middelen om niet-begrote kosten te dekken) en alle risico's waarvoor geen maatregelen zijn getroffen, uitgewerkt in een periodieke nota en een jaarlijkse paragraaf bij begroting en jaarrekening (art. 212 Gemeentewet, art. 11 BBV)."
bo_toelichting: "Twee samenhangende verschijningsvormen: de nota Weerstandsvermogen en Risicobeheersing (meerjarig beleidskader, vastgesteld op grond van de financiële verordening ex art. 212 Gemeentewet) en de jaarlijkse paragraaf Weerstandsvermogen en Risicobeheersing in begroting en jaarrekening (verplicht op grond van art. 11 BBV, met een vaste inhoud: risico-inventarisatie, weerstandscapaciteit-inventarisatie, beleid en kengetallen)."
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/risico|Risico]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: De risico-inventarisatie bevat de individuele risico's
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/reserve|Reserve]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Reserves vormen de incidentele weerstandscapaciteit
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/begroting|Begroting]]"
    richting: naar-dit-BO
    kardinaliteit: "1..1"
    beschrijving: De paragraaf is een verplicht onderdeel van de begroting
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/jaarrekening|Jaarrekening]]"
    richting: naar-dit-BO
    kardinaliteit: "1..1"
    beschrijving: De paragraaf is een verplicht onderdeel van de jaarrekening
bedrijfsprocessen: [Risicomanagement, P&C-cyclus]
bedrijfsfuncties: [Financieel beheer, Risicobeheer]
---

# Weerstandsvermogen en risicobeheersing

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Identificeerbaar | Ja — periodieke nota (meerjarig) en jaarlijkse paragraaf, elk met eigen vaststellingsmoment |
| Eigen attributen | Ja — risico-inventarisatie, weerstandscapaciteit-inventarisatie, beleid, kengetallen (netto schuldquote, solvabiliteitsratio, grondexploitatie, structurele exploitatieruimte, belastingcapaciteit) |
| Levenscyclus | Ja — nota opstellen (financiële verordening) → jaarlijkse paragraaf in begroting/jaarrekening → periodieke actualisatie van de nota |
| Gemeentelijk eigendom | Ja — de gemeenteraad stelt de nota vast, het college stelt de paragraaf op |
| Wettelijke grondslag | Ja — Gemeentewet art. 212 (financiële verordening) en BBV art. 11 |
| Registratieverplichting | Ja — de paragraaf heeft een wettelijk voorgeschreven minimuminhoud (art. 11 lid 2 BBV) |

Score: 6/6 criteria.

## Beschrijving

Het weerstandsvermogen geeft aan in hoeverre een gemeente in staat is om niet-afgedekte risico's op te vangen zonder dat het beleid ingrijpend moet worden gewijzigd. Het bestaat uit de verhouding tussen de beschikbare weerstandscapaciteit (de middelen die de gemeente kan vrijmaken om substantiële tegenvallers op te vangen — reserves, onbenutte belastingcapaciteit, begrotingsruimte, post onvoorzien) en de risico's waarvoor geen specifieke maatregelen zijn getroffen.

De gemeenteraad stelt op grond van de financiële verordening (art. 212 Gemeentewet) periodiek een nota Weerstandsvermogen en Risicobeheersing vast, met het beleid rond risicomanagement en de gewenste ratio weerstandsvermogen. Op grond van art. 11 BBV bevat de jaarlijkse paragraaf in begroting en jaarrekening ten minste: een inventarisatie van de weerstandscapaciteit, een inventarisatie van de risico's, het beleid omtrent weerstandscapaciteit en risico's, vijf verplichte financiële kengetallen, en een beoordeling van de onderlinge verhouding tussen die kengetallen.

Risico's die al zijn afgedekt door een reserve, voorziening of verzekering tellen niet mee in de risico-inventarisatie voor het weerstandsvermogen — alleen de risico's die niet op een andere manier zijn ondervangen zijn relevant.

## Juridische bron

Wettelijke grondslag: Gemeentewet art. 212 (financiële verordening) en Besluit begroting en verantwoording provincies en gemeenten (BBV), art. 11.

Toegelicht en uitgewerkt in [[Wiki/Bronsamenvattingen/Risicobeheer/nota-weerstandsvermogen-risicobeheersing-waadhoeke|Nota Weerstandsvermogen en Risicobeheersing (Gemeente Waadhoeke)]].

## Relaties

| Relatie | Bedrijfsobject | Richting | Beschrijving |
|---|---|---|---|
| associatie | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/risico\|Risico]] | ← | Risico-inventarisatie bevat de individuele risico's |
| associatie | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/reserve\|Reserve]] | ← | Reserves vormen de incidentele weerstandscapaciteit |
| associatie | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/begroting\|Begroting]] | ← | Paragraaf is verplicht begrotingsonderdeel |
| associatie | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/jaarrekening\|Jaarrekening]] | ← | Paragraaf is verplicht jaarrekeningonderdeel |

## Bedrijfsprocessen

- **Risicomanagement** — identificeren, kwantificeren en beheersen van risico's
- **P&C-cyclus** — jaarlijkse opname van de paragraaf in begroting en jaarrekening

## Bronnen
- [[Wiki/Bronsamenvattingen/Risicobeheer/nota-weerstandsvermogen-risicobeheersing-waadhoeke]]

## Terugmelding GGM

GGM-hiaat: wettelijk verplicht governance-instrument (art. 212 Gemeentewet, art. 11 BBV), kernonderdeel van de gemeentelijke P&C-cyclus naast de wel gemodelleerde [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/begroting|Begroting]]. Geen GGM-entiteit.
