---
type: element
naam: Frauderisicoanalyse
onderwerp: [Risicobeheer, Financien]
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

bo_definitie: "Jaarlijkse specificatie van de frauderisico-inventarisatie: een kans-maal-impactbeoordeling van interne fraudegevoelige processen, die bepaalt welke processen bijzondere aandacht krijgen in het verbijzonderde interne controleplan."
bo_toelichting: "Onderdeel van de financiële rechtmatigheidsverantwoording van het college (sinds 1 januari 2023, misbruik- en oneigenlijk-gebruikcriterium). Gebaseerd op de fraudedriehoek (gelegenheid × druk × rationalisatie) uit de COS 240-definitie van fraude. Te onderscheiden van misbruik: fraude is intern gericht (bestuur, college, ambtenaren), misbruik extern (inwoners, ondernemingen)."
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/weerstandsvermogen-en-risicobeheersing|Weerstandsvermogen en risicobeheersing]]"
    richting: bidirectioneel
    kardinaliteit: "1 → 1"
    beschrijving: "Beide onderdeel van de jaarlijkse rechtmatigheids-/risicoverantwoording, met een vergelijkbaar governance-patroon"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/fraudeonderzoek|Fraudeonderzoek]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Uitkomsten van een fraudeonderzoek scherpen de frauderisicoanalyse aan"
bedrijfsprocessen: [Risicomanagement, Verbijzonderde interne controle]
bedrijfsfuncties: [Financieel beheer, Risicobeheer]
---

# Frauderisicoanalyse

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Identificeerbaar | Ja — jaarlijkse, geactualiseerde beoordeling met een eigen vaststellingsmoment |
| Eigen attributen | Ja — geïnventariseerde fraudegevoelige processen (60+, per beleidsterrein), kansinschatting, financiële/niet-financiële impact, prioritering |
| Levenscyclus | Ja — inventarisatie fraudegevoelige processen → kans×impact-specificatie → prioritering → opname in verbijzonderd interne controleplan → jaarlijkse actualisatie |
| Gemeentelijk eigendom | Ja — het college is sinds 2023 verantwoordelijk voor de rechtmatigheidsverantwoording waar dit onderdeel van is |
| Wettelijke grondslag | Ja — indirect via art. 213 Gemeentewet en het misbruik- en oneigenlijk-gebruikcriterium van de rechtmatigheidsverantwoording; zelf een beleidsinstrument, geen wettelijk voorgeschreven vorm |
| Registratieverplichting | Ja — vastgelegd als afzonderlijk document, gekoppeld aan het jaarlijkse interne controleplan |

Score: 6/6 criteria.

## Beschrijving

Vóór 2023 voerde de accountant een aanvullende toets op de financiële rechtmatigheid van de jaarrekening uit; sinds 1 januari 2023 valt deze toets onder de verantwoordelijkheid van het college zelf, met drie criteria: het begrotingscriterium, het voorwaardencriterium en het misbruik- en oneigenlijk-gebruikcriterium. De frauderisicoanalyse onderbouwt dit laatste criterium voor het interne (fraude-)deel.

De analyse bestaat uit twee stappen. Eerst een **inventarisatie van de frauderisico-gevoeligheid**: welke activiteiten en processen lopen risico op fraude, beoordeeld met de fraudedriehoek (gelegenheid × druk × rationalisatie — hoe minder beheersmaatregelen, hoe hoger de gevoeligheid). Deze inventarisatie beslaat doorgaans tientallen processen, verspreid over beleidsterreinen als bestuur, treasury, administratie/verslaglegging, belastingen, personeel & organisatie, inkoop en aanbesteding, grondbedrijf & beheer, en burgerzaken/vergunningverlening.

Vervolgens wordt per risicogevoelig proces een **frauderisico-analyse (en impactbepaling)** gemaakt: een inschatting van de kans op fraude en de bijbehorende financiële en/of niet-financiële impact. Op basis van kans × impact wordt bepaald welke processen bijzondere aandacht krijgen. De uitkomst wordt jaarlijks geactualiseerd en opgenomen in het verbijzonderde interne controleplan, zodat er geen dubbele controles naast de reguliere procesgang ontstaan.

Fraude wordt hierbij nadrukkelijk onderscheiden van misbruik: **misbruik** is extern gericht (een inwoner of onderneming die opzettelijk onjuiste gegevens verstrekt om ten onrechte een uitkering of lagere heffing te krijgen), **fraude** is intern gericht (een opzettelijke, misleidende handeling door raadsleden, collegeleden of ambtenaren voor onrechtmatig voordeel — COS 240-definitie).

## Juridische bron

Geen directe wettelijke vormvoorschriften; indirecte grondslag via art. 213 Gemeentewet (accountantscontrole jaarrekening) en de rechtmatigheidsverantwoording van het college sinds 1 januari 2023 (misbruik- en oneigenlijk-gebruikcriterium), gebaseerd op de BBV-definitie van fraude en de COS 240-standaard. Zie [[Wiki/Bronsamenvattingen/Risicobeheer/fraudebeleid-en-frauderisicoanalyse-brummen|Fraudebeleid en Frauderisicoanalyse Gemeente Brummen]].

## Relaties

| Relatie | Bedrijfsobject | Richting | Beschrijving |
|---|---|---|---|
| associatie | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/weerstandsvermogen-en-risicobeheersing\|Weerstandsvermogen en risicobeheersing]] | ↔ | Beide onderdeel van de jaarlijkse rechtmatigheids-/risicoverantwoording |
| associatie | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/fraudeonderzoek\|Fraudeonderzoek]] | ← | Onderzoeksuitkomsten scherpen de analyse aan |

## Bedrijfsprocessen

- **Risicomanagement** — identificeren, kwantificeren en beheersen van (fraude)risico's
- **Verbijzonderde interne controle** — jaarlijkse opname van de frauderisico-analyse in het interne controleplan

## Bronnen
- [[Wiki/Bronsamenvattingen/Risicobeheer/fraudebeleid-en-frauderisicoanalyse-brummen]]

## Terugmelding GGM

GGM-hiaat: geen entiteit voor de frauderisicoanalyse. Enige fraude-gerelateerde GGM-entiteit is WoonfraudeAanvraagOfMelding (taakveld 1, Veiligheid en Vergunningen) — een ander concept: externe fraude door bewoners (bijv. illegale onderverhuur), niet de interne, bestuurs-/ambtenarengerichte fraude waar dit BO over gaat. Geen homoniem of duplicaat, wel vermeldenswaardig ter afbakening.
