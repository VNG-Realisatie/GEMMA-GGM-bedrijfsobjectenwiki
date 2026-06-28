---
model: haiku
---

Haal de volgende URL op en sla op als bronbestand: $ARGUMENTS

Stappen:
1. **Fetch de pagina met `curl`** — gebruik NOOIT WebFetch. Bronbestanden moeten een exacte kopie van de originele tekst zijn, geen samenvatting.
   ```bash
   curl -sL '{url}' -o /tmp/fetch-page.html
   ```
   Converteer de HTML naar markdown met een Python HTMLParser:
   - Strip `<script>`, `<style>`, `<nav>`, `<footer>` tags
   - Converteer headings (`<h1>`–`<h4>`) naar markdown `#`–`####`
   - Converteer `<p>` naar dubbele newline, `<li>` naar `- `, `<br>` naar newline
   - Bewaar alle overige tekst letterlijk
   - Verwijder navigatie-ruis: "Toon relaties in LiDO", "Maak een permanente link", "Toon wetstechnische informatie", "Druk het regelingonderdeel af", "Sla het regelingonderdeel op", losse bullets (`- ...`, `- ` zonder tekst)
   - Knip footer af bij markers als "Permanente link naar versie", "Exporteer regeling", "Keuze afdrukken", "Over deze website"
   - Voor wetten.overheid.nl: de wettekst begint bij de eerste `### Hoofdstuk` heading; alles daarvoor (inhoudsopgave, zoekbalk) weglaten
   - Normaliseer witruimte: max 2 opeenvolgende newlines, max 1 spatie
2. Bepaal het onderwerp — volg de indelingsregels in CLAUDE.md § "Bronnen toevoegen".
3. Als de pagina links naar bronbestanden heeft (1 level diep):
   - **PDF-bestanden:**
     1. download pdf-bestanden met `curl`
     2. converteer naar markdown met **convert_pdf**
     3. voeg frontmatter toe aan geconverteerde bestanden met:
        - `source:` directe URL naar het PDF-bestand
        - `source_page:` URL van de webpagina waar de PDF-link op stond
        - overige velden (title, author, created, description, tags) zoals bij de hoofdpagina
   - **HTML-pagina's** (beleidsdocumenten, regelgeving, etc.):
     1. fetch elke gelinkte pagina met `curl` + HTML-extractie (zelfde methode als stap 1)
     2. sla elk op als apart bronbestand met:
        - `source:` directe URL van de gelinkte pagina
        - `source_page:` URL van de webpagina waar de link op stond
        - overige velden (title, author, created, description, tags) zoals bij de hoofdpagina
4. Sla op als `Sources/{onderwerp}/{beschrijvende-slug}.md` (lowercase, kebab-case, max 60 tekens).
   - **Bij geconverteerde PDF's:** verplaats het .md-bestand met `mv` naar de doellocatie, voeg daarna alleen de frontmatter toe met Edit. Schrijf nooit de volledige inhoud opnieuw via Write.
   - **Bij HTML-pagina's:** schrijf frontmatter + geëxtraheerde body naar het doelbestand.
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
     - "{onderwerp}"
   ---
   ```
6. **Update `Bedrijfsarchitectuur/ToDo/ingest-backlog.md`** — als de bron bij een bestaand onderwerp hoort, voeg het toe aan de juiste sectie. Als het onderwerp nieuw is, maak een nieuwe sectie aan.
7. Meld welk bestand is aangemaakt en stel voor om `/ingest` te starten.
