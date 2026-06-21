---
type: bedrijfsobject
naam: Sportmateriaal
domein: [Sport en Bewegen]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Sportmateriaal"
ggm_guid: EAID_5B64A5F8_64B5_4d1b_BEDD_486ED2C2C493
ggm_uml_type: Class
ggm_beleidsdomein: "Sport"
ggm_taakveld: "5 Sport, Cultuur en Recreatie"
ggm_diagram: [Diagram Sportbeleid]
ggm_diagram_ids: [EAID_25BCAA7D_6255_4f3a_8408_DF91881FE29F]
ggm_definitie: "Materieel om sport mee te beoefenen of ter odnersteuning van de sportuitvoering."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Sportmateriaal"
ggm_gemma_guid: "488958ee-08fd-4818-af8b-2d7ebb73c01f"
ggm_gemma_definitie: "Materieel om sport mee te beoefenen of ter odnersteuning van de sportuitvoering."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-488958ee-08fd-4818-af8b-2d7ebb73c01f"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "gelijk aan GGM"
bronnen: [Wiki/Bronsamenvattingen/Sport en Bewegen/beleidsnota-sport-en-bewegen-2025-2032, Wiki/Bronsamenvattingen/Sport en Bewegen/uitvoeringsprogramma-sport-en-bewegen-2025]
relaties:
  - type: associatie
    bedrijfsobject: "[[Binnenlocatie]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Sportmateriaal bevindt zich in een binnenlocatie"
bedrijfsprocessen: [Sportmateriaalbeheer, Uniek Sporten Uitleen]
bedrijfsfuncties: [Sportaccommodatiebeheer]
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis (onderdeel sportinfrastructuur), herkenbaar (doelen, netten, sporthulpmiddelen), eigen bestaan, meervoud, levenscyclus (aanschaf, uitleen, onderhoud, afschrijving), relaties met [[Binnenlocatie]].

## Beschrijving

Sportmateriaal is materieel om sport mee te beoefenen of ter ondersteuning van de sportuitvoering. Het omvat zowel standaard sportuitrusting in accommodaties als aangepaste sporthulpmiddelen die via Uniek Sporten Uitleen tijdelijk beschikbaar worden gesteld aan inwoners met een beperking.

## GGM-bron

> "Materieel om sport mee te beoefenen of ter odnersteuning van de sportuitvoering." (GGM, entiteit Sportmateriaal, beleidsdomein Sport)

- **Entiteit:** Sportmateriaal
- **Beleidsdomein:** Sport
- **Attributen:** naam
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Binnenlocatie]] | bevindt zich in | 0..* | GGM |
