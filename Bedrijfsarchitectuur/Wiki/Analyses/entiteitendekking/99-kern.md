---
type: analyse
titel: "Entiteitendekking: 99 Kern"
datum: 2026-07-07
taakveld: "99 Kern"
beleidsdomeinen:
  - 99 Kern
  - BAG
  - RGBZPlus
  - RSGBPlus
totaal_entiteiten: 155
totaal_bo: 40
totaal_matches: 34
totaal_hiaten: 6
---

# Entiteitendekking: 99 Kern

## Beoordeling

4 beleidsdomeinen, 155 GGM-entiteiten. Dekking: 136 van 155 (88%) — 34 met BO, 102 ondersteunend, 19 niet gedekt. 6 BO's zonder GGM-entiteit.

Niet-BO entiteiten: 9× abstract, 25× classificatie, 2× component, 83× detail, 2× proces.

**Structurele patronen per beleidsdomein.** 99 Kern zelf bevat uitsluitend generieke geo/media-detailtypen (Locatie, Punt, Lijn, Gebied en hun groep-varianten, Foto, Video-opname, Periode) die losse attribuutgroepen zijn van een BO elders — geen daarvan bereikt zelfstandigheid. BAG is het schoonste domein: 10 van de 13 entiteiten worden BO, de rest (AdresseerbaarObject, BinnenlandsAdres) is adresseringsdetail en Onderzoek is een procesindicator. RGBZPlus laat het klassieke RGBZ-patroon zien: naast 2 abstracte boventypen (Betrokkene, Object) vooral classificaties (Bedrijfsprocestype, Deelprocestype, Documenttype) en detailgegevens die een zaak/document/besluit verder specificeren (Status, Statustype, KenmerkenZaak, OpschortingZaak, VerlengingZaak); Deelproces is het enige component (onderdeel van Bedrijfsproces). RSGBPlus is verreweg het grootste en meest gefragmenteerde domein (95 entiteiten, 14 BO's): het BRP-cluster splitst persoonsgegevens op in tientallen kleine detailentiteiten per levensgebeurtenis (Geboorte-, Overlijden-, Migratie-, Naamgebruik-, Nationaliteit- en Verblijfsvarianten van NatuurlijkPersoon/IngeschrevenPersoon), en het "Overig"-cluster bevat een reeks referentietabellen (Land, Provincie, AardZakelijkRecht, Valuta(soort), AcademischeTitel, Cultuurcode) naast dezelfde adres-/gebiedsbegrippen die BAG al als BO dekt.

**Functionele dekking.** RSGBPlus heeft met 14 niet-gedekte entiteiten verreweg de meeste hiaten van de vier domeinen (BAG: 1, RGBZPlus: 4). Vrijwel alle niet-gedekte RSGBPlus-entiteiten horen bij het BRP-persoonscluster: MigratieIngeschrevenNatuurlijkPersoon, NaamgebruikNatuurlijkPersoon, NationaliteitIngeschrevenNatuurlijkPersoon, SamengesteldeNaamNatuurlijkPersoon, VerblijfsrechtIngeschrevenNatuurlijkPersoon, VerstrekkingsbeperkingPartieelIngeschrevenNatuurlijkPersoon, NaamAanschrijvingNatuurlijkPersoon, NaamNatuurlijkPersoon, CorrespondentieadresBuitenland, VerblijfBuitenland, VerblijfBuitenlandSubject, plus Rekeningnummer, Land en Provincie. Dit is geen inhoudelijk gemiste BO-categorie maar een gevolg van modelleringsgranulariteit: het GGM splitst het NatuurlijkPersoon/IngeschrevenPersoon-domein in zeer veel kleine detailentiteiten die geen van alle een eigen keten naar een BO hebben omdat NatuurlijkPersoon zelf abstract is en niet elke subtype-tak (Bezoeker, Historisch Persoon, Vreemdeling) als BO is uitgewerkt. Land en Provincie zijn hier bijvangst: het zijn generieke referentietabellen (classificatie) zonder eigen BO, wat verwacht gedrag is voor codelijsten.

**Cross-domein hergebruik.** 99 Kern, BAG, RGBZPlus en RSGBPlus zijn de vier generieke basisregistratie-domeinen van het GGM: hun BO's (Zaak, Document, Besluit, Pand, Woonplaats, Ingeschreven Persoon, Kadastraal Perceel, WOZ-object, etc.) worden in praktisch alle overige taakvelden hergebruikt als kernobject (zaakbehandeling, adressering, betrokkenen). Dat verklaart ook waarom de "Dekking"-kolom bij losse detailentiteiten vaak naar een BO in een heel ander taakveld wijst (bijv. Locatie → Activiteit, Huishouden → Woonboot): het traceeralgoritme volgt de eerste bereikbare relatie, niet per se de inhoudelijk meest voor de hand liggende, wat op zichzelf een teken is van hoe centraal deze basisbegrippen door de rest van het model heen verweven zijn.

**Naamconflicten en disambiguatie.** Naast de reeds gemarkeerde "BO hernoemd"-synoniemen (Ingezetene, NietNatuurlijkPersoon, OrganisatorischeEenheid, MaatschappelijkeActiviteit, KadastraalPerceel, ZakelijkRecht) bevat RSGBPlus/Overig een aantal entiteiten die dezelfde naam dragen als een reeds gematchte BAG-BO maar in dit bestand als losstaande, ongekoppelde entiteit voorkomen: Ligplaats, OpenbareRuimte, Woonplaats, Verblijfsobject, Wijk en Gemeente. Dit zijn geen gemiste BO-kandidaten maar dubbele modelposities van hetzelfde begrip — de BAG-variant is de daadwerkelijke BO, de RSGBPlus/Overig-variant hangt via een omweg (Object, Locatie, Nummeraanduiding) aan een inhoudelijk ongerelateerd BO. Los daarvan bevat RSGBPlus ook een intern duplicaat: Land en LandOfgebied hebben vrijwel identieke definities en attribuutstructuur (landcode/landnaam/ISO-codes) en zijn zeer waarschijnlijk hetzelfde begrip dat tweemaal in het GGM is gemodelleerd.

## 99 Kern

10 entiteiten, 0 Entiteiten met BO.

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/99-kern/99-kern\|Foto]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/monument\|Monument]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/99-kern/99-kern\|Gebied]] | detail | via Locatie → [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/activiteit\|Activiteit]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/99-kern/99-kern\|Gebiedengroep]] | detail | via Locatie → [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/activiteit\|Activiteit]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/99-kern/99-kern\|Lijn]] | detail | via Locatie → [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/activiteit\|Activiteit]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/99-kern/99-kern\|Lijnengroep]] | detail | via Locatie → [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/activiteit\|Activiteit]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/99-kern/99-kern\|Locatie]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/activiteit\|Activiteit]] | Generiek kern-concept (Vastgoedobject); cross-domein |
| [[Wiki/GGM/99-kern/99-kern\|Periode]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archiefstuk\|Archiefstuk]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/99-kern/99-kern\|Punt]] | detail | via Locatie → [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/activiteit\|Activiteit]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/99-kern/99-kern\|Puntengroep]] | detail | via Locatie → [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/activiteit\|Activiteit]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/99-kern/99-kern\|Video-opname]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/griffie/vergadering\|Vergadering]] | Detailgegeven (geassocieerd met BO) |

## BAG

13 entiteiten, 10 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/99-kern/bag\|Buurt]] | [[Wiki/Bedrijfsobjecten/99-kern/bag/buurt\|Buurt]] ✅ | — |  | Exact match |
| [[Wiki/GGM/99-kern/bag\|Gemeente]] | [[Wiki/Bedrijfsobjecten/99-kern/bag/gemeente\|Gemeente]] ✅ | — |  | Exact match |
| [[Wiki/GGM/99-kern/bag\|Ligplaats]] | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/ligplaats\|Ligplaats]] ✅ | — |  | Exact match |
| [[Wiki/GGM/99-kern/bag\|Nummeraanduiding]] | [[Wiki/Bedrijfsobjecten/99-kern/bag/nummeraanduiding\|Nummeraanduiding]] ✅ | — |  | Exact match |
| [[Wiki/GGM/99-kern/bag\|OpenbareRuimte]] | [[Wiki/Bedrijfsobjecten/99-kern/bag/openbare-ruimte\|Openbare Ruimte]] ✅ | synoniem |  | BO hernoemd: Openbare Ruimte |
| [[Wiki/GGM/99-kern/bag\|Pand]] | [[Wiki/Bedrijfsobjecten/99-kern/bag/pand\|Pand]] ✅ | — |  | Exact match |
| [[Wiki/GGM/99-kern/bag\|Standplaats]] | [[Wiki/Bedrijfsobjecten/99-kern/bag/standplaats\|Standplaats (BAG)]] ✅ | synoniem |  | BO hernoemd: Standplaats (BAG) |
| [[Wiki/GGM/99-kern/bag\|Verblijfsobject]] | [[Wiki/Bedrijfsobjecten/99-kern/bag/verblijfsobject\|Verblijfsobject]] ✅ | — |  | Exact match |
| [[Wiki/GGM/99-kern/bag\|Wijk]] | [[Wiki/Bedrijfsobjecten/99-kern/bag/wijk\|Wijk]] ✅ | — |  | Exact match |
| [[Wiki/GGM/99-kern/bag\|Woonplaats]] | [[Wiki/Bedrijfsobjecten/99-kern/bag/woonplaats\|Woonplaats]] ✅ | — |  | Exact match |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/99-kern/bag\|AdresseerbaarObject]] | detail | via Object → [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/woonboot\|Woonboot]] | Detailgegeven |
| [[Wiki/GGM/99-kern/bag\|BinnenlandsAdres]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven |
| [[Wiki/GGM/99-kern/bag\|Onderzoek]] | proces | n.v.t. | Proces of processtap |

## RGBZPlus

37 entiteiten, 10 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/99-kern/rgbzplus\|Bedrijfsproces]] | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/bedrijfsproces\|Bedrijfsproces]] ✅ | — |  | Exact match |
| [[Wiki/GGM/99-kern/rgbzplus\|Besluit]] | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/besluit\|Besluit]] ✅ | — |  | Exact match |
| [[Wiki/GGM/99-kern/rgbzplus\|Betaling]] | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/betaling\|Betaling]] ✅ | — |  | Exact match |
| [[Wiki/GGM/99-kern/rgbzplus\|Document]] | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document\|Document]] ✅ | — |  | Exact match |
| [[Wiki/GGM/99-kern/rgbzplus\|Heffing]] | [[Wiki/Bedrijfsobjecten/99-kern/heffing\|Heffing]] ✅ | — |  | Exact match |
| [[Wiki/GGM/99-kern/rgbzplus\|Klantcontact]] | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/klantcontact\|Klantcontact]] ✅ | — |  | Exact match |
| [[Wiki/GGM/99-kern/rgbzplus\|Medewerker]] | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/medewerker\|Medewerker]] ✅ | — |  | Exact match |
| [[Wiki/GGM/99-kern/rgbzplus\|OrganisatorischeEenheid]] | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/organisatorische-eenheid\|Organisatorische eenheid]] ✅ | synoniem |  | BO hernoemd: Organisatorische eenheid |
| [[Wiki/GGM/99-kern/rgbzplus\|Zaak]] | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] ✅ | — |  | Exact match |
| [[Wiki/GGM/99-kern/rgbzplus\|Zaaktype]] | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaaktype\|Zaaktype]] ✅ | — |  | Exact match |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/99-kern/rgbzplus\|Betrokkene]] | abstract | n.v.t. | Abstract type |
| [[Wiki/GGM/99-kern/rgbzplus\|Object]] | abstract | n.v.t. | Boventype AdresseerbaarObject, Onbestemd Adres, Nummeraanduiding |
| [[Wiki/GGM/99-kern/rgbzplus\|Bedrijfsprocestype]] | classificatie | typering [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/bedrijfsproces\|Bedrijfsproces]] | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rgbzplus\|Deelprocestype]] | classificatie | via Bedrijfsprocestype → [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/bedrijfsproces\|Bedrijfsproces]] | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rgbzplus\|Documenttype]] | classificatie | typering [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document\|Document]] | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rgbzplus\|Deelproces]] | component | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/bedrijfsproces\|Bedrijfsproces]] | Component |
| [[Wiki/GGM/99-kern/rgbzplus\|AfwijkendBuitenlandsCorrespondentieadresRol]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/bag/wijk\|Wijk]] | Detailgegeven |
| [[Wiki/GGM/99-kern/rgbzplus\|AfwijkendCorrespondentiePostadresRol]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/bag/wijk\|Wijk]] | Detailgegeven |
| [[Wiki/GGM/99-kern/rgbzplus\|AnderZaakobjectZaak]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/99-kern/rgbzplus\|Besluittype]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/besluit\|Besluit]] | Typering bij Besluit — waardelijst |
| [[Wiki/GGM/99-kern/rgbzplus\|Brondocumenten]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document\|Document]] | Procesmetadata (brondocumentverwijzing bij mutatie van een relatie), geen zelfstandig object |
| [[Wiki/GGM/99-kern/rgbzplus\|ContactpersoonRol]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/99-kern/rgbzplus\|EnkelvoudigDocument]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document\|Document]] | Concrete verschijningsvorm van Document (enkelvoudig bestand, tegenover SamengesteldDocument), geen zelfstandig object |
| [[Wiki/GGM/99-kern/rgbzplus\|FormeleHistorie]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/99-kern/rgbzplus\|Identificatiekenmerk]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document\|Document]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/99-kern/rgbzplus\|KenmerkenZaak]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/99-kern/rgbzplus\|MaterieleHistorie]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/99-kern/rgbzplus\|Offerte]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/offerte\|Offerte]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/99-kern/rgbzplus\|OpschortingZaak]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/99-kern/rgbzplus\|SamengesteldDocument]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document\|Document]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/99-kern/rgbzplus\|Status]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] | Voortgangsindicatie op Zaak, geen zelfstandig BO |
| [[Wiki/GGM/99-kern/rgbzplus\|Statustype]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaaktype\|Zaaktype]] | Attribuut/modelleringskeuze, geen zelfstandig BO |
| [[Wiki/GGM/99-kern/rgbzplus\|StrijdigheidOfNietigheid]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/99-kern/rgbzplus\|VerlengingZaak]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/99-kern/rgbzplus\|VestigingVanZaakbehandelendeOrganisatie]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/dienstverband\|Dienstverband]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/99-kern/rgbzplus\|ZAAK - Origineel]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] | Duplicaat van [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] |
| [[Wiki/GGM/99-kern/rgbzplus\|InOnderzoek]] | proces | n.v.t. | Proces of processtap |

## RSGBPlus

95 entiteiten, 14 Entiteiten met BO.

### BRP — personen en burgerzaken

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/99-kern/rsgbplus\|Ingezetene]] | [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] ✅ | synoniem |  | BO hernoemd: Ingeschreven Persoon |
| [[Wiki/GGM/99-kern/rsgbplus\|NietNatuurlijkPersoon]] | [[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon\|Niet-Natuurlijk Persoon]] ✅ | synoniem |  | BO hernoemd: Niet-Natuurlijk Persoon |
| [[Wiki/GGM/99-kern/rsgbplus\|Reisdocument]] | [[Wiki/Bedrijfsobjecten/99-kern/brp/reisdocument\|Reisdocument]] ✅ | — |  | Exact match |
| [[Wiki/GGM/99-kern/rsgbplus\|SluitingOfAangaanHuwelijkOfGeregistreerdPartnerschap]] | [[Wiki/Bedrijfsobjecten/99-kern/brp/huwelijk\|Huwelijk]] ✅ | synoniem |  | BO hernoemd: Huwelijk |

**Entiteiten zonder BO:**

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/99-kern/rsgbplus\|IngeschrevenPersoon]] | abstract | n.v.t. | Boventype Leerling, Ouder Of Verzorger, Client |
| [[Wiki/GGM/99-kern/rsgbplus\|NatuurlijkPersoon]] | abstract | n.v.t. | Boventype Bezoeker, Historisch Persoon, Vreemdeling |
| [[Wiki/GGM/99-kern/rsgbplus\|AutoriteitAfgifteNederlandsReisdocument]] | classificatie | typering [[Wiki/Bedrijfsobjecten/99-kern/brp/reisdocument\|Reisdocument]] | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rsgbplus\|Partij]] | classificatie | referentietabel | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rsgbplus\|RedenVerkrijgingNationaliteit]] | classificatie | referentietabel | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rsgbplus\|RedenVerliesNationaliteit]] | classificatie | referentietabel | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rsgbplus\|Reisdocumentsoort]] | classificatie | typering [[Wiki/Bedrijfsobjecten/99-kern/brp/reisdocument\|Reisdocument]] | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rsgbplus\|OntbindingHuwelijk/geregistreerdPartnerschap]] | component | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/bag/woonplaats\|Woonplaats]] | Component |
| [[Wiki/GGM/99-kern/rsgbplus\|AdresBuitenland]] | detail | via Rechtspersoon → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeervergunning\|Parkeervergunning]] | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|GeboorteIngeschrevenNatuurlijkPersoon]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/bag/woonplaats\|Woonplaats]] | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|GeboorteIngeschrevenPersoon]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|Huishouden]] | detail | via Object → [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/woonboot\|Woonboot]] | Cross-cutting sociaal domein, eenheid voor beoordeling |
| [[Wiki/GGM/99-kern/rsgbplus\|MigratieIngeschrevenNatuurlijkPersoon]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|NaamgebruikNatuurlijkPersoon]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|Nationaliteit]] | detail | via NatuurlijkPersoon → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/gemeentebegrafenissen/gemeentebegrafenis\|Gemeentebegrafenis]] | eigenschap van persoon |
| [[Wiki/GGM/99-kern/rsgbplus\|NationaliteitIngeschrevenNatuurlijkPersoon]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|NederlandseNationaliteitIngeschrevenPersoon]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|OverlijdenIngeschrevenNatuurlijkPersoon]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/bag/woonplaats\|Woonplaats]] | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|OverlijdenIngeschrevenPersoon]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|Rechtspersoon]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeervergunning\|Parkeervergunning]] | abstract |
| [[Wiki/GGM/99-kern/rsgbplus\|SamengesteldeNaamNatuurlijkPersoon]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|VerblijfadresIngeschrevenNatuurlijkPersoon]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/ligplaats\|Ligplaats]] | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|VerblijfadresIngeschrevenPersoon]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|VerblijfsrechtIngeschrevenNatuurlijkPersoon]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|Verblijfstitel]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | koppelgegeven (IND) |
| [[Wiki/GGM/99-kern/rsgbplus\|VerstrekkingsbeperkingPartieelIngeschrevenNatuurlijkPersoon]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven |

### BRK — kadaster en rechten

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/99-kern/rsgbplus\|Appartementsrecht]] | [[Wiki/Bedrijfsobjecten/99-kern/brk/appartementsrecht\|Appartementsrecht]] ✅ | — |  | Exact match |
| [[Wiki/GGM/99-kern/rsgbplus\|KadastraalPerceel]] | [[Wiki/Bedrijfsobjecten/99-kern/brk/kadastraal-perceel\|Kadastraal Perceel]] ✅ | synoniem |  | BO hernoemd: Kadastraal Perceel |
| [[Wiki/GGM/99-kern/rsgbplus\|Tenaamstelling]] | [[Wiki/Bedrijfsobjecten/99-kern/brk/tenaamstelling\|Tenaamstelling]] ✅ | — |  | Exact match |
| [[Wiki/GGM/99-kern/rsgbplus\|ZakelijkRecht]] | [[Wiki/Bedrijfsobjecten/99-kern/brk/zakelijk-recht\|Zakelijk Recht]] ✅ | synoniem |  | BO hernoemd: Zakelijk Recht |
| [[Wiki/GGM/99-kern/rsgbplus\|Zekerheidsrecht]] | [[Wiki/Bedrijfsobjecten/99-kern/brk/zekerheidsrecht\|Zekerheidsrecht]] ✅ | — |  | Exact match |

**Entiteiten zonder BO:**

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/99-kern/rsgbplus\|KadastraleOnroerendeZaak]] | abstract | n.v.t. | Boventype Appartementsrecht, KadastraalPerceel |
| [[Wiki/GGM/99-kern/rsgbplus\|AardFiliatie]] | classificatie | referentietabel | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rsgbplus\|AkrKadastraleGemeentecode]] | classificatie | typering [[Wiki/Bedrijfsobjecten/99-kern/bag/gemeente\|Gemeente]] | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rsgbplus\|KadastraleGemeente]] | classificatie | typering [[Wiki/Bedrijfsobjecten/99-kern/bag/gemeente\|Gemeente]] | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rsgbplus\|Aantekening]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brk/tenaamstelling\|Tenaamstelling]] | procesnotitie |
| [[Wiki/GGM/99-kern/rsgbplus\|Appartementsrechtsplitsing]] | detail | via KpBetrokkenBij → [[Wiki/Bedrijfsobjecten/99-kern/brk/zakelijk-recht\|Zakelijk Recht]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/99-kern/rsgbplus\|KadastraleOnroerendeZaakAantekening]] | detail | via KadastraleOnroerendeZaak → [[Wiki/Bedrijfsobjecten/99-kern/woz-object\|WOZ-object]] | Registeraantekening op een kadastraal object (vgl. Aantekening bij Tenaamstelling) |
| [[Wiki/GGM/99-kern/rsgbplus\|KoopsomKadastraleOnroerendeZaak]] | detail | via KadastraleOnroerendeZaak → [[Wiki/Bedrijfsobjecten/99-kern/woz-object\|WOZ-object]] | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|LocatieKadastraleOnroerendeZaak]] | detail | via KadastraleOnroerendeZaak → [[Wiki/Bedrijfsobjecten/99-kern/woz-object\|WOZ-object]] | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|SplitsingstekeningReferentie]] | detail | via Appartementsrechtsplitsing → [[Wiki/Bedrijfsobjecten/99-kern/brk/zakelijk-recht\|Zakelijk Recht]] | Detailgegeven |

### NHR — handelsregister

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/99-kern/rsgbplus\|MaatschappelijkeActiviteit]] | [[Wiki/Bedrijfsobjecten/99-kern/nhr/maatschappelijke-activiteit\|Maatschappelijke Activiteit]] ✅ | synoniem |  | BO hernoemd: Maatschappelijke Activiteit |
| [[Wiki/GGM/99-kern/rsgbplus\|Vestiging]] | [[Wiki/Bedrijfsobjecten/99-kern/nhr/vestiging\|Vestiging]] ✅ | — |  | Exact match |

**Entiteiten zonder BO:**

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/99-kern/rsgbplus\|Briefadres]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/bag/nummeraanduiding\|Nummeraanduiding]] | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|Gebied]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/bag/buurt\|Buurt]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/99-kern/rsgbplus\|HandelsnamenVestiging]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/nhr/vestiging\|Vestiging]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/99-kern/rsgbplus\|SBIActiviteit]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/activiteit\|Activiteit]] | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|SBIActiviteitVestiging]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/nhr/vestiging\|Vestiging]] | Detailgegeven |

### WOZ — waardering onroerende zaken

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/99-kern/rsgbplus\|WOZ-Waarde]] | [[Wiki/Bedrijfsobjecten/99-kern/woz-waarde-bo\|WOZ-waarde]] ✅ | — |  | Exact match |
| [[Wiki/GGM/99-kern/rsgbplus\|WOZ-deelobject]] | [[Wiki/Bedrijfsobjecten/99-kern/woz-deelobject\|WOZ-deelobject]] ✅ | — |  | Exact match |
| [[Wiki/GGM/99-kern/rsgbplus\|WOZ-object]] | [[Wiki/Bedrijfsobjecten/99-kern/woz-object\|WOZ-object]] ✅ | — |  | Exact match |

**Entiteiten zonder BO:**

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/99-kern/rsgbplus\|SoortWOZObject]] | classificatie | typering [[Wiki/Bedrijfsobjecten/99-kern/woz-object\|WOZ-object]] | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rsgbplus\|WOZ-Deelobjectcode]] | classificatie | typering [[Wiki/Bedrijfsobjecten/99-kern/woz-deelobject\|WOZ-deelobject]] | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rsgbplus\|LocatieaanduidingAdresWOZObject]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/woz-object\|WOZ-object]] | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|OverigGebouwdObject]] | detail | via OverigeAdresseerbaarObjectAanduiding → [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/sport/sportpark\|Sportpark]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/99-kern/rsgbplus\|OverigeAdresseerbaarObjectAanduiding]] | detail | via Nummeraanduiding → [[Wiki/Bedrijfsobjecten/99-kern/nhr/vestiging\|Vestiging]] | Detailgegeven |

### Overig — generiek en RSGB-uitbreidingen

**Entiteiten zonder BO:**

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/99-kern/rsgbplus\|BenoemdObject]] | abstract | n.v.t. | Boventype BenoemdTerrein, GebouwdObject |
| [[Wiki/GGM/99-kern/rsgbplus\|BenoemdTerrein]] | abstract | n.v.t. | Boventype Ligplaats, Standplaats |
| [[Wiki/GGM/99-kern/rsgbplus\|GebouwdObject]] | abstract | n.v.t. | Boventype Verblijfsobject, OverigGebouwdObject |
| [[Wiki/GGM/99-kern/rsgbplus\|Nummeraanduiding]] | abstract | n.v.t. | Boventype OverigeAdresseerbaarObjectAanduiding |
| [[Wiki/GGM/99-kern/rsgbplus\|AanduidingVerblijfsrecht]] | classificatie | referentietabel | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rsgbplus\|AardAantekening]] | classificatie | referentietabel | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rsgbplus\|AardZakelijkRecht]] | classificatie | typering [[Wiki/Bedrijfsobjecten/99-kern/brk/zakelijk-recht\|Zakelijk Recht]] | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rsgbplus\|AcademischeTitel]] | classificatie | referentietabel | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rsgbplus\|CultuurcodeBebouwd]] | classificatie | referentietabel | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rsgbplus\|CultuurcodeOnbebouwd]] | classificatie | referentietabel | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rsgbplus\|LandOfgebied]] | classificatie | referentietabel | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rsgbplus\|SoortGrootte]] | classificatie | referentietabel | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rsgbplus\|Valuta]] | classificatie | referentietabel | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rsgbplus\|Valutasoort]] | classificatie | referentietabel | Typering/referentietabel |
| [[Wiki/GGM/99-kern/rsgbplus\|Adresaanduiding]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/bag/nummeraanduiding\|Nummeraanduiding]] | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|AdresseerbaarObjectAanduiding]] | detail | via Nummeraanduiding → [[Wiki/Bedrijfsobjecten/99-kern/nhr/vestiging\|Vestiging]] | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|Buurt]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/bag/openbare-ruimte\|Openbare Ruimte]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/99-kern/rsgbplus\|CorrespondentieadresBuitenland]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|Gemeente]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/asielstatushouder\|Asielstatushouder]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/99-kern/rsgbplus\|HandelsnamenMaatschappelijkeActiviteit]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/nhr/maatschappelijke-activiteit\|Maatschappelijke Activiteit]] | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|Land]] | classificatie | ⚠️ geen BO bereikbaar | Typering/referentietabel (codelijst landen); vrijwel identieke definitie als LandOfgebied in ditzelfde bestand |
| [[Wiki/GGM/99-kern/rsgbplus\|Ligplaats]] | detail | via Object → [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/woonboot\|Woonboot]] | Duplicaat van BAG-entiteit, reeds gedekt als [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/ligplaats\|Ligplaats]] |
| [[Wiki/GGM/99-kern/rsgbplus\|NaamAanschrijvingNatuurlijkPersoon]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|NaamNatuurlijkPersoon]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|Onbestemd Adres]] | detail | via Object → [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/woonboot\|Woonboot]] | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|OpenbareRuimte]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/monument\|Monument]] | Duplicaat van BAG-entiteit, reeds gedekt als [[Wiki/Bedrijfsobjecten/99-kern/bag/openbare-ruimte\|Openbare Ruimte]] |
| [[Wiki/GGM/99-kern/rsgbplus\|Postadres]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/bag/woonplaats\|Woonplaats]] | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|Provincie]] | classificatie | ⚠️ geen BO bereikbaar | Typering/referentietabel (codelijst provincies) |
| [[Wiki/GGM/99-kern/rsgbplus\|Rekeningnummer]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|Standplaats]] | detail | via Object → [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/woonboot\|Woonboot]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/99-kern/rsgbplus\|VerblijfBuitenland]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|VerblijfBuitenlandSubject]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|Verblijfsobject]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/sport/binnenlocatie\|Binnenlocatie]] | Detailgegeven |
| [[Wiki/GGM/99-kern/rsgbplus\|Wijk]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/sport/binnenlocatie\|Binnenlocatie]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/99-kern/rsgbplus\|Woonplaats]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brp/huwelijk\|Huwelijk]] | Duplicaat van BAG-entiteit, reeds gedekt als [[Wiki/Bedrijfsobjecten/99-kern/bag/woonplaats\|Woonplaats]] |

## BO's zonder GGM-entiteit

BO's waarvoor geen overeenkomstige GGM-entiteit bestaat. Data-objecten worden als hiaat teruggemeld aan het GGM-team; overige BO's bestaan alleen in GEMMA.

| BO | Data-object | Grondslag | Status |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/bro/constructie\|Constructie]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/99-kern/bro/gebruiksrecht\|Gebruiksrecht]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/99-kern/brk/publiekrechtelijke-beperking\|Publiekrechtelijke Beperking]] | ja | ggm-entiteit | **Terugmelding** |
| [[Wiki/Bedrijfsobjecten/99-kern/brk/stuk\|Stuk]] | ja | ggm-entiteit | **Terugmelding** |
| [[Wiki/Bedrijfsobjecten/99-kern/brk/stukdeel\|Stukdeel]] | ja | ggm-entiteit | **Terugmelding** |
| [[Wiki/Bedrijfsobjecten/99-kern/bro/verkenning\|Verkenning]] | nee | procesobject | **Alleen GEMMA-BO** |
