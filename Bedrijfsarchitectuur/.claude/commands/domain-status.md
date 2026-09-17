Geef een voortgangsoverzicht voor onderwerp: $ARGUMENTS

Input: `Wiki/` voor het opgegeven onderwerp.
Output: chat — rapporteer, maak geen pagina aan:

1. **Bronnen**: aantal verwerkt (met bronsamenvatting) / beschikbaar in `Sources/`
2. **Begrippen**: aantal in de onderwerpoverzichttabel, verdeling per type
3. **BO's**: aantal, verdeling per grondslag (ggm-entiteit/procesobject/governance-object)
4. **Herleidbaarheid**: hoeveel BO's hebben `bronnen` gevuld, hoeveel niet
5. **GGM-dekking**: aantal GGM-entiteiten in beleidsdomeinen die dit wiki-onderwerp raakt, % gedekt met BO. Verwijs naar het relevante `Wiki/Analyses/entiteitendekking/{taakveld}.md`-rapport voor de volledige analyse per beleidsdomein (entiteitstype, BO-match, hiaten).
6. **Openstaande acties**:
   - Onverwerkte bronnen (in Sources maar geen bronsamenvatting)
   - Begrippen zonder BO-beoordeling in onderwerpoverzicht
   - BO's zonder `bronnen` in frontmatter
   - BO's zonder GGM-velden (ggm_guid ontbreekt)
   - Terugmeldingen richting GGM
