# Paginatypes

Elke wiki-pagina heeft YAML-frontmatter en volgt een template.

| Paginatype | Template | Locatie |
|---|---|---|
| Element — bedrijfsobject | [../templates/element.md](../templates/element.md) | `Wiki/Bedrijfsobjecten/{taakveld}/{beleidsdomein}/` |
| Element — actor | [../templates/element.md](../templates/element.md) | `Wiki/Actoren/` (plat) |
| Element — rol | [../templates/element.md](../templates/element.md) | `Wiki/Rollen/` (plat) |
| Onderwerpoverzicht | [../templates/onderwerpoverzicht.md](../templates/onderwerpoverzicht.md) | `Wiki/Onderwerpoverzichten/` |
| Bronsamenvatting | [../templates/bronsamenvatting.md](../templates/bronsamenvatting.md) | `Wiki/Bronsamenvattingen/{onderwerp}/` |
| Analyse | [../templates/analyse.md](../templates/analyse.md) | `Wiki/Analyses/` |
| GGM-bronbestand | — | `Sources/GGM/{taakveld}/` (gegenereerd) |

De beoordelingslogica (wanneer wordt een begrip welk paginatype) staat niet hier maar in de prompts: [../prompts/assess-element.md](../prompts/assess-element.md) (beoordelen) en [../prompts/write-element.md](../prompts/write-element.md) (vastleggen).

## index.md

`Wiki/index.md` is het inhoudelijke overzicht van de hele wiki. Per sectie (Domeinen, Bedrijfsobjecten, Actoren, Rollen, …) één regel per pagina: een link met daarachter een beschrijving van één regel, met status en aantallen waar relevant. Elke prompt die pagina's toevoegt of verwijdert, werkt de index bij.

Voorbeeld van een regel:

```markdown
- [[belastingen|belastingen]] — Gemeentelijke belastingen, heffingen en retributies (afgerond, 11 BO's)
```

## log.md

`Wiki/log.md` is het chronologische logboek, nieuwste bovenaan. Formaat per entry:

```markdown
## [JJJJ-MM-DD] {type} | {korte titel}

- **Aanleiding:** waarom deze actie is uitgevoerd
- {wat er is gedaan, per punt; benoem aantallen en geraakte bestanden}
- **Verificatie:** hoe is gecontroleerd dat het klopt
```

Typen: `ingest`, `fix`, `audit`, `analyse`, `release`. Eén samenvattende entry per actie of sweep — geen entry per gewijzigd bestand.
