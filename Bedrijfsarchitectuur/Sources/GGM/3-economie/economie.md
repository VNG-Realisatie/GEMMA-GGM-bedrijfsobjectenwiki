---
type: ggm-beleidsdomein
naam: Model Economie
definitie: "Het informatiedomein dat gegevens omvat over economische ontwikkeling, bedrijvigheid en innovatie."
taakveld: "3 Economie"
aantal_entiteiten: 6
---

# GGM Beleidsdomein: Model Economie

Beleidsdomein binnen taakveld "3 Economie" (zie ../structuur-ggm.md).

## Entiteiten

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Contact** | Persoon waarmee communicatie plaatsvindt | contactsoort, datum, tekst | Nee | GGM |
| **Hotel** | Gebouw waar je tegen betaling kunt logeren. | aantalKamers | Nee | GGM |
| **Hotelbezoek** | Verblijf in een hotel | datumStart, datumEinde | Nee | GGM |
| **Verkooppunt** | Locatie waar iets wordt verkocht | winkelformule | Nee | GGM |
| **Werkgelegenheid** | De vraag naar arbeid, te berekenen door de totale productie te delen door de arbeidsproductiviteit per persoon. | aantalFulltimeMannen, aantalFulltimeVrouwen, aantalParttimeVrouwen, aantalParttimeMannen, grootteklasse | Nee | GGM |
| **Winkelvloeroppervlak** | Gemeten oppervlakte in vierkante meters van een winkel | winkelvloeroppervlakte, WVOKlasse, bronWVO, leegstand, aantalKassa | Nee | GGM |

## Overervingshiërarchie

```
Vestiging (abstract)
    └── Hotel
    └── Verkooppunt
```

## Relatiediagrammen

```
AdresseerbaarObject [1] ──── Winkelvloeroppervlak [0..1] (heeft)
Contact [0..*] ──── NatuurlijkPersoon [0..*] (met)
Contact [0..*] ──── Vestiging [0..1] (bij)
GebouwdObject [1] ──── Winkelvloeroppervlak [0..1] (heeft)
Hotel [1] ──── Hotelbezoek [0..*] (heeft)
Vestiging [1] ──── Werkgelegenheid [0..1] (heeft)
```

## Observaties

- Dit beleidsdomein bevat 6 entiteiten.
- Er zijn 2 generalisatierelaties aanwezig.
