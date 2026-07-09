---
type: element
naam: Schuldeiser
onderwerp: [schulden en armoede]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Schuldeiser
ggm_guid: EAID_DCDAD212_479E_4fc3_B886_585AE57D8C21
ggm_uml_type: Class
ggm_beleidsdomein: Schuldhulpverlening
ggm_taakveld: "Schulden"
ggm_diagram: [Schuldhulp Client]
ggm_definitie: "Een schuldeiser is bedrijf of persoon die recht heeft op een prestatie van een ander, de schuldenaar. In de meeste gevallen is de prestatie het betalen van geld."
ggm_herkomst: GGM

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Schuldeiser** als directe tegenhanger.
bo_definitie: "Een schuldeiser is bedrijf of persoon die recht heeft op een prestatie van een ander, de schuldenaar. In de meeste gevallen is de prestatie het betalen van geld."
bo_toelichting:
bo_subtypes: []
element_tegenhangers:
  - element: "[[Wiki/Actoren/schuldeiser|Schuldeiser (actor)]]"
    archimate_type: business-actor
    toelichting: "Dit bedrijfsobject legt de gegevens vast over de gelijknamige actor."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[schuld]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Schuldeiser heeft een of meer schulden"
bedrijfsprocessen: [schuldhulpverlening, collectief schuldregelen]
bedrijfsfuncties: [financiële hulpverlening]
---

## BO-criteria toetsing

6/6 criteria. Actor met eigen registratie (naam, peildatum), meerdere per traject, eigen levenscyclus (wordt geïdentificeerd, benaderd, akkoord/weigering). Herkenbaar voor elke schuldhulpverlener.

## Beschrijving

Een schuldeiser is een bedrijf of persoon aan wie de inwoner geld verschuldigd is. De meest voorkomende schuldeisers zijn de Belastingdienst (meest voorkomend) en zorgverzekeraars (op twee). De gemeente onderhandelt namens de inwoner met schuldeisers over schuldregelingen.

De handelende kant van dit begrip is vastgelegd als actor [[Wiki/Actoren/schuldeiser|Schuldeiser (actor)]].

Via **collectief schuldregelen** (Haagse innovatie, landelijk opgeschaald) geven schuldeisers vooraf akkoord op betaalvoorstellen. Deelnemers zijn o.a. Belastingdienst, CAK, CJIB, DUO, banken en verzekeraars.

## GGM-bron

> "Een schuldeiser is bedrijf of persoon die recht heeft op een prestatie van een ander, de schuldenaar."

- **Entiteit:** Schuldeiser (specialisatie van Rechtspersoon)
- **Beleidsdomein:** Schuldhulpverlening
- **Attributen:** peildatum, naam
- **Matchsterkte:** exact

## Relaties

| Type | Bedrijfsobject | Kardinaliteit | Beschrijving |
|---|---|---|---|
| associatie | [[schuld\|Schuld]] | 0..* | Schuldeiser bij schulden |

## Bronnen
- [[Wiki/Bronsamenvattingen/Schulden en Armoede/beleidsplan-schuldhulpverlening-den-haag-2024-2028]]
