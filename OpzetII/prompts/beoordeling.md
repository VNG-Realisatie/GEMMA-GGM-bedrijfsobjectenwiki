# beoordeling

**Doel:** een kandidaat per type toetsen, een modelleerbesluit formuleren en het element voorstellen; status naar `review`, en na teambesluit de uitkomst verwerken.
**Aanbevolen model:** standaard
**Parameters:** {{kandidaat}} — slug van de kandidaatpagina. Verplicht.
**Benodigde context:** de kandidaatpagina, de typekaders in [../typen/](../typen/), de gekoppelde source-pagina's, [../ontwerp/paginamodel.md](../ontwerp/paginamodel.md) (statusregels).
**Verwachte uitvoer:** volledige kandidaatpagina met status `review`, samenvatting ter bespreking, logregel; na teambesluit de verwerkte status.

## Prompt

Beoordeel kandidaat: {{kandidaat}}

1. **Toets per type** uit de `typen:`-lijst de criteria uit het typekader: vul in de sectie Typeanalyse per type de criteriatabel in — criterium | oordeel | onderbouwing met bronverwijzing. Geen oordeel zonder bron; onzeker = markeren.
2. **Weeg alternatieve typen** met de *Afbakening*-secties van de typekaders: zijn er typen die beter passen of óók van toepassing zijn (multi-type)? Voeg ze toe aan `typen:` en toets ze, of noteer ze onder Alternatieve typen met de reden van afvallen.
3. **Formuleer het modelleerbesluit**: per type `besluit: voorgesteld` of `besluit: afgevallen`, met motivatie in de sectie Modelleerbesluit. Blijft geen type overeind, motiveer waarom dit begrip geen element wordt.
4. **Stel de definitie voor** (frontmatter `definitie:` + sectie): letterlijke bronformulering waar mogelijk, anders eigen synthese — herkomst altijd vermelden.
5. **Stel relaties voor** (frontmatter `relaties:` + tabel): elk met relatietype, doel-element (kandidaat of bestaand GEMMA-element), beschrijving en bron.
6. **Zet status `review`**, log één regel, en **leg een samenvatting voor**: voorgestelde typen, definitie, relaties en de punten van twijfel.
7. **Verwerk daarna het teambesluit** — en alléén een expliciet teambesluit: `goedgekeurd` (besluit per gekozen type → `gekozen`) of `afgewezen` (pagina blijft bestaan met motivatie). Zet deze statussen nooit zelfstandig. Log de statusovergang.

## Voorbeeld

> Beoordeel kandidaat: omgevingsdienst
