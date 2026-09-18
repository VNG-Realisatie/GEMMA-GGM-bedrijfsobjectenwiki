---
type: element
naam: Aanbesteding
onderwerp: [inkoop]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Aanbesteding
ggm_guid: EAID_44EC6082_2682_43c7_A52E_0AD05B06A046
ggm_uml_type: Class
ggm_beleidsdomein: Inkoop
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Vastgoed Leveranciers, Diagram Inkoop Geen Inhuur]
ggm_diagram_ids: [EAID_06E44472_8C2A_40eb_9965_DCF91A1322C9, EAID_6683520C_EE21_4038_A418_D4C957172DF2]
ggm_definitie: "Kan een (enkel of meervoudige) onderhandse aanbesteding, of een nationale of Europese aanbesteding"
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

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Aanbesteding** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Aanbesteding Vastgoed** (detail) — Detailgegeven (geassocieerd met BO)
  - **Aankondiging** (detail) — GGM-component van Aanbesteding
  - **Kwalificatie** (detail) — Detailgegeven (geassocieerd met BO)
  - **Offerteaanvraag** (detail) — GGM-component van Aanbesteding
  - **SelectietabelAanbesteding** (detail) — Detailgegeven
  - **StartformulierAanbesteden** (detail) — Detailgegeven
bo_definitie: "Procedure waarmee de gemeente een opdracht voor werken, leveringen of diensten in de markt zet en gunt aan een ondernemer."
bo_toelichting:
bo_via_kandidaten:
  - ggm_entiteit: "Kwalificatie"
    ggm_guid: "EAID_AB2AED85_D2B0_45cf_9B1F_C6005E894494"
    reden: "Kwalificatie voor een nationale of Europese aanbesteding — expliciet in de GGM-definitie."
  - ggm_entiteit: "Offerteaanvraag"
    ggm_guid: "EAID_1EF1AC66_9563_4cdd_AE78_0878D651907A"
    reden: "Een offerteaanvraag is een aanbesteding bij inschrijving — expliciet in de GGM-definitie."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Gunning]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "mondt uit in"
  - type: associatie
    bedrijfsobject: "[[Offerte]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "ontvangt offertes"
  - type: associatie
    bedrijfsobject: "[[Aanbieding]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "ontvangt inschrijvingen"
  - type: associatie
    bedrijfsobject: "[[Inkooppakket]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "valt onder"
  - type: associatie
    bedrijfsobject: "[[Marktconsultatie]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "voorafgegaan door"
  - type: associatie
    bedrijfsobject: "[[Contract]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "leidt tot"
bedrijfsprocessen: [Inkopen, Aanbesteden, Contracteren]
bedrijfsfuncties: [Inkoopfunctie]
---

## BO-criteria toetsing

1. **Heeft betekenis binnen het onderwerp** — ja, centraal concept in gemeentelijke inkoop
2. **Is herkenbaar voor domeinexperts** — ja, kernproces voor inkopers en budgethouders
3. **Heeft een eigen bestaan** — ja, onafhankelijk van gunning of contract
4. **Kan in meervoud bestaan** — ja, gemeente voert meerdere aanbestedingen per jaar uit
5. **Heeft een eigen levenscyclus** — ja: voorbereiding → publicatie → beoordeling → gunning → afronding
6. **Heeft relaties met andere concepten** — ja: Gunning, Offerte, Inschrijving, Leverancier, Contract

Score: 6/6

## Beschrijving

Een aanbesteding is de procedure waarmee de gemeente een opdracht in de markt zet. Ondernemers kunnen daarop reageren door een offerte of inschrijving in te dienen. De keuze van aanbestedingsprocedure hangt af van de opdrachtwaarde en het type opdracht (werken, leveringen of diensten).

Gemeenten onderscheiden vier typen procedures:
- **Enkelvoudig onderhands** — de gemeente vraagt één ondernemer een offerte (onder de laagste drempel)
- **Meervoudig onderhands** — de gemeente vraagt 3-5 ondernemers een offerte
- **Nationaal openbaar** — alle ondernemers kunnen inschrijven via TenderNed
- **Europees openbaar** — verplicht boven de Europese drempelbedragen

## Subtypes

Herkende specialisaties van Aanbesteding. Gevonden in bronnen en/of GGM. Geen apart BO.

- **Aanbesteding Inhuur** — specialisatie voor inhuur van personen of diensten; eigen attributen (aanvraagnummer, hoogste/laagste tarief, perceel)

## GGM-componenten

GGM-entiteiten die onderdeel zijn van Aanbesteding. Gemodelleerd als aparte entiteiten in het GGM maar vormen geen zelfstandig bedrijfsobject.

- **Aankondiging** — publicatie van de aanbesteding op TenderNed of de gemeentelijke website
- **Offerteaanvraag** — uitvraagdocument gericht aan leveranciers
- **StartformulierAanbesteden** — intern formulier waarmee een aanbesteding wordt geïnitieerd
- **SelectietabelAanbesteding** — configuratietabel met drempelbedragen en bijbehorende procedures
- **Kwalificatie** — geschiktheidsverklaring van een leverancier voor deelname

## GGM-bron

> "Kan een (enkel of meervoudige) onderhandse aanbesteding, of een nationale of Europese aanbesteding" (GGM, beleidsdomein Inkoop)

**Matchsterkte:** exact — GGM-entiteit en BO zijn hetzelfde concept.

**Attributen:** naam, tendernedKenmerk, status, datumStart, volgendeSluiting, type, procedure, digitaal, referentienummer, datumPublicatie, scoreMaximaal

## BO-definitie

De GGM-definitie wijkt inhoudelijk af van het gemeentelijke gebruik van dit begrip. De BO-definitie is gebaseerd op de bronnen.

## Relaties

| Gerelateerd BO | Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Gunning\|Gunning]] | mondt uit in | → | 0..1 | GGM |
| [[Offerte\|Offerte]] | ontvangt | ← | 0..* | GGM |
| [[Aanbieding\|Aanbieding]] | ontvangt | ← | 0..* | GGM |
| [[Inkooppakket\|Inkooppakket]] | valt onder | ← | 0..1 | GGM |
| [[Marktconsultatie\|Marktconsultatie]] | voorafgegaan door | ← | 0..1 | bronnen |
| [[Contract\|Contract]] | leidt tot | → | 0..1 | bronnen |

## Bedrijfsprocessen

- **Inkopen** — het volledige inkoopproces (7 fasen)
- **Aanbesteden** — het in de markt zetten van een opdracht
- **Selecteren** — beoordelen en rangschikken van inschrijvingen/offertes

## Bedrijfsfuncties

- **Inkoopfunctie** — organisatie van inkoop (centraal, decentraal of gecoördineerd)

## Bronnen

- [[Wiki/Bronsamenvattingen/Inkoop/inkoop-en-aanbestedingsbeleid]]
