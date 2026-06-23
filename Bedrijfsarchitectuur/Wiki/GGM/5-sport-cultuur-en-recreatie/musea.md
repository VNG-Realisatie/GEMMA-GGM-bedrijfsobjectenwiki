---
type: ggm-beleidsdomein
naam: Musea
definitie: "Het informatiedomein dat gegevens omvat over de verwerving, het beheer, het onderzoek en de presentatie van museale collecties en tentoonstellingen binnen een overheidsorganisatie."
taakveld: "5 Sport, Cultuur en Recreatie"
aantal_entiteiten: 30
---

# GGM Beleidsdomein: Musea

### Generieke entiteiten Erfgoed

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Museumobject** | Beschrijving van een fenomeen in de werkelijkheid met een zekere cultuurhistorische waarde die deel uitmaakt van de culthuurhistorisch object index. Een museum object kan gedifiniëerd worden als een object met betrekking tot gebouwd, archeologisch, roerend of cultuurlandschappelijk erfgoed. Denk hierbij bijvoorbeeld aan een gebouwd of archeologisch rijksmonument, een schilderij of een beschermd stads- of dorpsgezicht. | verkrijging, medium, afmeting, bezitVanaf, bezitTot | Nee | GGM |

### Prinsenhof Collectie

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Belanghebbende** | Een persoon wiens belang rechtstreeks bij een besluit is betrokken. | datumStart, datumTot | Nee | GGM |
| **Bruikleen** | Lening voor tijdelijk gebruik | datumAanvraag, datumStart, datumEinde, aanvraagDoor, toestemmingDoor | Nee | GGM |
| **Collectie** | Een verzameling van verworven voorwerpen die is samengesteld op grond van vastgestelde criteria. | naam, omschrijving | Nee | GGM |
| **Incident** | Niet-gepland(e) gebeurtenis die of voorval dat tot schade of verlies leidt | naam, omschrijving, datum, locatie | Nee | GGM |
| **Lener** | Iemand die iets te leen krijgt, met name iemand die boeken, digitale bestanden of apparatuur leent bij een museum, bibliotheek, mediatheek of een andere uitleeninstantie | opmerkingen | Nee | GGM |
| **Samensteller** | Iemand die stukken informatie samenbrengt in tentoonstelingen, presentaties en naslagwerken. | rol | Nee | GGM |
| **Standplaats** | vanaf een vaste locatie te koop aanbieden, verkopen of afleveren van goederen of aanbieden van diensten, gebruikmakend van fysieke middelen zoals een kraam, een wagen of een tafel | beschrijving, adres, naamInstelling | Nee | GGM |
| **Tentoonstelling** | Een uitstalling van voorwerpen om door het grote publiek bekeken te worden. | titel, omschrijving, datumStart, datumEinde, subtitel | Nee | GGM |
| **Zaal** | Grote ruimte in een gebouw | naam, omschrijving, capaciteit, nummer | Nee | GGM |

### Prinsenhof Events en Relaties

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Activiteit** | Ieder menselijk handelen waarbij, of ieder menselijk nalaten waardoor een verandering of effect in de (fysieke) leefomgeving wordt of kan worden bewerkstelligd. | naam, omschrijving, aantalPersonen | Nee | GGM |
| **Activiteitsoort** | Typering van een activiteit | naam, omschrijving | Nee | GGM |
| **Doelgroep** | Een groep mensen of klanten die een bedrijf of organisatie wil benaderen om een product, dienst of informatie onder de aandacht te brengen | naam, omschrijving, branch, segment | Nee | GGM |
| **Mailing** | Per post verstuurde inhoud | naam, omschrijving, datum | Nee | GGM |
| **Museumrelatie** | Betrekking waarin het museum en personen tot elkaar staan | relatiesoort | Nee | GGM |
| **Productie-eenheid** | Een (deel van een) productiemiddel, dat zelfstandig (ofwel onafhankelijk van de andere delen van het desbetreffende productiemiddel) kan worden ingezet. | *(geen attributen)* | Nee | GGM |
| **Programma** | Een tijdelijke, flexibele organisatiestructuur, die is opgezet om de implementatie van een verzameling met elkaar samenhangende projecten en activiteiten te co&#246;rdineren, te sturen en te controleren teneinde te zorgen voor de realisatie van de eindresultaten en benefits die zijn gerelateerd aan de strategische doelstellingen van de organisatie. | naam, omschrijving, starttijd, eindtijd, prijsExclusiefBTW, BTW, locatie, publiekstaak, schoolniveau | Nee | GGM |
| **Programmasoort** | Typering van een programma | naam, omschrijving | Nee | GGM |
| **Reservering** | Het vooraf bespreken van een plaats in een openbare gelegenheid, vervoermiddel, restaurant e.d. | aantal, tijdVanaf, tijdTot, totaalprijs, BTW | Nee | GGM |
| **Rondleiding** | Bezichtiging met toelichting | naam, omschrijving, starttijd, eindtijd | Nee | GGM |
| **Voorziening** | Middel om services/maatregelen in te vullen. | naam, omschrijving, aantalBeschikbaar | Nee | GGM |

### Prinsenhof Verkoop

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Balieverkoop** | Verkoop aan de balie | verkooptijd, kanaal, aantal | Nee | GGM |
| **Balieverkoop Entreekaart** | Verkoop van een entreekaart aan de balie | rondleiding, datumStart, datumEindeGeldigheid, gebruiktOp | Nee | GGM |
| **Entreekaart** | Bewijs van toegang tot een gebouw of voorstelling | rondleiding | Nee | GGM |
| **Omzetgroep** | Artikelen worden gebruikt om omzet te registreren in de shop, de horeca of elders. De omzet wordt vervolgens getotaliseerd op rapportages. Om de artikelen te groeperen moet ieder artikel tot een omzetgroep behoren. | naam, omschrijving | Nee | GGM |
| **Product** | Het resultaat van een proces dat in het economisch verkeer een waarde bezit. | omschrijving, prijs, datumStart, datumEindeGeldigheid, codeMuseumjaarkaart, entreekaart | Nee | GGM |
| **Productgroep** | Groepering van producten | naam, omschrijving | Nee | GGM |
| **Winkelvoorraaditem** | Onderdeel in de winkelvoorraad | aantal, locatie, aantalInBestelling, datumLeveringBestelling | Nee | GGM |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Prijs** | De te betalen hoeveelheid geld | bedrag, datumStart, datumEindeGeldigheid | Nee | GGM |
| **Winkelverkoopgroep** | Groepering van winkelverkopen | *(geen attributen)* | Nee | GGM |

## Overervingshiërarchie

```
Balieverkoop (abstract)
    └── Balieverkoop Entreekaart
```

```
Erfgoed Object (abstract)
    └── Museumobject
```

```
Medewerker (abstract)
    └── Samensteller
```

```
Product (abstract)
    └── Entreekaart
```

```
Rechtspersoon (abstract)
    └── Belanghebbende
    └── Lener
    └── Museumrelatie
```

## Relatiediagrammen

```
Activiteit [1] ──── Activiteit [0..*] (bestaat uit)
Activiteit [0..*] ──── Activiteitsoort [1] (van soort)
Activiteit [1..1] ──── Reservering [0..*] (heeft)
Activiteit [0..*] ──── Rondleiding [0..1] (heeft)
Balieverkoop [0..*] ──── Prijs [1] (tegen prijs)
Balieverkoop [0..*] ──── Product [1] (betreft)
Bruikleen [0..*] ──── Tentoonstelling [0..*] (is bedoeld voor)
Collectie [0..*] ──── Museumobject [0..*] (bevat)
Doelgroep [1] ──── Doelgroep [0..*] (bestaat uit)
Incident [0..*] ──── Museumobject [0..*] (betreft)
Lener [1..*] ──── Bruikleen [0..*] (is)
Mailing [0..*] ──── Museumrelatie [0..*] (versturen aan)
Museumobject [0..*] ──── Belanghebbende [0..*] (heeft)
Museumobject [0..*] ──── Bruikleen [0..1] (In TMS loopt dit via LoanObjRefs)
Museumobject [0..*] ──── Standplaats [0..1] (locatie)
Museumobject [0..*] ──── Tentoonstelling [0..*] (onderdeel)
Museumrelatie [0..*] ──── Doelgroep [0..*] (valt binnen)
Museumrelatie [1] ──── Programma [0..*] (voor)
Product [0..*] ──── Omzetgroep [0..*] (valt binnen)
Product [1] ──── Prijs [1..*] (heeft prijs)
Product [0..*] ──── Productgroep [0..*] (valt binnen)
Programma [1] ──── Activiteit [0..*] (bestaat uit)
Programma [0..*] ──── Programmasoort [0..*] (voor)
Reservering [0..*] ──── Productie-eenheid [0..1] (betreft)
Reservering [0..*] ──── Voorziening [0..1] (betreft)
Reservering [0..*] ──── Zaal [0..1] (betreft)
Rondleiding [0..*] ──── Tentoonstelling [0..1] (voor)
Samensteller [0..*] ──── Tentoonstelling [0..*] (stelt samen)
Tentoonstelling [0..*] ──── Zaal [0..*]
Winkelvoorraaditem [0..1] ──── Product [1] (betreft)
```

## Observaties

- Dit beleidsdomein bevat 30 Objecttype-entiteiten (+ 2 diagramhulpobjecten zonder stereotype).
- Entiteiten zijn gegroepeerd in 4 diagramgroepen: Generieke entiteiten Erfgoed (1), Prinsenhof Collectie (10), Prinsenhof Events en Relaties (13), Prinsenhof Verkoop (7).
- Er zijn 7 generalisatierelaties aanwezig.
