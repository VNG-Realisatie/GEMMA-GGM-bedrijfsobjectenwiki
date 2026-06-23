---
type: ggm-beleidsdomein
naam: Gemeentebegrafenissen
definitie: "Het informatiedomein dat gegevens omvat over gemeentelijke uitvaarten, uitgevoerd wanneer niemand anders in de lijkbezorging voorziet, zoals vastgelegd in de Wet op de lijkbezorging."
taakveld: "6 Sociaal Domein"
aantal_entiteiten: 1
---

# GGM Beleidsdomein: Gemeentebegrafenissen

Beleidsdomein binnen taakveld "6 Sociaal Domein" (zie ../structuur-ggm.md).

## Entiteiten

### Gemeente Begrafenissen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Gemeentebegrafenis** | Teraardebestelling onder verantwoordelijjkheid van de gemeente. | melder, begrafeniskosten, gemeentelijkeKosten, verhaaldBedrag, datumBegrafenis, datumAfgedaan, datumGemeld, inkoopordernummer, doodsoorzaak, achtergrondMelding, urenGemeente, datumRuimingGraf | Nee | GGM |

## Overervingshiërarchie

Geen overervingshiërarchie aanwezig in dit beleidsdomein.

## Relatiediagrammen

### Gemeente Begrafenissen

```
Gemeentebegrafenis [0..1] ──── NatuurlijkPersoon [1] (heeft)
```

## Observaties

- Dit beleidsdomein bevat 1 entiteiten.
- Entiteiten zijn gegroepeerd in 1 diagramgroepen: Gemeente Begrafenissen (1).
