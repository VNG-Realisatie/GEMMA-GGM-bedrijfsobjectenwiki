---
type: bedrijfsobject
naam: Algoritmeregister
onderwerp: [Informatiesamenleving]
archimate_type: business-object
grondslag: procesobject

ggm_entiteit:
ggm_guid:
ggm_uml_type:
ggm_beleidsdomein:
ggm_taakveld:
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie:
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

ggm_duplicaat_entiteiten: []

bo_definitie: "Vastlegging van een algoritme in het Algoritmeregister met doel, werking, verantwoording en metadata conform de Publicatiestandaard."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/verwerkingsactiviteit|Verwerkingsactiviteit]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: "Algoritmeregister verwijst naar verwerkingsregister (link)"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/dpia|DPIA]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: "Algoritmeregister verwijst naar impactoets (link)"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/grondrechteneffectbeoordeling|Grondrechteneffectbeoordeling]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: "Hoog-risico AI-systemen (categorie A) vereisen grondrechteneffectbeoordeling"
bedrijfsprocessen: [AI-compliance, Algoritmeregister]
bedrijfsfuncties: [Informatievoorziening, Juridische zaken]
---

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Betekenis | Vastlegging van een algoritme met doel, werking, risico's en verantwoording conform de Publicatiestandaard |
| Herkenbaarheid | De gemeente herkent dit — "we moeten dit algoritme registreren in het algoritmeregister" |
| Eigen bestaan | ~25 velden over 4 secties (algemene info, verantwoord gebruik, werking, metadata) |
| Meervoud | Gemeente heeft meerdere registraties (parkeerscanauto, fraudedetectie, chatbot) |
| Levenscyclus | In ontwikkeling → in gebruik → buiten gebruik; versiebeheer met bewerkingsgeschiedenis |
| Relaties | Met organisatie (eigenaar), verwerkingsactiviteit (link), DPIA/impactoets (link), grondrechteneffectbeoordeling (bij categorie A) |

Resultaat: 6/6 — BO.

## Beschrijving

Het Algoritmeregister is het register waarin overheidsorganisaties hun algoritmes publiceren (algoritmes.overheid.nl). Per algoritme wordt informatie vastgelegd over het doel, de werking, de verantwoording en de metadata conform de Publicatiestandaard.

De registratie bevat ~25 velden verdeeld over 4 secties:

**Algemene informatie** (verplichte velden): naam, korte omschrijving, organisatie, thema, status, begin-/einddatum, contactgegevens, publicatiecategorie.

**Verantwoord gebruik**: doel en impact, afwegingen, menselijke tussenkomst, risicobeheer, wettelijke basis, link naar verwerkingsregister, impactoetsen.

**Werking**: gegevens, gegevensbronnen, technische werking, leverancier, broncode.

**Metadata**: taal, schema, bron-ID, zoektermen.

### Publicatiecategorie

Elke registratie wordt ingedeeld in een van drie categorieën:
- **Categorie A: Hoog-risico AI-systeem** — conform de AI-verordening; verplichtingen art. 26-27, inclusief [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/grondrechteneffectbeoordeling|Grondrechteneffectbeoordeling]]
- **Categorie B: Impactvolle algoritmes** — niet hoog-risico AI maar wel maatschappelijke impact
- **Categorie C: Overige algoritmes** — vrijwillige publicatie

### Levenscyclus

Een registratie doorloopt de statussen: in ontwikkeling → in gebruik → buiten gebruik. Het register ondersteunt versiebeheer met bewerkingsgeschiedenis.

## Procesbron

De Publicatiestandaard wordt beheerd door het Ministerie van BZK. Het register is gekoppeld aan de EU-databank voor hoog-risico AI-systemen (art. 49 AI-verordening). Voor overheden geldt vanaf 2 augustus 2026 een registratieplicht voor hoog-risico AI-systemen.

Zie [[Wiki/Bronsamenvattingen/Informatiesamenleving/handleiding-publicatiestandaard-algoritmeregister|Handleiding Publicatiestandaard]] voor alle velden met invoertypes en voorbeelden.
Zie [[Wiki/Bronsamenvattingen/Informatiesamenleving/eu-ai-verordening|EU AI-verordening]] voor de registratieplicht (art. 49) en de hoog-risico lijst (bijlage III).

## Relaties

| Relatie | Richting | Beschrijving |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/verwerkingsactiviteit\|Verwerkingsactiviteit]] | bidirectioneel | Registratie bevat link naar verwerkingsregister |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/dpia\|DPIA]] | bidirectioneel | Registratie bevat link naar impactoets |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/grondrechteneffectbeoordeling\|Grondrechteneffectbeoordeling]] | bidirectioneel | Hoog-risico AI (categorie A) vereist grondrechteneffectbeoordeling |

Buiten wiki-scope (geen BO):
- **Organisatie** — eigenaar van het algoritme (TOOI-waardelijst)
- **Leverancier** — externe partij die het algoritme levert
- **EU-databank** — Europese registratie voor hoog-risico AI-systemen

## Subtypes

Herkende specialisaties via de publicatiecategorie. Geen apart BO.

- **Hoog-risico AI-registratie** — categorie A, conform AI-verordening bijlage III
- **Impactvolle algoritme-registratie** — categorie B, maatschappelijke impact
- **Overige algoritme-registratie** — categorie C, vrijwillig

## Bedrijfsprocessen

- **AI-compliance** — naleven AI-verordening
- **Algoritmeregister** — publiceren en bijhouden van algoritme-entries in het register

## Bedrijfsfuncties

- **Informatievoorziening** — eigenaar algoritmes
- **Juridische zaken** — wettelijke basis en verantwoording

## Bronnen

- [[Wiki/Bronsamenvattingen/Informatiesamenleving/handleiding-publicatiestandaard-algoritmeregister]]
- [[Wiki/Bronsamenvattingen/Informatiesamenleving/eu-ai-verordening]]
- [[Wiki/Bronsamenvattingen/Informatiesamenleving/factsheet-ai-verordening-vng]]
- [[Wiki/Bronsamenvattingen/Informatiesamenleving/ai-verordening-ap]]

## Terugmelding GGM

Geen GGM-entiteit gevonden. Het GGM bevat geen AI-/algoritme-gerelateerde entiteiten.

Teruggemeld als #72 in [[Wiki/Analyses/ggm-terugmeldingen]].
