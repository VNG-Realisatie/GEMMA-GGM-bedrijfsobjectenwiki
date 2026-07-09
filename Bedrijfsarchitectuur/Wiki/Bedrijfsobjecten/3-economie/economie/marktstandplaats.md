---
type: element
naam: Marktstandplaats
onderwerp: [Economie]
archimate_type: "business-object"
grondslag: "procesobject"
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
ggm_gemma_naam: "Marktstandplaats"
ggm_gemma_guid:
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type:
ggm_gemma_url:
ggm_gemma_bron:
ggm_gemma_alternate_name:
bo_definitie: "Aangewezen locatie in de openbare ruimte waar goederen of diensten te koop worden aangeboden met verplaatsbare fysieke middelen, gereguleerd via de APV."
bo_toelichting:
bedrijfsprocessen: [standplaatsvergunningverlening, branchering ambulante handel, monitoring detailhandel]
bedrijfsfuncties: [vergunningverlening, economisch beleid]
bo_relaties:
  - type: compositie
    bedrijfsobject: "[[warenmarkt]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Een warenmarkt bestaat uit 6 of meer standplaatsen
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

Een marktstandplaats is een door de gemeente aangewezen locatie in de openbare ruimte waar met verplaatsbare middelen (kraam, wagen, tafel) goederen of diensten worden aangeboden. De gemeente reguleert marktstandplaatsen via de APV met een vergunningenstelsel dat branchering, selectievoorwaarden en een maximumaantal omvat.

Marktstandplaatsen worden onderscheiden in dagstandplaatsen (bij winkelgebieden of verspreid bij parken/begraafplaatsen), seizoensstandplaatsen en incidentele standplaatsen. Bij winkelgebieden zijn marktstandplaatsen beperkt tot food en bloemen/planten; non-food is voorbehouden aan fysieke winkels en warenmarkten.

De Dienstenwet is van toepassing op standplaatsuitgifte: vestigingsbeperkingen moeten niet-discriminerend, noodzakelijk en evenredig zijn.

**Disambiguatie:** Dit BO heette eerder "Standplaats" maar is hernoemd naar "Marktstandplaats" om verwarring te voorkomen met [[Standplaats (BAG)]] — het BAG-objecttype voor woonwagenstandplaatsen. De GGM-entiteit "Standplaats" (RSGBPlus/BAG) verwijst naar de woonwagenstandplaats, niet naar dit concept. De marktstandplaats heeft geen directe GGM-entiteit.

## Procesbron

De marktstandplaats is een procesobject dat ontstaat in het APV-vergunningsproces. Er is geen GGM-entiteit die dit concept dekt — de GGM-entiteit "Standplaats" gaat over BAG-standplaatsen (woonwagens). De eerdere GGM-match was onjuist.

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[warenmarkt]] (compositie) | standplaats is onderdeel van warenmarkt | 0..* | beleidsbron |

## Bedrijfsprocessen

- **Standplaatsvergunningverlening** — verlening, weigering en intrekking van standplaatsvergunningen op basis van APV
- **Branchering ambulante handel** — toewijzing van branches aan standplaatsen (food, bloemen/planten, seizoensgebonden)
- **Monitoring detailhandel** — periodieke beoordeling van het standplaatsenbestand


## Bronnen

- [[Wiki/Bronsamenvattingen/Economie/economie-speerpunten-vng]]
- [[Wiki/Bronsamenvattingen/Economie/ontwikkelingskader-detailhandel-2012]]
- [[Wiki/Bronsamenvattingen/Economie/detailhandel-utrecht-2015]]
- [[Wiki/Bronsamenvattingen/Economie/horecabeleid-utrecht]]
- [[Wiki/Bronsamenvattingen/Economie/actualisatie-marktruimte-hotelnota]]
- [[Wiki/Bronsamenvattingen/Economie/beleidsregels-terrassen-utrecht]]
- [[Wiki/Bronsamenvattingen/Economie/beleidsregel-hotels-utrecht]]
- [[Wiki/Bronsamenvattingen/Economie/beleidsregels-short-stay-utrecht]]
- [[Wiki/Bronsamenvattingen/Economie/beleidsnota-werklocaties-2035]]

## Terugmelding GGM

⚠️ Het GGM mist een entiteit voor marktstandplaatsen (APV-gereguleerde ambulante handel). De bestaande GGM-entiteit "Standplaats" in RSGBPlus/BAG gaat over woonwagenstandplaatsen. Overweeg toevoeging van een entiteit "Marktstandplaats" of "StandplaatsAPV" onder Economie (taakveld 3) met attributen voor branchering, type (dag/seizoen/incidenteel) en vergunningsstatus.
