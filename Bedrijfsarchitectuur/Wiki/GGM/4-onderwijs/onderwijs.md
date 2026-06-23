---
type: ggm-beleidsdomein
naam: Onderwijs
definitie: "Het informatiedomein dat gegevens omvat over het funderend onderwijs, gericht op het waarborgen van toegang tot en kwaliteit van primair en voortgezet onderwijs voor kinderen en jongeren."
taakveld: "4 Onderwijs"
aantal_entiteiten: 12
---

# GGM Beleidsdomein: Onderwijs

### Diagram Beslissingen Leerplicht

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Leerling** | Mens die een opleiding volgt, heeft gevolgd of gaat volgen of opgaat of is opgegaan voor een toets. (Bron: KOI) | kwetsbareJongere | Nee | GGM |
| **Ouder Of Verzorger** | Een persoon die wettelijk verantwoordelijk is voor de zorg en opvoeding van een kind. | *(geen attributen)* | Nee | GGM |
| **School** | Gebouw in gebruik voor basis, middelbaar of hoger onderwijs. | naam | Nee | GGM |

### Onderwijs: Leerlingen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Inschrijving** | Deelname van iemand aan een opleiding bij een onderwijsinstelling. | datum | Nee | GGM |
| **Leerjaar** | Is de codering van het jaar of het niveau waarin de leerling onderwijs volgt. | jaarStart, jaarEinde | Nee | GGM |
| **Locatie** | De locatie beschrijft middels co&#246;rdinaten de ruimtelijke dimensie of ruimtelijke afbakening van een regel of van een objecttype die in de regel beschreven wordt. (CIMOW) | adres | Nee | GGM |
| **Loopbaanstap** | Een logische en ook uitdagende stap naar een volgende functie binnen dezelfde functiefamilie of een andere, op hetzelfde schaalniveau of op een schaalniveau hoger. | schooljaar, onderwijstype, klas | Nee | GGM |
| **Onderwijsloopbaan** | Loopbaan als leerling in het onderwijs; loopbaan als leerling op school; tijd die iemand als leerling heeft doorgebracht op school, vaak met de bijgedachte aan de daarbij opgedane kennis en ervaring; tijd die men schoolgegaan heeft; onderwijscarri&#232;re; schoolloopbaan; schoolcarri&#232;re; schooltijd; de schooljaren | *(geen attributen)* | Nee | GGM |
| **Onderwijssoort** | Typologie voor onderwijs | onderwijstype, omschrijving | Nee | GGM |
| **Startkwalificatie** | Diploma van een opleiding als bedoeld in de WEB of een diploma hoger algemeen voortgezet onderwijs of voorbereidend wetenschappelijk onderwijs als bedoeld in de WVO; | datumBehaald | Nee | GGM |
| **Uitschrijving** | Beeindiging van een inschrijving van een leerling bij een school | datum, diplomaBehaald | Nee | GGM |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Onderwijsniveau** | De hoogte van een soort onderwijs in relatie tot andere soorten onderwijs | *(geen attributen)* | Nee | GGM |

## Overervingshiërarchie

```
IngeschrevenPersoon (abstract)
    └── Leerling
    └── Ouder Of Verzorger
```

```
NietNatuurlijkPersoon (abstract)
    └── School
    └── School
```

```
Vastgoedobject (abstract)
    └── Locatie
```

## Relatiediagrammen

```
Inschrijving [0..*] ──── School [1..1]
Leerling [1..1] ──── Inschrijving [0..*]
Leerling [1..1] ──── Onderwijsloopbaan [0..*]
Leerling [1..1] ──── Startkwalificatie [0..1]
Leerling [1..1] ──── Uitschrijving [0..*]
Onderwijsloopbaan ──── Loopbaanstap
School [0..1] ──── Locatie [1..*]
School [1..*] ──── Onderwijsloopbaan [0..*]
School [0..*] ──── Onderwijssoort [1..*]
School [1..1] ──── Uitschrijving [0..*]
```

## Observaties

- Dit beleidsdomein bevat 12 Objecttype-entiteiten (+ 1 Enumeraties).
- Entiteiten zijn gegroepeerd in 4 diagramgroepen: Diagram Beslissingen Leerplicht (3), Diagram Sportbeleid (1), Onderwijs: Leerlingen (10), Onderwijs: Relaties met Kern (3).
- Er zijn 5 generalisatierelaties aanwezig.
