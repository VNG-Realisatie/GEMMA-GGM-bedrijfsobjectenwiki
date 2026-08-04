# Migratieplan

Van de Claude-specifieke structuur naar Opzet als enige bron van waarheid. De stappen zijn klein en elk apart te committen; na elke stap blijft alles werkend.

## Stap 1 — Parallel draaien (nu)

`Opzet/` bestaat naast de oude structuur. De oude `CLAUDE.md` en `.claude/commands/` blijven functioneren. Gebruik deze fase om de nieuwe prompts in de praktijk te toetsen: voer een paar taken (ingest, lint, domain-status) uit vanuit de Opzet-prompts en corrigeer waar de herschreven tekst afwijkt van de bedoeling.

## Stap 2 — Opzet wordt leidend voor Claude Code

1. Vervang de inhoud van `Bedrijfsarchitectuur/CLAUDE.md` door een dunne verwijzing (zie [../adapters/claude-code.md](../adapters/claude-code.md)).
2. Vervang de bestanden in `.claude/commands/` door kopieën/symlinks van de Opzet-prompts (met `{{parameter}}` → `$ARGUMENTS`).
3. Verwijder `coverage.md` en `bo-coverage.md` uit `.claude/commands/`.
4. Werk in Claude Code een week met deze indirectie; los gaten op in `Opzet/`, niet in de adapters.

## Stap 3 — AGENTS.md in de root

Plaats een kopie of symlink van `Opzet/AGENTS.md` in de repo-root (en/of `Bedrijfsarchitectuur/`), zodat AGENTS.md-tools (Codex, Cursor, Aider) hem automatisch vinden. Let op: verwijzingen in AGENTS.md zijn relatief aan `Opzet/`; maak ze bij kopiëren root-relatief (`Opzet/context/...`).

## Stap 4 — Oude structuur opruimen

1. `Bedrijfsarchitectuur/templates/` vervangen door een verwijzing naar `Opzet/templates/` — of andersom: de Opzet-templates terugkopiëren zodra ze definitief zijn, en één van beide locaties opheffen. **Kies één canonieke locatie**; de wiki-tooling en prompts verwijzen nu naar `templates/`-paden, dus pas die verwijzingen in dezelfde commit aan.
2. `readme.md` actualiseren: verouderde skill-namen en `.claude/commands/`-verwijzing vervangen door een verwijzing naar `Opzet/` ("gefilterde kopie"-formulering is al correct).
3. Verifieer met `grep -r "\.claude/commands"` en `grep -r "/assess-bo\|/write-bo\|/coverage"` dat er buiten `Wiki/log.md` (historie — laten staan) geen verwijzingen naar de oude structuur meer zijn.

## Stap 5 — Andere tools aansluiten (naar behoefte)

Per tool de adapter volgen ([../adapters/](../adapters/)). Begin met een read-only taak (domain-status) om de contextlading te testen voordat schrijvende taken volgen.

## Wat bewust NIET migreert

- **Python-scripts** — blijven in `Bedrijfsarchitectuur/tools/` (zie [../tools/README.md](../tools/README.md)).
- **Wiki-inhoud** — de wiki zelf verandert niet door deze migratie. De linkconversie (VS Code-compatibiliteit) is een aparte, latere operatie: zie [aanbevelingen.md](aanbevelingen.md).
- **`Wiki/log.md`-historie** — oude `.claude/commands/`-paden in log-entries zijn geschiedenis en blijven staan.
- **Persoonlijke tool-configuratie** (Claude-permissions, memory) — vervalt vanzelf met de oude structuur; duurzame lessen staan al in `context/`.

## Terugvalscenario

Elke stap is een kleine commit; terugdraaien = de commit reverten. De oude commands en CLAUDE.md staan tot en met stap 3 onaangetast in git-historie.
