---
type: element
naam: Meerjarenplan
onderwerp: [Informatiesamenleving]
archimate_type: business-object
grondslag: governance-object

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

bo_definitie: "Document met langetermijndoelen en stappen om digitale overheidsinformatie duurzaam toegankelijk te maken (art. 6.2 Woo)."
bo_toelichting: "Per bestuurslaag stelt de koepelorganisatie één meerjarenplan op namens haar achterban: de VNG voor gemeenten, het Interprovinciaal Overleg voor provincies, de Unie van Waterschappen voor waterschappen, en het Rijk voor departementen en zelfstandige bestuursorganen. Het meerjarenplan voor gemeenten dateert van 22 april 2022 en wordt momenteel geactualiseerd voor de periode 2026-2030."
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Actoren/acoi|ACOI]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Het ACOI adviseert de minister periodiek over aanpassing van het meerjarenplan en rapporteert over de voortgang van de uitvoering"
bedrijfsprocessen: [Verbetering digitale informatiehuishouding]
bedrijfsfuncties: [Informatievoorziening]
---

# Meerjarenplan

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Identificeerbaar | Ja — één meerjarenplan per bestuurslaag, met eigen naam en versiedatum |
| Eigen attributen | Ja — langetermijndoelen, kortetermijnstappen, betrokken thema's |
| Levenscyclus | Ja — opgesteld → aangeboden aan Staten-Generaal → jaarlijks gemonitord → periodiek geactualiseerd |
| Gemeentelijk eigendom | Ja — het gemeentelijke meerjarenplan wordt namens gemeenten door de VNG opgesteld en aan de minister aangeboden |
| Wettelijke grondslag | Ja — Wet open overheid (art. 6.2) |
| Registratieverplichting | Ja — de minister zendt het meerjarenplan verplicht naar de Eerste en Tweede Kamer (art. 6.2 lid 1); het ACOI adviseert er periodiek over (art. 7.2 lid 2) |

Score: 6/6 criteria.

## Beschrijving

Het meerjarenplan is het document waarin een bestuurslaag beschrijft hoe zij haar digitale overheidsinformatie duurzaam toegankelijk maakt. Het bevat langetermijndoelen voor de verbetering van de wijze waarop digitale documenten worden vervaardigd, geordend, bewaard, vernietigd en ontsloten, en de stappen die daartoe op korte termijn worden gezet. Doel is dat eenieder zo veel mogelijk inzicht kan hebben in de aanwezigheid van publieke informatie bij een bestuursorgaan.

Er zijn vier meerjarenplannen "Digitale informatiehuishouding", eind 2023 gezamenlijk aangeboden aan de Eerste en Tweede Kamer: één voor het Rijk, één voor provincies (Interprovinciaal Overleg), één voor waterschappen (Unie van Waterschappen) en één voor gemeenten (VNG). Ze kennen elk eigen opgaven en accenten, met veel onderlinge overeenkomsten.

De VNG monitort jaarlijks via de monitor Implementatie Woo de voortgang van de implementatie bij gemeenten en gemeenschappelijke regelingen; de uitkomsten worden gebruikt om het meerjarenplan te actualiseren en gepubliceerd op het dashboard Woo op waarstaatjegemeente.nl. Het geactualiseerde meerjarenplan voor gemeenten (periode 2026-2030) besteedt onder meer meer aandacht aan actieve openbaarmaking en de samenhang tussen de Woo en de nieuwe Archiefwet.

Hoofdstuk 6 Woo, en daarmee de verplichting tot een meerjarenplan, heeft een tijdelijk karakter: zodra duurzaam is vastgesteld dat digitale informatie voldoende toegankelijk is, kan het hoofdstuk bij koninklijk besluit worden ingetrokken (art. 10.2f Woo).

## Juridische bron

Wettelijke grondslag: Wet open overheid, artikel 6.2 (Hoofdstuk 6 — Digitale informatiehuishouding).

Toelichting en context in [[Wiki/Bronsamenvattingen/Informatiesamenleving/wet-open-overheid-actieve-openbaarmaking|Wet open overheid — actieve openbaarmaking]] en in de handreiking Woo (VNG/Pels Rijcken), §6.3.

## Relaties

| Relatie | Bedrijfsobject | Richting | Beschrijving |
|---|---|---|---|
| associatie | [[Wiki/Actoren/acoi\|ACOI]] | ← | Het ACOI adviseert periodiek over aanpassing van het meerjarenplan en rapporteert over de stand van de informatiehuishouding |

## Bedrijfsprocessen

- **Verbetering digitale informatiehuishouding** — opstellen, aanbieden aan de Staten-Generaal, jaarlijks monitoren, periodiek actualiseren

## Bronnen
- [[Wiki/Bronsamenvattingen/Informatiesamenleving/wet-open-overheid-actieve-openbaarmaking]]

## Terugmelding GGM

GGM-hiaat: het meerjarenplan is een wettelijk verplicht governance-document (art. 6.2 Woo) zonder GGM-tegenhanger. Het GGM modelleert governance-instrumenten doorgaans niet compleet; voor dit specifieke instrument — met een eigen wettelijke aanbiedings- en monitoringsplicht — is er geen aanwijsbare reden om aan te nemen dat het GGM het wél zou moeten dekken buiten de reeds vastgelegde governance-objecten in dit domein.
