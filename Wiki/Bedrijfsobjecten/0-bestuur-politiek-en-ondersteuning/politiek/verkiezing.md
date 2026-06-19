---
type: bedrijfsobject
naam: Verkiezing
domein: [Bestuur]
archimate_type: business-object
grondslag: procesobject

# GGM-velden
ggm_entiteit: ~
ggm_guid: ~
ggm_uml_type: ~
ggm_beleidsdomein: "Politiek (niet expliciet gemodelleerd)"
ggm_taakveld: "0 Bestuur, Politiek en Ondersteuning"
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: ~
ggm_toelichting: ~
ggm_synoniemen: ~
ggm_herkomst: ~

# GEMMA-velden
gemma_definitie: "Periodieke vervangingskeuze van gekozen ambtsdragers, georganiseerd en uitgevoerd door de gemeente, met formele processen voor registratie, stemming en telling."
bronnen:
  - "Wiki/Bronsamenvattingen/Bestuur/verkiezingen-en-referenda.md"
  - "Wiki/Bronsamenvattingen/Bestuur/gemeenteraadsverkiezingen-2026.md"
relaties:
  - type: compositie
    bedrijfsobject: Stembureau
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Verkiezing omvat meerdere stembureaus als fysieke locaties"
  - type: associatie
    bedrijfsobject: Kiezer
    richting: bidirectioneel
    kardinaliteit: "*"
    beschrijving: "Kiezers brengen hun stem uit bij een verkiezing"
bedrijfsprocessen:
  - "Voorbereiding verkiezing (planning, registratie stembureaus, communicatie)"
  - "Uitvoering stemming (registratie kiezers, stemming, veiligheid)"
  - "Tellen en rapportage (telling stembureaus, uitslagrapportage)"
bedrijfsfuncties:
  - "Kiezen"
  - "Democratische participatie"
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

**Verkiezing is een proces**, niet een registratieobject. Gemeenten registreren uitslagen en stemmers, maar niet "verkiezingen" zelf als database-entiteit. Dit valt **buiten de scope van het GGM** — niet omdat het een hiaat is, maar omdat het GGM per definitie alleen data modelleert (zie [[Wiki/Analyses/ggm-dekkingspatroon]]).

**Geen terugmelding naar GGM** — dit is een scopekeuze, geen fout.

## BO-definitie

> **Verkiezing** — Periodieke vervangingskeuze van gekozen ambtsdragers (raadsleden, burgemeester, waterschapsleden, EP-vertegenwoordigers, TK-afgevaardigden), volledig georganiseerd en uitgevoerd door de gemeente conform de Kieswet en aanverwante regelgeving.

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
- [[verkiezingen-en-referenda|Verkiezingen en referenda]] — Gemeentelijke verantwoordelijkheid, Verkiezingsagenda 2030
- [[gemeenteraadsverkiezingen-2026|Gemeenteraadsverkiezingen 2026]] — Concrete organisatietaken en ondersteuning VNG
