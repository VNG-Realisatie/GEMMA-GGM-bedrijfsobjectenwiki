---
type: element
naam: Nummeraanduiding
onderwerp: [Basisregistraties, BAG]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Nummeraanduiding
ggm_guid: EAID_32A22BC6_89EC_44af_8D7D_79B12311AE2D
ggm_uml_type: Class
ggm_beleidsdomein: BAG
ggm_taakveld: "99 Kern"
ggm_diagram: ["Verkamering en Woonoverlast", "KVK", "Diagram Gebied Vestiging en Adres", "Diagram Monumenten", "Vroegsignalering", "Huishouden en Huwelijk"]
ggm_diagram_ids: ["EAID_B039478A_DAF7_458f_A7C7_E4744EC08DBF", "EAID_FC491653_1FBF_412a_A939_A705D501AE48", "EAID_50085E67_46AC_4f54_B204_436786266EE2", "EAID_7429E175_1CBE_4336_BF92_6C5029395E69", "EAID_07334A5A_E2F0_41ce_8510_B41BAF6876BD", "EAID_CABB9F3F_A6ED_479a_A175_6F61BE2BE8F8"]
ggm_definitie: "Een nummeraanduiding is een door het bevoegde gemeentelijke orgaan als zodanig toegekende aanduiding van een verblijfsobject, een standplaats of een ligplaats."
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

ggm_duplicaat_entiteiten:
  - entiteit: Nummeraanduiding
    guid: EAID_31A87864_6CE0_4e93_A493_ECD0FBDD4461
    beleidsdomein: RSGBPlus
    taakveld: "99 Kern"
    afwijkende_attributen: "RSGBPlus gebruikt domein-geprefixte geldigheidsvelden (datumBeginGeldigheidNummeraanduiding, etc.); minder attributen (geen versie, geometrie, documentvelden); voegt inOnderzoek toe"

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Nummeraanduiding** als directe tegenhanger. Daarnaast is **Nummeraanduiding** (beleidsdomein RSGBPlus) als vermoedelijk duplicaat gekoppeld — zie ggm_duplicaat_entiteiten. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Adresaanduiding** (detail) — Detailgegeven
  - **Briefadres** (detail) — Detailgegeven
  - **NADAanvullingBRP** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
  - **OverigeAdresseerbaarObjectAanduiding** (detail) — Detailgegeven
bo_definitie: "Een nummeraanduiding is een door het bevoegde gemeentelijke orgaan als zodanig toegekende aanduiding van een verblijfsobject, een standplaats of een ligplaats."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Openbare Ruimte]]"
    richting: "naar-dit-BO"
    kardinaliteit: "1"
    beschrijving: "Een nummeraanduiding ligt aan precies één openbare ruimte"
  - type: associatie
    bedrijfsobject: "[[Woonplaats]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..1"
    beschrijving: "Een nummeraanduiding ligt optioneel in een woonplaats (anders via openbare ruimte)"
  - type: associatie
    bedrijfsobject: "[[Verblijfsobject]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..1"
    beschrijving: "Hoofdadres of nevenadres van een verblijfsobject"
  - type: associatie
    bedrijfsobject: "[[Ligplaats]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..1"
    beschrijving: "Hoofdadres of nevenadres van een ligplaats"
  - type: associatie
    bedrijfsobject: "[[Standplaats]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..1"
    beschrijving: "Hoofdadres of nevenadres van een standplaats"
  - type: associatie
    bedrijfsobject: "[[Buurt]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..1"
    beschrijving: "Een nummeraanduiding ligt in een buurt"
bedrijfsprocessen: [BAG-registratie, Adresbeheer, BRP-adresregistratie, WOZ-waardering, Vergunningverlening]
bedrijfsfuncties: [Basisregistratie]
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis in het domein (het formele adres, koppelpunt tussen alle registraties), herkenbaar voor domeinexperts (huisnummer + postcode), eigen bestaan (formeel toegekende aanduiding), meervoud (tienduizenden per gemeente), eigen levenscyclus (toekennen, wijzigen, intrekken), relaties met [[Openbare Ruimte]], [[Verblijfsobject]], [[Ligplaats]], [[Standplaats]].

## Beschrijving

Een nummeraanduiding is het formele adres in de BAG. Het bestaat uit een huisnummer, optioneel een huisletter en huisnummertoevoeging, en een postcode. Elke nummeraanduiding ligt aan precies één [[Openbare Ruimte]] en hoort bij precies één adresseerbaar object ([[Verblijfsobject]], [[Ligplaats]] of [[Standplaats]]).

Het adres is het universele koppelpunt in de gemeentelijke informatiehuishouding: personen worden ingeschreven op een nummeraanduiding (BRP), WOZ-objecten worden eraan gekoppeld, vergunningen verwijzen ernaar. Elk adresseerbaar object heeft precies één hoofdadres; nevenadressen zijn alleen toegestaan bij meerdere relevante toegangen met wezenlijke betekenis.

## GGM-bron

> "Een nummeraanduiding is een door het bevoegde gemeentelijke orgaan als zodanig toegekende aanduiding van een verblijfsobject, een standplaats of een ligplaats." (GGM, entiteit Nummeraanduiding, beleidsdomein BAG)

- **Entiteit:** Nummeraanduiding
- **Beleidsdomein:** BAG
- **Attributen:** huisletter, huisnummer, huisnummertoevoeging, postcode, beginGeldigheid, eindeGeldigheid, status, geconstateerd, identificatie, typeAdresseerbaarObject, datumIngang, datumEinde, versie, geometrie, documentdatum, documentnummer
- **Matchsterkte:** exact

## GGM-duplicaten

De GGM-entiteit "Nummeraanduiding" komt voor in 2 beleidsdomeinen:

| Beleidsdomein | GUID | Status |
|---|---|---|
| **BAG** | `EAID_32A22BC6_89EC_44af_8D7D_79B12311AE2D` | **primair** — BAG is de bronregistratie voor adresgegevens |
| RSGBPlus | `EAID_31A87864_6CE0_4e93_A493_ECD0FBDD4461` | duplicaat — domein-geprefixte geldigheidsvelden; minder attributen (geen versie, geometrie, documentvelden); voegt inOnderzoek toe |

Teruggemeld als #59 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Openbare Ruimte]] | ligt aan | 1 | GGM + BAG Catalogus |
| [[Woonplaats]] | ligt in | 0..1 | GGM + BAG Catalogus |
| [[Verblijfsobject]] | is adres van | 0..1 | GGM + BAG Catalogus |
| [[Ligplaats]] | is adres van | 0..1 | GGM + BAG Catalogus |
| [[Standplaats]] | is adres van | 0..1 | GGM + BAG Catalogus |
| [[Buurt]] | ligt in | 0..1 | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bag-2018]]
