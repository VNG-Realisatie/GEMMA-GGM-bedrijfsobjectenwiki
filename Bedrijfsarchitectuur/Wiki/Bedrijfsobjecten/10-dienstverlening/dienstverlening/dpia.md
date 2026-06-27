---
type: bedrijfsobject
naam: DPIA
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

bo_definitie: "Beoordeling van het effect van een beoogde gegevensverwerking op de bescherming van persoonsgegevens, verplicht bij hoog-risicoverwerkingen."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/grondrechteneffectbeoordeling|Grondrechteneffectbeoordeling]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: "Grondrechteneffectbeoordeling vult DPIA aan bij AI-systemen (art. 27 lid 4 AI-verordening)"
bedrijfsprocessen: [Privacy-compliance, Inrichting gegevensverwerking]
bedrijfsfuncties: [Informatievoorziening, Juridische zaken, Privacy]
---

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Betekenis | Formele beoordeling van privacyrisico's, wettelijk gedefinieerd in art. 35 AVG |
| Herkenbaarheid | De gemeente herkent dit als zelfstandig ding — "we moeten een DPIA doen voor verwerking X" |
| Eigen bestaan | 4 verplichte elementen (art. 35 lid 7 a-d), eigen resultaat |
| Meervoud | Per hoog-risicoverwerking een aparte DPIA |
| Levenscyclus | Uitvoeren → FG-advies → evt. AP-raadpleging → hertoetsing bij wijziging → periodiek (3 jaar) |
| Relaties | Met verwerkingsactiviteit (onderwerp), FG (adviseur), AP (toezichthouder), grondrechteneffectbeoordeling (aanvulling) |

Resultaat: 6/6 — BO.

## Beschrijving

De DPIA (Data Protection Impact Assessment), in de wet gegevensbeschermingseffectbeoordeling (GEB) genoemd, is een verplichte beoordeling bij gegevensverwerkingen met een waarschijnlijk hoog risico voor de rechten en vrijheden van betrokkenen (art. 35 AVG).

De DPIA bevat minimaal vier elementen (art. 35 lid 7):
1. Systematische beschrijving van de verwerkingen en doeleinden
2. Beoordeling van noodzaak en evenredigheid
3. Beoordeling van risico's voor rechten en vrijheden van betrokkenen
4. Beoogde maatregelen om risico's aan te pakken

Een DPIA is in ieder geval verplicht bij (art. 35 lid 3):
- Geautomatiseerde beoordeling met rechtsgevolgen (profilering)
- Grootschalige verwerking bijzondere persoonsgegevens
- Stelselmatige en grootschalige monitoring openbare ruimten

De AP hanteert daarnaast een DPIA-lijst en de 9 EDPB-criteria (vuistregel: 2+ criteria → verplicht).

De DPIA is een continu proces: hertoetsing is verplicht bij verandering van risico (art. 35 lid 11) en periodiek aan te raden (bijv. eens per 3 jaar). Bij restrisico's is voorafgaande raadpleging bij de AP verplicht (art. 36). Publicatie is niet verplicht maar voor overheden aan te raden.

Bij gebruik van hoog-risico AI-systemen wordt de DPIA aangevuld met een [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/grondrechteneffectbeoordeling|Grondrechteneffectbeoordeling]] (art. 27 AI-verordening).

## Procesbron

Wettelijke grondslag: art. 35 Verordening (EU) 2016/679 (AVG). De verplichting geldt voor alle verwerkingsverantwoordelijken bij hoog-risicoverwerkingen.

Zie [[Wiki/Bronsamenvattingen/Informatiesamenleving/avg-verwerkingsregister-dpia|AVG art. 30, 35, 36]] voor de volledige wettekst.
Zie [[Wiki/Bronsamenvattingen/Informatiesamenleving/dpia-ap|DPIA — AP]] voor de praktische toelichting met 9 criteria en uitvoeringsinstructies.

## Relaties

| Relatie | Richting | Beschrijving |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/grondrechteneffectbeoordeling\|Grondrechteneffectbeoordeling]] | bidirectioneel | DPIA wordt aangevuld met grondrechteneffectbeoordeling bij AI-systemen |

Buiten wiki-scope (geen BO):
- **Verwerkingsactiviteit** — onderwerp van de beoordeling (potentieel BO)
- **FG** — verplichte adviesrol
- **AP** — toezichthouder, ontvangt voorafgaande raadpleging bij restrisico's

## Bedrijfsprocessen

- **Privacy-compliance** — waarborgen AVG-naleving
- **Inrichting gegevensverwerking** — beoordeling vóór start verwerking

## Bedrijfsfuncties

- **Informatievoorziening** — eigenaar verwerkingen
- **Juridische zaken** — privacytoetsing
- **Privacy** — FG en privacyteam

## Bronnen

- [[Wiki/Bronsamenvattingen/Informatiesamenleving/avg-verwerkingsregister-dpia]]
- [[Wiki/Bronsamenvattingen/Informatiesamenleving/dpia-ap]]

## Terugmelding GGM

Geen GGM-entiteit gevonden. Het GGM bevat geen privacy-/AVG-gerelateerde entiteiten.

Teruggemeld als #69 in [[Wiki/Analyses/ggm-terugmeldingen]].
