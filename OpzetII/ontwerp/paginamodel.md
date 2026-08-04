# Paginamodel

Drie permanente paginatypen. Templates: [../templates/](../templates/); ingevulde voorbeelden: [../voorbeelden/](../voorbeelden/).

| Paginatype | Locatie | Bevat | Bevat níet |
|---|---|---|---|
| **source** | `{wiki-root}/bronnen/` | metadata, bronlocatie, samenvatting, relevante passages, onderwerpkoppeling | ArchiMate-analyse |
| **topic** | `{wiki-root}/onderwerpen/` | omschrijving, gekoppelde bronnen, relevante termen, relevante elementtypen, extractietabel | elementdefinities |
| **element-candidate** | `{wiki-root}/kandidaten/` | bronanalyse, typeanalyse, alternatieve typen, modelleerbesluit, voorgestelde definitie en relaties, status | definitieve registratie (die staat in GEMMA) |

De element-candidate is de **centrale analysepagina**: er is geen aparte permanente analysepagina naast een elementpagina — analyse en voorstel staan op één pagina, per begrip precies één.

## Statuscyclus

```
                    ┌──▶ goedgekeurd ──▶ (export naar GEMMA)
kandidaat ──▶ review┤
                    └──▶ afgewezen
```

| Overgang | Wanneer | Wie |
|---|---|---|
| → `kandidaat` | aanmaak bij type-extractie (stap 3) | LLM, zelfstandig |
| `kandidaat` → `review` | bronanalyse én typeanalyse compleet, voorstel geformuleerd (stap 5) | LLM, na uitvoeren beoordeling |
| `review` → `goedgekeurd` | expliciet teambesluit | mens beslist; LLM verwerkt |
| `review` → `afgewezen` | expliciet teambesluit | mens beslist; LLM verwerkt |
| `review` → `kandidaat` | beoordeling blijkt onvolledig, terug voor aanvulling | LLM of mens |

Regels:

- De status staat uitsluitend in de frontmatter van de kandidaatpagina — nergens anders bijgehouden; overzichten worden gegenereerd.
- **Afgewezen kandidaten blijven bestaan**, met de motivatie in het modelleerbesluit. Zo is naspeurbaar wat al beoordeeld is en waarom, en wordt hetzelfde begrip niet opnieuw geanalyseerd.
- Na `goedgekeurd` volgt export (stap 6); de pagina krijgt een `export:`-markering. De verdere levenscyclus van de pagina ná export is een open punt — zie [open-punten.md](open-punten.md).

## Meerdere typen per kandidaat

Eén begrip kan meerdere ArchiMate-typen opleveren — een inwoner is bijvoorbeeld een actor of rol én een bedrijfsobject (er wordt informatie over vastgelegd). Dat blijft **één kandidaatpagina**:

- de frontmatter-lijst `typen:` bevat per overwogen type een entry met een `besluit:`-veld: leeg (nog niet beoordeeld) → `voorgesteld` of `afgevallen` (beoordeling) → `gekozen` (na goedkeuring);
- de typeanalyse-sectie bevat per type een eigen criteriatoetsing;
- bij export ontstaat per gekozen type een eigen ArchiMate-element.

Een pagina is `afgewezen` wanneer geen enkel type overeind blijft; `goedgekeurd` zodra ten minste één type is gekozen (afgevallen typen blijven met motivatie op de pagina staan).

## Linkconventie

- Alle verwijzingen tussen wiki-pagina's zijn **relatieve markdown-links** (`[vth-beleidsplan](../bronnen/vth-beleidsplan.md)`) — klikbaar in VS Code én Obsidian. Geen `[[wiki-links]]`.
- Citaten uit bronnen: blockquote met plaatsaanduiding (paragraaf/pagina), platte tekst, geen links in het citaat.
- Verwijzingen naar bestaande GEMMA-elementen: bij naam, met waar beschikbaar de GEMMA Online-URL.
