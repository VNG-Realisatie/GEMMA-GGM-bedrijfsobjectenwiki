---
type: element
naam: Wijk
onderwerp: [Basisregistraties, BAG]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Wijk
ggm_guid: EAID_120EA50B_B9A2_4869_A3BE_46931F631D33
ggm_uml_type: Class
ggm_beleidsdomein: BAG
ggm_taakveld: "99 Kern"
ggm_diagram: ["Diagram Gebied Vestiging en Adres", "Diagram Sportbeleid Locaties", "Schouwrondes en Arealen", "Vastgoed verankering RSGB IMBAG", "BAG", "Buurten en Wijken"]
ggm_diagram_ids: ["EAID_50085E67_46AC_4f54_B204_436786266EE2", "EAID_BA23F316_FE48_49a8_A26D_9B1D14713F76", "EAID_8BE01DD9_B915_4291_B190_AB69D0252391", "EAID_FDB58817_3F2A_4d73_A7DB_7906F9B9EB45", "EAID_53E16E43_EDF1_4b47_B0DD_C77D8FEFCCA3", "EAID_5D49277A_03E6_4e94_A3EE_79627327FA9E"]
ggm_definitie: "Een aaneengesloten gedeelte van het grondgebied van een gemeente, waarvan de grenzen zo veel mogelijk zijn gebaseerd op sociaal-geografische kenmerken."
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
  - entiteit: Wijk
    guid: EAID_2F759BC4_7E3C_4ce9_94FF_33A4106A6E5A
    beleidsdomein: RSGBPlus
    taakveld: "99 Kern"
    afwijkende_attributen: "RSGBPlus gebruikt domein-geprefixte namen (geometrieWijk, datumBeginGeldigheidWijk, etc.); voegt IMGeo-identificatie toe; minder attributen (geen status, versie, Geconstateerd, datumIngang, datumEinde)"

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Wijk** als directe tegenhanger. Daarnaast is **Wijk** (beleidsdomein RSGBPlus) als vermoedelijk duplicaat gekoppeld — zie ggm_duplicaat_entiteiten.
bo_definitie: "Een aaneengesloten gedeelte van het grondgebied van een gemeente, waarvan de grenzen zo veel mogelijk zijn gebaseerd op sociaal-geografische kenmerken."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Woonplaats]]"
    richting: "naar-dit-BO"
    kardinaliteit: "1"
    beschrijving: "Een wijk ligt in precies één woonplaats"
  - type: associatie
    bedrijfsobject: "[[Buurt]]"
    richting: "van-dit-BO"
    kardinaliteit: "1..*"
    beschrijving: "Een wijk bevat een of meer buurten"
bedrijfsprocessen: [Gebiedsindeling, Wijkgericht werken, Statistiek en monitoring]
bedrijfsfuncties: [Basisregistratie, Gebiedsgericht beleid]
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis in het domein (niveau voor wijkgericht werken en statistiek), herkenbaar voor domeinexperts (wijknaam), eigen bestaan (begrensd gebied), meervoud (tientallen per gemeente), eigen levenscyclus (instellen, herindelen, opheffen), relaties met [[Woonplaats]], [[Buurt]].

## Beschrijving

Een wijk is een aaneengesloten gedeelte van het gemeentelijk grondgebied, begrensd op basis van sociaal-geografische kenmerken. Wijken vormen het middenniveau van de gebiedsindeling: ze bevatten [[Buurt]]en en liggen binnen een [[Woonplaats]].

Wijken zijn de basis voor wijkgericht werken, gebiedsbudgetten en CBS-statistieken. De wijk is geen formeel BAG-objecttype maar wordt in het GGM-BAG-beleidsdomein gemodelleerd als onderdeel van de ruimtelijke hiërarchie.

## Generalisatie

Wijk is het middenniveau van de gemeentelijke gebiedsindelingshiërarchie: [[Gemeente]] → [[Woonplaats]] → **Wijk** → [[Buurt]]. Alle niveaus delen hetzelfde patroon: code, naam, geometrie, geldigheidsperiode. Wijk onderscheidt zich door de sociaal-geografische afbakening.

## GGM-bron

> "Een aaneengesloten gedeelte van het grondgebied van een gemeente, waarvan de grenzen zo veel mogelijk zijn gebaseerd op sociaal-geografische kenmerken." (GGM, entiteit Wijk, beleidsdomein BAG)

- **Entiteit:** Wijk
- **Beleidsdomein:** BAG
- **Attributen:** wijkcode, wijknaam, geometrie, beginGeldigheid, eindGeldigheid, identificatie, datumIngang, status, datumEinde, versie, Geconstateerd
- **Matchsterkte:** exact

## GGM-duplicaten

De GGM-entiteit "Wijk" komt voor in 2 beleidsdomeinen:

| Beleidsdomein | GUID | Status |
|---|---|---|
| **BAG** | `EAID_120EA50B_B9A2_4869_A3BE_46931F631D33` | **primair** — BAG is de bronregistratie voor de gebiedsindeling |
| RSGBPlus | `EAID_2F759BC4_7E3C_4ce9_94FF_33A4106A6E5A` | duplicaat — domein-geprefixte attribuutnamen; voegt IMGeo-identificatie toe; minder attributen (geen status, versie, Geconstateerd, datumIngang, datumEinde) |

Teruggemeld als #59 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Woonplaats]] | ligt in | 1 | GGM |
| [[Buurt]] | bevat | 1..* | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bag-2018]]
