---
type: element
naam: Sportpark
onderwerp: [Sport en Bewegen]
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
ggm_toelichting:
ggm_synoniemen: "Sportterrein"
ggm_herkomst:
ggm_gemma_naam: "Sportpark"
ggm_gemma_guid: "ca9df4ee-92e1-4c24-ace3-467d146a320e"
ggm_gemma_definitie: "Geheel van terreinen, gebouwen en voorzieningen voor verschillende takken van sport."
ggm_gemma_toelichting:
ggm_gemma_synoniemen: "Sportterrein"
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-ca9df4ee-92e1-4c24-ace3-467d146a320e"
ggm_gemma_bron:
ggm_gemma_alternate_name:
ggm_duplicaat_entiteiten:
  - entiteit: Sportterrein
    guid: EAID_A5A43927_9633_4584_865B_78AE4486E5B
    beleidsdomein: Beheer Openbare Ruimte
    taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
    afwijkende_attributen: "Sportterrein (Model IMBOR) heeft eigen attributen (drainage, gebruiksvorm, sportcomplex, sportterreinTypeSport, veldnummer, verlicht) die Sportpark niet heeft; ter discussie of dit conceptueel dichter bij Veld ligt dan bij Sportpark — zie terugmelding #92"
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Sportpark** als directe tegenhanger. Daarnaast is **Sportterrein** (beleidsdomein Beheer Openbare Ruimte) als vermoedelijk duplicaat gekoppeld — zie ggm_duplicaat_entiteiten.
bo_definitie: "Geheel van terreinen, gebouwen en voorzieningen voor verschillende takken van sport."
bo_toelichting:
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Sportlocatie]]"
    richting: "naar-dit-BO"
    kardinaliteit:
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

## GGM-duplicaten

De GGM-entiteit "Sportterrein" (taakveld 8, beleidsdomein Beheer Openbare Ruimte, Model IMBOR) representeert vermoedelijk hetzelfde concept als Sportpark:

| Beleidsdomein | GUID | Status |
|---|---|---|
| **Sport** (taakveld 5) | `EAID_FE1A2EF2_44FA_46fa_A583_7BAB858E17FD` | **primair** — gekozen omdat de definitie ("geheel van terreinen, gebouwen en voorzieningen") het beleidsniveau dekt waarop de gemeente sportparken bespreekt, en omdat Sportpark zelf "Sportterrein" als GGM-synoniem noemt |
| Beheer Openbare Ruimte (taakveld 8) | `EAID_A5A43927_9633_4584_865B_78AE4486E5B` | duplicaat — heeft eigen IMBOR-attributen (drainage, gebruiksvorm, sportcomplex, sportterreinTypeSport, veldnummer, verlicht) die Sportpark niet heeft |

De attributen `veldnummer` en `sportcomplex` op Sportterrein wijzen mogelijk eerder op het individuele-veld-niveau dan op het complex-niveau — Sportterrein zou dan conceptueel dichter bij [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/sport/veld\|Veld]] liggen (dat als compositie-onderdeel van Sportpark is gemodelleerd). GGM's eigen synoniemtags zijn hier inconsistent: Sportpark → synoniem "Sportterrein", maar Sportterrein zelf → synoniem "Sportveld". Dit is **ter discussie**; niet gegokt maar teruggemeld.

Teruggemeld als #92 in [[Wiki/Analyses/ggm-terugmeldingen]].

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Sportlocatie]] | generaliseert | | GGM |
| [[Veld]] | bevat | 0..* | GGM |
| [[Sportvereniging]] | wordt gebruikt door | 0..* | GGM |
| [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/overig-terrein\|Overig Terrein]] | ligt op | 1 | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Sport en Bewegen/beleidsnota-sport-en-bewegen-2025-2032]]
- [[Wiki/Bronsamenvattingen/Sport en Bewegen/uitvoeringsprogramma-sport-en-bewegen-2025]]
