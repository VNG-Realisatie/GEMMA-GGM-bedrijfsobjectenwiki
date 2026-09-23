---
type: element
naam: Huishoudenlid
onderwerp: [Basisregistraties, RSGBPlus]
archimate_type: business-object
grondslag: ggm-afgeleid

# GGM-velden
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

# GEMMA-waarden
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

analyse_ggm_dekking: ""
bo_definitie: "De positie die een ingeschreven persoon inneemt binnen een huishouden: hoofd, partner van het hoofd, kind, of overig lid."
bo_toelichting: "Het hoofd van het huishouden is degene die als vertegenwoordiger van het huishouden wordt aangesproken. Elke ingeschreven persoon heeft op elk moment ten hoogste één actieve positie in één huishouden (RSGB Deel II §2.18, attribuutsoort Huishoudenrelatiecode, kardinaliteit 1-1)."
bo_subtypes:
  - naam: Hoofd van het huishouden
    omschrijving: "Vertegenwoordiger van het huishouden"
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: huishoudenrelatiecode
  - naam: Partner van het hoofd
    omschrijving: ""
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: huishoudenrelatiecode
  - naam: Kind
    omschrijving: ""
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: huishoudenrelatiecode
  - naam: Overig lid
    omschrijving: ""
    ggm_entiteit: ""
    ggm_guid: ""
    ggm_attribuut: huishoudenrelatiecode
bo_via_kandidaten: []
bo_synoniemen:
  - naam: Huishoudenrelatie
    context: "RSGB Deel II-objecttypenaam"
bo_homoniemen: []
element_tegenhangers: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/huishouden|Huishouden]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Hoort bij een huishouden"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon|Ingeschreven Persoon]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Betreft een ingeschreven persoon"
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

| Criterium | Oordeel |
|---|---|
| Heeft betekenis binnen het onderwerp | ✅ Bepaalt wie als vertegenwoordiger van het huishouden wordt aangesproken (bijstand, huursubsidie) |
| Herkenbaar voor domeinexperts | ✅ "Hoofd van het huishouden", "gezinssamenstelling" zijn herkenbare begrippen in sociaal domein/burgerzaken |
| Heeft een eigen bestaan binnen het onderwerp | ✅ Bestaat als koppeling met een eigen rolcode, los van zowel de persoon als het huishouden |
| Kan in meervoud bestaan | ✅ Elk huishouden heeft één of meer leden |
| Heeft een eigen levenscyclus | ✅ Ontstaat en eindigt onafhankelijk van de levenscyclus van persoon of huishouden (bijv. bij verhuizing) |
| Heeft relaties met andere concepten | ✅ Huishouden, Ingeschreven Persoon |

6/6 — BO.

## Beschrijving

Huishoudenlid legt de positie vast die een ingeschreven persoon binnen een huishouden inneemt: hoofd van het huishouden, partner van het hoofd, kind, of overig lid. Het hoofd is degene die als vertegenwoordiger van het huishouden wordt aangesproken. Elke ingeschreven persoon heeft op elk moment ten hoogste één actieve positie, in ten hoogste één huishouden.

RSGB Deel II noemt dit objecttype "Huishoudenrelatie"; deze pagina gebruikt "Huishoudenlid" omdat dat de handeling van de onderliggende gegevens beter dekt (wie is lid, in welke rol) dan de technische informatiemodel-term "relatie".

## Afleiding

Geen aparte GGM-klasse: in de GGM-XMI is dit gemodelleerd als een rechtstreekse associatie "Huishouden → IngeschrevenPersoon (heeft)", zonder tussenliggende relatie-entiteit. Dit BO maakt de rolcode expliciet die RSGB Deel II bij die associatie beschrijft (attribuutsoort Huishoudenrelatiecode, waarden: hoofd/partner/kind/overig lid).

## Relaties

| Relatie | Richting | BO | Beschrijving | Bron |
|---|---|---|---|---|
| hoort bij | → | [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/huishouden\|Huishouden]] | | RSGB Deel II |
| betreft | → | [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | | RSGB Deel II |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/rsgb-deel-ii-specificaties]]
