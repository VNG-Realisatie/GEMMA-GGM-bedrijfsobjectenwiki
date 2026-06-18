---
type: ggm-beleidsdomein
naam: Organisatie-indeling
definitie: "Het informatiedomein dat gegevens omvat over de structuur en indeling van een organisatie, inclusief de inrichting en uitvoering van programma’s en projecten."
taakveld: "9 Interne Organisatie"
aantal_entiteiten: 2
---

# GGM Beleidsdomein: Organisatie-indeling

Beleidsdomein binnen taakveld "9 Interne Organisatie" (zie ../structuur-ggm.md).

## Entiteiten

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Programma** | Een tijdelijke, flexibele organisatiestructuur, die is opgezet om de implementatie van een verzameling met elkaar samenhangende projecten en activiteiten te co√∂rdineren, te sturen en te controleren teneinde te zorgen voor de realisatie van de eindresultaten en benefits die zijn gerelateerd aan de strategische doelstellingen van de organisatie. | naam | Nee | GGM |
| **Project** | Geheel van activiteiten uitgevoerd in een tijdelijk samenwerkingsverband gericht op het binnen bepaalde randvoorwaarden (bv. tijd, geld) bereiken van een vooraf gedefinieerd resultaat. | *(geen attributen)* | Nee | GGM |

## Overervingshiërarchie

Geen overervingshiërarchie aanwezig in dit beleidsdomein.

## Relatiediagrammen

```
Programma [0..1] ──── Plan [0..*] (binnen programma)
Project [0..*] ──── Kostenplaats [0..*] (heeft)
```

## Observaties

- Dit beleidsdomein bevat 2 entiteiten.
