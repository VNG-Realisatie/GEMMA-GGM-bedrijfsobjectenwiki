---
type: element
naam: Verhuurbare Eenheid
onderwerp: [Vastgoed]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Verhuurbaar Eenheid
ggm_guid: EAID_98A7AE65_A061_449a_94CD_6218069CA86A
ggm_uml_type: Class
ggm_beleidsdomein: Vastgoed
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Vastgoed Domeinmodel, POC Vastgoed, Vastgoed verankering RSGB IMBAG]
ggm_diagram_ids: [EAID_00D4246F_6ED7_4690_A180_ACCCD6AB1291, EAID_8B8444CB_1E64_454b_82F9_48A7C9011CE0, EAID_FDB58817_3F2A_4d73_A7DB_7906F9B9EB45]
ggm_definitie: "Een Verhuurbare Eenheid (VHE) is een eenheid die individueel verhuurbaar is. Verhuurbaar komt voort uit 'exploitatie'."
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

ggm_duplicaat_entiteiten: []

analyse_ggm_dekking: |
  Dit BO is de hernoeming van GGM-entiteit **Verhuurbaar Eenheid**.
bo_definitie: "Een Verhuurbare Eenheid (VHE) is een eenheid die individueel verhuurbaar is. Verhuurbaar komt voort uit 'exploitatie'."
bo_toelichting: ''
bo_subtypes: []
bo_relaties:
  - type: compositie
    bedrijfsobject: "[[Vastgoedobject]]"
    richting: naar-dit-BO
    kardinaliteit: "1..1"
    beschrijving: "Een verhuurbare eenheid hoort bij een vastgoedobject"
  - type: associatie
    bedrijfsobject: "[[Vastgoedcontract]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Een verhuurbare eenheid heeft een contractregel"
bedrijfsprocessen: [verhuur gemeentelijk vastgoed, bezettingsgraadsturing]
bedrijfsfuncties: [vastgoedexploitatie]
---

## BO-criteria toetsing

1. **Heeft betekenis** — sleutelbegrip in vastgoedexploitatie; onderscheid pand vs. verhuurbare eenheid is essentieel
2. **Herkenbaar** — vastgoedbeheerders werken met VHE's als eenheid van verhuur en facturering
3. **Eigen bestaan** — een VHE bestaat als afgebakend deel van een pand, ook zonder huurder
4. **Meervoud** — Amsterdam: 2.381 verhuurbare eenheden in 1.015 gebouwen
5. **Levenscyclus** — ontstaat bij oplevering/splitsing, wijzigt bij herindeling, vervalt bij sloop/samenvoeging
6. **Relaties** — naar [[Vastgoedobject]], [[Vastgoedcontract]]

## Beschrijving

Een verhuurbare eenheid (VHE) is een individueel verhuurbaar deel van een [[Vastgoedobject]]. Eén pand kan meerdere verhuurbare eenheden bevatten — bijvoorbeeld een buurthuis met een apart verhuurbare zaal, of een kantoorpand met meerdere verdiepingen die apart worden verhuurd. De VHE is de eenheid waarop de huurovereenkomst en de huurprijs worden bepaald.

> "We maken een onderscheid tussen gebouwen en de verhuurbare eenheden, bijvoorbeeld een deel van het gebouw." (bron: Vastgoedstrategie Amsterdam)

## GGM-bron

> Een Verhuurbare Eenheid (VHE) is een eenheid die individueel verhuurbaar is. Verhuurbaar komt voort uit 'exploitatie'.

- **Entiteit:** Verhuurbaar Eenheid
- **Beleidsdomein:** Vastgoed
- **Attributen:** identificatie, naam, datumWerkelijkBegin, datumWerkelijkEinde, type, adres, datumStart, datumEinde, afmeting, opmerkingen, nettoOppervlak, nettoOmtrek, bezetting, huurprijs
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedobject\|Vastgoedobject]] | naar-dit-BO | 1..1 | Een VHE hoort bij een vastgoedobject | GGM |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedcontract\|Vastgoedcontract]] | van-dit-BO | 0..1 | Via vastgoedcontractregel | GGM |

## Bedrijfsprocessen

- Verhuur en exploitatie van gemeentelijk vastgoed
- Bezettingsgraadsturing en ruimte-optimalisatie
- Huurprijsberekening per eenheid

## Bronnen

- [[Wiki/Bronsamenvattingen/Vastgoed/vastgoedstrategie-amsterdam]]
