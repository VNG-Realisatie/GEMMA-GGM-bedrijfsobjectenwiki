# type-extractie

**Doel:** per ArchiMate-elementtype kandidaten identificeren binnen een onderwerp en vastleggen als kandidaatpagina's (status `kandidaat`).
**Aanbevolen model:** standaard
**Parameters:** {{onderwerp}} — topic-slug, verplicht. {{type}} — type-slug uit [../typen/](../typen/), optioneel; leeg = alle `relevante_typen` van het topic die nog niet geëxtraheerd zijn.
**Benodigde context:** de topic-pagina en haar gekoppelde source-pagina's (zo nodig de bronbestanden in `Sources/`), het typekader `../typen/{type}.md`, [../templates/element-candidate.md](../templates/element-candidate.md), `{wiki-root}/kandidaten/` (dedupe).
**Verwachte uitvoer:** stub-kandidaatpagina's, bijgewerkte extractietabel op de topic-pagina, logregels, melding met twijfelgevallen.

## Prompt

Voer type-extractie uit voor onderwerp {{onderwerp}}, elementtype {{type}}.

1. **Pas de herkenningsvragen toe** uit de sectie *Herkenning* van het typekader op elke gekoppelde bron; verzamel een longlist van mogelijke kandidaten met hun vindplaatsen. Werk typegericht: geen generieke begrippenlijst.
2. **Dedupliceer tegen bestaande kandidaten** in `{wiki-root}/kandidaten/`:
   - zelfde begrip bestaat al onder een ander type → voeg een entry toe aan de `typen:`-lijst van die pagina (geen nieuwe pagina);
   - het is een synoniem van een bestaande kandidaat → vul `synoniemen:` aan;
   - alleen werkelijk nieuwe begrippen krijgen een eigen pagina.
3. **Maak per nieuwe kandidaat een stub** volgens [../templates/element-candidate.md](../templates/element-candidate.md): frontmatter (status `kandidaat`, onderwerp, type met leeg `besluit:`), sectie Context (1–2 zinnen) en de eerste vindplaatsen in de bronanalyse.
4. **Werk de extractietabel bij** op de topic-pagina: datum, type, resultaat.
5. **Log** één regel per aangemaakte of aangevulde pagina in `{wiki-root}/log.md`.
6. **Meld** de nieuwe kandidaten, de aanvullingen op bestaande, en apart de twijfelgevallen (wel signaalwoorden, maar onzeker of het een kandidaat is) — die leg je per stuk voor in plaats van er zelfstandig pagina's voor aan te maken.

## Voorbeeld

> Voer type-extractie uit voor onderwerp vergunningverlening-toezicht-handhaving, elementtype business-object.
