---
type: ggm-beleidsdomein
naam: HR
definitie: "Het informatiesubdomein dat gegevens omvat over het beheer en de ontwikkeling van personeel, gericht op het ondersteunen van de organisatie en haar medewerkers."
taakveld: "9 Interne Organisatie"
aantal_entiteiten: 31
---

# GGM Beleidsdomein: HR

Beleidsdomein binnen taakveld "9 Interne Organisatie" (zie ../structuur-ggm.md).

## Entiteiten

### Domain Objects

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Beoordeling** | Beoordeling is het oordeel van de professional over het functioneren van een leerling | datum, oordeel, omschrijving | Nee | GGM |
| **Declaratie** | Een opgave van te vergoeden kosten. | datumIndiening, datumDeclaratie, betreft, omschrijving, bedrag | Nee | GGM |
| **Declaratiesoort** | Typering van een declaratie | naam, omschrijving | Nee | GGM |
| **Dienstverband** | De rechtsbetrekking tussen werkgever en werknemer zoals vastgelegd in een arbeidsovereenkomst. | datumStart, datumEinde, salaris, periodiek, schaal, urenPerWeek | Nee | GGM |
| **Disciplinaire Maatregel** | Een besluit dat wordt opgelegd wanneer een persoon zijn verplichtingen niet of niet op de juiste wijze nakomt, of zich op andere wijze misdraagt. | datumGeconstateerd, datumOpgelegd, omschrijving, reden | Nee | GGM |
| **Formatieplaats** | Uitgangspunt is het vastgestelde formatieplan, dus niet de werkelijke bezetting. Het gaat hier om de toegestane formatie in fte van het ambtelijk apparaat van uw organisatie voor het begrotingsjaar | uren per week | Nee | GGM |
| **Functie** | Een samenhangende verzameling van rollen. Een functie kan worden gedefinieerd als het samenstel van feitelijk opgedragen taken en werkzaamheden | Naam, Omschrijving, Taken, Schaal, Code | Nee | GGM |
| **Functiehuis** | Model waarin functies van een organisatie worden beschreven. | naam, omschrijving | Nee | GGM |
| **GenotenOpleiding** | Afgeronde opleiding, een samenhangend geheel van vakken, gericht op de verwezenlijking van welomschreven doelstellingen op het gebied van kennis, inzicht en vaardigheden | datumStart, datumEinde, datumToewijzing, prijs, verrekenen | Nee | GGM |
| **Geweldsincident** | Een gebeurtenis met betrekking tot agressie en omvat het veroorzaken van verwondingen of schade bij mensen, dieren, of voorwerpen. | datum, type, omschrijving | Nee | GGM |
| **Individueel Keuzebudget** | Bedrag dat feitelijk beschikbaar gesteld wordt voor een individu om een bepaalde keus te kunnen maken | datumStart, datumEinde, datumToekenning, bedrag | Nee | GGM |
| **Inzet** | Uren inzet die gepleegd wordt in een bepaalde periode op een organisatorische eenheid en het percentage dat ook daadwerkelijk wordt uitgevoerd.Dit kan afwijken van de contractuele uren. | datumBegin, datumEinde, percentage, uren | Nee | GGM |
| **KeuzebudgetBesteding** | De daadwerkelijk uitgave van een keuzebudget | datum, bedrag | Nee | GGM |
| **KeuzebudgetBestedingsoort** | Typering van een keuzebudgetbesteding | naam, omschrijving | Nee | GGM |
| **NormProfiel** | Normprofiel of Normfunctie:nGenerieke functie zoals beschreven in HR21. Een functie kan worden gedefinieerd als het samenstel van feitelijk opgedragen taken en werkzaamheden | code, omschrijving, schaal | Nee | GGM |
| **Onderwijsinstituut** | Een instituut waar onderwijs wordt gegeven. | *(geen attributen)* | Nee | GGM |
| **Opleiding** | Een samenhangend geheel van vakken, gericht op de verwezenlijking van welomschreven doelstellingen op het gebied van kennis, inzicht en vaardigheden. | naam, omschrijving, prijs, instituut | Nee | GGM |
| **OrganisatorischeEenheidHR** | Specialisatie van de Organisatorische eenheid uit het RGBZ voor het HR domein. | naam, type | Nee | GGM |
| **Relatie** | Betrekking waarin personen, zaken, begrippen of grootheden van nature tot elkaar staan. | *(geen attributen)* | Nee | GGM |
| **Rol** | De rol van de medewerker, zoals afdelingshoofd of manager | datumBegin, datumEinde, omschrijving | Nee | GGM |
| **SoortDisciplinaireMaatregel** | Typering van een disciplinaire maatregel | naam, omschrijving | Nee | GGM |
| **Verlof** | Een periode waarin iemand toestemming heeft om iets te doen, in het bijzonder om afwezig te zijn. | datumtijdStart, datumtijdEinde, goedgekeurd, datumAanvraag, datumToekenning | Nee | GGM |
| **Verlofsoort** | Typering van verlof | naam, omschrijving | Nee | GGM |
| **Verzuim** | Een afwezigheid van een werknemer van werk. | datumtijdStart, datumtijdEinde | Nee | GGM |
| **Verzuimsoort** | Typologie van verzuim | naam, omschrijving | Nee | GGM |
| **Werknemer** | De contractuele wederpartij van de werkgever bij de arbeidsovereenkomst. | naam, voornaam, geboortedatum, woonplaats | Nee | GGM |

### Sollicitaties

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Sollicitant** | Persoon die werk zoekt | *(geen attributen)* | Nee | GGM |
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

### Domain Objects

```
Declaratie [0..*] ──── Declaratiesoort [1] (soort declaratie)
Dienstverband [0..*] ──── Functie [1] (dienstverband conform functie)
Dienstverband [0..*] ──── OrganisatorischeEenheidHR [1..*] (onderdeel van)
Dienstverband [0..*] ──── VestigingVanZaakbehandelendeOrganisatie [0..*] (is op vestiging)
Disciplinaire Maatregel [0..*] ──── SoortDisciplinaireMaatregel [1] (soort maatregel)
Formatieplaats [0..*] ──── Dienstverband [0..*] (toegewezen aan)
Formatieplaats [0..*] ──── Functie [1..*] (functie van formatieplaats)
Formatieplaats [1] ──── OrganisatorischeEenheidHR [0..1] (onderdeel van)
Functie [1] ──── NormProfiel [1] (gebaseerd op)
GenotenOpleiding [0..*] ──── Opleiding [1] (soort opleiding)
Individueel Keuzebudget [1] ──── KeuzebudgetBesteding [0..*] (besteding)
Individueel Keuzebudget [0..*] ──── Werknemer [1] (heeft individueel keuzebudget)
Inzet [1] ──── Dienstverband [0..*] (aantal volgens inzet)
Inzet [1] ──── Functie [1] (inzet voor functie)
Inzet [0..*] ──── OrganisatorischeEenheidHR [1] (inzet bij)
KeuzebudgetBesteding [0..*] ──── KeuzebudgetBestedingsoort [1] (soort besteding)
NormProfiel [1..*] ──── Functiehuis [1] (onderdeel van)
Opdrachtgever [0..*] ──── Functie [1] (uitgevoerd door)
Opdrachtnemer [0..*] ──── Functie [1] (uitgevoerd door)
Opleiding [1..*] ──── Onderwijsinstituut [1..*] (wordt gegeven door)
Relatie [0..*] ──── Werknemer [1] (is kind van)
Rol [0..*] ──── OrganisatorischeEenheidHR [0..1] (hoort bij)
Sollicitatiegesprek [0..*] ──── Werknemer [1..*] (doet sollicitatiegesprek)
Uren [1] ──── Dienstverband [0..*] (aantal volgens inzet)
Vacature [0..*] ──── Functie [1] (vacature bij functie)
Verlof [0..*] ──── Verlofsoort [1] (soort verlof)
Verzuim [0..*] ──── Verzuimsoort [1] (soort verzuim)
Werknemer [1] ──── Beoordeling [0..*] (Beoordeeld door)
Werknemer [1] ──── Beoordeling [0..*] (beoordeling van)
Werknemer [1] ──── Declaratie [0..*] (dient in)
Werknemer [1] ──── Dienstverband [1..*] (medewerker heeft dienstverband)
Werknemer [1] ──── Disciplinaire Maatregel [0..*] (heeft maatregel)
Werknemer [1] ──── GenotenOpleiding [0..*] (heeft genoten)
Werknemer [0..*] ──── Geweldsincident [1] (heeft ondergaan)
Werknemer [1] ──── Relatie [0..1] (is partner van)
Werknemer [1..*] ──── Rol [0..*] (heeft)
Werknemer [1] ──── Sollicitatie [0..*] (solliciteert)
Werknemer [1] ──── Verlof [0..*] (heeft verlof)
Werknemer [1] ──── Verzuim [0..*] (heeft verzuim)
```

### Sollicitaties

```
Sollicitant [1] ──── Sollicitatie [0..*] (solliciteert op functie)
Sollicitatie [0..*] ──── Vacature [1] (op vacature)
Sollicitatiegesprek [0..*] ──── Sollicitant [0..*] (kandidaat)
Sollicitatiegesprek [0..*] ──── Sollicitatie [1] (in kader van)
Sollicitatiegesprek [0..*] ──── Werknemer [1..*] (doet sollicitatiegesprek)
Vacature [0..*] ──── Functie [1] (vacature bij functie)
Werknemer [1] ──── Sollicitatie [0..*] (solliciteert)
```

### Overig

```
Uren [1] ──── Dienstverband [0..*] (aantal volgens inzet)
```

## Observaties

- Dit beleidsdomein bevat 31 entiteiten.
- Entiteiten zijn gegroepeerd in 3 diagramgroepen: Domain Objects (26), Sollicitaties (4), Overig (1).
- Er zijn 5 generalisatierelaties aanwezig.
