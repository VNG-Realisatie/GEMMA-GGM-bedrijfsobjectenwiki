---
type: ggm-beleidsdomein
naam: Sport
definitie: "Dit informatiedomein bevat data over collectiebeheer, tentoonstellingen, bezoekersaantallen en educatieve activiteiten van musea die onderdeel zijn van een overheidsorganisatie. Het ondersteunt de uitvoering van de museale functie conform de Erfgoedwet, inclusief het beheer van eventuele rijkscollecties. De gegevens worden gebruikt voor beleidsontwikkeling, verantwoording en publieksbereik van het cultureel erfgoed."
taakveld: "5 Sport, Cultuur en Recreatie"
aantal_entiteiten: 9
---

# GGM Beleidsdomein: Sport

### Diagram Sportbeleid

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Belijning** | Op of in het oppervlak van de verharding aangebrachte tekens ter geleiding, waarschuwing, regeling of informatie van het verkeer | naam | Nee | GGM |
| **Binnenlocatie** | Locatie binnen een gebouw | bouwjaar, vloeroppervlakte, klokurenOnderwijs, klokurenVerenigingen, onderhoudsstatus, onderhoudsniveau, geschatteKostenPerJaar, locatie, adres, sporthal, gymzaal, gemeentelijk | Nee | GGM |
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

```
Binnenlocatie ──── Belijning
Binnenlocatie ──── Sportmateriaal
Sportpark ──── Veld
Sportvereniging ──── Sportlocatie
Veld ──── Belijning
```

## Observaties

- Dit beleidsdomein bevat 9 Objecttype-entiteiten (+ 4 diagramhulpobjecten zonder stereotype).
- Entiteiten zijn gegroepeerd in 2 diagramgroepen: Diagram Sportbeleid (7), Diagram Sportbeleid Locaties (4).
- Er zijn 3 generalisatierelaties aanwezig.
