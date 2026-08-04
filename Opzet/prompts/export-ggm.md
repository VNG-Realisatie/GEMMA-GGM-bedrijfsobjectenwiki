# export-ggm

**Doel:** de vijf GGM-GEMMA CSV's genereren uit het geparsede XMI plus de wiki-BO-pagina's, voor de GGM-GEMMA-data-uitwisseling.
**Aanbevolen model:** standaard
**Parameters:** geen.
**Benodigde context:** [../tools/README.md](../tools/README.md), `Sources/GGM-repository/ggm_parsed.json`, `Wiki/Bedrijfsobjecten/`.
**Verwachte uitvoer:** vijf CSV's in `exports/` met datumstempel (separator `;`, alle velden gequote) plus een steekproefrapportage.

## Prompt

Genereer de GGM-GEMMA export-CSV's.

1. Zorg dat het geparsede XMI actueel is: `python3 tools/parse_ggm_xmi.py`
2. Draai het exportscript: `python3 tools/export_ggm_csv.py`
3. Toon de samenvatting en de bestanden in `exports/`:

| Bestand | Inhoud |
|---|---|
| `GGM_GEMMA_objecten_{datum}.csv` | Alle GGM-entiteiten + GEMMA-velden (conform de uitwisselspecificatie) |
| `GGM_GEMMA_relaties_{datum}.csv` | Alle GGM-relaties + GEMMA-velden (conform de uitwisselspecificatie) |
| `GGM_diagram_objecten_{datum}.csv` | Eén regel per diagram-entiteit |
| `GGM_beleidsdomeinen_{datum}.csv` | Beleidsdomein-metadata |
| `GGM_diagrammen_{datum}.csv` | Diagram-metadata |

4. Controleer steekproefsgewijs: een BO mét wiki-pagina heeft gevulde GEMMA-velden; een entiteit zonder pagina heeft lege of XMI-GEMMA-velden; relatie-GUIDs (source/target) kloppen; diagram-entiteiten komen overeen met het model.
5. Rapporteer de bevindingen.

**Prioriteit GEMMA-velden:** (1) wiki-BO-pagina (naam, definitie) → (2) XMI GEMMA-tags → (3) leeg. GEMMA-guid, -url en -type komen altijd uit de XMI GEMMA-tags (GEMMA-beheerd).

## Voorbeeld

> Genereer de GGM-GEMMA export-CSV's.
