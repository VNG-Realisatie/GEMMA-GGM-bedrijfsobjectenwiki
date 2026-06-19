---
type: bedrijfsobject
naam: Inburgeringstraject
domein: [Asiel en Integratie]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Inburgeringstraject
ggm_beleidsdomein: Inburgering
ggm_diagram: Inburgering
ggm_definitie: "Een Inburgeringstraject in de context van inburgering bij gemeenten is een persoonlijk begeleidingstraject dat nieuwkomers ondersteunt bij het leren van de Nederlandse taal, het begrijpen van de samenleving, en het ontwikkelen van vaardigheden om zelfstandig te participeren in de Nederlandse maatschappij. Het traject omvat doorgaans onderdelen zoals taallessen (NT2), kennis van de Nederlandse maatschappij (KNM), en participatieactiviteiten, zoals vrijwilligerswerk of een werkstage. Het inburgeringstraject wordt afgestemd op de behoeften, achtergrond en mogelijkheden van de nieuwkomer en heeft als doel hen te begeleiden naar maatschappelijke zelfredzaamheid en een actieve rol in de samenleving."
gemma_definitie: "gelijk aan GGM"
gerelateerde_begrippen: [inburgering]
relaties:
  - type: associatie
    bedrijfsobject: PIP
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Wordt aangestuurd door het PIP"
  - type: associatie
    bedrijfsobject: Leerroute
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Bevat een leerroute"
  - type: associatie
    bedrijfsobject: Examen
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Wordt afgesloten met examens"
---

# Inburgeringstraject

Persoonlijk begeleidingstraject dat nieuwkomers ondersteunt bij het leren van de Nederlandse taal, het begrijpen van de samenleving en het ontwikkelen van vaardigheden voor zelfstandige participatie.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus
- ✅ Heeft relaties met andere concepten

## GGM-bron

> Een Inburgeringstraject in de context van inburgering bij gemeenten is een persoonlijk begeleidingstraject dat nieuwkomers ondersteunt bij het leren van de Nederlandse taal, het begrijpen van de samenleving, en het ontwikkelen van vaardigheden om zelfstandig te participeren in de Nederlandse maatschappij. Het traject omvat doorgaans onderdelen zoals taallessen (NT2), kennis van de Nederlandse maatschappij (KNM), en participatieactiviteiten, zoals vrijwilligerswerk of een werkstage. Het inburgeringstraject wordt afgestemd op de behoeften, achtergrond en mogelijkheden van de nieuwkomer en heeft als doel hen te begeleiden naar maatschappelijke zelfredzaamheid en een actieve rol in de samenleving.

- **Entiteit:** Inburgeringstraject
- **Beleidsdomein:** Inburgering (taakveld 6 — Sociaal Domein)
- **Attributen:** UitkomstLeerbaarheidstoets
- **Matchsterkte:** exact

## Relaties

- ← [[pip]] — wordt aangestuurd door het PIP [1]
- → [[leerroute]] — bevat een leerroute [1]
- → [[examen]] — wordt afgesloten met examens [0..*]
