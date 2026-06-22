---
type: bedrijfsobject
naam: Short Stay Accommodatie
domein: [Economie]
archimate_type: "business-object"
grondslag: procesobject
ggm_entiteit: ""
ggm_beleidsdomein: ""
ggm_guid: ""
ggm_uml_type: ""
ggm_taakveld: ""
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: ""
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "Accommodatie voor bedrijfsmatig logies van minimaal twee weken tot maximaal zes maanden, gericht op internationale kenniswerkers en studenten."
bedrijfsprocessen: [short stay vergunningverlening, monitoring woningvoorraad]
bedrijfsfuncties: [vergunningverlening, economisch beleid, woonbeleid]
relaties:
  - type: associatie
    bedrijfsobject: "[[Horecabedrijf]]"
    richting: "naar-dit-BO"
    kardinaliteit: 0..1
    beschrijving: Short stay kan door een horecabedrijf of vastgoedexploitant worden aangeboden
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Apart gedefinieerd en gereguleerd via beleidsregels |
| Is herkenbaar voor domeinexperts | ✅ | Standaardbegrip in woon- en economisch beleid |
| Heeft een eigen bestaan | ✅ | Fysieke accommodatie met eigen kenmerken |
| Kan in meervoud bestaan | ✅ | Maximaal 1.080 eenheden (300 + 780) |
| Heeft een eigen levenscyclus | ✅ | Aanmelding → toekenning → exploitatie → eventueel beëindiging |
| Heeft relaties met andere concepten | ✅ | Woningvoorraad, exploitant, doelgroep |

6/6 criteria — BO.

## Beschrijving

Een short stay accommodatie is een accommodatie voor bedrijfsmatig logies van minimaal twee weken tot maximaal zes maanden aan dezelfde persoon. De accommodatie moet beschikken over eigen badkamer, keuken en toilet. Het beleid richt zich uitsluitend op twee doelgroepen: internationale kenniswerkers (expats) en internationale studenten.

De gemeente hanteert strikte capaciteitsgrenzen (1.080 eenheden totaal), ruimtenormen (minimaal 18 m² GBO per persoon) en maximale huurprijzen. Exploitanten moeten beschikken over huisregels en een beheerder.

## Procesbron

Short stay accommodatie ontstaat uit het vergunning-/aanmeldingsproces voor tijdelijk verblijf. De beleidsregels tijdelijk verblijf vormen de juridische grondslag, gericht op bescherming van de woningvoorraad.

> "Het bedrijfsmatig verstrekken van logies met een periode van minimaal twee weken tot maximaal zes maanden aan dezelfde persoon." — [[Wiki/Bronsamenvattingen/Economie/beleidsregels-short-stay-utrecht|Beleidsregels Tijdelijk Verblijf (Short Stay) Gemeente Utrecht]]

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Horecabedrijf]] | associatie | Horecabedrijf → Short Stay | 0..1 | Beleid |


## Bronnen

- [[Wiki/Bronsamenvattingen/Economie/beleidsregels-short-stay-utrecht]]

## Terugmelding GGM

**Short Stay Accommodatie** — Registratieobject voor tijdelijk verblijf (doelgroep, oppervlakte, huurprijs, exploitant, verblijfsduur, capaciteit). Dataobject vergelijkbaar met Hotel maar met eigen regelgeving en doelgroepen. Zou onder taakveld 3 Economie kunnen naast Hotel.
