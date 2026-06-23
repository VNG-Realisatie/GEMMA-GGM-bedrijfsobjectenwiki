---
type: ggm-beleidsdomein
naam: Parkeren
definitie: "Het informatiedomein dat gegevens omvat over het stilstaan van voertuigen op een daarvoor bestemde plaats, met als doel het reguleren van parkeerruimte en het bevorderen van leefbaarheid, bereikbaarheid en mobiliteit binnen de gemeente."
taakveld: "2 Verkeer, Vervoer en Waterstaat"
aantal_entiteiten: 13
---

# GGM Beleidsdomein: Parkeren

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

```
MulderFeit ──── Voertuig
Parkeerrecht [0..*] ──── Belprovider [0..1]
Parkeerrecht ──── Parkeerzone
Parkeerrecht ──── Voertuig
Parkeerscan [0..1] ──── Naheffing [0..1]
Parkeerscan ──── Parkeerrecht
Parkeerscan ──── Parkeervlak
Parkeerscan ──── Voertuig
Parkeervergunning ──── Parkeerrecht
Parkeervergunning ──── Parkeerzone
Parkeerzone [1..1] ──── Parkeervlak [0..*]
Parkeerzone [1..1] ──── Straatsectie [0..*]
Productgroep ──── Parkeervergunning
Productsoort ──── Parkeervergunning
Productsoort [0..*] ──── Productgroep [1..1]
Straatsectie [1..1] ──── Parkeervlak [0..*]
```

## Observaties

- Dit beleidsdomein bevat 13 Objecttype-entiteiten (+ 2 Enumeraties).
- Entiteiten zijn gegroepeerd in 2 diagramgroepen: Model Parkeren (13), Objecten bij Vergunningaanvraag (1).
- Er zijn 2 generalisatierelaties aanwezig.
