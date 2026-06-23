---
type: ggm-beleidsdomein
naam: Financien
definitie: "Het informatiesubdomein dat gegevens omvat over de financiële processen, planning en control, en het financieel beheer van de organisatie."
taakveld: "9 Interne Organisatie"
aantal_entiteiten: 24
---

# GGM Beleidsdomein: Financien

### Diagram GGM en Inkomen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Kostenplaats** | Rekening waaraan boekingen in een financiële administratie samen worden toegeschreven. | naam, omschrijving, kostenplaatssoortCode, kostenplaatssoortOmschrijving, kostenplaatstypeCode, kostenplaatstypeOmschrijving, BTWCode, BTWOmschrijving | Nee | GGM |

### Diagram Inkoop Geen Inhuur

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Inkooporder** | Een opdracht (gezien vanuit de klant) voor één of meer leveringen door de leverancier aan die klant van een bepaalde hoeveelheid gespecificeerde goederen en/of diensten onder overeengekomen leveringsvoorwaarden en prijzen. | ordernummer, omschrijving, totaalNettoBedrag, datumStart, datumEinde, betreft, saldo, wijzeVanAanbesteden, betalingMeerdereJaren, datumIngediend, artikelcode, goederencode | Nee | GGM |

### Financien Begroting en Budgetverantwoordelijkheid

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Begroting** | Een overzicht van de verwachte ontvangsten en voorziene uitgaven voor een bepaalde (meestal toekomstige) periode zodat hier een afstemming tussen plaats kan vinden om eventuele tekorten en overschotten vroegtijdig in kaart te kunnen brengen. | naam, omschrijving, nummer | Nee | GGM |
| **Begrotingregel** | Een item op de begroting | bedrag, soortRegel, batenLasten | Nee | GGM |
| **Doelstelling** | Een op korte of middellange termijn nagestreefde situatie | naam, omschrijving, nummer | Nee | GGM |
| **Hoofdrekening** | is kostensoort | nummer, naam, omschrijving, subcode, subcodeOmschrijving, PIAHoofdcategorieCode, PIAHoofcategorieOmschrijving | Nee | GGM |
| **Hoofdstuk** | Onderdeel van een langere tekst. | naam, omschrijving, nummer | Nee | GGM |
| **Opdrachtgever** | Persoon die een opdracht verstrekt. | naam, omschrijving, nummer, clustercode, clusterOmschrijving | Nee | GGM |
| **Opdrachtnemer** | Partij die een opdracht aanvaardt. | naam, omschrijving, nummer, clustercode, clustercodeOmschrijving | Nee | GGM |
| **Product** | Het resultaat van een proces dat in het economisch verkeer een waarde bezit. | naam, omschrijving, nummer | Nee | GGM |
| **Taakveld** | Een samenhangend geheel van activiteiten en taken en hangt onder een programma. | hoofdfunctie, hoofdfunctieOmschrijving, functiecodeIV3, functieomschrijvingIV3, taakveldcode, taakveldOmschrijving, subtaakveldCode, subtaakveldOmschrijving | Nee | GGM |

### Financien Verplichtingen en Facturen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Activa** | Bezittingen van een onderneming op een boekhoudkundige balans | naam, omschrijving | Nee | GGM |
| **Activasoort** | Typering van activa | naam, omschrijving | Nee | GGM |
| **Factuur** | Schriftelijke rekening of nota voor de geleverde zaken of verrichte diensten. | datumFactuur, omschrijving, code, betaaltermijn, betaalbaarPer, factuurbedragExclusiefBTW, factuurbedragBTW | Nee | GGM |

### Financien Verwerken Mutaties

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Bankafschrift** | Overzicht van de bij- en afschrijvingen van een rekening | nummer, datum | Nee | GGM |
| **Bankafschriftregel** | Een item op het bankafschrift | bedrag, bij, datum, rekeningVan | Nee | GGM |
| **Bankrekening** | Een rekening-courant bij een bank | nummer, bank, tennaamstelling | Nee | GGM |
| **Batch** | Verzameling van posten die in het kader van automatische verwerking een logisch geheel vormen. | datum, tijd, nummer | Nee | GGM |
| **Batchregel** | Een item uit een batch | bedrag, omschrijving, datumBetaling, rekeningVan, rekeningNaar | Nee | GGM |
| **Factuurregel** | Een item op de factuur | nummer, omschrijving, aantal, bedragExBTW, bedragBTW, BTWPercentage | Nee | GGM |
| **Mutatie** | Wijziging van een situatie | datum, bedrag | Nee | GGM |
| **Subrekening** | Ondergeschikte rekening van een hoofdrekening | naam, omschrijving, nummer | Nee | GGM |
| **Werkorder** | Opdracht voor de uitvoering van een activiteit of een stap in een proces. | naam, omschrijving, code, werkordertype, documentnummer | Nee | GGM |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Debiteur** | Iemand aan wie een dienst of product geleverd is waardoor recht op een vergoeding is ontstaan | *(geen attributen)* | Nee | GGM |

## Overervingshiërarchie

```
Rechtspersoon (abstract)
    └── Debiteur
```

## Relatiediagrammen

```
Activa [0..*] ──── Activasoort [1..1] (is soort)
Bankafschrift [1..1] ──── Bankafschriftregel [0..*] (heeft)
Bankafschriftregel [0..1] ──── Mutatie [0..1] (leidt tot)
Bankrekening [1..1] ──── Bankafschrift [0..*] (heeft)
Batch [1..1] ──── Batchregel [0..*] (heeft)
Batchregel [0..1] ──── Mutatie [0..1] (leidt tot)
Begroting [1..1] ──── Begrotingregel [0..*] (heeft)
Begrotingregel [0..*] ──── Doelstelling [0..1] (betreft)
Begrotingregel [0..*] ──── Hoofdrekening [0..1] (betreft)
Begrotingregel [0..*] ──── Hoofdstuk [1..1] (betreft)
Begrotingregel [0..*] ──── Kostenplaats [0..1] (betreft)
Begrotingregel [0..*] ──── Product [0..1] (betreft)
Debiteur [1..1] ──── Factuur [0..*] (heeft)
Doelstelling [1..*] ──── Opdrachtgever [1..1] (is opdrachtgever)
Doelstelling [1..1] ──── Product [0..*] (heeft)
Factuur [1..1] ──── Factuurregel [1..*] (heeft)
Factuur [0..*] ──── Inkooporder [0..1] (gedekt via)
Factuur [0..*] ──── Kostenplaats [0..1] (schrijft op)
Factuurregel [0..1] ──── Mutatie [0..1] (leidt tot)
Hoofdrekening [0..*] ──── Activa [0..*] (heeft)
Hoofdrekening [1..1] ──── Hoofdrekening [0..*] (valt binnen)
Hoofdrekening [1..*] ──── Kostenplaats [0..*] (heeft)
Hoofdrekening [1..1] ──── Subrekening [0..*] (heeft)
Hoofdrekening [1..1] ──── Werkorder [0..*] (heeft)
Hoofdstuk [1..1] ──── Doelstelling [0..*] (heeft)
Inkooporder [0..*] ──── Hoofdrekening [1..*] (wordt geschreven op)
Inkooporder [0..1] ──── Inkooporder [0..*] (gerelateerd)
Inkooporder [0..1] ──── Inkooporder [0..1] (oorspronkelijk)
Kostenplaats [0..*] ──── Inkooporder [0..*] (heeft)
Kostenplaats [1..*] ──── Opdrachtnemer [1..1] (is budgetverantwoordelijk)
Kostenplaats [1..1] ──── Subrekening [0..*] (heeft)
Kostenplaats [1..*] ──── Taakveld [1..*] (heeft)
Kostenplaats [1..1] ──── Werkorder [0..*] (heeft)
Mutatie [0..*] ──── Hoofdrekening [1..1] (van)
Mutatie [0..*] ──── Kostenplaats [1..1] (heeft betrekking op)
Opdrachtgever [0..1] ──── Product [0..*] (is opdrachtgever)
Opdrachtnemer [0..1] ──── Product [0..*] (is opdrachtnemer)
Product [0..*] ──── Kostenplaats [1..1] (heeft)
```

## Observaties

- Dit beleidsdomein bevat 24 Objecttype-entiteiten.
- Entiteiten zijn gegroepeerd in 13 diagramgroepen: Diagram GGM en Inkomen (1), Diagram Inkoop Geen Inhuur (2), Diagram Inkoop Inhuur (2), Diagram Verlengen Inhuur (2), Financien Begroting en Budgetverantwoordelijkheid (10), Financien Personen (2), Financien Verplichtingen en Facturen (6), Financien Verwerken Mutaties (12), Prinsenhof Events en Relaties (1), Subsidie en Kostenplaats (2), Subsidies (1), Vastgoed Domeinmodel  (3), Verplichtingen (3).
- Er zijn 1 generalisatierelaties aanwezig.
