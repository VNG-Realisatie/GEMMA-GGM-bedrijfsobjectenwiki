---
type: bedrijfsobject
naam: klacht
onderwerp: [informatiesamenleving, dienstverlening]
archimate_type: business-object
grondslag: procesobject

ggm_entiteit:
ggm_guid:
ggm_uml_type:
ggm_beleidsdomein:
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

ggm_duplicaat_entiteiten: []

bo_definitie: Uiting van ontevredenheid over een gedraging van een bestuursorgaan of een ambtenaar, behandeld conform titel 9.1 Awb.
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: [[zaak]]
    richting: naar-dit-BO
    kardinaliteit: "1..1"
    beschrijving: Klacht wordt behandeld als zaak
bedrijfsprocessen: [Behandelen klacht, Actieve openbaarmaking klachtoordelen]
bedrijfsfuncties: [Dienstverlening, Juridische zaken]
---

# Klacht

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Identificeerbaar | Ja — unieke klacht met klager, ontvangstdatum, gedraging |
| Eigen attributen | Ja — organisatieonderdeel, functiebenaming beklaagde, gedraging, bevindingen, oordeel, conclusies, dagtekening (wettelijk gedefinieerd, art. 3.3a lid 3 Woo) |
| Levenscyclus | Ja — ontvangst → onderzoek → horen → oordeel → actieve openbaarmaking |
| Gemeentelijk eigendom | Ja — gemeente behandelt klachten over eigen gedragingen |
| Wettelijke grondslag | Ja — titel 9.1 Awb (klachtbehandeling door bestuursorganen) |
| Registratieverplichting | Ja — verplicht jaarlijks register (art. 9:12a Awb), actieve openbaarmaking klachtoordelen (art. 3.3 lid 2 sub l Woo) |

Score: 6/6 criteria.

## Beschrijving

Een klacht is een uiting van ontevredenheid over een gedraging van een bestuursorgaan of een onder zijn verantwoordelijkheid werkzame persoon. De klachtbehandeling is geregeld in titel 9.1 van de Algemene wet bestuursrecht.

De gemeente behandelt klachten met een vaste procedure: ontvangstbevestiging, hoor en wederhoor (klager en beklaagde), onderzoek naar de feiten, en een schriftelijk oordeel. Het oordeel bevat wettelijk gedefinieerde elementen die actief openbaar moeten worden gemaakt.

Het bestuursorgaan is verplicht jaarlijks een overzicht te publiceren van ontvangen klachten (art. 9:12a Awb). De Woo voegt daaraan toe dat de schriftelijke oordelen in klachtprocedures actief openbaar worden gemaakt, hetzij integraal, hetzij via een overzicht met de wettelijk gedefinieerde attributen (art. 3.3a lid 3 Woo).

## Procesbron

Wettelijke grondslag: titel 9.1 Awb (art. 9:1 t/m 9:12a), aangevuld met Woo art. 3.3 lid 2 sub l en art. 3.3a lid 3.

Openbaarmaking gedocumenteerd in [[Wiki/Bronsamenvattingen/Informatiesamenleving/handreiking-woo-gemeentelijke-praktijk|Handreiking Woo in de gemeentelijke praktijk]] (VNG/Pels Rijcken 2025), paragraaf 3.5.10.

## Relaties

| Relatie | Bedrijfsobject | Richting | Beschrijving |
|---|---|---|---|
| associatie | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] | ← | Wordt behandeld als zaak |

## Bedrijfsprocessen

- **Behandelen klacht** — ontvangst, hoor en wederhoor, onderzoek, oordeel (titel 9.1 Awb)
- **Actieve openbaarmaking klachtoordelen** — publicatie oordelen via Woo-index of overzicht (art. 3.3a lid 3)

## Bronnen
- [[Wiki/Bronsamenvattingen/Informatiesamenleving/handreiking-woo-gemeentelijke-praktijk]]

## Terugmelding GGM

GGM-hiaat: het GGM bevat alleen "Klacht Leerlingenvervoer" als domeinspecifieke specialisatie (taakveld 4, Leerplicht en Leerlingenvervoer). Een generiek klachtobject op basis van titel 9.1 Awb ontbreekt. De Woo definieert wettelijk verplichte attributen voor klachtoordelen die actief openbaar moeten worden gemaakt, wat een cross-domein klachtconcept impliceert.

Teruggemeld als #67 in [[Wiki/Analyses/ggm-terugmeldingen]].
