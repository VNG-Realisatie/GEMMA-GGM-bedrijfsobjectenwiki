---
type: begrip
naam: zaakgericht werken
definitie: Werkwijze waarbij de gemeente haar dienstverlening organiseert rond zaken — samenhangende hoeveelheden werk met een gedefinieerde aanleiding en een gedefinieerd resultaat.
begripstype: thema
abstractieniveau: operationeel
domein: [Dienstverlening]
synoniemen: [zaakgericht werken, zaakgestuurd werken]
bronnen: [Sources/Standaarden/rgbz-1.0, Sources/Standaarden/ztc2-informatiemodel-v2.1]
ggm_entiteit:
status: concept
---

# Zaakgericht werken

Zaakgericht werken is de werkwijze waarbij alle activiteiten die nodig zijn om een aanleiding (aanvraag, melding, intern verzoek) af te handelen worden gebundeld tot één **zaak**. Die zaak krijgt een gestandaardiseerde set kenmerken (betrokkenen, statussen, documenten, resultaat) waardoor voortgang bewaakt, verantwoording afgelegd en informatie gedeeld kan worden — zowel intern als met ketenpartners.

> "Een zaak is een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moeten worden."
> — GFO Zaken (2004), overgenomen in RGBZ 1.0

## Context

Zaakgericht werken wordt als een belangrijk thema gezien om meer grip te krijgen op processen, zowel voor dienstverlening als interne doelen. KING (nu VNG Realisatie) ondersteunt gemeenten hierbij via de GEMMA, waarvan het RGBZ en de ZTC2 de informatiemodellen zijn.

De aanpak is niet beperkt tot externe dienstverlening. Ook interne zaken (van computerstoring tot bestemmingsplan) vallen binnen het werkingsgebied.

## Informatiemodellen

Zaakgericht werken wordt ondersteund door twee samenhangende informatiemodellen:

- Het **RGBZ** (Referentiemodel Gemeentelijke Basisgegevens Zaken) definieert de runtime-gegevens: welke gegevens bij een zaak worden vastgelegd.
- De **[[Wiki/Begrippen/zaaktypecatalogus|zaaktypecatalogus]]** (ZTC2) definieert de configuratie: welke zaaktypen bestaan, welke statussen ze doorlopen, welke resultaten mogelijk zijn.

### Berichtenstandaarden

Het RGBZ is uitgewerkt in berichtenstandaarden voor gegevensuitwisseling:
- **StUF-ZKN 3.10** — sectormodel Zaken, gebaseerd op RGBZ 1.0
- **Zaak- en Documentservices** — specifieke berichten voor veelvoorkomende gebeurtenissen
- **ZGW API's** — de opvolger via REST/JSON, neemt concepten over uit het nooit vastgestelde RGBZ 2.0

## Kernprincipes

1. **Zaaktype = bedrijfsproces**: de afbakening van een zaaktype komt overeen met een bedrijfsproces "van klant tot klant". Onderdelen van bedrijfsprocessen vormen geen zelfstandige zaken.
2. **Perspectief van de initiator**: wat een zaak is, wordt bekeken vanuit het perspectief van de initiator — niet vanuit de interne procesorganisatie.
3. **Generiek + specifiek**: het RGBZ standaardiseert generieke zaakgegevens; vakspecifieke informatie wordt per zaaktype geconfigureerd via de ZTC2.
4. **[[Wiki/Begrippen/zaakdossier|zaakdossier]]**: alle documenten bij een zaak vormen met de zaakkenmerken het zaakdossier. Archivering wordt bepaald door het [[Wiki/Begrippen/resultaattype|resultaattype]].

## Relaties

- [[Wiki/Begrippen/zaaktypecatalogus|zaaktypecatalogus]] — de structuur waarmee zaaktypen worden gedefinieerd
- [[Wiki/Begrippen/informatieobject|informatieobject]] — de informatiedragers die bij een zaak horen
- [[Wiki/Begrippen/zaakdossier|zaakdossier]] — het geheel van zaakkenmerken en documenten
- [[Wiki/Begrippen/resultaattype|resultaattype]] — de mogelijke uitkomsten die het archiefregime bepalen

## Afbakening

Zaakgericht werken is een *werkwijze*, niet een systeem of applicatie. Het omvat het organisatorisch principe én de informatiestandaarden die het ondersteunen. Het is domeinoverstijgend — het raakt alle gemeentelijke domeinen waarin zaken worden afgehandeld.

## GGM-relatie

Het GGM modelleert zaakgericht werken in beleidsdomein **RGBZPlus** (taakveld 99 Kern, 25 entiteiten). Dit omvat de kern (Zaak, Status, Besluit, Document, Betrokkene) plus GGM-uitbreidingen (Klantcontact, Heffing, Betaling, Bedrijfsproces). De ZTC2-configuratielaag (CATALOGUS, RESULTAATTYPE, EIGENSCHAP, ROLTYPE) zit niet in het GGM.

Daarnaast kent het GGM taakveld **10 Dienstverlening** dat gericht is op meldingen, aanvragen, baliecontacten en digitale interacties — het klantcontactdeel van zaakgericht werken.
