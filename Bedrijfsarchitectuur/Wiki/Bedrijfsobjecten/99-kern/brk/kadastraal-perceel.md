---
type: element
naam: Kadastraal Perceel
onderwerp: [Basisregistraties, BRK]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: KadastraalPerceel
ggm_guid: EAID_172AFD36_B400_4660_BFAC_4BBC1077D666
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram:
  - "BRK"
  - "KADASTRAAL PERCEEL"
  - "Detaillering Kadastrale Onroerende Zaken en Rechten op hoofdlijnen"
  - "Detaillering Kadastrale Onroerende Zaken en Rechten met attributen"
  - "Ruimte WOZ en Benoemd Object"
  - "Objecten bij Vergunningaanvraag"
ggm_diagram_ids:
  - EAID_DF9CEAAD_E574_40b3_970B_DC558AB579D0
  - EAID_27591AAC_E9E2_4266_8413_3EBD07DA5D11
  - EAID_0A286E07_9DEF_46a8_AC66_469F5A70564E
  - EAID_FF8B8883_467A_422e_A894_C513307057AF
  - EAID_F9683FD0_4AA1_40c0_A132_4EA8F639B371
  - EAID_C9CE09B7_32EF_40eb_9C82_7FD6EDEA1D9E
ggm_definitie: "Een KADASTRALE ONROERENDE ZAAK dat een kadastraal geïdentificeerd en met kadastrale grenzen begrensd deel van het Nederlands grondgebied betreft (art. 1 lid 1 Kadasterwet)."
ggm_toelichting: "Een KADASTRAAL PERCEEL behoort tezamen met het APPARTEMENTSRECHT tot de generalisatie KADASTRALE ONROERENDE ZAAK. Percelen worden cartografisch gerepresenteerd door een tweedimensionale vlakbegrenzing."
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam: KadastraalPerceel
ggm_gemma_guid: "0fd3695d-aa71-4f35-a8bf-7886c70e0ed8"
ggm_gemma_definitie: "Een KADASTRALE ONROERENDE ZAAK dat een kadastraal geïdentificeerd en met kadastrale grenzen begrensd deel van het Nederlands grondgebied betreft (art. 1 lid 1 Kadasterwet)."
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-0fd3695d-aa71-4f35-a8bf-7886c70e0ed8"
ggm_gemma_bron: "BRK."
ggm_gemma_alternate_name:

ggm_duplicaat_entiteiten: []

analyse_ggm_dekking: |
  Dit BO is de hernoeming van GGM-entiteit **KadastraalPerceel**.
bo_definitie: "Een KADASTRALE ONROERENDE ZAAK dat een kadastraal geïdentificeerd en met kadastrale grenzen begrensd deel van het Nederlands grondgebied betreft (art. 1 lid 1 Kadasterwet)."
bo_toelichting:
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Kadastraal Perceel]]"
    richting: naar-dit-BO
    kardinaliteit:
    beschrijving: "Specialisatie van KadastraleOnroerendeZaak (abstract)"
  - type: associatie
    bedrijfsobject: "[[Zakelijk Recht]]"
    richting: naar-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Op een perceel rusten een of meer zakelijke rechten"
  - type: associatie
    bedrijfsobject: "[[Zekerheidsrecht]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Op een perceel kan een zekerheidsrecht rusten (hypotheek/beslag)"
  - type: associatie
    bedrijfsobject: "[[Publiekrechtelijke Beperking]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een perceel kan onderwerp zijn van publiekrechtelijke beperkingen"
  - type: associatie
    bedrijfsobject: "[[WOZ-object]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een perceel kan onderdeel zijn van een of meer WOZ-objecten"
bedrijfsprocessen:
  - WOZ-taxatie
  - OZB-heffing
  - Vergunningverlening
  - Bestemmingsplantoetsing
  - Grondtransacties
bedrijfsfuncties:
  - Belastingheffing
  - Ruimtelijke ordening
  - Vergunningverlening
---

## BO-criteria toetsing

6/6 criteria. Kadastraal perceel is een concreet, identificeerbaar registratieobject met kadastrale aanduiding, eigen levenscyclus (ontstaan door splitsing/samenvoeging, beëindigd door samenvoeging), meervoudig (miljoenen percelen), en relaties met zakelijke rechten, personen, WOZ-objecten en publiekrechtelijke beperkingen.

## Beschrijving

Een kadastraal perceel is een stuk grond dat door het Kadaster is geïdentificeerd en begrensd. Elk perceel heeft een unieke kadastrale aanduiding (gemeente, sectie, perceelnummer) en een kadastrale grootte. De gemeente gebruikt perceelgegevens voor bestemmingsplantoetsing, vergunningverlening, WOZ-waardering, OZB-heffing en grondbeleid. Percelen vormen samen met [[Appartementsrecht|appartementsrechten]] de concrete specialisaties van het abstracte type Kadastrale Onroerende Zaak.

## Generalisatie

Kadastraal Perceel is een specialisatie van KadastraleOnroerendeZaak (abstract in GGM). De hiërarchie: **KadastraleOnroerendeZaak** → **Kadastraal Perceel** / [[Appartementsrecht]]. Alle niveaus delen: kadastrale aanduiding, relaties met zakelijke rechten en tenaamstellingen.

## GGM-bron

> "Een KADASTRALE ONROERENDE ZAAK dat een kadastraal geïdentificeerd en met kadastrale grenzen begrensd deel van het Nederlands grondgebied betreft (art. 1 lid 1 Kadasterwet)."

- **Entiteit:** KadastraalPerceel
- **Beleidsdomein:** RSGBPlus (99 Kern)
- **Attributen:** begrenzingPerceel, indicatieDeelperceel, omschrijvingDeelperceel, groottePerceel, aanduidingSoortGrootte, plaatscoordinatenPerceel
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | BO | Kardinaliteit | Bron |
|---|---|---|---|---|
| rust op | naar-dit-BO | [[Zakelijk Recht]] | 1..* | GGM |
| rust op | naar-dit-BO | [[Zekerheidsrecht]] | 0..* | GGM |
| beperkt | naar-dit-BO | [[Publiekrechtelijke Beperking]] | 0..* | BRK Catalogus |
| WOZ-koppeling | naar-dit-BO | [[WOZ-object]] | 0..* | GGM |
| gebaseerd op | van-dit-BO | [[Stukdeel]] | 0..* | BRK Catalogus |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-brk]]
