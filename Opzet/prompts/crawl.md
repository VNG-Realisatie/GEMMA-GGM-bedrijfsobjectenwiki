# crawl

**Doel:** webpagina('s) crawlen en de inhoud opleveren als schone markdown — voor JavaScript-zware of complexe pagina's waar een kale `curl` niet volstaat.
**Aanbevolen model:** standaard
**Parameters:** {{urls}} — één URL of een bestand met meerdere URL's. Verplicht.
**Benodigde context:** ⚠️ **omgevingsafhankelijk** — vereist een lokale installatie van de crawl4ai-bibliotheek met bijbehorende scripts en documentatie (in deze omgeving: `/home/mark/ai/shared/crawl4ai/`, met `SKILL.md` en `scripts/`). Zonder die installatie: gebruik de prompt `fetch` of installeer crawl4ai.
**Verwachte uitvoer:** schone markdown per pagina; desgewenst opgeslagen als bronbestand.

## Prompt

Crawl de webpagina('s) en lever de inhoud op als markdown: {{urls}}

1. Lees eerst de lokale crawl4ai-documentatie (`SKILL.md`) voor de volledige SDK-referentie.
2. Enkelvoudige pagina:
   ```bash
   python3 {crawl4ai-pad}/scripts/basic_crawler.py {{urls}}
   ```
3. Meerdere URL's:
   ```bash
   python3 {crawl4ai-pad}/scripts/batch_crawler.py {urls-bestand}
   ```
4. Complexere situaties (JavaScript-zwaar, login, extractie): schrijf een inline Python-script op basis van de patronen in de documentatie.

Richtlijnen:

- Lever schone markdown op; gebruik `css_selector` voor de hoofdinhoud en `excluded_tags=["nav", "footer", "aside"]` tegen boilerplate.
- Bij JavaScript-zware pagina's: `wait_for` gebruiken en `page_timeout` verhogen.
- Respecteer rate limits: delays bij batch-crawls.
- Wil de gebruiker het resultaat bewaren als bron, volg dan de indelingsregels in [../context/bronnen.md](../context/bronnen.md).

## Voorbeeld

> Crawl de webpagina en lever de inhoud op als markdown: https://www.utrecht.nl/bestuur-en-organisatie/beleid/
