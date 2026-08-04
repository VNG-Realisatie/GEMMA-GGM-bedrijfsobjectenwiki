# Conventies

## Taal

Nederlands. Gevestigde Engelse vaktermen (ArchiMate, business object) blijven Engels. Schrijf begrijpelijk: geen jargon tenzij nodig; elk concept moet voor domeinexperts herkenbaar zijn.

## Bestandsnamen

Lowercase met koppeltekens (kebab-case): `onroerende-zaak.md`, `verkiezing.md`. Geen spaties, hoofdletters of haakjes. Bronbestanden: beschrijvende slug, max 60 tekens.

## Links

**Doelconventie:** links moeten klikbaar werken in zowel VS Code als Obsidian. Dat betekent: **markdown-links met een pad relatief ten opzichte van het huidige bestand**, bijvoorbeeld `[Verkiezing](../Bedrijfsobjecten/2-bestuur/verkiezing.md)` (voorbeeldnotatie). Vault-absolute Obsidian-links (`[[Wiki/...]]`) resolven in VS Code verkeerd (relatief aan de huidige note) en creëren daar bij aanklikken een nieuwe pagina.

**Huidige praktijk in de wiki** (geldig totdat de linkconversie uit [../migratie/aanbevelingen.md](../migratie/aanbevelingen.md) is uitgevoerd — de analyse-scripts parsen deze syntax):

- Verwijzingen tussen wiki-pagina's: Obsidian-wiki-links.
- Alle `[[Wiki/...]]`-links (pad ≥ 2 segmenten) krijgen een alias, zodat de lezer een naam ziet en geen pad. In tabellen met escaped pipe: `[[pad\|alias]]`; buiten tabellen: `[[pad|alias]]`.
- Korte links zonder pad hoeven geen alias: `[[Stembureau]]`.
- Uitzondering: links in `## Bronnen`-secties hebben bewust géén alias — het pad maakt expliciet wat voor soort bestand de bron is.
- Verwijzingen naar `Sources/`-bestanden (geen wiki-pagina's): markdown-links.
- Frontmatter: waar een linkveld voorkomt zijn het markdown-links, behalve `bo_relaties.bedrijfsobject` — dat is een gequote wiki-link (zie [../templates/element.md](../templates/element.md)).

## Citaten

Citaten uit bronnen als blockquote (`>`) met bronvermelding. Citaten zijn platte tekst — geen links in geciteerde tekst. Bronnen nooit vertalen of parafraseren in een citaat: letterlijk overnemen.

## Frontmatter-stijl

- Lege waarde: niets na de dubbele punt (`ggm_guid:`) — nooit `""`, `''` of `~`.
- Niet-lege tekstwaarden: dubbele quotes waar nodig of voorgeschreven; nooit enkele quotes.
- Lege lijst: `[]`.

Volledige stijlregels en veldenschema: [../templates/element.md](../templates/element.md).
