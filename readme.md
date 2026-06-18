# GEMMA-GGM bedrijfsobjectenwiki

| Eigenaar | Ingevuld door |
|---------|----------------|
| Kennis Centrum Architectuur | Mark Backer |

Deze repository bevat een door LLM's onderhouden kenniswiki voor het identificeren, structureren en modelleren van begrippen en bedrijfsobjecten binnen het gemeentelijk domein. De repository is ingericht voor gebruik met Obsidian, waardoor relaties tussen domeinen, begrippen, bronnen en bedrijfsobjecten eenvoudig kunnen worden verkend.

## Doel

Het doel van deze repository is om op basis van de entiteiten van het Gemeentelijk Gegevensmodel (GGM) te komen tot een GEMMA bedrijfsobjectmodel. Op basis van uit gemeentelijke (beleids)documenten geëxtraheerde kennis worden bedrijfsobjecten afgeleid en vervolgens gematcht met GGM-entiteiten.

Hierdoor ontstaat een bedrijfsobjectmodel dat consistent is met het GGM, maar niet beperkt is tot de bestaande entiteiten. Entiteiten kunnen worden weggelaten of samengevoegd wanneer dit semantisch beter past, en er kunnen nieuwe bedrijfsobjecten worden toegevoegd wanneer hiervoor geen directe GGM-entiteit bestaat.

## Opzet

De map `Sources` bevat de bronmaterialen en wordt beschouwd als immutabel. Deze bestanden dienen uitsluitend als referentie voor analyse en modellering. Het GGM binnen `Sources/GGM` is een leesbare representatie van het bronmodel en vormt de referentie voor het mappen van begrippen en objecten.

De map `Wiki` bevat de afgeleide kennisbasis met domeinoverzichten, begrippen, bedrijfsobjecten, bronsamenvattingen en analyses. Nieuwe inzichten worden hier vastgelegd, gekoppeld en verder verrijkt op basis van de beschikbare bronnen.

De repository ondersteunt kennisopbouw, begrippenharmonisatie en de ontwikkeling van gemeentelijke bedrijfsarchitectuur op basis van herleidbare beleidsbronnen.

## Achtergrond

De opzet van deze repository is geïnspireerd op het concept van een LLM-onderhouden wiki zoals beschreven in `llm-wiki.md`. Dit document bevat het oorspronkelijke idee van een kennisbasis die door een taalmodel wordt opgebouwd en verrijkt op basis van bronmateriaal. In deze repository is dat concept toegepast op gemeentelijke beleidsinformatie, begrippenmodellering en bedrijfsarchitectuur.
## Licentie

Deze repository wordt beschikbaar gesteld onder de EUPL 1.2 (European Union Public Licence).