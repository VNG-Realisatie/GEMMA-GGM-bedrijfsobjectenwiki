---
type: bronsamenvatting
titel: "Wet studiefinanciering 2000 (WSF 2000)"
onderwerp: [werk en inkomen]
datum_ingest: 2026-07-07
---

## Samenvatting

De Wet studiefinanciering 2000 regelt de financiële ondersteuning van studenten in het beroepsonderwijs (mbo) en hoger onderwijs (hbo/wo) door DUO namens de Minister van Onderwijs, Cultuur en Wetenschap. Hoofdstuk 1 (Algemene bepalingen) definieert de kernbegrippen: **studiefinanciering** is "door Onze Minister verstrekte toekenning in verband met het volgen van een opleiding [...] waarop uitsluitend op grond van deze wet aanspraak bestaat" (art. 1.1) — nadrukkelijk een rijksregeling, geen gemeentelijke. Hoofdstuk 2 (Werkingssfeer) bepaalt wie in aanmerking komt: nationaliteit (art. 2.2), leeftijd (art. 2.3: vanaf 18 jaar tot en met 30 jaar) en onderwijssoort.

Hoofdstuk 3 beschrijft de vormen van studiefinanciering (art. 3.1): voor mbo bestaat het uit basisbeurs, basislening en aanvullende beurs/lening; voor hoger onderwijs uit basisbeurs, basislening, aanvullende beurs/lening én collegegeldkrediet; ontbreekt aanspraak op deze reguliere vormen, dan resteert levenlanglerenkrediet. Elke vorm kan geheel of gedeeltelijk worden toegekend als gift, prestatiebeurs (voorwaardelijke lening die onder voorwaarden in gift wordt omgezet) of lening. De reisvoorziening (art. 3.7) geeft recht op gereduceerd of gratis reizen. Toekenning gebeurt op aanvraag (art. 3.19), per studiefinancieringstijdvak (art. 3.21), met een beslistermijn van 8 weken (of eerder bij tijdige aanvraag voor het kalenderjaar).

## Kernbegrippen

- **Studiefinanciering** — de toekenning zelf: door DUO/de Minister verstrekt, niet door de gemeente. Bestaat uit basisbeurs, lening(en), eventueel collegegeldkrediet/levenlanglerenkrediet en reisvoorziening (art. 3.1). GGM: `Studiefinanciering`, herclassificeerd als `component`-subtype van Primair inkomstencomponent (Sociaal Domein Generiek) — zelfde patroon als Uitkering/Pensioen: de gemeente registreert dit alleen als inkomstenfeit van een cliënt, niet als eigen toekenningsproces.
- **Basisbeurs / basislening / aanvullende beurs / aanvullende lening** — de kernvormen (art. 3.6, 3.8, 3.15, 3.16); hoogte afhankelijk van uit-/thuiswonend en (voor aanvullende beurs) de veronderstelde ouderlijke bijdrage.
- **Prestatiebeurs** — voorwaardelijke lening die bij voldoende studieresultaat wordt omgezet in een gift (art. 1.1 definitie).
- **Collegegeldkrediet / levenlanglerenkrediet** — leningen specifiek voor resp. collegegeld (ho) en lesgeld/collegegeld buiten de reguliere studiefinancieringsperiode.
- **Reisvoorziening/reisrecht/reisproduct** — het reisrecht en de vormgeving daarvan (art. 3.7, 3.24-3.30 — niet in het uittreksel opgenomen).
- **Toekenning** — het besluit van Onze Minister op een aanvraag (art. 3.19); geen gemeentelijke bevoegdheid.

## Relevantie voor bedrijfsarchitectuur

1. **Hiaat opgelost via herclassificatie:** `Studiefinanciering` (GGM, Sociaal Domein Generiek) stond op `detail`/⚠️ "geen BO bereikbaar". Deze bron bevestigt dat het gemeentelijk perspectief hier hetzelfde is als bij Uitkering/Pensioen/Alimentatie: de gemeente registreert alleen dát een cliënt studiefinanciering ontvangt (relevant voor bijstand-/vermogenstoets), niet de toekenning zelf (die is DUO's proces). Herclassificatie naar `component`, route via Primair inkomstencomponent → [[Client]]. Zie [[Wiki/Analyses/entiteitendekking/6-sociaal-domein]].
2. **Geen BO-kandidaat:** het toekenningsproces zelf (aanvraag, beoordeling, uitbetaling door DUO) valt buiten het gemeentelijk perspectief — conform de regel dat de wiki beschrijft wat de gemeente zelf ziet/doet/registreert.
3. **Cross-link met Inkomen:** GGM's `Gestopte studiefinanciering` (beleidsdomein Inkomen, Reden-aanvraagsubtype) is de beëindigingsgebeurtenis van precies dit inkomstencomponent — nu expliciet gekoppeld in de entiteitendekking-analyse.

## Citaten

> "studiefinanciering: door Onze Minister verstrekte toekenning in verband met het volgen van een opleiding in het beroepsonderwijs of in het hoger onderwijs waarop uitsluitend op grond van deze wet aanspraak bestaat" (art. 1.1, WSF 2000)

> "Studiefinanciering bestaat voor een opleiding in het beroepsonderwijs uit een basisbeurs, een basislening en een aanvullende beurs of aanvullende lening, en kan geheel of gedeeltelijk worden toegekend in de vorm van: a. een gift; b. een prestatiebeurs; of c. een lening." (art. 3.1 lid 1, WSF 2000)

> "Onze Minister kent studiefinanciering toe aan degene die daartoe een aanvraag heeft ingediend en die voldoet aan de voorschriften gegeven bij of krachtens deze wet." (art. 3.19 lid 1, WSF 2000)

## Bronnen

- [[Sources/Onderwerpen/Werk en Inkomen/wet-studiefinanciering-2000-bwbr0011453]]
