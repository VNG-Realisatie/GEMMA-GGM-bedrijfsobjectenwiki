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

## GGM-taakvelden

Dit wiki-domein raakt twee GGM-taakvelden:
- **Taakveld 10 Dienstverlening** — meldingen, aanvragen, baliecontacten, telefonische afhandeling, formulieren, klantbeoordelingen en producten/diensten (16 entiteiten)
- **Taakveld 99 Kern / RGBZPlus** — de zaakgerichte kern: Zaak, Status, Besluit, Document, Betrokkene, Medewerker (25 entiteiten)

De ZTC2-configuratielaag (CATALOGUS, RESULTAATTYPE, EIGENSCHAP, ROLTYPE, ZAAKOBJECTTYPE) is niet in het GGM gemodelleerd.

## Begrippen

| Begrip | Type | Omschrijving | BO? | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|
| [[zaakgericht-werken]] | thema | Werkwijze: dienstverlening organiseren rond zaken | ❌ | Werkwijze, geen object | — | nee |
| overheidsbrede dienstverlening | thema | Integrale werkwijze: inwoners helpen met vragen aan meerdere overheidsorganisaties | ❌ | Werkwijze/organisatiemodel | BZK-programma overheidsbrede loketten | nee |
| digitale toegankelijkheid | thema | Kwaliteitskenmerk van gemeentelijke digitale kanalen (Wdo) | ❌ | Kwaliteitskenmerk, geen object | Toegankelijkheidsverklaring, WCAG | nee |
| [[gemeentelijke-inkoop]] | thema | Het geheel van inkoopactiviteiten (€40+ mrd) | ❌ | Thema, geen object | — | nee |
| [[aanbesteding]] | instrument | Verplichte inkoopprocedure boven drempelbedragen | ❌ | Instrument/procedure | Europese aanbesteding, meervoudig onderhands | nee |
| [[mvoi]] | instrument | Maatschappelijk verantwoord opdrachtgeven en inkopen | ❌ | Instrument/beleidskader | Manifest MVOI, actieplan MVOI | nee |
| [[aanvraag-of-melding]] | object | Verzoek of signaal aan de gemeente, startpunt dienstverlening | ✅ | 6/6 criteria, sterk match | Bijstandsaanvraag, MOR-melding, DigiD-vraag | ja |
| [[balieafspraak]] | object | Geplande afspraak voor een klantcontact aan de balie | ✅ | 6/6 criteria, exact match | Afspraak paspoort, afspraak sociaal raadslid | ja |
| [[product-of-dienst]] | object | Door de gemeente aangeboden dienst of product | ✅ | 6/6 criteria, sterk match | Paspoort, bijstandsuitkering, bouwvergunning | ja |
| [[zaaktypecatalogus]] | object | Verzameling zaaktypen met configuratie per domein | ✅ | BO, partieel match (ZTC2-standaard) | ZTC per gemeente | partieel |
| [[informatieobject]] | object | Geheel van gegevens ongeacht vorm (breder dan "document") | ✅ | 6/6 criteria, sterk match | PDF-aanvraag, e-mail, scan | ja |
| [[zaakdossier]] | object | Zaakkenmerken + informatieobjecten, basis voor archivering | ✅ | 6/6 criteria, sterk match | Zaakdossier vergunningaanvraag | ja |
| [[resultaattype]] | object | Mogelijke uitkomsten per zaaktype, bepaalt archiefregime | ✅ | BO, exact match (ZTC2) | Verleend, Geweigerd, Buiten behandeling | ja |
| IDO (Informatiepunt Digitale Overheid) | actor | Fysiek hulppunt in bibliotheken voor digitale overheidsvragen | ❌ | Actor/locatietype, geen registratieobject | IDO in bibliotheek Amsterdam | nee |

## Bedrijfsobjecten

| Begrip | Status | GGM-grondslag | Matchsterkte |
|---|---|---|---|
| [[aanvraag-of-melding]] | ✅ BO | AanvraagOfMelding (Model Dienstverlening) | sterk |
| [[balieafspraak]] | ✅ BO | Balieafspraak (Model Dienstverlening) | exact |
| [[product-of-dienst]] | ✅ BO | ProductOfDienst (Model Dienstverlening) | sterk |
| [[zaaktypecatalogus]] | ✅ BO | CATALOGUS (ZTC2) | partieel |
| [[informatieobject]] | ✅ BO | Document (RGBZPlus) | sterk |
| [[zaakdossier]] | ✅ BO | Zaak (RGBZPlus) | sterk |
| [[resultaattype]] | ✅ BO | RESULTAATTYPE (ZTC2) | exact |

## GGM-entiteitendekking

| GGM-beleidsdomein | Entiteiten | BO | Niet-BO | Niet beoordeeld | Reden niet beoordeeld |
|---|---|---|---|---|---|
| Model Dienstverlening (tv. 10) | 16 | 3 | 9 | 4 | Klantbeoordeling, Telefoontje, Telefoononderwerp, Telefoonstatus: operationeel/kwaliteitsregistratie, niet uit beleidsbronnen |
| RGBZPlus (tv. 99 Kern) | 25 | 2 | 23 | 0 | — |

### Niet-BO entiteiten Model Dienstverlening

| GGM-entiteit | Reden niet-BO |
|---|---|
| Aanvraagdata | Attribuutwaarden van AanvraagOfMelding, geen eigen bestaan |
| Afspraakstatus | Statuswaarde van Balieafspraak |
| Artikel | Publicatieobject, geen gemeentelijk registratieobject |
| ExterneBron | Technische herkomstverwijzing |
| Formuliersoort | Configuratie-object (template), geen bedrijfsobject |
| Formuliersoortveld | Velden binnen een formuliertemplate |
| Klantbeoordelingreden | Detailwaarde van Klantbeoordeling |
| MOR-AanvraagOfMelding | Specialisatie van AanvraagOfMelding, opgenomen in het generieke BO |
| Onderwerp | Classificatiewaarde, geen eigen bestaan |

### Twijfelgevallen (beoordeeld, niet als BO opgenomen)

- **Klantbeoordeling**: heeft meervoud en levenscyclus, maar is een kwaliteitsmetric, geen kern-bedrijfsobject. Kan bij toekomstige bronnen over klanttevredenheidsbeleid heroverwogen worden.
- **Telefoontje**: individueel telefoongesprek met technische attributen (trackID, ISDNconnectie). Te granulair en te operationeel voor bedrijfsniveau.

## GGM-dekkingsanalyse

Het GGM modelleert dienstverlening in twee lagen:

**Taakveld 10 (Model Dienstverlening)** bevat de kanaal- en contactregistratie: aanvragen/meldingen, balieafspraken, telefooncontacten, formulieren, producten/diensten en klantbeoordelingen. Drie entiteiten worden BO: AanvraagOfMelding, Balieafspraak en ProductOfDienst. De overige zijn attributen, statuswaarden, classificaties of specialisaties.

**Taakveld 99 Kern (RGBZPlus)** bevat de zaakgerichte kern: Zaak, Status, Besluit, Document, Betrokkene, Medewerker. Twee entiteiten worden BO in dit domein (Zaak → zaakdossier, Document → informatieobject). De overige zijn attribuutobjecten of raken andere domeinen.

**Structureel hiaat:** de ZTC2-configuratielaag (CATALOGUS, RESULTAATTYPE, EIGENSCHAP, ROLTYPE, ZAAKOBJECTTYPE) is een extern informatiemodel dat niet in het GGM is opgenomen. Zaaktypecatalogus en resultaattype zijn als BO opgenomen op basis van de ZTC2-standaard, niet op basis van GGM-entiteiten.

**Beleidslaag:** de VNG-bronnen over overheidsbrede dienstverlening, digitale toegankelijkheid en online dienstverlening beschrijven werkwijzen, organisatiemodellen en wettelijke verplichtingen — geen nieuwe data-objecten. Dit is structureel: het GGM modelleert wat gemeenten registreren, niet hoe ze hun dienstverlening organiseren.

## Informatiestandaarden

| Standaard | Versie | Scope |
|---|---|---|
| **RGBZ** | 1.0 (2010) | Runtime-datamodel: zaakgegevens, betrokkenen, documenten, statussen, besluiten |
| **ZTC2** | 2.1 (2014) | Configuratielaag: zaaktypen, statustypes, resultaattypes, roltypes, eigenschappen |
| **RSGB** | 2.02 (2018) | Basisgegevens: de objecten waarop zaken betrekking hebben |
| **StUF-Zaken** | 3.10 (2010) | Berichtenstandaard afgeleid van het RGBZ |

## Verwerkte bronnen

### Standaarden
- [[Wiki/Bronsamenvattingen/Standaarden/rgbz-informatiemodel|RGBZ 1.0 + Introductie]] — referentiemodel zaakgegevens, berichtenarchitectuur, evolutie naar ZGW API's
- [[Wiki/Bronsamenvattingen/Standaarden/ztc2-informatiemodel|ZTC2 v2.1]] — informatiemodel zaaktypecatalogus

### VNG-bronnen Dienstverlening
- [[Wiki/Bronsamenvattingen/Dienstverlening/raadgever-inkoop-en-aanbesteden|Raadgever inkoop en aanbesteden]] — inkoop, aanbestedingsregels en MVOI
- [[Wiki/Bronsamenvattingen/Dienstverlening/hand-out-overheidsbrede-dienstverlening|Hand-out overheidsbrede dienstverlening]] — BZK-programma overheidsbrede loketten, professionallijnen, IDO's
- [[Wiki/Bronsamenvattingen/Dienstverlening/overheidsbrede-startscan|Overheidsbrede Startscan]] — implementatiemethodiek overheidsbrede dienstverlening
- [[Wiki/Bronsamenvattingen/Dienstverlening/rubriek-dienstverlening|VNG-rubriek Dienstverlening]] — portaalpagina GGU, leveranciersmanagement, MijnServices
- [[Wiki/Bronsamenvattingen/Dienstverlening/online-dienstverlening|Online dienstverlening]] — Wmebv, MijnServices, IDO's
- [[Wiki/Bronsamenvattingen/Dienstverlening/digitale-toegankelijkheid|Digitale toegankelijkheid]] — Wdo, toegankelijkheidsverklaring
- [[Wiki/Bronsamenvattingen/Dienstverlening/inkoop-en-aanbesteden|Inkoop en aanbesteden (overzicht)]] — portaalpagina, overlapt met raadgever

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
