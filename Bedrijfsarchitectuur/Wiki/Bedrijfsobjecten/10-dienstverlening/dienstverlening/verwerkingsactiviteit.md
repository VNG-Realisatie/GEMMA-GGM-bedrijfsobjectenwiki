---
type: bedrijfsobject
naam: Verwerkingsactiviteit
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

bo_definitie: "Verwerking van persoonsgegevens met eigen doel en grondslag, verplicht geregistreerd in het verwerkingsregister conform AVG art. 30."
bo_toelichting: ''
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/dpia|DPIA]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Hoog-risicoverwerkingen vereisen een DPIA"
bedrijfsprocessen: [Privacy-compliance, Gegevensbeheer]
bedrijfsfuncties: [Informatievoorziening, Privacy]
---

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Betekenis | Individuele verwerking van persoonsgegevens met eigen doel en grondslag, art. 30 AVG |
| Herkenbaarheid | De gemeente herkent dit — "de verwerking van BRP-gegevens voor inburgering" |
| Eigen bestaan | 7 verplichte attributen (art. 30 lid 1 a-g) |
| Meervoud | Gemeente heeft tientallen tot honderden verwerkingsactiviteiten |
| Levenscyclus | Aanmaken → bijwerken → beëindigen |
| Relaties | Met verwerkingsregister (container), DPIA (beoordeling), FG (toezicht), betrokkenen (categorieën) |

Resultaat: 6/6 — BO.

## Beschrijving

Een verwerkingsactiviteit is een individuele verwerking van persoonsgegevens die de gemeente als verwerkingsverantwoordelijke uitvoert. Elke verwerkingsactiviteit heeft een eigen doel, grondslag en set betrokkenen. De gemeente is verplicht alle verwerkingsactiviteiten bij te houden in een verwerkingsregister (art. 30 AVG).

Per verwerkingsactiviteit registreert het verwerkingsregister 7 verplichte velden (art. 30 lid 1):

a) naam en contactgegevens verwerkingsverantwoordelijke, gezamenlijke verwerkingsverantwoordelijken, vertegenwoordiger, FG
b) verwerkingsdoeleinden
c) categorieën betrokkenen en categorieën persoonsgegevens
d) categorieën ontvangers (incl. derde landen/internationale organisaties)
e) doorgiften aan derde landen (incl. waarborgen)
f) beoogde bewaartermijnen per gegevenscategorie
g) beschrijving technische en organisatorische beveiligingsmaatregelen

Het verwerkingsregister is schriftelijk (incl. elektronisch) en wordt desgevraagd ter beschikking gesteld aan de toezichthouder (AP). Bij hoog-risicoverwerkingen is een [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/dpia|DPIA]] verplicht.

## Procesbron

Wettelijke grondslag: art. 30 Verordening (EU) 2016/679 (AVG). De verplichting geldt voor alle verwerkingsverantwoordelijken (uitzondering: <250 medewerkers bij incidentele, niet-risicovolle verwerkingen zonder bijzondere gegevens).

Zie [[Wiki/Bronsamenvattingen/Informatiesamenleving/avg-verwerkingsregister-dpia|AVG art. 30, 35, 36]] voor de volledige wettekst.

## Relaties

| Relatie | Richting | Beschrijving |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/dpia\|DPIA]] | naar-dit-BO | Hoog-risicoverwerkingen vereisen een DPIA |

Buiten wiki-scope (geen BO):
- **Verwerkingsregister** — container van verwerkingsactiviteiten
- **FG** — houdt toezicht op het register
- **AP** — kan register opvragen

## Bedrijfsprocessen

- **Privacy-compliance** — bijhouden verwerkingsregister
- **Gegevensbeheer** — inrichten en documenteren verwerkingen

## Bedrijfsfuncties

- **Informatievoorziening** — eigenaar verwerkingen
- **Privacy** — FG en privacyteam

## Bronnen

- [[Wiki/Bronsamenvattingen/Informatiesamenleving/avg-verwerkingsregister-dpia]]

## Terugmelding GGM

Geen GGM-entiteit gevonden. Het GGM bevat geen privacy-/AVG-gerelateerde entiteiten.

Teruggemeld als #70 in [[Wiki/Analyses/ggm-terugmeldingen]].
