---
type: bedrijfsobject
naam: Sportpark
domein: [Sport en Bewegen]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Sportpark"
ggm_guid: EAID_FE1A2EF2_44FA_46fa_A583_7BAB858E17FD
ggm_uml_type: Class
ggm_beleidsdomein: "Sport"
ggm_taakveld: "5 Sport, Cultuur en Recreatie"
ggm_diagram: [Diagram Sportbeleid, Diagram Sportbeleid Locaties]
ggm_diagram_ids: [EAID_25BCAA7D_6255_4f3a_8408_DF91881FE29F, EAID_BA23F316_FE48_49a8_A26D_9B1D14713F76]
ggm_definitie: "Geheel van terreinen, gebouwen en voorzieningen voor verschillende takken van sport."
ggm_toelichting: ""
ggm_synoniemen: "Sportterrein"
ggm_herkomst: ""
ggm_gemma_naam: "Sportpark"
ggm_gemma_guid: "ca9df4ee-92e1-4c24-ace3-467d146a320e"
ggm_gemma_definitie: "Geheel van terreinen, gebouwen en voorzieningen voor verschillende takken van sport."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: "Sportterrein"
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-ca9df4ee-92e1-4c24-ace3-467d146a320e"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "Geheel van terreinen, gebouwen en voorzieningen voor verschillende takken van sport."
relaties:
  - type: generalisatie
    bedrijfsobject: "[[Sportlocatie]]"
    richting: "naar-dit-BO"
    kardinaliteit: ""
    beschrijving: "Sportpark is een specialisatie van Sportlocatie"
  - type: compositie
    bedrijfsobject: "[[Veld]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Een sportpark bevat sportvelden"
  - type: associatie
    bedrijfsobject: "[[Sportvereniging]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Sportverenigingen gebruiken sportparken"
bedrijfsprocessen: [Ingebruikgeving sportaccommodaties, Capaciteitsplanning sport, Sportparkbeheer, Groot onderhoud en vervanging]
bedrijfsfuncties: [Sportaccommodatiebeheer, Sportbeleid]
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis in het domein (centraal in sportbeleid), herkenbaar voor domeinexperts, eigen bestaan (fysiek terrein), meervoud (meerdere sportparken in Utrecht), eigen levenscyclus (aanleg, herontwikkeling, openstelling, sluiting), relaties met [[Veld]], [[Sportvereniging]], [[Binnenlocatie]].

## Beschrijving

Een sportpark is een geheel van terreinen, gebouwen en voorzieningen voor verschillende takken van sport. De gemeente beheert sportparken, stuurt op capaciteit en ingebruikgeving, en bepaalt de maatschappelijke functie (openstelling voor buurtbewoners, maatschappelijke hotspots). In Utrecht zijn specifieke sportparken centraal in het beleid: Maarschalkerweerd-Noord, Nieuw Welgelegen, Rijnvliet, Strijkviertel, Zuilense Vecht, De Dreef, Vechtzoom, Thorbeckelaan en Papendorp.

## GGM-bron

> "Geheel van terreinen, gebouwen en voorzieningen voor verschillende takken van sport." (GGM, entiteit Sportpark, beleidsdomein Sport)

- **Entiteit:** Sportpark
- **Beleidsdomein:** Sport
- **Attributen:** *(geen)*
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Sportlocatie]] | generaliseert | | GGM |
| [[Veld]] | bevat | 0..* | GGM |
| [[Sportvereniging]] | wordt gebruikt door | 0..* | GGM |
| OverigBenoemdTerrein (BAG) | ligt op | 1 | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Sport en Bewegen/beleidsnota-sport-en-bewegen-2025-2032]]
- [[Wiki/Bronsamenvattingen/Sport en Bewegen/uitvoeringsprogramma-sport-en-bewegen-2025]]
