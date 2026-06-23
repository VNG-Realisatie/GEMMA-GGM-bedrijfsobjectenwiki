---
type: ggm-beleidsdomein
naam: Archief
definitie: "Het informatiedomein dat gegevens omvat over de vorming, het beheer, de toegankelijkheid en de duurzame bewaring van archieven, inclusief documenten en collecties van cultuurhistorische waarde."
taakveld: "Erfgoed"
aantal_entiteiten: 18
---

# GGM Beleidsdomein: Archief

### Archief Aanvragen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Aanvraag** | (officieel) verzoek, iets (officieel) vragen aan een bevoegde macht. | datumtijd | Nee | GGM |
| **Archiefstuk** | Bijeengebrachte informatie, ongeacht het medium, die wordt gecreëerd, ontvangen en gearchiveerd door een bureau, een instelling, een organisatie of een individu met het oog op het nakomen van wettelijke verplichtingen of het uitvoeren van zakelijke transacties.(AAT) | trefwoorden, openbaarheidsbeperking, inventarisnummer, omvang, beschrijving, uiterlijkeVorm | Nee | GGM |
| **Bezoeker** | Een persoon die iemand of iets bezoekt. | *(geen attributen)* | Nee | GGM |

### Archief Model

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Depot** | Plaats waar iets bewaard wordt. | naam, omschrijving | Nee | GGM |
| **DigitaalBestand** | Bestand dat uitsluitend met behulp van besturingsprogrammatuur of toepassingsprogrammatuur geraadpleegd kunnen worden | naam, omschrijving, mimetype, blob | Nee | GGM |
| **Kast** | Object met een permanent karakter dat dient om iets in te bergen en te beschermen. | kastnummer | Nee | GGM |
| **Plank** | Deel, plaat; stuk hout breder dan het dik is en langer dan breed. | planknummer | Nee | GGM |
| **Stelling** | Een systeem om goederen op te slaan die worden vervoerd en opgeslagen op pallets, in bundels of per stuk.(Wikipedia) | stellingnummer | Nee | GGM |
| **Uitgever** | Iemand die iets op de markt brengt; iemand die iets uitgeeft | *(geen attributen)* | Nee | GGM |
| **Vindplaats** | Een plek waar men iets gevonden heeft. | *(geen attributen)* | Nee | GGM |

### Archief Model Indeling

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Archief** | De bewaarplaats van belangrijke gegevens die zijn vastgelegd in documentvorm alsook de verzameling van documenten die voor een bepaald doel vervaardigd zijn. | naam, omschrijving, openbaarheidsbeperking, archiefnummer | Nee | GGM |
| **Archiefcategorie** | Typologie van een archief conform landelijke indeling | naam, omschrijving, nummer | Nee | GGM |
| **Indeling** | Onderwerpen groeperen in samenhangende categorieën. | naam, nummer, omschrijving, indelingsoort | Nee | GGM |
| **Index** | *(geen definitie in GGM)* | indexnaam, indexwaarde | Nee | GGM |
| **Nadere Toegang** | De bevoegdheid om gegevens te raadplegen, bepaalde plaatsen te betreden of een bepaalde taak uit te oefenen. | *(geen attributen)* | Nee | GGM |
| **Ordeningsschema** | Ordening om archief en collecties beter vindbaar en bruikbaar voor betrokkenen. | naam, text | Nee | GGM |
| **Rechthebbende** | Een rechthebbende is iemand die rechten heeft op een goed. | *(geen attributen)* | Nee | GGM |

### Generieke entiteiten Erfgoed

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Auteur** | De persoon die verantwoordelijk is voor de inhoud van een (digitaal) document | datumGeboorte, datumOverlijden | Nee | GGM |

## Overervingshiërarchie

```
Document (abstract)
    └── Archiefstuk
```

```
Erfgoed Object (abstract)
    └── Archiefstuk
```

```
Historisch Persoon  (abstract)
    └── Auteur
```

```
NatuurlijkPersoon (abstract)
    └── Bezoeker
```

```
Rechtspersoon (abstract)
    └── Rechthebbende
    └── Uitgever
```

## Relatiediagrammen

```
Aanvraag [0..*] ──── Archiefstuk [0..*]
Archief [0..*] ──── Archiefcategorie [0..*]
Archief [0..*] ──── Rechthebbende [0..1]
Archiefstuk [0..*] ──── Archief [1..1]
Archiefstuk [1..1] ──── DigitaalBestand [0..*]
Archiefstuk [1..1] ──── Nadere Toegang [0..1]
Archiefstuk [0..*] ──── Ordeningsschema [0..*]
Archiefstuk [0..*] ──── Uitgever [0..1]
Archiefstuk [0..*] ──── Vindplaats [1..1]
Bezoeker [1..1] ──── Aanvraag [0..*]
Depot [1..1] ──── Stelling [0..*]
Indeling [0..*] ──── Archief [1..1]
Indeling [0..1] ──── Archiefstuk [0..*]
Indeling [1..1] ──── Indeling [0..*]
Kast [0..1] ──── Plank [0..*]
Nadere Toegang [1..1] ──── Index [1..*]
Stelling [1..1] ──── Kast [0..*]
Vindplaats [0..*] ──── Depot [1..1]
Vindplaats [0..*] ──── Kast [1..1]
Vindplaats [0..*] ──── Plank [1..1]
Vindplaats [0..*] ──── Stelling [0..1]
```

## Observaties

- Dit beleidsdomein bevat 18 Objecttype-entiteiten.
- Entiteiten zijn gegroepeerd in 5 diagramgroepen: Archief Aanvragen (3), Archief Model (8), Archief Model Indeling (8), Archief Relaties met Kern (3), Generieke entiteiten Erfgoed (2).
- Er zijn 6 generalisatierelaties aanwezig.
