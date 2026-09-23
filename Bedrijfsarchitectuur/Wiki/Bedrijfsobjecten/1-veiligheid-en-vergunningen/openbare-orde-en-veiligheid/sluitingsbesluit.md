---
type: element
naam: Sluitingsbesluit
onderwerp: [Openbare Orde en Veiligheid]
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

bo_definitie: "Besluit van de burgemeester om een woning, niet voor publiek toegankelijk lokaal, publiek toegankelijk gebouw of bijbehorend erf voor een bepaalde duur te sluiten wegens ernstige verstoring van de openbare orde (art. 174/174a Gemeentewet, art. 13b Opiumwet)."
bo_toelichting: "Conceptueel verwant aan het VTH-specifieke Handhavingsbesluit (sanctie bij een geconstateerde overtreding, door het college), maar met een andere bevoegde actor (de burgemeester, als hoeder van de openbare orde) en een andere rechtsgrondslag (Gemeentewet/Opiumwet i.p.v. VTH-regelgeving) — daarom als zelfstandig BO vastgelegd."
bo_subtypes:
  - naam: "Sluiting woning/lokaal/erf bij verstoring openbare orde"
    omschrijving: "Sluiting bij ernstige verstoring van de openbare orde door gedragingen, geweld of aangetroffen wapens (art. 174a Gemeentewet, 'Wet Victoria')."
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: "Sluiting bij drugshandel"
    omschrijving: "Sluiting van een woning, lokaal of erf bij het aantreffen van drugs of voorwerpen/stoffen bestemd voor drugsbereiding (art. 13b Opiumwet, 'Wet Damocles')."
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: "Sluiting publiek toegankelijk gebouw"
    omschrijving: "Sluiting van voor het publiek openstaande gebouwen en erven bij verstoring van de openbare orde in de uitoefening van het algemene toezicht (art. 174 Gemeentewet)."
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
bo_relaties: []
bedrijfsprocessen: [Bestuurlijke sluiting]
bedrijfsfuncties: [Openbare orde en veiligheid, Aanpak ondermijning]
---

# Sluitingsbesluit

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Identificeerbaar | Ja — elk sluitingsbesluit betreft een specifiek pand/woning/erf met een eigen dossier |
| Eigen attributen | Ja — sluitingsgrond, duur, betrokken pand/adres, eventuele verlenging, hersteltermijn voor belanghebbenden |
| Levenscyclus | Ja — signalen/constatering → besluit (met bekendmaking en hersteltermijn, tenzij spoedeisend) → sluiting → eventuele verlenging → opheffing |
| Gemeentelijk eigendom | Ja — de burgemeester neemt het besluit als bevoegd gezag voor de openbare orde |
| Wettelijke grondslag | Ja — Gemeentewet art. 174 en 174a, Opiumwet art. 13b |
| Registratieverplichting | Ja — schriftelijk besluit met sluitingsduur, bekendgemaakt aan belanghebbenden |

Score: 6/6 criteria.

## Beschrijving

Een sluitingsbesluit is het besluit van de burgemeester om een woning, een niet voor het publiek toegankelijk lokaal, een publiek toegankelijk gebouw of een daarbij behorend erf (tijdelijk) te sluiten, ter bescherming van de openbare orde. De belangrijkste grondslag is artikel 174a Gemeentewet ("Wet Victoria"): sluiting bij ernstige verstoring van de openbare orde door gedragingen in de woning of het lokaal, door ernstig geweld of de dreiging daarmee, of door het aantreffen van een wapen. De burgemeester bepaalt de duur van de sluiting in het besluit en kan deze bij herhalingsgevaar verlengen. Bij de bekendmaking krijgen belanghebbenden in beginsel eerst de gelegenheid maatregelen te treffen om de verstoring te beëindigen, tenzij voorafgaande bekendmaking in spoedeisende gevallen niet mogelijk is.

Een tweede, veelgebruikte grondslag is artikel 13b Opiumwet ("Wet Damocles"): sluiting bij het aantreffen van drugs of bij drugshandel vanuit een pand, zonder dat afzonderlijk een verstoring van de openbare orde hoeft te worden aangetoond — de aanwezigheid van een handelshoeveelheid volstaat. Daarnaast kan de burgemeester op grond van het algemene toezicht (art. 174 Gemeentewet) ook publiek toegankelijke gebouwen sluiten. De VNG-menukaart bestuurlijke interventies ondermijning noemt sluiting als instrument bij onder meer horeca-inrichtingen, coffeeshops, growshops en woningen met overlast.

## Procesbron

Het sluitingsbesluit ontstaat in het proces van bestuurlijke handhaving van de openbare orde door de burgemeester, doorgaans na signalen van politie, boa's of andere gemeentelijke diensten. Zie [[Wiki/Bronsamenvattingen/Bestuur/gemeentewet-wettekst|Gemeentewet — wettekst]], art. 174 en 174a, en de "Menukaart bestuurlijke interventies ondermijning" in [[Wiki/Bronsamenvattingen/Openbare Orde en Veiligheid/handreiking-apv-en-ondermijning|Handreiking APV en ondermijning]] (items 25-28, 32-35).

## Bedrijfsprocessen

- **Bestuurlijke sluiting** — signalering, besluitvorming (incl. hersteltermijn), bekendmaking, uitvoering, eventuele verlenging, opheffing

## Bronnen
- [[Wiki/Bronsamenvattingen/Bestuur/gemeentewet-wettekst]]
- [[Wiki/Bronsamenvattingen/Openbare Orde en Veiligheid/handreiking-apv-en-ondermijning]]

## Terugmelding GGM

GGM-hiaat: bestuursrechtelijk sluitingsinstrument zonder GGM-tegenhanger, wettelijk kernonderdeel van de gemeentelijke aanpak van ondermijning en overlast. Conceptueel verwant aan het VTH-specifieke [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/handhavingsbesluit|Handhavingsbesluit]] (beide zijn sanctiebesluiten), maar met afwijkende bevoegde actor (burgemeester i.p.v. college) en rechtsgrondslag (openbare-ordebevoegdheid i.p.v. VTH-regelgeving); daarom hier als zelfstandig BO vastgelegd, geen generalisatie-relatie.
