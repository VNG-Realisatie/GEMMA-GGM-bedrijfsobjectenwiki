---
type: ggm-beleidsdomein
naam: Sport
definitie: "Dit informatiedomein bevat data over collectiebeheer, tentoonstellingen, bezoekersaantallen en educatieve activiteiten van musea die onderdeel zijn van een overheidsorganisatie. Het ondersteunt de uitvoering van de museale functie conform de Erfgoedwet, inclusief het beheer van eventuele rijkscollecties. De gegevens worden gebruikt voor beleidsontwikkeling, verantwoording en publieksbereik van het cultureel erfgoed."
taakveld: "5 Sport, Cultuur en Recreatie"
aantal_entiteiten: 13
---

# GGM Beleidsdomein: Sport

Beleidsdomein binnen taakveld "5 Sport, Cultuur en Recreatie" (zie ../structuur-ggm.md).

## Entiteiten

### Diagram Sportbeleid

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Belijning** | Op of in het oppervlak van de verharding aangebrachte tekens ter geleiding, waarschuwing, regeling of informatie van het verkeer | naam | Nee | GGM |
| **Binnenlocatie** | Locatie binnen een gebouw | bouwjaar, vloeroppervlakte, klokurenOnderwijs, klokurenVerenigingen, onderhoudsstatus, onderhoudsniveau, geschatteKostenPerJaar, locatie, adres, sporthal, gymzaal, gemeentelijk | Nee | GGM |
| **Proxyconnector** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **Proxyconnector** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **Proxyconnector** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **Proxyconnector** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **Sportlocatie** | Locatie waar de betreffende sport plaatsvindt | naam | Nee | GGM |
| **Sportmateriaal** | Materieel om sport mee te beoefenen of ter odnersteuning van de sportuitvoering. | naam | Nee | GGM |
| **Sportpark** | Geheel van terreinen, gebouwen en voorzieningen voor verschillende takken van sport. | *(geen attributen)* | Nee | GGM |
| **Sportvereniging** | Organisatievorm waarin sport bedreven kan worden | naam, typeSport, binnensport, buitensport, email, adres, ledenaantal, aantalNormTeams | Nee | GGM |
| **Veld** | Een stuk land dat speciaal voor het bedrijven van een veldsport gereedgemaakt is | *(geen attributen)* | Nee | GGM |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Bezetting** | Aantal deelnemers aan een activiteit | *(geen attributen)* | Nee | GGM |
| **Onderhoudskosten** | Kosten voor het onderhoud van iemand of iets, hetzij om te voorzien in de levensbehoeften van personen, hetzij voor de instandhouding en verzorging van zaken. | *(geen attributen)* | Nee | GGM |

## Overervingshiërarchie

```
NietNatuurlijkPersoon (abstract)
    └── Sportvereniging
```

```
Sportlocatie (abstract)
    └── Binnenlocatie
    └── Sportpark
```

## Relatiediagrammen

### Diagram Sportbeleid

```
Binnenlocatie [0..*] ──── Belijning [0..*] (heeft)
Binnenlocatie [0..*] ──── Sportmateriaal [0..*] (heeft)
Binnenlocatie [0..*] ──── Verblijfsobject [0..1] (is gevestigd in)
Binnenlocatie [0..*] ──── Wijk [1] (bedient)
Proxyconnector  ──── Proxyconnector 
School [0..*] ──── Sportlocatie [0..*] (gebruikt)
Sportpark [0..1] ──── OverigBenoemdTerrein [1] (ligt op)
Sportpark [0..1] ──── Veld [0..*] (heeft)
Sportvereniging [0..*] ──── Sport [1..*] (oefent uit)
Sportvereniging [0..*] ──── Sportlocatie [0..*] (gebruikt)
Veld [0..*] ──── Belijning [0..*] (heeft)
Veld [0..1] ──── OverigBenoemdTerrein [1] (ligt op)
```

## Observaties

- Dit beleidsdomein bevat 13 entiteiten.
- Entiteiten zijn gegroepeerd in 2 diagramgroepen: Diagram Sportbeleid (11), Overig (2).
- Er zijn 3 generalisatierelaties aanwezig.
