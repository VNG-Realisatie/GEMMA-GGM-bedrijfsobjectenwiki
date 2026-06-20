---
type: begrip
naam: informatieobject
definitie: Geheel van gegevens met een eigen identiteit ongeacht zijn vorm — breder dan 'document', omvat ook foto's, datasets, geluidsopnames, webpagina's en samengestelde objecten.
begripstype: object
abstractieniveau: operationeel
domein: [Dienstverlening]
synoniemen: [document, informatie-object]
bronnen: [Sources/Standaarden/rgbz-1.0, Sources/Standaarden/ztc2-informatiemodel-v2.1]
ggm_entiteit: Document
status: concept
---

# Informatieobject

Een informatieobject is een geheel van gegevens met een eigen identiteit, ongeacht zijn vorm, met de bijbehorende metadata, ontvangen of opgemaakt bij de uitvoering van taken. Het begrip is breder dan het veelgebruikte "document" en omvat alle vormen van informatie: tekstverwerkingsdocumenten, papieren brieven, webpagina's, landkaarten, foto's, geluidsopnames, datasets, blogs, e-mails met bijlagen.

> "'Informatieobject' is een generiekere term voor het veelgebruikte begrip 'document' dat beperkter van reikwijdte is."
> — GEMMA Zaaktypecatalogus 2, Informatiemodel v2.1

## Context

Het RGBZ (2010) hanteert nog de term "document" maar bedoelt feitelijk dezelfde brede scope. De ZTC2 (2014) vervangt "document" door "informatieobject" om deze breedte expliciet te maken. Het bijbehorende type heet INFORMATIEOBJECTTYPE (in plaats van DOCUMENTTYPE).

De fysieke vorm van hetgeen ontvangen of gecreëerd is, is niet bepalend voor de afbakening. Een aanvraag op papier met bijlagen kan als één informatieobject beschouwd worden, net als een digitale aanvraag met tekening (CAD) en berekening (spreadsheet).

## Enkelvoudig en samengesteld

Het RGBZ onderscheidt:
- **Enkelvoudig document/informatieobject** — als één geheel te behandelen en te beheren
- **Samengesteld document/informatieobject** — bestaat uit twee of meer enkelvoudige objecten die vanwege gezamenlijke vervaardiging/ontvangst of vanwege aard/omvang als geheel beschouwd worden

## Relatie tot zaak

Informatieobjecten worden via ZAAKDOCUMENT aan een zaak gerelateerd (N:M-relatie). Eén informatieobject kan relevant zijn voor meerdere zaken. Alle informatieobjecten bij een zaak vormen samen met de zaakkenmerken het [[Wiki/Begrippen/zaakdossier|zaakdossier]].

Een informatieobject wordt pas "archiefstuk" (record) zodra de zaakkenmerken aangeven dat alle gekoppelde objecten gearchiveerd dienen te zijn.

## GGM-relatie

Het GGM modelleert dit als **Document** (abstract) met specialisaties **EnkelvoudigDocument** en **SamengesteldDocument** in beleidsdomein RGBZPlus (taakveld 99 Kern). Het GGM hanteert dus nog de RGBZ-terminologie "document", niet de ZTC2-terminologie "informatieobject".

## Relaties

- [[Wiki/Begrippen/zaakgericht-werken|zaakgericht-werken]] — informatieobjecten zijn een kernonderdeel van zaakgericht werken
- [[Wiki/Begrippen/zaakdossier|zaakdossier]] — het geheel van informatieobjecten en zaakkenmerken
- [[Wiki/Begrippen/zaaktypecatalogus|zaaktypecatalogus]] — INFORMATIEOBJECTTYPE wordt per catalogus geconfigureerd
- [[Wiki/Begrippen/resultaattype|resultaattype]] — bepaalt het archiefregime van informatieobjecten
