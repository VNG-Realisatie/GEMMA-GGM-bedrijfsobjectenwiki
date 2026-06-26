---
type: bronsamenvatting
titel: Baseline Informatiebeveiliging Overheid 2 (BIO2)
onderwerp: [informatiesamenleving]
datum_ingest: 2026-06-26
---

# Baseline Informatiebeveiliging Overheid 2 (BIO2)

De BIO2 (versie 1.3 definitief, 9 januari 2026) is het verplichte normenkader voor informatiebeveiliging binnen alle overheidsentiteiten. Het is vastgesteld door het Overheidsbreed Beleidsoverleg Digitale Overheid (OBDO) en wettelijk verankerd via de Cyberbeveiligingswet (Cbw). BZK is stelselverantwoordelijke; het Centrum Informatiebeveiliging en Privacybescherming (CIP) beheert het document.

## Structuur

De BIO2 bestaat uit twee delen:

1. **Deel 1 BIO2-kader** — context, doel, verplichtingen, ISMS, risicomanagement, governance, transparantie en toezicht.
2. **Deel 2 BIO-overheidsmaatregelen** — verplichte maatregelen gestructureerd volgens ISO 27001 bijlage A / ISO 27002. Circa 100 overheidsmaatregelen, genummerd op basis van de bijbehorende ISO-beheersmaatregel.

## Kernbegrippen

- **Managementsysteem voor informatiebeveiliging (ISMS)** — werkwijze om informatiebeveiliging gestructureerd toe te passen; niet een applicatie maar een organisatorisch systeem op basis van ISO 27001. Borgt beschikbaarheid, integriteit en vertrouwelijkheid.
- **Verklaring van Toepasselijkheid (VvT)** — verplicht document (ISO 27001) waarin de entiteit vastlegt welke beheersmaatregelen zijn geïmplementeerd en welke zijn uitgezonderd. Overheidsmaatregelen worden expliciet opgenomen.
- **Risicoregister** — register met tijdelijk geaccepteerde risico's en het proces voor opvolging.
- **Informatiebeveiligingsbeleid** — door bestuur vastgesteld beleid met uitgangspunten, organisatie van de beveiligingsfunctie, betrouwbaarheidseisen en evaluatiefrequentie (maatregel 5.01.01).
- **In Control Verklaring (ICV)** — jaarlijkse verklaring over de gehele informatiebeveiliging, afgelegd als onderdeel van de P&C-cyclus onder coördinatie van de CISO (maatregel 5.36.01).
- **CISO** — Chief Information Security Officer, verantwoordelijk voor coördinatie informatiebeveiliging, onafhankelijk advies aan bestuur (maatregel 5.02.02).
- **Informatiebeveiligingsincident** — breed begrip dat datalekken omvat; meldplicht bij CSIRT binnen wettelijke termijn (maatregel 5.24.07).
- **Overheidsmaatregel** — verplicht toe te passen beveiligingsmaatregel op tactisch niveau, aanvullend op ISO 27002. Kan niet op basis van risicoafweging worden geaccepteerd.

## Verplichtingen

De BIO stelt drie kernverplichtingen:
1. ISO 27001 toepassen voor het ISMS — minimaal kritische bedrijfsprocessen en informatiesystemen in scope.
2. ISO 27002 + verplichte overheidsmaatregelen toepassen als beheersmaatregelen.
3. Opzet, bestaan en werking van maatregelen aantonen — via audits, pentesten, red-teamtesten.

## Governance-rollen

> "De bestuurder is verantwoordelijk voor het treffen van passende en evenredige technische, operationele en organisatorische maatregelen" (§12.1)

- **Bestuurder** — eindverantwoordelijk voor risicomanagement en digitale weerbaarheid
- **Lijnmanagement** — eigenaar van informatie(systemen), verantwoordelijk voor toepassing maatregelen
- **CISO** — coördinatie, advies aan bestuur, rapportage over implementatie
- **Interne toezichthouder** — ondersteunt bestuurder bij toezicht

## Relevantie voor bedrijfsarchitectuur

De BIO2 is een governance-kader zonder concrete registratieobjecten. Alle begrippen zijn governance-instrumenten (beleid, VvT, ICV), processen (risicomanagement, incidentbeheer) of actoren (CISO, bestuurder). De BIO2 levert geen nieuwe BO's op.

De BIO2 geeft wel context bij bestaande BO's:
- [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/datalek|Datalek]] — de BIO schrijft meldplicht bij CSIRT voor (maatregel 5.24.07) en bewaartermijn van 3 jaar voor incidentinformatie (5.28.01)
- [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/dpia|DPIA]] — de BIO verplicht risicoafwegingen bij nieuwe informatiesystemen (5.08.01) die verwant zijn aan DPIA's

## Relevante citaten

> "De BIO is van toepassing op de informatiebeveiliging van alle typen omgevingen, onder andere operationele technologie (OT) en zorginformatie." (§3)

> "Het toepassen van de BIO voor de beveiliging van netwerk- en informatiesystemen is via de Cbw verplicht voor alle entiteiten die vallen onder de sector 'Overheid'." (§11.1)

> "Informatieveiligheid is een standaard onderdeel van het jaarverslag van de organisatie." (§9)

## Bronnen

- [[Sources/Onderwerpen/Informatiesamenleving/bio2-baseline-informatiebeveiliging-overheid]]
