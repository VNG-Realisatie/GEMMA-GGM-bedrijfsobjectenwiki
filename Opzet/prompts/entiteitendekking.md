# entiteitendekking

**Doel:** de uniforme GGM-dekkingsrapportage genereren of verversen: per taakveld/beleidsdomein welke entiteiten BO zijn, welke niet (met entiteitstype en relatie tot een BO), en welke BO's geen GGM-grondslag hebben.
**Aanbevolen model:** standaard
**Parameters:** {{taakveld}} — taakveldnummer; optioneel (leeg = alle taakvelden).
**Benodigde context:** [../tools/README.md](../tools/README.md), `Wiki/Analyses/entiteitendekking/`, `Wiki/GGM/`, de BO-pagina's in scope.
**Verwachte uitvoer:** verse per-taakveldrapporten + totaaloverzicht + reviewlijst; beoordeelde review-items; gesynchroniseerde BO-frontmatter (`analyse_ggm_dekking`); bijgewerkte index/log.

## Prompt

Genereer of ververs de entiteitendekking-rapportage voor: {{taakveld}}

**Stap 1: Script draaien.**

```bash
python3 tools/entiteitendekking.py --all              # alle taakvelden
python3 tools/entiteitendekking.py --taakveld {{taakveld}}
python3 tools/entiteitendekking.py --all --dry-run    # alleen tellingen
```

Het script genereert in `Wiki/Analyses/entiteitendekking/`: per-taakveldrapporten, `totaaloverzicht.md` en `review.md`.

**Stap 2: Review.** `review.md` bevat twee soorten items, niet te verwarren:

1. **`confidence=low`** — de classificatie is onzeker; controleer het gesuggereerde entiteitstype en pas aan waar nodig.
2. **`⚠️ ter discussie tussen {BO1} / {BO2}`** — een structurele ambiguïteit: meerdere even goede kandidaat-BO's; het script kiest bewust niet. Dit is een inhoudelijke keuze voor een mens. Werkwijze: lees de GGM-definitie en vergelijk met elke kandidaat; kies de best passende BO (of laat het staan als geen kandidaat past); registreer de keuze in de frontmatter van de gekozen BO onder `bo_via_kandidaten`; draai stap 1 opnieuw — de keuze is dan permanent. Triage eerst bij veel items; forceer geen keuze.

**Stap 3: Beoordeling verrijken.** Vervang in elk per-taakveldrapport de `<!-- REVIEW -->`-marker in de `## Beoordeling`-sectie door interpretatie: structurele patronen, functionele dekking, cross-domeinobservaties, naamconflicten. **Herhaal geen tellingen of per-entiteitdetail** — die staan al in de scriptgegenereerde statistiekregels en blijven bij her-runs vers, in tegenstelling tot deze prozasectie.

**Stap 4: Afronden.** `Wiki/index.md` en `Wiki/log.md` bijwerken.

**Stap 5: BO-frontmatter synchroniseren** (bewust een losse stap, zodat versiebeheer toont of een run alleen `Wiki/Analyses/` raakte of ook BO-pagina's):

```bash
python3 tools/entiteitendekking_sync_bo.py --dry-run   # preview
python3 tools/entiteitendekking_sync_bo.py             # schrijven
```

Dit schrijft `analyse_ggm_dekking` (de omgekeerde index: welke GGM-entiteiten dekt dit BO) chirurgisch terug naar BO-pagina's — alleen dat veld. Let op: dit script herberekent altijd vanuit de brondata; handmatige correcties in rapport-markdown werken er niet in door — alleen wijzigingen in BO-frontmatter of scriptlogica.

**Spelregels van het rapport:**

- **n.v.t. telt niet mee in het dekkingspercentage** (noemer = GGM-entiteiten − n.v.t.): abstract/proces/meetinstrument/cross-cutting-entiteiten zijn bewust nooit matchkandidaat.
- **Actoren en rollen zijn géén n.v.t.**: ze matchen op pagina's in `Wiki/Actoren/`/`Wiki/Rollen/` via `ggm_guid`. Ongematchte actor/rol-entiteiten tellen als niet gedekt en verschijnen in de review. Alleen na menselijke beoordeling buiten scope geplaatste actoren/rollen (extern perspectief) worden n.v.t. — registreer die in de `NVT_ACTOR_ROL`-set in `tools/entiteitendekking.py` zodat de curatie her-runs overleeft. Vergelijk bij vóór/na-analyses absolute aantallen: een groeiende noemer kan het percentage laten dalen zonder inhoudelijke achteruitgang.
- Verifieer na de run dat de totaalrij in `totaaloverzicht.md` klopt met de kolomsommen.

## Voorbeeld

> Genereer of ververs de entiteitendekking-rapportage voor: taakveld 9 (Interne Organisatie)
