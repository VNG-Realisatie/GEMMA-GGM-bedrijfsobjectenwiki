---
type: bedrijfsobject
naam: Ouder Of Verzorger
domein: [onderwijs]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Ouder Of Verzorger
ggm_guid: EAID_51C8E3DF_FFF4_4a20_9CB2_AA5FA50579E2
ggm_uml_type: Class
ggm_beleidsdomein: Onderwijs
ggm_taakveld: "4 Onderwijs"
ggm_diagram: [Diagram Beslissingen Leerplicht, "Onderwijs: Relaties met Kern"]
ggm_diagram_ids: [EAID_26A453D9_47AF_487e_854B_3B4BC6D6A308, EAID_D33047E8_3A39_4171_A7EC_93B137023ED8]
ggm_definitie: "Een persoon die wettelijk verantwoordelijk is voor de zorg en opvoeding van een kind."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""

ggm_gemma_naam: OuderOfVerzorger
ggm_gemma_guid: 91982611-d658-4c52-8869-0bbf87b487d3
ggm_gemma_definitie: "Een persoon die wettelijk verantwoordelijk is voor de zorg en opvoeding van een kind."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: business-object
ggm_gemma_url: https://gemmaonline.nl/index.php/GEMMA/id-91982611-d658-4c52-8869-0bbf87b487d3
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""

bo_definitie: "Een persoon die wettelijk verantwoordelijk is voor de zorg en opvoeding van een kind."
bo_toelichting: ''
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Leerling]]"
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: Ouder of verzorger is verantwoordelijk voor leerling
  - type: associatie
    bedrijfsobject: "[[Procesverbaal Onderwijs]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Procesverbaal wordt opgemaakt tegen ouder of verzorger
  - type: associatie
    bedrijfsobject: "[[Doorgeleiding OM]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Doorgeleiding naar OM betreft ouder of verzorger
bedrijfsprocessen: [Leerplichthandhaving, Leerlingenvervoer]
bedrijfsfuncties: [Leerplicht]
---

## BO-criteria toetsing

6/6 criteria: heeft betekenis (ja), herkenbaar (ja), eigen bestaan (ja), meervoud (ja), levenscyclus (ja — ouder/verzorger wordt geregistreerd bij inschrijving kind, is aanspreekpunt gedurende schoolloopbaan, rol eindigt bij meerderjarigheid), relaties (ja — met leerling, procesverbaal, doorgeleiding OM).

## Beschrijving

Een ouder of verzorger is de persoon die wettelijk verantwoordelijk is voor de zorg en opvoeding van een kind. De gemeente interacteert met ouders/verzorgers bij leerplichthandhaving: zij ontvangen verzuimmeldingen, worden uitgenodigd voor gesprekken en zijn adressaat van het procesverbaal bij ongeoorloofd verzuim. Daarnaast dienen ouders/verzorgers aanvragen in voor leerlingenvervoer. In het GGM erft Ouder Of Verzorger van IngeschrevenPersoon.

## GGM-bron

> "Een persoon die wettelijk verantwoordelijk is voor de zorg en opvoeding van een kind." — GGM, entiteit Ouder Of Verzorger, beleidsdomein Onderwijs

- **Entiteit:** Ouder Of Verzorger
- **Beleidsdomein:** Onderwijs
- **Attributen:** —
- **Matchsterkte:** exact

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Beschrijving |
|---|---|---|---|---|
| [[Leerling]] | associatie | van-dit-BO | 1..* | Ouder of verzorger is verantwoordelijk voor leerling |
| [[Procesverbaal Onderwijs]] | associatie | van-dit-BO | 0..* | Procesverbaal wordt opgemaakt tegen ouder of verzorger |
| [[Doorgeleiding OM]] | associatie | van-dit-BO | 0..* | Doorgeleiding naar OM betreft ouder of verzorger |

## Bedrijfsprocessen

- Leerplichthandhaving — aanspreekpunt bij verzuim, procesverbaal, doorgeleiding
- Leerlingenvervoer — aanvrager van vervoersvoorzieningen voor kind

## Bedrijfsfuncties

- Leerplicht

## Bronnen

- [[Wiki/Bronsamenvattingen/onderwijs/passend-onderwijs]]
- [[Wiki/Bronsamenvattingen/onderwijs/leerlingenvervoer]]
