---
type: bedrijfsobject
naam: Ingeschreven Persoon
onderwerp: [Basisregistraties, BRP]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Ingezetene
ggm_guid: EAID_CA19D17F_3EB7_459d_9883_16F0C0B5D35E
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram: [Burgerzaken, "(Zaak)objecten", "Huishouden en Huwelijk"]
ggm_diagram_ids: []
ggm_definitie: "Een individueel menselijk wezen, ingeschreven in het Nederlands Bevolkingsregister."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: "GGM"

ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""

ggm_duplicaat_entiteiten: []

gemma_definitie: "Een persoon met een persoonslijst in de Basisregistratie Personen (BRP), bijgehouden door een gemeente (ingezetene) of de RNI (niet-ingezetene)."
gemma_subtypes: []
relaties:
  - type: associatie
    bedrijfsobject: "[[Nummeraanduiding]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Woont op adres via verblijfplaatsgegevens (BRP categorie 08)"
  - type: associatie
    bedrijfsobject: "[[Verblijfsobject]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Verblijft in verblijfsobject (via BAG-koppeling in BRP)"
  - type: associatie
    bedrijfsobject: "[[Huwelijk]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Heeft huwelijken of geregistreerde partnerschappen"
  - type: associatie
    bedrijfsobject: "[[Reisdocument]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Heeft reisdocumenten"
  - type: associatie
    bedrijfsobject: "[[Gemeente]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Is ingeschreven in gemeente"
bedrijfsprocessen: [Burgerzaken, Vergunningverlening, Belastingheffing, Sociale voorzieningen, Verkiezingen]
bedrijfsfuncties: [Bevolkingsadministratie, Burgerzakenloket]
---

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Herkenbaar in dagelijks werk | ✅ | Elke gemeentelijke dienstverlening begint bij de persoon; het BSN is de universele sleutel |
| Eigenaar/houder | ✅ | Gemeente is bijhoudingsverantwoordelijke (Wet BRP) |
| Levenscyclus | ✅ | Eerste inschrijving → mutaties → opschorting (emigratie/overlijden) |
| Meervoudig | ✅ | Elke gemeente heeft duizenden tot honderdduizenden ingeschreven personen |
| Gegevens | ✅ | BSN, A-nummer, naam, geboorte, geslacht, adres, nationaliteit, kiesrecht, etc. |
| Relaties met andere BO's | ✅ | [[Verblijfsobject]], [[Nummeraanduiding]], [[Gemeente]], [[Huwelijk]], [[Reisdocument]] |

## Beschrijving

Een Ingeschreven Persoon is iemand met een persoonslijst (PL) in de Basisregistratie Personen. De PL bevat alle persoonsgegevens in 13 categorieën: identificatie (A-nummer, BSN), naam, geboorte, geslacht, ouders, nationaliteit, huwelijk/partnerschap, overlijden, verblijfplaats, kinderen, verblijfstitel, gezagsverhouding, reisdocumenten en kiesrecht.

De gemeente is bijhoudingsverantwoordelijke voor haar ingezetenen. Eenmaal ingeschreven wordt een PL niet meer verwijderd — bij emigratie of overlijden wordt de bijhouding opgeschort. De BRP koppelt personen aan BAG-objecten: de verblijfplaats bevat de identificatiecode van het [[Verblijfsobject]] en de [[Nummeraanduiding]].

## Subtypes

Herkende specialisaties van Ingeschreven Persoon. Geen apart BO.

- **Ingezetene** — persoon ingeschreven bij een gemeente; volledige PL met alle 13 categorieën
- **Niet-ingezetene** — persoon ingeschreven in de RNI (Registratie Niet-Ingezetenen); beperkte PL (categorieën 01, 04, 06, 07, 08, 10 + RNI-specifiek 16, 17)

## GGM-componenten

GGM-entiteiten die onderdeel zijn van Ingeschreven Persoon. Gemodelleerd als aparte entiteiten in het GGM maar vormen geen zelfstandig bedrijfsobject — het zijn eigenschappen of deelregistraties van de persoon.

- **NationaliteitIngeschrevenNatuurlijkPersoon** — gegevens over het bezit van een nationaliteit door een persoon (verkrijging, beëindiging, bijzonder Nederlanderschap)
- **VerblijfsrechtIngeschrevenNatuurlijkPersoon** — gegevens over het verblijfsrecht (verblijfstitel) van een vreemdeling
- **GeboorteIngeschrevenNatuurlijkPersoon** — gegevens over de geboorte (datum, plaats, land)
- **OverlijdenIngeschrevenNatuurlijkPersoon** — gegevens over het overlijden (datum, plaats, land)
- **MigratieIngeschrevenNatuurlijkPersoon** — gegevens over immigratie en emigratie
- **VerblijfadresIngeschrevenNatuurlijkPersoon** — gegevens over het verblijfadres
- **VerstrekkingsbeperkingPartieelIngeschrevenNatuurlijkPersoon** — verstrekkingsbeperking voor specifieke partijen
- **NaamgebruikNatuurlijkPersoon** — naamgegevens voor aanschrijving
- **SamengesteldeNaamNatuurlijkPersoon** — voornamen, voorvoegsel, geslachtsnaam, adellijke titel

## GGM-bron

> "Een individueel menselijk wezen, ingeschreven in het Nederlands Bevolkingsregister."

- **GGM-entiteit:** Ingezetene (concreet), generaliseert van IngeschrevenPersoon (abstract) → NatuurlijkPersoon (abstract) → Rechtspersoon (abstract)
- **Beleidsdomein:** RSGBPlus
- **Attributen Ingezetene (7):** aanduidingUitgeslotenKiesrecht, aanduidingEuropeesKiesrecht, indicatieCurateleregister, indicatieGezagMinderjarige, datumVerkrijgingVerblijfstitel, datumVerliesVerblijfstitel, indicatieBlokkering
- **Attributen IngeschrevenPersoon (24):** adresHerkomst, anummer, beschrijvingLocatie, burgerlijkeStaat, indicatieGeheim, gemeenteVanInschrijving, landWaarvandaanIngeschreven, landWaarnaarVertrokken, datumInschrijvingGemeente, datumBeginGeldigheidVerblijfplaats, signaleringReisdocument, buitenlandsReisdocument, datumVestigingNederland, datumVertrekUitNederland, redenOpschortingBijhouding, datumOpschortingBijhouding, ingezetene, datumEindeGeldigheidVerblijfsplaats, redenEindeBewoning, verblijfstitel, ouder1, gezinsrelatie, ouder2, partnerID
- **Attributen NatuurlijkPersoon (25):** aanduidingNaamgebruik, voornamen, academischeTitel, datumGeboorte, geboorteplaats, geslachtsnaam, overlijdensplaats, datumOverlijden, geboorteland, geslachtsaanduiding, landOverlijden, burgerservicenummer, nationaliteit, anummer, indicatieOverleden, IndicatieAfschermingPersoonsgegevens, e.a.
- **Matchsterkte:** exact — de GGM-overervingshiërarchie dekt precies de BRP-structuur

## BO-definitie

De GGM-definitie van Ingezetene ("Een individueel menselijk wezen, ingeschreven in het Nederlands Bevolkingsregister") beschrijft alleen ingezetenen. De GEMMA-definitie is breder: "Een persoon met een persoonslijst in de Basisregistratie Personen (BRP), bijgehouden door een gemeente (ingezetene) of de RNI (niet-ingezetene)." Dit sluit aan bij de Wet BRP die zowel ingezetenen als niet-ingezetenen omvat.

## Relaties

| Gerelateerd BO | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/bag/nummeraanduiding\|Nummeraanduiding]] | → | 0..1 | Woont op adres (BRP cat. 08, element 11.90) | BRP/GGM |
| [[Wiki/Bedrijfsobjecten/99-kern/bag/verblijfsobject\|Verblijfsobject]] | → | 0..1 | Verblijft in verblijfsobject (BRP cat. 08, element 11.80) | BRP/GGM |
| [[Wiki/Bedrijfsobjecten/99-kern/bag/gemeente\|Gemeente]] | → | 1 | Is ingeschreven in gemeente | BRP/GGM |
| [[Wiki/Bedrijfsobjecten/99-kern/brp/huwelijk\|Huwelijk]] | → | 0..* | Heeft huwelijken/partnerschappen (BRP cat. 05) | BRP/GGM |
| [[Wiki/Bedrijfsobjecten/99-kern/brp/reisdocument\|Reisdocument]] | → | 0..* | Heeft reisdocumenten (BRP cat. 12) | BRP/GGM |

## Bedrijfsprocessen

- Burgerzaken (geboorteaangifte, huwelijksvoltrekking, verhuisaangifte, overlijdensaangifte)
- Vergunningverlening (persoonsgegevens aanvrager)
- Belastingheffing (adres en verblijfsobject bepalen heffingsplicht)
- Sociale voorzieningen (inkomen, zorg, bijstand — koppeling met persoonsgegevens)
- Verkiezingen (kiesrechtgegevens op PL)
- Identiteitsdocumenten (aanvraag en uitgifte paspoort/ID-kaart)

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/logisch-ontwerp-brp-2025q1]]
- [[Wiki/Bronsamenvattingen/Standaarden/rsgb-en-informatiemodellen]]
