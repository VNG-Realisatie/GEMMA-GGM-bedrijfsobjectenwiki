Crawl een webpagina en lever de inhoud op als markdown: $ARGUMENTS

Input: URL(s).
Output: chat; optioneel `Sources/`-bestand op verzoek (zie indelingsregels in CLAUDE.md).

Gebruik de crawl4ai Python-library om de opgegeven URL(s) te crawlen en de inhoud als markdown terug te geven.

## Referentie

Lees eerst het SKILL.md-bestand voor de volledige SDK-referentie:
- Skill-documentatie: /home/mark/ai/shared/crawl4ai/SKILL.md
- Kant-en-klare scripts: /home/mark/ai/shared/crawl4ai/scripts/

## Standaard aanpak

1. Gebruik het basic_crawler.py script voor enkelvoudige pagina's:
   ```bash
   python3 /home/mark/ai/shared/crawl4ai/scripts/basic_crawler.py <URL>
   ```

2. Gebruik batch_crawler.py voor meerdere URL's:
   ```bash
   python3 /home/mark/ai/shared/crawl4ai/scripts/batch_crawler.py <urls-bestand>
   ```

3. Voor complexere situaties (JavaScript-zware pagina's, login, extractie), schrijf een inline Python-script op basis van de patronen in SKILL.md.

## Richtlijnen

- Lever de output op als schone markdown
- Gebruik `css_selector` om alleen de main content te selecteren als de pagina veel navigatie/footer bevat
- Gebruik `excluded_tags=["nav", "footer", "aside"]` om boilerplate te verwijderen
- Bij JavaScript-zware pagina's: gebruik `wait_for` en verhoog `page_timeout`
- Respecteer rate limits: voeg delays toe bij batch-crawls
- De gebruiker kan vragen om de resultaten op te slaan als Sources-bestand — volg dan de indelingsregels uit CLAUDE.md
