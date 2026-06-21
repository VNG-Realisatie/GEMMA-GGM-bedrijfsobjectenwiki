---
type: bedrijfsobject
naam: Stembureau
domein: [Bestuur]
archimate_type: "business-object"
grondslag: procesobject
ggm_entiteit: "~"
ggm_beleidsdomein: "Politiek (niet expliciet gemodelleerd)"
ggm_guid: ""
ggm_uml_type: ""
ggm_taakveld: ""
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: "~"
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "Fysieke locatie waar kiezers hun stem uitbrengen; geregistreerd met adres, capaciteit, toegankelijkheidseigenschappen en personeelsinzet."
bedrijfsprocessen: ""
bedrijfsfuncties: ""
relaties:
  - type: associatie
    bedrijfsobject: Verkiezing
    richting: "naar-dit-BO"
    kardinaliteit: "*"
    beschrijving: Stembureau maakt onderdeel uit van een verkiezing
  - type: associatie
    bedrijfsobject: Referendum
    richting: "naar-dit-BO"
    kardinaliteit: "*"
    beschrijving: Stembureau maakt onderdeel uit van een referendum
  - type: associatie
    bedrijfsobject: Locatie
    richting: "naar-dit-BO"
    kardinaliteit: 1
    beschrijving: "Stembureau bevindt zich op een specifieke BAG-locatie"
---

# Stembureau

## BO-criteria toetsing

| Criterium | Van toepassing? | Opmerkingen |
|---|---|---|
| Betekenis binnen domein | ✅ | Kernfaciliteit van elk verkiezings/referendumproces |
| Herkenbaar voor experts | ✅ | Stafmedewerkers, voorzitters stembureaus, kiezers herkennen dit direct |
| Eigen bestaan | ✅ | Aparte entiteit met adres, samenstelling, capaciteit |
| Kan in meervoud bestaan | ✅ | Elke verkiezing heeft honderden tot duizenden stembureaus |
| Eigen levenscyclus | ✅ | Aanwijzing → voorbereiding → inrichting → bemensing → operatie → telling → archivering |
| Relaties met andere objecten | ✅ | Relaties met verkiezingen, referenda, locaties, kiezers |

**Conclusie:** 6/6 criteria ✅ — Dit is een sterke BO-kandidaat.

## Beschrijving

Een stembureau is een fysieke locatie waar kiezers hun stem uitbrengen. Gemeenten registreren stembureaus met:

- **Locatie**: BAG-adres, toegankelijkheid (parkeerplaatsen, invalide toilet, roltoel)
- **Capaciteit**: Aantal plekken, werking (aantal hokjes, stemtijd per persoon)
- **Bemensing**: Voorzitter, leden, waarnemers per partij/organisatie
- **Voorstemming**: Locatie en momenten voor vervroegd stemmen
- **Communicatie**: Openbare registratie en informatie aan kiezers

De VNG-bron (2026) benadrukt inclusiviteit: "gemeenten die stembureaus inclusiever hebben ingericht voor specifieke doelgroepen."

## GGM-grondslag

Dit BO heeft **geen GGM-entiteit**. Anders dan [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/politiek/verkiezing|Verkiezing]] en [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/politiek/referendum|Referendum]] is Stembureau wél een **registratieobject** — gemeenten leggen fysieke locaties, capaciteit en toegankelijkheid vast in informatiesystemen.

Dit zou in het GGM kunnen — vergelijkbaar met BAG-locaties maar met stemming-specifieke attributen. 

**Terugmelding: Ja** — voorstellen aan GGM-team om Stembureau als registratieobject te modelleren, waarschijnlijk onder taakveld 0 (Bestuur) of als specialisatie van Lokatie.

## BO-definitie

> **Stembureau** — Aangewezen fysieke locatie waar kiezers hun stem uitbrengen, geregistreerd met adres, capaciteit, toegankelijkheidseigenschappen, bemensing en voorstemming-mogelijkheden.

## Attributen (gemeentelijk perspectief)

- **Stembureaunummer**: Unieke identifier per verkiezing
- **Adres** (BAG): Fysieke locatie
- **Capaciteit**: Aantal mogelijke stemmers per uur/dag
- **Voorzitter**: Aansprekpunt
- **Toegankelijkheid**: Parkeerplek, invalide toilet, roltoel, doventoelk, begeleider
- **Voorstemming**: Beschikbaar ja/nee, momenten
- **Bijzonderheden**: Herinrichtingen, experimenten

## Relaties

- **Verkiezing** [*] — Stembureau fungeert in meerdere verkiezingen
- **Referendum** [*] — Stembureau fungeert in meerdere referenda
- **Locatie** (BAG) [1] — Stembureau heeft vaste BAG-locatie
- **Stembureauvoorzitter** (Persoon) [1] — Verantwoordelijke voor uitvoering

## Bedrijfsprocessen

1. **Stembureaus aanwijzen** (planning, capaciteitsberekening)
2. **Stembureaus inrichten** (toegankelijkheid, faciliteiten, bemensing)
3. **Stemming uitvoeren** (registratie, toezicht, noodsituaties)
4. **Telling uitvoeren** (per stembureau en samenvoeging)
5. **Archivering** (materialen, rapportage)

## Bedrijfsfuncties

- **Democratische participatie** — Fysieke faciliteit voor stemming
- **Inclusiviteit en gelijke toegang** — Toegankelijkheidseigenschappen
- **Transparantie** — Openbare stemming met waarnemers

## Bronsignalering

Zie bronsamenvattingen:
- [[Wiki/Bronsamenvattingen/Bestuur/verkiezingen-en-referenda|Verkiezingen en referenda]] — Toegankelijkheid en inclusiviteit; handreiking VNG
- [[Wiki/Bronsamenvattingen/Bestuur/gemeenteraadsverkiezingen-2026|Gemeenteraadsverkiezingen 2026]] — Communicatie over stemprocedures

## Opmerking: Verschil met BAG-locatie

Stembureau is niet hetzelfde als een BAG-locatie (bijv. "Basisschool De Toekomst"). Het stembureau **bevindt zich op** een BAG-locatie, maar is een separate registratie met specifieke eigenschappen (capaciteit, bemensing, voorstemming) per verkiezing/referendum. Dezelfde BAG-locatie kan meerdere stembureaus herbergen en stembureaus kunnen wisselen van locatie.
