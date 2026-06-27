---
type: bronsamenvatting
titel: Wet basisregistratie ondergrond (Wet BRO)
onderwerp: [Basisregistraties]
datum_ingest: 2026-06-27
---

# Wet basisregistratie ondergrond

## Samenvatting

De Wet BRO (Rijksoverheid, geldend per 4-6-2026) regelt de basisregistratie met gegevens en modellen over de ondergrond van Nederland. De BRO bestaat uit drie componenten: het register brondocumenten ondergrond, de registratie ondergrond en het register inzake meldingen modellen.

De wet definieert vier objecttypen die in de registratie worden opgenomen (art. 19-22):

**[[Verkenning]]** (art. 19) — waarneming van de opbouw van de ondergrond op een punt, langs een lijn of in een vlak. Bevat: identificatiecode, verkenningstype, locatie, tijdstip, bronhouder, meetresultaten. Alle kerngegevens zijn authentiek.

**Gebruiksrecht** (art. 20) — besluit, melding of gegevens gericht op winnen/benutten van natuurlijke hulpbronnen, opslaan van stoffen, bodemkwaliteit of graven boven interventiewaarde. Bevat: identificatiecode, type, locatie, ruimtelijke begrenzing, houder (KvK), voorschriften.

**[[Constructie]]** (art. 21) — werk in de ondergrond voor winnen, opslaan of meten. Bevat: identificatiecode, type, locatie, eigenaar (KvK), kenmerken bestanddelen, meetresultaten.

**Authentiek model** (art. 22) — schematische weergave ondergrond in 2D/3D. Vier typen: geomorfologisch, bodemkundig, geologisch, hydrogeologisch. De Minister is bronhouder, TNO is maker.

**Bronhouderschap** (art. 9): bestuursorganen en drinkwaterbedrijven die bij wettelijke taken brondocumenten ontvangen of genereren over de ondergrond, leveren deze aan via het bronhouderportaal. Aanlevering binnen 20 werkdagen. De bronhouder controleert jaarlijks de eigen uitvoering (art. 9a).

**Gebruiksplicht** (art. 27): bestuursorganen die een authentiek BRO-gegeven nodig hebben voor hun publiekrechtelijke taak, gebruiken dat gegeven. Uitzonderingen: aantekening "in onderzoek", eigen terugmelding, onvoldoende voor taakvervulling.

**Terugmeldplicht** (art. 30): bestuursorganen die gerede twijfel hebben over de juistheid of volledigheid van een authentiek gegeven, melden dit onder opgaaf van redenen. Behandeling binnen 3 werkdagen tot maximaal 16 weken bij nader onderzoek.

## Kernbegrippen

- **[[Verkenning]]** — waarneming van de opbouw van de ondergrond; specialisaties: bodemonderzoek, sondering, grondwaterstandonderzoek, grondwatersamenstellingsonderzoek
- **[[Constructie]]** — werk in de ondergrond; specialisatie: grondwatermonitoringput
- **Gebruiksrecht** — juridisch construct over winnen, opslaan of saneren; specialisatie: grondwateronttrekkingsvergunning, bodemsaneringsmelding
- **Authentiek model** — landelijke 2D/3D weergave ondergrond; TNO is maker, gemeente is geen bronhouder
- **Bronhouder** — bestuursorgaan verantwoordelijk voor aanlevering en kwaliteit van gegevens aan een basisregistratie; gemeente is bronhouder voor BAG, BRP, BRO, WOZ
- **Afnemer** — bestuursorgaan dat authentieke gegevens gebruikt met gebruiksplicht; gemeente is afnemer van BRK, NHR en alle overige basisregistraties
- **Terugmelder** — bestuursorgaan dat gerede twijfel meldt bij bronhouder; wettelijke plicht voor alle bestuursorganen
- **Dataleverancier** — organisatie die namens bronhouder gegevens aanlevert; bij BRO typisch ingenieursbureaus
- **Registratiehouder** — Minister verantwoordelijk voor de basisregistratie (BZK voor BRO)
- **Beheerder** — operationeel beheerder van de registratie (PDOK/TNO voor BRO, Kadaster voor LV BAG/WOZ/BRK)

## Relevantie voor bedrijfsarchitectuur

De Wet BRO definieert drie objecttypen waar de gemeente bronhouder van is: Verkenning, Constructie en Gebruiksrecht. Deze zijn niet in het GGM gemodelleerd (hiaat). De wet legt ook het rollenmodel vast dat voor alle basisregistraties geldt: bronhouder, afnemer, terugmelder. Dit rollenmodel is cross-cutting en hoort in het onderwerpoverzicht Basisregistraties.

> "Een bestuursorgaan dat bij de vervulling van zijn publiekrechtelijke taak een gegeven nodig heeft dat krachtens deze wet als authentiek gegeven in de registratie ondergrond beschikbaar is, gebruikt dat authentieke gegeven." (art. 27 lid 1)

## Bronnen
- [[Sources/Standaarden/wet-bro-bwbr0037095]]
