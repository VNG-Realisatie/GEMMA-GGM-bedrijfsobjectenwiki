---
type: element
naam: Warenmarkt
onderwerp: [Economie]
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
bo_definitie: "Georganiseerde, periodieke verkoop van waren op een aangewezen locatie in de openbare ruimte, bestaande uit zes of meer standplaatsen, gereguleerd via de Marktverordening."
bo_toelichting:
bedrijfsprocessen: [marktorganisatie, vergunningverlening markten, monitoring detailhandel]
bedrijfsfuncties: [economisch beleid, vergunningverlening]
bo_relaties:
  - type: compositie
    bedrijfsobject: "[[Marktstandplaats]]"
    richting: "van-dit-BO"
    kardinaliteit: "6..*"
    beschrijving: Een warenmarkt bestaat uit 6 of meer standplaatsen
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Kernbegrip in ambulante handel, gereguleerd via Marktverordening |
| Is herkenbaar voor domeinexperts | ✅ | Standaard begrip, alle gemeenten met markten |
| Heeft een eigen bestaan | ✅ | Specifieke markten op vaste locaties met eigen identiteit |
| Kan in meervoud bestaan | ✅ | 12+ in Utrecht: dagmarkten, weekmarkten, themamarkten |
| Heeft een eigen levenscyclus | ✅ | Ingesteld → actief → eventueel omgevormd of opgeheven |
| Heeft relaties met andere concepten | ✅ | Bestaat uit standplaatsen, op een locatie, gereguleerd door marktverordening |

6/6 criteria — BO.

## Beschrijving

Een warenmarkt is een georganiseerde, periodieke verkoop van waren op een door de gemeente aangewezen locatie. De Marktverordening definieert een markt als een samenstelling van zes of meer standplaatsen. Gemeenten onderscheiden dagmarkten (bijv. Vredenburg), weekmarkten en themamarkten (bloemen, boeken/antiek, streekproducten, boerenmarkten).

De warenmarkt is functioneel verbonden met het winkelgebied: de markt profiteert van de bezoekersstromen van winkels, en de marktdag is vaak een drukke dag voor omliggende winkels. De gemeente beheert markten via de Marktverordening en is verantwoordelijk voor locatiebepaling, frequentie en marktmeesterschap.

Registreerbare eigenschappen: locatie, frequentie (dag/week), type (regulier/thema), aantal kramen, branchering, openingstijden.

## Procesbron

De warenmarkt ontstaat uit het gemeentelijk marktbeleid en wordt ingesteld via de Marktverordening. Het is een dataobject dat de gemeente registreert (locatie, frequentie, type, branchering) maar dat niet in het GGM is gemodelleerd.

> "De regels voor markten staan in de Marktverordening. Van een markt is sprake bij 6 of meer standplaatsen." (bron: [[Wiki/Bronsamenvattingen/Economie/ontwikkelingskader-detailhandel-2012|Ontwikkelingskader Detailhandel 2012]])

> "In Utrecht zijn er 12 bestaande warenmarkten (zowel dag- als weekmarkten) en daarnaast nog enkele themamarkten zoals de bloemenmarkt (Janskerkhof), de lapjesmarkt (Breedstraat), de boerenmarkt (Vredenburg) en de antiek- en boekenmarkt (Mariaplaats)." (bron: Ontwikkelingskader Detailhandel 2012, §V.3)

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Marktstandplaats]] (compositie) | warenmarkt bevat standplaatsen | 6..* | beleidsbron |

## Bedrijfsprocessen

- **Marktorganisatie** — instelling, wijziging en opheffing van warenmarkten
- **Vergunningverlening markten** — vergunningen voor marktkooplieden
- **Monitoring detailhandel** — beoordeling functioneren markten in relatie tot winkelgebieden


## Bronnen

- [[Wiki/Bronsamenvattingen/Economie/ontwikkelingskader-detailhandel-2012]]

## Terugmelding GGM

⚠️ Warenmarkt ontbreekt als entiteit in het GGM. Het is een registreerbaar dataobject met eigen eigenschappen (locatie, frequentie, type, branchering) dat alle gemeenten met markten beheren. Past conceptueel in taakveld 3 Economie. Vergelijkbaar met [[Marktstandplaats]] (dat wél in het GGM staat, zij het onder Musea).
