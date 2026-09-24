---
type: element
naam: Constructie
onderwerp: [Basisregistraties]
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

bo_definitie: "Werk in de ondergrond voor het winnen of benutten van natuurlijke hulpbronnen, het opslaan van stoffen of het meten van een aan de ondergrond gerelateerde parameter, geregistreerd in de BRO."
bo_toelichting: "De gemeente is bronhouder van constructies die zij laat aanleggen of beheert, zoals grondwatermonitoringputten. Elke constructie heeft een BRO-ID, type, locatie, eigenaar en kenmerken van bestanddelen."
bo_subtypes: []
bo_synoniemen: []
bo_homoniemen: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Verkenning]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: "Verkenningen worden uitgevoerd in/bij constructies"
bedrijfsprocessen:
  - "Grondwatermonitoring"
  - "Beheer ondergrondse infrastructuur"
bedrijfsfuncties:
  - "Waterbeheer"
---

# Constructie

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Identiteit | ✅ | Eigen BRO-ID, type, locatie, eigenaar |
| Levenscyclus | ✅ | Aanleg, wijziging (verlenging buis, nieuwe filter), beëindiging |
| Eigenaarschap | ✅ | Gemeente is bronhouder en vaak eigenaar |
| Relaties | ✅ | Gekoppeld aan verkenningen (metingen), monitoringnetten |
| Meervoud | ✅ | Tientallen tot honderden monitoringputten per gemeente |

## Beschrijving

Een Constructie is een werk in de ondergrond, geregistreerd in de Basisregistratie Ondergrond. Voor de gemeente zijn grondwatermonitoringputten (GMW) de belangrijkste specialisatie: fysieke constructies met buizen en filters waarmee grondwaterstanden en -samenstelling worden gemeten.

De gemeente laat putten aanleggen door gespecialiseerde bedrijven en is als bronhouder verantwoordelijk voor de registratie in de BRO. De constructie heeft een eigen levenscyclus: aanleg, eventuele wijzigingen (nieuwe buis, filterverlenging) en uiteindelijk beëindiging.

Alle authentieke gegevens per constructie (art. 21 Wet BRO): identificatiecode, type, locatie, eigenaar (KvK-nummer), kenmerken bestanddelen, meetresultaten.

## Specialisaties

Concrete BRO-registratieobjecten die specialisaties zijn van Constructie:

- **Grondwatermonitoringput (GMW)** — fysieke constructie met buizen en filters voor meting van grondwaterstand en -samenstelling; honderden per gemeente; eigen BRO-ID, locatie, kenmerken per buis

## Procesbron

Wettelijke grondslag: art. 9 en 21 Wet BRO. De gemeente bestelt aanleg en onderhoud van monitoringputten bij gespecialiseerde bedrijven.

## Relaties

| Relatie | BO | Richting | Beschrijving | Bron |
|---|---|---|---|---|
| associatie | [[Verkenning]] | ↔ | Verkenningen (metingen) worden uitgevoerd in constructies | Wet BRO |

## Terugmelding GGM

GGM-hiaat: BRO-objecttypen niet in het GGM gemodelleerd.

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/wet-bro]]
- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bro-gld]]
