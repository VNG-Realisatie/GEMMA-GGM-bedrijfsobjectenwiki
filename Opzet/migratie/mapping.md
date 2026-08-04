# Mapping: oud → nieuw

## CLAUDE.md (per sectie)

| Oude sectie (Bedrijfsarchitectuur/CLAUDE.md) | Nieuw bestand |
|---|---|
| Titel + intro | [../context/project.md](../context/project.md), [../AGENTS.md](../AGENTS.md) |
| Doel (4 stappen, herleidbaarheidsketen) | [../context/project.md](../context/project.md) |
| Werkwijze (onderwerp-voor-onderwerp) | [../context/project.md](../context/project.md) |
| Onderhoudscyclus | [../context/project.md](../context/project.md), [../workflows/onderhoudscyclus.md](../workflows/onderhoudscyclus.md) |
| LLM-rol | [../context/project.md](../context/project.md), [../context/ai-richtlijnen.md](../context/ai-richtlijnen.md) |
| Directorystructuur | [../context/architectuur.md](../context/architectuur.md) (gecorrigeerd naar de werkelijke structuur) |
| Bronnen (Sources) + Bronnen toevoegen | [../context/bronnen.md](../context/bronnen.md) |
| GGM-bronbestandformaat + GGM-terminologie | [../context/bronnen.md](../context/bronnen.md), [../templates/ggm-bron.md](../templates/ggm-bron.md) |
| Wiki-pagina's (tabel paginatypes) | [../context/paginatypes.md](../context/paginatypes.md) |
| Beoordelingslogica (verwijzingen) | [../context/paginatypes.md](../context/paginatypes.md) |
| Conventies | [../context/conventies.md](../context/conventies.md) |
| Ingest workflow | [../workflows/ingest.md](../workflows/ingest.md) |
| Vragen beantwoorden | [../workflows/vragen-beantwoorden.md](../workflows/vragen-beantwoorden.md) |
| Lint | [../workflows/lint.md](../workflows/lint.md) |
| Skills (tabel) | [../prompts/README.md](../prompts/README.md) |
| Model voorkeur (Haiku) | [../prompts/README.md](../prompts/README.md) (veld "Aanbevolen model") |
| Tools (tabel) + GGM-data gebruiken | [../tools/README.md](../tools/README.md), [../context/ai-richtlijnen.md](../context/ai-richtlijnen.md) |
| Citation & verification rules | [../context/schrijfregels.md](../context/schrijfregels.md) |
| Principes | [../context/regels.md](../context/regels.md) |
| Regels (12) | [../context/regels.md](../context/regels.md) (geherformuleerd conform besluiten 3, 5 en 6) |

## Commands (alle 17)

| Oud (.claude/commands/) | Nieuw | Opmerking |
|---|---|---|
| `ingest.md` | [../prompts/ingest.md](../prompts/ingest.md) | Slash-orkestratie → promptverwijzingen; bronlocatie conform besluit 2 |
| `assess-element.md` | [../prompts/assess-element.md](../prompts/assess-element.md) | Externe actoren conform besluit 5 |
| `write-element.md` | [../prompts/write-element.md](../prompts/write-element.md) | Definitieregels (stap 5) verplaatst naar [../context/schrijfregels.md](../context/schrijfregels.md) |
| `entiteitendekking.md` | [../prompts/entiteitendekking.md](../prompts/entiteitendekking.md) | — |
| `domain-status.md` | [../prompts/domain-status.md](../prompts/domain-status.md) | Model: licht |
| `lint.md` | [../prompts/lint.md](../prompts/lint.md) | Dode verwijzing `enrich_bo_frontmatter.py` verwijderd; Haiku-instructie → "licht" |
| `fetch.md` | [../prompts/fetch.md](../prompts/fetch.md) | `model: haiku`-frontmatter → "licht"; "nooit WebFetch" → toolneutraal geformuleerd |
| `clip.md` | [../prompts/clip.md](../prompts/clip.md) | — |
| `convert_pdf.md` | [../prompts/convert-pdf.md](../prompts/convert-pdf.md) | Bestandsnaam nu kebab-case |
| `crawl.md` | [../prompts/crawl.md](../prompts/crawl.md) | Gemarkeerd als omgevingsafhankelijk (externe crawl4ai-installatie) |
| `generate-ggm.md` | [../prompts/generate-ggm.md](../prompts/generate-ggm.md) | — |
| `export-ggm.md` | [../prompts/export-ggm.md](../prompts/export-ggm.md) | Verouderde `/tmp`-redirect uit stap 1 verwijderd (script schrijft zelf naar de repository) |
| `audit-duplicaten.md` | [../prompts/audit-duplicaten.md](../prompts/audit-duplicaten.md) | Haiku-instructie → "licht" |
| `audit-definities.md` | [../prompts/audit-definities.md](../prompts/audit-definities.md) | — |
| `audit-actoren.md` | [../prompts/audit-actoren.md](../prompts/audit-actoren.md) | Subagent-golven → toolneutrale batchinstructie |
| `coverage.md` | — vervallen | Deprecated; vervangen door entiteitendekking |
| `bo-coverage.md` | — vervallen | Deprecated; vervangen door entiteitendekking |

## Overig

| Oud | Nieuw |
|---|---|
| `templates/element.md` | [../templates/element.md](../templates/element.md) — `bo_homoniemen` consequent, linktypo gefixt, taakverwijzingen geneutraliseerd |
| `templates/bronsamenvatting.md` | [../templates/bronsamenvatting.md](../templates/bronsamenvatting.md) — bronpad conform besluit 2, aliasregel geëxpliciteerd |
| `templates/onderwerpoverzicht.md` | [../templates/onderwerpoverzicht.md](../templates/onderwerpoverzicht.md) — begripstypen-tabel gededupliceerd (staat in assess-element) |
| `templates/analyse.md` | [../templates/analyse.md](../templates/analyse.md) |
| `templates/ggm-bron.md` | [../templates/ggm-bron.md](../templates/ggm-bron.md) |
| `templates/index-log.md` (bestond niet) | [../context/paginatypes.md](../context/paginatypes.md) — formaat uit de praktijk gedocumenteerd |
| `.claude/settings.local.json` | — niet overdraagbaar; per tool in [../adapters/](../adapters/) |
| Memory-bestanden (feedbackregels) | Inhoudelijk verwerkt in [../context/bronnen.md](../context/bronnen.md), [../context/schrijfregels.md](../context/schrijfregels.md), [../context/regels.md](../context/regels.md), [../context/ai-richtlijnen.md](../context/ai-richtlijnen.md) |
| `readme.md` (werkwijze-deel) | Blijft bestaan; actualiseren volgens [migratieplan.md](migratieplan.md) stap 4 |
