# Analyse van de oude structuur

Peildatum: 2026-07-18. Dit document beschrijft wat er was, wat Claude-specifiek was, en wat er per onderdeel mee is gebeurd.

## Inventaris

| Onderdeel | Locatie | Omvang | Oordeel |
|---|---|---|---|
| `CLAUDE.md` | `Bedrijfsarchitectuur/` | 264 regels, monolitisch | **Opgesplitst** in [../AGENTS.md](../AGENTS.md), [../context/](../context/) (8 bestanden) en [../workflows/](../workflows/) (4 bestanden) |
| Slash-commands | `.claude/commands/` (repo-root) | 17 bestanden | **15 omgezet** naar [../prompts/](../prompts/); 2 vervallen (deprecated) |
| `settings.local.json` | `.claude/` | alleen permissions | **Niet overdraagbaar** (Claude-specifiek); per tool behandeld in [../adapters/](../adapters/) |
| Memory/feedback | `~/.claude/.../memory/` + in-repo | los mechanisme | **Mechanisme niet overdraagbaar**; de projectkennis eruit is opgenomen in `context/` |
| Templates | `Bedrijfsarchitectuur/templates/` | 5 bestanden | **Overgenomen en consistent gemaakt** in [../templates/](../templates/) |
| Python-scripts | `Bedrijfsarchitectuur/tools/` | 13 scripts | **Blijven staan** (al vendor-neutraal); gecatalogiseerd in [../tools/README.md](../tools/README.md) |
| `readme.md`, `llm-wiki.md` | `Bedrijfsarchitectuur/` | projectdocumentatie | Blijven; readme actualiseren (zie [migratieplan.md](migratieplan.md)) |

## Claude-specifieke onderdelen en hun omzetting

| Claude-specifiek | Diende voor | Vendor-neutrale vorm |
|---|---|---|
| `CLAUDE.md` (automatisch geladen) | Projectinstructies per sessie | `AGENTS.md` (open standaard) + `context/`-bestanden; per tool geladen via [../adapters/](../adapters/) |
| Slash-commands met `$ARGUMENTS` | Herbruikbare taakaanroepen | Promptbestanden met benoemde `{{parameter}}`-placeholders en gedocumenteerde context/uitvoer |
| `model: haiku`-frontmatter en "Voer uit op Haiku"-instructies | Goedkope uitvoering van read-only taken | Kopveld **Aanbevolen model: licht/standaard**; toolonafhankelijk uitgelegd in [../prompts/README.md](../prompts/README.md) |
| Slash-orkestratie (`/ingest` roept `/assess-element` aan) | Taakketens | Verwijzing naar het promptbestand als volgende taak |
| Subagent-golven in `audit-actoren` | Parallelle sweeps | "Parallel in batches als de tool het ondersteunt; anders sequentieel" |
| `settings.local.json` permissions | Toestemmingen voor tools/shell | Niet overdraagbaar; equivalent per tool in de adapters (bijv. Aider-config, Cursor-rules) |
| Memory-systeem | Persistente feedback tussen sessies | Niet overdraagbaar; de duurzame lessen zijn nu gewone projectkennis in `context/` (o.a. multi-gemeente-bronnen, XMI als bron van waarheid, definitieregels, niet-herschrijven-regel) |
| Skills-terminologie | Naam voor de commands | Overal "prompt"/"taak" |

## Niet overgenomen

- **`coverage.md` en `bo-coverage.md`** — deprecated; volledig vervangen door de entiteitendekking-taak. De bijbehorende scripts (`coverage_analysis.py`, `bo_coverage_assess.py`) staan als opschoonkandidaat in [aanbevelingen.md](aanbevelingen.md).
- **Dode verwijzing `tools/enrich_bo_frontmatter.py`** (genoemd in het oude `lint.md`) — het script bestaat niet; de nieuwe lint-prompt verwijst naar het wél bestaande `migrate_frontmatter_style.py`.
- **`templates/index-log.md`** — werd in CLAUDE.md genoemd maar bestond niet; het index/log-formaat is nu uit de praktijk gedocumenteerd in [../context/paginatypes.md](../context/paginatypes.md).

## Tegenstrijdigheden in de oude structuur (opgelost, met besluit)

Besproken met de eigenaar op 2026-07-18:

1. **"Ongefiltreerde" (CLAUDE.md) vs. "gefilterde" (readme) kopie van het GGM** → *gefilterd* is juist: er is destijds gefilterd, maar zonder expliciete criteria.
2. **Bronlocatie** `Sources/{onderwerp}/` vs. `Sources/Onderwerpen/{onderwerp}/` (beide gedocumenteerd én in gebruik) → gemeentelijke onderwerpen altijd onder `Onderwerpen/`, met een vaste uitzonderingenlijst direct onder `Sources/`.
3. **"Wijzig nooit Sources" vs. de Niet-relevant-verplaatsstap in ingest** → inhoud is immutabel; ordenen (verplaatsen/hernoemen) en frontmatter-intake mogen.
4. **Linkconventies conflicteerden** (wiki-links vs. markdown-links naar Sources; vault-absolute wiki-links breken in VS Code) → doelconventie: relatieve markdown-links die in VS Code én Obsidian werken; huidige wiki-praktijk blijft geldig tot de linkconversie (zie [aanbevelingen.md](aanbevelingen.md)).
5. **Regel "externe actoren geen eigen begrip" vs. bestaande ketenpartner-pagina's in Wiki/Actoren** → externe actoren mogen een actor-/rolpagina; het gemeentelijk perspectief begrenst alleen de BO-scope.
6. **"Bespreek eerst" vs. autonomieregels vs. "vragen per begrip"** → getrapt model: bespreken op bronniveau, autonomie bij eenduidige begrippen, twijfelgevallen per stuk.

## Feitelijke fouten in de oude structuur (gecorrigeerd in de nieuwe bestanden)

- CLAUDE.md-directoryboom noemde `Wiki/Onderwerpen/`; de echte map heet `Wiki/Onderwerpoverzichten/`. De boom miste bovendien `Wiki/GGM/`, `Wiki/GEMMA/`, `exports/`, `ToDo/` en `Clippings/`.
- `readme.md` noemt verouderde skill-namen (`/assess-bo`, `/write-bo`, "9 skills") en het vervangen `/coverage`.
- De skill-tabel in CLAUDE.md miste 4 bestaande commands (audit-definities, audit-actoren, convert_pdf, crawl).
- `templates/element.md` noemde het frontmatterveld `homoniemen` waar praktijk en schema `bo_homoniemen` gebruiken (26 pagina's), en bevatte een kapotte linksyntax in de linkconventie.
- De crawl-taak hangt af van bestanden buiten de repo (`crawl4ai`-installatie) — nu expliciet als omgevingsafhankelijk gemarkeerd.
