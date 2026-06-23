---
type: bedrijfsobject
naam: Levering
domein: [Maatschappelijke Ondersteuning]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Levering
ggm_guid: EAID_F0CE97B6_3004_4424_A0AA_5034BC0144D1
ggm_uml_type: Class
ggm_beleidsdomein: "Generiek Jeugd en Wmo"
ggm_taakveld: "6 Sociaal Domein"
ggm_diagram: ["Sociaal Domein Beschikking en Voorziening: Domain Objects"]
ggm_diagram_ids: [EAID_5AE29494_3572_4924_B2B8_3206E55D71BB]
ggm_definitie: "Levering van zorg door leverancier."
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

gemma_definitie: "Daadwerkelijk geleverde zorg of ondersteuning door een zorgaanbieder aan een cliënt."
relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/toewijzing|Toewijzing]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "op basis van toewijzing"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/voorziening|Voorziening]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "betreft voorziening"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client|Client]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "geleverd aan cliënt"
bedrijfsprocessen: [zorglevering registreren, declaratie verwerken, zorgcontinuïteit bewaken]
bedrijfsfuncties: [voorzieningenbeheer, contractbeheer]
---

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Herkenbaar in gemeentelijk domein | ✅ | Leveringsberichten zijn kern van het iWmo/iJw-berichtenverkeer |
| Besproken op bestuurlijk niveau | ✅ | Leveringsgegevens in verantwoording en contractmonitoring |
| Vastgelegd in systemen | ✅ | Geregistreerd via berichtenverkeer in suite voor sociaal domein |
| Eigen attributen | ✅ | eenheid, frequentie, omvang, code, datumStart, datumStop, stopreden |
| Relaties met andere objecten | ✅ | Toewijzing, Voorziening, Client |
| Levenscyclus | ✅ | Start bij aanvang zorg, wordt periodiek geregistreerd, eindigt bij stopreden |

## Beschrijving

Een levering is de registratie van daadwerkelijk geleverde zorg of ondersteuning door een zorgaanbieder aan een cliënt. De aanbieder meldt via het iWmo/iJw-berichtenverkeer welke zorg is geleverd, in welke omvang en frequentie. De gemeente gebruikt leveringsgegevens voor declaratieverwerking, contractmonitoring en verantwoording. Bij beëindiging wordt een stopreden vastgelegd.

## GGM-bron

> "Levering van zorg door leverancier." — GGM Generiek Jeugd en Wmo

- **Entiteit:** Levering
- **Beleidsdomein:** Generiek Jeugd en Wmo
- **Attributen:** eenheid, frequentie, omvang, code, datumStart, datumStop, stopreden
- **Matchsterkte:** exact

## Relaties

| Gerelateerd BO | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/toewijzing\|Toewijzing]] | ← | 1 | op basis van toewijzing | GGM |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/voorziening\|Voorziening]] | ← | 1 | betreft voorziening | GGM |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | ← | 1 | geleverd aan cliënt | GGM |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | ← | 1 | geleverde prestatie bij beschikking | GGM |

## Bedrijfsprocessen

- Zorglevering registreren
- Declaratie verwerken
- Zorgcontinuïteit bewaken

## Bedrijfsfuncties

- Voorzieningenbeheer
- Contractbeheer

## Bronnen

- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/maatwerkvoorzieningen-wmo]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/beleidsregels-jeugdhulp-oost-gelre]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/beleidsnota-jeugd-utrecht]]
