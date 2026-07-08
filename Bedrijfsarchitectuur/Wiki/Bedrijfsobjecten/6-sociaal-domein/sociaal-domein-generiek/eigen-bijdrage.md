---
type: element
naam: Eigen bijdrage
domein: [Maatschappelijke Ondersteuning]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Eigen bijdrage
ggm_guid: EAID_87acd5ea_3ed9_40d8_96b0_8c29ce9296da
ggm_uml_type: Class
ggm_beleidsdomein: "Sociaal Domein Generiek"
ggm_taakveld: "6 Sociaal Domein"
ggm_diagram: ["Diagram Inkomsten"]
ggm_diagram_ids: []
ggm_definitie: "Eigen bijdrage bijvoorbeeld voor CAK of kinderopvang"
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: GGM

ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Eigen bijdrage** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Beslag op inkomen** (detail) — Detailgegeven (weinig attributen)
  - **Kostencomponent** (detail) — Detailgegeven (weinig attributen)
  - **Reiskosten naar het werk** (detail) — Detailgegeven (weinig attributen)
  - **Te betalen alimentatie** (detail) — Detailgegeven (weinig attributen)
bo_definitie: "Financiële bijdrage die een cliënt verschuldigd is voor Wmo-voorzieningen, vastgesteld door het CAK op basis van gemeentelijke gegevens."
bo_toelichting: ''
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client|Client]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "wordt opgelegd aan cliënt"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/toewijzing|Toewijzing]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "geeft aanleiding tot eigen bijdrage"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/levering|Levering]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "geeft aanleiding tot eigen bijdrage"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking|Beschikking]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "melding eigen bijdrage betreft beschikking"
bedrijfsprocessen: [eigen bijdrage bepalen, melding eigen bijdrage aan CAK, kostprijsbewaking]
bedrijfsfuncties: [financieel beheer sociaal domein, cliëntadministratie]
---

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Herkenbaar in gemeentelijk domein | ✅ | Kern van Wmo-financiering; abonnementstarief is politiek gevoelig onderwerp |
| Besproken op bestuurlijk niveau | ✅ | Eigen bijdrage regelingen in verordeningen, raadsinformatie, verantwoording |
| Vastgelegd in systemen | ✅ | Geregistreerd in suite sociaal domein, gecommuniceerd aan CAK via iEb-berichtenverkeer |
| Eigen attributen | ✅ | Soort (GGM); periodetypen (abonnementstarief, beschermd wonen), startdatum, stopdatum (GIZO) |
| Relaties met andere objecten | ✅ | Client, Toewijzing, Levering, Beschikking, CAK |
| Levenscyclus | ✅ | Bepaald door gemeente → gemeld aan CAK → opgelegd aan cliënt → geïnd |

## Beschrijving

De eigen bijdrage is het bedrag dat een cliënt zelf betaalt voor Wmo-voorzieningen. De gemeente bepaalt welke producten eigen-bijdrageplichtig zijn en communiceert via het iEb-berichtenverkeer de relevante gegevens aan het CAK, dat de eigen bijdrage vaststelt en int.

Er zijn twee regimes:
- **Abonnementstarief:** vaste maandelijkse bijdrage voor maatwerkvoorzieningen (sinds 2019, Wmo 2015 art. 2.1.4a). De start- en stopzorg berichten worden gebruikt als trigger.
- **Beschermd wonen:** aparte eigen bijdrage met eigen berekeningsmethode en perioden.

De gemeente levert aan het CAK de "leveringsdatum" aan: de datum waarop de cliënt voor het eerst het toegewezen product geleverd krijgt. Deze datum wordt vastgesteld op basis van de toewijzing, de declaratie of de levering, afhankelijk van de lokale afspraken.

## GGM-bron

> "Eigen bijdrage bijvoorbeeld voor CAK of kinderopvang" — GGM Sociaal Domein Generiek

- **Entiteit:** Eigen bijdrage
- **Beleidsdomein:** Sociaal Domein Generiek
- **Attributen:** Soort
- **Matchsterkte:** exact
- **Generalisatie:** subtype van Kostencomponent (abstract)

## GGM-componenten

GGM-entiteiten die onderdeel zijn van Eigen bijdrage. Gemodelleerd als aparte entiteiten in het GGM maar vormen geen zelfstandig bedrijfsobject.

- **Melding Eigen bijdrage** — melding aan het CAK met datumStart en datumStop, gerelateerd aan Beschikking (GGM Generiek Jeugd en Wmo)

## Relaties

| Gerelateerd BO | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | ← | 1 | wordt opgelegd aan cliënt | GIZO |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/toewijzing\|Toewijzing]] | ← | 0..* | geeft aanleiding tot eigen bijdrage | GIZO |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/levering\|Levering]] | ← | 0..* | geeft aanleiding tot eigen bijdrage | GIZO |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | ← | 1 | melding eigen bijdrage betreft beschikking | GGM |

## Bedrijfsprocessen

- Eigen bijdrage bepalen
- Melding eigen bijdrage aan CAK
- Kostprijsbewaking

## Bedrijfsfuncties

- Financieel beheer sociaal domein
- Cliëntadministratie

## Bronnen

- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/informatiemodel-gizo]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/wmo-2015]]
