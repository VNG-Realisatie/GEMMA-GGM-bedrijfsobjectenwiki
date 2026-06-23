---
type: ggm-beleidsdomein
naam: HR
definitie: "Het informatiesubdomein dat gegevens omvat over het beheer en de ontwikkeling van personeel, gericht op het ondersteunen van de organisatie en haar medewerkers."
taakveld: "9 Interne Organisatie"
aantal_entiteiten: 31
---

# GGM Beleidsdomein: HR

### Bezetting en Formatie

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Dienstverband** | De rechtsbetrekking tussen werkgever en werknemer zoals vastgelegd in een arbeidsovereenkomst. | datumStart, datumEinde, salaris, periodiek, schaal, urenPerWeek | Nee | GGM |
| **Formatieplaats** | Uitgangspunt is het vastgestelde formatieplan, dus niet de werkelijke bezetting. Het gaat hier om de toegestane formatie in fte van het ambtelijk apparaat van uw organisatie voor het begrotingsjaar | uren per week | Nee | GGM |
| **Functie** | Een samenhangende verzameling van rollen. Een functie kan worden gedefinieerd als het samenstel van feitelijk opgedragen taken en werkzaamheden | Naam, Omschrijving, Taken, Schaal, Code | Nee | GGM |
| **Functiehuis** | Model waarin functies van een organisatie worden beschreven. | naam, omschrijving | Nee | GGM |
| **Inzet** | Uren inzet die gepleegd wordt in een bepaalde periode op een organisatorische eenheid en het percentage dat ook daadwerkelijk wordt uitgevoerd.Dit kan afwijken van de contractuele uren. | datumBegin, datumEinde, percentage, uren | Nee | GGM |
| **NormProfiel** | Normprofiel of Normfunctie:nGenerieke functie zoals beschreven in HR21. Een functie kan worden gedefinieerd als het samenstel van feitelijk opgedragen taken en werkzaamheden | code, omschrijving, schaal | Nee | GGM |
| **OrganisatorischeEenheidHR** | Specialisatie van de Organisatorische eenheid uit het RGBZ voor het HR domein. | naam, type | Nee | GGM |
| **Rol** | De rol van de medewerker, zoals afdelingshoofd of manager | datumBegin, datumEinde, omschrijving | Nee | GGM |
| **Werknemer** | De contractuele wederpartij van de werkgever bij de arbeidsovereenkomst. | naam, voornaam, geboortedatum, woonplaats | Nee | GGM |

### Documenten

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Beoordeling** | Beoordeling is het oordeel van de professional over het functioneren van een leerling | datum, oordeel, omschrijving | Nee | GGM |

### Domain Objects

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Declaratie** | Een opgave van te vergoeden kosten. | datumIndiening, datumDeclaratie, betreft, omschrijving, bedrag | Nee | GGM |
| **Declaratiesoort** | Typering van een declaratie | naam, omschrijving | Nee | GGM |
| **Disciplinaire Maatregel** | Een besluit dat wordt opgelegd wanneer een persoon zijn verplichtingen niet of niet op de juiste wijze nakomt, of zich op andere wijze misdraagt. | datumGeconstateerd, datumOpgelegd, omschrijving, reden | Nee | GGM |
| **GenotenOpleiding** | Afgeronde opleiding, een samenhangend geheel van vakken, gericht op de verwezenlijking van welomschreven doelstellingen op het gebied van kennis, inzicht en vaardigheden | datumStart, datumEinde, datumToewijzing, prijs, verrekenen | Nee | GGM |
| **Geweldsincident** | Een gebeurtenis met betrekking tot agressie en omvat het veroorzaken van verwondingen of schade bij mensen, dieren, of voorwerpen. | datum, type, omschrijving | Nee | GGM |
| **Individueel Keuzebudget** | Bedrag dat feitelijk beschikbaar gesteld wordt voor een individu om een bepaalde keus te kunnen maken | datumStart, datumEinde, datumToekenning, bedrag | Nee | GGM |
| **KeuzebudgetBesteding** | De daadwerkelijk uitgave van een keuzebudget | datum, bedrag | Nee | GGM |
| **KeuzebudgetBestedingsoort** | Typering van een keuzebudgetbesteding | naam, omschrijving | Nee | GGM |
| **Onderwijsinstituut** | Een instituut waar onderwijs wordt gegeven. | *(geen attributen)* | Nee | GGM |
| **Opleiding** | Een samenhangend geheel van vakken, gericht op de verwezenlijking van welomschreven doelstellingen op het gebied van kennis, inzicht en vaardigheden. | naam, omschrijving, prijs, instituut | Nee | GGM |
| **Relatie** | Betrekking waarin personen, zaken, begrippen of grootheden van nature tot elkaar staan. | *(geen attributen)* | Nee | GGM |
| **SoortDisciplinaireMaatregel** | Typering van een disciplinaire maatregel | naam, omschrijving | Nee | GGM |
| **Verlof** | Een periode waarin iemand toestemming heeft om iets te doen, in het bijzonder om afwezig te zijn. | datumtijdStart, datumtijdEinde, goedgekeurd, datumAanvraag, datumToekenning | Nee | GGM |
| **Verlofsoort** | Typering van verlof | naam, omschrijving | Nee | GGM |
| **Verzuim** | Een afwezigheid van een werknemer van werk. | datumtijdStart, datumtijdEinde | Nee | GGM |
| **Verzuimsoort** | Typologie van verzuim | naam, omschrijving | Nee | GGM |

### Relaties met Kern

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Sollicitant** | Persoon die werk zoekt | *(geen attributen)* | Nee | GGM |

### Sollicitaties

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Sollicitatie** | Verzoek om in een functie te worden aangesteld. | datum | Nee | GGM |
| **Sollicitatiegesprek** | Onderhoud tussen sollicitant en werkgever met betrekking tot een sollicatie | datum, opmerkingen, volgendGesprek, aangenomen | Nee | GGM |
| **Vacature** | Een arbeidsplaats binnen een bedrijf of organisatie die nog gevuld dient te worden door werkzoekenden. | datumOpengesteld, datumGesloten, intern, extern, deeltijd, vastedienst | Nee | GGM |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Uren** | Aantal besteedde uren aan een activiteit | aantal | Nee | GGM |

## Overervingshiërarchie

```
Medewerker (abstract)
    └── Werknemer
```

```
NatuurlijkPersoon (abstract)
    └── Relatie
    └── Sollicitant
```

```
NietNatuurlijkPersoon (abstract)
    └── Onderwijsinstituut
```

```
OrganisatorischeEenheid (abstract)
    └── OrganisatorischeEenheidHR
```

## Relatiediagrammen

```
Declaratie [0..*] ──── Declaratiesoort [1..1]
Dienstverband ──── Functie
Dienstverband ──── OrganisatorischeEenheidHR
Disciplinaire Maatregel [0..*] ──── SoortDisciplinaireMaatregel [1..1]
Formatieplaats ──── Dienstverband
Formatieplaats ──── Functie
Formatieplaats ──── OrganisatorischeEenheidHR
Functie ──── NormProfiel
GenotenOpleiding [0..*] ──── Opleiding [1..1]
Individueel Keuzebudget [1..1] ──── KeuzebudgetBesteding [0..*]
Individueel Keuzebudget [0..*] ──── Werknemer [1..1]
Inzet ──── Dienstverband
Inzet ──── Functie
Inzet ──── OrganisatorischeEenheidHR
KeuzebudgetBesteding [0..*] ──── KeuzebudgetBestedingsoort [1..1]
NormProfiel ──── Functiehuis
Opleiding [1..*] ──── Onderwijsinstituut [1..*]
Relatie ──── Werknemer
Rol ──── OrganisatorischeEenheidHR
Sollicitant [1..1] ──── Sollicitatie [0..*]
Sollicitatie [0..*] ──── Vacature [1..1]
Sollicitatiegesprek [0..*] ──── Sollicitant [0..*]
Sollicitatiegesprek [0..*] ──── Sollicitatie [1..1]
Sollicitatiegesprek [0..*] ──── Werknemer [1..*]
Uren [1..1] ──── Dienstverband [0..*]
Vacature [0..*] ──── Functie [1..1]
Verlof [0..*] ──── Verlofsoort [1..1]
Verzuim [0..*] ──── Verzuimsoort [1..1]
Werknemer [1..1] ──── Beoordeling [0..*]
Werknemer [1..1] ──── Declaratie [0..*]
Werknemer [1..1] ──── Dienstverband [1..*]
Werknemer [1..1] ──── Disciplinaire Maatregel [0..*]
Werknemer [1..1] ──── GenotenOpleiding [0..*]
Werknemer [0..*] ──── Geweldsincident [1..1]
Werknemer ──── Relatie
Werknemer ──── Rol
Werknemer [1..1] ──── Sollicitatie [0..*]
Werknemer [1..1] ──── Verlof [0..*]
Werknemer [1..1] ──── Verzuim [0..*]
```

## Observaties

- Dit beleidsdomein bevat 31 Objecttype-entiteiten.
- Entiteiten zijn gegroepeerd in 6 diagramgroepen: Bezetting en Formatie (9), Documenten (3), Domain Objects (26), Financien Personen (1), Relaties met Kern (4), Sollicitaties (6).
- Er zijn 5 generalisatierelaties aanwezig.
