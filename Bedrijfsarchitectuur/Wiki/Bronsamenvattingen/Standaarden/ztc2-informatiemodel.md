---
type: bronsamenvatting
titel: "GEMMA Zaaktypecatalogus 2 (ZTC2) — Informatiemodel v2.1"
domein: [Dienstverlening]
datum_ingest: 2026-06-18
begrippen_geextraheerd: [zaaktypecatalogus, resultaattype]
---

# Bronsamenvatting: ZTC2 Informatiemodel v2.1

**Bron:** GEMMA Zaaktypecatalogus 2 — Informatiemodel, versie 2.1 (KING, juli 2014)

## Doel en positionering

De ZTC2 definieert de structuur van zaaktypecatalogi: welke kenmerken een zaaktype heeft, wat ze betekenen en hoe ze zich tot elkaar verhouden. Het is de **configuratielaag** bovenop het RGBZ: waar het RGBZ de runtime-data beschrijft (zaken, statussen, documenten), beschrijft de ZTC2 de configuratie (zaaktypen, statustypes, resultaattypen).

> "Bij het ontwerp van de GEMMA Zaaktypecatalogus (ZTC) 2 is vooral gefocust op maximale aansluiting van de ZTC op het Referentiemodel Gemeentelijke Basisgegevens Zaken (RGBZ)."

**Kernonderscheid RGBZ vs. ZTC2:**
- RGBZ: instanties — een specifieke ZAAK met een specifieke STATUS
- ZTC2: typen — het ZAAKTYPE met de mogelijke STATUSTYPEn

## Objecttypen

De ZTC2 kent 9 objecttypen en 3 relatieklassen, georganiseerd binnen een CATALOGUS:

### Catalogusstructuur

| Objecttype | Definitie | Nieuw t.o.v. RGBZ |
|---|---|---|
| **CATALOGUS** | Verzameling van ZAAKTYPEn voor een domein, beheerd als één geheel. Uniek per RSIN + Domein. | Ja |
| **ZAAKTYPE** | Het geheel van karakteristieke eigenschappen van zaken van eenzelfde soort. Afbakening = bedrijfsproces "van klant tot klant". | Uitbreiding |

### Configuratie per zaaktype

| Objecttype | Definitie | Nieuw t.o.v. RGBZ |
|---|---|---|
| **STATUSTYPE** | Generieke aanduiding van de aard van een STATUS. Met checklistitems, doorlooptijdnorm en informatieverplichting. | Uitbreiding |
| **RESULTAATTYPE** | Indeling van resultaten naar hun aard (verleend, geweigerd, etc.). Bepaalt het archiefregime: vernietigen of bewaren. | Ja |
| **ROLTYPE** | Generieke aanduiding van de aard van een ROL (bijv. aanvrager, behandelaar, adviseur). Met generieke en specifieke benamingen. | Ja |
| **EIGENSCHAP** | Zaaktypespecifiek gegeven dat niet als standaard zaakkenmerk in het RGBZ zit (bijv. "Datum evenement" bij evenementenvergunning). | Ja |
| **INFORMATIEOBJECTTYPE** | Aanduiding van de aard van informatieobjecten — vervangt DOCUMENTTYPE met bredere scope. | Naamswijziging |
| **BESLUITTYPE** | Generieke aanduiding van de aard van een BESLUIT (bouwvergunning, ontheffing, subsidie). | Uit RGBZ |
| **ZAAKOBJECTTYPE** | De objecttypen waarop een zaak van het ZAAKTYPE betrekking kan hebben — maakt het mogelijk registratie af te dwingen. | Ja |

### Relatieklassen

| Relatieklasse | Beschrijving |
|---|---|
| **ZAAK-INFORMATIEOBJECT-TYPE** | Welke informatieobjecttypen relevant zijn per zaaktype, met richting (inkomend/uitgaand). |
| **ZAAK-INFORMATIEOBJECT-TYPE ARCHIEFREGIME** | Afwijkende archiveringskenmerken voor specifieke informatieobjecten bij bepaalde resultaten. |
| **ZAAKTYPENRELATIE** | Relaties tussen zaaktypen: deelzaken, vervolgzaken, bijdragezaken, betrekking-op-zaken. |

## Kernconcepten

### Zaaktype = bedrijfsproces
> "Het traject van (aan)vraag cq. aanleiding voor de zaak tot en met de levering van de producten/of diensten die een passend antwoord vormen op die aanleiding, bepaalt de omvang en afbakening van de zaak en daarmee van het zaaktype. Hiermee komt de afbakening van een zaaktype overeen met een bedrijfsproces: 'van klant tot klant'."

Onderdelen van bedrijfsprocessen vormen geen zelfstandige zaken. Een aanleiding die niet leidt tot de start van een bedrijfsproces leidt niet tot een zaak.

### Resultaattype en archivering
Het RESULTAATTYPE is cruciaal voor correct archiveren: het bepaalt of een zaakdossier vernietigd of blijvend bewaard moet worden, en na welke termijn. In uitzonderingsgevallen kan het archiefregime van individuele informatieobjecten afwijken van het zaakdossier als geheel.

### Van document naar informatieobject
De ZTC2 vervangt "document" door "informatieobject": een generiekere term die ook foto's, datasets, geluidsopnames, webpagina's etc. omvat. De fysieke vorm is niet bepalend voor wat als informatieobject beschouwd wordt.

### Meerdere catalogi
Er kan niet één landelijke zaaktypecatalogus bestaan. Er zullen catalogi zijn per organisatie, per sector en per keten. Het CATALOGUS-objecttype maakt dit mogelijk met een unieke identificatie per domein + eigenaar.

### Eigenschap als extensiemechanisme
EIGENSCHAP voorziet in zaaktypespecifieke gegevens die niet als standaard zaakkenmerk in het RGBZ zitten. Het biedt twee specificatiewijzen: (a) eenvoudig via formaat/lengte/waardenverzameling, (b) via referentie naar een extern informatiemodel en XML-schema.

## Context en gebruik (uit Begeleidend document)

De ZTC2 is niet één landelijke catalogus maar een **sjabloon** voor zaaktypecatalogi. Organisaties, sectoren en ketens maken eigen catalogi gevuld met hun zaaktypen.

> "KING is na uitvoerig onderzoek tot de conclusie gekomen dat de verbreding die voor aansluiting van de zaaktypecatalogus op RGBZ nodig is, niet valt te combineren met een uitputtende lijst van in hoge mate gestandaardiseerde zaaktypen binnen één, door KING te ontwikkelen en beheren, catalogus voor gemeenten."

**Functie van de ZTC2:**
1. **Configuratie-instrument** — zaaktypen parametriseren generieke referentieprocessen (doorlooptijden, documenten, rollen, besluiten)
2. **Communicatie-instrument** — "het goede gesprek" over zaakgericht werken, gemeenschappelijke taal
3. **Managementinformatie** — KPI's via doorlooptijden, statussen, resultaten per zaaktype
4. **Systeemconfiguratie** — zaaksystemen lezen parameters uit de ZTC en configureren procesondersteuning

**Relaties met andere bouwstenen:**
- PDC → Zaaktype: 1:n (één zaaktype kan meerdere producten opleveren)
- Formulier → Zaaktype: n:1 (meerdere formulieren leiden tot zaken van één zaaktype)
- Referentieproces → Zaaktype: 1:n (zaaktypen parametriseren een generiek proces)
- RGBZ ↔ ZTC2: twee-eenheid (runtime-data vs. configuratie)

**Beheermodel:**
- **KING:** sjablonen, informatiemodel, uitwisselformaat, referentiezaaktypen, validatie
- **Gemeenten/sectoren:** inhoud van eigen catalogi
- **Landelijke publicatie:** KING valideert conformiteit, publiceert catalogi met keurmerk

**Omvang per zaaktype:** ~300 attribuut- en relatiesoorten (32 zaaktype-attrs + statustypen, documenttypen, besluittypen, resultaattypen, roltypen, eigenschappen, zaakobjecttypen).

## Relevantie voor bedrijfsarchitectuur

- De ZTC2 definieert objecttypen die **niet** in het GGM zitten: CATALOGUS, RESULTAATTYPE, EIGENSCHAP, ZAAKOBJECTTYPE, ROLTYPE
- Het GGM-beleidsdomein RGBZPlus bevat de RGBZ-kern maar niet de ZTC2-configuratielaag — dit is een structureel hiaat
- De ZTC2-concepten zijn essentieel voor hoe gemeenten zaakgericht-werken inrichten
- zaaktypecatalogus en resultaattype zijn begrippen die uit deze bron komen
- De relatie ZAAKTYPE = bedrijfsproces maakt de brug naar de GEMMA-procesarchitectuur

## Bronnen

- [[Sources/Standaarden/ztc2-informatiemodel-v2.1]]
- [[Sources/Onderwerpen/Standaarden/ztc2-begeleidend-document]]
