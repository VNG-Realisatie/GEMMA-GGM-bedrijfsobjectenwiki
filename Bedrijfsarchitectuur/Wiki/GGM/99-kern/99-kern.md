---
type: ggm-beleidsdomein
naam: 99 Kern
definitie: "Het informatiedomein dat de fundamentele gegevensstructuren en -definities bevat, gebaseerd op de Nederlandse basisregistraties, en dat dient als fundament voor alle overige informatiedomeinen."
taakveld: "99 Kern"
aantal_entiteiten: 10
---

# GGM Beleidsdomein: 99 Kern

### Archief Model Indeling

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Periode** | bepaalde tijdsduur. | datumStart, datumEinde, omschrijving | Nee | GGM |

### Brede Handhaving

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Foto** | Afbeelding op een plat vlak vervaardigd door middel van fotografie | bestandsnaam, bestandstype, datumtijd, bestandsgrootte, pixelsX, pixelsY, locatie | Nee | GGM |

### Diagram Griffie

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Video-opname** | Opnametechniek om bewegende beelden als een elektronisch signaal te registreren en weer te geven. | datumtijd, lengte, videoformaat, bestandsgrootte | Nee | GGM |

### Generieke Locatie

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Gebied** | Een aaneengesloten gedeelte van een wijk, waarvan de grenzen zo veel mogelijk gebaseerd zijn op topografische elementen. | gebiedsAanduiding | Nee | GGM |
| **Gebiedengroep** | Verzameling van gebieden | *(geen attributen)* | Nee | GGM |
| **Lijn** | Denkbeeldige streep op de aardoppervlakte | lijnLocatie | Nee | GGM |
| **Lijnengroep** | Verzameling van lijnen | *(geen attributen)* | Nee | GGM |
| **Locatie** | De locatie beschrijft middels co√∂rdinaten de ruimtelijke dimensie of ruimtelijke afbakening van een regel of van een objecttype die in de regel beschreven wordt. (CIMOW) | naam, hoogte, NEN3610ID | Nee | GGM |
| **Punt** | Plaats in de ruimte | puntLocatie | Nee | GGM |
| **Puntengroep** | Verzameling van punten | *(geen attributen)* | Nee | GGM |

## Overervingshiërarchie

```
Locatie (abstract)
    └── Gebied
    └── Gebiedengroep
    └── Lijn
    └── Lijnengroep
    └── Punt
    └── Puntengroep
```

## Relatiediagrammen

```
Gebiedengroep [0..1] ──── Gebied [1..*] (omvat)
Lijnengroep [0..1] ──── Lijn [0..*] (omvat)
Puntengroep [0..1] ──── Punt [1..*] (omvat)
```

## Observaties

- Dit beleidsdomein bevat 10 Objecttype-entiteiten.
- Entiteiten zijn gegroepeerd in 13 diagramgroepen: Archief Model Indeling (1), Brede Handhaving (1), Diagram Griffie (1), Diagram Monumenten Detail (1), Dimensies Diagram (1), Financien Begroting en Budgetverantwoordelijkheid (1), Generieke Locatie (7), Generieke entiteiten Erfgoed (2), Omgevingswet Juridische Regels (CIMOW) (1), Omgevingswet Omgevingsplan StOP TPOD (1), Omgevingswet Toepasbare Regels (1), Omgevingswet Verzoek Activiteit op Locatie (1), Omgevingswet Verzoeken (IMAM) (1).
- Er zijn 6 generalisatierelaties aanwezig.
