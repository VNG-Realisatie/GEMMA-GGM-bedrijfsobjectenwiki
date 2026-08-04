# Aanbevelingen en ontbrekende onderdelen

## 1. Linkconversie voor VS Code + Obsidian (besluit 4)

Het grootste openstaande punt: de wiki gebruikt vault-absolute Obsidian-links (`[[Wiki/...|alias]]`) die in VS Code verkeerd resolven en bij aanklikken nieuwe pagina's creëren. Doelconventie ([../context/conventies.md](../context/conventies.md)): relatieve markdown-links.

Aanpak:

1. Zet in Obsidian *Settings → Files & Links → New link format* op **Relative path to file** en *Use [[Wikilinks]]* **uit** — nieuwe links zijn dan meteen goed.
2. Schrijf een conversiescript (analoog aan `migrate_frontmatter_style.py`: idempotent, met verificatie en terugdraai-optie per bestand) dat `[[pad|alias]]` en `[[pad\|alias]]` omzet naar relatieve markdown-links.
3. **Pas de parsers eerst aan**: `entiteitendekking.py`, `export_ggm_csv.py` en de lint-checks parsen wiki-links (o.a. `bo_relaties.bedrijfsobject`, vetgedrukte subtype-namen, `## Bronnen`-secties). Converteer pas als de tooling beide syntaxen leest.
4. Converteer in fasen (per Wiki-submap), telkens met `entiteitendekking.py --all` als regressietest.

## 2. Opschonen

- `tools/coverage_analysis.py` en `tools/bo_coverage_assess.py` verwijderen (vervangen door `entiteitendekking.py`), samen met de laatste command-bestanden in stap 2 van het [migratieplan](migratieplan.md).
- Losse artefacten in de repo-root (`output.md`, `screenshot.png`, `GGM_DEKKING_DATABLOCK.md`, `ggm_entiteiten_dekking_extract.json`) verplaatsen naar `Wiki/Analyses/` of verwijderen.
- `Bedrijfsarchitectuur/export_spec.md` (work-in-progress, overlapt met de bestaande 5-CSV-export) afmaken of samenvoegen met [../prompts/export-ggm.md](../prompts/export-ggm.md).

## 3. Ontbrekende onderdelen die een generiek AI-project zou moeten hebben

- **Verificatie-checklist na ingest** — een korte, afvinkbare lijst (keten sluitend? index/log bijgewerkt? tellingen kloppen?) als vast slot van [../workflows/ingest.md](../workflows/ingest.md); nu impliciet.
- **Prompt-regressietest** — een kleine set voorbeeldcasussen (één begrip per uitkomstklasse: BO/geen-BO/actor/homoniem) waarmee je na een promptwijziging of modelwissel controleert of de beoordeling stabiel blijft.
- **Versionering van prompts** — prompts wijzigen gedrag; noteer wijzigingen in `Wiki/log.md` (type `fix`) of geef prompts een versieregel, zodat beoordelingen uit verschillende periodes duidbaar zijn.
- **Onboarding-document voor teamleden** — de [presentatie](../presentatie.md) dekt de kennissessie; een halve pagina "je eerste ingest, stap voor stap" zou de drempel verder verlagen.
- **Licentie in Opzet** — de wiki is EUPL 1.2 (readme); neem die vermelding ook op in [../README.md](../README.md) zodra Opzet leidend wordt.
- **Decision log** — de zes besluiten van 2026-07-18 staan nu in [analyse.md](analyse.md); overweeg een vast, licht formaat (datum, vraag, besluit, motivatie) voor toekomstige werkafspraak-besluiten, bijv. als sectie in `Wiki/log.md`.

## 4. Kleinere verbeteringen

- **Contextbudget-profielen** — per prompt staat de benodigde context al in de kop; voor chat- en lokale tools zou een kant-en-klaar "bundelscript" (concateneer AGENTS.md + regels + prompt) het handwerk uit [../adapters/chat-tools.md](../adapters/chat-tools.md) automatiseren.
- **Backlog-hygiëne** — `ToDo/` bevat naast de ingest-backlog ook oudere notities; periodiek opschonen of samenvoegen met de openstaande-acties-secties in de onderwerpoverzichten.
- **Multi-line frontmatter-artefacten** — drie BO-pagina's hebben nog een oud XMI-importartefact in `ggm_definitie` (zie `Wiki/log.md` 2026-07-09); eenmalig handmatig herstellen.
