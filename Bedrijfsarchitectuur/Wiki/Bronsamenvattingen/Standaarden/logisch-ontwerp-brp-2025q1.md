---
type: bronsamenvatting
titel: "Logisch Ontwerp BRP 2025.Q1"
onderwerp: [Basisregistraties, BRP]
datum_ingest: 2026-06-25
---

## Samenvatting

Het Logisch Ontwerp BRP (LO BRP) is de formele systeembeschrijving van de Basisregistratie Personen, vastgesteld door de minister van BZK. Het beschrijft de functionele en technische eisen waaraan alle systemen binnen het BRP-stelsel moeten voldoen. Het document verschijnt vier keer per jaar; deze versie (2025.Q1) is van kracht per 1 januari 2025.

De BRP registreert persoonsgegevens van **ingezetenen** (bijgehouden door gemeenten) en **niet-ingezetenen** (bijgehouden in de RNI, Registratie Niet-Ingezetenen). Eenmaal ingeschreven wordt een persoonslijst niet meer verwijderd.

### Structuur persoonslijst

De persoonslijst (PL) is onderverdeeld in **categorieën** met bij elkaar horende gegevens:

| Cat. | Naam | Mult. | Omschrijving |
|---|---|---|---|
| 01 | Persoon | 1 | Identificatie (A-nr, BSN), naam, geboorte, geslacht, naamgebruik |
| 02 | Ouder1 | 1 | Gegevens over de eerste ouder |
| 03 | Ouder2 | 1 | Gegevens over de tweede ouder |
| 04 | Nationaliteit | 0,n | Nationaliteit(en) met verkrijging/beëindiging |
| 05 | Huwelijk/GP | 0,n | Gesloten of ontbonden huwelijk of geregistreerd partnerschap |
| 06 | Overlijden | 0,1 | Overlijdensdatum, -plaats en -land |
| 07 | Inschrijving | 1 | Opname, status PL, blokkering, opschorting, geheimhouding |
| 08 | Verblijfplaats | 1 | Adres (koppeling met BAG), adres buitenland, immigratie |
| 09 | Kind | 0,n | Gegevens over kinderen |
| 10 | Verblijfstitel | 0,1 | Verblijfsrechtelijke status (vreemdelingen) |
| 11 | Gezagsverhouding | 0,1 | Gezag over minderjarige, curatele |
| 12 | Reisdocument | 0,n | Nederlands paspoort of identiteitskaart |
| 13 | Kiesrecht | 0,1 | Europees kiesrecht, uitsluiting kiesrecht |

Categorieën 16 (Tijdelijk verblijfsadres) en 17 (Contactgegevens) komen uitsluitend voor in de RNI.

Bij wijziging van gegevens wordt historie aangelegd (historisch categorienummer = actueel + 50).

### Koppeling met BAG

Categorie 08 Verblijfplaats bevat een directe koppeling met de BAG: element 11.80 (Identificatiecode verblijfplaats) en 11.90 (Identificatiecode nummeraanduiding) verwijzen naar BAG-objecten. De adresgegevens in de BRP moeten overeenkomen met de BAG.

### Stelselarchitectuur

Het BRP-stelsel omvat: gemeentelijke systemen, RNI, afnemersystemen, BRP-Verstrekkingsvoorziening (BRP-V), Berichtendienst, webservices, API's, Terugmeldvoorziening (TMV), Beheervoorziening BSN (BvBSN), en diverse kwaliteits- en controletools.

## Kernbegrippen

- **Ingeschreven Persoon** — een persoon met een persoonslijst in de BRP. Onderverdeeld in ingezetenen (bijgehouden door gemeenten) en niet-ingezetenen (bijgehouden in RNI). Geïdentificeerd door A-nummer en burgerservicenummer (BSN).
- **Persoonslijst** — het geheel van persoonsgegevens dat over een persoon in de BRP is opgenomen. Geen fysiek document maar een logische gegevensverzameling.
- **Huwelijk/Geregistreerd partnerschap** — registratie van een verbintenis met sluiting/aangaan en eventuele ontbinding. Meervoudig: een persoon kan meerdere (opeenvolgende) verbintenissen hebben.
- **Nationaliteit** — hoedanigheid van tot een bepaalde natie te behoren. Meervoudig: een persoon kan meerdere nationaliteiten bezitten, elk met eigen verkrijging en eventuele beëindiging.
- **Reisdocument** — Nederlands paspoort of Nederlandse identiteitskaart. Meervoudig, eigen levenscyclus (uitgifte→verval), wordt na bewaartermijn van PL verwijderd.
- **Verblijfstitel** — verblijfsrechtelijke status van een vreemdeling. Aangeleverd door de IND.
- **Gezagsverhouding** — gegevens over gezag over een minderjarige of curatele. Gebruikt voor vaststelling wettelijke vertegenwoordigers.
- **Kiesrecht** — Europees kiesrecht en eventuele uitsluiting kiesrecht. Statusgegevens.
- **Verwijzing** — afgeleide gegevensverzameling die doorverwijst naar de (volgende) gemeente van inschrijving.
- **Afnemersindicatie** — indicatie dat een afnemer geïnteresseerd is in wijzigingen van een persoon, voor spontane gegevensverstrekking.

## Relevantie voor bedrijfsarchitectuur

De BRP is naast de BAG de belangrijkste basisregistratie voor gemeenten. Elke inwoner heeft een persoonslijst die door de gemeente wordt bijgehouden. De BRP levert persoonsgegevens aan vrijwel alle gemeentelijke processen: burgerzaken, sociaal domein, belastingen, vergunningen, verkiezingen.

> "De basisgegevens vormen nog maar het topje van de ijsberg van wat gemeenten aan gegevens nodig hebben om hun processen uit te voeren."
> — [[Wiki/Bronsamenvattingen/Standaarden/rsgb-en-informatiemodellen|RSGB 2.02 Deel I]]

> "Het staat gemeenten vrij, uiteraard binnen de grenzen van de AVG extra gegevens voor eigen beleidsdoeleinden bij te houden."

De koppeling BRP→BAG (via identificatiecodes in categorie 08) maakt dat elke ingeschreven persoon traceerbaar is naar een [[Verblijfsobject]], [[Ligplaats]] of [[Standplaats]] via een [[Nummeraanduiding]].

Het GGM modelleert de BRP-entiteiten in het beleidsdomein RSGBPlus (128 entiteiten). De kernentiteiten zijn: IngeschrevenPersoon (abstract), Ingezetene, NatuurlijkPersoon (abstract), Rechtspersoon (abstract), Reisdocument, Nationaliteit, Verblijfstitel, SluitingOfAangaanHuwelijkOfGeregistreerdPartnerschap, OntbindingHuwelijk/geregistreerdPartnerschap.

## Bronnen

- [[Sources/Standaarden/logisch-ontwerp-brp-2025q1]]
