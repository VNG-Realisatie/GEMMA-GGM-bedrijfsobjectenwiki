---
type: element
naam: Trajectplan
onderwerp: [werk en inkomen]
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

bo_definitie: "Overkoepelend plan dat de re-integratieactiviteiten voor een werkzoekende organiseert en coördineert."
bo_toelichting: "Het trajectplan bundelt meerdere re-integratievoorzieningen in een samenhangend geheel. Het SGR modelleert het als aparte klasse met eigen attributen. Het GGM koppelt werkzoekende direct aan re-integratievoorzieningen zonder tussenliggend plan-object — dit is een GGM-hiaat."
bo_synoniemen:
- naam: Plan van aanpak
  context: Participatiewet art. 44a en art. 9a lid 7-9 — de wettelijke term voor hetzelfde concept dat het SGR "Trajectplan" noemt
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Werkzoekende]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "trajectplan voor werkzoekende"
  - type: associatie
    bedrijfsobject: "[[Re-integratievoorziening]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "organiseert re-integratievoorzieningen"
bedrijfsprocessen: [intake werkzoekende, trajectbepaling, voortgangsbewaking, evaluatie en afsluiting]
bedrijfsfuncties: [arbeidsparticipatie, re-integratie]
---

## BO-criteria toetsing

| Criterium | Toets |
|---|---|
| Betekenis binnen domein | ✅ Overkoepelend plan dat samenhang brengt in re-integratieactiviteiten |
| Herkenbaar voor domeinexperts | ✅ Standaardbegrip bij klantmanagers; expliciet in SGR gemodelleerd |
| Eigen bestaan | ✅ Coördineert meerdere re-integratievoorzieningen voor één werkzoekende |
| Meervoud | ✅ Per werkzoekende een trajectplan |
| Levenscyclus | ✅ Opgesteld → actief → afgerond/beëindigd |
| Relaties | ✅ Werkzoekende, Re-integratievoorziening, contactcoach |

Score: **6/6**

## Beschrijving

Een trajectplan is het overkoepelende plan dat beschrijft welke re-integratieactiviteiten worden ingezet voor een werkzoekende en in welke volgorde. Het brengt samenhang aan tussen afzonderlijke re-integratievoorzieningen en dient als sturingsinstrument voor de klantmanager.

Het SGR modelleert het trajectplan als aparte klasse met attributen voor datum aanvang en einde, financiële administratieve afhandeling, contactgegevens van de re-integratiecoach, en verwijzingen naar de gekoppelde re-integratievoorzieningen. Zowel de GSD (gemeente) als UWV werken met trajectplannen.

Het onderscheid met [[Re-integratievoorziening]] is: het trajectplan is het *plan* (coördinatie, tijdlijn, doelen), de re-integratievoorziening is het *middel* (specifieke toekenning met registratienummer en eigen levenscyclus).

De Participatiewet gebruikt voor hetzelfde concept de term "plan van aanpak" (art. 44a, verplicht bij toekenning van bijstand aan personen van 18-27 jaar; art. 9a lid 7-9, voor de alleenstaande ouder met ontheffing van de arbeidsverplichting). Het plan bevat de uitwerking van de ondersteuning en de daaraan verbonden verplichtingen, en wordt periodiek geëvalueerd en zo nodig bijgesteld — dit bevestigt de levenscyclus (opgesteld → actief → periodiek herzien → afgerond) die het SGR als Trajectplan modelleert.

## Procesbron

Het trajectplan is afgeleid uit het SGR 19.0 (BKWI), waar het als aparte klasse is gemodelleerd in het conceptueel gegevensdeelmodel Arbeidstoeleidingsgegevens. Zie [[Wiki/Bronsamenvattingen/Werk en Inkomen/wet-suwi-en-sgr|Wet SUWI en SGR]]. De wettelijke grondslag voor het "plan van aanpak" staat in art. 44a en art. 9a lid 7-9 Participatiewet. Zie [[Wiki/Bronsamenvattingen/Werk en Inkomen/participatiewet|Participatiewet]].

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| trajectplan voor [[Werkzoekende]] | naar dit BO | 1 | SGR |
| organiseert [[Re-integratievoorziening\|Re-integratievoorziening]] | van dit BO | 0..* | SGR |

## Bronnen

- [[Wiki/Bronsamenvattingen/Werk en Inkomen/wet-suwi-en-sgr]]
- [[Wiki/Bronsamenvattingen/Werk en Inkomen/participatiewet]]

## Terugmelding GGM

GGM-hiaat: het GGM Werk-domein koppelt Werkzoekende direct aan Reintegratievoorziening [0..*] zonder tussenliggend plan-object. Het SGR modelleert Trajectplan als aparte klasse. Teruggemeld als #85 in [[Wiki/Analyses/ggm-terugmeldingen]].
