---
type: ggm-beleidsdomein
naam: Dimensies
taakveld: "99 Kern"
aantal_entiteiten: 1
---

# GGM Beleidsdomein: Dimensies

Beleidsdomein binnen taakveld "99 Kern" (zie ../structuur-ggm.md).

## Entiteiten

### Dimensies Diagram

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Periode** | bepaalde tijdsduur. | datumStart, datumEinde, omschrijving | Nee | GGM |

## Overervingshiërarchie

Geen overervingshiërarchie aanwezig in dit beleidsdomein.

## Relatiediagrammen

### Dimensies Diagram

```
Archief [0..*] ──── Periode [1..*] (stamt uit)
Archiefstuk [0..*] ──── Periode [1..*] (stamt uit)
Begroting [0..*] ──── Periode [1..*] (valt binnen)
Hoofdstuk [0..*] ──── Periode [1..*] (binnen)
```

## Observaties

- Dit beleidsdomein bevat 1 entiteiten.
- Entiteiten zijn gegroepeerd in 1 diagramgroepen: Dimensies Diagram (1).
