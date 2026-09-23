---
type: element
naam: Financiële Voorziening
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
bo_definitie: "Verplichting of risico op de balans waarvan de omvang onzeker is maar redelijkerwijs te schatten, gevormd conform BBV art. 44."
bo_toelichting: "Voorzieningen worden gevormd voor vier grondslagen: onzekere verplichtingen/verliezen, bestaande risico's, egalisatie van lasten, en vervangingsinvesteringen bij heffingen."
bo_subtypes: []
bo_synoniemen: []
bo_homoniemen: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Begroting]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: "Dotaties aan voorzieningen worden begroot"
  - type: associatie
    bedrijfsobject: "[[Jaarrekening]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: "Verloop wordt verantwoord in de jaarrekening"
  - type: associatie
    bedrijfsobject: "[[Reserve]]"
    richting: associatie
    kardinaliteit: "0..*"
    beschrijving: "Reserves en voorzieningen vormen samen het eigen vermogen en de verplichtingen"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/risico|Risico]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een voorziening kan een risico afdekken (grondslag 'bestaande risico's', BBV art. 44 lid 1 onder 2)"
bedrijfsprocessen: [Begrotingscyclus, Jaarrekening]
bedrijfsfuncties: [Planning en control, Financieel beheer]
---

# Financiële Voorziening

Verplichting of risico op de balans waarvan de omvang onzeker is maar redelijkerwijs te schatten, gevormd conform BBV art. 44.

## BO-criteria toetsing

6/6 criteria: betekenisvol (verplicht balansonderdeel), herkenbaar (elke gemeente heeft voorzieningen), eigen bestaan (onafhankelijk van begroting), meervoud (meerdere per gemeente), levenscyclus (vorming, dotatie, aanwending, vrijval), relaties (begroting, jaarrekening, reserves).

## Naamkeuze

De BBV-term is "voorziening", maar die naam is een homoniem — in het GGM-beleidsdomein Generiek Jeugd en Wmo verwijst [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/voorziening|Voorziening]] naar een middel voor ondersteuning/hulp. Dit BO heet **Financiële Voorziening**.

**Overwogen namen:**
- **Financiële Voorziening** — duidelijk onderscheid met Wmo-voorziening, sluit aan bij "financieel domein"
- Balansvoorziening — te technisch, niet gangbaar in gemeentelijke praktijk
- BBV-voorziening — te specifiek naar het besluit

## Beschrijving

Gemeenten vormen voorzieningen op grond van vier grondslagen (BBV art. 44 lid 1):
1. Verplichtingen en verliezen waarvan de omvang onzeker is
2. Bestaande risico's voor te verwachten verplichtingen/verliezen
3. Egalisatie van lasten over meerdere begrotingsjaren
4. Bijdragen aan toekomstige vervangingsinvesteringen bij heffingen

Per voorziening wordt het verloop (saldo begin, toevoegingen, vrijval, aanwendingen, saldo eind) jaarlijks verantwoord (BBV art. 55). Rentetoevoegingen zijn niet toegestaan (art. 45).

## Procesbron

Uit het begrotings- en verantwoordingsproces. Dotaties worden begroot; het verloop wordt verantwoord in de jaarrekening.

## Relaties

| Gerelateerd BO | Relatie | Bron |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/begroting\|Begroting]] | Dotaties worden begroot | BBV art. 44 |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/jaarrekening\|Jaarrekening]] | Verloop wordt verantwoord | BBV art. 55 |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/reserve\|Reserve]] | Samen vormen ze het eigen vermogen en verplichtingen | BBV art. 41-44 |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/risico\|Risico]] | Een voorziening kan een risico afdekken | Nota Weerstandsvermogen en Risicobeheersing |

## Bronnen

- [[Wiki/Bronsamenvattingen/Financien/besluit-begroting-en-verantwoording]]
- [[Wiki/Bronsamenvattingen/Financien/begrippenlijst-gemeentebegroting]]

## Terugmelding GGM

Financiële voorziening (BBV art. 44) ontbreekt als entiteit in het GGM-beleidsdomein Financien. Past in het balansmodel naast Activa en Reserves. Zie [[Wiki/Analyses/ggm-terugmeldingen]].
