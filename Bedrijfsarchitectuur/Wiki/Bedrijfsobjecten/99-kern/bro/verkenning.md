---
type: element
naam: Verkenning
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

bo_definitie: "Waarneming van de opbouw van de ondergrond op een punt, langs een lijn of in een vlak, geregistreerd in de Basisregistratie Ondergrond."
bo_toelichting: "De gemeente is bronhouder van verkenningen die bij de uitvoering van wettelijke taken worden uitgevoerd. De uitvoering wordt doorgaans uitbesteed aan ingenieursbureaus (dataleveranciers). Elke verkenning heeft een BRO-ID, verkenningstype, locatie, tijdstip en meetresultaten. Alle kerngegevens zijn authentiek."
bo_subtypes: []
bo_synoniemen: []
bo_homoniemen: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Constructie]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: "Verkenningen worden uitgevoerd in of bij constructies (bijv. waterstandmeting in monitoringput)"
bedrijfsprocessen:
  - "Grondwatermonitoring"
  - "Bodemonderzoek"
  - "Geotechnisch onderzoek"
bedrijfsfuncties:
  - "Bodembeheer"
  - "Waterbeheer"
---

# Verkenning

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Identiteit | ✅ | Eigen BRO-ID (identificatiecode), verkenningstype, locatie |
| Levenscyclus | ✅ | Wordt aangemaakt, kan worden aangevuld, gecorrigeerd, uit registratie genomen |
| Eigenaarschap | ✅ | Gemeente is bronhouder, verantwoordelijk voor kwaliteit |
| Relaties | ✅ | Gekoppeld aan constructies (putten), monitoringnetten, brondocumenten |
| Meervoud | ✅ | Honderden per gemeente (bodemonderzoeken, sonderingen, grondwatermetingen) |

## Beschrijving

Een Verkenning is een waarneming van de opbouw van de ondergrond, vastgelegd als registratieobject in de Basisregistratie Ondergrond (BRO). De gemeente bestelt verkenningen bij de uitvoering van wettelijke taken — bodemonderzoek bij bouwplannen, sonderingen bij infrastructuurprojecten, grondwaterstandmetingen bij peilbeheer.

De gemeente is bronhouder: verantwoordelijk voor aanlevering (via het bronhouderportaal, binnen 20 werkdagen) en kwaliteit (jaarlijkse controle). De feitelijke uitvoering en aanlevering worden doorgaans uitbesteed aan ingenieursbureaus (dataleveranciers).

Alle authentieke gegevens per verkenning (art. 19 Wet BRO): identificatiecode, verkenningstype, locatie, tijdstip, bronhouder, meetresultaten.

## Subtypes

Concrete BRO-registratieobjecten die specialisaties zijn van Verkenning:

- **Grondwaterstandonderzoek (GLD)** — herhaaldelijke metingen van waterstand in meter NAP; observaties met tijdmeetwaardereeksen; kwaliteitsregimes IMBRO/IMBRO/A
- **Grondwatersamenstellingsonderzoek (GAR)** — monitoring grondwaterkwaliteit
- **Booronderzoek (BHR-GT, BHR-P)** — waarneming van grondopbouw via boring
- **Sondering (CPT)** — meting van grondweerstand via conus

## Procesbron

De gemeente bestelt verkenningen bij bodemonderzoek (omgevingsvergunning, sanering), geotechnisch onderzoek (infrastructuurprojecten) en grondwatermonitoring (peilbeheer). Wettelijke grondslag: art. 9 en 19 Wet BRO.

## Relaties

| Relatie | BO | Richting | Beschrijving | Bron |
|---|---|---|---|---|
| associatie | [[Constructie]] | ↔ | Verkenning in/bij constructie (meting in monitoringput) | Wet BRO |
| associatie | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | ← | Bodemonderzoek als bijlage bij omgevingsvergunning of melding | cross-domein |

## Terugmelding GGM

GGM-hiaat: de BRO en haar objecttypen zijn niet in het GGM gemodelleerd. Het GGM bevat geen entiteiten voor Verkenning, Constructie of Gebruiksrecht.

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/wet-bro]]
- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bro-gld]]
