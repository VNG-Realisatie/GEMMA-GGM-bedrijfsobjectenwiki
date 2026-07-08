---
type: element
naam: Openbare Ruimte
onderwerp: [Basisregistraties, BAG]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: OpenbareRuimte
ggm_guid: EAID_BFE30E32_8CB9_4272_A559_9FB3FD74DACC
ggm_uml_type: Class
ggm_beleidsdomein: BAG
ggm_taakveld: "99 Kern"
ggm_diagram: ["Objecten bij Vergunningaanvraag", "Diagram Gebied Vestiging en Adres", "Diagram Monumenten", "Huishouden en Huwelijk", "Ruimte Adressen, gebouwen en terreinen", "Vastgoed verankering RSGB IMBAG"]
ggm_diagram_ids: ["EAID_C9CE09B7_32EF_40eb_9C82_7FD6EDEA1D9E", "EAID_50085E67_46AC_4f54_B204_436786266EE2", "EAID_7429E175_1CBE_4336_BF92_6C5029395E69", "EAID_CABB9F3F_A6ED_479a_A175_6F61BE2BE8F8", "EAID_7561B00D_273B_425a_B2FE_1C3AE499ED2E", "EAID_FDB58817_3F2A_4d73_A7DB_7906F9B9EB45"]
ggm_definitie: "Een openbare ruimte is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorziene buitenruimte die binnen één woonplaats is gelegen."
ggm_toelichting: "Een buitenruimte die door de gemeente als openbare ruimte is aangewezen en waaraan de gemeente een naam heeft gegeven. Een openbare ruimte ligt binnen 1 woonplaats. De BAG kent 7 soorten openbare ruimten: weg, water, spoorbaan, terrein, kunstwerk, landschappelijk gebied en administratief gebied. Een openbare ruimte is meestal een straat(naam)."
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

ggm_duplicaat_entiteiten:
  - entiteit: OpenbareRuimte
    guid: EAID_FB13857C_C695_4b53_8060_BACFA0E16950
    beleidsdomein: RSGBPlus
    taakveld: "99 Kern"
    afwijkende_attributen: "RSGBPlus gebruikt domein-geprefixte namen (IdentificatiecodeOpenbareRuimte, statusOpenbareRuimte, etc.); voegt IMGeo-identificatie toe; minder attributen (geen versie, wegsegment, straatcode, documentvelden); voegt inOnderzoek toe"

analyse_ggm_dekking: |
  Dit BO is de hernoeming van GGM-entiteit **OpenbareRuimte**. Daarnaast is **OpenbareRuimte** (beleidsdomein RSGBPlus) als vermoedelijk duplicaat gekoppeld — zie ggm_duplicaat_entiteiten.
bo_definitie: "Een openbare ruimte is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorziene buitenruimte die binnen één woonplaats is gelegen."
bo_toelichting: ''
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Woonplaats]]"
    richting: "naar-dit-BO"
    kardinaliteit: "1"
    beschrijving: "Een openbare ruimte ligt in precies één woonplaats"
  - type: associatie
    bedrijfsobject: "[[Nummeraanduiding]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Nummeraanduidingen liggen aan een openbare ruimte"
  - type: associatie
    bedrijfsobject: "[[Buurt]]"
    richting: "naar-dit-BO"
    kardinaliteit: "1..*"
    beschrijving: "Een openbare ruimte ligt in een of meer buurten"
bedrijfsprocessen: [BAG-registratie, Straatnaambeheer, Adresbeheer]
bedrijfsfuncties: [Basisregistratie]
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis in het domein (straatnaam, onderdeel van elk adres), herkenbaar voor domeinexperts (straat, plein, waterweg), eigen bestaan (benoemde buitenruimte), meervoud (duizenden per gemeente), eigen levenscyclus (vaststellen, hernoemen, intrekken), relaties met [[Woonplaats]], [[Nummeraanduiding]], [[Buurt]].

## Beschrijving

Een openbare ruimte is in de praktijk meestal een straatnaam. Het is een door de gemeente aangewezen en benoemde buitenruimte binnen één [[Woonplaats]]. De BAG kent 7 typen openbare ruimte: weg, water, spoorbaan, terrein, kunstwerk, landschappelijk gebied en administratief gebied.

Openbare ruimten vormen het middenniveau van de adresseringshiërarchie: [[Woonplaats]] → **Openbare Ruimte** → [[Nummeraanduiding]]. Elke [[Nummeraanduiding]] ligt aan precies één openbare ruimte. De vaststelling volgt uit een formeel besluit van het bevoegde gemeentelijke orgaan.

## GGM-bron

> "Een openbare ruimte is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorziene buitenruimte die binnen één woonplaats is gelegen." (GGM, entiteit OpenbareRuimte, beleidsdomein BAG)

- **Entiteit:** OpenbareRuimte
- **Beleidsdomein:** BAG
- **Attributen:** identificatie, status, naamOpenbareruimte, geconstateerd, typeOpenbareruimte, straatnaam, huisnummerranges, labelNaam, geometrie, wegsegment, begingeldigheid, eindGeldigheid, straatcode, versie, datumIngang, datumEinde, documentdatum, documentnummer
- **Matchsterkte:** exact

## GGM-duplicaten

De GGM-entiteit "OpenbareRuimte" komt voor in 2 beleidsdomeinen:

| Beleidsdomein | GUID | Status |
|---|---|---|
| **BAG** | `EAID_BFE30E32_8CB9_4272_A559_9FB3FD74DACC` | **primair** — BAG is de bronregistratie voor openbare ruimten |
| RSGBPlus | `EAID_FB13857C_C695_4b53_8060_BACFA0E16950` | duplicaat — domein-geprefixte attribuutnamen; voegt IMGeo-identificatie toe; minder attributen (geen versie, wegsegment, straatcode, documentvelden); voegt inOnderzoek toe |

Teruggemeld als #59 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Woonplaats]] | ligt in | 1 | GGM + BAG Catalogus |
| [[Nummeraanduiding]] | adresseert | 0..* | GGM + BAG Catalogus |
| [[Buurt]] | ligt in | 1..* | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bag-2018]]
