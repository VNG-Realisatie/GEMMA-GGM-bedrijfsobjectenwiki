---
type: ggm-beleidsdomein
naam: Generiek
taakveld: "99 Kern"
aantal_entiteiten: 9
---

# GGM Beleidsdomein: Generiek

Beleidsdomein binnen taakveld "99 Kern" (zie ../structuur-ggm.md).

## Entiteiten

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

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Foto** | Afbeelding op een plat vlak vervaardigd door middel van fotografie | bestandsnaam, bestandstype, datumtijd, bestandsgrootte, pixelsX, pixelsY, locatie | Nee | GGM |
| **Video-opname** | Opnametechniek om bewegende beelden als een elektronisch signaal te registreren en weer te geven. | datumtijd, lengte, videoformaat, bestandsgrootte | Nee | GGM |

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

### Generieke Locatie

```
Activiteit [0..*] ──── Locatie [1..*] (is verbonden met)
Gebiedengroep [0..1] ──── Gebied [1..*] (omvat)
Gebiedsaanwijzing [0..*] ──── Locatie [1..*] (verwijst naar)
Juridische Regel [0..*] ──── Locatie [1..*] (werkingsgebied)
Lijnengroep [0..1] ──── Lijn [0..*] (omvat)
Normwaarde [0..*] ──── Locatie [1..*] (geldt voor)
Projectlocatie [0..*] ──── Locatie [0..1] (betreft)
Puntengroep [0..1] ──── Punt [1..*] (omvat)
Regeltekst [0..*] ──── Locatie [0..*] (werkingsgebied)
Toepasbare Regel [0..*] ──── Locatie [0..*] (betreft)
Verzoek [0..*] ──── Locatie [1..*] (betreft)
```

### Overig

```
Beschermde Status [1] ──── Foto [0..*] (monument fotos)
Foto [0..*] ──── Erfgoed Object [0..*] (betreft)
VTH-Melding [0..1] ──── Foto [0..*] (heeft)
Vergadering [1] ──── Video-opname [0..*] (betreft)
Video-opname [0..1] ──── Agendapunt [0..*] (betreft)
Video-opname [0..*] ──── Erfgoed Object [0..*] (betreft)
```

## Observaties

- Dit beleidsdomein bevat 9 entiteiten.
- Entiteiten zijn gegroepeerd in 2 diagramgroepen: Generieke Locatie (7), Overig (2).
- Er zijn 6 generalisatierelaties aanwezig.
