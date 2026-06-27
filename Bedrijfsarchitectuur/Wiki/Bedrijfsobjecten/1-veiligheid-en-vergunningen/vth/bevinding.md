---
type: bedrijfsobject
naam: Bevinding
onderwerp: [Omgevingswet]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Bevinding
ggm_guid: EAID_ED0D0224_0A30_435b_AB25_87FDA8DF4078
ggm_uml_type: Class
ggm_beleidsdomein: "1 Veiligheid en Vergunningen"
ggm_taakveld: "1 Veiligheid en Vergunningen"
ggm_diagram: [Diagram Vergunningen en Meldingen, Verkamering en Woonoverlast]
ggm_diagram_ids: [EAID_BB52C835_0B2D_4164_AC9D_9D6EDBD7E267, EAID_B039478A_DAF7_458f_A7C7_E4744EC08DBF]
ggm_definitie: "Een bevinding is de uitkomst van een waarneming of onderzoek die aangeeft wat is geconstateerd bij beoordeling of inspectie."
ggm_toelichting: "In algemene en bestuurlijke contexten verwijst bevinding naar wat er naar voren komt uit onderzoek, inspectie of waarneming, bijvoorbeeld tijdens een controle, audit of beoordeling van een situatie."
ggm_synoniemen: ""
ggm_herkomst: ""

ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""

bo_definitie: "Uitkomst van een inspectie of waarneming die vastlegt wat is geconstateerd, inclusief het controle-element, het niveau, het resultaat en het risico."
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Inspectie]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een bevinding hoort bij een inspectie"
  - type: associatie
    bedrijfsobject: "[[Bevinding]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een bevinding kan gerelateerd zijn aan andere bevindingen"
bedrijfsprocessen: [toezicht op realisatie, toezicht op bestaande bouw, handhaving]
bedrijfsfuncties: [toezicht en handhaving]
---

## BO-criteria toetsing

1. **Identificeerbare instanties** — elke bevinding is een afzonderlijke constatering met eigen attributen
2. **Eigen attributen** — controleElement, controleniveau, resultaat, risico, diepte, activiteit, fase
3. **Levenscyclus** — geconstateerd → beoordeeld → opgevolgd (kan leiden tot handhaving)
4. **Meerdere processen** — toezicht op realisatie, toezicht op bestaande bouw, handhaving
5. **Relevant op bedrijfsniveau** — bevindingen worden gemonitord op thema en ernst in VTH-jaarplannen; bepalen of handhaving nodig is
6. **Gemeentelijk perspectief** — de gemeente registreert bevindingen als onderbouwing voor handhavingsbeslissingen

## Beschrijving

Een bevinding is de uitkomst van een inspectie: wat is er geconstateerd bij de controle? Het registreert op welk controle-element de bevinding betrekking heeft (bijv. constructieve veiligheid, brandveiligheid), op welk niveau is gecontroleerd, wat het resultaat is en welk risico de bevinding vertegenwoordigt. De ernst van de bevinding, in combinatie met het gedrag van de overtreder, bepaalt via de sanctiematrix welke vervolgactie de gemeente neemt.

> "Voor het toezicht op de realisatie van vergunning wordt gemonitord op: de uitgevoerde controles, hercontrole of nieuwe controle, de geconstateerde overtredingen, de ernst van de geconstateerde overtreding." (bron: Uitvoeringsbeleid VTH Delft §5.6)

## GGM-bron

> Een bevinding is de uitkomst van een waarneming of onderzoek die aangeeft wat is geconstateerd bij beoordeling of inspectie.

- **Entiteit:** Bevinding
- **Beleidsdomein:** 1 Veiligheid en Vergunningen
- **Attributen:** controleElement, controleniveau, resultaat, risico, diepte, activiteit, fase, datumAanmaak, aangemaaktDoor, datumMutatie, gemuteerdDoor
- **Matchsterkte:** exact — definitie en scope komen overeen

## Relaties

| Relatie | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/inspectie\|Inspectie]] | van-dit-BO | 0..* | Een bevinding hoort bij een inspectie | GGM |
| [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/bevinding\|Bevinding]] | naar-dit-BO | 0..* | Bevindingen kunnen hiërarchisch gerelateerd zijn | GGM |

## Bedrijfsprocessen

- Toezicht op realisatie (constatering afwijking van vergunning)
- Toezicht op bestaande bouw (constatering overtreding)
- Handhaving (onderbouwing voor sanctiebeslissing)

## Bronnen
- [[Wiki/Bronsamenvattingen/Omgevingswet/uitvoeringsbeleid-vth-delft]]
