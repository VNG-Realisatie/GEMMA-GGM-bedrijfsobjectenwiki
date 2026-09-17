Genereer GGM-GEMMA export CSV's.

Input: `ggm_parsed.json` + `Wiki/Bedrijfsobjecten/`.
Output: `exports/*.csv` (5 bestanden, via `tools/export_ggm_csv.py`).

Stappen:
1. Zorg dat het geparsede XMI beschikbaar is:
   ```
   python3 tools/parse_ggm_xmi.py > /tmp/ggm_parsed.json
   ```
2. Draai het export-script:
   ```
   python3 tools/export_ggm_csv.py
   ```
3. Toon de samenvatting die het script print en de bestanden in `exports/`.
4. Controleer steekproefsgewijs:
   - Een BO met wiki-pagina: GEMMA-velden moeten ingevuld zijn
   - Een entiteit zonder wiki-pagina: GEMMA-velden leeg of uit XMI GEMMA-tags
   - Een relatie: source/target GUIDs moeten kloppen
   - Een diagram: entiteiten moeten overeenkomen met het GGM-model
5. Rapporteer bevindingen aan de gebruiker.

De CSV's worden aangemaakt in `exports/` met datumstempel. Separator is `;`, alle velden quoted.

### CSV-bestanden

| Bestand | Inhoud | Conform |
|---|---|---|
| `GGM_GEMMA_objecten_{datum}.csv` | Alle GGM-entiteiten + GEMMA-velden | Specificatie GGM-GEMMA data-uitwisseling |
| `GGM_GEMMA_relaties_{datum}.csv` | Alle GGM-relaties + GEMMA-velden | Specificatie GGM-GEMMA data-uitwisseling |
| `GGM_diagram_objecten_{datum}.csv` | Per diagram-entiteit één regel | Nieuw (GGM-diagramindeling) |
| `GGM_beleidsdomeinen_{datum}.csv` | Beleidsdomein metadata | Nieuw |
| `GGM_diagrammen_{datum}.csv` | Diagram metadata | Nieuw |

### GEMMA-velden prioriteit

1. Wiki BO-pagina (naam, gemma_definitie)
2. XMI GEMMA-tags (fallback)
3. Leeg

GEMMA-guid, GEMMA-url, GEMMA-type: altijd uit XMI GEMMA-tags (GEMMA-beheerd).
