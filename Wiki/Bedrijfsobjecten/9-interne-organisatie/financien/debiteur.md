---
type: bedrijfsobject
naam: Debiteur
domein: [Financien, Terug-en-invordering]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Debiteur"
ggm_guid: EAID_E74D0D46_66EB_4deb_A540_7AB08E95F956
ggm_uml_type: Class
ggm_beleidsdomein: "Financien"
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: []
ggm_diagram_ids: [EAPK_4F010A09_D9D0_4bcf_A233_8430F8EFE54A]
ggm_definitie: "Iemand aan wie een dienst of product geleverd is waardoor recht op een vergoeding is ontstaan"
ggm_toelichting: ""
ggm_synoniemen: "Schuldenaar"
ggm_herkomst: ""
ggm_gemma_naam: "Debiteur"
ggm_gemma_guid: "e21e51ee-3a32-444b-80c7-b6694ff37253"
ggm_gemma_definitie: "Iemand aan wie een dienst of product geleverd is waardoor recht op een vergoeding is ontstaan"
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: "Schuldenaar"
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-e21e51ee-3a32-444b-80c7-b6694ff37253"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: ""
definitie: Persoon die een bedrag verschuldigd is aan de gemeente
bronnen: ["Bronsamenvattingen/Financien/raadgever-gemeentebegroting.md", "Bronsamenvattingen/Financien/raadgever-inkomstenbronnen.md"]
bedrijfsprocessen: [Facturering, Debiteurenadministratie, Invordering]
bedrijfsfuncties: [Financieel beheer, Inning en invordering]
status: concept
---

# Debiteur

Persoon die een bedrag verschuldigd is aan de gemeente. Het GGM definieert Debiteur in twee beleidsdomeinen met verschillende accenten.

## GGM-bron

**Financien (taakveld 9):**
> Iemand aan wie een dienst of product geleverd is waardoor recht op een vergoeding is ontstaan.

- **Attributen:** *(geen)*

**Terug-en-invordering (taakveld 6 → Sociaal Domein → Inkomen):**
> Binnen het domein van terug- en invorderen is een debiteur een persoon waarop de gemeente een of meerdere vorderingen heeft.

- **Attributen:** Eigen kenmerk, Opvoerdatum, Soort debiteur

**Verschil:** Financien benadrukt het privaatrechtelijke aspect (dienst geleverd → recht op betaling). T&I benadrukt het publiekrechtelijke aspect (openstaande vorderingen).

## Bo-definitie (afwijkend)

De bedrijfsobjectdefinitie is breder dan beide GGM-definities: "Persoon die een bedrag verschuldigd is aan de gemeente" dekt zowel de privaatrechtelijke als de publiekrechtelijke context.

## Bedrijfsprocessen

- **Facturering** — debiteur als ontvanger van facturen
- **Debiteurenadministratie** — beheer van openstaande posten
- **Invordering** — debiteur als persoon met openstaande vorderingen

## Bedrijfsfuncties

- **Financieel beheer** — debiteurenregistratie
- **Inning en invordering** — vorderingenbeheer

## Relaties

- Ontvangt [[factuur]]en (privaatrechtelijk)
- Heeft [[vordering]]en (publiekrechtelijk/sociaal domein)
- Verwant aan [[belastingplichtige]] — maar een belastingplichtige is specifiek iemand met een wettelijke belastingplicht, terwijl een debiteur breder is (ook dienstverlening)
- Kan een [[aflossingsplan]] hebben
- Kan in aanmerking komen voor [[kwijtschelding]]
