---
type: bedrijfsobject
naam: MJOP
onderwerp: [Vastgoed]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: MJOP
ggm_guid: EAID_A110896B_0CAD_46cf_9226_840DEE3328F0
ggm_uml_type: Class
ggm_beleidsdomein: Vastgoed
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Vastgoed Domeinmodel]
ggm_diagram_ids: [EAID_00D4246F_6ED7_4690_A180_ACCCD6AB1291]
ggm_definitie: "Meerjaren Onderhoudsplanning"
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
  Dit BO heeft de GGM-entiteit **MJOP** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **MJOP-Item** (detail) — Detailgegeven
  - **Prijzenboekitem** (detail) — Detailgegeven (weinig attributen)
bo_definitie: "Dynamisch planningsdocument per vastgoedobject dat het verwachte onderhoud over een periode van 15 jaar beschrijft, gevoed door inspecties."
bo_toelichting: ''
bo_subtypes: []
bo_via_kandidaten:
  - ggm_entiteit: "Prijzenboekitem"
    ggm_guid: "EAID_697512E4_0C8E_4be8_8E95_9E2E4BD50F85"
    reden: "Prijzenboekitems worden gebruikt om onderhoud in het MJOP te begroten."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Vastgoedobject]]"
    richting: naar-dit-BO
    kardinaliteit: "1..1"
    beschrijving: "Een MJOP betreft een vastgoedobject"
  - type: associatie
    bedrijfsobject: "[[Inspectie]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Een inspectie leidt tot een MJOP"
  - type: associatie
    bedrijfsobject: "[[Werkbon]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een MJOP wordt gerealiseerd door werkbonnen"
bedrijfsprocessen: [planmatig onderhoud vastgoed, verduurzaming vastgoedportefeuille]
bedrijfsfuncties: [gebouwbeheer, vastgoedmanagement]
---

## BO-criteria toetsing

1. **Heeft betekenis** — kerninstrument van planmatig vastgoedbeheer
2. **Herkenbaar** — elke vastgoedbeheerder kent de MJOP als sturend document
3. **Eigen bestaan** — een MJOP bestaat per vastgoedobject, onafhankelijk van individuele werkbonnen
4. **Meervoud** — elk gebouw heeft een eigen MJOP
5. **Levenscyclus** — opgesteld na inspectie → jaarlijks bijgesteld → hernieuwd na 15 jaar
6. **Relaties** — naar [[Vastgoedobject]], [[Inspectie]], [[Werkbon]]

## Beschrijving

De Meerjaren Onderhoudsplanning (MJOP) is het centrale planningsinstrument voor het onderhoud van een [[Vastgoedobject]]. Het beschrijft het verwachte onderhoud over een periode van 15 jaar en wordt jaarlijks bijgesteld op basis van nieuwe [[Inspectie]]-resultaten. De MJOP bestaat uit MJOP-items die elk een onderhoudsmaatregel beschrijven, gekoppeld aan een bouwdeel en een kostenraming.

Het onderscheid tussen klein onderhoud (dagelijkse reparaties), groot onderhoud (ingrijpend, cyclisch) en investeringen (kwaliteitsverbetering, wettelijke eisen) bepaalt de financiering: klein onderhoud uit de beheerbegroting, groot onderhoud uit de egalisatiereserve, investeringen via afzonderlijke aanvragen.

> "De MJOP is gebaseerd op het verwachtte onderhoud over een periode van 15 jaar en wordt jaarlijks op basis van beschikbaar komende inspecties bijgesteld. Hiermee wordt het MJOP een dynamisch plan dat jaarlijks geactualiseerd wordt." (bron: Beleidsplan Vastgoed Hulst)

## GGM-componenten

GGM-entiteiten die onderdeel zijn van MJOP. Gemodelleerd als aparte entiteiten in het GGM maar vormen geen zelfstandig bedrijfsobject.

- **MJOP-Item** — individuele onderhoudsmaatregel binnen een MJOP; legt code, omschrijving, kosten, start-/einddatum en opzegtermijnen vast; gekoppeld aan bouwdeel en prijzenboekitem
- **Prijzenboekitem** — onderdeel van een prijzenboek; legt verrichting, prijs en geldigheidsdatum vast; basis voor kostenraming MJOP-items

## GGM-bron

> Meerjaren Onderhoudsplanning

- **Entiteit:** MJOP
- **Beleidsdomein:** Vastgoed
- **Attributen:** datum, omschrijving
- **Matchsterkte:** exact

## BO-definitie

De GGM-definitie wijkt inhoudelijk af van het gemeentelijke gebruik van dit begrip. De BO-definitie is gebaseerd op de bronnen.

## Relaties

| Relatie | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedobject\|Vastgoedobject]] | naar-dit-BO | 1..1 | Een MJOP betreft een vastgoedobject | GGM |
| [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/inspectie\|Inspectie]] | naar-dit-BO | 0..1 | Een inspectie leidt tot een MJOP | GGM |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/werkbon\|Werkbon]] | van-dit-BO | 0..* | Gerealiseerd door werkbonnen | GGM |

## Bedrijfsprocessen

- Planmatig onderhoud van gemeentelijk vastgoed
- Begrotingsopstelling onderhoud (egalisatiereserve)
- Verduurzaming vastgoedportefeuille
- Jaarlijkse bijstelling op basis van inspecties

## Bronnen

- [[Wiki/Bronsamenvattingen/Vastgoed/beleidsplan-vastgoed-hulst]]
- [[Wiki/Bronsamenvattingen/Vastgoed/vastgoedstrategie-amsterdam]]
