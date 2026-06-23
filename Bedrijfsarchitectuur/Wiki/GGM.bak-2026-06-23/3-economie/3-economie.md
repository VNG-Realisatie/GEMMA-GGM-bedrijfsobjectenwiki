---
type: ggm-beleidsdomein
naam: 3 Economie
definitie: "Het informatiedomein dat gegevens omvat over economische ontwikkeling, bedrijvigheid en innovatie."
taakveld: "3 Economie"
aantal_entiteiten: 6
---

# GGM Beleidsdomein: 3 Economie

### Diagram Economie

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Contact** | Persoon waarmee communicatie plaatsvindt | contactsoort, datum, tekst | Nee | GGM |
| **Hotel** | Gebouw waar je tegen betaling kunt logeren. | aantalKamers | Nee | GGM |
| **Hotelbezoek** | Verblijf in een hotel | datumStart, datumEinde | Nee | GGM |
| **Verkooppunt** | Locatie waar iets wordt verkocht | winkelformule | Nee | GGM |
| **Werkgelegenheid** | De vraag naar arbeid, te berekenen door de totale productie te delen door de arbeidsproductiviteit per persoon. | aantalFulltimeMannen, aantalFulltimeVrouwen, aantalParttimeVrouwen, aantalParttimeMannen, grootteklasse | Nee | GGM |

### Diagram Gebied Vestiging en Adres

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Winkelvloeroppervlak** | Gemeten oppervlakte in vierkante meters van een winkel | winkelvloeroppervlakte, WVOKlasse, bronWVO, leegstand, aantalKassa | Nee | GGM |

## Overervingshiërarchie

```
Vestiging (abstract)
    └── Hotel
    └── Verkooppunt
```

## Relatiediagrammen

```
Hotel ──── Hotelbezoek
```

## Observaties

- Dit beleidsdomein bevat 6 Objecttype-entiteiten (+ 2 diagramhulpobjecten zonder stereotype).
- Entiteiten zijn gegroepeerd in 2 diagramgroepen: Diagram Economie (5), Diagram Gebied Vestiging en Adres (1).
- Er zijn 2 generalisatierelaties aanwezig.
