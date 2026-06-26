---
type: bedrijfsobject
naam: WOZ-waarde
domein:
- Belastingen
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: WOZ-Waarde
ggm_guid: EAID_7C387F42_EC1A_4a78_B09B_533AAB03C0C2
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: 99 Kern
ggm_diagram:
- Vastgoed WOZ
- Detaillering WOZ-objecttypen op hoofdlijnen
- Detaillering WOZ-objecttypen met attributen
- WOZ-OBJECT
- WOZ-WAARDE
ggm_diagram_ids:
- EAID_0CF01F05_D23F_454a_A0CD_042C2DD9EE7D
- EAID_3F813481_9A40_4b1b_9B24_1FD069230A45
- EAID_5E76FEEA_58F8_41fd_9FF1_B44274C80FA5
- EAID_4785522F_7798_4d8d_A437_48602B8ACA21
- EAID_EB7771AD_FBE8_40e5_9CD7_2C8EED4A6C33
ggm_definitie: De op grond van de Wet WOZ vastgestelde waarde van het WOZ-object naar de genoemde waardepeildatum.
ggm_toelichting: ''
ggm_synoniemen: ''
ggm_herkomst: ''
ggm_gemma_naam: ''
ggm_gemma_guid: ''
ggm_gemma_definitie: ''
ggm_gemma_toelichting: ''
ggm_gemma_synoniemen: ''
ggm_gemma_type: ''
ggm_gemma_url: ''
ggm_gemma_bron: ''
ggm_gemma_alternate_name: ''
gemma_definitie: De op grond van de Wet WOZ vastgestelde waarde van een WOZ-object naar een bepaalde waardepeildatum.
definitie: De op grond van de Wet WOZ vastgestelde waarde van het WOZ-object naar de genoemde waardepeildatum.
bedrijfsprocessen:
- WOZ-taxatie
- OZB-heffing
- bezwaarbehandeling WOZ
- WOZ-beschikking verzenden
bedrijfsfuncties:
- Waardering onroerende zaken
- Belastingheffing
status: concept
relaties:
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/99-kern/woz-object|WOZ-object]]'
  richting: naar-dit-BO
  kardinaliteit: 1
  beschrijving: Elke WOZ-waarde hoort bij precies één WOZ-object
---

# WOZ-waarde (bedrijfsobject)

De vastgestelde marktwaarde van een [[Wiki/Bedrijfsobjecten/99-kern/woz-object|woz-object]] op een bepaalde waardepeildatum, formeel bekendgemaakt via een WOZ-beschikking.

## GGM-bron

> **WOZ-Waarde**: De op grond van de Wet WOZ vastgestelde waarde van het WOZ-object naar de genoemde waardepeildatum.
> — *GGM v2.5.1, RSGBPlus (taakveld 99 Kern)*

**Entiteit:** WOZ-Waarde (BRWOZ)
**Attributen:** datumWaardepeiling, vastgesteldeWaarde, datumPeilingToestand, statusBeschikking

## BO-definitie

Het bedrijfsobject WOZ-waarde omvat zowel de getaxeerde waarde als het beschikkingsaspect (statusBeschikking). In de GGM is de WOZ-beschikking geen aparte entiteit maar een attribuut van WOZ-Waarde. Op bedrijfsniveau geldt hetzelfde: de beschikking IS de formele vaststelling van de waarde.

De WOZ-waarde is de centrale heffingsmaatstaf voor:
- Gemeentelijke heffingen: OZB, riool- en waterzorgheffing, forensenbelasting
- Rijksbelastingen: eigenwoningforfait, erfbelasting
- Waterschapsbelasting
- Niet-fiscaal: hypotheekverstrekking, huurprijsberekening, fraudebestrijding

De waarde loopt altijd een jaar achter: WOZ-beschikking 2026 bevat de waarde op peildatum 1 januari 2025.

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Afwijking |
|---|---|---|---|
| Hoort bij | [[Wiki/Bedrijfsobjecten/99-kern/woz-object\|woz-object]] | WOZ-Waarde → WOZ-object [1] | Geen |

**Relatie met begrippen buiten GGM (hiaten):**
- Is heffingsmaatstaf voor de belastingaanslag — GGM modelleert deze keten niet
- Wordt vastgesteld door de heffingsambtenaar — actor niet in GGM
- Staat open voor bezwaar door de belastingplichtige — bezwaarproces niet in GGM

## Beslissing: WOZ-beschikking geen apart BO

De WOZ-beschikking is op bedrijfsniveau niet onderscheidbaar van de WOZ-waarde: de beschikking is het formele besluit dat de waarde vaststelt. In het GGM is dit weergegeven als attribuut statusBeschikking op WOZ-Waarde. Het begrip woz-beschikking blijft als apart begrip bestaan (het beschrijft het administratieve document), maar wordt niet als apart bedrijfsobject uitgewerkt.

## Bedrijfsprocessen

- **WOZ-taxatie**: waardebepaling via geautomatiseerde modellen en taxatiewijzers
- **WOZ-beschikking verzenden**: jaarlijks in de eerste 8 weken, 9+ miljoen beschikkingen
- **OZB-heffing**: waarde × tarief = aanslag
- **Bezwaarbehandeling**: beoordeling van bezwaren tegen de vastgestelde waarde

## Bronnen

- [[Wiki/Bronsamenvattingen/Belastingen/belastingtypen]]
- [[Wiki/Bronsamenvattingen/Belastingen/belastinggebied]]
- [[Wiki/Bronsamenvattingen/Belastingen/belastingpolitiek]]
- [[Wiki/Bronsamenvattingen/Belastingen/belastingverordening]]
- [[Wiki/Bronsamenvattingen/Belastingen/bevoegdhedenverdeling]]
- [[Wiki/Bronsamenvattingen/Belastingen/invordering-en-kwijtschelding]]
- [[Wiki/Bronsamenvattingen/Belastingen/kostendekkende-tarieven]]
- [[Wiki/Bronsamenvattingen/Belastingen/wettelijke-grenzen]]
- [[Wiki/Bronsamenvattingen/Belastingen/raadgever-gemeentelijke-belastingen]]
- [[Wiki/Bronsamenvattingen/Belastingen/raadgever-kostenonderbouwing]]
- [[Wiki/Bronsamenvattingen/Belastingen/raadgever-woz]]
