# Tools: Python-scripts

De scripts staan in `Bedrijfsarchitectuur/tools/` en zijn vendor-neutraal (Python 3, geen LLM-afhankelijkheid). Ze horen bij het project, niet bij de AI-laag; daarom staan ze niet in deze Opzet-map. Draai ze vanuit `Bedrijfsarchitectuur/`.

## Actieve scripts

| Script | Functie | Gebruikt door prompt |
|---|---|---|
| `parse_ggm_xmi.py` | Parse GGM-XMI → `Sources/GGM-repository/ggm_parsed.json`. Alleen bij een nieuwe GGM-release. | [generate-ggm](../prompts/generate-ggm.md), [export-ggm](../prompts/export-ggm.md), [write-element](../prompts/write-element.md) |
| `generate_ggm_wiki.py` | Genereer `Wiki/GGM/`-markdown uit de geparsede JSON. Telt alleen Objecttypen. `--dry-run` voor preview. | [generate-ggm](../prompts/generate-ggm.md) |
| `generate_ggm_enrich_bo.py` | Ververs `ggm_*`/`ggm_gemma_*`-frontmatter op BO-pagina's uit de JSON; raakt geen andere velden. `--dry-run` voor preview. | [generate-ggm](../prompts/generate-ggm.md) |
| `export_ggm_csv.py` | Genereer de 5 GGM-GEMMA CSV's uit JSON + wiki-BO-pagina's naar `exports/`. | [export-ggm](../prompts/export-ggm.md) |
| `entiteitendekking.py` | GGM-dekkingsanalyse: match, classificeer, traceer relaties; per-taakveldrapporten + totaaloverzicht + reviewlijst. `--all`, `--taakveld N`, `--dry-run`. | [entiteitendekking](../prompts/entiteitendekking.md) |
| `entiteitendekking_sync_bo.py` | Schrijf `analyse_ggm_dekking` chirurgisch terug naar BO-pagina's (alleen dat veld). `--dry-run` voor preview. | [entiteitendekking](../prompts/entiteitendekking.md) |
| `convert_pdf.py` | PDF → markdown; het markdown-bestand verschijnt naast de PDF. | [convert-pdf](../prompts/convert-pdf.md), [clip](../prompts/clip.md) |
| `migrate_frontmatter_style.py` | Normaliseer de frontmatter-stijl wiki-breed (lege waarden, quotestijl, veldnaam `onderwerp:`). Idempotent, met YAML-verificatie per bestand. | [lint](../prompts/lint.md) (als fix) |

## Eenmalige migratiescripts (bewaard als referentie)

`migrate_bo_bronnen.py`, `migrate_bronnen_to_body.py`, `migrate_bo_field_rename.py` — eerdere eenmalige datamigraties; niet meer nodig in de reguliere werkstroom.

## Vervangen scripts (kandidaat voor opschoning)

`coverage_analysis.py` en `bo_coverage_assess.py` — de oudere dekkingsanalyses; volledig vervangen door `entiteitendekking.py`. Zie [../migratie/aanbevelingen.md](../migratie/aanbevelingen.md).

## Extern (buiten de repo)

De crawl-taak ([crawl](../prompts/crawl.md)) gebruikt een lokale crawl4ai-installatie buiten deze repository — omgevingsafhankelijk, niet mee te migreren.
