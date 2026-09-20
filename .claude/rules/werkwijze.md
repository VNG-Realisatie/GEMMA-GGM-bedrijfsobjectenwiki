# Werkwijze (generiek)

Geldt voor alle wiki's in deze repo. Wiki-specifieke uitwerking: `Bedrijfsarchitectuur/.claude/rules/wiki-conventies.md`.

## Tekst verplaatsen
- [W1] ALS de instructie "verplaats X naar Y" of "splits dit op" is → gebruik de exacte bestaande tekst; alleen knippen en plakken.
- [W2] NOOIT herformuleren, inkorten of "verbeteren" bij [W1].
- [W3] ALLEEN herschrijven ALS de gebruiker dat expliciet vraagt.

## Subagents
- [W4] ALTIJD na subagent-werk cross-cutting updates (gedeelde/centrale bestanden) verifiëren. NOOIT aannemen dat agents die bijwerken; "bestand bestaat + juist format" volstaat niet. Checklist Bedrijfsarchitectuur: [WC22].

## Wetteksten (wetten.overheid.nl)
- [W5] ALS de URL op wetten.overheid.nl staat → NOOIT WebFetch (parafraseert of kort in). Bronbestand bevat de originele tekst.
- [W6] ALTIJD: (1) `curl -sL` → HTML downloaden; (2) Python HTMLParser: navigatie, footer en LiDO-links strippen; (3) wettekst begint bij de eerste "Hoofdstuk"-heading. Vergelijkbaar patroon: [SRC12].
