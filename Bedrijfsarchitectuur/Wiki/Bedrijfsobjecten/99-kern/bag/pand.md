---
type: element
naam: Pand
onderwerp: [Basisregistraties, BAG]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Pand
ggm_guid: EAID_11595AD8_CE67_40dd_BDA9_489DC7D244ED
ggm_uml_type: Class
ggm_beleidsdomein: BAG
ggm_taakveld: "99 Kern"
ggm_diagram: ["Objecten bij Vergunningaanvraag", "Hoofdobjecten IMGeo en Beheerobjecten", "Vastgoed verankering RSGB IMBAG", "Vastgoed WOZ", "BAG", "ONDERZOEK"]
ggm_diagram_ids: ["EAID_C9CE09B7_32EF_40eb_9C82_7FD6EDEA1D9E", "EAID_4896574A_C4DD_4b27_A3B9_4481F4B29CCB", "EAID_FDB58817_3F2A_4d73_A7DB_7906F9B9EB45", "EAID_0CF01F05_D23F_454a_A0CD_042C2DD9EE7D", "EAID_53E16E43_EDF1_4b47_B0DD_C77D8FEFCCA3", "EAID_9B0FEF1A_4146_409e_8B71_B12D4B4AB8A8"]
ggm_definitie: "Een pand is een kleinste bij de totstandkoming functioneel en bouwkundig-constructief zelfstandige eenheid die direct en duurzaam met de aarde is verbonden en betreedbaar en afsluitbaar is."
ggm_toelichting: "Een zelfstandig bouwwerk, zowel zelfstandig in de manier hoe het is gebouwd als waarvoor het is bedoeld om te gebruiken. Een pand voldoet ook aan de volgende eisen: een pand is direct en voor lange tijd met de aarde verbonden (een pand is niet makkelijk te verplaatsen) en een pand kun je binnengaan en afsluiten."
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

ggm_duplicaat_entiteiten:
  - entiteit: Pand
    guid: EAID_26D1113F_F7B3_4bdd_9AAE_EA14CC9F3C3F
    beleidsdomein: RSGBPlus
    taakveld: "99 Kern"
    afwijkende_attributen: "RSGBPlus gebruikt domein-geprefixte namen (pandidentificatie, pandstatus, etc.) en voegt LOD1/2/3-geometrie, IMGeo-identificatie en inwinningGeometrie toe; mist versie/datumIngang/datumEinde"

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Pand** als directe tegenhanger. Daarnaast is **Pand** (beleidsdomein RSGBPlus) als vermoedelijk duplicaat gekoppeld — zie ggm_duplicaat_entiteiten.
bo_definitie: "Een pand is een kleinste bij de totstandkoming functioneel en bouwkundig-constructief zelfstandige eenheid die direct en duurzaam met de aarde is verbonden en betreedbaar en afsluitbaar is."
bo_toelichting:
bo_relaties:
  - type: compositie
    bedrijfsobject: "[[Verblijfsobject]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Een pand bevat nul of meer verblijfsobjecten"
  - type: associatie
    bedrijfsobject: "[[WOZ-object]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "WOZ-objecten kunnen gekoppeld zijn aan panden"
  - type: associatie
    bedrijfsobject: "[[Nummeraanduiding]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Panden zonder verblijfsobjecten worden via nummeraanduiding geadresseerd"
  - type: associatie
    bedrijfsobject: "[[Buurt]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..1"
    beschrijving: "Pand ligt in een buurt"
bedrijfsprocessen: [BAG-registratie, Bouwvergunningverlening, WOZ-waardering, Vastgoedbeheer]
bedrijfsfuncties: [Basisregistratie, Vergunningverlening, Belastingheffing]
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis in het domein (kern BAG-object, fundament voor WOZ, vergunningen, vastgoed), herkenbaar voor domeinexperts (universeel begrepen), eigen bestaan (fysiek bouwwerk), meervoud (tienduizenden per gemeente), eigen levenscyclus (bouwvergunning verleend → in aanbouw → in gebruik → gesloopt), relaties met [[Verblijfsobject]], [[WOZ-object]], [[Nummeraanduiding]].

## Beschrijving

Een pand is de basisregistratie-eenheid voor gebouwen. Het is de kleinste bouwkundige eenheid die zelfstandig staat: het kan niet worden opgesplitst in kleinere panden. Een pand bevat nul of meer [[Verblijfsobject]]en — een leeg bedrijfspand heeft geen verblijfsobjecten, een flatgebouw heeft er veel.

De gemeente registreert panden in de BAG op basis van vergunningen en constateringen. De afbakening volgt gedetailleerde regels: bouwkundig-constructief zelfstandig (sloping raakt geen buren), functioneel zelfstandig, direct en duurzaam met de aarde verbonden, omsloten en dicht, betreedbaar, en de kleinste mogelijke eenheid. Verplaatsbare bouwwerken (units, containers) zijn geen pand. Hobbykassen en bunkers (tot ingebruikname) ook niet.

Panden zijn het koppelpunt voor WOZ-waardering, omgevingsvergunningen, monumentenstatus, en beheer openbare ruimte.

## GGM-bron

> "Een pand is een kleinste bij de totstandkoming functioneel en bouwkundig-constructief zelfstandige eenheid die direct en duurzaam met de aarde is verbonden en betreedbaar en afsluitbaar is." (GGM, entiteit Pand, beleidsdomein BAG)

- **Entiteit:** Pand
- **Beleidsdomein:** BAG
- **Attributen:** identificatie, status, statusVoortgangBouw, oorspronkelijkBouwjaar, oppervlakte, brutoInhoudPand, geconstateerd, hoogsteBouwlaag, laagsteBouwlaag, geometrieBovenaanzicht, geometrieMaaiveld, relatieveHoogteligging, documentnummer, documentdatum, beginGeldigheid, eindGeldigheid, geometriePunt, datumIngang, versie, datumEinde
- **Matchsterkte:** exact

## GGM-duplicaten

De GGM-entiteit "Pand" komt voor in 2 beleidsdomeinen:

| Beleidsdomein | GUID | Status |
|---|---|---|
| **BAG** | `EAID_11595AD8_CE67_40dd_BDA9_489DC7D244ED` | **primair** — BAG is de bronregistratie voor gebouwen |
| RSGBPlus | `EAID_26D1113F_F7B3_4bdd_9AAE_EA14CC9F3C3F` | duplicaat — domein-geprefixte attribuutnamen (pandidentificatie, pandstatus); voegt LOD1/2/3-geometrie en IMGeo-identificatie toe die BAG niet heeft |

RSGBPlus voegt 3D-geometrieën (LOD1, LOD2, LOD3) en inwinningGeometrie toe die de BAG-entiteit niet heeft. Dit zijn IMGeo-uitbreidingen bovenop de BAG-kern.

Teruggemeld als #59 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Verblijfsobject]] | bevat | 0..* | GGM + BAG Catalogus |
| [[WOZ-object]] | wordt gewaardeerd als | 0..* | GGM |
| [[Nummeraanduiding]] | heeft als adres | 0..* | GGM |
| [[Buurt]] | ligt in | 0..1 | GGM |

## Bedrijfsprocessen

- **BAG-registratie** — bijhouden van pandgegevens op basis van vergunningen, constateringen en terugmeldingen
- **Bouwvergunningverlening** — omgevingsvergunning leidt tot nieuw pand in BAG
- **WOZ-waardering** — pand is basis voor objectafbakening WOZ
- **Vastgoedbeheer** — gemeentelijk vastgoed geregistreerd als panden

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bag-2018]]
