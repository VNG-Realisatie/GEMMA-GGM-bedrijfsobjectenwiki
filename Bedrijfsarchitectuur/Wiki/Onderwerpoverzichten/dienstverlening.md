---
type: domein
naam: Dienstverlening
status: afgerond
verwerkingsdatum: 2026-09-23
bronnen_count: 9
begrippen_count: 30
bo_count: 16
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
|[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]]|object|Afgebakende werkeenheid met aanleiding, doorlooptijd en resultaat; organiserend principe voor dienstverlening| ✅ | ja |6/6 criteria, exact match|Vergunningaanvraag, bijstandszaak, melding openbare ruimte|ja|
|[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document\|Document]]|object|Informatiedrager ongeacht vorm, ontvangen of opgemaakt bij taakuitvoering (ZTC2: informatieobject)| ✅ | ja |6/6 criteria, exact match|PDF-aanvraag, e-mail, scan, foto, dataset|ja|
|[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]]|object|Verzoek of signaal aan de gemeente, startpunt dienstverlening| ✅ | ja |6/6 criteria, sterk match|Bijstandsaanvraag, MOR-melding, DigiD-vraag|ja|
|[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/balieafspraak\|Balieafspraak]]|object|Geplande afspraak voor een klantcontact aan de balie| ✅ | ja |6/6 criteria, exact match|Afspraak paspoort, afspraak sociaal raadslid|ja|
|[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/product-of-dienst\|Product of dienst]]|object|Door de gemeente aangeboden dienst of product| ✅ | ja |6/6 criteria, sterk match|Paspoort, bijstandsuitkering, bouwvergunning|ja|
|informatieobject|synoniem|ZGW API's / ZTC2-naam voor dezelfde entiteit als GGM "Document"; bredere term dan dagelijks begrip "document"| ❌ | ja |Synoniem van [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document\|Document]] (identieke definitie); geen apart BO|PDF, XML-bericht, scan, dataset, e-mail|ja (= Document)|
|zaakdossier|concept|Zaakkenmerken + informatieobjecten samen; basis voor archivering| ❌ | nee |Impliciet concept (RGBZ): geen apart objecttype maar de verzameling van zaak + documenten|Zaakdossier vergunningaanvraag|nee|
|zaaktypecatalogus|object|Verzameling zaaktypen met configuratie per domein| ✅ | ja |BO, partieel match (ZTC2-standaard)|ZTC per gemeente|partieel|
|resultaattype|object|Mogelijke uitkomsten per zaaktype, bepaalt archiefregime| ✅ | ja |BO, exact match (ZTC2)|Verleend, Geweigerd, Buiten behandeling|ja|
|IDO (Informatiepunt Digitale Overheid)|actor|Fysiek hulppunt in bibliotheken voor digitale overheidsvragen| ❌ | nee |Actor/locatietype, geen eigen levenscyclus als gemeentelijk concept|IDO in bibliotheek Amsterdam|nee|
|[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/besluit\|Besluit]]|object|Formele beslissing op een individueel geval binnen een zaak| ✅ | ja |6/6 criteria, exact match|Vergunningbesluit, toekenning uitkering, bezwaarbesluit|ja|
|[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/klantcontact\|Klantcontact]]|object|Contactmoment dat werkelijk heeft plaatsgevonden tussen burger/bedrijf en gemeente| ✅ | ja |6/6 criteria, exact match|Telefooncontact, baliebezoek, e-mailcontact|ja|
|[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/betaling\|Betaling]]|object|Overboeken of ontvangen van geld in het kader van een zaak| ✅ | ja |6/6 criteria, exact match|Legesbetaling, uitkeringsuitbetaling|ja|
|[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/bedrijfsproces\|Bedrijfsproces]]|object|Reeks activiteiten die bijdraagt aan levering van een product of dienst| ✅ | ja |6/6 criteria, exact match|Vergunningproces, uitkeringsproces|ja|
|[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/medewerker\|Medewerker]]|actor|Medewerker van de organisatie die zaken behandelt| ✅ | ja |6/6 criteria, exact match|Vergunningverlener, klantadviseur|ja|
|[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/organisatorische-eenheid\|Organisatorische eenheid]]|actor|Functioneel afgebakend onderdeel dat verantwoordelijk is voor zaakbehandeling| ✅ | ja |6/6 criteria, exact match|Afdeling Vergunningen, team Burgerzaken|ja|
|[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaaktype\|Zaaktype]]|object|Definitie van een soort zaak met doorlooptijd, servicenorm en archiefcode| ✅ | ja |6/6 criteria, exact match|Omgevingsvergunning regulier, bijstandsaanvraag|ja|
|ZAAK - Origineel|object|GGM-variant van Zaak met zelfde definitie| ❌ | ja |Duplicaat van [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]]|—|ja|
|Statustype|object|Generieke aanduiding van de aard van een status| ❌ | ja |Attribuut/modelleringskeuze, geen zelfstandig BO|In behandeling, Afgerond|ja|
|Status|object|Stand van zaken van een zaak| ❌ | ja |Voortgangsindicatie op Zaak, geen zelfstandig BO|Status "in behandeling" op zaak|ja|
|Besluittype|object|Generieke aanduiding van de aard van een besluit| ❌ | ja |Typering bij Besluit — waardelijst|Vergunningbesluit, subsidiebesluit|ja|
|[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/vergunningen-en-ontheffingen\|Vergunningen en ontheffingen]]|object|Domeinoverstijgend parent-BO: formeel besluit met toestemming voor een activiteit of uitzondering op een verbod| ✅ | ja |6/6 criteria, procesobject|Omgevingsvergunning, kapvergunning, evenementenvergunning|nee (hiaat)|
|[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/woo-verzoek\|Woo-verzoek]]|object|Verzoek om openbaarmaking publieke informatie (art. 4.1 Woo)| ✅ | ja |6/6 criteria, wettelijk verplicht; primair vastgelegd onder Informatiesamenleving|Verzoek om raadsstukken, interne memo's|nee (hiaat)|
|[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/klacht\|Klacht]]|object|Uiting van ontevredenheid over gedraging bestuursorgaan (titel 9.1 Awb)| ✅ | ja |6/6 criteria, wettelijk verplicht; primair vastgelegd onder Informatiesamenleving|Klacht over behandeling aan balie|nee (hiaat)|

## Bedrijfsobjecten

| Begrip | Status | GGM-grondslag | Matchsterkte |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] | ✅ BO | Zaak (RGBZPlus) | exact |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document\|Document]] | ✅ BO | Document (RGBZPlus) | exact |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | ✅ BO | AanvraagOfMelding (Model Dienstverlening) | sterk |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/balieafspraak\|Balieafspraak]] | ✅ BO | Balieafspraak (Model Dienstverlening) | exact |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/product-of-dienst\|Product of dienst]] | ✅ BO | ProductOfDienst (Model Dienstverlening) | sterk |
| zaaktypecatalogus | ✅ BO | CATALOGUS (ZTC2) | partieel |
| resultaattype | ✅ BO | RESULTAATTYPE (ZTC2) | exact |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/besluit\|Besluit]] | ✅ BO | Besluit (RGBZPlus) | exact |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/klantcontact\|Klantcontact]] | ✅ BO | Klantcontact (RGBZPlus) | exact |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/betaling\|Betaling]] | ✅ BO | Betaling (RGBZPlus) | exact |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/bedrijfsproces\|Bedrijfsproces]] | ✅ BO | Bedrijfsproces (RGBZPlus) | exact |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/medewerker\|Medewerker]] | ✅ BO | Medewerker (RGBZPlus) | exact |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/organisatorische-eenheid\|Organisatorische eenheid]] | ✅ BO | OrganisatorischeEenheid (RGBZPlus) | exact |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaaktype\|Zaaktype]] | ✅ BO | Zaaktype (RGBZPlus) | exact |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/vergunningen-en-ontheffingen\|Vergunningen en ontheffingen]] | ✅ BO | — | geen match (procesobject, hiaat) |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/woo-verzoek\|Woo-verzoek]] | ✅ BO | — | geen match (hiaat); primair Informatiesamenleving |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/klacht\|Klacht]] | ✅ BO | — | geen match (hiaat); primair Informatiesamenleving |

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
- [Sources/GGM/10-dienstverlening/dienstverlening.md](Wiki/GGM/10-dienstverlening/dienstverlening.md) — 16 entiteiten Model Dienstverlening

## Evolutie

Het RGBZ 1.0 (2010) is de huidige officiële standaard. RGBZ 2.0 heeft nooit een officiële status bereikt, maar concepten eruit zijn overgenomen in de **ZGW API's** (REST/JSON), die wél officieel zijn. De ZGW API's zijn de opvolger van de StUF-ZKN berichtenstandaard.

## Openstaande vragen

- De ZTC2-configuratielaag ontbreekt in het GGM. Is dit een bewuste keuze (de ZTC2 is een apart informatiemodel) of een hiaat?
- Hoe actueel is het GGM-beleidsdomein RGBZPlus gezien de evolutie RGBZ 1.0 → RGBZ 2.0 (concept) → ZGW API's?
- Klantbeoordeling: bij toekomstige bronnen over klanttevredenheidsbeleid heroverwegen als BO-kandidaat?

## Terugmeldingen richting GGM

- **AanvraagOfMelding**: definitie "Komt overeen met een VJV" is een systeemreferentie, geen inhoudelijke definitie
- **ProductOfDienst**: definitie "Bron: QP_CALENDAR.CFM_SERVICES" is een systeemreferentie, geen inhoudelijke definitie

## Conclusie

Domein afgerond: 9 bronnen verwerkt, 16 BO's vastgelegd (grotendeels exacte RGBZPlus/ZTC2-matches). De 3 openstaande vragen zijn vooruitkijkende onderzoeksnotities over standaardevolutie (RGBZ 1.0→2.0→ZGW API's, ZTC2-status) en toekomstige klantbeoordelingsbronnen — geen blokkerende BO-classificatievraag, blijven gedocumenteerd staan.

**2026-09-23 sync-correctie:** de map `Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/` bevatte 3 BO's die hier nooit waren opgenomen: [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/vergunningen-en-ontheffingen|Vergunningen en ontheffingen]] (eigen aan dit domein) en [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/woo-verzoek|Woo-verzoek]]/[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/klacht|Klacht]] (primair vastgelegd onder Informatiesamenleving, hier cross-getagd). Toegevoegd aan de begrippentabel. Overige 8 BO's in die map (algoritmeregister, datalek, dpia, grondrechteneffectbeoordeling, verwerkersovereenkomst, verwerkingsactiviteit, informatieobject) horen inhoudelijk bij Informatiesamenleving resp. Informatiebeheer en staan daar al correct — bewust niet ook hier opgenomen.
