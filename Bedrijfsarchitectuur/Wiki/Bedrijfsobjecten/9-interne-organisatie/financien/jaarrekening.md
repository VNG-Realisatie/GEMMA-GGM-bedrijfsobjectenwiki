---
type: element
naam: Jaarrekening
onderwerp: [Financien]
archimate_type: "business-object"
grondslag: "procesobject"
ggm_entiteit:
ggm_guid:
ggm_uml_type:
ggm_beleidsdomein:
ggm_taakveld:
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie:
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:
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
bo_definitie: "Verantwoordingsdocument met het overzicht van gerealiseerde baten en lasten, de balans en de rechtmatigheidsverantwoording over een begrotingsjaar."
bo_toelichting: "Onderdeel van de jaarstukken (BBV art. 24). Pendant van de Begroting: de begroting raamt, de jaarrekening verantwoordt."
bo_subtypes: []
bo_synoniemen:
  - naam: "Jaarstukken"
    context: "BBV — jaarstukken = jaarverslag + jaarrekening"
bo_homoniemen: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Begroting]]"
    richting: bidirectioneel
    kardinaliteit: "1..1"
    beschrijving: "Jaarrekening verantwoordt de realisatie ten opzichte van de begroting"
  - type: associatie
    bedrijfsobject: "[[Reserve]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: "Gerealiseerde mutaties in reserves worden verantwoord"
  - type: associatie
    bedrijfsobject: "[[Financiële Voorziening]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: "Verloop voorzieningen wordt verantwoord"
  - type: associatie
    bedrijfsobject: "[[Activa]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: "Balans bevat de activa per balansdatum"
  - type: associatie
    bedrijfsobject: "[[Verbonden Partij]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: "Paragraaf verbonden partijen in het jaarverslag"
bedrijfsprocessen: [Jaarrekening, Begrotingscyclus]
bedrijfsfuncties: [Planning en control, Financieel beheer]
---

# Jaarrekening

Verantwoordingsdocument met het overzicht van gerealiseerde baten en lasten, de balans en de rechtmatigheidsverantwoording over een begrotingsjaar.

## BO-criteria toetsing

6/6 criteria: betekenisvol (wettelijk verplicht document), herkenbaar (kernproduct gemeentefinanciën), eigen bestaan (onafhankelijk van begroting), meervoud (per jaar), levenscyclus (opmaken, vaststellen, controleren, goedkeuren), relaties (begroting, reserves, voorzieningen, activa).

## Beschrijving

De jaarrekening is onderdeel van de jaarstukken (BBV art. 24) en bestaat uit:
- Overzicht van baten en lasten met toelichting (BBV art. 27-28)
- Balans met toelichting (BBV art. 30-57)
- Rechtmatigheidsverantwoording (BBV art. 58b)
- Accountantsverklaring
- Verantwoordingsinformatie specifieke uitkeringen

De jaarrekening is de pendant van de [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/begroting|Begroting]]: de begroting raamt, de jaarrekening verantwoordt. De indeling is identiek (BBV art. 4).

## Procesbron

Uit het verantwoordingsproces. Het college stelt de jaarstukken op, de raad stelt ze vast.

## Relaties

| Gerelateerd BO | Relatie | Bron |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/begroting\|Begroting]] | Verantwoordt de realisatie t.o.v. de begroting | BBV art. 4, 27 |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/reserve\|Reserve]] | Verantwoordt gerealiseerde mutaties in reserves | BBV art. 54 |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/financiele-voorziening\|Financiële Voorziening]] | Verantwoordt verloop voorzieningen | BBV art. 55 |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/activa\|Activa]] | Balans bevat activa per balansdatum | BBV art. 31-40 |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/verbonden-partij\|Verbonden Partij]] | Paragraaf verbonden partijen in jaarverslag | BBV art. 26 |

## Bronnen

- [[Wiki/Bronsamenvattingen/Financien/besluit-begroting-en-verantwoording]]
- [[Wiki/Bronsamenvattingen/Financien/raadgever-gemeentebegroting]]

## Terugmelding GGM

Jaarrekening ontbreekt als entiteit in het GGM-beleidsdomein Financien. De Begroting is wel gemodelleerd; de jaarrekening als pendant ontbreekt. Zie [[Wiki/Analyses/ggm-terugmeldingen]].
