---
type: element
naam: Vestiging
onderwerp: [Basisregistraties, NHR]
archimate_type: business-object
grondslag: ggm-entiteit

# GGM-velden
ggm_entiteit: Vestiging
ggm_guid: EAID_B60B8EF9_D1C0_4e36_BF9B_1C16F92518DD
ggm_uml_type: Class
ggm_beleidsdomein:
ggm_taakveld: "99 Kern"
ggm_diagram:
  - KVK
  - NHR
  - VESTIGING
  - MAATSCHAPPELIJKE ACTIVITEIT
  - Diagram Economie
  - Diagram Gebied Vestiging en Adres
  - BENOEMD OBJECT
  - ADRESSEERBAAR OBJECT AANDUIDING
  - Detaillering subjecten op hoofdlijnen
  - Detaillering subjecten met attributen
  - Detaillering Subjecten
  - Detaillering WOZ-objecttypen op hoofdlijnen
  - Detaillering WOZ-objecttypen met attributen
ggm_diagram_ids:
  - EAID_FC491653_1FBF_412a_A939_A705D501AE48
  - EAID_A4A7A187_57B9_4ecb_9B3D_012C51E981E2
  - EAID_3CAB7DD2_51D3_45b3_9CE1_61E0150F792D
  - EAID_0B75D3CA_1D93_46c7_9268_BD8276836FE2
  - EAID_21D78104_E6EA_4d5c_9DBE_AB71F7DC99E7
  - EAID_50085E67_46AC_4f54_B204_436786266EE2
  - EAID_515E0990_C193_43cb_8EAF_907796BD3B1F
  - EAID_EB829228_B970_4bc9_A9B4_5E88B9EF07D3
  - EAID_BE50EA2F_917E_434f_91ED_0EB06CCBEFB6
  - EAID_EB4053EE_18A5_4578_8973_7FD5967CDFC8
  - EAID_71A3B7DD_0097_4a32_8E4B_09735D7404E8
  - EAID_3F813481_9A40_4b1b_9B24_1FD069230A45
  - EAID_5E76FEEA_58F8_41fd_9FF1_B44274C80FA5
ggm_definitie: "Een gebouw of complex van gebouwen waar duurzame uitoefening van de activiteiten van een onderneming of rechtspersoon plaatsvindt."
ggm_toelichting: "Ofschoon de definitie in het NHR doet vermoeden dat het hier om een ruimtelijk object gaat, beschouwen we een VESTIGING in het RSGB als een specialisatie van SUBJECT."
ggm_synoniemen:
ggm_herkomst:

# GEMMA-waarden
ggm_gemma_naam:
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
  Dit BO heeft de GGM-entiteit **Vestiging** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Contact** (detail) — Detailgegeven (geassocieerd met BO)
  - **HandelsnamenVestiging** (detail) — Detailgegeven (weinig attributen)
  - **SBIActiviteitVestiging** (detail) — Detailgegeven
  - **Verkooppunt** (detail) — Detailgegeven (weinig attributen)
  - **Werkgelegenheid** (detail) — Detailgegeven (geassocieerd met BO)
bo_definitie: "Locatie waar een onderneming of rechtspersoon duurzaam activiteiten uitoefent, geïdentificeerd met vestigingsnummer."
bo_toelichting: ''
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Maatschappelijke Activiteit]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Uitoefening van activiteiten van een maatschappelijke activiteit"
  - type: associatie
    bedrijfsobject: "[[Niet-Natuurlijk Persoon]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Behoort toe aan een niet-natuurlijk persoon"
  - type: associatie
    bedrijfsobject: "[[Nummeraanduiding]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Heeft als locatie-adres een BAG-adres"
  - type: generalisatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/3-economie/economie/horecabedrijf|Horecabedrijf]]"
    richting: van-dit-BO
    kardinaliteit: ""
    beschrijving: "Horecabedrijf is een specialisatie van Vestiging"
bedrijfsprocessen:
  - Vergunningverlening
  - Belastingheffing
  - Toezicht en handhaving
  - Economisch beleid
bedrijfsfuncties:
  - Vergunningverlening
  - Belastingheffing
  - Economische zaken
---

## BO-criteria toetsing

| Criterium | Oordeel |
|---|---|
| Gemeentelijk belang | ✅ Vergunningen, belastingen, VTH, economisch beleid richten zich op vestigingen |
| Meervoudig | ✅ Honderdduizenden vestigingen in het Handelsregister |
| Levenscyclus | ✅ Datum aanvang, datum einde, datum voortzetting |
| Identificeerbaar | ✅ Vestigingsnummer (uniek), gekoppeld aan BAG-adres |
| Relaties | ✅ Maatschappelijke Activiteit, Nummeraanduiding (BAG), NietNatuurlijkPersoon |
| Registratieobject | ✅ Authentiek gegeven in het Handelsregister |

## Beschrijving

Een Vestiging is een gebouw of complex van gebouwen waar duurzame uitoefening van de activiteiten van een onderneming of rechtspersoon plaatsvindt. Elke vestiging heeft een uniek vestigingsnummer en is gekoppeld aan een BAG-adres ([[Nummeraanduiding]]).

Er zijn twee soorten vestigingen:
- **Commerciële vestiging** — behoort bij een onderneming (economisch actieve maatschappelijke activiteit). Elke onderneming heeft minimaal één commerciële vestiging.
- **Niet-commerciële vestiging** — behoort bij een rechtspersoon die geen onderneming drijft (bijv. een stichting met alleen maatschappelijke activiteiten).

Eén vestiging is aangewezen als **hoofdvestiging**; de overige zijn nevenvestigingen.

De gemeente gebruikt vestigingen in meerdere domeinen. De bestaande BO's [[Horecabedrijf]] en [[Hotel]] zijn domeinspecifieke specialisaties van Vestiging. Voor vergunningverlening, belastingheffing en toezicht is de vestiging het object waarop de gemeente handelt.

> "Ofschoon de definitie in het NHR doet vermoeden dat het hier om een ruimtelijk object gaat, beschouwen we een VESTIGING in het RSGB als een specialisatie van SUBJECT." (GGM-toelichting)

## Subtypes

Herkende specialisaties van Vestiging. Geen apart BO (tenzij vermeld).

- **Commerciële vestiging** — vestiging bij een onderneming
- **Niet-commerciële vestiging** — vestiging bij een rechtspersoon zonder onderneming

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/3-economie/economie/horecabedrijf\|Horecabedrijf]] | Bedrijf voor eten, drinken en/of logies | Vestiging (partieel) |
| [[Wiki/Bedrijfsobjecten/3-economie/economie/hotel\|Hotel]] | Verblijfsaccommodatie met subtypes | Hotel |

## GGM-componenten

GGM-entiteiten die onderdeel zijn van Vestiging. Gemodelleerd als aparte entiteiten in het GGM (voor gegevensgroepen) maar vormen geen zelfstandig bedrijfsobject.

- **HandelsnamenVestiging** — handelsnaam, verkorte naam en volgorde per vestiging (meervoudig)
- **SBIActiviteitVestiging** — SBI-code en indicatie hoofdactiviteit per vestiging (meervoudig)
- **Werkgelegenheid** — werkgelegenheidsgegevens gekoppeld aan een vestiging

## GGM-bron

> "Een gebouw of complex van gebouwen waar duurzame uitoefening van de activiteiten van een onderneming of rechtspersoon plaatsvindt."

- **Entiteit:** Vestiging
- **Package:** RSGB Model > Model Kern RSGB
- **Attributen:** vestigingsnummer, handelsnaam, verkorteNaam, datumAanvang, datumEinde, datumVoortzetting, toevoegingAdres, fulltimeWerkzameMannen, parttimeWerkzameMannen, fulltimeWerkzameVrouwen, parttimeWerkzameVrouwen, commercieleVestiging, totaalWerkzamePersonen
- **Matchsterkte:** exact

## BO-definitie

De GGM-definitie wijkt inhoudelijk af van het gemeentelijke gebruik van dit begrip. De BO-definitie is gebaseerd op de bronnen.

## Relaties

| Relatie | Richting | BO | Beschrijving | Bron |
|---|---|---|---|---|
| uitoefening van activiteiten | → | [[Maatschappelijke Activiteit]] | Vestiging oefent activiteiten uit van een MA | GGM |
| is hoofdvestiging van | → | [[Maatschappelijke Activiteit]] | Eén vestiging is de hoofdvestiging | GGM |
| behoort toe aan | → | [[Niet-Natuurlijk Persoon]] | NNP heeft vestigingen | GGM |
| heeft als locatie-adres | → | [[Nummeraanduiding]] | BAG-adres van de vestiging | GGM |
| heeft hoofd/nevenlocatie in | → | Adresseerbaar Object | Fysieke locatie in BAG | GGM |

## Bedrijfsprocessen

- Vergunningverlening (horeca, evenementen, omgeving)
- Belastingheffing (OZB, reclame, precario)
- Toezicht en handhaving
- Economisch beleid (werklocaties, detailhandel, SBI-analyse)

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-nhr]]
