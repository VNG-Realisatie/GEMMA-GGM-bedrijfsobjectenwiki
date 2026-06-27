---
type: bedrijfsobject
naam: Infectieziektemelding
onderwerp: [openbare gezondheid]
archimate_type: business-object
grondslag: procesobject

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

bo_definitie: "Melding van een (vermoedelijke) meldingsplichtige infectieziekte conform de Wet publieke gezondheid, die bij de GGD wordt afgehandeld namens de gemeente."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[NatuurlijkPersoon]]"
    richting: van-dit-BO
    kardinaliteit: "1 → 1"
    beschrijving: "De index (patiënt) op wie de melding betrekking heeft"
bedrijfsprocessen: [infectieziektebestrijding, bron- en contactonderzoek, outbreak management]
bedrijfsfuncties: [volksgezondheid]
---

## BO-criteria toetsing

| # | Criterium | Toepassing |
|---|---|---|
| 1 | Betekenis binnen onderwerp | Kern van de infectieziektebestrijding; wettelijke meldingsplicht Wpg |
| 2 | Herkenbaar voor domeinexperts | Standaardbegrip bij GGD en volksgezondheid |
| 3 | Eigen bestaan | Elke melding is een zelfstandig geval |
| 4 | Meervoud | Duizenden per jaar per GGD-regio |
| 5 | Eigen levenscyclus | Melding → verificatie → BCO → bestrijdingsmaatregelen → afsluiting |
| 6 | Relaties | Index (persoon), verwekker, instelling, bestrijdingsmaatregelen |

Score: 6/6.

## Beschrijving

Artsen en laboratoria zijn op grond van de Wet publieke gezondheid verplicht bepaalde infectieziekten te melden bij de GGD. De GGD voert de infectieziektebestrijding uit namens de gemeente. Elke melding doorloopt een vaststaand proces: verificatie, bron- en contactonderzoek (BCO), bepalen en inzetten van bestrijdingsmaatregelen, en afsluiting.

Meldingsplichtige ziekten zijn ingedeeld in groepen met verschillende bevoegdheden:
- **Groep A** — direct melden aan RIVM en burgemeester; isolatie en quarantaine mogelijk
- **Groep B1/B2** — melden aan GGD; BCO en bestrijdingsmaatregelen
- **Groep C** — melden aan GGD; monitoring en advisering

De gemeente is wettelijk verantwoordelijk maar de uitvoering ligt volledig bij de GGD. Dit maakt de infectieziektemelding het primaire raakvlak tussen meldingsplicht en gemeentelijke verantwoordelijkheid.

## Subtypes

Herkende specialisaties van infectieziektemelding. Gevonden in bronnen. Geen apart BO.

- **A-ziektemelding** — melding van een A-ziekte (bijv. pokken, pest, virale hemorragische koorts); direct aan RIVM en burgemeester
- **B-ziektemelding** — melding van een B1- of B2-ziekte (bijv. tuberculose, kinkhoest, legionellose); aan GGD
- **C-ziektemelding** — melding van een C-ziekte (bijv. malaria, hepatitis B); aan GGD
- **Art. 26-melding** — melding van een uitbraak in een instelling (bijv. verpleeghuis, kinderopvang)

## Procesbron

Wettelijke basis: Wet publieke gezondheid (Wpg), met name de meldingsplicht voor artsen (art. 21-24) en hoofden van laboratoria (art. 25). De gemeente is verantwoordelijk voor de uitvoering van de infectieziektebestrijding (art. 14 Wpg) en draagt dit over aan de GGD.

Zie [[Wiki/Bronsamenvattingen/Openbare Gezondheid/kerntaken-infectieziektebestrijding|Kerntaken infectieziektebestrijding]] voor de beschrijving van het meldingsproces en de zeven kerntaken van de IZB.

## Relaties

| Gerelateerd object | Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| NatuurlijkPersoon | index (patiënt) | → | 1 → 1 | Wpg |

## Bedrijfsprocessen

- **Infectieziektebestrijding** — verificatie, BCO, bestrijdingsmaatregelen
- **Bron- en contactonderzoek** — identificatie bron en contacten
- **Outbreak management** — opschaling bij uitbraken

## Bronnen

- [[Wiki/Bronsamenvattingen/Openbare Gezondheid/kerntaken-infectieziektebestrijding]]

## Terugmelding GGM

GGM-hiaat: het GGM kent geen beleidsdomein voor volksgezondheid/infectieziektebestrijding onder taakveld 7. De infectieziektemelding past als specialisatie van het bestaande AanvraagOfMelding-patroon. Zie #65 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
