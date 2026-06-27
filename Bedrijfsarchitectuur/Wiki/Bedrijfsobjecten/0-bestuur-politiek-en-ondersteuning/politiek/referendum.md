---
type: bedrijfsobject
naam: Referendum
domein:
- Bestuur
archimate_type: business-object
grondslag: procesobject
ggm_entiteit: '~'
ggm_beleidsdomein: Politiek (niet expliciet gemodelleerd)
ggm_guid: ''
ggm_uml_type: ''
ggm_taakveld: ''
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: '~'
ggm_toelichting: ''
ggm_synoniemen: ''
ggm_herkomst: ''
ggm_gemma_naam: ''
ggm_gemma_guid: ''
ggm_gemma_definitie: ''
ggm_gemma_toelichting: ''
ggm_gemma_synoniemen: ''
ggm_gemma_type: ''
ggm_gemma_url: ''
ggm_gemma_bron: ''
ggm_gemma_alternate_name: ''
bo_definitie: Volksstemming over een onderwerp, ingesteld door de raad of op grond van burgerbetrokkenheid, georganiseerd en uitgevoerd door de gemeente.
bedrijfsprocessen: ''
bedrijfsfuncties: ''
bo_relaties:
- type: compositie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/politiek/stembureau|Stembureau]]'
  richting: van-dit-BO
  kardinaliteit: 1..*
  beschrijving: Referendum wordt afgestemd via dezelfde stembureaus als verkiezingen
- type: associatie
  bedrijfsobject: Onderwerp
  richting: naar-dit-BO
  kardinaliteit: 1
  beschrijving: Referendum behandelt een specifiek beleidsonderwerp
---

# Referendum

## BO-criteria toetsing

| Criterium | Van toepassing? | Opmerkingen |
|---|---|---|
| Betekenis binnen domein | ✅ | Vorm van burgerbetrokkenheid en directe democratie |
| Herkenbaar voor experts | ✅ | Gemeenteraadsleden, wethouders, burgers kennen referenda |
| Eigen bestaan | ✅ | Aparte organisatorische verantwoordelijkheid |
| Kan in meervoud bestaan | ✅ | Meerdere referenda mogelijk over verschillende onderwerpen |
| Eigen levenscyclus | ✅ | Initiatie → voorbereiding → stemming → telling → resultatenafhandeling |
| Relaties met andere objecten | ✅ | Relaties met stembureaus, onderwerpen, resultaten |

**Conclusie:** 6/6 criteria ✅ — Dit is een sterke BO-kandidaat.

## Beschrijving

Een referendum is een volksstemming waarbij kiezers rechtstreeks over een onderwerp kunnen stemmen. Gemeenten organiseren referenda op basis van:

- **Wettelijke grondslag**: Gemeentelijke Kieswet bepaalt referendum-procedures
- **Raadsbesluit**: Raad besluit een referendum uit te schrijven
- **Burgerinitiatief**: Onder bepaalde voorwaarden kunnen burgers om een referendum vragen

Organisatorisch is een referendum vergelijkbaar met verkiezingen (dezelfde stembureaus, stemregistratie, telling), maar de vraagstelling en opzet zijn anders. Daarom is het een apart BO met eigen scope.

## GGM-grondslag

Dit BO heeft **geen GGM-entiteit** — en dat is logisch. Net als [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/politiek/verkiezing|Verkiezing]] is **Referendum een proces**, niet een registratieobject. Dit valt **buiten de scope van het GGM** per definitie (zie [[Wiki/Analyses/ggm-dekkingspatroon|GGM-dekkingspatroon]]).

**Geen terugmelding naar GGM** — dit is een structurele scopekeuze, geen fout.

## BO-definitie

> **Referendum** — Volksstemming over een onderwerp, ingesteld door de raad of op basis van burgerinitiatief, georganiseerd en uitgevoerd door de gemeente conform de Gemeentelijke Kieswet.

## Onderscheid met Verkiezing

- **Verkiezing**: Periodiek, vervangingskeuze ambtsdragers, vastgestelde schema
- **Referendum**: Ad hoc, zaakgericht, door raad of burger geïnitieerd, geen vaste periodiek

## Relaties

- **Stembureau** [1..*] — Referendum wordt afgestemd via stembureaus
- **Onderwerp** [1] — Referendum behandelt één concrete beleidsvaag
- **Referendum-uitslag** (procesobject) — Telling en analyse van resultaten

## Bedrijfsprocessen

1. **Referendum initiëren** (raadsbesluit of burgerinitiatie)
2. **Referendum voorbereiden** (vraagstelling afbakenen, communicatie)
3. **Referendum uitvoeren** (stemming, veiligheid)
4. **Resultaten verwerken** (telling, beleidsbeslissing)

## Bedrijfsfuncties

- **Directe democratie** — Kiezers besluiten rechtstreeks
- **Burgerparticipatie** — Betrokkenheid van inwoners

## Bronsignalering

Zie bronsamenvatting:
- [[Wiki/Bronsamenvattingen/Bestuur/verkiezingen-en-referenda|Verkiezingen en referenda]] — Gemeentelijke verantwoordelijkheid voor alle referenda

## Bronnen

- [[Wiki/Bronsamenvattingen/Bestuur/verkiezingen-en-referenda]]
