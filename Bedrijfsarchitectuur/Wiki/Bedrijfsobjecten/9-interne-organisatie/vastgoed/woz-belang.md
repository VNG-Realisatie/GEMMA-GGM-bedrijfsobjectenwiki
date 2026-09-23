---
type: element
naam: WOZ-belang
onderwerp: [Basisregistraties, WOZ, Vastgoed]
archimate_type: business-object
grondslag: ggm-entiteit

# GGM-velden
ggm_entiteit: WOZ-Belang
ggm_guid: EAID_E71DC5EC_EEEB_4d27_A3C1_B46FD34AD41B
ggm_uml_type: Class
ggm_beleidsdomein: Vastgoed
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram:
  - "Vastgoed WOZ"
ggm_diagram_ids: []
ggm_definitie: "De (rechts-)persoon die door de gemeente is aangewezen als \"belanghebbende eigenaar\", \"belanghebbende gebruiker\" of eventueel \"medebelanghebbende\" van het WOZ-object."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst: BRWOZ

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
bo_definitie: "Aanwijzing van een rechtspersoon als belanghebbende eigenaar, belanghebbende gebruiker of medebelanghebbende van een WOZ-object."
bo_toelichting: "Het belang wordt in de Basisregistratie WOZ opgenomen zodra dit bekend is; opname wordt bij de eerstvolgende WOZ-beschikking aan de belanghebbende kenbaar gemaakt. Koppelt [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/rechtspersoon|Rechtspersoon]] aan [[Wiki/Bedrijfsobjecten/99-kern/woz-object|WOZ-object]] — de grondslag voor wie een WOZ-beschikking ontvangt (zie ook de rol [[Wiki/Rollen/belanghebbende|Belanghebbende]])."
bo_subtypes:
  - naam: Belanghebbende eigenaar
    omschrijving: "Rechtspersoon aangewezen als eigenaar van het WOZ-object"
    ggm_entiteit: "WOZ-Belang"
    ggm_guid: EAID_E71DC5EC_EEEB_4d27_A3C1_B46FD34AD41B
    ggm_attribuut: eigenaarGebruiker
  - naam: Belanghebbende gebruiker
    omschrijving: "Rechtspersoon aangewezen als gebruiker van het WOZ-object"
    ggm_entiteit: "WOZ-Belang"
    ggm_guid: EAID_E71DC5EC_EEEB_4d27_A3C1_B46FD34AD41B
    ggm_attribuut: eigenaarGebruiker
bo_via_kandidaten: []
bo_synoniemen: []
bo_homoniemen: []
element_tegenhangers: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/woz-object|WOZ-object]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een WOZ-object heeft een of meer WOZ-belangen"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/rechtspersoon|Rechtspersoon]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een rechtspersoon kan als belanghebbende bij meerdere WOZ-objecten zijn aangewezen"
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

| Criterium | Oordeel |
|---|---|
| Heeft betekenis binnen het onderwerp | ✅ Bepaalt aan wie de WOZ-beschikking wordt verstuurd en wie bezwaar kan maken |
| Herkenbaar voor domeinexperts | ✅ Heffingsambtenaren en belastingafdeling werken dagelijks met "wie is belanghebbende" |
| Heeft een eigen bestaan binnen het onderwerp | ✅ Los van zowel het WOZ-object als de rechtspersoon: een aanwijzing die kan wijzigen zonder dat object of persoon wijzigt |
| Kan in meervoud bestaan | ✅ Eigenaar, gebruiker en eventueel medebelanghebbenden naast elkaar |
| Heeft een eigen levenscyclus | ✅ Datum begin/einde geldigheid belang, status belang |
| Heeft relaties met andere concepten | ✅ WOZ-object, Rechtspersoon |

6/6 — sterke BO.

## Beschrijving

WOZ-belang is de aanwijzing van een rechtspersoon als belanghebbende eigenaar, belanghebbende gebruiker of medebelanghebbende van een WOZ-object. Het belang wordt in de Basisregistratie WOZ opgenomen zodra dit bekend is, en de opname wordt bij de eerstvolgende WOZ-beschikking aan de belanghebbende kenbaar gemaakt.

Dit BO is de koppeling tussen [[Wiki/Bedrijfsobjecten/99-kern/woz-object|WOZ-object]] en [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/rechtspersoon|Rechtspersoon]] die eerder al genoemd werd in de relaties van Rechtspersoon ("is aangewezen belanghebbende bij WOZ-BELANG") en in [[Wiki/Bedrijfsobjecten/99-kern/woz-object|WOZ-object]]'s bestaande relatie naar de rol [[Wiki/Rollen/belanghebbende|Belanghebbende]] — dit BO maakt die relatie expliciet als apart, dateerbaar gegeven in plaats van een directe object-persoon-koppeling.

## GGM-bron

> "De (rechts-)persoon die door de gemeente is aangewezen als 'belanghebbende eigenaar', 'belanghebbende gebruiker' of eventueel 'medebelanghebbende' van het WOZ-object."

- **Entiteit:** WOZ-Belang
- **Package:** GGM beleidsdomein Vastgoed (taakveld 9 Interne Organisatie)
- **Attributen:** datumBeginGeldigheid, datumEindeGeldigheid, eigenaarGebruiker
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | BO | Beschrijving | Bron |
|---|---|---|---|---|
| betreft | → | [[Wiki/Bedrijfsobjecten/99-kern/woz-object\|WOZ-object]] | Het WOZ-object waarop het belang betrekking heeft | GGM |
| heeft als aangewezen belanghebbende | → | [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/rechtspersoon\|Rechtspersoon]] | De rechtspersoon die het belang draagt | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/rsgb-deel-ii-specificaties]]
