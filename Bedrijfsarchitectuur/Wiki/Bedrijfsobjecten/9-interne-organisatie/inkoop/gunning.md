---
type: element
naam: Gunning
onderwerp: [inkoop]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Gunning
ggm_guid: EAID_3FB9B466_D147_42d7_99D1_2D14A007D16C
ggm_uml_type: Class
ggm_beleidsdomein: Inkoop
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Diagram Inkoop Inhuur, Diagram Inkoop Geen Inhuur]
ggm_diagram_ids: [EAID_1172FBF0_04B4_46c7_9FB5_F34730E060FB, EAID_6683520C_EE21_4038_A418_D4C957172DF2]
ggm_definitie: "Gunning van een (enkel of meervoudige) onderhandse aanbesteding, of een nationale of Europese aanbesteding Of voor levering personeel"
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
  Dit BO heeft de GGM-entiteit **Gunning** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Aanbesteding Inhuur** (detail) — Detailgegeven
bo_definitie: "Formeel besluit waarmee de gemeente een opdracht toewijst aan een ondernemer op basis van een aanbestedingsprocedure."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Aanbesteding]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "voortgekomen uit"
  - type: associatie
    bedrijfsobject: "[[Offerte]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "betreft"
  - type: associatie
    bedrijfsobject: "[[Aanbieding]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "betreft"
bedrijfsprocessen: [Selecteren, Contracteren]
bedrijfsfuncties: [Inkoopfunctie]
---

## BO-criteria toetsing

1. **Heeft betekenis binnen het onderwerp** — ja, het moment van toewijzing van een opdracht
2. **Is herkenbaar voor domeinexperts** — ja, inkopers en juristen kennen gunning als formeel besluit
3. **Heeft een eigen bestaan** — ja, gunning is een apart vastgelegd besluit met eigen datum en publicatie
4. **Kan in meervoud bestaan** — ja, elke aanbesteding kan een gunning opleveren
5. **Heeft een eigen levenscyclus** — ja: voornemen → standstill → definitieve gunning → publicatie
6. **Heeft relaties met andere concepten** — ja: Aanbesteding, Offerte, Inschrijving

Score: 6/6

## Beschrijving

Een gunning is het formele besluit waarmee de gemeente een opdracht toewijst aan de winnende ondernemer. Bij nationale en Europese aanbestedingen geldt een publicatieplicht en een standstill-termijn (Alcateltermijn) tussen het voornemen tot gunning en de definitieve gunning.

Gunning geschiedt standaard op basis van beste prijs-kwaliteitverhouding (BPKV), met uitzonderingen voor laagste prijs of laagste kosten op basis van levenscycluskosten.

## GGM-bron

> "Gunning van een (enkel of meervoudige) onderhandse aanbesteding, of een nationale of Europese aanbesteding Of voor levering personeel" (GGM, beleidsdomein Inkoop)

**Matchsterkte:** exact — GGM-entiteit en BO zijn hetzelfde concept.

**Attributen:** datumGunning, bericht, datumVoorlopigeGunning, gegundePrijs, datumPublicatie

## BO-definitie

De GGM-definitie wijkt inhoudelijk af van het gemeentelijke gebruik van dit begrip. De BO-definitie is gebaseerd op de bronnen.

## Relaties

| Gerelateerd BO | Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Aanbesteding\|Aanbesteding]] | voortgekomen uit | ← | 0..1 | GGM |
| [[Offerte\|Offerte]] | betreft | ← | 0..1 | GGM |
| [[Aanbieding\|Aanbieding]] | betreft | ← | 0..1 | GGM |

## Bedrijfsprocessen

- **Selecteren** — beoordelen en rangschikken, voornemen tot gunning
- **Contracteren** — definitieve gunning leidt tot contractondertekening

## Bedrijfsfuncties

- **Inkoopfunctie** — gunningsbesluit nemen

## Bronnen

- [[Wiki/Bronsamenvattingen/Inkoop/inkoop-en-aanbestedingsbeleid]]
