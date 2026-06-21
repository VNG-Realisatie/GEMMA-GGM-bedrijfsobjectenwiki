Haal de volgende URL op en sla op als bronbestand: $ARGUMENTS

Stappen:
1. Fetch de pagina met WebFetch. Prompt: "BELANGRIJK: Behoud de ORIGINELE NEDERLANDSE tekst EXACT zoals deze op de pagina staat. Vertaal NIETS naar het Engels. Geef ALLEEN de beschrijvende/inleidende tekst terug die het onderwerp inhoudelijk beschrijft. Laat het volgende WEG: navigatie, breadcrumbs, lijsten met gerelateerde onderwerpen, nieuwsberichten, agendapunten, footer, sidebar, cookie-meldingen, links naar publicaties/brieven. Geef de tekst terug als platte markdown."
2. Bepaal het domein — volg de indelingsregels in CLAUDE.md § "Bronnen toevoegen".
3. Als de pagina links naar bronbestanden heeft (1 level diep):
   - **PDF-bestanden:**
     1. download pdf-bestanden
     2. converteer naar markdown met **convert_pdf**
     3. voeg frontmatter toe aan geconverteerde bestanden met:
        - `source:` directe URL naar het PDF-bestand
        - `source_page:` URL van de webpagina waar de PDF-link op stond
        - overige velden (title, author, created, description, tags) zoals bij de hoofdpagina
   - **HTML-pagina's** (beleidsdocumenten, regelgeving, etc.):
     1. fetch elke gelinkte pagina met WebFetch (zelfde prompt als stap 1)
     2. sla elk op als apart bronbestand met:
        - `source:` directe URL van de gelinkte pagina
        - `source_page:` URL van de webpagina waar de link op stond
        - overige velden (title, author, created, description, tags) zoals bij de hoofdpagina
4. Sla op als `Sources/{domein}/{beschrijvende-slug}.md` (lowercase, kebab-case, max 60 tekens).
5. Voeg frontmatter toe:
   ```yaml
   ---
   title: "{titel van de pagina}"
   source: "{originele URL}"
   author: "{auteur of organisatie}"
   published:
   created: {datum van vandaag}
   description: "{korte beschrijving, max 1 zin}"
   tags:
     - "{domein}"
   ---
   ```
6. Meld welk bestand is aangemaakt en stel voor om `/ingest` te starten.
