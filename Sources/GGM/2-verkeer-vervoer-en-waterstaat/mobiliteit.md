---
type: ggm-beleidsdomein
naam: Mobiliteit
definitie: "Het informatiedomein dat de structuur, definities en relaties van gegevens omvat met betrekking tot verkeer en vervoer van personen en goederen, gericht op het faciliteren van efficiënte en duurzame mobiliteit."
taakveld: "2 Verkeer, Vervoer en Waterstaat"
aantal_entiteiten: 7
---

# GGM Beleidsdomein: Mobiliteit

Beleidsdomein binnen taakveld "2 Verkeer, Vervoer en Waterstaat" (zie ../structuur-ggm.md).

## Entiteiten

### Verkeer en Vervoer: Stremmingen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Stremming** | Situatie waarbij de doorstroming van het (vaar)wegverkeer plaatselijk is geblokkeerd als gevolg van een incident | naam, datumStart, datumEinde, datumAanmelding, status, datumWijziging, geschiktVoorPublicatie, delenToegestaan, locatie, hinderklasse, aantalGehinderden | Nee | GGM |

### Diagram Verkeer en Vervoer

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **VLogInfo** | V-log is een open standaard voor datalogging van een verkeersregelinstallatie. | tijdstip, snelheid, startgroen, eindegroen, verkeerWilGroen, wachttijd, detectieVerkeer | Nee | GGM |
| **Verkeerstelling** | Een onderzoek om inzicht te krijgen in het verkeer, in de hoeveelheid verkeer, de verdeling en de gereden snelheid. | tijdVanaf, tijdTot, aantal | Nee | GGM |

### Gladheid

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Strooidag** | Dag waarop op wegen gestrooid wordt ter voorkoming van gladheid | datum, minimumtemperatuur, tijdMinimumtemperatuur, maximumtemperatuur, tijdMaximumtemperatuur | Nee | GGM |
| **Strooiroute** | Traject waarop het strooien plaatsvindt | route | Nee | GGM |
| **StrooirouteUitvoering** | De route die uiteindelijk is gevolgd voor het strooien | route, geplandStart, geplandEinde, werkelijkeStart, werkelijkEinde | Nee | GGM |

### Verkeersbesluiten

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Verkeersbesluit** | Een besluit van een wegbeheerder om een bepaald verkeersteken te plaatsen, te wijzigen of in te trekken of een bepaalde fysieke maatregel te treffen. | referentienummer, datumBesluit, datumStart, titel, straat, postcode, huisnummer, datumEinde | Nee | GGM |

## Overervingshiërarchie

Geen overervingshiërarchie aanwezig in dit beleidsdomein.

## Relatiediagrammen

### Verkeer en Vervoer: Stremmingen

```
Medewerker [1] ──── Stremming [0..*] (ingevoerd door)
Medewerker [0..1] ──── Stremming [0..*] (gewijzigd door)
Stremming [0..*] ──── Wegdeel [0..*] (betreft)
```

### Diagram Verkeer en Vervoer

```
Sensor [1] ──── Verkeerstelling [0..*] (gegenereerd door)
VLogInfo [0..*] ──── Kast [0..1] (gegenereerd door)
VLogInfo [0..*] ──── Paal [0..1] (gegenereerd door)
VLogInfo [0..*] ──── Sensor [0..1] (gegenereerd door)
```

### Gladheid

```
StrooirouteUitvoering [0..*] ──── Strooidag [0..1] (uitvoering op)
StrooirouteUitvoering [0..*] ──── Strooiroute [1] (volgens)
```

### Verkeersbesluiten

```
Verkeersbesluit [1] ──── Document [1] (is vastgelegd in)
```

## Observaties

- Dit beleidsdomein bevat 7 entiteiten.
- Entiteiten zijn gegroepeerd in 4 diagramgroepen: Verkeer en Vervoer: Stremmingen (1), Diagram Verkeer en Vervoer (2), Gladheid (3), Verkeersbesluiten (1).
