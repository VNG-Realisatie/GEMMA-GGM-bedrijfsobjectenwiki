---
type: element
naam: Contract
onderwerp: [inkoop]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Contract
ggm_guid: EAID_9FBF9FB8_B28D_4733_8443_607B8498F446
ggm_uml_type: Class
ggm_beleidsdomein: Inkoop
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Sociaal Domein Beschikking en Voorziening: Domain Objects, Financien Verplichtingen en Facturen, Diagram Verlengen Inhuur, Diagram Inkoop Inhuur, Diagram Inkoop Geen Inhuur]
ggm_diagram_ids: [EAID_5AE29494_3572_4924_B2B8_3206E55D71BB, EAID_0723EB5C_4A2C_44d4_B15B_37AC71B5D711, EAID_21AD192F_EEF1_493b_9BFD_D37EF6C93236, EAID_1172FBF0_04B4_46c7_9FB5_F34730E060FB, EAID_6683520C_EE21_4038_A418_D4C957172DF2]
ggm_definitie: "Bindende overeenkomst"
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
  Dit BO heeft de GGM-entiteit **Contract** als directe tegenhanger.
bo_definitie: "Bindende overeenkomst"
bo_toelichting: ''
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Leverancier]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "contractant"
  - type: associatie
    bedrijfsobject: "[[Aanbesteding]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "voortgekomen uit"
  - type: associatie
    bedrijfsobject: "[[Contract]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "bovenliggend contract"
bedrijfsprocessen: [Contracteren, Bewaken, Nazorg]
bedrijfsfuncties: [Inkoopfunctie, Contractmanagement]
---

## BO-criteria toetsing

1. **Heeft betekenis binnen het onderwerp** — ja, het resultaat van het inkoopproces
2. **Is herkenbaar voor domeinexperts** — ja, kernconcept voor contractmanagers en budgethouders
3. **Heeft een eigen bestaan** — ja, blijft bestaan onafhankelijk van de aanbesteding die eraan voorafging
4. **Kan in meervoud bestaan** — ja, gemeente beheert honderden contracten
5. **Heeft een eigen levenscyclus** — ja: ondertekening → uitvoering → verlenging/wijziging → beëindiging
6. **Heeft relaties met andere concepten** — ja: Leverancier, Aanbesteding, financiële verplichtingen

Score: 6/6

## Beschrijving

Een contract is de bindende overeenkomst die de gemeente sluit met een leverancier na gunning van een opdracht. Het contract legt vast wat wordt geleverd, tegen welke voorwaarden en prijs, en voor welke periode.

Contractbeheer omvat vier rollen: contracteigenaar (bestuurlijk verantwoordelijk), contractmanager (operationeel verantwoordelijk), contractgebruiker (dagelijks gebruik) en contractbeheerder (administratief). De intensiteit van contractmanagement hangt af van omvang en risico/impact.

Contracten kunnen hiërarchisch zijn: een raamovereenkomst kan deelcontracten of nadere overeenkomsten bevatten.

## GGM-componenten

GGM-entiteiten die onderdeel zijn van Contract. Gemodelleerd als aparte entiteiten in het GGM maar vormen geen zelfstandig bedrijfsobject.

- **Aanvraag Inkooporder** — intern bestelformulier voor het plaatsen van een bestelling binnen een bestaand contract

## GGM-bron

> "Bindende overeenkomst" (GGM, beleidsdomein Inkoop)

**Matchsterkte:** exact — GGM-entiteit en BO zijn hetzelfde concept. De GGM-definitie is minimaal maar klopt.

**Attributen:** contractRevisie, internContractID, internContractRevisie, status, groep, type, categorie, classificatie, voorwaarde, beschrijving, zoekwoorden, autorisatiegroep, opmerkingen, datumStart, datumEinde, datumCreatie

Het contract verschijnt op 5 GGM-diagrammen (Inkoop, Sociaal Domein, Financiën, Inhuur), wat de domeindoorsnijdende aard bevestigt.

## Relaties

| Gerelateerd BO | Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Leverancier\|Leverancier]] | contractant | ← | 1 | GGM |
| [[Aanbesteding\|Aanbesteding]] | voortgekomen uit | ← | 0..1 | bronnen |
| [[Contract\|Contract]] | bovenliggend contract | ← | 0..1 | GGM |

## Bedrijfsprocessen

- **Contracteren** — tekenen overeenkomst, registreren, informeren afgewezen ondernemers
- **Bewaken** — termijnen, prestaties, MVOI-afspraken, factuurbetaling
- **Nazorg** — beheer (prijsindexering, looptijd), evaluatie

## Bedrijfsfuncties

- **Inkoopfunctie** — afsluiten contracten
- **Contractmanagement** — bewaken en beheren van lopende contracten

## Bronnen

- [[Wiki/Bronsamenvattingen/Inkoop/inkoop-en-aanbestedingsbeleid]]
