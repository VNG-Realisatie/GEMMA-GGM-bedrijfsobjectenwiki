---
type: element
naam: Buurt
onderwerp: [Basisregistraties, BAG]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Buurt
ggm_guid: EAID_38649FF6_88C6_437d_AF8E_A9023D55E16C
ggm_uml_type: Class
ggm_beleidsdomein: BAG
ggm_taakveld: "99 Kern"
ggm_diagram: ["Objecten bij Vergunningaanvraag", "Diagram Gebied Vestiging en Adres", "Schouwrondes en Arealen", "Vastgoed verankering RSGB IMBAG", "BAG", "Buurten en Wijken"]
ggm_diagram_ids: ["EAID_C9CE09B7_32EF_40eb_9C82_7FD6EDEA1D9E", "EAID_50085E67_46AC_4f54_B204_436786266EE2", "EAID_8BE01DD9_B915_4291_B190_AB69D0252391", "EAID_FDB58817_3F2A_4d73_A7DB_7906F9B9EB45", "EAID_53E16E43_EDF1_4b47_B0DD_C77D8FEFCCA3", "EAID_5D49277A_03E6_4e94_A3EE_79627327FA9E"]
ggm_definitie: "Een aaneengesloten gedeelte van een wijk, waarvan de grenzen zo veel mogelijk gebaseerd zijn op topografische elementen."
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
  - entiteit: Buurt
    guid: EAID_67CC2144_6B88_433c_853D_07379C66D6CF
    beleidsdomein: RSGBPlus
    taakveld: "99 Kern"
    afwijkende_attributen: "RSGBPlus gebruikt domein-geprefixte namen (buurtcode, buurtnaam, buurtgeometrie, etc.); voegt IMGeo-identificatie toe; minder attributen (geen status, versie, Geconstateerd, datumIngang, datumEinde)"

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Buurt** als directe tegenhanger. Daarnaast is **Buurt** (beleidsdomein RSGBPlus) als vermoedelijk duplicaat gekoppeld — zie ggm_duplicaat_entiteiten. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Areaal** (detail) — Detailgegeven (geassocieerd met BO)
bo_definitie: "Een aaneengesloten gedeelte van een wijk, waarvan de grenzen zo veel mogelijk gebaseerd zijn op topografische elementen."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wijk]]"
    richting: "naar-dit-BO"
    kardinaliteit: "1"
    beschrijving: "Een buurt ligt in precies één wijk"
  - type: associatie
    bedrijfsobject: "[[Nummeraanduiding]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Nummeraanduidingen liggen in een buurt"
  - type: associatie
    bedrijfsobject: "[[Openbare Ruimte]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Openbare ruimten liggen in buurten"
  - type: associatie
    bedrijfsobject: "[[Pand]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Panden liggen in een buurt"
bedrijfsprocessen: [Gebiedsindeling, Wijkgericht werken, Statistiek en monitoring]
bedrijfsfuncties: [Basisregistratie, Gebiedsgericht beleid]
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis in het domein (kleinste statistische en beleidsmatige gebiedseenheid), herkenbaar voor domeinexperts (buurtnaam), eigen bestaan (begrensd gebied), meervoud (honderden per gemeente), eigen levenscyclus (instellen, herindelen, opheffen), relaties met [[Wijk]], [[Nummeraanduiding]], [[Pand]].

## Beschrijving

Een buurt is het laagste niveau van de gemeentelijke gebiedsindeling. Het is een aaneengesloten gedeelte van een [[Wijk]], begrensd op basis van topografische elementen (wegen, water, spoor). Buurten worden gebruikt voor statistiek (CBS), wijkgericht werken, en als basis voor gebiedsgericht beleid.

Elke buurt heeft een code, naam en geometrie. De buurt is geen formeel BAG-objecttype maar wordt wel in het GGM-BAG-beleidsdomein gemodelleerd als onderdeel van de ruimtelijke hiërarchie.

## Generalisatie

Buurt is het laagste niveau van de gemeentelijke gebiedsindelingshiërarchie: [[Gemeente]] → [[Woonplaats]] → [[Wijk]] → **Buurt**. Alle niveaus delen hetzelfde patroon: code, naam, geometrie, geldigheidsperiode. Buurt onderscheidt zich door de topografische afbakening (niet bestuurlijk maar fysiek begrensd).

## GGM-bron

> "Een aaneengesloten gedeelte van een wijk, waarvan de grenzen zo veel mogelijk gebaseerd zijn op topografische elementen." (GGM, entiteit Buurt, beleidsdomein BAG)

- **Entiteit:** Buurt
- **Beleidsdomein:** BAG
- **Attributen:** code, naam, geometrie, beginGeldigheid, eindGeldigheid, identificatie, datumIngang, status, datumEinde, versie, Geconstateerd
- **Matchsterkte:** exact

## GGM-duplicaten

De GGM-entiteit "Buurt" komt voor in 2 beleidsdomeinen:

| Beleidsdomein | GUID | Status |
|---|---|---|
| **BAG** | `EAID_38649FF6_88C6_437d_AF8E_A9023D55E16C` | **primair** — BAG is de bronregistratie voor de gebiedsindeling |
| RSGBPlus | `EAID_67CC2144_6B88_433c_853D_07379C66D6CF` | duplicaat — domein-geprefixte attribuutnamen (buurtcode, buurtnaam, buurtgeometrie); voegt IMGeo-identificatie toe; minder attributen (geen status, versie, Geconstateerd, datumIngang, datumEinde) |

Teruggemeld als #59 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Wijk]] | ligt in | 1 | GGM |
| [[Nummeraanduiding]] | bevat | 0..* | GGM |
| [[Openbare Ruimte]] | bevat | 0..* | GGM |
| [[Pand]] | bevat | 0..* | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bag-2018]]
