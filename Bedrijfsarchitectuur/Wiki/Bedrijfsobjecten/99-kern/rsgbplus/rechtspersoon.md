---
type: element
naam: Rechtspersoon
onderwerp: [Basisregistraties, RSGBPlus]
archimate_type: business-object
grondslag: ggm-entiteit

# GGM-velden
ggm_entiteit: Rechtspersoon
ggm_guid: EAID_9DF5AC43_3673_4b9a_BB5E_6DCA7BE28835
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram:
  - "Kern:Personen"
  - "Kern: Detaillering in Subjecten"
  - "Detaillering subjecten op hoofdlijnen"
  - "Detaillering Subjecten "
  - NHR
  - BRK
  - "ZAKELIJK RECHT PERSOON"
ggm_diagram_ids: []
ggm_definitie: "Een NATUURLIJK PERSOON of een NIET-NATUURLIJK PERSOON"
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

# GEMMA-waarden
ggm_gemma_naam: Rechtspersoon
ggm_gemma_guid: "cad45b80-14d3-4a0c-a906-0c1614dc9570"
ggm_gemma_definitie: "Een NATUURLIJK PERSOON of een NIET-NATUURLIJK PERSOON"
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-cad45b80-14d3-4a0c-a906-0c1614dc9570"
ggm_gemma_bron:
ggm_gemma_alternate_name:

ggm_duplicaat_entiteiten: []

analyse_ggm_dekking: ""
bo_definitie: "Natuurlijke of niet-natuurlijke persoon van wie het gegevensbeheer van essentieel belang is voor de gemeentelijke taakuitoefening."
bo_toelichting: "Door KING toegevoegde generalisatie (RSGB, 1 mei 2008), niet afkomstig uit een eigen basisregistratie. Bundelt Natuurlijk Persoon en Niet-Natuurlijk Persoon zodat correspondentiegegevens (postadres, telefoon, e-mail, bankrekening) en de relaties naar zakelijk recht, WOZ-belang, subsidies en vastgoedcontracten maar één keer gemodelleerd hoeven te worden."
bo_subtypes: []
bo_via_kandidaten: []
bo_synoniemen: []
bo_homoniemen: []
element_tegenhangers: []
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon|Niet-Natuurlijk Persoon]]"
    richting: van-dit-BO
    kardinaliteit:
    beschrijving: "Niet-Natuurlijk Persoon is de organisatiekant-specialisatie van Rechtspersoon"
  - type: generalisatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/brp/natuurlijk-persoon|Natuurlijk Persoon]]"
    richting: van-dit-BO
    kardinaliteit:
    beschrijving: "Natuurlijk Persoon is de persoonskant-specialisatie van Rechtspersoon"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/brk/tenaamstelling|Tenaamstelling]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Is gerechtigde van zakelijk recht op een kadastraal object"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/woz-object|WOZ-object]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Is aangewezen belanghebbende bij een WOZ-belang"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/nhr/maatschappelijke-activiteit|Maatschappelijke Activiteit]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Is eigenaar van een maatschappelijke activiteit"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedcontract|Vastgoedcontract]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Vastgoedcontract heeft een rechtspersoon als contractpartij"
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

| Criterium | Oordeel |
|---|---|
| Heeft betekenis binnen het onderwerp | ✅ Standaard juridisch/gemeentelijk begrip: rechtspersoon versus natuurlijk persoon |
| Herkenbaar voor domeinexperts | ✅ Beleidsmedewerkers, juristen en financiële afdelingen gebruiken de term dagelijks (contractpartij, belanghebbende, debiteur) |
| Eigen bestaan binnen het onderwerp | ✅ Bestaat onafhankelijk als "met wie communiceert de gemeente" — los van de rol die de rechtspersoon in een specifiek domein vervult (eigenaar, huurder, schuldeiser, indiener) |
| Kan in meervoud bestaan | ✅ Elke ingezetene en elke ingeschreven organisatie is een rechtspersoon |
| Heeft een eigen levenscyclus | ✅ Ontstaan/beëindiging (per specialisatie: geboorte/overlijden of oprichting/uitschrijving) |
| Heeft relaties met andere concepten | ✅ Tenaamstelling, WOZ-belang, Maatschappelijke Activiteit, Vastgoedcontract, en tientallen domeinspecifieke rollen (zie Beschrijving) |

6/6 — sterke BO.

## Beschrijving

Rechtspersoon is de RSGB-generalisatie van [[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon|Niet-Natuurlijk Persoon]] (organisaties, NHR) en Natuurlijk Persoon (individuen; de gemeentelijke specialisatie [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon|Ingeschreven Persoon]] dekt hiervan de ingezetenen). Het modelleert alles waarmee de gemeente contact onderhoudt en waarover correspondentiegegevens worden vastgelegd: postadres, telefoonnummer, e-mailadres, bankrekeningnummer.

In het GGM is Rechtspersoon niet alleen de generalisatie van Natuurlijk Persoon/Niet-Natuurlijk Persoon, maar ook de generalisatiewortel voor een groot aantal domeinspecifieke rollen: Eigenaar, Huurder, Pachter, Debiteur, Schuldeiser, Signaalpartner, Leverancier, Grondbeheerder, Bevoegd Gezag, Gemachtigde, Initiatiefnemer, Indiener, Rechthebbende, Uitgever, Belanghebbende, Lener, Museumrelatie en Betrokkene. Deze rollen zijn zelf al (deels) als eigen BO of actor vastgelegd in hun eigen domein (bijvoorbeeld [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuldeiser|Schuldeiser]], [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/signaalpartner|Signaalpartner]], [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/leverancier|Leverancier]]) en verwijzen daar al naar Rechtspersoon als generalisatie; deze pagina is het ontbrekende ankerpunt waarnaar die verwijzingen linken.

**Herziening eerdere beslissing:** bij de NHR-ingest (2026-06-25) is Rechtspersoon beoordeeld als "te abstract voor een BO" en niet vastgelegd. Bij de RSGB Deel II-ingest is dat oordeel herzien: de omvang en herbruikbaarheid van de relaties (tientallen domeinrollen generaliseren ernaar) en de herkenbaarheid van het begrip bij domeinexperts wegen zwaarder dan het abstracte karakter. Zie [[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon|Niet-Natuurlijk Persoon]] voor de bijgewerkte relatie.

## Specialisaties

| Specialisatie | Omschrijving | GGM-entiteit |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon\|Niet-Natuurlijk Persoon]] | Organisatie of samenwerkingsverband met rechtspersoonlijkheid, geregistreerd in het Handelsregister | NietNatuurlijkPersoon |
| [[Wiki/Bedrijfsobjecten/99-kern/brp/natuurlijk-persoon\|Natuurlijk Persoon]] | Individueel menselijk wezen; [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] dekt hiervan de gemeentelijke ingezetenen | NatuurlijkPersoon |

## GGM-bron

> "Een NATUURLIJK PERSOON of een NIET-NATUURLIJK PERSOON"

- **Entiteit:** Rechtspersoon
- **Package:** RSGB Model > Model Kern RSGB
- **Attributen:** identificatie, naam, rechtsvorm, KVKnummer, adresBinnenland, adresBuitenland, adresCorrespondentie, telefoonnummer, faxnummer, emailadres, rekeningnummer
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | BO | Beschrijving | Bron |
|---|---|---|---|---|
| specialisatie | → | [[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon\|Niet-Natuurlijk Persoon]] | Organisatiekant van Rechtspersoon | GGM |
| specialisatie | → | [[Wiki/Bedrijfsobjecten/99-kern/brp/natuurlijk-persoon\|Natuurlijk Persoon]] | Persoonskant van Rechtspersoon | GGM |
| gerechtigde van | → | [[Wiki/Bedrijfsobjecten/99-kern/brk/tenaamstelling\|Tenaamstelling]] | Zakelijk recht op een kadastraal object | GGM |
| belanghebbende bij | → | [[Wiki/Bedrijfsobjecten/99-kern/woz-object\|WOZ-object]] | Aangewezen belanghebbende bij WOZ-belang | GGM |
| eigenaar van | → | [[Wiki/Bedrijfsobjecten/99-kern/nhr/maatschappelijke-activiteit\|Maatschappelijke Activiteit]] | Eigenaarschap van een maatschappelijke activiteit | GGM |
| contractpartij bij | ← | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedcontract\|Vastgoedcontract]] | Rechtspersoon als huurder/pachter in een vastgoedcontract | GGM |

Daarnaast generaliseren tientallen domeinspecifieke rollen in het GGM naar Rechtspersoon (Eigenaar, Huurder, Pachter, Debiteur, Schuldeiser, Signaalpartner, Leverancier, Grondbeheerder, Bevoegd Gezag, Gemachtigde, Initiatiefnemer, Indiener, Rechthebbende, Uitgever, Belanghebbende, Lener, Museumrelatie, Betrokkene) — zie Beschrijving. Deze zijn niet allemaal als losse `bo_relaties`-regel opgenomen; ze zijn zelf al (deels) als BO/actor vastgelegd binnen hun eigen domein.

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/rsgb-deel-ii-specificaties]]
