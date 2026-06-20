---
type: bedrijfsobject
naam: Standplaats
domein: [Economie]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Standplaats
ggm_guid: EAID_98F3132E_F97A_4f49_B4F5_28618BB693F8
ggm_uml_type: Class
ggm_beleidsdomein: Musea
ggm_taakveld: "5 Sport, Cultuur en Recreatie"
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: "vanaf een vaste locatie te koop aanbieden, verkopen of afleveren van goederen of aanbieden van diensten, gebruikmakend van fysieke middelen zoals een kraam, een wagen of een tafel"
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst: GGM

ggm_gemma_naam:
ggm_gemma_guid:
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type:
ggm_gemma_url:
ggm_gemma_bron:
ggm_gemma_alternate_name:

gemma_definitie: "Aangewezen locatie in de openbare ruimte waar goederen of diensten te koop worden aangeboden met verplaatsbare fysieke middelen, gereguleerd via de APV."
bronnen:
  - [[Wiki/Bronsamenvattingen/Economie/ontwikkelingskader-detailhandel-2012]]
  - [[Wiki/Bronsamenvattingen/Economie/detailhandel-utrecht-2015]]
relaties:
  - type: compositie
    bedrijfsobject: [[warenmarkt]]
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een warenmarkt bestaat uit 6 of meer standplaatsen"
bedrijfsprocessen: [standplaatsvergunningverlening, branchering ambulante handel, monitoring detailhandel]
bedrijfsfuncties: [vergunningverlening, economisch beleid]
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Expliciet gedefinieerd in APV, onderdeel van ambulante handel |
| Is herkenbaar voor domeinexperts | ✅ | Standaard begrip in economisch beleid en vergunningverlening |
| Heeft een eigen bestaan | ✅ | Fysieke locatie, aangewezen door gemeente |
| Kan in meervoud bestaan | ✅ | 102 standplaatsen in Utrecht (88 gemeentegrond + 14 derden) |
| Heeft een eigen levenscyclus | ✅ | Aangewezen → vergund → actief → eventueel opgeheven |
| Heeft relaties met andere concepten | ✅ | Onderdeel van warenmarkt, heeft vergunning, branchering |

6/6 criteria — BO.

## Beschrijving

Een standplaats is een door de gemeente aangewezen locatie in de openbare ruimte waar met verplaatsbare middelen (kraam, wagen, tafel) goederen of diensten worden aangeboden. De gemeente reguleert standplaatsen via de APV met een vergunningenstelsel dat branchering, selectievoorwaarden en een maximumaantal omvat.

Standplaatsen worden onderscheiden in dagstandplaatsen (bij winkelgebieden of verspreid bij parken/begraafplaatsen), seizoensstandplaatsen en incidentele standplaatsen. Bij winkelgebieden zijn standplaatsen beperkt tot food en bloemen/planten; non-food is voorbehouden aan fysieke winkels en warenmarkten.

De Dienstenwet is van toepassing op standplaatsuitgifte: vestigingsbeperkingen moeten niet-discriminerend, noodzakelijk en evenredig zijn.

## GGM-bron

> "vanaf een vaste locatie te koop aanbieden, verkopen of afleveren van goederen of aanbieden van diensten, gebruikmakend van fysieke middelen zoals een kraam, een wagen of een tafel" (GGM entiteit: Standplaats, beleidsdomein Musea, taakveld 5)

**Matchsterkte: sterk** — De GGM-definitie komt inhoudelijk overeen met de APV-definitie. De plaatsing onder Musea is echter opmerkelijk: standplaatsen zijn een breed gemeentelijk concept (ambulante handel, APV), niet specifiek voor musea. De GGM-attributen (beschrijving, adres, naamInstelling) dekken slechts een deel van wat gemeenten registreren (branchering, type, seizoen, vergunningsstatus ontbreken).

**Let op:** De BAG/RSGB kent ook een "Standplaats" (EAID_86952BDA), maar dat betreft de woonwagenstandplaats — een ander concept.

## BO-definitie

De GEMMA-definitie is breder dan de GGM-definitie: het benadrukt de APV-regulering en het openbare-ruimte-karakter, wat essentieel is voor het gemeentelijk perspectief.

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[warenmarkt]] (compositie) | standplaats is onderdeel van warenmarkt | 0..* | beleidsbron |

## Bedrijfsprocessen

- **Standplaatsvergunningverlening** — verlening, weigering en intrekking van standplaatsvergunningen op basis van APV
- **Branchering ambulante handel** — toewijzing van branches aan standplaatsen (food, bloemen/planten, seizoensgebonden)
- **Monitoring detailhandel** — periodieke beoordeling van het standplaatsenbestand

## Terugmelding GGM

⚠️ De GGM-entiteit Standplaats staat onder beleidsdomein Musea (taakveld 5), terwijl het een breed APV-concept is dat onder alle gemeentelijke domeinen valt. Overweeg herplaatsing naar Economie (taakveld 3) of een generiek domein. Daarnaast ontbreken attributen voor branchering, type (dag/seizoen/incidenteel) en vergunningsstatus.
