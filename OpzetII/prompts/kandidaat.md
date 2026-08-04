# kandidaat

**Doel:** de bronanalyse van een kandidaat volledig uitwerken: van stub naar beoordeelbare pagina.
**Aanbevolen model:** standaard
**Parameters:** {{kandidaat}} — slug van de kandidaatpagina. Verplicht.
**Benodigde context:** de kandidaatpagina, de source-pagina's van alle gekoppelde onderwerpen (zo nodig de bronbestanden in `Sources/`), [../templates/element-candidate.md](../templates/element-candidate.md).
**Verwachte uitvoer:** kandidaatpagina met gevulde secties Context en Bronanalyse, gemarkeerde open vragen, logregel.

## Prompt

Werk de bronanalyse uit voor kandidaat: {{kandidaat}}

1. **Loop alle bronnen langs** van de gekoppelde onderwerpen — ook bronnen die bij de extractie niet de vindplaats waren kunnen het begrip noemen. Vind je het begrip in een onderwerp dat nog niet gekoppeld is, vul `onderwerpen:` aan.
2. **Vul de bronanalyse**: per bron een link naar de source-pagina met de relevante passages (verwijzing of kort letterlijk citaat met plaatsaanduiding), gevonden termen en synoniemen. Vul `synoniemen:` in de frontmatter aan.
3. **Schrijf de context**: het begrip in gewone taal, op het niveau waarop de bronnen erover praten.
4. **Markeer open vragen** die de bronnen niet beantwoorden (bijv. onduidelijke afbakening, ontbrekende levenscyclus-informatie) — markeren, niet gokken.
5. **Controleer op samenval**: blijkt het begrip tijdens de uitwerking samen te vallen met een andere kandidaat, leg dat voor voordat je samenvoegt.
6. **Log** één regel in `{wiki-root}/log.md`.
7. **Meld** dat de kandidaat gereed is voor beoordeling (prompt [beoordeling.md](beoordeling.md)), met de open vragen.

## Voorbeeld

> Werk de bronanalyse uit voor kandidaat: toezichthouder
