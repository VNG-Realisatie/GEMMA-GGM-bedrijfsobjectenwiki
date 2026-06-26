---
type: bedrijfsobject
naam: Werkbon
onderwerp: [Vastgoed]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Werkbon
ggm_guid: EAID_C5AA8835_219D_4bfa_85EF_8BA45F732BCD
ggm_uml_type: Class
ggm_beleidsdomein: Vastgoed
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Vastgoed Domeinmodel, Vastgoed Leveranciers]
ggm_diagram_ids: [EAID_00D4246F_6ED7_4690_A180_ACCCD6AB1291, EAID_06E44472_8C2A_40eb_9965_DCF91A1322C9]
ggm_definitie: "Document waarin een hoeveelheid werk is beschreven."
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

gemma_definitie: "gelijk aan GGM"
gemma_subtypes: []
relaties:
  - type: associatie
    bedrijfsobject: "[[Vastgoedobject]]"
    richting: naar-dit-BO
    kardinaliteit: "1..1"
    beschrijving: "Een werkbon betreft een vastgoedobject"
  - type: associatie
    bedrijfsobject: "[[MJOP]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Een werkbon realiseert een MJOP-item"
bedrijfsprocessen: [uitvoering onderhoud vastgoed, klachtenonderhoud]
bedrijfsfuncties: [gebouwbeheer]
---

## BO-criteria toetsing

1. **Heeft betekenis** — het operationele werkinstrument voor onderhoud aan vastgoed
2. **Herkenbaar** — medewerkers buitendienst en aannemers werken dagelijks met werkbonnen
3. **Eigen bestaan** — een werkbon beschrijft een specifieke hoeveelheid werk, los van het MJOP
4. **Meervoud** — tientallen tot honderden werkbonnen per jaar per gemeente
5. **Levenscyclus** — aangemaakt → toegewezen → uitgevoerd → afgemeld
6. **Relaties** — naar [[Vastgoedobject]], [[MJOP]], Bouwdeel, Leverancier, Inkooporder

## Beschrijving

Een werkbon is een document dat een hoeveelheid uit te voeren werk aan een [[Vastgoedobject]] beschrijft. Werkbonnen worden aangemaakt vanuit het [[MJOP]] (gepland onderhoud) of als reactie op klachten en storingen (klachtenonderhoud). Ze worden gekoppeld aan specifieke bouwdelen of bouwdeelelementen van het vastgoedobject.

De uitvoering kan in eigen beheer (door medewerkers van de gemeente) of worden uitbesteed aan een leverancier via een inkooporder. Het Gebouw Beheer Systeem registreert werkbonnen als onderdeel van de onderhoudshistorie.

## GGM-bron

> Document waarin een hoeveelheid werk is beschreven.

- **Entiteit:** Werkbon
- **Beleidsdomein:** Vastgoed
- **Attributen:** *(geen in GGM)*
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedobject\|Vastgoedobject]] | naar-dit-BO | 1..1 | Een werkbon betreft een vastgoedobject | GGM |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/mjop\|MJOP]] | naar-dit-BO | 0..1 | Gerealiseerd vanuit een MJOP | GGM |

## Bedrijfsprocessen

- Uitvoering planmatig onderhoud (vanuit MJOP)
- Klachtenonderhoud (reactief, op basis van meldingen)
- Kleine reparaties en storingen

## Bronnen

- [[Wiki/Bronsamenvattingen/Vastgoed/beleidsplan-vastgoed-hulst]]
