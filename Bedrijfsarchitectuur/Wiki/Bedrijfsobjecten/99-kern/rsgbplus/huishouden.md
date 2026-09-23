---
type: element
naam: Huishouden
onderwerp: [Basisregistraties, RSGBPlus]
archimate_type: business-object
grondslag: ggm-entiteit

# GGM-velden
ggm_entiteit: Huishouden
ggm_guid: EAID_6FB0A5B7_7B5F_437f_A462_4B1EADB964E4
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram:
  - "(Zaak)objecten"
  - "Kern:Personen"
  - "Huishouden en Huwelijk"
ggm_diagram_ids: []
ggm_definitie: "Een duurzame samenlevingsvorm van een of meer natuurlijke personen binnen een VERBLIJFSOBJECT, STANDPLAATS of LIGPLAATS."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

# GEMMA-waarden
ggm_gemma_naam: Huishouden
ggm_gemma_guid: "2515abf4-dea2-44eb-8886-c90c1ab42069"
ggm_gemma_definitie: "Een duurzame samenlevingsvorm van een of meer natuurlijke personen binnen een VERBLIJFSOBJECT, STANDPLAATS of LIGPLAATS."
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-2515abf4-dea2-44eb-8886-c90c1ab42069"
ggm_gemma_bron:
ggm_gemma_alternate_name: "Huishouden (RSGB Model)"

ggm_duplicaat_entiteiten:
  - entiteit: Huishouden
    guid: EAID_F0467610_553B_47cd_A9F7_3B1D20CC425E
    beleidsdomein: Sociaal Domein Generiek
    taakveld: "6 Sociaal Domein"
    afwijkende_attributen: "Sociaal Domein Generiek-variant is dunner (1 attribuut: soort) en proces-specifiek (bijstand/schuldhulp-context); RSGBPlus is de rijkere, canonieke bron (huishoudensoort/-nummer/-grootte/geldigheid)"

analyse_ggm_dekking: ""
bo_definitie: "Duurzame samenlevingsvorm van een of meer natuurlijke personen binnen één verblijfsobject, standplaats of ligplaats."
bo_toelichting: "Institutioneel huishouden (verpleeg-/bejaardentehuis, gevangenis, >1 jaar verblijf) of particulier huishouden (personen die alleen of samen in een woonruimte zijn gehuisvest en zelf in hun dagelijks onderhoud voorzien). Bewust los gemodelleerd van de verblijfsrelaties van Ingeschreven Persoon op adresseerbare objecten: huishouden is geen verplicht gegeven, bij wijziging van verblijfsrelaties is de nieuwe huishoudensamenstelling niet altijd direct bekend, en de verblijfsrelatie zelf maakt deel uit van het basisregistratiestelsel (Ingeschreven Persoon/BRP) en is een van de meest gevraagde relaties."
bo_subtypes:
  - naam: Institutioneel huishouden
    omschrijving: "Personen die langer dan een jaar in een instelling verblijven (verpleeg-, bejaarden-, kindertehuis, opvoedingsinternaat, revalidatiecentrum, gevangenis)"
    ggm_entiteit: Huishouden
    ggm_guid: EAID_6FB0A5B7_7B5F_437f_A462_4B1EADB964E4
    ggm_attribuut: huishoudensoort
  - naam: Particulier huishouden
    omschrijving: "Een of meer personen die alleen of samen in een woonruimte zijn gehuisvest en zelf in hun dagelijks onderhoud voorzien"
    ggm_entiteit: Huishouden
    ggm_guid: EAID_6FB0A5B7_7B5F_437f_A462_4B1EADB964E4
    ggm_attribuut: huishoudensoort
bo_via_kandidaten: []
bo_synoniemen: []
bo_homoniemen: []
element_tegenhangers: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/bag/verblijfsobject|Verblijfsobject]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Is gehuisvest in een verblijfsobject, standplaats of ligplaats"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon|Ingeschreven Persoon]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Heeft leden, elk met een eigen positie in het huishouden (zie [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/huishoudenlid|Huishoudenlid]])"
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

| Criterium | Oordeel |
|---|---|
| Heeft betekenis binnen het onderwerp | ✅ Kernbegrip voor bijstand, huursubsidie, woningbehoefte en WOZ-objectafbakening |
| Herkenbaar voor domeinexperts | ✅ Burgerzaken/sociaal domein spreken dagelijks over huishoudens en huishoudensamenstelling |
| Heeft een eigen bestaan binnen het onderwerp | ✅ Bestaat los van de individuele leden en los van het verblijfsobject |
| Kan in meervoud bestaan | ✅ Elk verblijfsobject/standplaats/ligplaats kan een eigen huishouden hebben |
| Heeft een eigen levenscyclus | ✅ Datum begin/einde geldigheid huishouden |
| Heeft relaties met andere concepten | ✅ Verblijfsobject, Ingeschreven Persoon (via Huishoudenlid) |

6/6 — sterke BO.

## Beschrijving

Een Huishouden is de feitelijke leefvorm van een of meer natuurlijke personen binnen één verblijfsobject, standplaats of ligplaats — onderscheiden in institutionele huishoudens (langdurig verblijf in een instelling) en particuliere huishoudens (zelfstandige huisvesting met eigen dagelijks onderhoud). Het begrip is relevant voor beleidsvelden als bijstand, huursubsidie en woningbehoefteonderzoek, die elk een eigen concretisering van "duurzaamheid" kunnen hanteren.

RSGB modelleert Huishouden bewust **naast** de verblijfsrelaties van Ingeschreven Persoon op adresseerbare objecten (die al deel uitmaken van het basisregistratiestelsel): huishouden is geen verplicht gegeven, bij een wijziging van verblijfsrelaties is de nieuwe huishoudensamenstelling niet altijd direct bekend, en de verblijfsrelatie is zelf een van de meest gevraagde BRP-relaties. Beide bestaan dus naast elkaar met een eigen doel.

## GGM-duplicaten

De GGM-entiteitnaam "Huishouden" komt voor in 2 beleidsdomeinen:

| Beleidsdomein | GUID | Status |
|---|---|---|
| **RSGBPlus** | `EAID_6FB0A5B7_7B5F_437f_A462_4B1EADB964E4` | **primair** — rijkere, canonieke bron (7 attributen: huishoudensoort, -nummer, -grootte, geldigheid) |
| Sociaal Domein Generiek | `EAID_F0467610_553B_47cd_A9F7_3B1D20CC425E` | duplicaat — dunner (1 attribuut), proces-specifiek gebruik binnen bijstand/schuldhulp |

Beide vertegenwoordigen hetzelfde concept; RSGBPlus is als canonieke mapping gekozen omdat het de volledige gegevensdefinitie draagt.

## GGM-bron

> "Een duurzame samenlevingsvorm van een of meer natuurlijke personen binnen een VERBLIJFSOBJECT, STANDPLAATS of LIGPLAATS."

- **Entiteit:** Huishouden
- **Package:** RSGB Model > Model Kern RSGB
- **Attributen:** huishoudensoort, huishoudennummer, huishoudengrootte, datumBeginGeldigheidHuishouden, datumEindeGeldigheidHuishouden
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | BO | Beschrijving | Bron |
|---|---|---|---|---|
| is gehuisvest in | → | [[Wiki/Bedrijfsobjecten/99-kern/bag/verblijfsobject\|Verblijfsobject]] | Ook ligplaats/standplaats mogelijk | GGM |
| heeft leden | ← | [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | Via [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/huishoudenlid\|Huishoudenlid]], dat de rol (hoofd/partner/kind/overig lid) draagt | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/rsgb-deel-ii-specificaties]]
