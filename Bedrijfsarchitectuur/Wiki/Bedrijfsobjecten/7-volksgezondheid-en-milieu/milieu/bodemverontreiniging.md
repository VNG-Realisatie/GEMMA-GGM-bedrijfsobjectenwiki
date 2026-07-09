---
type: element
naam: Bodemverontreiniging
onderwerp: [Milieu]
archimate_type: "business-object"
grondslag: procesobject
ggm_entiteit:
ggm_beleidsdomein:
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
bo_definitie: "Geregistreerde locatie waar de bodem of het grondwater verontreinigd is, met type verontreiniging, omvang en saneringsstatus."
bo_toelichting:
bedrijfsprocessen: [bodemsanering, gebiedsgericht grondwaterbeheer, milieuhandhaving, bodemonderzoek]
bedrijfsfuncties: [milieubeheer, vergunningverlening]
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/saneringsplan|Saneringsplan]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Voor een verontreiniging wordt een saneringsplan opgesteld
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/grondwatermeetpunt|Grondwatermeetpunt]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: Meetpunten monitoren de verspreiding van verontreinigingen
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/bodemkwaliteitskaart|Bodemkwaliteitskaart]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: Bekende verontreinigingen worden als puntbron uitgesloten van de kaart
---

## BO-criteria toetsing

| Criterium | Van toepassing? |
|---|---|
| Heeft betekenis binnen het domein | ✅ Kernobject in milieubeheer |
| Herkenbaar voor domeinexperts | ✅ Wettelijk gedefinieerd (Wet bodembescherming/Omgevingswet) |
| Heeft eigen bestaan | ✅ Individuele locatie met eigen registratie |
| Kan in meervoud bestaan | ✅ Honderden tot duizenden per gemeente |
| Heeft eigen levenscyclus | ✅ Ontdekking → onderzoek → sanering → nazorg → afmelding |
| Heeft relaties met andere concepten | ✅ Saneringsplan, meetpunten, bodemkwaliteitskaart |

**6/6 criteria van toepassing.**

## Beschrijving

Een bodemverontreiniging is een geregistreerde locatie waar de bodem of het grondwater is verontreinigd met stoffen boven de vastgestelde normen. Elke verontreiniging heeft een locatie, type verontreinigende stoffen (VOCl, zware metalen, PAK, PFAS), omvang (horizontaal en verticaal), en een saneringsstatus.

De gemeente registreert verontreinigingen als bevoegd gezag. Bij spoedlocaties zijn maatregelen verplicht om mens, plant, dier en bodem te beschermen. In het gebiedsplan Utrecht worden vermengde grondwaterverontreinigingen gebiedsgericht beheerd in plaats van per geval.

> "Metingen hebben aangetoond dat het grondwater in de stad grotendeels verontreinigd is. Hieruit volgt onder meer dat sprake is van gebruiksbeperkingen en er maatregelen genomen moeten worden om mens en milieu te beschermen." (bron: [[Wiki/Bronsamenvattingen/Milieu/gebiedsplan-grondwaterbeheer|Gebiedsplan gebiedsgericht grondwaterbeheer en visie op duurzaam gebruik van de ondergrond]])

## Procesbron

Verontreinigingen worden geïdentificeerd via bodemonderzoek en monitoring. De registratie valt onder de Wet bodembescherming (overgangsrecht Omgevingswet). De gemeente is bevoegd gezag voor de meeste bodemverontreinigingen.

## Relaties

- **[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/saneringsplan|Saneringsplan]]** — voor elke (ernstige) verontreiniging wordt een saneringsplan opgesteld
- **[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/grondwatermeetpunt|Grondwatermeetpunt]]** — meetpunten monitoren de verspreiding van verontreinigingspluimen
- **[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/bodemkwaliteitskaart|Bodemkwaliteitskaart]]** — verontreinigingen worden als puntbron uitgesloten van de kwaliteitskaart

## Bedrijfsprocessen

- **Bodemsanering** — aanpak van de verontreiniging
- **Gebiedsgericht grondwaterbeheer** — integrale beheersing van vermengde verontreinigingen
- **Milieuhandhaving** — toezicht op naleving saneringsverplichtingen
- **Bodemonderzoek** — identificatie en afbakening van verontreinigingen


## Bronnen

- [[Wiki/Bronsamenvattingen/Milieu/gebiedsplan-grondwaterbeheer]]

## Terugmelding GGM

Bodemverontreiniging is een kernregistratie-object voor gemeenten als bevoegd gezag bodem. Het GGM heeft geen beleidsdomein hiervoor. Dit is een structureel hiaat — vergelijkbaar met hoe het GGM wel BAG-locaties maar niet milieu-locaties modelleert. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
