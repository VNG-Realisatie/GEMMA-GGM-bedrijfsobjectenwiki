---
type: bedrijfsobject
naam: Horecabedrijf
domein: [Economie]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Vestiging
ggm_guid: EAID_B60B8EF9_D1C0_4e36_BF9B_1C16F92518DD
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram: ["Diagram Economie", "Diagram Gebied Vestiging en Adres", "KVK"]
ggm_diagram_ids: ["EAID_21D78104_E6EA_4d5c_9DBE_AB71F7DC99E7", "EAID_50085E67_46AC_4f54_B204_436786266EE2", "EAID_FC491653_1FBF_412a_A939_A705D501AE48"]
ggm_definitie: "Een gebouw of complex van gebouwen waar duurzame uitoefening van de activiteiten van een onderneming of rechtspersoon plaatsvindt."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst: NHR

ggm_gemma_naam: Vestiging
ggm_gemma_guid: b403d1ab-a0ee-4ca0-befa-01bbc54bf403
ggm_gemma_definitie: "Een gebouw of complex van gebouwen waar duurzame uitoefening van de activiteiten van een onderneming of rechtspersoon plaatsvindt."
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: business-object
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-b403d1ab-a0ee-4ca0-befa-01bbc54bf403"
ggm_gemma_bron: NHR
ggm_gemma_alternate_name:

gemma_definitie: "Bedrijf dat zich richt op het verstrekken van eten, drinken en/of logies, gereguleerd via de Verordening horeca en het Ontwikkelingskader Horeca."
gemma_toelichting: "De gemeente reguleert horecabedrijven via vergunningen, hinderprofielen en locatiebeleid. Het horecabeleid zoekt balans tussen levendigheid, leefbaarheid en een divers aanbod."
gemma_subtypes:
  - naam: Horecavergunning
    omschrijving: "Vergunning voor de exploitatie van een horecabedrijf, subtype van vergunning"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
bronnen:
  - [[Wiki/Bronsamenvattingen/Economie/horecabeleid-utrecht]]
  - [[Wiki/Bronsamenvattingen/Economie/beleidsregels-terrassen-utrecht]]
relaties:
  - type: generalisatie
    bedrijfsobject: "[[Vestiging]]"
    richting: van-dit-BO
    kardinaliteit: ""
    beschrijving: "Horecabedrijf is een specialisatie van Vestiging"
  - type: associatie
    bedrijfsobject: "[[Hotel]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een horecabedrijf kan een hotel exploiteren"
  - type: associatie
    bedrijfsobject: "[[Terras]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een horecabedrijf kan een terras exploiteren"
  - type: associatie
    bedrijfsobject: "[[Bed-and-breakfast]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een horecabedrijf kan een B&B exploiteren"
bedrijfsprocessen: [horecavergunningverlening, handhaving horeca, horecabeleid]
bedrijfsfuncties: [vergunningverlening, handhaving, economisch beleid]
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Centraal begrip in Verordening horeca en Ontwikkelingskader |
| Is herkenbaar voor domeinexperts | ✅ | Standaardbegrip voor vergunningverleners en beleidsmakers |
| Heeft een eigen bestaan | ✅ | Exploitatie op een fysieke locatie met vergunning |
| Kan in meervoud bestaan | ✅ | Honderden horecabedrijven in een gemeente |
| Heeft een eigen levenscyclus | ✅ | Aanvraag → vergunning → exploitatie → sluiting |
| Heeft relaties met andere concepten | ✅ | Hotel, terras, vergunning, hinderprofiel |

6/6 criteria — BO.

## Beschrijving

Een horecabedrijf is een onderneming die zich richt op het verstrekken van eten, drinken en/of logies. De gemeente reguleert horecabedrijven via de Verordening horeca, het Ontwikkelingskader Horeca en een vergunningenstelsel. Kernafwegingen zijn leefbaarheid (hinderprofiel), balans met detailhandel en wonen, en spreiding over de stad.

Het Utrechtse beleid stimuleert horeca buiten de historische binnenstad en beoordeelt horecaontwikkeling in het centrum kritisch.

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| Horecavergunning | Vergunning voor exploitatie van een horecabedrijf | — |

De horecavergunning is een subtype van vergunning, hier vastgelegd vanwege de directe koppeling met het horecabedrijf.

## GGM-bron

> "Een gebouw of complex van gebouwen waar duurzame uitoefening van de activiteiten van een onderneming of rechtspersoon plaatsvindt." — GGM (Vestiging), RSGB

- **Entiteit**: Vestiging
- **Beleidsdomein**: RSGBPlus (Kern)
- **Matchsterkte**: **partieel** — Vestiging is het generieke concept; horecabedrijf is een specialisatie die het GGM niet apart modelleert

Het GGM kent geen specifieke horecaentiteit. Horecabedrijf is een specialisatie van Vestiging, herkenbaar via SBI-code. De GGM-entiteit Hotel is een aparte specialisatie van Vestiging.

## BO-definitie

De eigen definitie wijkt af van de GGM-definitie doordat het specifiek gaat om horeca (eten, drinken, logies) terwijl Vestiging elke bedrijfsvestiging omvat.

| Veld | Waarde |
|---|---|
| GGM-definitie | Een gebouw of complex van gebouwen waar duurzame uitoefening van de activiteiten van een onderneming of rechtspersoon plaatsvindt. |
| GEMMA-definitie | Bedrijf dat zich richt op het verstrekken van eten, drinken en/of logies, gereguleerd via de Verordening horeca en het Ontwikkelingskader Horeca. |

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Vestiging]] | generalisatie | Horecabedrijf → Vestiging | — | GGM (overerving) |
| [[Hotel]] | associatie | Horecabedrijf → Hotel | 0..* | Beleid |
| [[Terras]] | associatie | Horecabedrijf → Terras | 0..* | Beleidsregel terrassen |
| [[Bed-and-breakfast]] | associatie | Horecabedrijf → B&B | 0..* | Beleid |
