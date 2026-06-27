---
type: bronsamenvatting
titel: BRO Catalogus Grondwaterstandonderzoek (GLD)
onderwerp: [Basisregistraties]
datum_ingest: 2026-06-27
---

# BRO Catalogus Grondwaterstandonderzoek (GLD)

## Samenvatting

De BRO-catalogus GLD (Geonovum, juni 2023) beschrijft het registratieobject Grondwaterstandonderzoek in detail. Een GLD bevat beoordeelde tijd-meetwaardereeksen van waterstand in meter NAP voor één filter van een grondwatermonitoringput.

Het grondwaterdomein in de BRO omvat vier registratieobjecten die samen het monitoringsysteem vormen:
- **Grondwatermonitoringnet (GMN)** — verzameling locaties onder een monitoringdoel → specialisatie van logisch netwerk
- **Grondwatermonitoringput (GMW)** — fysieke constructie met buizen en filters → specialisatie van [[Constructie]]
- **Grondwaterstandonderzoek (GLD)** — monitoring grondwaterkwantiteit → specialisatie van [[Verkenning]]
- **Grondwatersamenstellingsonderzoek (GAR)** — monitoring grondwaterkwaliteit → specialisatie van [[Verkenning]]

Het GLD-proces omvat vijf stappen: meten, omrekenen, controleren, corrigeren, keuren. Meetwaarden worden aangeleverd als observaties met tijdmeetwaardereeksen. Elk tijdmeetwaardepaar heeft een kwaliteitsstatus (goedgekeurd, niet goedgekeurd, nog niet beoordeeld).

Twee kwaliteitsregimes: IMBRO (strikt, na inwerkingtreding wet) en IMBRO/A (versoepeld, historische data).

## Kernbegrippen

- **Grondwatermonitoringput (GMW)** — fysieke constructie in de ondergrond met buizen en filters; gemeente is bronhouder; specialisatie van [[Constructie]]
- **Grondwatermonitoringnet (GMN)** — logische groepering van meetpunten onder een monitoringdoel; gemeente beheert
- **Grondwaterstandonderzoek (GLD)** — registratieobject met meetreeksen waterstand; specialisatie van [[Verkenning]]
- **Observatie** — geheel van meetactiviteiten in een bepaalde periode; component van GLD
- **Tijdmeetwaardereeks** — chronologische reeks tijdstip-waterstand paren; component van Observatie
- **Kwaliteitsregime** — IMBRO (strikt) of IMBRO/A (historische data met vrijstellingen)

## Relevantie voor bedrijfsarchitectuur

De catalogus toont hoe de wettelijke objecttypen [[Verkenning]] en [[Constructie]] concreet worden ingevuld voor het grondwaterdomein. GMW is een specialisatie van Constructie, GLD en GAR zijn specialisaties van Verkenning. De gemeente is bronhouder en besteedt de uitvoering uit aan leveranciers (dataleverancier).

Het grondwaterdomein illustreert het patroon dat voor alle BRO-domeinen geldt: fysieke objecten (putten, boringen) → meetactiviteiten (observaties) → geregistreerde resultaten (meetreeksen).

## Bronnen
- [[Sources/Standaarden/catalogus-bro-gld]]
