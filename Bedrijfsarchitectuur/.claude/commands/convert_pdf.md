Converteer PDF naar Markdown: $ARGUMENTS

Input: PDF-bestand.
Output: markdown-bestand blijft in `{pdf-folder}` staan (via `tools/convert_pdf.py`); de originele PDF verhuist naar `{pdf-folder}/converted_pdf`.

Stappen:
1. Als $ARGUMENTS leeg is, zoek PDF-bestanden in de huidige directory en `Clippings/` en vraag welke.
2. Converteer met: python tools/convert_pdf.py {bestand.pdf}
3. Het markdown-bestand verschijnt naast de originele PDF.
4. Voeg YAML-frontmatter toe bovenaan het geconverteerde markdown-bestand:
   ```yaml
   ---
   title: "{titel uit het document}"
   source: "{directe URL naar het PDF-bestand, als bekend}"
   source_page: "{URL van de webpagina waar de PDF-link op stond, als bekend}"
   author: "{auteur of organisatie}"
   published:
   created: {datum van vandaag}
   description: "{korte beschrijving, max 1 zin}"
   tags:
     - "{domein}"
   ---
   ```
5. Verplaats ALLEEN de originele PDF naar `{pdf-folder}/converted_pdf`. Het markdown-bestand blijft in `{pdf-folder}` staan (niet meeverplaatsen); `converted_pdf/` bevat uitsluitend PDF's.
6. Meld het resultaat.
