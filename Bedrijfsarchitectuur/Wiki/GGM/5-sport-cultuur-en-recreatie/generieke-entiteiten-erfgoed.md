---
type: ggm-beleidsdomein
naam: Generieke Entiteiten Erfgoed
definitie: "Alle generieke objecttypen die gebruikt worden door de verschillende erfgoeddomeinen"
taakveld: "Erfgoed"
aantal_entiteiten: 3
---

# GGM Beleidsdomein: Generieke Entiteiten Erfgoed

### Generieke entiteiten Erfgoed

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Erfgoed Object** | Uit het verleden geërfde materiële en immateriële objecten | titel, omschrijving, dateringVanaf, dateringTot | Nee | GGM |
| **Historisch Persoon** | Natuurlijk persoon waarvan informatie beschikbaar is uit het verleden. | naam, datumGeboorte, datumOverlijden, omschrijving, woondeOp, beroep, publiekToegankelijk | Nee | GGM |
| **Objectclassificatie** | Systematische identificatie en ordening van objecten in categorieën overeenkomstig logisch gestructureerde conventies, methoden en procedureregels weergegeven in een classificatiesysteem. | naam, omschrijving | Nee | GGM |

## Overervingshiërarchie

```
NatuurlijkPersoon (abstract)
    └── Historisch Persoon 
```

## Relatiediagrammen

```
Erfgoed Object [0..*] ──── Objectclassificatie [0..*] (valt binnen)
Historisch Persoon  [0..*] ──── Erfgoed Object [0..*] (speelt rol in)
```

## Observaties

- Dit beleidsdomein bevat 3 Objecttype-entiteiten.
- Entiteiten zijn gegroepeerd in 2 diagramgroepen: Generieke entiteiten Erfgoed (3), Prinsenhof Collectie (1).
- Er zijn 1 generalisatierelaties aanwezig.
