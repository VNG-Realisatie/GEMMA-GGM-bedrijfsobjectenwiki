---
type: begrip
naam: woz-waarde
definitie: De marktwaarde van een onroerende zaak, vastgesteld door de gemeente onder de Wet WOZ op peildatum 1 januari van het voorgaande jaar.
begripstype: object
abstractieniveau: operationeel
domein: [Belastingen]
synoniemen: [WOZ-taxatie, getaxeerde waarde]
bronnen: ["[[Sources/Onderwerpen VNG/Belastingen/raadgever-woz]]"]
ggm_entiteit: WOZ-Waarde (RSGBPlus, taakveld 99 Kern)
status: concept
---

# WOZ-waarde

De prijs die de meestbiedende koper zou willen betalen voor een [[onroerende-zaak]]. Wordt jaarlijks vastgesteld door de gemeente op basis van geautomatiseerde taxatiemodellen en bekendgemaakt via een [[woz-beschikking]].

> "De WOZ-waarde is de prijs die de meestbiedende koper wil betalen voor een onroerende zaak. Dat is dus de werkelijke marktwaarde."
> — *Raadgever WOZ, VNG*

## Context

De WOZ-waarde is de centrale [[heffingsmaatstaf]] voor de drie omvangrijkste gemeentelijke heffingen (OZB, rioolheffing, afvalstoffenheffing) en voor rijksbelastingen (eigenwoningforfait, erfbelasting). Daarnaast wordt de WOZ-waarde gebruikt voor hypotheekverstrekking, maximale huurprijsberekening en fraudebestrijding.

De WOZ is een van de 11 basisregistraties in Nederland. De waarde loopt altijd een jaar achter op de beschikking: de WOZ-beschikking van 2026 bevat de waarde op peildatum 1 januari 2025.

Een stijging van de WOZ-waarde leidt niet automatisch tot een hogere [[belastingaanslag]] — de gemeenteraad stelt de tarieven vast en kan deze aanpassen.

## Relaties

- Wordt vastgesteld per [[onroerende-zaak]]
- Bekendgemaakt via een [[woz-beschikking]]
- Is [[heffingsmaatstaf]] voor OZB en andere heffingen
- Toezicht door de [[waarderingskamer]]
- Onderdeel van de [[belastingmix]]-afweging (tarief × WOZ-waarde = aanslag)

## Afbakening

- Niet hetzelfde als de koopprijs of de vraagprijs — het is de getaxeerde marktwaarde
- Niet hetzelfde als de kadastrale waarde

## GGM

**Match:** GGM-entiteit "WOZ-Waarde" in RSGBPlus (taakveld 99 Kern, herkomst BRWOZ). Attributen: datumWaardepeiling, vastgesteldeWaarde, datumPeilingToestand, statusBeschikking. De entiteit dekt de waarde inclusief beschikkingsstatus. Zie bedrijfsobject [[woz-waarde-bo]].

Het GGM modelleert de WOZ-waarde als basisregistratie-gegeven, niet als onderdeel van het heffingsproces (aanslag, tarief). Die keten ontbreekt — zie [[ggm-hiaten-belastingendomein]].
