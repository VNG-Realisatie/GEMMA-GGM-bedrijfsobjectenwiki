---
type: ggm-beleidsdomein
naam: Parkeren
definitie: "Het informatiedomein dat gegevens omvat over het stilstaan van voertuigen op een daarvoor bestemde plaats, met als doel het reguleren van parkeerruimte en het bevorderen van leefbaarheid, bereikbaarheid en mobiliteit binnen de gemeente."
taakveld: "2 Verkeer, Vervoer en Waterstaat"
aantal_entiteiten: 13
---

# GGM Beleidsdomein: Parkeren

Beleidsdomein binnen taakveld "2 Verkeer, Vervoer en Waterstaat" (zie ../structuur-ggm.md).

## Entiteiten

### Model Parkeren

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Belprovider** | Leverancier of dienstverlener van modiele beldiensten | code | Nee | GGM |
| **MulderFeit** | Een administratieve overtreding met betrekking tot parkeren, zoals bepaald onder de Wet administratiefrechtelijke handhaving verkeersvoorschriften (WAHV), ook wel bekend als de Mulderwet. | bonnummer, overtreding, vorderingnummer, dienstCD, bedrag, parkeertarief, datumBezwaar, bezwaarToegewezen, bezwaarIngetrokken, bezwaarAfgehandeld, datumGeseponeerd, datumBetaling, datumIndiening, redenSeponeren, organisatie | Nee | GGM |
| **Naheffing** | Het achteraf vorderen van te weinig betaalde belasting | bonnummer, overtreding, vorderingnummer, dienstCD, fiscaal, bedrag, parkeertarief, datumBezwaar, bezwaarToegewezen, bezwaarIngetrokken, bezwaarAfgehandeld, datumGeseponeerd, datumBetaling, datumIndiening, redenSeponeren, organisatie | Nee | GGM |
| **Parkeergarage** | Open constructie die geheel of gedeeltelijk in gebruik is als voorziening voor het parkeren van voertuigen | *(geen attributen)* | Nee | GGM |
| **Parkeerrecht** | Het onder bepaalde voorwaarden (zoals betaling parkeerbelasting of parkeergeld) ontstane recht om een voertuig gedurende een bepaalde of onbepaalde periode op een daartoe benoemde parkeerplaats of in/op een daartoe benoemde parkeervoorziening te parkeren. | datumtijdStart, datumtijdEinde, aanmaaktijd, productnaam, productomschrijving, bedragAankoop, bedragBTW | Nee | GGM |
| **Parkeerscan** | Waarneming van een parkeeractie door een scanauto | transactieID, codeScanvoertuig, codeGebruiker, kenteken, coordinaten, parkeerrecht, tijdstip, foto | Nee | GGM |
| **Parkeervergunning** | Officiele toestemming dat je op een bepaalde plek mag parkeren | nummer, type, datumStart, datumEindeGeldigheid, datumReservering, minutenAfgeschreven, minutenGeldig, minutenResterend, kenteken | Nee | GGM |
| **Parkeervlak** | Parkeergelegenheid bestemd voor het parkeren van een of meerdere voertuigen direct langs de doorgaande weg gelegen. | vlakID, doelgroep, plaats, coordinaten, fiscaal, aantal | Nee | GGM |
| **Parkeerzone** | Een afgebakend gebied binnen een gemeente waar specifieke parkeerregels en -voorwaarden van toepassing zijn. | geometrie, naam, sectorcode, typeCode, typeNaam, soortCode, IPMCode, IPMNaam, gebruik, aantalParkeervlakken, alleenDagtarief, uurtarief, dagtarief, starttarief, startdag, eindedag, starttijd, eindtijd, isParkeergarage | Nee | GGM |
| **Productgroep** | Groepering van producten | code, omschrijving, beslisboom | Nee | GGM |
| **Productsoort** | Typologie van een product | code, omschrijving, tarief, tariefperiode | Nee | GGM |
| **Straatsectie** | Gedeelte van een straat | code, omschrijving, zoneCode | Nee | GGM |
| **Voertuig** | Vervoermiddel bestemd voor het verkeer over wegen | kenteken, merk, kleur, type, land | Nee | GGM |

## Overervingshiërarchie

```
Leverancier (abstract)
    └── Belprovider
```

```
Parkeerzone (abstract)
    └── Parkeergarage
```

## Relatiediagrammen

### Model Parkeren

```
MulderFeit [0..*] ──── Voertuig [0..1] (betreft voertuig)
Object [0..1] ──── Voertuig [0..1] (is)
Parkeerrecht [0..*] ──── Belprovider [0..1] (leverancier)
Parkeerrecht [0..*] ──── Parkeerzone [1..*] (betreft)
Parkeerrecht [0..*] ──── Voertuig [1] (betreft)
Parkeerscan [0..*] ──── Medewerker [1] (uitgevoerd door)
Parkeerscan [0..1] ──── Naheffing [0..1] (komt voort uit)
Parkeerscan [0..1] ──── Parkeerrecht [0..1] (verificatie)
Parkeerscan [0..*] ──── Parkeervlak [1] (betreft)
Parkeerscan [0..*] ──── Voertuig [1] (betreft)
Parkeervergunning [*] ──── Ingezetene [1]
Parkeervergunning [0..1] ──── Parkeerrecht [0..1] (resulteert)
Parkeervergunning [0..*] ──── Parkeerzone [1..*] (geldig voor)
Parkeervergunning [0..*] ──── Rechtspersoon [1] (houder)
Parkeerzone [1] ──── Parkeervlak [0..*] (bevat)
Parkeerzone [1] ──── Straatsectie [0..*] (bevat)
Productgroep [1] ──── Parkeervergunning [0..*] (soort)
Productsoort [1] ──── Parkeervergunning [0..*] (soort)
Productsoort [0..*] ──── Productgroep [1] (valt binnen)
Straatsectie [1] ──── Parkeervlak [0..*] (bevat)
```

## Observaties

- Dit beleidsdomein bevat 13 entiteiten.
- Entiteiten zijn gegroepeerd in 1 diagramgroepen: Model Parkeren (13).
- Er zijn 2 generalisatierelaties aanwezig.
