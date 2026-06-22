---
type: bedrijfsobject
naam: Dienstverband
domein: [Arbeidszaken]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Dienstverband
ggm_guid: EAID_63FF86E2_1BB0_48f6_8D95_3D82E8D2FA06
ggm_uml_type: Class
ggm_beleidsdomein: HR
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Domain Objects, Documenten, Bezetting en Formatie]
ggm_diagram_ids: [EAID_891372E6_27FB_442d_9CC4_08C2659E8C53, EAID_E8C1CCDA_FF3C_498a_8FC9_FD6E461092FA, EAID_0B1C1CCE_E0D1_413d_A38B_7A9B03A21610]
ggm_definitie: "De rechtsbetrekking tussen werkgever en werknemer zoals vastgelegd in een arbeidsovereenkomst."
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

gemma_definitie: "De rechtsbetrekking tussen werkgever en werknemer zoals vastgelegd in een arbeidsovereenkomst."
gemma_subtypes:
  - naam: Arbeidsovereenkomst voor onbepaalde tijd
    omschrijving: "Vast contract zonder einddatum"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: Arbeidsovereenkomst voor bepaalde tijd
    omschrijving: "Tijdelijk contract met einddatum (ketenregeling: max 3 contracten, 36 maanden)"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: Project-arbeidsovereenkomst
    omschrijving: "Tijdelijk contract gekoppeld aan objectief bepaalbaar projecteinde"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: Oproepovereenkomst
    omschrijving: "Contract zonder vaste urenomvang (nuluren of min-max, min 15 uur/maand per cao)"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
relaties:
  - type: associatie
    bedrijfsobject: "[[Werknemer]]"
    richting: naar-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Werknemer heeft een of meer dienstverbanden"
  - type: associatie
    bedrijfsobject: "[[Functie]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Dienstverband conform functie"
  - type: associatie
    bedrijfsobject: "[[Formatieplaats]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Formatieplaats toegewezen aan dienstverband"
bedrijfsprocessen: [Werving en selectie, Personeelsadministratie, Salarisadministratie, Uitstroom]
bedrijfsfuncties: [Personeelsbeheer, Salarisverwerking]
---

## BO-criteria toetsing

| Criterium | Score |
|---|---|
| Heeft betekenis binnen het domein | ✅ Kernbegrip in gemeentelijke personeelsadministratie |
| Herkenbaar voor domeinexperts | ✅ Elke HR-medewerker werkt dagelijks met dienstverbanden |
| Heeft eigen bestaan binnen het domein | ✅ Bestaat onafhankelijk als juridisch contract |
| Kan in meervoud bestaan | ✅ Honderden tot duizenden per gemeente |
| Heeft eigen levenscyclus | ✅ Sluiten → verlengen → wijzigen → beëindigen |
| Heeft relaties met andere concepten | ✅ Werknemer, Functie, Formatieplaats, OrganisatorischeEenheid |

Score: **6/6**

## Beschrijving

Het dienstverband is de formele arbeidsrelatie tussen de gemeente als werkgever en een werknemer. Het legt vast welke functie wordt vervuld, voor hoeveel uren, tegen welk salaris, en voor welke periode. Elk dienstverband heeft een startdatum en eventueel een einddatum.

Sinds de normalisering van de ambtenarenstatus (Wnra, 2020) vallen gemeenteambtenaren onder het private arbeidsrecht. De Cao Gemeenten regelt de sectorspecifieke arbeidsvoorwaarden.

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| Arbeidsovereenkomst voor onbepaalde tijd | Vast contract zonder einddatum | — |
| Arbeidsovereenkomst voor bepaalde tijd | Tijdelijk contract (ketenregeling: max 3 contracten, 36 maanden) | — |
| Project-arbeidsovereenkomst | Einddatum gekoppeld aan objectief bepaalbaar projecteinde | — |
| Oproepovereenkomst | Zonder vaste urenomvang (min 15 uur/maand per cao) | — |

De subtypes komen uit de [[Wiki/Bronsamenvattingen/Arbeidszaken/handreiking-flexibele-arbeidsinzet|Handreiking flexibele arbeidsinzet]]. Het GGM modelleert Dienstverband als enkele entiteit zonder subtypering.

## GGM-bron

> "De rechtsbetrekking tussen werkgever en werknemer zoals vastgelegd in een arbeidsovereenkomst."

- **Entiteit:** Dienstverband
- **Beleidsdomein:** HR (taakveld 9 Interne Organisatie)
- **Attributen:** datumStart, datumEinde, salaris, periodiek, schaal, urenPerWeek
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Werknemer]] heeft dienstverband | naar dit BO | 1..* | GGM |
| Dienstverband conform [[Functie]] | van dit BO | 1 | GGM |
| [[Formatieplaats]] toegewezen aan dienstverband | naar dit BO | 0..* | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Arbeidszaken/handreiking-flexibele-arbeidsinzet]]
- [[Wiki/Bronsamenvattingen/Arbeidszaken/arbeidsvoorwaarden]]
- [[Wiki/Bronsamenvattingen/Arbeidszaken/cva-beleidsplan-2023-2026]]
