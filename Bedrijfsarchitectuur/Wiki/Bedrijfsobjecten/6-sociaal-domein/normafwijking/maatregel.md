---
type: element
naam: Maatregel
onderwerp: [werk en inkomen]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Maatregel
ggm_guid: EAID_0B63B508_9F69_A5D7_4387_2632D2C24782
ggm_uml_type: Class
ggm_beleidsdomein: Normafwijking
ggm_taakveld: Inkomen
ggm_diagram: [Normafwijking]
ggm_diagram_ids: [EAID_1818B773_1463_43c7_BACA_FEE391FE27CD]
ggm_definitie: "Een maatregel is een besluit of handeling waarmee een bestuursorgaan of rechter ingrijpt om een doel te bereiken, een probleem op te lossen of een regel te handhaven."
ggm_toelichting: "In (bestuurs)recht en beleid duidt maatregel op een actie, handeling of besluit van een overheid of instantie dat gericht is op het beïnvloeden van gedrag, de toepassing van regels of de situatie van betrokkenen. Dit kan variëren van een administratieve beslissing in een individuele zaak tot een ingreep die een persoon, organisatie of situatie raakt."
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
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Maatregel** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Afwijkende maatregel** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
  - **Maatregel op uitkering** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
  - **Verlaging door maatregel** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
bo_definitie: "Een besluit waarmee de gemeente de bijstand verlaagt omdat een bijstandsgerechtigde een aan de bijstand verbonden verplichting niet of niet behoorlijk is nagekomen."
bo_toelichting: "GGM-definitie is generiek bestuursrechtelijk (elk overheidsingrijpen); in de bijstandscontext is dit specifiek de verlaging van de uitkering op grond van art. 18 Participatiewet (afstemming) of art. 18b (onvoldoende beheersing Nederlandse taal), met percentage en duur vastgelegd in de gemeentelijke verordening (art. 8 lid 1 onderdeel a). Volgt altijd op een [[Wiki/Bedrijfsobjecten/6-sociaal-domein/normafwijking/normafwijking|Normafwijking]]."
bo_subtypes: []
bo_synoniemen:
- naam: Verlaging
  context: Participatiewet, art. 18 — de bijstandsverlaging die de maatregel bewerkstelligt
bo_homoniemen: []
element_tegenhangers: []
bo_relaties:
- type: generalisatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/normafwijking/boete|Boete]]"
  richting: van-dit-BO
  kardinaliteit:
  beschrijving: Boete is een specialisatie van Maatregel, apart gemodelleerd vanwege een ander rechtskarakter (punitief i.p.v. afstemming)
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/normafwijking/normafwijking|Normafwijking]]"
  richting: naar-dit-BO
  kardinaliteit: "1..1"
  beschrijving: Elke maatregel volgt op precies één normafwijking
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening|Inkomensvoorziening]]"
  richting: van-dit-BO
  kardinaliteit: "1..1"
  beschrijving: De maatregel verlaagt een specifieke inkomensvoorziening
bedrijfsprocessen: [afstemmingsbeoordeling, opleggen maatregel, herziening maatregel]
bedrijfsfuncties: [handhaving, inkomensondersteuning]
---

# Maatregel

Besluit waarmee de gemeente de bijstand tijdelijk verlaagt omdat een bijstandsgerechtigde een verplichting niet of niet behoorlijk is nagekomen, afgestemd op diens omstandigheden en mate van verwijtbaarheid.

## BO-criteria toetsing

| Criterium | Toets |
|---|---|
| Betekenis binnen domein | ✅ Kernbegrip in de handhaving van bijstandsverplichtingen |
| Herkenbaar voor domeinexperts | ✅ Standaardterm bij klantmanagers en in gemeentelijke maatregelenverordeningen |
| Eigen bestaan | ✅ Eigen identificatie, type, aanvangs-, vaststellings- en einddatum |
| Meervoud | ✅ Oplopende reeks maatregelen bij herhaalde niet-nakoming (art. 18 lid 5-8) |
| Levenscyclus | ✅ Vaststelling → aanvang → looptijd → einde, met mogelijkheid tot herziening bij alsnog nakomen (art. 18 lid 11) |
| Relaties | ✅ Normafwijking, Inkomensvoorziening, specialisatie Boete |

Score: **6/6**

## Beschrijving

Wanneer een [[Wiki/Bedrijfsobjecten/6-sociaal-domein/normafwijking/normafwijking|Normafwijking]] is vastgesteld en verwijtbaarheid aanwezig is, verlaagt het college de bijstand met een maatregel. De Participatiewet kent een oplopende staffel: eerste overtreding 100% gedurende 1-3 maanden (art. 18 lid 5), bij herhaling binnen 12 maanden een langere periode (lid 6), daarna telkens 3 maanden (lid 7-8). Het college stemt de maatregel af op de omstandigheden van de belanghebbende als dringende redenen daartoe noodzaken (lid 10) en kan de verlaging herzien zodra de belanghebbende de verplichtingen alsnog nakomt (lid 11). Een aparte staffel geldt bij onvoldoende beheersing van de Nederlandse taal (art. 18b): 20% (6 maanden) → 40% (6 maanden) → 100% (onbepaalde tijd).

## Subtypes

Herkende varianten uit het GGM (`Afwijkende maatregel`, `Maatregel op uitkering`) en de Participatiewet. Beide zijn parametrische varianten van hetzelfde maatregelbesluit — geen eigen identificatie of levenscyclus los van de Maatregel zelf, dus geen apart BO.

- **Maatregel op uitkering** (GGM) — de reguliere verlaging volgens de wettelijke staffel (art. 18 lid 4-8 Participatiewet): vast percentage en periode per overtreding.
- **Afwijkende maatregel** (GGM) — de op de individuele omstandigheden afgestemde variant (art. 18 lid 10 Participatiewet, "dringende redenen"): afwijkend bedrag of percentage, apart gemotiveerd.

## GGM-bron

> Een maatregel is een besluit of handeling waarmee een bestuursorgaan of rechter ingrijpt om een doel te bereiken, een probleem op te lossen of een regel te handhaven.

- **Entiteit:** Maatregel (abstract, generaliseert naar Boete, Afwijkende maatregel, Maatregel op uitkering)
- **Beleidsdomein:** Normafwijking (taakveld Inkomen, onder 6 Sociaal Domein)
- **Attributen:** Datum aanvang maatregel, Datum einde maatregel, Datum vaststelling maatregel, identificatie, Type maatregel
- **Matchsterkte:** sterk — de GGM-definitie is generiek bestuursrechtelijk geformuleerd (elk overheidsingrijpen), niet bijstand-specifiek; de bijstandscontext is toegevoegd in `bo_toelichting`.

## Relaties

| Relatie | BO | Beschrijving |
|---|---|---|
| ← | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/normafwijking/normafwijking\|Normafwijking]] | Elke maatregel volgt op een normafwijking |
| → | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/normafwijking/boete\|Boete]] | Specialisatie: bestuurlijke boete i.p.v. afstemmingsmaatregel |
| → | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]] | De maatregel verlaagt deze inkomensvoorziening |

## Bronnen

- [[Wiki/Bronsamenvattingen/Werk en Inkomen/participatiewet]]
