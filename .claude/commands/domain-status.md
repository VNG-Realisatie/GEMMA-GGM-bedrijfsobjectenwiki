Geef een voortgangsoverzicht voor domein: $ARGUMENTS

Rapporteer in chat (maak geen pagina aan):

1. **Bronnen**: aantal verwerkt (met bronsamenvatting) / beschikbaar in `Sources/`
2. **Begrippen**: aantal in de domeinoverzichttabel, verdeling per type
3. **BO's**: aantal, verdeling per grondslag (ggm-entiteit/procesobject/governance-object)
4. **Herleidbaarheid**: hoeveel BO's hebben `bronnen` gevuld, hoeveel niet
5. **GGM-dekking**: aantal entiteiten in GGM voor dit domein (uit `Sources/GGM-repository/ggm_parsed.json`), % met BO, hoeveel met `ggm_gemma_guid`
6. **Openstaande acties**:
   - Onverwerkte bronnen (in Sources maar geen bronsamenvatting)
   - Begrippen zonder BO-beoordeling in domeinoverzicht
   - BO's zonder `bronnen` in frontmatter
   - BO's zonder GGM-velden (ggm_guid ontbreekt)
   - Terugmeldingen richting GGM
