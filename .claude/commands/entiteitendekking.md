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

Lees `review.md`. Dit bevat entiteiten met `confidence=low` — classificatie onzeker. Per item: controleer het gesuggereerde entiteitstype en pas aan in de draft als nodig.

### Stap 3: Beoordeling verrijken

Elk per-taakveld rapport heeft een `## Beoordeling` sectie bovenin met `<!-- REVIEW -->` marker. Vervang met inhoudelijke beoordeling:

- Structurele patronen (welke typen entiteiten worden geen BO en waarom)
- Functionele dekking (wat ontbreekt inhoudelijk in het GGM)
- Cross-domein observaties
- Naamconflicten en disambiguatie

### Stap 4: Afronden

1. Update `Wiki/index.md` met de nieuwe analyse-pagina's
2. Voeg entry toe aan `Wiki/log.md`

## Rapportstructuur

Per taakveld: secties per beleidsdomein, elk met drie tabellen:

**BO-matches**: GGM-entiteit → BO, met entiteitstype en naamoverlap (homoniemen/synoniemen uit BO-frontmatter)

**Geen BO-match**: entiteitstype + Relatie tot BO (subtype van/compositie van/associatie →/typering van/via X →)

**GGM-hiaten**: BO's zonder GGM-entiteit, met data-object kolom (Terugmelding vs. Alleen BO)

RSGBPlus krijgt subsecties per registratie (BRP, BRK, NHR, WOZ, Overig).

## Relatie met andere skills

| Skill | Relatie |
|---|---|
| `/assess-bo` | Levert BO-beoordelingen; entiteitendekking visualiseert het resultaat |
| `/ingest` | Genereert de input (BO's, begrippen); entiteitendekking maakt de analyse achteraf |
| `/domain-status` | Rapporteert voortgang per onderwerp; entiteitendekking rapporteert per beleidsdomein |
