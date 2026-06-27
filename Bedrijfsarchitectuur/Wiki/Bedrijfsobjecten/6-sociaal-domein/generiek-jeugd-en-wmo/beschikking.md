---
type: bedrijfsobject
naam: Beschikking
domein: [Maatschappelijke Ondersteuning]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Beschikking
ggm_guid: EAID_71D7E96D_641A_4b6a_A325_DED07C3B5836
ggm_uml_type: Class
ggm_beleidsdomein: "Generiek Jeugd en Wmo"
ggm_taakveld: "6 Sociaal Domein"
ggm_diagram: ["Sociaal Domein Beschikking en Voorziening: Domain Objects", Beperkingen, AanvraagOfMelding]
ggm_diagram_ids: [EAID_5AE29494_3572_4924_B2B8_3206E55D71BB, EAID_9B278A50_862A_4085_B362_C41392101916, EAID_5F3782EB_C416_461c_A9FA_40991A7F0165]
ggm_definitie: "In het bestuursrecht: Een beslissing van een overheidsorgaan in een concreet geval, bijvoorbeeld het verlenen van een bouwvergunning. In het civiele recht: een rechterlijke uitspraak in een procedure die begint met een verzoekschrift."
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

bo_definitie: "Formeel besluit van de gemeente op een aanvraag of melding voor ondersteuning onder de Wmo of Jeugdwet, met rechtsgevolgen voor de cliënt."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/voorziening|Voorziening]]"
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "heeft voorzieningen (via Beschikte Voorziening)"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client|Client]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "betreft cliënt"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/toewijzing|Toewijzing]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "leidt tot toewijzing"
bedrijfsprocessen: [aanvraag/melding Wmo-Jeugd afhandelen, beschikking afgeven, bezwaar en beroep behandelen]
bedrijfsfuncties: [toegang sociaal domein, beschikkingenbeheer]
---

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Herkenbaar in gemeentelijk domein | ✅ | Centraal beslisdocument in Wmo/Jeugdwet-keten |
| Besproken op bestuurlijk niveau | ✅ | Aantallen beschikkingen in raadsinformatie en programmabegroting |
| Vastgelegd in systemen | ✅ | Geregistreerd in Wmo/Jeugd-applicatie (suite voor sociaal domein) |
| Eigen attributen | ✅ | datumAfgifte, code, grondslagen, commentaar, wet |
| Relaties met andere objecten | ✅ | Client, Beschikte Voorziening, Toewijzing, Melding/Aanvraag |
| Levenscyclus | ✅ | Ontstaat bij besluit, kan worden gewijzigd, ingetrokken of verlopen |

## Beschrijving

Een beschikking is het formele besluit van de gemeente op een aanvraag of melding voor ondersteuning onder de Wmo 2015 of de Jeugdwet. Het beschrijft welke voorziening(en) de cliënt krijgt, in welke omvang en voor welke periode. De beschikking heeft rechtsgevolgen: de cliënt kan bezwaar en beroep aantekenen.

In het Utrechtse model neemt het buurtteam het beschikkingsbesluit namens de gemeente, op basis van een gemotiveerd besluit volgens het beoordelingskader van de Centrale Raad van Beroep.

## GGM-bron

> "In het bestuursrecht: Een beslissing van een overheidsorgaan in een concreet geval." — GGM Generiek Jeugd en Wmo

- **Entiteit:** Beschikking
- **Beleidsdomein:** Generiek Jeugd en Wmo
- **Attributen:** datumAfgifte, code, grondslagen, commentaar, wet
- **Matchsterkte:** exact

## Relaties

| Gerelateerd BO | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/voorziening\|Voorziening]] | → | 1..* | heeft voorzieningen (via Beschikte Voorziening) | GGM |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | ← | 1 | betreft cliënt | GGM |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/toewijzing\|Toewijzing]] | → | 0..* | leidt tot toewijzing | GGM |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/levering\|Levering]] | → | 0..* | geleverde prestatie | GGM |

## Bedrijfsprocessen

- Aanvraag/melding Wmo-Jeugd afhandelen
- Beschikking afgeven
- Bezwaar en beroep behandelen

## Bedrijfsfuncties

- Toegang sociaal domein
- Beschikkingenbeheer

## Bronnen

- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/beleidsregels-jeugdhulp-oost-gelre]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/beleidsnota-jeugd-utrecht]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/jeugdwet]]
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/wmo-2015]]
