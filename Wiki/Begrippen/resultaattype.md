---
type: begrip
naam: resultaattype
definitie: Indeling van mogelijke resultaten van zaken van een zaaktype naar hun aard (verleend, geweigerd, ingetrokken, etc.) — bepaalt het archiefregime van het zaakdossier.
begripstype: object
abstractieniveau: operationeel
domein: [Dienstverlening]
synoniemen: []
bronnen: [Sources/Standaarden/ztc2-informatiemodel-v2.1]
ggm_entiteit:
status: concept
---

# Resultaattype

Het resultaattype is de indeling of groepering van resultaten van zaken van hetzelfde zaaktype naar hun aard: "verleend", "geweigerd", "verwerkt", "ingetrokken", et cetera. Het is geïntroduceerd in de ZTC2 (al aanwezig in ZTC 1) en bepaalt het archiefregime van het [[zaakdossier]].

## Context

Elke zaak heeft een resultaat. In veel gevallen valt dit samen met een besluit ("Evenementenvergunning verleend", "Energiesubsidie geweigerd"), maar het komt ook voor dat zaken worden afgehandeld zonder besluit: aangiften, meldingen, intrekking van een aanvraag.

> "Het resultaat van een zaak is van groot belang voor de archivering: het resultaattype bepaalt mede of de zaak en het bijbehorende dossier moeten worden vernietigd (na enige termijn) of blijvend bewaard moeten worden."
> — GEMMA Zaaktypecatalogus 2, Informatiemodel v2.1

## Archiefregime

Het resultaattype bepaalt drie archiveringskenmerken:

| Kenmerk | Beschrijving |
|---|---|
| **Archiefnominatie** | Blijvend bewaren of (op termijn) vernietigen |
| **Archiefactietermijn** | Termijn waarna het zaakdossier vernietigd of overgebracht moet worden |
| **Brondatum archiefprocedure** | Aanduiding van de brondatum waarop de termijn start |

Het resultaattype verwijst naar de relevante passage in de **Selectielijst Archiefbescheiden** van de verantwoordelijke overheidsorganisatie.

## Voorwaarden

Bij een resultaattype kunnen voorwaarden worden geconfigureerd:
- Welke **ZAAKOBJECTTYPEN** verplicht gerelateerd moeten zijn
- Welke **INFORMATIEOBJECTTYPEN** verplicht aanwezig moeten zijn in het zaakdossier
- De brondatum kan afhangen van een **EIGENSCHAP** van de zaak

## GGM-relatie

Het GGM kent **geen** entiteit Resultaattype. Het RGBZ-deel in het GGM (beleidsdomein RGBZPlus) bevat de Zaak-entiteit met archiveringsattributen (archiefnominatie, datumVernietigingDossier), maar het resultaattype als configuratie-objecttype bij een zaaktype ontbreekt. Dit is onderdeel van het bredere hiaat: het GGM modelleert de zaak-runtime maar niet de volledige ZTC2-configuratielaag.

## Relaties

- [[zaaktypecatalogus]] — het resultaattype wordt per zaaktype geconfigureerd in de catalogus
- [[zaakdossier]] — het resultaattype bepaalt het archiefregime van het dossier
- [[informatieobject]] — individuele informatieobjecten kunnen een afwijkend archiefregime hebben
- [[zaakgericht-werken]] — resultaattypes zijn een essentieel onderdeel van de inrichting
