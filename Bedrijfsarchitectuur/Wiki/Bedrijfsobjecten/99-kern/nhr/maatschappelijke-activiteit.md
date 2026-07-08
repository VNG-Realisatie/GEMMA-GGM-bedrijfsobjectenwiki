---
type: bedrijfsobject
naam: Maatschappelijke Activiteit
onderwerp: [Basisregistraties, NHR]
archimate_type: business-object
grondslag: ggm-entiteit

# GGM-velden
ggm_entiteit: MaatschappelijkeActiviteit
ggm_guid: EAID_3DC85114_5C3F_4930_B98B_6EB6ED71FC2E
ggm_uml_type: Class
ggm_beleidsdomein:
ggm_taakveld: "99 Kern"
ggm_diagram:
  - KVK
  - NHR
  - MAATSCHAPPELIJKE ACTIVITEIT
  - Diagram Economie
  - PERSOON
  - VESTIGING
  - Objecten bij Vergunningaanvraag
  - Detaillering subjecten op hoofdlijnen
  - Detaillering subjecten met attributen
ggm_diagram_ids:
  - EAID_FC491653_1FBF_412a_A939_A705D501AE48
  - EAID_A4A7A187_57B9_4ecb_9B3D_012C51E981E2
  - EAID_0B75D3CA_1D93_46c7_9268_BD8276836FE2
  - EAID_21D78104_E6EA_4d5c_9DBE_AB71F7DC99E7
  - EAID_72DE3820_C251_45ac_A1C2_3A133A7791F3
  - EAID_3CAB7DD2_51D3_45b3_9CE1_61E0150F792D
  - EAID_C9CE09B7_32EF_40eb_9C82_7FD6EDEA1D9E
  - EAID_BE50EA2F_917E_434f_91ED_0EB06CCBEFB6
  - EAID_EB4053EE_18A5_4578_8973_7FD5967CDFC8
ggm_definitie: "Een verband tussen één of meer personen met voldoende mate van zelfstandigheid, inbreng van arbeid of middelen, winstoogmerk en extern optreden (i.g.v. een onderneming) dan wel een in een organisatorisch verband, dat toebehoort aan een niet-natuurlijk persoon welke registratieplichtig is, uitgeoefende activiteit die niet valt onder de criteria voor onderneming of bedrijfsmatigheid welke adresseerbaar is middels ofwel een vestiging ofwel het adres van een bepaalde vertegenwoordiger (i.g.v. een niet-ondernemings-activiteit)."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst: "KING o.b.v NHR"

# GEMMA-waarden
ggm_gemma_naam: MaatschappelijkeActiviteit
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
  Dit BO is de hernoeming van GGM-entiteit **MaatschappelijkeActiviteit**. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **HandelsnamenMaatschappelijkeActiviteit** (detail) — Detailgegeven
  - **Nationaliteit** (detail) — eigenschap van persoon
bo_definitie: "Een verband tussen één of meer personen met voldoende mate van zelfstandigheid, inbreng van arbeid of middelen, winstoogmerk en extern optreden (i.g.v. een onderneming) dan wel een in een organisatorisch verband, dat toebehoort aan een niet-natuurlijk persoon welke registratieplichtig is, uitgeoefende activiteit die niet valt onder de criteria voor onderneming of bedrijfsmatigheid welke adresseerbaar is middels ofwel een vestiging ofwel het adres van een bepaalde vertegenwoordiger (i.g.v. een niet-ondernemings-activiteit)."
bo_toelichting: ''
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Niet-Natuurlijk Persoon]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Heeft als eigenaar"
  - type: associatie
    bedrijfsobject: "[[Ingeschreven Persoon]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Is functionaris van"
  - type: associatie
    bedrijfsobject: "[[Vestiging]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Uitoefening van activiteiten via vestigingen"
bedrijfsprocessen:
  - Inschrijving Handelsregister
  - Vergunningverlening
  - Belastingheffing
bedrijfsfuncties:
  - Economische zaken
  - Vergunningverlening
  - Belastingheffing
---

## BO-criteria toetsing

| Criterium | Oordeel |
|---|---|
| Gemeentelijk belang | ✅ Gemeente gebruikt MA's voor belastingen, vergunningen, VTH, economisch beleid |
| Meervoudig | ✅ Honderdduizenden MA's in het Handelsregister |
| Levenscyclus | ✅ Datum aanvang, datum einde, faillissement |
| Identificeerbaar | ✅ KVK-nummer, RSIN |
| Relaties | ✅ Eigenaar (Rechtspersoon), Vestiging, NatuurlijkPersoon (functionaris) |
| Registratieobject | ✅ Authentiek gegeven in het Handelsregister |

## Beschrijving

Een Maatschappelijke Activiteit is het centrale object in het Handelsregister. Het verbindt een persoon (natuurlijk of niet-natuurlijk) aan economische of maatschappelijke activiteiten. Elke inschrijving in het Handelsregister is een maatschappelijke activiteit, geïdentificeerd met een KVK-nummer.

Een maatschappelijke activiteit die voldoet aan de criteria van de Handelsregisterwet (zelfstandigheid, inbreng, winstoogmerk, extern optreden) kwalificeert als **onderneming**. Dit wordt in het informatiemodel vastgelegd via het attribuut `indicatieEconomischActief` — onderneming is geen apart objecttype.

De gemeente gebruikt maatschappelijke activiteiten in vrijwel alle domeinen: belastingheffing (OZB, reclamebelasting, BIZ), vergunningverlening (horeca, evenementen, omgevingsvergunning), toezicht en handhaving, economisch beleid (werklocaties, detailhandel) en schuldhulpverlening (schuldeisers).

## Subtypes

Herkende specialisaties van Maatschappelijke Activiteit. Geen apart BO.

- **Onderneming** — economische activiteit die voldoet aan wettelijke criteria (indicatieEconomischActief = ja). Heeft altijd minimaal één commerciële vestiging.
- **Niet-ondernemingsactiviteit** — activiteit van een niet-natuurlijk persoon die niet als onderneming kwalificeert (bijv. stichting zonder winstoogmerk).

## GGM-componenten

GGM-entiteiten die onderdeel zijn van Maatschappelijke Activiteit. Gemodelleerd als aparte entiteiten in het GGM (voor gegevensgroepen) maar vormen geen zelfstandig bedrijfsobject.

- **HandelsnamenMaatschappelijkeActiviteit** — handelsnaam, verkorte naam en volgorde (meervoudig)

## GGM-bron

> "Een verband tussen één of meer personen met voldoende mate van zelfstandigheid, inbreng van arbeid of middelen, winstoogmerk en extern optreden (i.g.v. een onderneming) dan wel een in een organisatorisch verband, dat toebehoort aan een niet-natuurlijk persoon welke registratieplichtig is, uitgeoefende activiteit die niet valt onder de criteria voor onderneming of bedrijfsmatigheid welke adresseerbaar is middels ofwel een vestiging ofwel het adres van een bepaalde vertegenwoordiger (i.g.v. een niet-ondernemings-activiteit)."

- **Entiteit:** MaatschappelijkeActiviteit
- **Package:** RSGB Model > Model Kern RSGB
- **Herkomst:** KING o.b.v NHR
- **Attributen:** KVKnummer, datumAanvang, datumEindeGeldig, indicatieEconomischActief, statutaireNaam, rechtsvorm, URL, RSIN, adresBinnenland, adresCorrespondentie, telefoonnummer, datumFaillisement
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | BO | Beschrijving | Bron |
|---|---|---|---|---|
| heeft als eigenaar | → | [[Niet-Natuurlijk Persoon]] | Eigenaar van de MA is een rechtspersoon | GGM |
| is functionaris van | → | [[Ingeschreven Persoon]] | Natuurlijk persoon als functionaris | GGM |
| uitoefening activiteiten | ← | [[Vestiging]] | Vestiging oefent activiteiten uit van deze MA | GGM |
| is hoofdvestiging van | ← | [[Vestiging]] | Eén vestiging is de hoofdvestiging | GGM |

## Bedrijfsprocessen

- Inschrijving en mutering Handelsregister
- Vergunningverlening (horeca, evenementen, omgeving)
- Belastingheffing (OZB, reclame, BIZ, precario)
- Toezicht en handhaving

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-nhr]]
