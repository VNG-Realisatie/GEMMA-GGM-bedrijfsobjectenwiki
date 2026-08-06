# GEMMA online/ — werkregels

Deze map is een lokale, groeiende spiegel van `redactie.gemmaonline.nl` (de MediaWiki-redactieomgeving van het GEMMA-team bij VNG), bedoeld om uiteindelijk naar de echte GEMMA Online-redactieomgeving te publiceren. Alles hieronder geldt voor elke taak binnen `GEMMA online/`.

## 1. Lokaal eerst, wiki alleen op expliciete opdracht

Alles wat voor `GEMMA online/` gemaakt of aangepast wordt, gebeurt eerst in de lokale bestanden (Write/Edit). Pas met een expliciete opdracht van de gebruiker ("zet dit door naar de wiki", "publiceer dit") wordt een wijziging via de mediawiki-mcp-server naar de echte wiki doorgezet (`create-page`/`update-page`/`delete-page`). Lees-tools (`get-page`, `get-pages`, `parse-wikitext`, `search-page`, `search-page-by-prefix`, `get-links-here`, `get-site-info`, `whoami`) blijven altijd vrij te gebruiken voor onderzoek en verificatie.

## 2. Mappenstructuur volgt de GEMMA Online-categorieën

Content wordt georganiseerd in mappen die de categoriehiërarchie (`Categorie:`-namespace op redactie.gemmaonline.nl) volgen, bijv. `GEMMA online/Thema-architecturen/Data/`. Eén hoofdmap per pagina — de map van de meest specifieke/topische categorie; geen duplicatie naar andere categoriemappen, geen frontmatter met de overige categorieën erbij. Een categoriemap wordt pas aangemaakt zodra er daadwerkelijk een pagina in geplaatst wordt — niet vooraf de volledige categorieboom namaken. Bij twijfel over de juiste hoofdcategorie van een (nog niet gepubliceerde) pagina: navragen bij de gebruiker, niet gokken. De mapnaam is de exacte categorienaam (bv. `GEMMA ArchiMedesTemplates`, `SWCAPITemplates`); zusters in de categorieboom worden zustermappen, niet in elkaar genest, tenzij de ene categorie ook echt een subcategorie van de andere is.

Huidige mappen (peildatum 2026-08-06):
```
GEMMA online/
├── GEMMA sjablonen/
│   ├── GEMMA ArchiMedesTemplates/
│   ├── GEMMA ArchiMedesTemplatesObsolete/
│   ├── GEMMA opmaakTemplates/
│   ├── GEMMA publicatieCustomTemplates/
│   └── GEMMA SmartCoreTemplates/
├── SWCAPITemplates/
├── Standaarden paginas/
├── Thema-architecturen/
│   ├── Common Ground/
│   ├── Data/
│   ├── Duurzame toegankelijkheid/
│   ├── Eventorientatie/
│   └── Privacy en Informatiebeveiliging/
└── Toelichtingen/
```

## 3. Geen frontmatter, geen enkele wijziging aan de inhoud

Bestanden zijn en blijven een exacte kopie van de MediaWiki-broncode (wikitext): geen frontmatter, geen herformattering, geen vertaling, geen opschoning. Bij twijfel over correcte overname: `PAGESIZE:<titel>|R` via `parse-wikitext` vergelijken met de lokale bytegrootte (`wc -c`).

## 4. Subpagina's (titel met '/') → geneste mappen, `_index` voor knooppunten

Heeft een wikititel zelf een `/` (MediaWiki-subpagina, bv. `Sjabloon:ToonDomein/Applicatieservices/Tabel`), dan wordt elk segment na de namespace-prefix een echte geneste map. Heeft een pagina zelf ook onderliggende subpagina's (moet dus zowel bestand als map zijn), dan komt haar eigen inhoud in een bestand genaamd `_index` binnen die map.

Voorbeeld:
```
Sjabloon:ToonDomein/_index                              ← inhoud van Sjabloon:ToonDomein zelf
Sjabloon:ToonDomein/Applicatieservices/_index            ← inhoud van .../Applicatieservices
Sjabloon:ToonDomein/Applicatieservices/Tabel             ← leaf, geen eigen subpagina's
```

## 5. Alleen Redactiestatus=Actueel ophalen

Bij het ophalen van onderliggende/gelinkte pagina's van een landingspagina (thema-architectuur e.d.): check eerst de `{{Publicatie|...|Redactiestatus=...}}`-header. Alleen `Actueel` opslaan; `Gearchiveerd` overslaan — niet fetchen, niet opslaan.

## 6. Bekende MCP-tool-eigenaardigheden op deze wiki

`get-category-members` geeft altijd een lege lijst terug op redactie.gemmaonline.nl, ook voor categorieën die overduidelijk gevuld zijn; `search-page` met `incategory:"..."` heeft hetzelfde mankement. Workaround: gebruik `parse-wikitext` met een zelfgeschreven `<categorytree>`: `<categorytree mode="all" depth="3" showcount="on">CategorieNaam</categorytree>` voor subcategorieën/aantallen, `<categorytree mode="pages" depth="1" showcount="on">CategorieNaam</categorytree>` per (sub)categorie voor paginatitels (uit de HTML-links parsen). Dieper dan de opgegeven `depth` blijft ingeklapt (`style="display:none"`) en moet je los opvragen. `get-page`/`get-pages` cappen op 50.000 bytes met een sectiemarker; gebruik `section=N` om de rest op te halen. Prefix-zoeken (`search-page-by-prefix`) met een expliciete `namespace`-parameter werkt betrouwbaarder dan de namespace-prefix (`Categorie:`, `Sjabloon:`) in de `prefix`-string zelf verwerken.

## 7. Namespace-aliassen op deze wiki

`Categorie:` = `Category:` (NS 14), `Sjabloon:` = `Template:` (NS 10). Beide vormen resolven naar dezelfde pagina; geen fout als je het tegenkomt, wel iets om op te letten bij het zoeken naar alle verwijzingen naar een pagina.

## 8. Authenticatie-context

Het account (`MarkBacker`) draait met volle rechten (`sysop`/`bureaucrat`/`interface-admin`, kan aanmaken/bewerken/verplaatsen/uploaden), niet read-only — de bescherming tegen ongewenst schrijven zit alleen in regel 1 hierboven, niet in de accountrechten zelf. `delete-page` vereist bovendien de rechtengroep Beheerders of redacteur, die dit account niet heeft; een aangemaakte pagina die weg moet, kan alleen inert gemaakt worden (lege `<includeonly>`), niet daadwerkelijk verwijderd.
