---
type: begrip
naam: zaakdossier
definitie: Het geheel van zaakkenmerken en informatieobjecten bij een zaak — vormt de basis voor archivering en verantwoording.
begripstype: object
abstractieniveau: operationeel
domein: [Dienstverlening]
synoniemen: [dossier, zaakarchief]
bronnen: [Sources/Standaarden/rgbz-1.0, Sources/Standaarden/ztc2-informatiemodel-v2.1]
ggm_entiteit:
status: concept
---

# Zaakdossier

Het zaakdossier is het geheel van alle informatieobjecten (documenten) bij een zaak, tezamen met de zaakkenmerken. Het is geen apart objecttype in het RGBZ of de ZTC2 maar een impliciet concept dat ontstaat doordat informatieobjecten aan een zaak worden gerelateerd.

## Context

Het zaakdossier is cruciaal voor twee doelen:
1. **Verantwoording** — achteraf kunnen aantonen dat een zaak inhoudelijk goed en procesmatig correct is afgehandeld
2. **Archivering** — het archiefregime (vernietigen of bewaren, en na welke termijn) wordt bepaald door het [[resultaattype]] van de zaak

> "Door documenten te registreren en aan een zaak te relateren wordt het archief bij/van de zaak opgebouwd; alle documenten bij een zaak vormen tezamen met de zaakkenmerken het zaakdossier."
> — RGBZ 1.0

## Archiefregime

Het [[resultaattype]] bij een zaak bepaalt het archiefregime voor het gehele zaakdossier:
- **Archiefnominatie**: blijvend bewaren of (op termijn) vernietigen
- **Archiefactietermijn**: de termijn waarna het dossier vernietigd of overgebracht moet worden
- **Brondatum archiefprocedure**: het moment waarop de termijn start

In uitzonderingsgevallen kan het archiefregime van individuele [[informatieobject]]en afwijken van het zaakdossier als geheel. Privacygevoeligheid kan reden zijn om objecten eerder te vernietigen; specifieke wetgeving (bijv. BAG) kan vereisen dat een omgevingsvergunning eeuwig bewaard blijft terwijl het zaakdossier na 20 jaar vernietigd wordt.

## Objectdossier

Het RGBZ modelleert ook geen "objectdossier" als apart objecttype. Een objectdossier — alle zaken die betrekking hebben op een bepaald OBJECT — is afleidbaar uit de relaties ZAAK → ZAAKOBJECT → OBJECT.

## GGM-relatie

Het GGM kent geen entiteit "Zaakdossier". Het concept is afleidbaar uit de relaties Zaak → Document (via ZAAKDOCUMENT-relatie). De archiveringskenmerken zitten bij de Zaak-entiteit zelf (archiefnominatie, datumVernietigingDossier).

## Relaties

- [[zaakgericht-werken]] — het zaakdossier ontstaat als onderdeel van zaakgericht werken
- [[informatieobject]] — de informatiedragers die het dossier vormen
- [[resultaattype]] — bepaalt het archiefregime van het dossier
