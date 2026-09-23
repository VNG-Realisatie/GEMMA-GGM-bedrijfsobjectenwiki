---
type: element
naam: Subsidie
onderwerp: [recht]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Subsidie
ggm_guid: EAID_FD701A55_6865_44aa_9A73_C46E02481796
ggm_uml_type: Class
ggm_beleidsdomein: Subsidies
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Subsidies, Subsidie en Kostenplaats]
ggm_diagram_ids: [EAID_F408BDED_51D4_4204_9B95_F0C6C2474DC3, EAID_ACD61AD1_1B3D_46aa_96E7_F438387BE495]
ggm_definitie: "Aan derden toegekende financiële middelen, bestemd voor het uitvoeren van bepaalde activiteiten"
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam: Subsidie
ggm_gemma_guid: "1fe5c807-e9a7-4f44-a2b6-816341875d6e"
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-1fe5c807-e9a7-4f44-a2b6-816341875d6e"
ggm_gemma_bron:
ggm_gemma_alternate_name:

ggm_duplicaat_entiteiten: []

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Subsidie** als directe tegenhanger.
bo_definitie: "Aan derden toegekende financiële middelen, bestemd voor het uitvoeren van bepaalde activiteiten."
bo_toelichting:
bo_subtypes: []
bo_via_kandidaten: []
bo_synoniemen: []
bo_homoniemen: []
element_tegenhangers: []
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/politiek/partijsubsidie|Partijsubsidie]]"
    richting: van-dit-BO
    kardinaliteit:
    beschrijving: "Partijsubsidie is een specialisatie van Subsidie (bedrijfsniveau, geen GGM-generalisatie)"
  - type: generalisatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/loonkostensubsidie|Loonkostensubsidie]]"
    richting: van-dit-BO
    kardinaliteit:
    beschrijving: "Loonkostensubsidie is een specialisatie van Subsidie (bedrijfsniveau, geen GGM-generalisatie — eigen GGM-entiteit in beleidsdomein Werk)"
  - type: generalisatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/sloopregeling|Sloopregeling]]"
    richting: van-dit-BO
    kardinaliteit:
    beschrijving: "Sloopregeling is een specialisatie van Subsidie (bedrijfsniveau, geen GGM-generalisatie)"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/subsidies/subsidieaanvraag|Subsidieaanvraag]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "aanvraag die kan leiden tot een subsidie"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/subsidies/subsidiebeschikking|Subsidiebeschikking]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "besluit dat de subsidie toekent of afwijst"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/kostenplaats|Kostenplaats]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "financiële administratie van de subsidie"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak|Zaak]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "subsidieproces doorlopen als zaak"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document|Document]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "onderliggende stukken (aanvraagformulier, jaarrekening, verantwoording)"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/medewerker|Medewerker]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "behandelend medewerker"
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

| Criterium | Toets |
|---|---|
| Heeft betekenis binnen het onderwerp | ✅ Kernbegrip van het subsidierecht: financieel beleidsinstrument waarmee de gemeente activiteiten van derden ondersteunt |
| Is herkenbaar voor domeinexperts | ✅ Subsidiejuristen en -medewerkers werken dagelijks met het begrip |
| Heeft een eigen bestaan | ✅ Bestaat onafhankelijk van de aanvraag die eraan voorafging en de beschikking die het toekent |
| Kan in meervoud bestaan | ✅ Een gemeente verstrekt tegelijk vele subsidies aan verschillende ontvangers |
| Heeft een eigen levenscyclus | ✅ Aanvraag → beschikking (toekenning/afwijzing) → verstrekking (voorschotten) → verantwoording → vaststelling |
| Heeft relaties met andere concepten | ✅ Met Subsidieaanvraag, Subsidiebeschikking, Kostenplaats, Zaak, Document, Medewerker en de ontvangende rechtspersoon |

Score: 6/6

## Beschrijving

Een subsidie is de financiële tegemoetkoming die de gemeente aan een derde (rechtspersoon of natuurlijk persoon) toekent voor het uitvoeren van bepaalde activiteiten, zonder dat daar een tegenprestatie in de vorm van een levering aan de gemeente tegenover staat. Subsidies vormen een belangrijk beleidsinstrument: de gemeente stuurt met subsidievoorwaarden op maatschappelijke doelen zonder de uitvoering zelf ter hand te nemen.

De VNG ondersteunt gemeenten met de Model Algemene subsidieverordening (ASV), die onder meer inzet op proportionaliteit tussen subsidiebedrag en administratieve lasten: bij lagere subsidiebedragen gelden minder strenge verantwoordingsplichten. De ASV vormt daarmee het governance-kader waarbinnen het bedrijfsobject Subsidie wordt toegepast; de verordening zelf is geen bedrijfsobject maar het juridisch instrument dat het proces normeert.

De gemeente kent daarnaast specifieke, wettelijk of beleidsmatig genormeerde subsidievormen met een eigen BO-pagina: [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/politiek/partijsubsidie|Partijsubsidie]] (subsidie aan decentrale politieke partijen), [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/loonkostensubsidie|Loonkostensubsidie]] (Participatiewet) en [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/sloopregeling|Sloopregeling]] (subsidie aan inwoners bij milieuzone-aanscherping). Het GGM modelleert deze niet als specialisatie van de generieke entiteit Subsidie (geen generalisatierelatie in het XMI, en Loonkostensubsidie heeft zelfs een eigen GGM-entiteit in een ander beleidsdomein). Op bedrijfsniveau zijn het wél specialisaties van Subsidie — vastgelegd als generalisatie-relatie (zie Specialisaties), met Subsidie als het generieke beleidsinstrument waar de ASV op van toepassing is.

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/politiek/partijsubsidie\|Partijsubsidie]] | Subsidie aan decentrale politieke partijen | — (geen GGM-entiteit) |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/loonkostensubsidie\|Loonkostensubsidie]] | Tegemoetkoming aan werkgever bij verminderde loonwaarde werknemer | Loonkostensubsidie (beleidsdomein Werk, ander taakveld) |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/sloopregeling\|Sloopregeling]] | Subsidie aan inwoners voor voertuigvervanging bij milieuzone-aanscherping | — (geen GGM-entiteit) |

## GGM-bron

> "Aan derden toegekende financiële middelen, bestemd voor het uitvoeren van bepaalde activiteiten."
> — GGM, entiteit *Subsidie*, beleidsdomein Subsidies (taakveld 9 Interne Organisatie)

**Matchsterkte:** exact — de GGM-entiteit beschrijft precies het concept van de subsidie zoals de bron het beschrijft.

**Attributen (GGM, selectie):** subsidiebedrag, subsidiesoort, status, datumStart, datumEinde, deadlineIndiening, coFinanciering, hoogteSubsidie, datumSubsidievaststelling, subsidievaststellingBedrag, ontvangenBedrag, socialReturnVerplichting, doelstelling.

## Relaties

| Gerelateerd BO | Relatie | Richting | Bron |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/politiek/partijsubsidie\|Partijsubsidie]] | is specialisatie van Subsidie | Subsidie → Partijsubsidie | Bedrijfsniveau (geen GGM-generalisatie) |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/loonkostensubsidie\|Loonkostensubsidie]] | is specialisatie van Subsidie | Subsidie → Loonkostensubsidie | Bedrijfsniveau (geen GGM-generalisatie) |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/sloopregeling\|Sloopregeling]] | is specialisatie van Subsidie | Subsidie → Sloopregeling | Bedrijfsniveau (geen GGM-generalisatie) |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/subsidies/subsidieaanvraag\|Subsidieaanvraag]] | aanvraag die kan leiden tot een subsidie | Subsidieaanvraag → Subsidie | GGM |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/subsidies/subsidiebeschikking\|Subsidiebeschikking]] | besluit dat de subsidie toekent of afwijst | Subsidiebeschikking → Subsidie | GGM |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/kostenplaats\|Kostenplaats]] | financiële administratie | Subsidie → Kostenplaats | GGM |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] | subsidieproces als zaak | Subsidie → Zaak | GGM |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document\|Document]] | onderliggende stukken | Subsidie → Document | GGM |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/medewerker\|Medewerker]] | behandelend medewerker | Subsidie → Medewerker | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Recht/subsidierecht]]

## Terugmelding GGM

Het GGM-beleidsdomein Subsidies bevat naast Subsidie, Subsidieaanvraag en Subsidiebeschikking ook Subsidieprogramma, Subsidiecomponent en de enumeratie Subsidieniveau. Deze bron (een korte VNG-rubriekpagina) noemt alleen de aanvraag- en verstrekkingskant van subsidies, niet de programmatische bundeling of financiële deelcomponenten — voor die begrippen ontbreekt op dit moment een brongrond. Gesignaleerd voor een toekomstige, rijkere subsidierecht-bron (bijv. Model ASV-tekst of Awb titel 4.2) via [[Wiki/Analyses/ggm-terugmeldingen]].
