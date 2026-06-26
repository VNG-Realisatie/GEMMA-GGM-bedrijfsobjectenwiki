---
type: bedrijfsobject
naam: Gemeenschappelijke Regeling
domein:
- Bestuur
archimate_type: business-object
grondslag: governance-object
ggm_entiteit: '~'
ggm_beleidsdomein: Niet expliciet gemodelleerd
ggm_guid: ''
ggm_uml_type: ''
ggm_taakveld: ''
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: '~'
ggm_toelichting: ''
ggm_synoniemen: ''
ggm_herkomst: ''
ggm_gemma_naam: ''
ggm_gemma_guid: ''
ggm_gemma_definitie: ''
ggm_gemma_toelichting: ''
ggm_gemma_synoniemen: ''
ggm_gemma_type: ''
ggm_gemma_url: ''
ggm_gemma_bron: ''
ggm_gemma_alternate_name: ''
gemma_definitie: Publiekrechtelijke samenwerkingsconstructie tussen gemeenten, provincies en/of waterschappen, gevormd op basis van de Wet gemeenschappelijke regelingen (Wgr), met eigen juridische persoonlijkheid,
  bestuur en financiën.
bedrijfsprocessen: ''
bedrijfsfuncties: ''
relaties:
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/99-kern/bag/gemeente|Gemeente]]'
  richting: bidirectioneel
  kardinaliteit: 2..*
  beschrijving: Gemeenschappelijke Regeling is samenwerking van meerdere gemeenten (en mogelijk ook provincies, waterschappen)
- type: associatie
  bedrijfsobject: Bestuur
  richting: naar-dit-BO
  kardinaliteit: 1
  beschrijving: Gemeenschappelijke Regeling heeft eigen bestuur en governance
---

# Gemeenschappelijke Regeling

## BO-criteria toetsing

| Criterium | Van toepassing? | Opmerkingen |
|---|---|---|
| Betekenis binnen domein | ✅ | Kern van inter-gemeente samenwerking |
| Herkenbaar voor experts | ✅ | Raadsleden, wethouders, managers herkennen GR-structuren direct |
| Eigen bestaan | ✅ | Aparte juridische entiteit (ingeschreven KvK) |
| Kan in meervoud bestaan | ✅ | Honderden gemeenschappelijke regelingen in Nederland |
| Eigen levenscyclus | ✅ | Oprichting → operatie → wijziging → opheffing (vaak 50+ jaar) |
| Relaties met andere objecten | ✅ | Relaties met gemeente (deelnemers), bestuurders, financiën, taken |

**Conclusie:** 6/6 criteria ✅ — Dit is een sterke BO-kandidaat.

## Beschrijving

Een Gemeenschappelijke Regeling (GR) is een juridische construct waarmee gemeenten, provincies en waterschappen formeel kunnen samenwerken. Op basis van de **Wet gemeenschappelijke regelingen (Wgr)** kunnen deze publiekrechtelijke partners gezamenlijk taken uitvoeren.

Voorbeelden van GR's:

- **GGD** (Gezondheidsdienst) — gemeentelijke gezondheidstaken (RIVM, jeugdgezondheidszorg)
- **RUD** (Regionale Uitvoeringsdienst) — uitvoering rijksregelingen (werk, inkomensvoorziening)
- **Regionale woningmarktregelingen** — huisvestingsbalans, woningbouwopgaven
- **Jeugdzorg** — uitvoering Jeugdwet
- **Sociale Teams** — integrale ondersteuning

De **Wgr-wijziging van 1 juli 2022** versterkte de democratische legitimatie door eisen aan:
- Raadsinvloed op GR-bestuur
- Transparantie van GR-begroting en jaarrekening
- Waarborging van klachtenprocedures

## Juridische grondslag

> **Wet gemeenschappelijke regelingen (Wgr)** — Grondwettelijk grondslag (art. 126 Gw) voor samenwerking tussen publiekrechtelijke lichamen. De Wgr bepaalt de procedure voor oprichting, bestuursvorm, financiën en opheffing.

Elke GR heeft:
- Deelnemersovereenkomst (juridisch document)
- Eigen rechtspersoonlijkheid (handlichaam met eigen vermogen)
- Inschrijving in KvK-handelsregister
- Raad van Advies en/of Raad van Bestuur (afhankelijk van GR-type)

## BO-definitie

> **Gemeenschappelijke Regeling** — Publiekrechtelijke samenwerkingsconstructie tussen gemeenten, provincies en/of waterschappen, gevormd op grondslag van de Wet gemeenschappelijke regelingen, met eigen juridische persoonlijkheid, bestuursstructuur, vermogen en taken.

## Verschil met andere samenwerkingsvormen

| Vorm | Juridische basis | Persoonlijkheid | Bestuur |
|---|---|---|---|
| **Gemeenschappelijke Regeling** | Wgr | Ja (eigen) | Raad/College |
| **Samenwerkingsovereenkomst** | Civielrechtelijk | Nee (doorgerekend) | Gezamenlijke commissie |
| **Fusie** | Gemeentewet | Ja (ene gemeente) | Raad nieuwe gemeente |
| **Gemeente-maatschappij** | Privaatrecht | Ja (BV/NV) | Raad van Commissarissen |

## Attributen (gemeentelijk perspectief)

- **Deelnemende overheden**: Lijst van gemeenten/provincies/waterschappen
- **Takenpakket**: Welke taken worden gezamenlijk uitgevoerd
- **Begroting**: Jaarlijkse financiële planning
- **Personeel**: Aantal werknemers, organisatiestructuur
- **Klachtenprocedure**: Hoe burgers kunnen reageren
- **Raadszetel/invloed**: Welke gemeenteraadslid voert het woord

## Relaties

- **Gemeente** [2..*] — Gemeenschappelijke Regeling heeft twee of meer deelnemers
- **Bestuur** [1] — Eigen bestuurs- en financiële verantwoordelijkheid
- **Taken/Bedrijfsprocessen** [1..*] — Gezamenlijke uitvoering van specifieke taken

## Bedrijfsprocessen

1. **GR oprichten** (onderhandeling partners, deelnemersovereenkomst, KvK-inschrijving)
2. **Bestuur voeren** (raadsvergaderingen, commissies, beleidsvorming)
3. **Taken uitvoeren** (primaire functies: GGD-taken, jeugdzorg, etc.)
4. **Financiën beheren** (begroting, jaarrekening, kascontrole)
5. **GR wijzigen of opheffen** (deelnemerswijzigingen, taakuitbreiding, ontbinding)

## Bedrijfsfuncties

- **Regionale samenwerking** — Pooling van middelen en expertise
- **Schaalvergroting** — Efficiencybaten door samenvoeging
- **Democratische legitimatie** — Raden betrokken bij GR-bestuur
- **Specialisatie** — Deskundigheid op bepaalde beleidsterreinen

## Bronsignalering

Zie bronsamenvatting:
- [[Wiki/Bronsamenvattingen/Bestuur/gemeentelijke-samenwerking|Gemeentelijke Samenwerking]] — Wgr-grondslag, voorbeelden (GGD, RUD, etc.), wijziging 2022

## GGM-hiaat

Dit BO heeft **geen GGM-entiteit**. Gemeenschappelijke Regelingen zijn juridische/organisatorische constructies die niet in het GGM worden gemodelleerd. Dit is een **structureel hiaat** omdat:

1. Het GGM modelleert organisatiestructuur alleen op gemeentelijk niveau (taakveld 9: Organisatie-indeling bevat slechts Program en Project)
2. Inter-gemeente samenwerkingsvormen (GR, samenwerkingsverbanden) zijn niet opgenomen
3. Dit is relevant voor gemeentelijk bestuur: 80%+ van gemeenten werkt met één of meer GR's

**Terugmelding:** Gemeenschappelijke Regelingen zouden kunnen worden gemodelleerd in GGM taakveld 0 (Bestuur) of taakveld 9 (Interne Organisatie), als nieuw beleidsdomein "Inter-gemeente Samenwerking" of uitbreiding van Organisatie-indeling.

## Bronnen

- [[Wiki/Bronsamenvattingen/Bestuur/gemeentelijke-samenwerking]]
