---
type: bedrijfsobject
naam: Grondrechteneffectbeoordeling
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

gemma_definitie: "Verplichte beoordeling door overheden van de gevolgen voor de grondrechten bij inzet van een hoog-risico AI-systeem."
relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak|Zaak]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Beoordeling kan als zaak worden behandeld"
bedrijfsprocessen: [AI-compliance, Ingebruikname AI-systeem]
bedrijfsfuncties: [Informatievoorziening, Juridische zaken]
---

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Betekenis | Formele beoordeling van grondrechtenrisico's bij inzet hoog-risico AI, wettelijk gedefinieerd in art. 27 AI-verordening |
| Herkenbaarheid | De gemeente herkent dit als een verplichte actie per hoog-risico AI-systeem |
| Eigen bestaan | Bestaat onafhankelijk; heeft 6 verplichte elementen (art. 27 lid 1 a-f) |
| Meervoud | Per hoog-risico AI-systeem een aparte beoordeling |
| Levenscyclus | Uitvoeren → melden aan markttoezichtautoriteit → actualiseren bij wijzigingen |
| Relaties | Met AI-systeem (onderwerp), DPIA (aanvulling op), markttoezichtautoriteit (ontvanger) |

Resultaat: 6/6 — BO.

## Beschrijving

De grondrechteneffectbeoordeling is een verplichte beoordeling die overheden en andere publiekrechtelijke organen moeten uitvoeren vóór de inzet van een hoog-risico AI-systeem (art. 27 AI-verordening). De beoordeling brengt in kaart welke gevolgen het gebruik van het AI-systeem kan hebben voor de grondrechten van burgers.

De beoordeling bestaat uit zes verplichte elementen:
1. Beschrijving van de processen waarbij het AI-systeem wordt gebruikt
2. Periode en frequentie van gebruik
3. Categorieën personen die gevolgen ondervinden
4. Specifieke risico's op schade voor die personen
5. Uitvoering van menselijk toezicht
6. Maatregelen bij het voordoen van risico's, inclusief interne governance en klachtenregelingen

De beoordeling vormt een aanvulling op de gegevensbeschermingseffectbeoordeling (DPIA, AVG art. 35) en vervangt deze niet. Het AI-bureau ontwikkelt een sjabloon/vragenlijst om de beoordeling te vereenvoudigen.

Na uitvoering meldt de gebruiksverantwoordelijke de resultaten aan de markttoezichtautoriteit. Bij wijzigingen in een van de zes elementen moet de beoordeling worden geactualiseerd.

## Procesbron

Wettelijke grondslag: art. 27 Verordening (EU) 2024/1689 (AI-verordening). De verplichting geldt voor publiekrechtelijke organen en particuliere entiteiten die openbare diensten verlenen.

Zie [[Wiki/Bronsamenvattingen/Informatiesamenleving/eu-ai-verordening|EU AI-verordening]] voor de volledige wettekst van art. 27 met de zes verplichte elementen.

Zie [[Wiki/Bronsamenvattingen/Informatiesamenleving/factsheet-ai-verordening-vng|VNG Uitvoeringsanalyse]] voor het gemeentelijk perspectief: het AI-bureau ontwikkelt een sjabloon, VNG/BZK maken dit beschikbaar voor gemeenten met geleerde lessen uit de IAMA-evaluatie.

## Relaties

| Relatie | Richting | Beschrijving |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] | naar-dit-BO | Beoordeling kan als zaak worden behandeld |

Buiten wiki-scope (geen BO):
- **DPIA** — grondrechteneffectbeoordeling is een aanvulling op de DPIA (art. 27 lid 4)
- **Hoog-risico AI-systeem** — onderwerp van de beoordeling
- **Markttoezichtautoriteit** — ontvangt de resultaten van de beoordeling (art. 27 lid 3)

## Bedrijfsprocessen

- **AI-compliance** — vaststellen of AI-systemen aan verplichtingen voldoen
- **Ingebruikname AI-systeem** — beoordeling moet vóór eerste gebruik zijn uitgevoerd

## Bedrijfsfuncties

- **Informatievoorziening** — eigenaar AI-systemen
- **Juridische zaken** — grondrechtentoetsing

## Bronnen

- [[Wiki/Bronsamenvattingen/Informatiesamenleving/eu-ai-verordening]]
- [[Wiki/Bronsamenvattingen/Informatiesamenleving/ai-verordening-ap]]
- [[Wiki/Bronsamenvattingen/Informatiesamenleving/factsheet-ai-verordening-vng]]

## Terugmelding GGM

Geen GGM-entiteit gevonden. Dit is een procesobject dat voortkomt uit de AI-verordening (2024). Het GGM bevat (nog) geen AI-gerelateerde entiteiten.

Teruggemeld als #68 in [[Wiki/Analyses/ggm-terugmeldingen]].
