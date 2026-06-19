---
type: bedrijfsobject
naam: Debiteur
domein: [Financien, Terug-en-invordering]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Debiteur
ggm_beleidsdomein: Financien, Terug-en-invordering
definitie: Persoon die een bedrag verschuldigd is aan de gemeente
gerelateerde_begrippen: [belastingplichtige]
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
