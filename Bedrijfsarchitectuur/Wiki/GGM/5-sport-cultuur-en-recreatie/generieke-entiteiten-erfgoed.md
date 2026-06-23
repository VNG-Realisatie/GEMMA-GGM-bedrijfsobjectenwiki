---
type: ggm-beleidsdomein
naam: Generieke Entiteiten Erfgoed
definitie: "Alle generieke objecttypen die gebruikt worden door de verschillende erfgoeddomeinen"
taakveld: "5 Sport, Cultuur en Recreatie"
aantal_entiteiten: 3
---

# GGM Beleidsdomein: Generieke Entiteiten Erfgoed

Onderdeel van beleidsdomein **Erfgoed** binnen taakveld "5 Sport, Cultuur en Recreatie" (zie ../structuur-ggm.md).

## Entiteiten

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Erfgoed Object** | Uit het verleden geërfde materiële en immateriële objecten | titel, omschrijving, dateringVanaf, dateringTot | Nee | GGM |
| **Historisch Persoon ** | Natuurlijk persoon waarvan informatie beschikbaar is uit het verleden. | naam, datumGeboorte, datumOverlijden, omschrijving, woondeOp, beroep, publiekToegankelijk | Nee | GGM |
| **Objectclassificatie** | Systematische identificatie en ordening van objecten in categorieën overeenkomstig logisch gestructureerde conventies, methoden en procedureregels weergegeven in een classificatiesysteem. | naam, omschrijving | Nee | GGM |

## Overervingshiërarchie

```
Erfgoed Object (abstract)
    └── Archiefstuk
    └── Museumobject
```

```
Historisch Persoon  (abstract)
    └── Auteur
```

```
NatuurlijkPersoon (abstract)
    └── Historisch Persoon 
```

## Relatiediagrammen

```
Erfgoed Object [0..*] ──── Objectclassificatie [0..*] (valt binnen)
Foto [0..*] ──── Erfgoed Object [0..*] (betreft)
Historisch Persoon  [0..*] ──── Erfgoed Object [0..*] (speelt rol in)
Museumobject [0..*] ──── Historisch Persoon  [0..*] (heeft verbinding)
Tentoonstelling [0..*] ──── Historisch Persoon  [0..*] (is gewijd aan)
Video-opname [0..*] ──── Erfgoed Object [0..*] (betreft)
```

## Observaties

- Dit beleidsdomein bevat 3 entiteiten.
- Er zijn 4 generalisatierelaties aanwezig.
