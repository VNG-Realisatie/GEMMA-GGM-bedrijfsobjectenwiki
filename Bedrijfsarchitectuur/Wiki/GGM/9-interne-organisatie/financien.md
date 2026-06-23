---
type: ggm-beleidsdomein
naam: Financien
definitie: "Het informatiesubdomein dat gegevens omvat over de financiële processen, planning en control, en het financieel beheer van de organisatie."
taakveld: "9 Interne Organisatie"
aantal_entiteiten: 24
---

# GGM Beleidsdomein: Financien

Beleidsdomein binnen taakveld "9 Interne Organisatie" (zie ../structuur-ggm.md).

## Entiteiten

### Financien Verwerken Mutaties

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Bankafschrift** | Overzicht van de bij- en afschrijvingen van een rekening | nummer, datum | Nee | GGM |
| **Bankafschriftregel** | Een item op het bankafschrift | bedrag, bij, datum, rekeningVan | Nee | GGM |
| **Bankrekening** | Een rekening-courant bij een bank | nummer, bank, tennaamstelling | Nee | GGM |
| **Batch** | Verzameling van posten die in het kader van automatische verwerking een logisch geheel vormen. | datum, tijd, nummer | Nee | GGM |
| **Batchregel** | Een item uit een batch | bedrag, omschrijving, datumBetaling, rekeningVan, rekeningNaar | Nee | GGM |
| **Factuur** | Schriftelijke rekening of nota voor de geleverde zaken of verrichte diensten. | datumFactuur, omschrijving, code, betaaltermijn, betaalbaarPer, factuurbedragExclusiefBTW, factuurbedragBTW | Nee | GGM |
| **Factuurregel** | Een item op de factuur | nummer, omschrijving, aantal, bedragExBTW, bedragBTW, BTWPercentage | Nee | GGM |
| **Hoofdrekening** | is kostensoort | nummer, naam, omschrijving, subcode, subcodeOmschrijving, PIAHoofdcategorieCode, PIAHoofcategorieOmschrijving | Nee | GGM |
| **Kostenplaats** | Rekening waaraan boekingen in een financiële administratie samen worden toegeschreven. | naam, omschrijving, kostenplaatssoortCode, kostenplaatssoortOmschrijving, kostenplaatstypeCode, kostenplaatstypeOmschrijving, BTWCode, BTWOmschrijving | Nee | GGM |
| **Mutatie** | Wijziging van een situatie | datum, bedrag | Nee | GGM |
| **Subrekening** | Ondergeschikte rekening van een hoofdrekening | naam, omschrijving, nummer | Nee | GGM |
| **Werkorder** | Opdracht voor de uitvoering van een activiteit of een stap in een proces. | naam, omschrijving, code, werkordertype, documentnummer | Nee | GGM |

### Financien Personen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Opdrachtgever** | Persoon die een opdracht verstrekt. | naam, omschrijving, nummer, clustercode, clusterOmschrijving | Nee | GGM |
| **Opdrachtnemer** | Partij die een opdracht aanvaardt. | naam, omschrijving, nummer, clustercode, clustercodeOmschrijving | Nee | GGM |

### Financien Verplichtingen en Facturen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Activa** | Bezittingen van een onderneming op een boekhoudkundige balans | naam, omschrijving | Nee | GGM |
| **Activasoort** | Typering van activa | naam, omschrijving | Nee | GGM |
| **Inkooporder** | Een opdracht (gezien vanuit de klant) voor één of meer leveringen door de leverancier aan die klant van een bepaalde hoeveelheid gespecificeerde goederen en/of diensten onder overeengekomen leveringsvoorwaarden en prijzen. | ordernummer, omschrijving, totaalNettoBedrag, datumStart, datumEinde, betreft, saldo, wijzeVanAanbesteden, betalingMeerdereJaren, datumIngediend, artikelcode, goederencode | Nee | GGM |

### Financien Begroting en Budgetverantwoordelijkheid

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Begroting** | Een overzicht van de verwachte ontvangsten en voorziene uitgaven voor een bepaalde (meestal toekomstige) periode zodat hier een afstemming tussen plaats kan vinden om eventuele tekorten en overschotten vroegtijdig in kaart te kunnen brengen. | naam, omschrijving, nummer | Nee | GGM |
| **Begrotingregel** | Een item op de begroting | bedrag, soortRegel, batenLasten | Nee | GGM |
| **Doelstelling** | Een op korte of middellange termijn nagestreefde situatie | naam, omschrijving, nummer | Nee | GGM |
| **Hoofdstuk** | Onderdeel van een langere tekst. | naam, omschrijving, nummer | Nee | GGM |
| **Product** | Het resultaat van een proces dat in het economisch verkeer een waarde bezit. | naam, omschrijving, nummer | Nee | GGM |
| **Taakveld** | Een samenhangend geheel van activiteiten en taken en hangt onder een programma. | hoofdfunctie, hoofdfunctieOmschrijving, functiecodeIV3, functieomschrijvingIV3, taakveldcode, taakveldOmschrijving, subtaakveldCode, subtaakveldOmschrijving | Nee | GGM |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Debiteur** | Iemand aan wie een dienst of product geleverd is waardoor recht op een vergoeding is ontstaan | *(geen attributen)* | Nee | GGM |

## Overervingshiërarchie

```
Inkooporder (abstract)
    └── Verplichting Wmo Jeugd
```

```
Rechtspersoon (abstract)
    └── Debiteur
```

## Relatiediagrammen

### Financien Verwerken Mutaties

```
Applicatie [1] ──── Batch [0..*] (heeft herkomst)
Bankafschrift [1] ──── Bankafschriftregel [0..*] (heeft)
Bankafschriftregel [0..1] ──── Mutatie [0..1] (leidt tot)
Bankrekening [1] ──── Bankafschrift [0..*] (heeft)
Bankrekening [1] ──── Betaling [0..*] (van)
Bankrekening [1] ──── Betaling [0..*] (naar)
Batch [1] ──── Batchregel [0..*] (heeft)
Batch [0..*] ──── ExterneBron [1] (heeft herkomst)
Batchregel [0..1] ──── Mutatie [0..1] (leidt tot)
Begrotingregel [0..*] ──── Hoofdrekening [0..1] (betreft)
Begrotingregel [0..*] ──── Kostenplaats [0..1] (betreft)
Betaling [0..*] ──── Bankafschriftregel [0..1] (komt voor op)
Debiteur [1] ──── Factuur [0..*] (heeft)
Factuur [1] ──── Factuurregel [1..*] (heeft)
Factuur [0..*] ──── Inkooporder [0..1] (gedekt via)
Factuur [0..*] ──── Kostenplaats [0..1] (schrijft op)
Factuur [0..*] ──── Leverancier [1] (crediteur)
Factuurregel [0..1] ──── Mutatie [0..1] (leidt tot)
FormulierInhuur [0..*] ──── Kostenplaats [1] (heeft)
Hoofdrekening [0..*] ──── Activa [0..*] (heeft)
Hoofdrekening [1] ──── Hoofdrekening [0..*] (valt binnen)
Hoofdrekening [1..*] ──── Kostenplaats [0..*] (heeft)
Hoofdrekening [1] ──── Subrekening [0..*] (heeft)
Hoofdrekening [1] ──── Werkorder [0..*] (heeft)
Inkooporder [0..*] ──── Hoofdrekening [1..*] (wordt geschreven op)
Kostenplaats [0..*] ──── Inkooporder [0..*] (heeft)
Kostenplaats [1..*] ──── Opdrachtnemer [1] (is budgetverantwoordelijk)
Kostenplaats [1] ──── Subrekening [0..*] (heeft)
Kostenplaats [1..*] ──── Taakveld [1..*] (heeft)
Kostenplaats [1] ──── Vastgoedobject [0..*] (heeft)
Kostenplaats [1] ──── Werkorder [0..*] (heeft)
Leveringscomponent [0..*] ──── Kostenplaats [0..1] (heeft)
Mutatie [0..*] ──── Hoofdrekening [1] (van)
Mutatie [0..*] ──── Hoofdrekening [1] (naar)
Mutatie [0..*] ──── Kostenplaats [1] (heeft betrekking op)
OrganisatorischeEenheid [0..1] ──── Kostenplaats [1] (heeft)
Product [0..*] ──── Kostenplaats [1] (heeft)
Programma [0..*] ──── Kostenplaats [1] (heeft)
Project [0..*] ──── Kostenplaats [0..*] (heeft)
Subsidie [0..*] ──── Kostenplaats [0..1] (heeft)
Subsidiecomponent [0..*] ──── Kostenplaats [1] (heeft)
Zakelijk Recht [0..*] ──── Kostenplaats [1] (heeft)
```

### Financien Personen

```
Doelstelling [1..*] ──── Opdrachtgever [1] (is opdrachtgever)
Kostenplaats [1..*] ──── Opdrachtnemer [1] (is budgetverantwoordelijk)
Opdrachtgever [0..*] ──── Functie [1] (uitgevoerd door)
Opdrachtgever [0..1] ──── Product [0..*] (is opdrachtgever)
Opdrachtnemer [0..*] ──── Functie [1] (uitgevoerd door)
Opdrachtnemer [0..1] ──── Product [0..*] (is opdrachtnemer)
```

### Financien Verplichtingen en Facturen

```
Aanvraag Inkooporder [0..*] ──── Inkooporder [0..1] (mondt uit in )
Activa [0..*] ──── Activasoort [1] (is soort)
Factuur [0..*] ──── Inkooporder [0..1] (gedekt via)
FormulierVerlengingInhuur [0..*] ──── Inkooporder [1] (betreft)
Hoofdrekening [0..*] ──── Activa [0..*] (heeft)
Inkooporder [0..1] ──── Contract [1] (betreft)
Inkooporder [0..*] ──── Hoofdrekening [1..*] (wordt geschreven op)
Inkooporder [0..1] ──── Inkooporder [0..*] (gerelateerd)
Inkooporder [0..1] ──── Inkooporder [0..1] (oorspronkelijk)
Inkooporder [0..*] ──── Inkooppakket [1] (heeft)
Inkooporder [0..*] ──── Leverancier [1] (verplichting aan)
Inkooporder [1] ──── Werkbon [0..*] (hoort bij)
Kostenplaats [0..*] ──── Inkooporder [0..*] (heeft)
```

### Financien Begroting en Budgetverantwoordelijkheid

```
Begroting [1] ──── Begrotingregel [0..*] (heeft)
Begroting [0..*] ──── Periode [1..*] (valt binnen)
Begrotingregel [0..*] ──── Doelstelling [0..1] (betreft)
Begrotingregel [0..*] ──── Hoofdrekening [0..1] (betreft)
Begrotingregel [0..*] ──── Hoofdstuk [1] (betreft)
Begrotingregel [0..*] ──── Kostenplaats [0..1] (betreft)
Begrotingregel [0..*] ──── Product [0..1] (betreft)
Doelstelling [1..*] ──── Opdrachtgever [1] (is opdrachtgever)
Doelstelling [1] ──── Product [0..*] (heeft)
Hoofdstuk [1] ──── Doelstelling [0..*] (heeft)
Hoofdstuk [0..*] ──── Periode [1..*] (binnen)
Kostenplaats [1..*] ──── Taakveld [1..*] (heeft)
Opdrachtgever [0..1] ──── Product [0..*] (is opdrachtgever)
Opdrachtnemer [0..1] ──── Product [0..*] (is opdrachtnemer)
Product [0..*] ──── Kostenplaats [1] (heeft)
```

### Overig

```
Debiteur [1] ──── Factuur [0..*] (heeft)
```

## Observaties

- Dit beleidsdomein bevat 24 entiteiten.
- Entiteiten zijn gegroepeerd in 5 diagramgroepen: Financien Verwerken Mutaties (12), Financien Personen (2), Financien Verplichtingen en Facturen (3), Financien Begroting en Budgetverantwoordelijkheid (6), Overig (1).
- Er zijn 2 generalisatierelaties aanwezig.
