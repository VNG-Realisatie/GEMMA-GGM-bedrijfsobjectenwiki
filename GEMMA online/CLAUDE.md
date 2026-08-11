# GEMMA online/ — werkregels

Deze map is een lokale, groeiende spiegel van `redactie.gemmaonline.nl` (de MediaWiki-redactieomgeving van het GEMMA-team bij VNG), bedoeld om uiteindelijk naar de echte GEMMA Online-redactieomgeving te publiceren. Alles hieronder geldt voor elke taak binnen `GEMMA online/`.

## 1. Lokaal eerst, wiki alleen op expliciete opdracht

Wijzigingen altijd eerst lokaal (Write/Edit). Pas naar de echte wiki (`create-page`/`update-page`/`delete-page`) na expliciete opdracht — "zet dit door naar de wiki", "publiceer dit". Lees-tools (`get-page`, `get-pages`, `parse-wikitext`, `search-page`, `search-page-by-prefix`, `get-links-here`, `get-site-info`, `whoami`) altijd vrij te gebruiken voor onderzoek en verificatie.

## 2. Mappenstructuur volgt de GEMMA Online-categorieën

Mappen volgen de categoriehiërarchie (`Categorie:`-namespace op redactie.gemmaonline.nl), bijv. `GEMMA online/Thema-architecturen/Data/`. Eén hoofdmap per pagina: de meest specifieke/topische categorie. Geen duplicatie naar andere categoriemappen, geen frontmatter met de overige categorieën erbij. Categoriemap pas aanmaken zodra er echt een pagina in komt — niet vooraf de hele categorieboom namaken. Twijfel over de hoofdcategorie van een nog niet gepubliceerde pagina: navragen bij de gebruiker, niet gokken. Mapnaam = exacte categorienaam (bv. `GEMMA ArchiMedesTemplates`, `SWCAPITemplates`). Zusters in de categorieboom worden zustermappen, niet genest, tenzij de ene categorie ook echt een subcategorie van de andere is.

Huidige mappen (peildatum 2026-08-07):
```
GEMMA online/
├── GEMMA sjablonen/
│   ├── GEMMA ArchiMedesTemplates/
│   ├── GEMMA ArchiMedesTemplatesObsolete/
│   ├── GEMMA opmaakTemplates/
│   ├── GEMMA publicatieCustomTemplates/
│   └── GEMMA SmartCoreTemplates/
├── SmartConnectArchiMate™/
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

Bestanden zijn en blijven een exacte kopie van de MediaWiki-broncode (wikitext): geen frontmatter, geen herformattering, geen vertaling, geen opschoning. Twijfel over correcte overname: `PAGESIZE:<titel>|R` via `parse-wikitext` vergelijken met de lokale bytegrootte (`wc -c`).

## 4. Subpagina's (titel met '/') → geneste mappen, `_index` voor knooppunten

Wikititel met `/` (MediaWiki-subpagina, bv. `Sjabloon:ToonDomein/Applicatieservices/Tabel`): elk segment na de namespace-prefix wordt een echte geneste map. Heeft de pagina zelf ook subpagina's (dus zowel bestand als map nodig): eigen inhoud in een bestand `_index` binnen die map.

Voorbeeld:
```
Sjabloon:ToonDomein/_index                              ← inhoud van Sjabloon:ToonDomein zelf
Sjabloon:ToonDomein/Applicatieservices/_index            ← inhoud van .../Applicatieservices
Sjabloon:ToonDomein/Applicatieservices/Tabel             ← leaf, geen eigen subpagina's
```

## 5. Alleen Redactiestatus=Actueel ophalen

Bij het ophalen van onderliggende/gelinkte pagina's van een landingspagina (thema-architectuur e.d.): eerst de `{{Publicatie|...|Redactiestatus=...}}`-header checken. Alleen `Actueel` opslaan; `Gearchiveerd` overslaan — niet fetchen, niet opslaan.

## 6. Bekende MCP-tool-eigenaardigheden op deze wiki

`get-category-members` geeft altijd een lege lijst terug, ook bij overduidelijk gevulde categorieën; `search-page` met `incategory:"..."` heeft hetzelfde mankement. Workaround: `parse-wikitext` met een zelfgeschreven `<categorytree>`. Voor subcategorieën/aantallen: `<categorytree mode="all" depth="3" showcount="on">CategorieNaam</categorytree>`. Voor paginatitels per (sub)categorie: `<categorytree mode="pages" depth="1" showcount="on">CategorieNaam</categorytree>`, titels uit de HTML-links parsen. Dieper dan de opgegeven `depth` blijft ingeklapt (`style="display:none"`) — apart opvragen. `get-page`/`get-pages` cappen op 50.000 bytes met een sectiemarker; `section=N` voor de rest. Prefix-zoeken (`search-page-by-prefix`): een expliciete `namespace`-parameter werkt betrouwbaarder dan de namespace-prefix (`Categorie:`, `Sjabloon:`) in de `prefix`-string zelf.

## 7. Namespace-aliassen op deze wiki

`Categorie:` = `Category:` (NS 14). `Sjabloon:` = `Template:` (NS 10). Beide vormen resolven naar dezelfde pagina — geen fout als je het tegenkomt, wel iets om op te letten bij het zoeken naar alle verwijzingen naar een pagina.

## 7a. Eigen CSS/JS-pagina's (Gebruiker:.../common.css e.d.) niet via de API te bewerken

`create-page`/`update-page` op de eigen `Gebruiker:MarkBacker/common.css` faalt met `mycustomcssprotected: You do not have permission to edit this CSS page`, ook al heeft het account (zie 8) sysop/bureaucrat/interface-admin-rechten. Vermoedelijk vereist het recht `editmyusercss` een 2FA-geverifieerde sessie die de API-token niet heeft. Workaround: de gebruiker plakt de inhoud zelf in de browser-editor; lokaal wél gewoon eerst wegschrijven zoals altijd (regel 1).

## 8. Authenticatie-context

Het account (`MarkBacker`) draait met volle rechten (`sysop`/`bureaucrat`/`interface-admin`): aanmaken, bewerken, verplaatsen, uploaden — niet read-only. De bescherming tegen ongewenst schrijven zit alleen in regel 1 hierboven, niet in de accountrechten zelf. `delete-page` vereist bovendien de rechtengroep Beheerders of redacteur, die dit account niet heeft; een aangemaakte pagina die weg moet, kan alleen inert gemaakt worden (lege `<includeonly>`), niet daadwerkelijk verwijderd.

## 9. Wikitext-alinea's op één regel, ook in comments

Bij het schrijven of bewerken van wikitext — zichtbare tekst én HTML-comments (`<!-- ... -->`) — staat een alinea altijd op één fysieke regel, nooit handmatig afgebroken. Documentatie (bv. `noinclude`-blokken) staccato houden: korte zinnen, goed leesbaar, niet uitgesponnen.
