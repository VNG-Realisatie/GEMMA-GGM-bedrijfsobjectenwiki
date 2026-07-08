---
type: bedrijfsobject
naam: Niet-Natuurlijk Persoon
onderwerp: [Basisregistraties, NHR]
archimate_type: business-object
grondslag: ggm-entiteit

# GGM-velden
ggm_entiteit: NietNatuurlijkPersoon
ggm_guid: EAID_3D5CCB29_91E4_458e_8BCD_6741198E45B8
ggm_uml_type: Class
ggm_beleidsdomein:
ggm_taakveld: "99 Kern"
ggm_diagram:
  - KVK
  - NHR
  - NIET-NATUURLIJK PERSOON
  - Kern:Personen
  - "Kern: Detaillering in Subjecten"
  - Detaillering subjecten op hoofdlijnen
  - Detaillering subjecten met attributen
  - Detaillering Subjecten
  - Betrokkene
  - BRK
  - APPARTEMENTRECHTSPLITSING
ggm_diagram_ids:
  - EAID_FC491653_1FBF_412a_A939_A705D501AE48
  - EAID_A4A7A187_57B9_4ecb_9B3D_012C51E981E2
  - EAID_AA6A32A2_564F_4406_8286_D935DB9DD91A
  - EAID_30391B0F_CF52_4dc1_BC1B_36D428BF0120
  - EAID_513E7AD3_1E8A_460f_9D78_2D8A6AA9EF98
  - EAID_BE50EA2F_917E_434f_91ED_0EB06CCBEFB6
  - EAID_EB4053EE_18A5_4578_8973_7FD5967CDFC8
  - EAID_71A3B7DD_0097_4a32_8E4B_09735D7404E8
  - EAID_0516C81B_D5F6_4b7a_AD98_82FD3B218A6B
  - EAID_DF9CEAAD_E574_40b3_970B_DC558AB579D0
  - EAID_0C767444_9817_4d3b_90CB_92D82729A6F9
ggm_definitie: "Een INGESCHREVEN NIET-NATUURLIJK PERSOON of een ANDER BUITENLANDS NIET-NATUURLIJK PERSOON"
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

# GEMMA-waarden
ggm_gemma_naam: NietNatuurlijkPersoon
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
  Dit BO is de hernoeming van GGM-entiteit **NietNatuurlijkPersoon**. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **AdresBuitenland** (detail) — Detailgegeven
  - **Gerechtelijke uitspraak** (detail) — Detailgegeven (weinig attributen)
  - **Gezagsverhouding** (detail) — juridische status
  - **Onderwijsinstituut** (detail) — Detailgegeven (weinig attributen)
bo_definitie: "Organisatie of samenwerkingsverband met rechtspersoonlijkheid, geregistreerd in het Handelsregister."
bo_toelichting: ''
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Ingeschreven Persoon]]"
    richting: bidirectioneel
    kardinaliteit: ""
    beschrijving: "Complement: NNP is de organisatiekant, Ingeschreven Persoon de persoonskant van Rechtspersoon"
  - type: associatie
    bedrijfsobject: "[[Maatschappelijke Activiteit]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Heeft als eigenaar van een maatschappelijke activiteit"
  - type: associatie
    bedrijfsobject: "[[Vestiging]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Heeft vestigingen"
  - type: associatie
    bedrijfsobject: "[[Tenaamstelling]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Rechthebbende op onroerende zaken (via Rechtspersoon)"
bedrijfsprocessen:
  - Vergunningverlening
  - Subsidieverstrekking
  - Belastingheffing
  - Inkoop en aanbesteding
  - Toezicht en handhaving
bedrijfsfuncties:
  - Vergunningverlening
  - Subsidieverstrekking
  - Belastingheffing
  - Inkoop
---

## BO-criteria toetsing

| Criterium | Oordeel |
|---|---|
| Gemeentelijk belang | ✅ Vergunninghouders, contractpartners, subsidieaanvragers, belastingplichtigen |
| Meervoudig | ✅ Miljoenen organisaties in het Handelsregister |
| Levenscyclus | ✅ Datum aanvang, datum einde, in oprichting, uitschrijving |
| Identificeerbaar | ✅ NNPID, KVK-nummer, RSIN |
| Relaties | ✅ Vestiging, Maatschappelijke Activiteit, Tenaamstelling (BRK), meerdere domein-rollen |
| Registratieobject | ✅ Authentiek gegeven in het Handelsregister |

## Beschrijving

Een Niet-Natuurlijk Persoon is een organisatie met rechtspersoonlijkheid: BV, NV, stichting, vereniging, coöperatie, onderlinge waarborgmaatschappij, publiekrechtelijke rechtspersoon, kerkgenootschap, of buitenlandse rechtspersoon. Het is het complement van [[Ingeschreven Persoon]] (BRP): samen dekken zij het volledige spectrum van subjecten waarmee de gemeente te maken heeft.

In het GGM is NietNatuurlijkPersoon een specialisatie van Rechtspersoon (abstract type). NatuurlijkPersoon is de andere specialisatie, waarvan [[Ingeschreven Persoon]] (IngeschrevenPersoon) weer een specialisatie is. Rechtspersoon zelf is te abstract voor een BO.

De gemeente heeft in vrijwel elk domein met niet-natuurlijke personen te maken: als vergunninghouder (horeca, evenementen), als subsidieaanvrager, als contractpartner (inkoop), als belastingplichtige (OZB, reclamebelasting), als schuldeiser (schuldhulpverlening), als schoolbestuur (onderwijs), als sportvereniging, als zorgaanbieder (Wmo/Jeugdwet).

## Subtypes

Herkende specialisaties van Niet-Natuurlijk Persoon op basis van rechtsvorm. Geen apart BO.

- **Besloten vennootschap (BV)** — meest voorkomende rechtsvorm voor ondernemingen
- **Naamloze vennootschap (NV)** — kapitaalvennootschap met overdraagbare aandelen
- **Stichting** — rechtspersoon zonder leden, opgericht voor een doel
- **Vereniging** — rechtspersoon met leden, opgericht voor een doel
- **Coöperatie** — vereniging die overeenkomsten sluit met of ten behoeve van leden
- **Publiekrechtelijke rechtspersoon** — overheidsorgaan (gemeente, waterschap, etc.)
- **Vennootschap onder firma (VOF)** — samenwerkingsverband zonder rechtspersoonlijkheid (registratieplichtig)
- **Maatschap** — samenwerkingsverband van beroepsbeoefenaren
- **Kerkgenootschap** — religieuze organisatie met rechtspersoonlijkheid

## GGM-bron

> "Een INGESCHREVEN NIET-NATUURLIJK PERSOON of een ANDER BUITENLANDS NIET-NATUURLIJK PERSOON"

- **Entiteit:** NietNatuurlijkPersoon
- **Package:** RSGB Model > Model Kern RSGB
- **Attributen:** NNPID, statutaireNaam, datumAanvang, rechtsvorm, datumEinde, statutaireZetel, datumVoortzetting, faxnummer, KVKnummer, ingeschreven, RSINNummer, datumUitschrijving, websiteURL, inOprichting
- **Matchsterkte:** exact

## BO-definitie

De GGM-definitie wijkt inhoudelijk af van het gemeentelijke gebruik van dit begrip. De BO-definitie is gebaseerd op de bronnen.

## Relaties

| Relatie | Richting | BO | Beschrijving | Bron |
|---|---|---|---|---|
| heeft als eigenaar | → | [[Maatschappelijke Activiteit]] | Eigenaar van een maatschappelijke activiteit | GGM |
| heeft | → | [[Vestiging]] | Heeft vestigingen | GGM |
| contactpersoon | → | [[Ingeschreven Persoon]] | Heeft een contactpersoon (NatuurlijkPersoon) | GGM |
| rechthebbende | → | [[Tenaamstelling]] | Rechthebbende op onroerende zaken (via Rechtspersoon) | GGM |
| WOZ-belang | → | [[WOZ-object]] | Heeft belang bij WOZ-objecten (via Rechtspersoon) | GGM |

Domeinspecifieke rollen (geen aparte BO-relatie, maar het NNP-object wordt gebruikt als):
- [[Schuldeiser]] (schuldhulpverlening), [[Sportvereniging]] (sport), School/Onderwijsinstituut (onderwijs), Leverancier (inkoop), Subsidieontvanger (subsidies)

## Bedrijfsprocessen

- Vergunningverlening en -beheer
- Subsidieverstrekking en -verantwoording
- Belastingheffing (OZB, reclame, BIZ)
- Inkoop en aanbesteding
- Toezicht en handhaving
- Schuldhulpverlening (als schuldeiser)

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-nhr]]
