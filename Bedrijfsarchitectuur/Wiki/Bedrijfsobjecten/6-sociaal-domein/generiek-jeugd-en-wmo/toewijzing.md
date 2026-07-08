---
type: element
naam: Toewijzing
domein: [Maatschappelijke Ondersteuning]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Toewijzing
ggm_guid: EAID_01ECE551_A7B0_4b99_B6E7_F654D6AC15D5
ggm_uml_type: Class
ggm_beleidsdomein: "Generiek Jeugd en Wmo"
ggm_taakveld: "6 Sociaal Domein"
ggm_diagram: ["Sociaal Domein Beschikking en Voorziening: Domain Objects"]
ggm_diagram_ids: [EAID_5AE29494_3572_4924_B2B8_3206E55D71BB]
ggm_definitie: "Toewijzing die door gemeente aan zorgaanbieder wordt gestuurd."
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
  Dit BO heeft de GGM-entiteit **Toewijzing** als directe tegenhanger.
bo_definitie: "Toewijzing die door gemeente aan zorgaanbieder wordt gestuurd."
bo_toelichting: ''
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking|Beschikking]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "volgt uit beschikking"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/voorziening|Voorziening]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "betreft voorziening (via Beschikte Voorziening)"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/levering|Levering]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "leidt tot levering"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client|Client]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "betreft cliënt (via Beschikking)"
bedrijfsprocessen: [toewijzing versturen, toewijzing wijzigen, toewijzing intrekken]
bedrijfsfuncties: [toegang sociaal domein, contractbeheer]
---

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Herkenbaar in gemeentelijk domein | ✅ | Standaardbericht in iWmo/iJw-berichtenverkeer tussen gemeente en aanbieder |
| Besproken op bestuurlijk niveau | ✅ | Toewijzingsaantallen in managementrapportages sociaal domein |
| Vastgelegd in systemen | ✅ | Geregistreerd in suite voor sociaal domein, verstuurd via berichtenverkeer |
| Eigen attributen | ✅ | toewijzingnummer, datumToewijzing, datumStart, datumEinde, omvang, eenheid, frequentie, wet |
| Relaties met andere objecten | ✅ | Beschikking, Voorziening, Levering, Client |
| Levenscyclus | ✅ | Aangemaakt na beschikking, verstuurd naar aanbieder, gewijzigd of ingetrokken |

## Beschrijving

Een toewijzing is de opdracht die de gemeente aan een zorgaanbieder stuurt om een beschikte voorziening te leveren aan een cliënt. De toewijzing specificeert welke voorziening, in welke omvang, frequentie en periode geleverd moet worden. Het is een centraal object in het iWmo/iJw-berichtenverkeer: na het versturen van de toewijzing start de aanbieder de zorglevering.

## GGM-bron

> "Toewijzing die door gemeente aan zorgaanbieder wordt gestuurd." — GGM Generiek Jeugd en Wmo

- **Entiteit:** Toewijzing
- **Beleidsdomein:** Generiek Jeugd en Wmo
- **Attributen:** toewijzingnummer, datumToewijzing, datumStartToewijzing, datumEindeToewijzing, redenWijziging, omvang, commentaar, eenheid, frequentie, datumAanschaf, code, wet
- **Matchsterkte:** exact

## Relaties

| Gerelateerd BO | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | ← | 1 | volgt uit beschikking | GGM |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/voorziening\|Voorziening]] | ← | 1 | betreft voorziening (via Beschikte Voorziening) | GGM |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/levering\|Levering]] | → | 0..* | leidt tot levering | GGM |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | ← | 1 | betreft cliënt (via Beschikking) | GGM |

## Bedrijfsprocessen

- Toewijzing versturen
- Toewijzing wijzigen
- Toewijzing intrekken

## Bedrijfsfuncties

- Toegang sociaal domein
- Contractbeheer

## Bronnen

- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/maatwerkvoorzieningen-wmo]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/beleidsregels-jeugdhulp-oost-gelre]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/beleidsnota-jeugd-utrecht]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/jeugdwet]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/wmo-2015]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/procesbeschrijving-ijw-3.1]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/informatiemodel-gizo]]
