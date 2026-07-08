---
type: element
naam: Zakelijk Recht
onderwerp: [Basisregistraties, BRK]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: ZakelijkRecht
ggm_guid: EAID_8C809341_AC60_4378_8BA0_0843E8C06AF3
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram:
  - "BRK"
  - "ZAKELIJK RECHT"
  - "TENAAMSTELLING"
  - "Detaillering Kadastrale Onroerende Zaken en Rechten op hoofdlijnen"
  - "Detaillering Kadastrale Onroerende Zaken en Rechten met attributen"
  - "Ruimte WOZ en Benoemd Object"
  - "Vastgoed Domeinmodel"
ggm_diagram_ids:
  - EAID_DF9CEAAD_E574_40b3_970B_DC558AB579D0
  - EAID_A308855C_FB69_43cf_AA98_12555468AAAE
  - EAID_BAB7CC48_0969_4064_98B6_6C4F51207155
  - EAID_0A286E07_9DEF_46a8_AC66_469F5A70564E
  - EAID_FF8B8883_467A_422e_A894_C513307057AF
  - EAID_F9683FD0_4AA1_40c0_A132_4EA8F639B371
  - EAID_00D4246F_6ED7_4690_A180_ACCCD6AB1291
ggm_definitie: "Het eigendom van, of een beperkt recht van een natuurlijk of niet-natuurlijk persoon (PERSOON) op, een onroerende zaak (met uitzondering van hypotheken en beslagen)."
ggm_toelichting: "Zie de catalogus van de BRK. Rechten worden beschouwd vanuit één onroerende zaak. Recht vormt de relatie tussen één onroerende zaak en één of meer tenaamgestelde personen."
ggm_synoniemen: ""
ggm_herkomst: ""

ggm_gemma_naam: ZakelijkRecht
ggm_gemma_guid: 671ec5bd-e8ac-44d7-8a01-cc9b439c6c5f
ggm_gemma_definitie: "Het eigendom van, of een beperkt recht van een natuurlijk of niet-natuurlijk persoon (PERSOON) op, een onroerende zaak (met uitzondering van hypotheken en beslagen)."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: business-object
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-671ec5bd-e8ac-44d7-8a01-cc9b439c6c5f"
ggm_gemma_bron: "BRK"
ggm_gemma_alternate_name: "ZakelijkRecht (RSGB Model)"

ggm_duplicaat_entiteiten: []

analyse_ggm_dekking: |
  Dit BO is de hernoeming van GGM-entiteit **ZakelijkRecht**. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **AardZakelijkRecht** (classificatie) — Typering/referentietabel
  - **Appartementsrechtsplitsing** (detail) — Detailgegeven (weinig attributen)
  - **KadastraleMutatie** (detail) — Detailgegeven (geassocieerd met BO)
  - **KpBetrokkenBij** (detail) — Detailgegeven (geassocieerd met BO)
  - **KpOnstaanUit** (detail) — Detailgegeven (geassocieerd met BO)
  - **SplitsingstekeningReferentie** (detail) — Detailgegeven
bo_definitie: "Het eigendom van, of een beperkt recht van een natuurlijk of niet-natuurlijk persoon (PERSOON) op, een onroerende zaak (met uitzondering van hypotheken en beslagen)."
bo_toelichting: ''
bo_via_kandidaten:
  - ggm_entiteit: "KadastraleOnroerendeZaakAantekening"
    ggm_guid: "EAID_0BC18F79_3560_4e43_8154_7CCDC7D67A03"
    reden: "Aantekening over een feit met gevolgen voor de uitoefening van rechten op de onroerende zaak."
  - ggm_entiteit: "KoopsomKadastraleOnroerendeZaak"
    ggm_guid: "EAID_B1CB6F3A_A1F5_43f2_B077_02AD7441B1E3"
    reden: "De koopsom hangt samen met het verkregen zakelijk recht, niet met de WOZ-waardering of een zekerheidsrecht."
  - ggm_entiteit: "LocatieKadastraleOnroerendeZaak"
    ggm_guid: "EAID_1ECAEB3C_EBE2_4afb_8D34_6AFEEFDF3FCA"
    reden: "Locatieaanduiding van de onroerende zaak waarop het zakelijk recht rust."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Kadastraal Perceel]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Een zakelijk recht rust op een kadastraal perceel of appartementsrecht"
  - type: associatie
    bedrijfsobject: "[[Appartementsrecht]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Een zakelijk recht rust op een kadastraal perceel of appartementsrecht"
  - type: associatie
    bedrijfsobject: "[[Tenaamstelling]]"
    richting: naar-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Een zakelijk recht heeft een of meer tenaamstellingen"
  - type: associatie
    bedrijfsobject: "[[Stukdeel]]"
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Een zakelijk recht is gebaseerd op een of meer stukdelen"
bedrijfsprocessen:
  - WOZ-taxatie
  - OZB-heffing
  - Eigendomsverificatie
  - Erfpachtbeheer
bedrijfsfuncties:
  - Belastingheffing
  - Vastgoedbeheer
---

## BO-criteria toetsing

6/6 criteria. Zakelijk recht is het centrale concept dat vastlegt wie welk recht heeft op welk kadastraal object. Herkenbaar voor domeinexperts, eigen identificatie en levenscyclus (vestiging → overdracht → beëindiging), meervoudig (meerdere rechten per object), relaties met kadastrale objecten en personen.

## Beschrijving

Een zakelijk recht legt vast dat een persoon eigenaar is van, of een beperkt recht heeft op, een onroerende zaak. De aard van het recht kan zijn: eigendom, erfpacht, opstal, vruchtgebruik, gebruik en bewoning. De gemeente gebruikt zakelijke rechten om te bepalen wie de OZB-aanslag en WOZ-beschikking ontvangt, wie vergunninghouder kan zijn, en aan wie te handhaven. Het zakelijk recht koppelt via [[Tenaamstelling]] aan een persoon ([[Ingeschreven Persoon]] of niet-natuurlijk persoon).

## Subtypes

Herkende specialisaties van Zakelijk Recht. Gevonden in de BRK Catalogus. Geen apart BO.

- **Eigendom** — volle eigendom van een onroerende zaak
- **Erfpacht** — recht om andermans grond te gebruiken
- **Opstal** — recht om gebouwen op andermans grond te hebben
- **Vruchtgebruik** — recht om andermans zaak te gebruiken en de vruchten te genieten
- **Gebruik en bewoning** — beperkt persoonlijk gebruiksrecht

## GGM-bron

> "Het eigendom van, of een beperkt recht van een natuurlijk of niet-natuurlijk persoon (PERSOON) op, een onroerende zaak (met uitzondering van hypotheken en beslagen)."

- **Entiteit:** ZakelijkRecht
- **Beleidsdomein:** RSGBPlus (99 Kern)
- **Attributen:** identificatieZakelijkRecht, aardZakelijkRecht, datumIngangRecht, datumEindeRecht, toelichtingBewaarder
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | BO | Kardinaliteit | Bron |
|---|---|---|---|---|
| rust op | van-dit-BO | [[Kadastraal Perceel]] / [[Appartementsrecht]] | 1 | GGM |
| tenaamstelling | naar-dit-BO | [[Tenaamstelling]] | 1..* | GGM |
| is belast met | naar-dit-BO | [[Zakelijk Recht]] | 0..* | GGM (beperkt recht belast eigendom) |
| gebaseerd op | van-dit-BO | [[Stukdeel]] | 1..* | BRK Catalogus |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-brk]]
