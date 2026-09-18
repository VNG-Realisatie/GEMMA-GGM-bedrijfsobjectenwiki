---
type: element
naam: Verkiezing
onderwerp:
- Bestuur
archimate_type: business-object
grondslag: procesobject
ggm_entiteit:
ggm_beleidsdomein: Politiek (niet expliciet gemodelleerd)
ggm_guid:
ggm_uml_type:
ggm_taakveld:
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie:
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:
ggm_gemma_naam:
ggm_gemma_guid:
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type:
ggm_gemma_url:
ggm_gemma_bron:
ggm_gemma_alternate_name:
bo_definitie: "Periodiek georganiseerd democratisch proces waarbij kiezers ambtsdragers kiezen, door de gemeente voorbereid en uitgevoerd."
bo_toelichting:
bedrijfsprocessen: []
bedrijfsfuncties: []
bo_relaties:
- type: compositie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/politiek/stembureau|Stembureau]]"
  richting: van-dit-BO
  kardinaliteit: "1..*"
  beschrijving: Verkiezing omvat meerdere stembureaus als fysieke locaties
- type: associatie
  bedrijfsobject: "Kiezer"
  richting: bidirectioneel
  kardinaliteit: "*"
  beschrijving: Kiezers brengen hun stem uit bij een verkiezing
---

# Verkiezing

## BO-criteria toetsing

| Criterium | Van toepassing? | Opmerkingen |
|---|---|---|
| Betekenis binnen domein | ✅ | Kernproces van gemeentelijk bestuur |
| Herkenbaar voor experts | ✅ | Raadsleden, stafmedewerkers, burgers herkennen verkiezingen direct |
| Eigen bestaan | ✅ | Aparte entiteit met eigen planning, proces, uitvoering |
| Kan in meervoud bestaan | ✅ | Meerdere verkiezingen (raad 2026, kamer 2026, waterschappen, europa) |
| Eigen levenscyclus | ✅ | Voorbereiding → voorstemming → stemming → telling → beklachting → einduitslag |
| Relaties met andere objecten | ✅ | Relaties met stembureaus, kiezers, uitslagen |

**Conclusie:** 6/6 criteria ✅ — Dit is een sterke BO-kandidaat.

## Beschrijving

Een verkiezing is een periodieke vervangingskeuze van gekozen ambtsdragers (raadsleden, burgemeester, waterschapsleden, Europese parlementsleden, Tweede Kamerlieden). Gemeenten dragen volledige organisatorische verantwoordelijkheid:

- **Voorbereiding**: Registratie stembureaus, communicatie over procedure en stemmogelijkheden, inrichting toegankelijkheid
- **Uitvoering**: Controle kiezersinschrijving, uitgifte stempassen, registratie aanwezige kiezers, toezicht op stemming
- **Telling**: Telling per stembureau, rapportage uitslagen, archivering stemmaterialen
- **Beklachting**: Afhandeling indieningen (art. 6K Kieswet)

Gemeente organiseert alle landsverkiezingen (TK, PS, waterschappen, EP) én gemeenteraadsverkiezingen. Dit zijn formeel verschillende processen maar vergelijkbare organisatiestructuur.

## GGM-grondslag

Dit BO heeft **geen GGM-entiteit** — en dat is logisch. Het GGM modelleert **dataobjecten** (wat gemeenten registreren in informatiesystemen), niet **processen** (hoe werk verloopt). 

**Verkiezing is een proces**, niet een registratieobject. Gemeenten registreren uitslagen en stemmers, maar niet "verkiezingen" zelf als database-entiteit. Het GGM dekt dit niet: procesobjecten als dit zijn in het GGM niet compleet gemodelleerd.

**Geen terugmelding naar GGM** — dit is een scopekeuze, geen fout.

## Relaties

- **Stembureau** [1..*] — Verkiezing omvat meerdere stembureaus
- **Kiezer** [*] — Kiezers brengen stem uit bij verkiezing
- **Uitslag** (procesobject) — Telling van stemmen resulteert in uitslag

## Bedrijfsprocessen

1. **Verkiezing organiseren** (voorbereiding, planning, communicatie)
2. **Verkiezing uitvoeren** (registratie, stemming, toezicht)
3. **Uitslag vaststellen** (telling, rapportage, archivering)
4. **Beklachtingen afhandelen** (Kieswet art. 6K)

## Bedrijfsfuncties

- **Kiezen** — Burgers oefenen hun actieve stemrecht uit
- **Democratische participatie** — Primaire functie van lokale democratie

## Bronsignalering

Zie bronsamenvattingen:
- [[Wiki/Bronsamenvattingen/Bestuur/verkiezingen-en-referenda|Verkiezingen en referenda]] — Gemeentelijke verantwoordelijkheid, Verkiezingsagenda 2030
- [[Wiki/Bronsamenvattingen/Bestuur/gemeenteraadsverkiezingen-2026|Gemeenteraadsverkiezingen 2026]] — Concrete organisatietaken en ondersteuning VNG

## Bronnen

- [[Wiki/Bronsamenvattingen/Bestuur/verkiezingen-en-referenda]]
- [[Wiki/Bronsamenvattingen/Bestuur/gemeenteraadsverkiezingen-2026]]
