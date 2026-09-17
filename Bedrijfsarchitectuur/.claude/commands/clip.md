Verwerk de clipping: $ARGUMENTS

Input: `Clippings/*.md`.
Output: `Sources/{onderwerp}/*.md`.

Stappen:
1. Lees het bestand in `Clippings/`. Als $ARGUMENTS leeg is, toon de bestanden in `Clippings/` en vraag welke.
2. Als het bestand een pdf is, zet deze om naar markdown met **convert_pdf**.
3. Bepaal het onderwerp — volg de indelingsregels in CLAUDE.md § "Bronnen toevoegen".
4. Verplaats naar `Sources/{onderwerp}/{beschrijvende-slug}.md` (lowercase, kebab-case, max 60 tekens).
5. Vul ontbrekende frontmatter aan (description, tags).
6. Meld welk bestand is aangemaakt en stel voor om `/ingest` te starten.

Let op: bronbestanden worden NOOIT vertaald of herschreven. Behoud de originele tekst.
