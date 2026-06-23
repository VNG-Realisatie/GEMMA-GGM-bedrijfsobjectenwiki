---
type: ggm-beleidsdomein
naam: Bouwen en Wonen
definitie: "Het informatiedomein dat gegevens omvat over de planning, ontwikkeling en uitvoering van woningbouwprojecten, gericht op het realiseren van voldoende, betaalbare en duurzame woningen."
taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
aantal_entiteiten: 7
---

# GGM Beleidsdomein: Bouwen en Wonen

Beleidsdomein binnen taakveld "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing" (zie ../structuur-ggm.md).

## Entiteiten

### Woningbouwprojecten

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Gebouw** | Een complex van ruimten uitsluitend bedoeld voor de huisvesting van een afzonderlijk huishouden | aantal, aantalAdressen, aantalKamers, energielabel, oppervlakte, duurzaam, natuurinclusief, regenwater, aardgasloos | Nee | GGM |
| **Huurwoningen** | Wen woning die de bewoner huurt van de eigenaar, veelal een woningcorporatie of een particulier. | huurprijs | Nee | GGM |
| **Koopwoningen** | Een woning die eigendom is van een particulier (in het algemeen de bewoner van de woning). | koopprijs | Nee | GGM |
| **Plan** | Project waarin woningen worden gerealiseerd | naam, nummer, aardgasloos, gebiedstransformatie, intentie, bestemmingGoedgekeurd, onherroepelijk, eigendomGemeente, 70ProcentVerkocht, startVerkoop, startbouw, eersteOplevering, laatsteOplevering, percelen | Nee | GGM |
| **Projectleider** | De persoon die een project aanstuurt | naam | Nee | GGM |
| **Projectontwikkelaar** | Een persoon of een firma die een project ontwikkelt voor financieel gewin. | naam, adres | Nee | GGM |
| **Studentenwoningen** | Een woning waar uitsluitend (meerdere) studenten (of soms ook werkende jongeren) een woongemeenschap vorme | zelfstandig, huurprijs | Nee | GGM |

## Overervingshiërarchie

```
Gebouw (abstract)
    └── Huurwoningen
    └── Koopwoningen
    └── Studentenwoningen
```

```
NatuurlijkPersoon (abstract)
    └── Projectleider
```

```
NietNatuurlijkPersoon (abstract)
    └── Projectontwikkelaar
```

## Relatiediagrammen

### Woningbouwprojecten

```
Omgevingsvergunning [0..*] ──── Plan [0..1] (betrekking op)
Plan [1] ──── Gebouw [1..*] (Bestaat uit)
Programma [0..1] ──── Plan [0..*] (binnen programma)
Projectleider [0..1] ──── Plan [0..*] (is projectleider van)
Projectontwikkelaar [1..*] ──── Plan [0..*] (heeft)
```

## Observaties

- Dit beleidsdomein bevat 7 entiteiten.
- Entiteiten zijn gegroepeerd in 1 diagramgroepen: Woningbouwprojecten (7).
- Er zijn 5 generalisatierelaties aanwezig.
