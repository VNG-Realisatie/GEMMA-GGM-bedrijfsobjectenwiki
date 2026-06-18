---
type: ggm-beleidsdomein
naam: Onderwijs
definitie: "Het informatiedomein dat gegevens omvat over het funderend onderwijs, gericht op het waarborgen van toegang tot en kwaliteit van primair en voortgezet onderwijs voor kinderen en jongeren."
taakveld: "4 Onderwijs"
aantal_entiteiten: 12
---

# GGM Beleidsdomein: Onderwijs

Beleidsdomein binnen taakveld "4 Onderwijs" (zie ../structuur-ggm.md).

## Entiteiten

### Onderwijs: Leerlingen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Inschrijving** | Deelname van iemand aan een opleiding bij een onderwijsinstelling. | datum | Nee | GGM |
| **Leerjaar** | Is de codering van het jaar of het niveau waarin de leerling onderwijs volgt. | jaarStart, jaarEinde | Nee | GGM |
| **Leerling** | Mens die een opleiding volgt, heeft gevolgd of gaat volgen of opgaat of is opgegaan voor een toets. (Bron: KOI) | kwetsbareJongere | Nee | GGM |
| **Locatie** | De locatie beschrijft middels co&#246;rdinaten de ruimtelijke dimensie of ruimtelijke afbakening van een regel of van een objecttype die in de regel beschreven wordt. (CIMOW) | adres | Nee | GGM |
| **Loopbaanstap** | Een logische en ook uitdagende stap naar een volgende functie binnen dezelfde functiefamilie of een andere, op hetzelfde schaalniveau of op een schaalniveau hoger. | schooljaar, onderwijstype, klas | Nee | GGM |
| **Onderwijsloopbaan** | Loopbaan als leerling in het onderwijs; loopbaan als leerling op school; tijd die iemand als leerling heeft doorgebracht op school, vaak met de bijgedachte aan de daarbij opgedane kennis en ervaring; tijd die men schoolgegaan heeft; onderwijs<font color="#0e0e0e">carri&#232;re</font>; schoolloopbaan; school<font color="#0e0e0e">carri&#232;re</font>; schooltijd; de schooljaren | *(geen attributen)* | Nee | GGM |
| **Onderwijssoort** | Typologie voor onderwijs | onderwijstype, omschrijving | Nee | GGM |
| **School** | Gebouw in gebruik voor basis, middelbaar of hoger onderwijs. | naam | Nee | GGM |
| **Startkwalificatie** | Diploma van een opleiding als bedoeld in de WEB of een diploma hoger algemeen voortgezet onderwijs of voorbereidend wetenschappelijk onderwijs als bedoeld in de WVO; | datumBehaald | Nee | GGM |
| **Uitschrijving** | Beeindiging van een inschrijving van een leerling bij een school | datum, diplomaBehaald | Nee | GGM |

### Onderwijs: Relaties met Kern

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Ouder Of Verzorger** | Een persoon die wettelijk verantwoordelijk is voor de zorg en opvoeding van een kind. | *(geen attributen)* | Nee | GGM |

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
```

```
Vastgoedobject (abstract)
    └── Locatie
```

## Relatiediagrammen

### Onderwijs: Leerlingen

```
AanvraagOfMelding [0..*] ──── Leerling [1] (betreft)
AanvraagOfMelding [0..*] ──── School [0..1] (betreft)
Beslissing [0..*] ──── Leerling [1] (betreft)
Beslissing [0..*] ──── School [0..1] (betreft)
Inschrijving [0..*] ──── School [1] (heeft)
Klacht Leerlingenvervoer [0..*] ──── Leerling [1] (betreft)
Leerling [1] ──── Inschrijving [0..*] (heeft)
Leerling [1] ──── Onderwijsloopbaan [0..*] (heeft)
Leerling [1] ──── Procesverbaal Onderwijs [0..*] (betreft leerling)
Leerling [1] ──── Startkwalificatie [0..1] (heeft)
Leerling [1] ──── Uitschrijving [0..*] (heeft)
Leerling [1] ──── Verzuimmelding [0..*] (heeft)
Leerling [1] ──── Vrijstelling [0..*] (heeft)
Leerling [1] ──── Ziekmelding Leerlingenvervoer [0..*] (betreft)
School [0..1] ──── Locatie [1..*] (school heeft)
School [1..*] ──── Onderwijsloopbaan [0..*] (kent)
School [0..*] ──── Onderwijssoort [1..*] (heeft)
School [0..*] ──── Sportlocatie [0..*] (gebruikt)
School [1] ──── Uitschrijving [0..*] (heeft)
Verzuimmelding [0..*] ──── School [1] (heeft)
Vrijstelling [0..*] ──── School [1] (heeft)
```

### Onderwijs: Relaties met Kern

```
Doorgeleiding OM [0..*] ──── Ouder Of Verzorger [0..*] (verantwoordelijk ouder)
Procesverbaal Onderwijs [0..*] ──── Ouder Of Verzorger [1..*] (verantwoordelijke ouder)
```

## Observaties

- Dit beleidsdomein bevat 12 entiteiten.
- Entiteiten zijn gegroepeerd in 3 diagramgroepen: Onderwijs: Leerlingen (10), Onderwijs: Relaties met Kern (1), Overig (1).
- Er zijn 5 generalisatierelaties aanwezig.
