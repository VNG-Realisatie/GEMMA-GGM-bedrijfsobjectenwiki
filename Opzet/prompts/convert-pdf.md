# convert-pdf

**Doel:** een PDF converteren naar een markdown-bronbestand met frontmatter — altijd via het conversiescript, nooit door de PDF visueel over te typen.
**Aanbevolen model:** standaard
**Parameters:** {{pdf}} — pad naar het PDF-bestand; optioneel (leeg = zoek PDF's in de huidige map en `Clippings/` en vraag welke).
**Benodigde context:** [../tools/README.md](../tools/README.md), [../context/bronnen.md](../context/bronnen.md).
**Verwachte uitvoer:** een markdown-bestand met frontmatter naast de originele PDF; de verwerkte PDF verplaatst naar een `converted_pdf/`-submap.

## Prompt

Converteer PDF naar markdown: {{pdf}}

1. Is er geen bestand opgegeven, zoek dan PDF's in de huidige map en `Clippings/` en vraag welke.
2. Converteer met:
   ```bash
   python3 tools/convert_pdf.py {{pdf}}
   ```
   Het markdown-bestand verschijnt naast de originele PDF. Typ de PDF nooit visueel over — het script is de enige route.
3. Voeg YAML-frontmatter toe bovenaan het geconverteerde bestand, volgens het schema in [../context/bronnen.md](../context/bronnen.md) (met `source:` = directe PDF-URL en `source_page:` = pagina waar de link stond, indien bekend).
4. Verplaats de verwerkte PDF naar `{pdf-map}/converted_pdf/`.
5. Meld het resultaat.

## Voorbeeld

> Converteer PDF naar markdown: `Clippings/kadernota-2026.pdf`
