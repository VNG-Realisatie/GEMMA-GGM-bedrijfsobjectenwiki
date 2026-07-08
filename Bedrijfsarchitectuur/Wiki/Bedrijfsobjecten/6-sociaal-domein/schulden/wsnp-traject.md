---
type: bedrijfsobject
naam: WSNP-traject
onderwerp: [schulden en armoede]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: WSNP-traject
ggm_guid: EAID_513A944D_0FEC_4f78_B290_63274D22C58C
ggm_uml_type: Class
ggm_beleidsdomein: Schuldhulpverlening
ggm_taakveld: "Schulden"
ggm_diagram: [Schuldhulpproces]
ggm_definitie: "Een WSNP-traject (Wet schuldsanering natuurlijke personen) is een wettelijk regeling in Nederland waarmee individuen met problematische schulden via een saneringsplan onder toezicht van een bewindvoerder hun schulden kunnen aflossen en na drie jaar een schone lei kunnen krijgen."
ggm_herkomst: GGM

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **WSNP-traject** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Inkomen** (detail) — Detailgegeven
  - **Leefsituatie** (detail) — Detailgegeven (geassocieerd met BO)
  - **Partner** (detail) — Detailgegeven (weinig attributen)
  - **Woningbezit** (detail) — Detailgegeven (weinig attributen)
bo_definitie: "Een WSNP-traject (Wet schuldsanering natuurlijke personen) is een wettelijk regeling in Nederland waarmee individuen met problematische schulden via een saneringsplan onder toezicht van een bewindvoerder hun schulden kunnen aflossen en na drie jaar een schone lei kunnen krijgen."
bo_toelichting: ''
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[schuldhulptraject]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Vervolg op schuldhulptraject bij falen minnelijke regeling"
bedrijfsprocessen: [schuldhulpverlening]
bedrijfsfuncties: [financiële hulpverlening]
---

## BO-criteria toetsing

6/6 criteria. Zelfstandig wettelijk traject met eigen bewindvoerder, eigen verzoek/goedkeuring, en eigen levenscyclus (verzoek → toelating → uitvoering → schone lei). Loopt parallel aan of na het gemeentelijke schuldhulptraject.

## Beschrijving

Het WSNP-traject is de wettelijke schuldsanering wanneer een minnelijke regeling niet slaagt. De rechter benoemt een bewindvoerder die toeziet op de aflossing. Na drie jaar volgt een "schone lei" (kwijtschelding restschulden). De gemeente verwijst door naar de WSNP en levert een WSNP-verklaring (art. 285 Fw).

Den Haag pleit ervoor om bij evident kansloze minnelijke trajecten direct naar de WSNP te verwijzen zonder eerst een minnelijk voorstel te laten stranden.

## GGM-bron

> "Een WSNP-traject is een wettelijk regeling waarmee individuen met problematische schulden via een saneringsplan onder toezicht van een bewindvoerder hun schulden kunnen aflossen en na drie jaar een schone lei kunnen krijgen."

- **Entiteit:** WSNP-traject
- **Beleidsdomein:** Schuldhulpverlening
- **Attributen:** datumVerzoek, datumGoedkeuring, startdatum, einddatum
- **Matchsterkte:** exact

## Relaties

| Type | Bedrijfsobject | Kardinaliteit | Beschrijving |
|---|---|---|---|
| associatie | [[schuldhulptraject\|Schuldhulptraject]] | 0..1 | Vervolg bij falen minnelijk traject |

## Bronnen
- [[Wiki/Bronsamenvattingen/Schulden en Armoede/beleidsplan-schuldhulpverlening-den-haag-2024-2028]]
