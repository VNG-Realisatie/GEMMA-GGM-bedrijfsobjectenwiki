---
type: domein
naam: Dienstverlening
status: in-behandeling
verwerkingsdatum: 2026-06-19
bronnen_count: 9
begrippen_count: 14
bo_count: 7
---

# Domein: Dienstverlening

Gemeentelijke dienstverlening — zaakgericht werken, zaaktypecatalogi, klantcontact, producten- en dienstencatalogus, en de informatiestandaarden die het dienstverleningsproces ondersteunen. Dit domein is domeinoverstijgend: het levert de generieke structuur waarmee alle gemeentelijke domeinen hun dienstverlening organiseren.

## Begrippen

|Begrip|Type|Omschrijving|BO?| Data-object |Reden|Voorbeelden|GGM|
|---|---|---|---|---|---|---|---|
|zaakgericht werken|thema|Werkwijze: dienstverlening organiseren rond zaken| ❌ | nee |Werkwijze, geen object|—|nee|
|overheidsbrede dienstverlening|thema|Integrale werkwijze: inwoners helpen met vragen aan meerdere overheidsorganisaties| ❌ | nee |Werkwijze/organisatiemodel|BZK-programma overheidsbrede loketten|nee|
|digitale toegankelijkheid|thema|Kwaliteitskenmerk van gemeentelijke digitale kanalen (Wdo)| ❌ | nee |Kwaliteitskenmerk, geen object|Toegankelijkheidsverklaring, WCAG|nee|
|gemeentelijke inkoop|thema|Het geheel van inkoopactiviteiten (€40+ mrd)| ❌ | nee |Thema, geen object|—|nee|
|aanbesteding|instrument|Verplichte inkoopprocedure boven drempelbedragen| ❌ | nee |Instrument/procedure|Europese aanbesteding, meervoudig onderhands|nee|
|MVOI|instrument|Maatschappelijk verantwoord opdrachtgeven en inkopen| ❌ | nee |Instrument/beleidskader|Manifest MVOI, actieplan MVOI|nee|
|[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]]|object|Verzoek of signaal aan de gemeente, startpunt dienstverlening| ✅ | ja |6/6 criteria, sterk match|Bijstandsaanvraag, MOR-melding, DigiD-vraag|ja|
|[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/balieafspraak\|Balieafspraak]]|object|Geplande afspraak voor een klantcontact aan de balie| ✅ | ja |6/6 criteria, exact match|Afspraak paspoort, afspraak sociaal raadslid|ja|
|[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/product-of-dienst\|Product of dienst]]|object|Door de gemeente aangeboden dienst of product| ✅ | ja |6/6 criteria, sterk match|Paspoort, bijstandsuitkering, bouwvergunning|ja|
|zaaktypecatalogus|object|Verzameling zaaktypen met configuratie per domein| ✅ | ja |BO, partieel match (ZTC2-standaard)|ZTC per gemeente|partieel|
|informatieobject|object|Geheel van gegevens ongeacht vorm (breder dan "document")| ✅ | ja |6/6 criteria, sterk match|PDF-aanvraag, e-mail, scan|ja|
|zaakdossier|object|Zaakkenmerken + informatieobjecten, basis voor archivering| ✅ | ja |6/6 criteria, sterk match|Zaakdossier vergunningaanvraag|ja|
|resultaattype|object|Mogelijke uitkomsten per zaaktype, bepaalt archiefregime| ✅ | ja |BO, exact match (ZTC2)|Verleend, Geweigerd, Buiten behandeling|ja|
|IDO (Informatiepunt Digitale Overheid)|actor|Fysiek hulppunt in bibliotheken voor digitale overheidsvragen| ❌ | nee |Actor/locatietype, geen eigen levenscyclus als gemeentelijk concept|IDO in bibliotheek Amsterdam|nee|

## Bedrijfsobjecten

| Begrip | Status | GGM-grondslag | Matchsterkte |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | ✅ BO | AanvraagOfMelding (Model Dienstverlening) | sterk |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/balieafspraak\|Balieafspraak]] | ✅ BO | Balieafspraak (Model Dienstverlening) | exact |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/product-of-dienst\|Product of dienst]] | ✅ BO | ProductOfDienst (Model Dienstverlening) | sterk |
| zaaktypecatalogus | ✅ BO | CATALOGUS (ZTC2) | partieel |
| informatieobject | ✅ BO | Document (RGBZPlus) | sterk |
| zaakdossier | ✅ BO | Zaak (RGBZPlus) | sterk |
| resultaattype | ✅ BO | RESULTAATTYPE (ZTC2) | exact |

## Informatiestandaarden

| Standaard | Versie | Scope |
|---|---|---|
| **RGBZ** | 1.0 (2010) | Runtime-datamodel: zaakgegevens, betrokkenen, documenten, statussen, besluiten |
| **ZTC2** | 2.1 (2014) | Configuratielaag: zaaktypen, statustypes, resultaattypes, roltypes, eigenschappen |
| **RSGB** | 2.02 (2018) | Basisgegevens: de objecten waarop zaken betrekking hebben |
| **StUF-Zaken** | 3.10 (2010) | Berichtenstandaard afgeleid van het RGBZ |

## Verwerkte bronnen

### Standaarden
- [[Wiki/Bronsamenvattingen/Standaarden/rgbz-informatiemodel|Referentiemodel Gemeentelijke Basisgegevens Zaken (RGBZ) 1.0]] — referentiemodel zaakgegevens, berichtenarchitectuur, evolutie naar ZGW API's
- [[Wiki/Bronsamenvattingen/Standaarden/ztc2-informatiemodel|GEMMA Zaaktypecatalogus 2 (ZTC2) — Informatiemodel v2.1]] — informatiemodel zaaktypecatalogus

### VNG-bronnen Dienstverlening
- [[Wiki/Bronsamenvattingen/Dienstverlening/raadgever-inkoop-en-aanbesteden|Raadgever Inkoop en aanbesteden]] — inkoop, aanbestedingsregels en MVOI
- [[Wiki/Bronsamenvattingen/Dienstverlening/hand-out-overheidsbrede-dienstverlening|Hand-out overheidsbrede dienstverlening voor gemeenten]] — BZK-programma overheidsbrede loketten, professionallijnen, IDO's
- [[Wiki/Bronsamenvattingen/Dienstverlening/overheidsbrede-startscan|Overheidsbrede Startscan voor gemeenten]] — implementatiemethodiek overheidsbrede dienstverlening
- [[Wiki/Bronsamenvattingen/Dienstverlening/rubriek-dienstverlening|VNG-rubriek Dienstverlening en bedrijfsvoering]] — portaalpagina GGU, leveranciersmanagement, MijnServices
- [[Wiki/Bronsamenvattingen/Dienstverlening/online-dienstverlening|Online dienstverlening]] — Wmebv, MijnServices, IDO's
- [[Wiki/Bronsamenvattingen/Dienstverlening/digitale-toegankelijkheid|Digitale toegankelijkheid]] — Wdo, toegankelijkheidsverklaring
- [[Wiki/Bronsamenvattingen/Dienstverlening/inkoop-en-aanbesteden|Inkoop en aanbesteden (overzichtspagina)]] — portaalpagina, overlapt met raadgever

### GGM-bron
- [Sources/GGM/10-dienstverlening/dienstverlening.md](Sources/GGM/10-dienstverlening/dienstverlening.md) — 16 entiteiten Model Dienstverlening

## Evolutie

Het RGBZ 1.0 (2010) is de huidige officiële standaard. RGBZ 2.0 heeft nooit een officiële status bereikt, maar concepten eruit zijn overgenomen in de **ZGW API's** (REST/JSON), die wél officieel zijn. De ZGW API's zijn de opvolger van de StUF-ZKN berichtenstandaard.

## Openstaande vragen

- De ZTC2-configuratielaag ontbreekt in het GGM. Is dit een bewuste keuze (de ZTC2 is een apart informatiemodel) of een hiaat?
- Hoe actueel is het GGM-beleidsdomein RGBZPlus gezien de evolutie RGBZ 1.0 → RGBZ 2.0 (concept) → ZGW API's?
- Klantbeoordeling: bij toekomstige bronnen over klanttevredenheidsbeleid heroverwegen als BO-kandidaat?

## Terugmeldingen richting GGM

- **AanvraagOfMelding**: definitie "Komt overeen met een VJV" is een systeemreferentie, geen inhoudelijke definitie
- **ProductOfDienst**: definitie "Bron: QP_CALENDAR.CFM_SERVICES" is een systeemreferentie, geen inhoudelijke definitie
