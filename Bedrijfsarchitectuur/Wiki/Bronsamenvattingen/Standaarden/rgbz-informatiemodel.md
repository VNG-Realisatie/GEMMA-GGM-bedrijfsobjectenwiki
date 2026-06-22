---
type: bronsamenvatting
titel: "Referentiemodel Gemeentelijke Basisgegevens Zaken (RGBZ) 1.0"
domein: [Dienstverlening]
datum_ingest: 2026-06-18
begrippen_geextraheerd: [zaakgericht werken, zaakdossier, informatieobject]
---

# Bronsamenvatting: RGBZ 1.0

**Bronnen:**
- Referentiemodel Gemeentelijke Basisgegevens Zaken, versie 1.0 (KING, september 2010)
- Introductie RGBZ (vng-realisatie.github.io/RGBZ/)

## Doel en positionering

Het RGBZ specificeert de gegevens en hun samenhang die gemeenten minimaal nodig hebben om betrokkenen bij zaken te informeren, zaken te verantwoorden en desgewenst te reconstrueren. Het is onderdeel van GEMMA en vervangt het GFO Zaken (2004).

> "Het model specificeert de gegevens en hun samenhang die gemeenten, daarmee samenwerkende organisaties en hun klanten minimaal nodig hebben om voldoende op de hoogte te zijn van lopende en afgeronde zaken."

**Relatie tot andere modellen:**
- Het RGBZ is het "hoe"-model: hoe de gemeente haar taken uitoefent
- Het RSGB is het "wat"-model: de objecten waarop die taakuitoefening betrekking heeft
- De ZTC2 definieert welke zaaktypen in de gegevensuitwisseling betrokken zijn
- StUF-Zaken is de berichtenstandaard afgeleid van het RGBZ

**Afbakening:** Gericht op het dienstverleningsmanagement — de verbindende schakel tussen klantcontact en vakspecialist. Standaardiseert generieke zaakgegevens (kenmerken, betrokkenen, documenten, voortgang) maar niet vakspecifieke informatie.

## Objecttypen

Het RGBZ bevat 17 objecttypen in een samenhangende structuur rond de ZAAK:

### Kern

| Objecttype | Definitie | Herkomst |
|---|---|---|
| **ZAAK** | Een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moeten worden. | GFO Zaken |
| **ZAAKTYPE** | Kenmerken van groepen vergelijkbare zaken. | GFO Zaken |
| **STATUS** | Aanduiding van de stand van zaken op basis van een betekenisvol behaald resultaat voor de initiator. | GFO Zaken |
| **STATUSTYPE** | Generieke aanduiding van de aard van een STATUS. | GFO Zaken |

### Betrokkenen en Rollen

| Objecttype | Definitie | Herkomst |
|---|---|---|
| **BETROKKENE** | SUBJECT dat een rol kan spelen bij een ZAAK — generalisatie van NP, NNP, Vestiging, OrgEenheid, Medewerker. | KING |
| **ROL** | Taken, rechten en/of verplichtingen van een BETROKKENE ten aanzien van een specifieke ZAAK. | KING |
| **MEDEWERKER** | Medewerker van de zaakbehandelende organisatie. | GFO Zaken |
| **ORGANISATORISCHE EENHEID** | Functioneel afgebakend onderdeel binnen de zaakbehandelende organisatie. | GFO Zaken |
| **VESTIGING VAN ZAAKBEHANDELENDE ORGANISATIE** | Locatie waar een organisatorische eenheid haar activiteiten uitoefent. | KING |

### Documenten en Besluiten

| Objecttype | Definitie | Herkomst |
|---|---|---|
| **DOCUMENT** | Geheel van gegevens met eigen identiteit, ongeacht vorm — ENKELVOUDIG of SAMENGESTELD. | KING (NEN 2082) |
| **ENKELVOUDIG DOCUMENT** | Document dat als één geheel wordt behandeld en beheerd. | KING |
| **SAMENGESTELD DOCUMENT** | Document dat uit twee of meer enkelvoudige documenten bestaat. | KING |
| **DOCUMENTTYPE** | Aanduiding van de aard van een DOCUMENT. | KING |
| **ZAAKDOCUMENT** | N:M-relatie tussen ZAAK en DOCUMENT. | KING |
| **BESLUIT** | Een na overweging of beraadslaging vastgestelde beslissing voor een individueel of concreet geval. | KING (GFO Zaken) |
| **BESLUITTYPE** | Generieke aanduiding van de aard van een BESLUIT. | KING |

### Zaakobject

| Objecttype | Definitie | Herkomst |
|---|---|---|
| **OBJECT** | Het object waarop een ZAAK betrekking kan hebben — generalisatie van 35+ RSGB/RGBZ-objecttypen. | KING |
| **ZAAKOBJECT** | Relatie tussen ZAAK en OBJECT. | KING |

## Kernconcepten

### Zaak als bedrijfsproces
De zaak wordt bekeken vanuit het perspectief van de initiator. Het traject van aanleiding tot levering van producten/diensten bepaalt omvang en afbakening. Een **deelzaak** is op zich weer een ZAAK, gerelateerd aan de hoofdzaak. Een zaak die betrekking heeft op een andere zaak (bijv. bezwaar op een beschikking) wordt gemodelleerd via "betreft andere ZAAK".

### Zaakdossier
Het zaakdossier is geen apart objecttype maar een impliciet concept: alle documenten bij een zaak vormen tezamen met de zaakkenmerken het zaakdossier. Archivering hangt af van het resultaat van de zaak.

### Documenten als informatieobjecten
Het RGBZ hanteert "document" maar bedoelt feitelijk elke vorm van informatie: tekstverwerkingsdocumenten, brieven, webpagina's, foto's, geluidsopnames, datasets, e-mails met bijlagen. De ZTC2 vervangt later "document" door het bredere begrip "informatieobject".

### Rollen
Een ROL beschrijft *wat* iemand doet bij een zaak, niet *wie* het is. Rollen zijn de taken die iemand uitvoert, onafhankelijk van functie of organisatie.

## Status en evolutie

De actuele officiële versie is **RGBZ 1.0** ('in gebruik'), geïmplementeerd in StUF-ZKN 3.10.

Er bestaat een **RGBZ 2.0** (conceptversie) die nooit een officiële status heeft bereikt. Sommige nieuwe concepten uit RGBZ 2.0 zijn overgenomen in de **ZGW API's** (Zaakgericht Werken API's), die wél een officiële status hebben. De ZGW API's zijn de opvolger van StUF-ZKN voor zaakgegevensuitwisseling via REST/JSON.

### Historische lijn

```
GFO Zaken (VNG, 2004)
    ↓ verbinding met RSGB
RGBZ 1.0 (KING, 2010)  ← huidige standaard
    ↓ conceptversie
RGBZ 2.0 (concept, nooit vastgesteld)
    ↓ concepten overgenomen
ZGW API's (VNG Realisatie, officieel)
```

### Berichtenarchitectuur

Het RGBZ is uitgewerkt in een ecosysteem van berichtenstandaarden:

| Standaard | Beschrijving |
|---|---|
| **StUF-ZKN 3.10** | Sectormodel Zaken — berichtenstandaard afgeleid van het RGBZ |
| **Zaak- en Documentservices** | Specifieke berichten voor veelvoorkomende gebeurtenissen in zaakgericht werken en documentmanagement |
| **ZGW API's** | Opvolger via REST/JSON — neemt concepten over uit RGBZ 2.0 |

## Relevantie voor bedrijfsarchitectuur

- Het RGBZ is de grondslag voor het GGM-beleidsdomein **RGBZPlus** (taakveld 99 Kern, 25 entiteiten)
- Het GGM heeft het RGBZ uitgebreid met Klantcontact, Heffing, Betaling, Bedrijfsproces
- Het RGBZ maakt de brug tussen RSGB-objecten en gemeentelijke processen via het zaak-concept
- Begrippen als zaakgericht-werken, zaakdossier en informatieobject komen hier vandaan
- De evolutie RGBZ 1.0 → RGBZ 2.0 (concept) → ZGW API's is relevant voor de vraag hoe actueel het GGM-beleidsdomein RGBZPlus nog is

## Bronnen

- [[Sources/Standaarden/rgbz-1.0]]
