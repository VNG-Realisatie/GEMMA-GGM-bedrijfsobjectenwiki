# fetch

**Doel:** een URL ophalen als exacte kopie en opslaan als bronbestand in `Sources/`.
**Aanbevolen model:** licht
**Parameters:** {{url}} — de op te halen URL. Verplicht.
**Benodigde context:** [../context/bronnen.md](../context/bronnen.md) (indelingsregels en frontmatter-schema), `Sources/Onderwerpen/` (bestaande onderwerpmappen), `ToDo/ingest-backlog.md`.
**Verwachte uitvoer:** één of meer bronbestanden in `Sources/Onderwerpen/{onderwerp}/` met frontmatter; bijgewerkte backlog; voorstel om een ingest te starten.

## Prompt

Haal de volgende URL op en sla op als bronbestand: {{url}}

1. **Haal de pagina op met `curl`** — gebruik géén ingebouwde fetch-functie van de tool die de inhoud samenvat of parafraseert. Bronbestanden zijn een exacte kopie van de originele tekst.
   ```bash
   curl -sL '{{url}}' -o /tmp/fetch-page.html
   ```
   Converteer de HTML naar markdown met een eenvoudige HTML-parser (bijv. Python `HTMLParser`):
   - strip `<script>`, `<style>`, `<nav>`, `<footer>`;
   - headings `<h1>`–`<h4>` → `#`–`####`; `<p>` → dubbele newline; `<li>` → `- `; `<br>` → newline; alle overige tekst letterlijk bewaren;
   - verwijder navigatieruis (bijv. "Toon relaties in LiDO", "Maak een permanente link", "Toon wetstechnische informatie", lege bullets);
   - knip de footer af bij markers als "Permanente link naar versie", "Over deze website";
   - voor wetten.overheid.nl: de wettekst begint bij de eerste `### Hoofdstuk`-heading — alles daarvoor weglaten;
   - normaliseer witruimte (max 2 opeenvolgende newlines, max 1 spatie).
2. **Bepaal het onderwerp** volgens de indelingsregels in [../context/bronnen.md](../context/bronnen.md).
3. **Gelinkte bronbestanden** (1 niveau diep): PDF's downloaden met `curl` en converteren via de prompt `convert-pdf`; gelinkte HTML-beleidspagina's ophalen met dezelfde methode als stap 1. Elk krijgt een eigen bronbestand met `source:` (directe URL) en `source_page:` (de pagina waar de link stond).
4. **Sla op** als `Sources/Onderwerpen/{onderwerp}/{beschrijvende-slug}.md` (lowercase, kebab-case, max 60 tekens). Geconverteerde PDF's verplaats je met `mv` en vul je alleen aan met frontmatter — schrijf nooit de volledige inhoud opnieuw.
5. **Voeg frontmatter toe** volgens het schema in [../context/bronnen.md](../context/bronnen.md).
6. **Werk `ToDo/ingest-backlog.md` bij** — bestaand onderwerp: toevoegen aan de sectie; nieuw onderwerp: nieuwe sectie.
7. **Meld** welk bestand is aangemaakt en stel voor een ingest te starten (prompt `ingest`).

## Voorbeeld

> Haal de volgende URL op en sla op als bronbestand: https://vng.nl/publicaties/position-paper-dierenwelzijn
