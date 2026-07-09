---
type: element
naam: Sportvereniging
onderwerp: [Sport en Bewegen]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Sportvereniging"
ggm_guid: EAID_852AD372_B353_49c2_A4E7_F87D8AA96AD7
ggm_uml_type: Class
ggm_beleidsdomein: "Sport"
ggm_taakveld: "5 Sport, Cultuur en Recreatie"
ggm_diagram: [Diagram Sportbeleid]
ggm_diagram_ids: [EAID_25BCAA7D_6255_4f3a_8408_DF91881FE29F]
ggm_definitie: "Organisatievorm waarin sport bedreven kan worden"
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:
ggm_gemma_naam: "Sportvereniging"
ggm_gemma_guid: "59d3efaa-a05f-477a-a271-49bac323939f"
ggm_gemma_definitie: "Organisatievorm waarin sport bedreven kan worden"
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-59d3efaa-a05f-477a-a271-49bac323939f"
ggm_gemma_bron:
ggm_gemma_alternate_name:
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Sportvereniging** als directe tegenhanger.
bo_definitie: "Organisatie waarin sport wordt beoefend en die als primaire gebruiker optreedt van gemeentelijke sportaccommodaties."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Sportlocatie]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Een sportvereniging gebruikt sportlocaties"
  - type: associatie
    bedrijfsobject: "[[Sportpark]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Een sportvereniging is gevestigd op een sportpark"
bedrijfsprocessen: [Ingebruikgeving sportaccommodaties, Subsidieverlening sport, Ondersteuning sportaanbieders]
bedrijfsfuncties: [Sportbeleid, Sportaccommodatiebeheer]
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis (primaire organisatievorm voor sportbeoefening), herkenbaar, eigen bestaan (rechtspersoon), meervoud (700+ aanbieders in Utrecht, waarvan groot deel verenigingen), levenscyclus (oprichting, vitaliteitsscan, opheffing), relaties met [[Sportlocatie]], Sport. Begripstype is actor; goedgekeurd door team.

## Beschrijving

Een sportvereniging is een organisatievorm waarin sport bedreven kan worden. In Utrecht zijn sportverenigingen de primaire aanbieders naast commerciële sport- en beweegaanbieders en (urban sports) communities. De gemeente ondersteunt sportverenigingen via SportUtrecht (vitaliteitsscan, bestuurlijke ondersteuning), geeft sportaccommodaties in gebruik en verleent subsidies. Vitaliteitsuitdagingen zijn oplopende kosten, regeldruk en een tekort aan vrijwilligers en kader.

## GGM-bron

> "Organisatievorm waarin sport bedreven kan worden" (GGM, entiteit Sportvereniging, beleidsdomein Sport)

- **Entiteit:** Sportvereniging
- **Beleidsdomein:** Sport
- **Attributen:** naam, typeSport, binnensport, buitensport, email, adres, ledenaantal, aantalNormTeams
- **Matchsterkte:** exact
- **Overerving:** specialisatie van NietNatuurlijkPersoon (abstract)

## BO-definitie

De GGM-definitie wijkt inhoudelijk af van het gemeentelijke gebruik van dit begrip. De BO-definitie is gebaseerd op de bronnen.

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Sportlocatie]] | gebruikt | 0..* | GGM |
| Sport | oefent uit | 1..* | GGM |
| NietNatuurlijkPersoon (RSGB) | generaliseert | | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Sport en Bewegen/beleidsnota-sport-en-bewegen-2025-2032]]
- [[Wiki/Bronsamenvattingen/Sport en Bewegen/uitvoeringsprogramma-sport-en-bewegen-2025]]
