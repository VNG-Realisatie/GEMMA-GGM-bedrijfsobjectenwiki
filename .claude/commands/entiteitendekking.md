Genereer of ververs de entiteitendekking-rapportage: $ARGUMENTS

Doel: uniforme analyse van GGM-entiteiten per taakveld/beleidsdomein. Toont per beleidsdomein welke entiteiten BO zijn, welke niet (met entiteitstype en relatie tot BO), en welke BO's geen GGM-grondslag hebben (hiaten). Vervangt ggm-vergelijking, ggm-dekking en bo-dekking in één rapport.

## Werkwijze

### Stap 1: Script draaien

```bash
python3 tools/entiteitendekking.py --all              # alle taakvelden
python3 tools/entiteitendekking.py --taakveld 9       # één taakveld
python3 tools/entiteitendekking.py --all --dry-run    # alleen counts
```

Het script genereert in `Wiki/Analyses/entiteitendekking/`:
- Per-taakveld rapporten (~12 bestanden)
- `totaaloverzicht.md` — samenvattende tabel per beleidsdomein
- `review.md` — items die LLM-review nodig hebben

### Stap 2: Review

Lees `review.md`. Dit bevat twee soorten items, niet met elkaar te verwarren:

1. **`confidence=low`** — classificatie onzeker (`classify_entity` vond geen sterk signaal). Per item: controleer het gesuggereerde entiteitstype en pas aan in de draft als nodig.
2. **`⚠️ ter discussie tussen [[BO1]] / [[BO2]]`** (in de per-taakveld tabel, kolom BO/Dekking) — een structurele ambiguïteit: `compute_dekking` vond meerdere even-goede kandidaat-BO's (zelfde aantal hops, zelfde beleidsdomein, geen naam-bevestiging voor één van beide) en kiest bewust niet stilzwijgend. Dit is geen classificatie-onzekerheid maar een echte inhoudelijke keuze die een mens moet maken.

**Workflow voor `ter discussie`-items:**
1. Lees de GGM-definitie van de entiteit (`Wiki/GGM/{taakveld}/...`) en vergelijk met de definitie van elke kandidaat-BO.
2. Kies de BO waar de entiteit inhoudelijk het beste bij past — of concludeer dat geen van de kandidaten past (dan blijft het `ter discussie` staan, of de entiteit krijgt een eigen beoordeling in de Beoordeling-sectie).
3. Registreer de keuze op de frontmatter van de **gekozen** BO-pagina onder `bo_via_kandidaten` (zie `templates/bedrijfsobject.md`) — dezelfde curatie-aanpak als `bo_subtypes`.
4. Draai Stap 1 opnieuw: de entiteit wordt dan direct herkend (stap 0 in `compute_dekking`, vóór alle heuristiek) en verdwijnt uit de ambigue lijst, permanent (niet opnieuw berekend bij een volgende run).

Behandel niet alle `ter discussie`-items in één keer als het er veel zijn — triage eerst (duidelijke gevallen apart van genuine twijfelgevallen), en forceer geen keuze als geen enkele kandidaat goed past.

### Stap 3: Beoordeling verrijken

Elk per-taakveld rapport heeft een `## Beoordeling` sectie bovenin met `<!-- REVIEW -->` marker. Vervang met inhoudelijke beoordeling:

- Structurele patronen (welke typen entiteiten worden geen BO en waarom)
- Functionele dekking (wat ontbreekt inhoudelijk in het GGM)
- Cross-domein observaties
- Naamconflicten en disambiguatie

**Herhaal geen tellingen, percentages of per-entiteit-detail.** Die staan al in de scriptgegenereerde statistiekregel per beleidsdomein (zie Rapportstructuur) en, per BO, in `analyse_ggm_dekking` (Stap 5) — beide blijven altijd vers na een her-run, in tegenstelling tot deze proza-sectie. Focus uitsluitend op interpretatie: waarom ontbreken bepaalde typen, wat betekent dit inhoudelijk.

### Stap 4: Afronden

1. Update `Wiki/index.md` met de nieuwe analyse-pagina's
2. Voeg entry toe aan `Wiki/log.md`

### Stap 5: BO-frontmatter synchroniseren

```bash
python3 tools/entiteitendekking_sync_bo.py --dry-run   # preview per BO
python3 tools/entiteitendekking_sync_bo.py              # echt schrijven
```

Herberekent dezelfde analyse (los van wat er in de per-taakveld rapporten staat) en schrijft `analyse_ggm_dekking` — de omgekeerde index "welke GGM-entiteiten dekt dit BO" — terug naar elke BO-pagina met GGM-betrokkenheid. Chirurgische patch: raakt alleen dat ene veld, nooit `bo_*`/`ggm_*`/body.

**Losse stap, niet gebundeld in Stap 1.** Zo laat `git diff` altijd zien of een run alleen `Wiki/Analyses/` raakte of ook BO-pagina's in `Wiki/Bedrijfsobjecten/`.

**Bekende inconsistentie:** dit script herberekent altijd vanuit de brondata (GGM + BO-pagina's), nooit vanuit het gegenereerde rapport-bestand. Een handmatige correctie die bij Stap 2 in de draft-markdown wordt doorgevoerd, wordt dus **niet** meegenomen door Stap 5 — alleen wijzigingen in de scriptlogica zelf (`classify_entity`/`compute_dekking` in `entiteitendekking.py`) of in BO-frontmatter zelf werken door.

## Totaaloverzicht

`totaaloverzicht.md` bevat een **totaalrij bovenin** de detailtabel met kolomtotalen:

| Maat | Berekening |
|---|---|
| GGM-entiteiten | som kolom GGM-entiteiten |
| Entiteiten met BO | som kolom Entiteiten met BO |
| Entiteiten ondersteunend aan BO | som kolom Entiteiten ondersteunend aan BO |
| Niet gedekt | som kolom Niet gedekt |
| Niet gedekt (%) | Niet gedekt / GGM-entiteiten × 100 |
| BO's zonder GGM-entiteit | som kolom BO zonder GGM-entiteit |
| **BO's totaal** | Entiteiten met BO + BO's zonder GGM-entiteit |

Na het draaien van het script: **verifieer** dat de totaalrij overeenkomt met de kolomsommen. Het script overschrijft `totaaloverzicht.md` bij elke run — handmatige aanpassingen aan de totaalrij moeten na het script worden aangebracht als het script dit nog niet automatisch doet.

## Rapportstructuur

Per taakveld: per beleidsdomein een scriptgegenereerde statistiekregel (totaal, met BO, ondersteunend, niet gedekt, dekkingspercentage) gevolgd door **één samengevoegde tabel**:

`GGM-entiteit | BO / Dekking | Entiteitstype | Naamoverlap | Beoordeling`

De BO/Dekking-kolom toont óf de directe BO-link (`[[BO]] ✅`) óf de indirecte route (`beschrijft`/`via X →`/`typering`/`n.v.t.`/`⚠️ geen BO bereikbaar`/`⚠️ ter discussie tussen [[BO1]] / [[BO2]]`/`generieke bouwsteen`) — een BO-match is structureel gewoon het simpelste geval van dekking, dus geen aparte tabel nodig. `⚠️ ter discussie` betekent: meerdere even-goede kandidaten gevonden, zie Stap 2. Alfabetisch gesorteerd op GGM-entiteitnaam. Naamoverlap toont `synoniem: X` en/of `homoniem: [[Y]]`, samengevoegd uit `bo_synoniemen`/`bo_homoniemen`.

**GGM-hiaten**: BO's zonder GGM-entiteit, met data-object kolom (Terugmelding vs. Alleen BO) — aparte sectie onderaan, ongewijzigd.

RSGBPlus krijgt subsecties per registratie (BRP, BRK, NHR, WOZ, Overig), elk met dezelfde samengevoegde tabel.

## Relatie met andere skills

| Skill | Relatie |
|---|---|
| `/assess-bo` | Levert BO-beoordelingen; entiteitendekking visualiseert het resultaat |
| `/ingest` | Genereert de input (BO's, begrippen); entiteitendekking maakt de analyse achteraf |
| `/domain-status` | Rapporteert voortgang per onderwerp; entiteitendekking rapporteert per beleidsdomein |
| `/generate-ggm` | Ververst BO-frontmatter (`ggm_*`) na een nieuwe GGM-release; entiteitendekking berekent daarna de dekking op basis daarvan |
