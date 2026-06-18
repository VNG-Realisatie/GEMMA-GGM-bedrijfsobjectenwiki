---
type: bedrijfsobject
naam: WOZ-waarde
domein: [Belastingen]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: WOZ-Waarde
ggm_beleidsdomein: RSGBPlus (Kern)
definitie: De op grond van de Wet WOZ vastgestelde waarde van het WOZ-object naar de genoemde waardepeildatum.
gerelateerde_begrippen: [woz-waarde, woz-beschikking, heffingsmaatstaf, belastingaanslag]
relaties:
  - type: associatie
    bedrijfsobject: WOZ-object
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: Elke WOZ-waarde hoort bij precies één WOZ-object
bedrijfsprocessen: [WOZ-taxatie, OZB-heffing, bezwaarbehandeling WOZ, WOZ-beschikking verzenden]
bedrijfsfuncties: [Waardering onroerende zaken, Belastingheffing]
status: concept
---

# WOZ-waarde (bedrijfsobject)

De vastgestelde marktwaarde van een [[woz-object]] op een bepaalde waardepeildatum, formeel bekendgemaakt via een WOZ-beschikking.

## GGM-bron

> **WOZ-Waarde**: De op grond van de Wet WOZ vastgestelde waarde van het WOZ-object naar de genoemde waardepeildatum.
> — *GGM v2.5.1, RSGBPlus (taakveld 99 Kern)*

**Entiteit:** WOZ-Waarde (BRWOZ)
**Attributen:** datumWaardepeiling, vastgesteldeWaarde, datumPeilingToestand, statusBeschikking

## BO-definitie

Het bedrijfsobject WOZ-waarde omvat zowel de getaxeerde waarde als het beschikkingsaspect (statusBeschikking). In de GGM is de WOZ-beschikking geen aparte entiteit maar een attribuut van WOZ-Waarde. Op bedrijfsniveau geldt hetzelfde: de beschikking IS de formele vaststelling van de waarde.

De WOZ-waarde is de centrale [[heffingsmaatstaf]] voor:
- Gemeentelijke heffingen: OZB, riool- en waterzorgheffing, forensenbelasting
- Rijksbelastingen: eigenwoningforfait, erfbelasting
- Waterschapsbelasting
- Niet-fiscaal: hypotheekverstrekking, huurprijsberekening, fraudebestrijding

De waarde loopt altijd een jaar achter: WOZ-beschikking 2026 bevat de waarde op peildatum 1 januari 2025.

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Afwijking |
|---|---|---|---|
| Hoort bij | [[woz-object]] | WOZ-Waarde → WOZ-object [1] | Geen |

**Relatie met begrippen buiten GGM (hiaten):**
- Is [[heffingsmaatstaf]] voor de [[belastingaanslag]] — GGM modelleert deze keten niet
- Wordt vastgesteld door de [[heffingsambtenaar]] — actor niet in GGM
- Staat open voor bezwaar door de [[belastingplichtige]] — bezwaarproces niet in GGM

## Beslissing: WOZ-beschikking geen apart BO

De WOZ-beschikking is op bedrijfsniveau niet onderscheidbaar van de WOZ-waarde: de beschikking is het formele besluit dat de waarde vaststelt. In het GGM is dit weergegeven als attribuut statusBeschikking op WOZ-Waarde. Het begrip [[woz-beschikking]] blijft als apart begrip bestaan (het beschrijft het administratieve document), maar wordt niet als apart bedrijfsobject uitgewerkt.

## Bedrijfsprocessen

- **WOZ-taxatie**: waardebepaling via geautomatiseerde modellen en taxatiewijzers
- **WOZ-beschikking verzenden**: jaarlijks in de eerste 8 weken, 9+ miljoen beschikkingen
- **OZB-heffing**: waarde × tarief = aanslag
- **Bezwaarbehandeling**: beoordeling van bezwaren tegen de vastgestelde waarde
