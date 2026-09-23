# Skills herstructureren (compact, minder redundantie)

Status: **uitgevoerd** (2026-09-23). Vervangt de eerdere `ToDo/Audit-skills vereenvoudigen.md`.

## Context

Analyse van alle 15 skills in `Bedrijfsarchitectuur/.claude/commands/`, de generieke skills `crawl`/`setup-omgeving`, `CLAUDE.md`, `agent/rules/werkwijze.md`, `documentatie.md` en de 7 templates in `Bedrijfsarchitectuur/templates/` — op structuur, redundantie en formattering, met CLAUDE.md's eigen stijl (`- [ID] **kernonderwerp** — normatieve tekst`, tabellen) als maatstaf. Uitgangspunt: templates zijn sjablonen, geen rules — ze mogen naar een vormregel verwijzen maar niet zelf een regel of skill-tabel herhalen.

Gevonden: regeldubbelingen in CLAUDE.md zelf, dezelfde `bo_definitie`-vormcriteria drie keer herhaald (skill + skill + template), een begripstype-tabel gekopieerd tussen skill en template, en de drie audit-skills (`audit-duplicaten`, `audit-definities`, `audit-actoren`) overlappend met elkaar en met `lint_checks.py` — bevestigt en verscherpt het eerdere signaal in `Audit-skills vereenvoudigen.md`.

## Uitgevoerd

### 1. CLAUDE.md — regeldubbelingen opgeheven
- [x] `[IH6]`/`[IH7]` samengevoegd (beide: onzekere GGM-matching/mapping → `ter discussie`, nooit gokken); §5-prozaherhaling vervangen door verwijzing.
- [x] `[PR1]`/`[SRC6]` ontdubbeld: `[PR1]` blijft generiek, `[SRC6]` alleen de SRC-specifieke toevoeging met verwijzing naar `[PR1]`.
- [x] Model-pinning op één manier: YAML-frontmatter `model: haiku` in `lint.md` (patroon van `fetch.md`); prozazinnen geschrapt; `documentatie.md` verwijst naar de frontmatter-conventie i.p.v. het apart te beweren.

### 2. Vormregels vs. templates ontdubbeld
- [x] Nieuwe regel **`[VR3]`** (niet `[BO]` — geldt voor `bo_definitie` op elk elementtype: BO/actor/rol, niet BO-specifiek) in CLAUDE.md §6 Scope- & vormregels.
- [x] `write-element.md` Stap 5 en `templates/element.md` (frontmatter-placeholder) verwijzen nu naar `[VR3]` i.p.v. de criteria te herhalen.
- [x] `templates/onderwerpoverzicht.md` §Begripstypen: 8-rijen-tabel geschrapt, verwijst nu naar `assess-element.md` Stap 2 (had 'm zelf al gekopieerd terwijl het onderaan al naar die skill verwees).
- Gecheckt en akkoord bevonden (geen wijziging): `templates/element.md`'s Frontmatter-stijl-sectie (terecht lokaal, geen cross-cutting regel) en de per-template Linkconventie-secties (legitieme laag boven `[WC1]`/`[WC2]`).

### 3. Audit-landschap herbouwd: `/lint` (technisch) + `/audit-element` (inhoudelijk)
- [x] Besluit (via vraag aan gebruiker): de werkvoorraad-sweep uit `audit-actoren` is een derde modus in `/audit-element` geworden, geen aparte skill.
- [x] `lint.md` uitgebreid: `[VR3]`-referentie en `bo_synoniemen`-volledigheid toegevoegd als (nog niet gescripte) Stap-2-items. Bij verificatie bleek `lint_checks.py` de symmetrie- (`bo_homoniemen`) en synoniemveld-checks al te dekken — `audit-duplicaten` Stap 4/5 waren dus al pure duplicatie, niet alleen "mechaniseerbaar".
- [x] Nieuwe skill `audit-element.md` met drie modi: `definities` (uit `audit-definities` Stap 2a/2c/2d/4), `duplicaten` (uit `audit-duplicaten` Stap 1–3), `werkvoorraad` (uit `audit-actoren` Track 1+2). Draait op BO + Actoren + Rollen (voorheen alleen BO voor definitie-/duplicaatcontrole). Niet Haiku-gepind (inhoudelijke beoordeling, anders dan de oude `audit-duplicaten`-pin).
- [x] `audit-duplicaten.md`, `audit-definities.md`, `audit-actoren.md` verwijderd (`git rm`); kruisverwijzingen in `element-pipeline.md` en `CLAUDE.md` §6 bijgewerkt.
- [x] `documentatie.md`-skilltabel en de "Model voorkeur"-regel bijgewerkt.

### 4. Generieke documentatie losgekoppeld
- [x] Nieuw `agent/documentatie.md`: Karpathy LLM-wiki-patroon (verplaatst uit `Bedrijfsarchitectuur/documentatie.md` §Kernidee) + functie-overzicht voor `crawl`/`setup-omgeving`.
- [x] `Bedrijfsarchitectuur/documentatie.md`: §Kernidee ingekort tot verwijzing; `crawl`-rij uit de skilltabel, met pointer naar `agent/documentatie.md`.
- [x] `README.md`: `agent/`-rij uitgebreid met `documentatie.md`.

## Verificatie

- `python3 tools/lint_checks.py` gedraaid na alle wijzigingen: **"Regelverwijzingen: onbekend/dubbel ID of verboden zin: 0"** — de `[IH6]`/`[IH7]`-samenvoeging en de nieuwe `[VR3]` breken geen bestaande ID-referenties. `bo_definitie`-checks (leeg/placeholder) ongewijzigd op 0.
- `git status`/`git diff --stat` gecontroleerd: alleen de bestanden uit dit plan zijn geraakt.
- Niet gedaan (aan gebruiker): handmatige doorloop van `/audit-element`'s drie modi op een echt voorbeeld, en het bijwerken van `Opzet/` (die dezelfde drie audit-skills als vendor-neutrale kopie bevat onder `Opzet/prompts/` — buiten scope van dit plan, nu wel stale t.o.v. de nieuwe `/audit-element`).
