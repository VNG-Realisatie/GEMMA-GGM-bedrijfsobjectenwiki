---
type: element
naam: Woning
onderwerp: [Wonen]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Gebouw
ggm_guid: EAID_681DB26F_D779_4796_B467_576E5A25F581
ggm_uml_type: Class
ggm_beleidsdomein: Bouwen en Wonen
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram: [Woningbouwprojecten]
ggm_diagram_ids: [EAID_5B2022A2_1DAB_476d_BBCD_CD27F56F169F]
ggm_definitie: "Een complex van ruimten uitsluitend bedoeld voor de huisvesting van een afzonderlijk huishouden"
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam: Gebouw
ggm_gemma_guid: "69e60d64-7165-488f-a392-0e75eb4e99fb"
ggm_gemma_definitie: "Een complex van ruimten uitsluitend bedoeld voor de huisvesting van een afzonderlijk huishouden"
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-69e60d64-7165-488f-a392-0e75eb4e99fb"
ggm_gemma_bron:
ggm_gemma_alternate_name:

analyse_ggm_dekking: |
  Dit BO is de hernoeming van GGM-entiteit **Gebouw**. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Huurwoningen** (specialisatie) — Specialisatie van Woning — zie bo_subtypes
  - **Koopwoningen** (specialisatie) — Specialisatie van Woning — zie bo_subtypes
  - **Studentenwoningen** (specialisatie) — Specialisatie van Woning — zie bo_subtypes
bo_definitie: "Een complex van ruimten uitsluitend bedoeld voor de huisvesting van een afzonderlijk huishouden"
bo_toelichting:
bo_subtypes:
  - naam: "Sociale huurwoning"
    omschrijving: "Huurwoning met een huurprijs onder de liberalisatiegrens (€900,07 in 2025), toegewezen via woonruimteverdeling"
    ggm_entiteit: Huurwoningen
    ggm_guid: EAID_E0F7D3A0_46C8_4e70_AA10_3888B60D14C0
    ggm_attribuut: generalisatie
  - naam: "Middenhuurwoning"
    omschrijving: "Huurwoning met 144-186 WWS-punten en huurprijs €900-€1.185, gereguleerd via Wet betaalbare huur"
  - naam: "Betaalbare koopwoning"
    omschrijving: Koopwoning met verkoopprijs tot de betaalbaarheidsgrens van het Rijk (€405.000 in 2025)
    ggm_entiteit: Koopwoningen
    ggm_guid: EAID_7FECB5B2_E6CB_4637_9FD4_6EBA2CA96BBA
    ggm_attribuut: generalisatie
  - naam: "Studentenwoning"
    omschrijving: "Woning verhuurd met campuscontract aan studenten, zelfstandig of onzelfstandig"
    ggm_entiteit: Studentenwoningen
    ggm_guid: EAID_98C74EAB_3411_4d1a_8321_FF30567B6877
    ggm_attribuut: generalisatie
  - naam: "Eengezinswoning"
    omschrijving: "Woning bestemd voor bewoning door één huishouden, doorgaans grondgebonden"
  - naam: "Meergezinswoning"
    omschrijving: "Woning in een gebouw met meerdere zelfstandige woningen (appartement)"
  - naam: "Vrijstaande woning"
    omschrijving: "Eengezinswoning die aan geen enkele zijde grenst aan een andere woning"
  - naam: "Twee-onder-een-kapwoning"
    omschrijving: "Eengezinswoning die aan één zijde grenst aan een andere woning"
  - naam: "Hoekwoning"
    omschrijving: "Eengezinswoning aan het einde van een rij aaneengesloten woningen"
  - naam: "Tussenwoning"
    omschrijving: "Eengezinswoning tussen twee andere woningen in een rij aaneengesloten woningen"
  - naam: "Galerijwoning"
    omschrijving: "Meergezinswoning ontsloten via een gemeenschappelijke galerij"
  - naam: "Portiekwoning"
    omschrijving: "Meergezinswoning ontsloten via een gedeeld portiek/trappenhuis voor een beperkt aantal woningen"
  - naam: "Maisonnette"
    omschrijving: "Meergezinswoning verdeeld over twee bouwlagen binnen hetzelfde gebouw"
  - naam: "Bovenwoning / Benedenwoning"
    omschrijving: "Meergezinswoning boven resp. op de begane grond van een gebouw met maximaal twee woningen"
  - naam: "Woning boven bedrijfsruimte"
    omschrijving: "Woning gelegen boven een niet-woonfunctie (bedrijfsruimte, winkel)"
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Woningbouwplan]]"
    richting: naar-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Een woningbouwplan realiseert woningen"
  - type: associatie
    bedrijfsobject: "[[Urgentverklaring]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een urgentverklaring geeft voorrang bij toewijzing van een woning"
  - type: associatie
    bedrijfsobject: "[[Pand]]"
    richting: vanuit-dit-BO
    kardinaliteit: "1..1"
    beschrijving: "Een woning bevindt zich in een pand; een pand kan één woning (grondgebonden) of meerdere woningen (appartementengebouw) bevatten"
bedrijfsprocessen: [Woonruimteverdeling, Woningbouwprogrammering, Vergunningverlening huisvesting, Handhaving goed verhuurderschap]
bedrijfsfuncties: [Volkshuisvesting, Woonbeleid, Vergunningverlening]
---

## BO-criteria toetsing

| Criterium | Score |
|---|---|
| Heeft betekenis binnen het domein | ✅ Centraal concept in woonbeleid |
| Herkenbaar voor domeinexperts | ✅ |
| Heeft een eigen bestaan | ✅ Fysiek object met adres |
| Kan in meervoud bestaan | ✅ 167.000 woningen in Utrecht |
| Heeft een eigen levenscyclus | ✅ Gebouwd, bewoond, gerenoveerd, gesloopt |
| Heeft relaties met andere concepten | ✅ Woningbouwplan, urgentverklaring, woningcorporatie |

Score: **6/6** — BO.

## Beschrijving

Een woning is een zelfstandige woonruimte bedoeld voor de permanente huisvesting van één huishouden. De gemeente Utrecht telde op 1 januari 2024 167.123 woningen. De woningvoorraad wordt getypeerd naar prijssegment: sociale huur, middenhuur, betaalbare koop en vrije sector. Het gemeentelijk woonbeleid stuurt op de samenstelling van deze voorraad met als ambitie 60% betaalbare woningen in 2040.

## Specialisaties

Geen van de onderstaande subtypes heeft een eigen BO-pagina — ze zijn classificaties van Woning, vastgelegd in `bo_subtypes`.

### Naar marktsegment

| Specialisatie | Omschrijving | GGM-entiteit |
|---|---|---|
| Sociale huurwoning | Huurprijs onder liberalisatiegrens (€900,07 in 2025). Toewijzing via WoningNet/DĀK. Corporaties bezitten 29% van de voorraad. | [Huurwoningen](Sources/GGM/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/bouwen-en-wonen.md) |
| Middenhuurwoning | Huurprijs €900–€1.185, 144–186 WWS-punten. Minimaal 20 jaar in segment (25 op gemeentegrond). Drie oppervlaktezones (A/B/C). | — (GGM-hiaat) |
| Betaalbare koopwoning | Verkoopprijs tot €405.000 (2025). Zelfbewoningsplicht en antispeculatiebeding. | [Koopwoningen](Sources/GGM/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/bouwen-en-wonen.md) |
| Studentenwoning | Campuscontract, stopt na beëindiging studie. Zelfstandig of onzelfstandig (WWSO). | [Studentenwoningen](Sources/GGM/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/bouwen-en-wonen.md) |

Niet als apart subtype: nultredenwoning en zorggeschikte woning zijn woningkenmerken (toegankelijkheidsclassificatie), geen marktsegmenten.

### Naar bouwvorm

Naast de marktsegment-indeling (huur/koop) hanteert het digiGO-informatiemodel IMWO een indeling naar bouwvorm. Dit is een aparte, onafhankelijke classificatie-as (een woning heeft zowel een marktsegment als een bouwvorm):

| Specialisatie | Omschrijving |
|---|---|
| Eengezinswoning | Woning bestemd voor bewoning door één huishouden, doorgaans grondgebonden |
| Meergezinswoning | Woning in een gebouw met meerdere zelfstandige woningen (appartement) |
| Vrijstaande woning | Eengezinswoning die aan geen enkele zijde grenst aan een andere woning |
| Twee-onder-een-kapwoning | Eengezinswoning die aan één zijde grenst aan een andere woning |
| Hoekwoning | Eengezinswoning aan het einde van een rij aaneengesloten woningen |
| Tussenwoning | Eengezinswoning tussen twee andere woningen in een rij aaneengesloten woningen |
| Galerijwoning | Meergezinswoning ontsloten via een gemeenschappelijke galerij |
| Portiekwoning | Meergezinswoning ontsloten via een gedeeld portiek/trappenhuis voor een beperkt aantal woningen |
| Maisonnette | Meergezinswoning verdeeld over twee bouwlagen binnen hetzelfde gebouw |
| Bovenwoning / Benedenwoning | Meergezinswoning boven resp. op de begane grond van een gebouw met maximaal twee woningen |
| Woning boven bedrijfsruimte | Woning gelegen boven een niet-woonfunctie (bedrijfsruimte, winkel) |

Het GGM kent voor deze indeling een enumeratie `soortWoonobject` (Model BAG en RSGBPlus/Enumeratiesoort), maar deze heeft in de geëxporteerde XMI geen ingevulde literalen — zie Terugmelding GGM hieronder.

## GGM-bron

> "Een complex van ruimten uitsluitend bedoeld voor de huisvesting van een afzonderlijk huishouden" — GGM-entiteit **Gebouw**, beleidsdomein Bouwen en Wonen

**Matchsterkte: sterk.** De GGM-entiteit "Gebouw" komt inhoudelijk overeen met het beleidsconcept "Woning". De beleidsnota hanteert de definitie: "het complex van ruimten dat een zelfstandige woonruimte vormt, bedoeld voor de permanente huisvesting van één afzonderlijk huishouden." De GGM-naam "Gebouw" is generieker dan de beleidsterm "Woning".

**Attributen GGM:** aantal, aantalAdressen, aantalKamers, energielabel, oppervlakte, duurzaam, natuurinclusief, regenwater, aardgasloos.

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Woningbouwplan]] realiseert woningen | naar Woning | 1..* | GGM (Plan → Gebouw) |
| [[Urgentverklaring]] geeft voorrang bij toewijzing | naar Woning | 0..* | Beleidsnota |
| Woning bevindt zich in [[Pand]] | vanuit Woning | 1..1 | IMWO (zie Terugmelding GGM) |

## Bedrijfsprocessen

- **Woonruimteverdeling** — Toewijzing van sociale huurwoningen via aanbodmodel, loting en bemiddeling
- **Woningbouwprogrammering** — Programmering en monitoring van nieuwbouw via MPR
- **Vergunningverlening huisvesting** — Verlening huisvestingsvergunningen
- **Handhaving goed verhuurderschap** — Toezicht op verhuurkwaliteit

## Bronnen

- [[Wiki/Bronsamenvattingen/Wonen/beleidsnota-wonen-utrecht]]
- [[Wiki/Bronsamenvattingen/Wonen/huisvestingsverordening-utrecht]]
- [[Wiki/Bronsamenvattingen/Wonen/nadere-regel-huisvestingsverordening]]
- [[Wiki/Bronsamenvattingen/Wonen/beleidsregel-huisvestingsverordening]]
- [[Wiki/Bronsamenvattingen/Wonen/actieplan-betaalbare-koopwoningen]]
- [[Wiki/Bronsamenvattingen/Wonen/actieplan-middenhuur]]
- [[Wiki/Bronsamenvattingen/Wonen/werkwijze-extra-woningen]]
- [[Wiki/Bronsamenvattingen/Wonen/woonboten-utrecht]]
- [[Wiki/Bronsamenvattingen/Wonen/woonbotenbeleid-utrecht-2007]]
- [[Wiki/Bronsamenvattingen/Wonen/historische-schepen-utrecht-2015]]
- [[Wiki/Bronsamenvattingen/Standaarden/imwo-informatiemodel-woongebouwen]]

## Terugmelding GGM

> **Middenhuurwoning** — Ontbreekt als subtype van Gebouw in het GGM. Sinds de Wet betaalbare huur (2024) is middenhuur een wettelijk gereguleerd segment met eigen prijsgrenzen (144–186 WWS-punten, €900–€1.185) en instandhoudingstermijnen. Zou passen als subtype van Gebouw naast Huurwoningen en Koopwoningen in beleidsdomein Bouwen en Wonen.

> **Enumeratie `soortWoonobject` zonder literalen** — Het GGM bevat de enumeratie `soortWoonobject` (Model BAG én RSGBPlus/Enumeratiesoort) als plaatshouder voor een indeling naar bouwvorm, maar deze heeft in de geëxporteerde XMI geen ingevulde literalen. Het digiGO-informatiemodel IMWO ([[Wiki/Bronsamenvattingen/Standaarden/imwo-informatiemodel-woongebouwen]]) benoemt hiervoor wel expliciete objecttypen (Eengezinswoning, Meergezinswoning, Vrijstaande woning, Twee-onder-een-kapwoning, Hoekwoning, Tussenwoning, Galerijwoning, Portiekwoning, Maisonnette, Boven-/Benedenwoning, Woning boven bedrijfsruimte) — hier vastgelegd als `bo_subtypes` naar bouwvorm, zie sectie "Subtypes → Naar bouwvorm".

> **Ontbrekende relatie Gebouw ↔ Pand** — Het GGM modelleert de GGM-entiteit Gebouw (Model Wonen, hernoemd tot BO Woning) zonder relatie naar Pand (Model BAG/99 Kern). Het digiGO-informatiemodel IMWO onderscheidt expliciet WoonGebouw (het pand/de constructie, kan meerdere woningen bevatten) van WoonObject/Woning (de individuele bewoonbare eenheid) — een hiërarchie die in de BAG al bestaat tussen [[Pand]] en Verblijfsobject. Hier vastgelegd als `bo_relaties`-item Woning → Pand; geen apart BO WoonGebouw, omdat het gemeentelijke object hiervoor al bestaat als [[Pand]] (zie ook [[Wiki/Bronsamenvattingen/Standaarden/imwo-informatiemodel-woongebouwen]]).
