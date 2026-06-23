---
type: ggm-beleidsdomein
naam: Leerplicht en Leerlingenvervoer
definitie: "Het informatiedomein dat gegevens omvat over de naleving van de leerplichtwet en de organisatie van leerlingenvervoer, gericht op het waarborgen van toegang tot onderwijs voor alle kinderen en jongeren."
taakveld: "4 Onderwijs"
aantal_entiteiten: 15
---

# GGM Beleidsdomein: Leerplicht en Leerlingenvervoer

Beleidsdomein binnen taakveld "4 Onderwijs" (zie ../structuur-ggm.md).

## Entiteiten

### Diagram Beslissingen Leerplicht

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **AanvraagOfMelding** | Komt overeen met een VJV | datum, opmerkingen, soortVerzuimOfAanvraag, reden | Nee | GGM |
| **AanvraagVrijstelling** | Vrijstelling van een aanvraag voor leerlingenvervoer | datumAanvraag, buitenlandseSchoollocatie | Nee | GGM |
| **Beschikking Leerlingenvervoer** | Een formeel besluit dat genomen wordt door een bevoegde instantie over het al dan niet toekennen van leerlingenvervoer aan een bepaalde leerling. | *(geen attributen)* | Nee | GGM |
| **Beslissing** | Selectie van een voorstelbare werkelijkheid (voorkeursvariant) uit een aantal mogelijke werkelijkheden (varianten) op basis van een verzameling van criteria. | datum, reden, opmerkingen | Nee | GGM |
| **Doorgeleiding OM** | De overdracht van een leerplichtzaak aan het Openbaar Ministerie voor juridische vervolging. | afdoening | Nee | GGM |
| **HALT-verwijzing** | Jongeren van 12 tot 18 jaar die strafbare feiten plegen, zoals bijvoorbeeld: winkeldiefstal, vernieling, openbaar dronkenschap of oplichting kunnen naar Halt worden verwezen. In sommige gevallen is daarvoor toestemming nodig van het Openbaar Ministerie. | afdoening, datumRetour, datumMutatie, memo | Nee | GGM |
| **Klacht Leerlingenvervoer** | Een uiting van ontevredenheid over het vervoer van leerlingen. | *(geen attributen)* | Nee | GGM |
| **Leerplichtambtenaar** | Ambtenaar die toezicht houdt op de uitvoering van de leerplichtwet. | *(geen attributen)* | Nee | GGM |
| **Procesverbaal Onderwijs** | Een officieel document dat een overtreding van de leerplichtwet vastlegt. | reden, opmerkingen, datumIngelicht, sanctiesoort, uitspraak, proeftijd, geldboete, verzuimsoort, datumZitting, datumAfgehandeld, datumUitspraak, datumEindeProeftijd, geldboeteVoorwaardelijk | Nee | GGM |
| **Verlofaanvraag** | Een verzoek om toestemming te krijgen iets te doen, bijvoorbeeld vakantie of studie | datumStart, datumTot, soortVerlof | Nee | GGM |
| **Vervoerder** | Degene die openbaar vervoer of besloten busvervoer verricht, niet in de hoedanigheid van bestuurder van een auto, bus, trein, metro, tram of een via een geleidesysteem voortbewogen voertuig. | *(geen attributen)* | Nee | GGM |
| **Verzuimmelding** | Een melding dat een leerling niet op school verschijnt. De school moet actie ondernemen naar de leerling (en zijn ouders). Een school moet het verzuim melden bij de gemeente. | datumStart, datumEinde, voorstelSchool | Nee | GGM |
| **Vrijstelling** | Een formeel besluit waarbij een leerling wordt ontheven van de leerplicht. | datumStart, datumEinde, aanvraagToegekend, verzuimsoort, buitenlandseSchoollocatie | Nee | GGM |
| **Ziekmelding Leerlingenvervoer** | Een melding van een zieke leerling die recht heeft op vervoer van en naar onderwijs. | *(geen attributen)* | Nee | GGM |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Aanvraag Leerlingenvervoer** | Een aanvraag voor een leerling die recht heeft op vervoer van en naar onderwijs. | *(geen attributen)* | Nee | GGM |

## Overervingshiërarchie

```
AanvraagOfMelding (abstract)
    └── AanvraagOfMelding
    └── AanvraagVrijstelling
    └── Verlofaanvraag
    └── Verzuimmelding
```

```
Beslissing (abstract)
    └── Beschikking Leerlingenvervoer
    └── Doorgeleiding OM
    └── HALT-verwijzing
    └── Procesverbaal Onderwijs
    └── Vrijstelling
```

```
Leverancier (abstract)
    └── Vervoerder
```

```
Medewerker (abstract)
    └── Leerplichtambtenaar
```

## Relatiediagrammen

### Diagram Beslissingen Leerplicht

```
AanvraagOfMelding [0..1] ──── Beslissing [0..1] (leidt tot)
AanvraagOfMelding [0..*] ──── Leerling [1] (betreft)
AanvraagOfMelding [0..*] ──── School [0..1] (betreft)
Beschikking Leerlingenvervoer [0..*] ──── Vervoerder [0..*] (vervoerder)
Beslissing [0..*] ──── Leerling [1] (betreft)
Beslissing [0..*] ──── Leerplichtambtenaar [1] (behandelaar)
Beslissing [0..*] ──── School [0..1] (betreft)
Doorgeleiding OM [0..*] ──── Ouder Of Verzorger [0..*] (verantwoordelijk ouder)
Klacht Leerlingenvervoer [0..*] ──── Leerling [1] (betreft)
Klacht Leerlingenvervoer [0..*] ──── Vervoerder [1] (betreft)
Leerling [1] ──── Procesverbaal Onderwijs [0..*] (betreft leerling)
Leerling [1] ──── Verzuimmelding [0..*] (heeft)
Leerling [1] ──── Vrijstelling [0..*] (heeft)
Leerling [1] ──── Ziekmelding Leerlingenvervoer [0..*] (betreft)
Leerplichtambtenaar [1] ──── Procesverbaal Onderwijs [0..*] (opgelegd door)
Procesverbaal Onderwijs [0..*] ──── Ouder Of Verzorger [1..*] (verantwoordelijke ouder)
Verzuimmelding [0..*] ──── School [1] (heeft)
Vrijstelling [0..*] ──── School [1] (heeft)
```

## Observaties

- Dit beleidsdomein bevat 15 entiteiten.
- Entiteiten zijn gegroepeerd in 2 diagramgroepen: Diagram Beslissingen Leerplicht (14), Overig (1).
- Er zijn 11 generalisatierelaties aanwezig.
