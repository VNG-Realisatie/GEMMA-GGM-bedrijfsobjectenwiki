---
type: element
naam: Reserve
onderwerp: [Financien]
archimate_type: "business-object"
grondslag: "procesobject"
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
bo_definitie: "Eigen vermogen van de gemeente op de balans, onderscheiden in algemene reserve (vrij besteedbaar) en bestemmingsreserves (door de raad geoormerkt)."
bo_toelichting: "Reserves zijn geen geld maar zitten vast in bezittingen. Ze vormen de buffer voor financiële tegenvallers en de financieringsruimte voor investeringen."
bo_subtypes: []
bo_synoniemen: []
bo_homoniemen: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Begroting]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: "Toevoegingen en onttrekkingen aan reserves worden via de begroting vastgesteld"
  - type: associatie
    bedrijfsobject: "[[Jaarrekening]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: "Gerealiseerde mutaties worden verantwoord in de jaarrekening"
  - type: associatie
    bedrijfsobject: "[[Financiële Voorziening]]"
    richting: associatie
    kardinaliteit: "0..*"
    beschrijving: "Reserves en voorzieningen vormen samen het eigen vermogen en de verplichtingen"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/risico|Risico]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een reserve kan een risico afdekken; dekt het risico af, dan telt het niet mee in de risico-inventarisatie voor het weerstandsvermogen"
bedrijfsprocessen: [Begrotingscyclus, Jaarrekening]
bedrijfsfuncties: [Planning en control, Financieel beheer]
---

# Reserve

Eigen vermogen van de gemeente op de balans, onderscheiden in algemene reserve (vrij besteedbaar) en bestemmingsreserves (door de raad geoormerkt).

## BO-criteria toetsing

6/6 criteria: betekenisvol (kernonderdeel balans), herkenbaar (elke gemeente kent reserves), eigen bestaan (onafhankelijk van begroting), meervoud (tientallen reserves per gemeente), levenscyclus (instellen, toevoegen, onttrekken, opheffen), relaties (begroting, jaarrekening, activa).

## Beschrijving

Reserves vormen samen met het gerealiseerde resultaat het eigen vermogen van de gemeente (BBV art. 42). De raad beslist over instelling, toevoegingen en onttrekkingen. Per reserve wordt het verloop (saldo begin, toevoegingen, onttrekkingen, saldo eind) jaarlijks verantwoord (BBV art. 54).

## Specialisaties

Herkende specialisaties van Reserve. Geen apart BO.

- **Algemene reserve** — vrij besteedbaar eigen vermogen, buffer voor financiële tegenvallers
- **Bestemmingsreserve** — reserve waaraan de raad een bepaalde bestemming heeft gegeven (BBV art. 43 lid 2)

## Procesbron

Uit het begrotings- en verantwoordingsproces. De [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/begroting|Begroting]] raamt de toevoegingen en onttrekkingen; de jaarrekening verantwoordt het gerealiseerde verloop.

## Relaties

| Gerelateerd BO | Relatie | Bron |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/begroting\|Begroting]] | Begroting raamt toevoegingen en onttrekkingen | BBV art. 17 lid d |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/jaarrekening\|Jaarrekening]] | Jaarrekening verantwoordt gerealiseerd verloop | BBV art. 27, 54 |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/activa\|Activa]] | Reserves zijn gebonden aan bezittingen op de balans | BBV art. 42 |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/risico\|Risico]] | Een reserve kan een risico afdekken (weerstandscapaciteit) | Nota Weerstandsvermogen en Risicobeheersing |

## Bronnen

- [[Wiki/Bronsamenvattingen/Financien/besluit-begroting-en-verantwoording]]
- [[Wiki/Bronsamenvattingen/Financien/begrippenlijst-gemeentebegroting]]
- [[Wiki/Bronsamenvattingen/Financien/raadgever-financiele-conditie]]

## Terugmelding GGM

Reserve ontbreekt als entiteit in het GGM-beleidsdomein Financien. Het eigen vermogen (reserves + resultaat) is een fundamenteel onderdeel van de gemeentelijke balans. Zie [[Wiki/Analyses/ggm-terugmeldingen]].
