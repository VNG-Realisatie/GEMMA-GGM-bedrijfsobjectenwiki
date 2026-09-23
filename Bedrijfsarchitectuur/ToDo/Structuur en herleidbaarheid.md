# Structuur en herleidbaarheid

Status per 2026-09-23. Alle 4 openstaande punten uit de vorige versie zijn via interview besloten en (op één punt na) geïmplementeerd.

## 1. Indeling: onderwerp vs. taakveld/beleidsdomein — ✅ opgelost (besloten: bewust impliciet)

**Oorspronkelijk issue:** rubrieken, onderwerpen, taakvelden, domeinen en beleidsdomeinen overlapten op niet-eenduidige wijze; een harde mapping ontbrak, ook voor terugmelden op de ggm-indeling.

**Opgelost:**
- Terminologie teruggebracht tot twee vaste assen: **onderwerp** (brongedreven, ad hoc — `Sources/Onderwerpen/{onderwerp}/`, `Wiki/Bronsamenvattingen/{onderwerp}/`, `Wiki/Onderwerpoverzichten/{onderwerp}.md`) en **taakveld/beleidsdomein** (vastliggend, GGM-ontleend — `Wiki/Bedrijfsobjecten/{taakveld}/{beleidsdomein}/`, `Wiki/GGM/{taakveld}/`).
- GGM-terugmelden loopt niet via "onderwerp" maar direct vanuit de BO-pagina op de GGM-indeling (zie §4).
- **Besluit (interview 2026-09-23):** geen expliciete n:n-mappingtabel onderwerp ↔ taakveld/beleidsdomein. De huidige contextuele bepaling per `/domain-status`-run volstaat; formeel vastleggen levert onderhoudslast op die niet opweegt tegen het voordeel. Geen verdere actie.

## 2. GGM als bron + leesbare samenvatting in de wiki — ✅ opgelost

Bron van waarheid: `Sources/GGM-repository/ggm_parsed.json` (via `/generate-ggm`, [SRC1]–[SRC4]). Top-down index: [[Wiki/GGM/structuur-ggm|Structuur GGM]]. Pagina per beleidsdomein: `Wiki/GGM/{taakveld}/` (gegenereerd, [WC12]: nooit handmatig bewerken).

## 3. Frontmatter `bedrijfsfuncties`/`bedrijfsprocessen` — ✅ besloten en gebouwd, 🔶 migratie loopt nog

**Oorspronkelijk issue:** vrije lijsten zonder eigen pagina's → niet herleidbaar, geen consistentie.

**Besluit (interview 2026-09-23):** bedrijfsfuncties en bedrijfsprocessen worden volwaardige elementen met eigen pagina, zelfde behandeling als bedrijfsobject/actor/rol:
- **Locatie:** onder taakveld/beleidsdomein, zoals BO's (niet plat zoals Actoren/Rollen) — `Wiki/Bedrijfsfuncties/{taakveld}/{beleidsdomein}/` en `Wiki/Bedrijfsprocessen/{taakveld}/{beleidsdomein}/`.
- **Bron:** ad hoc, net als BO's — pagina ontstaat zodra een BO ernaar verwijst, herleid naar de bron waarin de gemeente de functie/het proces noemt. Geen vooraf geïmporteerde lijst.
- **Beoordelingsflow:** zelfde flow als BO/actor/rol — nieuw elementtype in `/assess-element` en `/write-element`, hergebruikt de bestaande 6-criteria-structuur en `templates/element.md`.

**Gebouwd:**
- Nieuwe naslagpagina [[Wiki/GEMMA/functies-en-processen|Bedrijfsfuncties en bedrijfsprocessen]] — definities en 6 diagnostische vragen per type, analoog aan [[Wiki/GEMMA/actoren-en-rollen|Actoren en rollen]].
- `templates/element.md` — locaties, `archimate_type: business-function|business-process` toegevoegd, `bedrijfsprocessen`/`bedrijfsfuncties` omgezet van vrije tekst naar verplichte wiki-links.
- `/assess-element` — begripstypen `bedrijfsfunctie`/`bedrijfsproces` toegevoegd (Stap 2), nieuwe Stap 2c (functie/proces-toets), Stap 3- en Stap 11-tabellen bijgewerkt.
- `/write-element` — nieuwe Stap 12 (Bedrijfsfunctie- en bedrijfsprocespagina's), analoog aan Stap 11 (Actor/rol) maar met taakveld/beleidsdomein-substructuur en het twee-pagina-patroon als uitzondering i.p.v. regel.
- `Bedrijfsarchitectuur/CLAUDE.md` — §3-paginatypetabel, §7-directorystructuur en [BO12] bijgewerkt.
- `tools/lint_checks.py` — `Wiki/Bedrijfsfuncties/`/`Wiki/Bedrijfsprocessen/` meegenomen in alle generieke elementchecks (frontmatter-compleetheid, `archimate_type`-enum, map-plaatsing); twee nieuwe checks: wees-bedrijfsfunctie/-proces (pagina door niets genoemd) en vrije-tekst/dode-link-detectie op de `bedrijfsprocessen`/`bedrijfsfuncties`-velden.

**Nog open — migratie-achterstand, bewust niet nu gebulkt:** de eerste lint-run na dit besluit vindt **1296** bestaande `bedrijfsprocessen`/`bedrijfsfuncties`-items die nog vrije tekst zijn (alle BO's van vóór dit besluit). Dit is verwachte achterstand, geen regressie — elke migratie vereist een inhoudelijke beoordeling van de onderliggende functie/het proces (net als een BO niet blind wordt aangemaakt) en wordt dus geleidelijk gedaan via `/assess-element`+`/write-element`, niet in bulk. Zie `.claude/commands/lint.md` voor de expliciete niet-bulk-instructie.

**Bewust buiten scope gelaten:** `tools/entiteitendekking.py` matcht Wiki/Bedrijfsfuncties//Bedrijfsprocessen-pagina's nog niet tegen GGM-`proces`-entiteiten (die blijven n.v.t. in de dekkingsanalyse, zoals al vóór dit besluit). Functioneel consistent met "GGM dekt processen doorgaans niet compleet" — zou pas relevant worden als er ooit GGM-procesentiteiten met een duidelijke BO-achtige grondslag opduiken. Geen actie nu.

## 4. GGM-terugmeldingen — ✅ opgelost

`templates/ggm-terugmelding.md` + doorlopend logbestand `Wiki/Analyses/ggm-terugmeldingen.md`. Terugmelden gebeurt vanuit de BO-pagina op `ggm_guid`/GGM-structuur.

## 5. GGM-dekking (bottom-up matching + per-beleidsdomein rapport) — ✅ opgelost

Vrijwel 1-op-1 geïmplementeerd in `/entiteitendekking` (`tools/entiteitendekking.py`): per-taakveld rapporten + `totaaloverzicht.md` met de gevraagde tellingen (met BO, ondersteunend, niet gedekt/hiaat, n.v.t., BO's zonder GGM-entiteit), ambigue matches expliciet als "⚠️ ter discussie" i.p.v. geraden, `review.md` voor laag-confidence classificaties, `entiteitendekking_sync_bo.py` voor de omgekeerde index per BO.

## 6. Lint: samengestelde end-to-end traceability-check — ✅ gebouwd (besloten: nu bouwen)

**Besluit (interview 2026-09-23):** één samengestelde check i.p.v. drie losse deelbevindingen laten volstaan.

**Gebouwd:** `check_traceability_naar_bron()` in `tools/lint_checks.py` — per BO-pagina één "geen pad naar brondocument"-signaal, met de precieze plek waar de keten breekt (niet gelinkt vanuit onderwerpoverzicht / geen `## Bronnen`-sectie / `## Bronnen`-sectie zonder bronsamenvatting-link / geen van de gelinkte bronsamenvattingen heeft een geldige Sources-link). Rapportregel: "Element zonder volledig pad naar brondocument". Eerste run: 18 bevindingen (bestaande gaten, geen regressie door deze wijziging).

## 7. Ingest bottom-up: bronsamenvatting → onderwerpoverzicht — ✅ gebouwd (besloten: nu bouwen)

**Besluit (interview 2026-09-23):** nieuwe check toevoegen, analoog aan `check_orphan_bos`.

**Gebouwd:** `check_bronsamenvatting_verwerkt()` in `tools/lint_checks.py` — signaleert `Wiki/Bronsamenvattingen/`-pagina's die in geen enkel onderwerpoverzicht worden genoemd. Rapportregel: "Bronsamenvatting niet verwerkt in onderwerpoverzicht". Eerste run: 10 bevindingen.

---

## Openstaand vervolgwerk

| # | Punt | Actie | Urgentie |
|---|---|---|---|
| 3 | 1296 bestaande `bedrijfsprocessen`/`bedrijfsfuncties`-vermeldingen zijn nog vrije tekst | Geleidelijk migreren via `/assess-element`+`/write-element` per functie/proces, niet in bulk | Laag — achterstand, geen fout |
| 3 | `entiteitendekking.py` matcht bedrijfsfunctie/-proces-pagina's niet tegen GGM `proces`-entiteiten | Pas oppakken als er een concrete aanleiding is (bijv. een GGM-procesentiteit met BO-achtige grondslag) | Zeer laag |
| 6/7 | Eerste runs van de twee nieuwe checks (18 resp. 10 bevindingen) nog niet inhoudelijk getriaged | Doorlopen via `/lint` — beoordelen welke terecht zijn en welke omissie | Middel |
