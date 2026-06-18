---
type: begrip
naam: zaaktypecatalogus
definitie: Verzameling van zaaktypen voor een domein, inclusief alle configuratie (statustypes, resultaattypes, roltypes, eigenschappen) die bepaalt hoe zaken van elk type worden behandeld.
begripstype: object
abstractieniveau: operationeel
domein: [Dienstverlening]
synoniemen: [ZTC, zaaktypecatalogus, ZTC2]
bronnen: [Sources/Standaarden/ztc2-informatiemodel-v2.1]
ggm_entiteit:
status: concept
---

# Zaaktypecatalogus

De zaaktypecatalogus (ZTC) is de verzameling zaaktypen die een gemeente (of een sector, of een keten) onderscheidt, inclusief alle configuratie die bepaalt hoe zaken van elk type worden afgehandeld: welke statussen ze doorlopen, welke resultaten mogelijk zijn, welke rollen betrokkenen kunnen vervullen, welke informatieobjecten relevant zijn en welke zaaktypespecifieke eigenschappen worden vastgelegd.

> "Een zaaktypecatalogus bevat de zaaktypen die onderscheiden worden binnen het domein waarop die catalogus gericht is."
> — GEMMA Zaaktypecatalogus 2, Informatiemodel v2.1

## Context

KING (nu VNG Realisatie) heeft onderkend dat er niet één landelijke zaaktypecatalogus kan bestaan. De ZTC2 voorziet daarom in het objecttype CATALOGUS waarmee catalogi per domein, organisatie, sector of keten worden aangemaakt. Elke catalogus wordt uniek geïdentificeerd door de combinatie van het RSIN van de eigenaar en het domein.

## Structuur

Een zaaktypecatalogus bevat op het hoogste niveau drie objecttypen:

1. **ZAAKTYPE** — de kern: welke zaaktypen bestaan, met configuratie voor behandeling, doorlooptijd, archivering
2. **BESLUITTYPE** — de besluittypen die herbruikbaar zijn over meerdere zaaktypen
3. **INFORMATIEOBJECTTYPE** — de informatieobjecttypen die herbruikbaar zijn over meerdere zaaktypen

Binnen elk zaaktype worden geconfigureerd:
- **STATUSTYPE** — de mijlpalen die een zaak doorloopt
- **[[resultaattype]]** — de mogelijke uitkomsten met archiefregime
- **ROLTYPE** — de rollen die betrokkenen kunnen vervullen
- **EIGENSCHAP** — zaaktypespecifieke gegevens
- **ZAAKOBJECTTYPE** — de objecttypen waarop een zaak betrekking kan hebben

## Relatie tot RGBZ

De ZTC2 is de configuratielaag, het RGBZ is de runtime-laag:

| ZTC2 (configuratie) | RGBZ (runtime) |
|---|---|
| ZAAKTYPE | ZAAK |
| STATUSTYPE | STATUS |
| BESLUITTYPE | BESLUIT |
| INFORMATIEOBJECTTYPE | DOCUMENT |
| ROLTYPE | ROL |

## GGM-relatie

Het GGM bevat Zaaktype en Statustype in beleidsdomein RGBZPlus, maar niet de volledige ZTC2-configuratiestructuur. CATALOGUS, RESULTAATTYPE, EIGENSCHAP, ROLTYPE en ZAAKOBJECTTYPE ontbreken in het GGM. Dit is een structureel hiaat: het GGM modelleert de zaak-runtime maar niet de zaaktype-configuratie.

## Relaties

- [[zaakgericht-werken]] — het werkprincipe dat de zaaktypecatalogus ondersteunt
- [[resultaattype]] — de uitkomsten die per zaaktype worden geconfigureerd
- [[informatieobject]] — de informatiedragers die per zaaktype worden geconfigureerd
