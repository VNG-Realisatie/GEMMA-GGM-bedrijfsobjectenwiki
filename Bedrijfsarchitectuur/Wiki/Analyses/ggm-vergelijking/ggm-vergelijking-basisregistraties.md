---
type: analyse
titel: "GGM-vergelijking Basisregistraties"
datum: 2026-06-28
aanleiding: "Vergelijking GGM-entiteiten met bronbegrippen voor basisregistraties"
scope_beleidsdomeinen:
  - BAG
  - RSGBPlus
ggm_entiteiten_count: 91
bronbegrippen_count: 57
bo_count: 30
hiaten_count: 6
---

# GGM-vergelijking Basisregistraties

Vergelijking van de GGM-entiteiten in beleidsdomeinen **BAG** (13 entiteiten) en **RSGBPlus** (128 entiteiten) met de 57 begrippen en 30 BO's uit het [[Wiki/Onderwerpoverzichten/basisregistraties|onderwerpoverzicht Basisregistraties]]. Het onderwerp omvat zes registraties: BAG, BRP, BRK, NHR, WOZ en BRO. Van RSGBPlus zijn 21 IMGeo/BGT-entiteiten en 7 tekenwijze-hulpobjecten buiten scope (deze horen bij het onderwerp grootschalige topografie). Na deduplicatie van BAG-duplicaten en interne varianten resteren 91 unieke GGM-entiteiten in deze analyse.

Bronnen: Catalogus BAG 2018, Logisch Ontwerp BRP 2025.Q1, Catalogus BRK 2020, Gegevenscatalogus NHR 3.0.4, Wet BRO, BRO Catalogus GLD. Herleidbaarheidsketen: Sources/ → Bronsamenvattingen/ → Bedrijfsobjecten/.

## Tabel 1: GGM-entiteiten met match in de bronnen

| GGM-entiteit | GGM-beleidsdomein | Bronbegrip / BO | Entiteitstype | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/99-kern/bag\|AdresseerbaarObject]] | BAG | Adresseerbaar object ❌ | abstract | Boventype Verblijfsobject, Ligplaats, Standplaats |
| [[Wiki/GGM/99-kern/bag\|Buurt]] | BAG | [[Wiki/Bedrijfsobjecten/99-kern/bag/buurt\|Buurt]] ✅ BO | — | Exact match; gebiedsindeling |
| [[Wiki/GGM/99-kern/bag\|Gemeente]] | BAG | [[Wiki/Bedrijfsobjecten/99-kern/bag/gemeente\|Gemeente]] ✅ BO | — | Exact match; door KING toegevoegd, niet formeel BAG |
| [[Wiki/GGM/99-kern/bag\|Ligplaats]] | BAG | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/ligplaats\|Ligplaats]] ✅ BO | — | Exact match |
| [[Wiki/GGM/99-kern/bag\|Nummeraanduiding]] | BAG | [[Wiki/Bedrijfsobjecten/99-kern/bag/nummeraanduiding\|Nummeraanduiding]] ✅ BO | — | Exact match; universeel koppelpunt |
| [[Wiki/GGM/99-kern/bag\|OpenbareRuimte]] | BAG | [[Wiki/Bedrijfsobjecten/99-kern/bag/openbare-ruimte\|Openbare Ruimte]] ✅ BO | — | Exact match |
| [[Wiki/GGM/99-kern/bag\|Pand]] | BAG | [[Wiki/Bedrijfsobjecten/99-kern/bag/pand\|Pand]] ✅ BO | — | Exact match |
| [[Wiki/GGM/99-kern/bag\|Standplaats]] | BAG | [[Wiki/Bedrijfsobjecten/99-kern/bag/standplaats\|Standplaats (BAG)]] ✅ BO | — | Exact match; BAG-standplaats, niet marktstandplaats |
| [[Wiki/GGM/99-kern/bag\|Verblijfsobject]] | BAG | [[Wiki/Bedrijfsobjecten/99-kern/bag/verblijfsobject\|Verblijfsobject]] ✅ BO | — | Exact match |
| [[Wiki/GGM/99-kern/bag\|Wijk]] | BAG | [[Wiki/Bedrijfsobjecten/99-kern/bag/wijk\|Wijk]] ✅ BO | — | Exact match; gebiedsindeling |
| [[Wiki/GGM/99-kern/bag\|Woonplaats]] | BAG | [[Wiki/Bedrijfsobjecten/99-kern/bag/woonplaats\|Woonplaats]] ✅ BO | — | Exact match |
| [[Wiki/GGM/99-kern/rsgbplus\|Aantekening]] | RSGBPlus | Aantekening ❌ | detail | Bijzonderheid bij KOZ of recht; procesnotitie |
| [[Wiki/GGM/99-kern/rsgbplus\|Appartementsrecht]] | RSGBPlus | [[Wiki/Bedrijfsobjecten/99-kern/brk/appartementsrecht\|Appartementsrecht]] ✅ BO | — | Exact match; subtype KadastraleOnroerendeZaak |
| [[Wiki/GGM/99-kern/rsgbplus\|HandelsnamenVestiging]] | RSGBPlus | Handelsnaam ❌ | detail | Groepattribuut; handelsnaam per vestiging |
| [[Wiki/GGM/99-kern/rsgbplus\|Ingezetene]] | RSGBPlus | [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] ✅ BO | — | BO matcht op GGM-subtype Ingezetene; BO-naam breder dan GGM |
| [[Wiki/GGM/99-kern/rsgbplus\|KadastraalPerceel]] | RSGBPlus | [[Wiki/Bedrijfsobjecten/99-kern/brk/kadastraal-perceel\|Kadastraal Perceel]] ✅ BO | — | Exact match; subtype KadastraleOnroerendeZaak |
| [[Wiki/GGM/99-kern/rsgbplus\|KadastraleOnroerendeZaak]] | RSGBPlus | Kadastraal Object ❌ | abstract | Boventype Appartementsrecht en KadastraalPerceel |
| [[Wiki/GGM/99-kern/rsgbplus\|MaatschappelijkeActiviteit]] | RSGBPlus | [[Wiki/Bedrijfsobjecten/99-kern/nhr/maatschappelijke-activiteit\|Maatschappelijke Activiteit]] ✅ BO | — | Exact match; kern NHR |
| [[Wiki/GGM/99-kern/rsgbplus\|Nationaliteit]] | RSGBPlus | Nationaliteit ❌ | detail | Eigenschap van persoon |
| [[Wiki/GGM/99-kern/rsgbplus\|NietNatuurlijkPersoon]] | RSGBPlus | [[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon\|Niet-Natuurlijk Persoon]] ✅ BO | — | Exact match; complement van Ingeschreven Persoon |
| [[Wiki/GGM/99-kern/rsgbplus\|OverlijdenIngeschrevenNatuurlijkPersoon]] | RSGBPlus | Overlijden ❌ | detail | Eenmalige gebeurtenis op persoonslijst |
| [[Wiki/GGM/99-kern/rsgbplus\|Rechtspersoon]] | RSGBPlus | Rechtspersoon ❌ | abstract | Generalisatie NatuurlijkPersoon/NietNatuurlijkPersoon |
| [[Wiki/GGM/99-kern/rsgbplus\|Reisdocument]] | RSGBPlus | [[Wiki/Bedrijfsobjecten/99-kern/brp/reisdocument\|Reisdocument]] ✅ BO | — | Exact match |
| [[Wiki/GGM/99-kern/rsgbplus\|SBIActiviteit]] | RSGBPlus | SBI-code ❌ | classificatie | Standaard Bedrijfsindeling; referentietabel |
| [[Wiki/GGM/99-kern/rsgbplus\|SluitingOfAangaanHuwelijkOfGeregistreerdPartnerschap]] | RSGBPlus | [[Wiki/Bedrijfsobjecten/99-kern/brp/huwelijk\|Huwelijk]] ✅ BO | synoniem | BO hernoemd naar 'Huwelijk' voor leesbaarheid |
| [[Wiki/GGM/99-kern/rsgbplus\|Tenaamstelling]] | RSGBPlus | [[Wiki/Bedrijfsobjecten/99-kern/brk/tenaamstelling\|Tenaamstelling]] ✅ BO | — | Exact match; koppeling recht↔persoon |
| [[Wiki/GGM/99-kern/rsgbplus\|Verblijfstitel]] | RSGBPlus | Verblijfstitel ❌ | detail | Verblijfsrechtelijke status vreemdeling |
| [[Wiki/GGM/99-kern/rsgbplus\|Vestiging]] | RSGBPlus | [[Wiki/Bedrijfsobjecten/99-kern/nhr/vestiging\|Vestiging]] ✅ BO | — | Exact match; koppelpunt beleid↔locatie |
| [[Wiki/GGM/99-kern/rsgbplus\|WOZ-deelobject]] | RSGBPlus | [[Wiki/Bedrijfsobjecten/99-kern/woz-deelobject\|WOZ-deelobject]] ✅ BO | — | Exact match; compositie WOZ-object |
| [[Wiki/GGM/99-kern/rsgbplus\|WOZ-object]] | RSGBPlus | [[Wiki/Bedrijfsobjecten/99-kern/woz-object\|WOZ-object]] ✅ BO | — | Exact match |
| [[Wiki/GGM/99-kern/rsgbplus\|WOZ-Waarde]] | RSGBPlus | [[Wiki/Bedrijfsobjecten/99-kern/woz-waarde-bo\|WOZ-waarde]] ✅ BO | — | Exact match; eigen levenscyclus (jaarlijks) |
| [[Wiki/GGM/99-kern/rsgbplus\|ZakelijkRecht]] | RSGBPlus | [[Wiki/Bedrijfsobjecten/99-kern/brk/zakelijk-recht\|Zakelijk Recht]] ✅ BO | — | Exact match |
| [[Wiki/GGM/99-kern/rsgbplus\|Zekerheidsrecht]] | RSGBPlus | [[Wiki/Bedrijfsobjecten/99-kern/brk/zekerheidsrecht\|Zekerheidsrecht]] ✅ BO | — | Exact match; hypotheek of beslag |

## Tabel 2: GGM-entiteiten zonder match in de bronnen

| GGM-entiteit | GGM-beleidsdomein | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/99-kern/bag\|BinnenlandsAdres]] | BAG | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/woz-object\|WOZ-object]] | Adrescomponenten WOZ-object |
| [[Wiki/GGM/99-kern/bag\|Onderzoek]] | BAG | proces | n.v.t. | Terugmeldingsprocedure op BAG-objectkenmerken |
| [[Wiki/GGM/99-kern/rsgbplus\|AdresseerbaarObjectAanduiding]] | RSGBPlus | abstract | n.v.t. | RSGB-variant adresseerbaar object |
| [[Wiki/GGM/99-kern/rsgbplus\|BenoemdObject]] | RSGBPlus | abstract | n.v.t. | Boventype GebouwdObject en BenoemdTerrein |
| [[Wiki/GGM/99-kern/rsgbplus\|BenoemdTerrein]] | RSGBPlus | abstract | n.v.t. | Boventype Ligplaats en Standplaats (RSGB-variant) |
| [[Wiki/GGM/99-kern/rsgbplus\|GebouwdObject]] | RSGBPlus | abstract | n.v.t. | Boventype Verblijfsobject en OverigGebouwdObject |
| [[Wiki/GGM/99-kern/rsgbplus\|IngeschrevenPersoon]] | RSGBPlus | abstract | n.v.t. | Boventype Ingezetene; BO matcht op concreet subtype |
| [[Wiki/GGM/99-kern/rsgbplus\|NatuurlijkPersoon]] | RSGBPlus | abstract | n.v.t. | Boventype IngeschrevenPersoon |
| [[Wiki/GGM/99-kern/rsgbplus\|AanduidingVerblijfsrecht]] | RSGBPlus | classificatie | typering Verblijfstitel, beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | Codetabel verblijfsrechtindicatie |
| [[Wiki/GGM/99-kern/rsgbplus\|AardAantekening]] | RSGBPlus | classificatie | typering Aantekening, beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brk/tenaamstelling\|Tenaamstelling]] | Typering kadastrale aantekening |
| [[Wiki/GGM/99-kern/rsgbplus\|AardFiliatie]] | RSGBPlus | classificatie | typering filiatie KOZ, beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brk/kadastraal-perceel\|Kadastraal Perceel]] | Reden perceelssplitsing/-samenvoeging |
| [[Wiki/GGM/99-kern/rsgbplus\|AardZakelijkRecht]] | RSGBPlus | classificatie | typering [[Wiki/Bedrijfsobjecten/99-kern/brk/zakelijk-recht\|Zakelijk Recht]] | Aard zakelijk recht (eigendom, erfpacht, etc.) |
| [[Wiki/GGM/99-kern/rsgbplus\|AcademischeTitel]] | RSGBPlus | classificatie | typering NatuurlijkPersoon, beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | Wetenschappelijke/academische graad |
| [[Wiki/GGM/99-kern/rsgbplus\|AutoriteitAfgifteNederlandsReisdocument]] | RSGBPlus | classificatie | typering [[Wiki/Bedrijfsobjecten/99-kern/brp/reisdocument\|Reisdocument]] | Uitgevende instantie reisdocument |
| [[Wiki/GGM/99-kern/rsgbplus\|CultuurcodeBebouwd]] | RSGBPlus | classificatie | typering LocatieKOZ, beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brk/kadastraal-perceel\|Kadastraal Perceel]] | Categorisering bebouwing perceel |
| [[Wiki/GGM/99-kern/rsgbplus\|CultuurcodeOnbebouwd]] | RSGBPlus | classificatie | typering LocatieKOZ, beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brk/kadastraal-perceel\|Kadastraal Perceel]] | Categorisering onbebouwd grondgebruik |
| [[Wiki/GGM/99-kern/rsgbplus\|KadastraleGemeente]] | RSGBPlus | classificatie | typering [[Wiki/Bedrijfsobjecten/99-kern/brk/kadastraal-perceel\|Kadastraal Perceel]] | Kadastrale gebiedsindeling |
| [[Wiki/GGM/99-kern/rsgbplus\|LandOfgebied]] | RSGBPlus | classificatie | referentietabel, diverse relaties | Referentiecodelijst landen |
| [[Wiki/GGM/99-kern/rsgbplus\|Partij]] | RSGBPlus | classificatie | n.v.t. | BRP-afnemer/-verstrekker bij centrale voorzieningen |
| [[Wiki/GGM/99-kern/rsgbplus\|RedenVerkrijgingNationaliteit]] | RSGBPlus | classificatie | typering Nationaliteit, beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | Reden verkrijging NL nationaliteit |
| [[Wiki/GGM/99-kern/rsgbplus\|RedenVerliesNationaliteit]] | RSGBPlus | classificatie | typering Nationaliteit, beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | Reden verlies NL nationaliteit |
| [[Wiki/GGM/99-kern/rsgbplus\|Reisdocumentsoort]] | RSGBPlus | classificatie | typering [[Wiki/Bedrijfsobjecten/99-kern/brp/reisdocument\|Reisdocument]] | Model Nederlands reisdocument |
| [[Wiki/GGM/99-kern/rsgbplus\|SoortGrootte]] | RSGBPlus | classificatie | typering [[Wiki/Bedrijfsobjecten/99-kern/brk/kadastraal-perceel\|Kadastraal Perceel]] | Wijze vaststelling perceelsgrootte |
| [[Wiki/GGM/99-kern/rsgbplus\|SoortWOZObject]] | RSGBPlus | classificatie | typering [[Wiki/Bedrijfsobjecten/99-kern/woz-object\|WOZ-object]] | Soort object (Waarderingskamer-codelijst) |
| [[Wiki/GGM/99-kern/rsgbplus\|Valutasoort]] | RSGBPlus | classificatie | typering KoopsomKOZ, beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brk/kadastraal-perceel\|Kadastraal Perceel]] | Munteenheid kadastrale koopsom |
| [[Wiki/GGM/99-kern/rsgbplus\|WOZ-Deelobjectcode]] | RSGBPlus | classificatie | typering [[Wiki/Bedrijfsobjecten/99-kern/woz-deelobject\|WOZ-deelobject]] | Soort deelobject (Waarderingskamer) |
| [[Wiki/GGM/99-kern/rsgbplus\|KadastraleOnroerendeZaakAantekening]] | RSGBPlus | component | item bij KOZ, beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brk/kadastraal-perceel\|Kadastraal Perceel]]/[[Wiki/Bedrijfsobjecten/99-kern/brk/appartementsrecht\|Appartementsrecht]] | Bijzonderheid bij onroerende zaak |
| [[Wiki/GGM/99-kern/rsgbplus\|OntbindingHuwelijk/geregistreerdPartnerschap]] | RSGBPlus | component | component van [[Wiki/Bedrijfsobjecten/99-kern/brp/huwelijk\|Huwelijk]] | Einde huwelijk/partnerschap |
| [[Wiki/GGM/99-kern/rsgbplus\|FunctioneelGebied]] | RSGBPlus | cross-cutting | n.v.t. | Functioneel benoemd gebied; RSGB-uitbreiding buiten BAG |
| [[Wiki/GGM/99-kern/rsgbplus\|Gebied]] | RSGBPlus | cross-cutting | n.v.t. | Generieke gebiedsindeling (overlapt met Buurt) |
| [[Wiki/GGM/99-kern/rsgbplus\|Huishouden]] | RSGBPlus | cross-cutting | n.v.t. | Samenlevingsvorm; raakt meerdere domeinen (sociaal, wonen) |
| [[Wiki/GGM/99-kern/rsgbplus\|OverigBenoemdTerrein]] | RSGBPlus | cross-cutting | n.v.t. | RSGB-terrein buiten BAG |
| [[Wiki/GGM/99-kern/rsgbplus\|OverigGebouwdObject]] | RSGBPlus | cross-cutting | n.v.t. | Eenheid van gebruik buiten BAG-verblijfsobjecten |
| [[Wiki/GGM/99-kern/rsgbplus\|Provincie]] | RSGBPlus | cross-cutting | n.v.t. | Bestuurlijke gebiedsindeling boven gemeente |
| [[Wiki/GGM/99-kern/rsgbplus\|AdresBuitenland]] | RSGBPlus | detail | beschrijft Rechtspersoon → [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]]/[[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon\|Niet-Natuurlijk Persoon]] | Buitenlands adres subject |
| [[Wiki/GGM/99-kern/rsgbplus\|AkrKadastraleGemeentecode]] | RSGBPlus | detail | beschrijft KadastraleGemeente → [[Wiki/Bedrijfsobjecten/99-kern/brk/kadastraal-perceel\|Kadastraal Perceel]] | AKR-codering kadastrale gemeente |
| [[Wiki/GGM/99-kern/rsgbplus\|Appartementsrechtsplitsing]] | RSGBPlus | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brk/appartementsrecht\|Appartementsrecht]] | Splitsingsstructuur appartementsrecht |
| [[Wiki/GGM/99-kern/rsgbplus\|Briefadres]] | RSGBPlus | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | Inschrijvingsadres (niet-woonadres) |
| [[Wiki/GGM/99-kern/rsgbplus\|CorrespondentieadresBuitenland]] | RSGBPlus | detail | beschrijft Rechtspersoon → [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]]/[[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon\|Niet-Natuurlijk Persoon]] | Buitenlands correspondentieadres |
| [[Wiki/GGM/99-kern/rsgbplus\|GeboorteIngeschrevenNatuurlijkPersoon]] | RSGBPlus | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | Geboortegegevens persoon |
| [[Wiki/GGM/99-kern/rsgbplus\|HandelsnamenMaatschappelijkeActiviteit]] | RSGBPlus | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/nhr/maatschappelijke-activiteit\|Maatschappelijke Activiteit]] | Handelsnaam maatschappelijke activiteit |
| [[Wiki/GGM/99-kern/rsgbplus\|KoopsomKadastraleOnroerendeZaak]] | RSGBPlus | detail | beschrijft KOZ → [[Wiki/Bedrijfsobjecten/99-kern/brk/kadastraal-perceel\|Kadastraal Perceel]]/[[Wiki/Bedrijfsobjecten/99-kern/brk/appartementsrecht\|Appartementsrecht]] | Transactiebedrag onroerende zaak |
| [[Wiki/GGM/99-kern/rsgbplus\|LocatieKadastraleOnroerendeZaak]] | RSGBPlus | detail | beschrijft KOZ → [[Wiki/Bedrijfsobjecten/99-kern/brk/kadastraal-perceel\|Kadastraal Perceel]]/[[Wiki/Bedrijfsobjecten/99-kern/brk/appartementsrecht\|Appartementsrecht]] | Locatieaanduiding kadastrale zaak |
| [[Wiki/GGM/99-kern/rsgbplus\|LocatieaanduidingAdresWOZObject]] | RSGBPlus | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/woz-object\|WOZ-object]] | Locatieomschrijving WOZ-object |
| [[Wiki/GGM/99-kern/rsgbplus\|MigratieIngeschrevenNatuurlijkPersoon]] | RSGBPlus | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | Immigratie-/emigratiegegevens |
| [[Wiki/GGM/99-kern/rsgbplus\|NaamgebruikNatuurlijkPersoon]] | RSGBPlus | detail | beschrijft NatuurlijkPersoon → [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | Aanschrijfnaam persoon |
| [[Wiki/GGM/99-kern/rsgbplus\|NederlandseNationaliteitIngeschrevenPersoon]] | RSGBPlus | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | Bijzonder Nederlanderschap |
| [[Wiki/GGM/99-kern/rsgbplus\|Onbestemd Adres]] | RSGBPlus | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/bag/nummeraanduiding\|Nummeraanduiding]] | Niet-regulier adrestype |
| [[Wiki/GGM/99-kern/rsgbplus\|OverigeAdresseerbaarObjectAanduiding]] | RSGBPlus | detail | beschrijft OverigGebouwdObject (cross-cutting) | Adressering niet-BAG-objecten |
| [[Wiki/GGM/99-kern/rsgbplus\|Postadres]] | RSGBPlus | detail | beschrijft Rechtspersoon → [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]]/[[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon\|Niet-Natuurlijk Persoon]] | Postbus-/antwoordnummeradres |
| [[Wiki/GGM/99-kern/rsgbplus\|Rekeningnummer]] | RSGBPlus | detail | beschrijft Rechtspersoon → [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]]/[[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon\|Niet-Natuurlijk Persoon]] | IBAN/BIC bankrekening |
| [[Wiki/GGM/99-kern/rsgbplus\|SBIActiviteitVestiging]] | RSGBPlus | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/nhr/vestiging\|Vestiging]] | Koppeling SBI-activiteit aan vestiging |
| [[Wiki/GGM/99-kern/rsgbplus\|SamengesteldeNaamNatuurlijkPersoon]] | RSGBPlus | detail | beschrijft NatuurlijkPersoon → [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | Formele naamcomponenten persoon |
| [[Wiki/GGM/99-kern/rsgbplus\|SplitsingstekeningReferentie]] | RSGBPlus | detail | beschrijft Appartementsrechtsplitsing → [[Wiki/Bedrijfsobjecten/99-kern/brk/appartementsrecht\|Appartementsrecht]] | Verwijzing naar splitsingstekening |
| [[Wiki/GGM/99-kern/rsgbplus\|VerblijfBuitenland]] | RSGBPlus | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | Verblijfadres buitenland |
| [[Wiki/GGM/99-kern/rsgbplus\|VerblijfadresIngeschrevenNatuurlijkPersoon]] | RSGBPlus | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | Woonadres in Nederland |
| [[Wiki/GGM/99-kern/rsgbplus\|VerblijfsrechtIngeschrevenNatuurlijkPersoon]] | RSGBPlus | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | Verblijfsrechtgegevens vreemdeling |
| [[Wiki/GGM/99-kern/rsgbplus\|VerstrekkingsbeperkingPartieelIngeschrevenNatuurlijkPersoon]] | RSGBPlus | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | Gedeeltelijke verstrekkingsbeperking persoonsgegevens |

## Tabel 3: Bronbegrippen zonder GGM-equivalent (hiaten)

| Begrip uit bronnen | BO-status | Grondslag | GGM-hiaat? |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/brk/publiekrechtelijke-beperking\|Publiekrechtelijke Beperking]] | ✅ BO | WKPB — gemeente is bronhouder beperkingsbesluiten | **Ja** — ontbreekt volledig in GGM BAG en RSGBPlus |
| [[Wiki/Bedrijfsobjecten/99-kern/brk/stuk\|Stuk]] | ✅ BO | BRK openbare registers — brondocument (akte, kadasterstuk) | **Ja** — ontbreekt volledig in GGM |
| [[Wiki/Bedrijfsobjecten/99-kern/brk/stukdeel\|Stukdeel]] | ✅ BO | BRK openbare registers — onderdeel van stuk met rechtsfeiten | **Ja** — ontbreekt volledig in GGM |
| [[Wiki/Bedrijfsobjecten/99-kern/bro/verkenning\|Verkenning]] | ✅ BO | Wet BRO art. 19 — waarneming opbouw ondergrond | **Ja** — BRO is volledig absent in GGM |
| [[Wiki/Bedrijfsobjecten/99-kern/bro/constructie\|Constructie]] | ✅ BO | Wet BRO art. 21 — werk in de ondergrond | **Ja** — BRO is volledig absent in GGM |
| [[Wiki/Bedrijfsobjecten/99-kern/bro/gebruiksrecht\|Gebruiksrecht]] | ✅ BO | Wet BRO art. 20 — besluit/melding winnen, opslaan, bodemkwaliteit | **Ja** — BRO is volledig absent in GGM |

## Beoordeling

### Dekking

24 van 30 BO's hebben een GGM-match (80%). Alle 24 matches zijn exact of sterk. De 6 hiaten vallen in twee categorieën: BRK-brondocumenten (Stuk, Stukdeel, Publiekrechtelijke Beperking) en de complete BRO (Verkenning, Constructie, Gebruiksrecht).

### Structurele patronen

Van de 91 GGM-entiteiten in scope:
- **33 in tabel 1** (match in bronnen): 24× BO, 3× abstract, 3× detail, 2× classificatie, 1× synoniem
- **58 in tabel 2** (geen match): 6× abstract, 18× classificatie, 2× component, 6× cross-cutting, 24× detail, 1× proces

Het patroon is kenmerkend voor het RSGB: het GGM modelleert op **genormaliseerd dataniveau** met aparte entiteiten voor elk attribuutcluster (geboortegegevens, naamgegevens, verblijfadres). De BO-laag abstraheert dit naar het **bedrijfsniveau**: [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon|Ingeschreven Persoon]] absorbeert 12 detail-entiteiten (geboorte, migratie, naam, verblijfadres, nationaliteit, verblijfsrecht, verstrekkingsbeperking). Dit is het sterkste voorbeeld van RSGB-normalisatie in de wiki.

### BO-dekking detail/component-entiteiten

Alle 44 detail/component/classificatie-entiteiten in tabel 2 hebben een dekkingsketen die bij een BO uitkomt. Er zijn **0 BO-hiaten**: geen concept ontbreekt als parent-BO om detail-entiteiten structureel te dekken.

### Hiaten

De 6 hiaten vallen in twee structureel verschillende categorieën:

**BRK-brondocumenten (3 hiaten)**

Publiekrechtelijke Beperking, Stuk en Stukdeel ontbreken in het GGM. Dit is opvallend omdat het GGM de BRK-objecten (perceel, appartementsrecht, zakelijk recht, tenaamstelling, zekerheidsrecht) wél volledig modelleert. De ontbrekende objecten zijn:
- **Publiekrechtelijke Beperking**: de gemeente is hier *bronhouder* (via WKPB). Dit is het enige BRK-object waarvoor de gemeente niet alleen afnemer maar bronhouder is — een significante lacune.
- **Stuk/Stukdeel**: de brondocumenten in de openbare registers waaruit rechtswijzigingen traceren. Dit zijn authentieke gegevens waaraan de gemeente gebonden is.

**BRO — volledig absent (3 hiaten)**

De Basisregistratie Ondergrond (Verkenning, Constructie, Gebruiksrecht) ontbreekt compleet in het GGM. De gemeente is bronhouder voor verkenningen en constructies bij gemeentelijke taken (grondwatermonitoring, bodemsanering, geotechnisch onderzoek). Dit is een **structurele lacune** in het GGM: een hele wettelijke basisregistratie is niet gemodelleerd.

### RSGBPlus duplicaten en varianten

Het RSGBPlus bevat systematische duplicaten van BAG-entiteiten (Buurt, Gemeente, Pand, Verblijfsobject, etc.) en interne varianten (GeboorteIngeschrevenNatuurlijkPersoon ≈ GeboorteIngeschrevenPersoon). Deze 10 BAG-duplicaten en ~12 interne varianten zijn in deze analyse geconsolideerd. De BO's matchen op de BAG-versie (BAG-GUIDs) of de meest specifieke RSGBPlus-versie.

### Naamverschillen

- **Synoniem**: SluitingOfAangaanHuwelijkOfGeregistreerdPartnerschap → BO hernoemd naar **Huwelijk** voor leesbaarheid
- **Niveauverschil**: GGM Ingezetene → BO **Ingeschreven Persoon** (BO-naam is breder dan GGM-subtype; dekt conceptueel ook de abstracte IngeschrevenPersoon)
- **Standplaats-disambiguatie**: GGM-entiteit Standplaats (BAG) correct gematcht op [[Wiki/Bedrijfsobjecten/99-kern/bag/standplaats|Standplaats (BAG)]], niet op Marktstandplaats (Economie)

### Bewuste abstractiekeuzes

- **Adresseerbaar object** is geen BO maar abstract boventype — de drie concrete subtypes (Verblijfsobject, Ligplaats, Standplaats) zijn BO
- **Kadastraal Object / Onroerende Zaak** is geen BO — de twee concrete subtypes (Kadastraal Perceel, Appartementsrecht) zijn BO
- **Rechtspersoon** is geen BO — de twee concrete subtypes (Ingeschreven Persoon, Niet-Natuurlijk Persoon) zijn BO
- **Ingezetene/Niet-ingezetene**: het GGM modelleert alleen Ingezetene als concreet subtype. Niet-ingezetene (RNI) ontbreekt in het GGM maar is ook geen BO: de gemeente is alleen bijhoudingsautoriteit voor ingezetenen

### Begrippen als attribuut (geen aparte GGM-entiteit)

De begrippentabel bevat enkele begrippen die in het GGM als attribuut op een entiteit zijn gemodelleerd, niet als aparte entiteit: **Gezagsverhouding** (indicatieGezagMinderjarige op Ingezetene), **Kiesrecht** (aanduidingUitgeslotenKiesrecht/aanduidingEuropeesKiesrecht op Ingezetene), en **Gebruiksdoel** (enumeratie op Verblijfsobject). Dit is correct: deze begrippen hebben geen eigen levenscyclus.

### Leidingnetwerk

De begrippentabel noteert "GGM: ja" voor Leidingnetwerk, maar deze entiteit is niet gevonden in de GGM-beleidsdomeinen BAG of RSGBPlus. Mogelijk verwijderd bij een GGM-update of gemodelleerd in een niet-onderzocht beleidsdomein. De BO-beoordeling is ❌ (nutsbedrijf-scope), dus dit heeft geen impact op de gemeentelijke BO-dekking.
