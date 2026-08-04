# export

**Doel:** goedgekeurde kandidaten exporteren naar bestanden voor het GEMMA ArchiMate-model, zonder dubbele vastlegging.
**Aanbevolen model:** standaard
**Parameters:** {{scope}} — slug(s) van te exporteren kandidaten, optioneel; leeg = alle kandidaten met status `goedgekeurd` en leeg `export:`-veld.
**Benodigde context:** [../ontwerp/exportmodel.md](../ontwerp/exportmodel.md), `{wiki-root}/kandidaten/`, [../typen/](../typen/) (exportcodes).
**Verwachte uitvoer:** `{wiki-root}/export/{datum}/` met `elementen.csv`, `relaties.csv` en `rapport.md`; gevulde `export:`-velden; logregel.

## Prompt

Exporteer goedgekeurde kandidaten: {{scope}}

1. **Selecteer** de kandidaten binnen de scope met status `goedgekeurd` en leeg `export:`-veld.
2. **Valideer** per kandidaat: minstens één type met `besluit: gekozen`, een gevulde `definitie:`, en bronverwijzingen in de bronanalyse. Onvolledige kandidaten sla je over en vermeld je in het rapport.
3. **Genereer** in `{wiki-root}/export/{jjjj-mm-dd}/` de bestanden volgens [../ontwerp/exportmodel.md](../ontwerp/exportmodel.md):
   - `elementen.csv` — per gekozen type één regel, met de exportcode uit het typekader;
   - `relaties.csv` — alleen relaties waarvan beide uiteinden geëxporteerd/goedgekeurd zijn of een bestaand GEMMA-element betreffen;
   - `rapport.md` — wat is geëxporteerd, welke relaties op de wachtlijst staan (doel nog niet goedgekeurd), wat is overgeslagen en waarom.
4. **Markeer** elke geëxporteerde kandidaat: vul `export:` met datum en bestand.
5. **Log** één regel voor de run in `{wiki-root}/log.md`.
6. **Meld** het resultaat en wijs op de open punten die export raakt (aansluiting op de bestaande CSV-pijplijn; levenscyclus van de pagina na export) — benoemen, niet oplossen.

## Voorbeeld

> Exporteer goedgekeurde kandidaten: omgevingsvergunning
