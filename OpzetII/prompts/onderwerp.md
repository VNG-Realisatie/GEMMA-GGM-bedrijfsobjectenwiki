# onderwerp

**Doel:** een topic-pagina aanmaken of bijwerken die bronnen rond een domein groepeert en de extractie-werkeenheid afbakent.
**Aanbevolen model:** standaard
**Parameters:** {{onderwerp}} — naam of slug van het onderwerp. Verplicht.
**Benodigde context:** [../templates/topic.md](../templates/topic.md), [../typen/](../typen/) (voor `relevante_typen`), `{wiki-root}/bronnen/` en `{wiki-root}/onderwerpen/`.
**Verwachte uitvoer:** nieuwe of bijgewerkte topic-pagina, logregel.

## Prompt

Maak of actualiseer de topic-pagina voor: {{onderwerp}}

1. **Controleer bestaand.** Bestaat er al een topic dat dit onderwerp (deels) dekt? Werk dan dat topic bij in plaats van een tweede aan te maken; overlapt het gedeeltelijk, leg de afbakening voor.
2. **Schrijf of actualiseer de pagina** volgens [../templates/topic.md](../templates/topic.md): omschrijving met afbakening, tabel met gekoppelde bronnen (source-pagina + relevantie), relevante termen uit die bronnen.
3. **Schat `relevante_typen` in**: loop de typekaders in [../typen/](../typen/) langs en noteer welke elementtypen in dit onderwerp te verwachten zijn — dit stuurt latere type-extracties.
4. **Wederkerigheid:** zorg dat de gekoppelde source-pagina's dit topic in hun `onderwerpen:` hebben staan.
5. **Log** één regel in `{wiki-root}/log.md`.
6. **Meld** welke extracties voor dit onderwerp nog openstaan (relevante_typen zonder regel in de extractietabel).

## Voorbeeld

> Maak of actualiseer de topic-pagina voor: vergunningverlening, toezicht en handhaving
