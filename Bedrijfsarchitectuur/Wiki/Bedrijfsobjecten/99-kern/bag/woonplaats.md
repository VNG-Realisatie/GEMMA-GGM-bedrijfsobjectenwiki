---
type: element
naam: Woonplaats
onderwerp: [Basisregistraties, BAG]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Woonplaats
ggm_guid: EAID_24BDA4BA_CFCC_4e3f_8305_671F4ED7C502
ggm_uml_type: Class
ggm_beleidsdomein: BAG
ggm_taakveld: "99 Kern"
ggm_diagram: ["Vastgoed verankering RSGB IMBAG", "BAG", "ONDERZOEK", "Buurten en Wijken", "Kern:Gemeente Wijk en buurt", "Detaillering adressen, gebouwen en terreinen op hoofdlijnen"]
ggm_diagram_ids: ["EAID_FDB58817_3F2A_4d73_A7DB_7906F9B9EB45", "EAID_53E16E43_EDF1_4b47_B0DD_C77D8FEFCCA3", "EAID_9B0FEF1A_4146_409e_8B71_B12D4B4AB8A8", "EAID_5D49277A_03E6_4e94_A3EE_79627327FA9E", "EAID_29EB3097_1D02_4f00_8E7D_74A901E0FFCB", "EAID_00CCCF33_A542_47e6_AFA6_2F9F4E2670D8"]
ggm_definitie: "Een woonplaats is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorzien gedeelte van het grondgebied van de gemeente."
ggm_toelichting: "Een stuk grond binnen de gemeente dat als woonplaats is aangewezen en waaraan de gemeente ook een naam heeft gegeven."
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
  - entiteit: Woonplaats
    guid: EAID_039AFF88_F5F7_4c1a_B7E4_1BDFC495F67A
    beleidsdomein: RSGBPlus
    taakveld: "99 Kern"
    afwijkende_attributen: "RSGBPlus gebruikt domein-geprefixte namen (woonplaatsIdentificatie, woonplaatsStatus, etc.); minder attributen (geen versie, voorkomen, tijdstipRegistratie, eindRegistratie, tijdstipActief, documentvelden); voegt inOnderzoek toe"

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Woonplaats** als directe tegenhanger. Daarnaast is **Woonplaats** (beleidsdomein RSGBPlus) als vermoedelijk duplicaat gekoppeld — zie ggm_duplicaat_entiteiten. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **GeboorteIngeschrevenNatuurlijkPersoon** (detail) — Detailgegeven
  - **OntbindingHuwelijk/geregistreerdPartnerschap** (onderdeel) — Onderdeel (naamindicatie)
  - **OverlijdenIngeschrevenNatuurlijkPersoon** (detail) — Detailgegeven
  - **Postadres** (detail) — Detailgegeven
bo_definitie: "Een woonplaats is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorzien gedeelte van het grondgebied van de gemeente."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Openbare Ruimte]]"
    richting: "van-dit-BO"
    kardinaliteit: "1..*"
    beschrijving: "Een woonplaats bevat een of meer openbare ruimten"
  - type: associatie
    bedrijfsobject: "[[Gemeente]]"
    richting: "naar-dit-BO"
    kardinaliteit: "1"
    beschrijving: "Een woonplaats ligt in een gemeente"
  - type: associatie
    bedrijfsobject: "[[Wijk]]"
    richting: "van-dit-BO"
    kardinaliteit: "1..*"
    beschrijving: "Een woonplaats bevat wijken"
  - type: associatie
    bedrijfsobject: "[[Nummeraanduiding]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Nummeraanduidingen kunnen in een woonplaats liggen"
bedrijfsprocessen: [BAG-registratie, Adresbeheer]
bedrijfsfuncties: [Basisregistratie]
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis in het domein (onderdeel van elk adres), herkenbaar voor domeinexperts (plaatsnaam), eigen bestaan (geografisch begrensd gebied), meervoud (meerdere woonplaatsen per gemeente mogelijk), eigen levenscyclus (aanwijzen, hernoemen, intrekken), relaties met [[Openbare Ruimte]], [[Gemeente]], [[Nummeraanduiding]].

## Beschrijving

Een woonplaats is het hoogste niveau in de BAG-adresseringshiërarchie. Het is een door de gemeente aangewezen en benoemd gedeelte van het grondgebied. Elke [[Openbare Ruimte]] ligt in precies één woonplaats. De woonplaats bepaalt het eerste deel van een adres.

Een gemeente kan meerdere woonplaatsen bevatten, maar een woonplaats hoort bij precies één gemeente. De indeling volgt uit formele aanwijzing door het bevoegde gemeentelijke orgaan.

## Generalisatie

Woonplaats is onderdeel van de gemeentelijke gebiedsindelingshiërarchie: [[Gemeente]] → **Woonplaats** → [[Wijk]] → [[Buurt]]. Alle niveaus delen hetzelfde patroon: code, naam, geometrie, geldigheidsperiode, formele aanwijzing. Woonplaats onderscheidt zich doordat het een formeel BAG-objecttype is met wettelijke status.

## GGM-bron

> "Een woonplaats is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorzien gedeelte van het grondgebied van de gemeente." (GGM, entiteit Woonplaats, beleidsdomein BAG)

- **Entiteit:** Woonplaats
- **Beleidsdomein:** BAG
- **Attributen:** identificatie, woonplaatsnaam, woonplaatsnaamNEN, geconstateerd, status, geometrie, beginGeldigheid, eindGeldigheid, datumIngang, datumEinde, versie, documentnummer, documentdatum, voorkomen, tijdstipRegistratie, eindRegistratie, tijdstipActief
- **Matchsterkte:** exact

## GGM-duplicaten

De GGM-entiteit "Woonplaats" komt voor in 2 beleidsdomeinen:

| Beleidsdomein | GUID | Status |
|---|---|---|
| **BAG** | `EAID_24BDA4BA_CFCC_4e3f_8305_671F4ED7C502` | **primair** — BAG is de bronregistratie voor woonplaatsen |
| RSGBPlus | `EAID_039AFF88_F5F7_4c1a_B7E4_1BDFC495F67A` | duplicaat — domein-geprefixte attribuutnamen; minder attributen (geen versie, voorkomen, tijdstipRegistratie, eindRegistratie, documentvelden); voegt inOnderzoek toe |

Teruggemeld als #59 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Openbare Ruimte]] | bevat | 1..* | GGM + BAG Catalogus |
| [[Gemeente]] | ligt in | 1 | GGM |
| [[Wijk]] | bevat | 1..* | GGM |
| [[Nummeraanduiding]] | wordt geadresseerd in | 0..* | GGM + BAG Catalogus |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bag-2018]]
