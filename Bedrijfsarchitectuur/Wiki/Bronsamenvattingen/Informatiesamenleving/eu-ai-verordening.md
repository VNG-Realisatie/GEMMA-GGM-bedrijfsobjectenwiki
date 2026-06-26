---
type: bronsamenvatting
titel: "Verordening (EU) 2024/1689 — AI-verordening (selectie)"
onderwerp: [Informatiesamenleving]
datum_ingest: 2026-06-26
---

# Verordening (EU) 2024/1689 — AI-verordening

Selectie van de gemeenterelevante artikelen uit de EU AI-verordening (Verordening 2024/1689, gepubliceerd 12 juli 2024). De volledige verordening bevat 113 artikelen en 13 bijlagen; deze samenvatting focust op definities (art. 3), verboden (art. 5), verplichtingen voor gebruiksverantwoordelijken (art. 26), grondrechtenbeoordeling (art. 27) en de hoog-risico lijst (bijlage III).

## Samenvatting

### Definities (art. 3)

De verordening definieert 68 begrippen. Gemeenterelevant:

- **AI-systeem** (lid 1): "een op een machine gebaseerd systeem dat is ontworpen om met verschillende niveaus van autonomie te werken en dat na het inzetten ervan aanpassingsvermogen kan vertonen, en dat [...] uit de ontvangen input afleidt hoe output te genereren zoals voorspellingen, inhoud, aanbevelingen of beslissingen."
- **Gebruiksverantwoordelijke** (lid 4): "een natuurlijke of rechtspersoon, overheidsinstantie, agentschap of ander orgaan die/dat een AI-systeem onder eigen verantwoordelijkheid gebruikt."
- **Aanbieder** (lid 3): "een natuurlijke of rechtspersoon [...] die/dat een AI-systeem [...] ontwikkelt of laat ontwikkelen en dat systeem [...] in de handel brengt."
- **Ernstig incident** (lid 49): incident of gebrekkig functioneren van een AI-systeem dat direct of indirect leidt tot: a) overlijden of ernstige gezondheidsschade; b) ernstige verstoring kritieke infrastructuur; c) schending van grondrechten; d) ernstige schade aan eigendommen of milieu.
- **AI-geletterdheid** (lid 56): "vaardigheden, kennis en begrip die aanbieders, gebruiksverantwoordelijken en betrokken personen [...] in staat stellen geïnformeerd AI-systemen in te zetten."

### Verboden AI-praktijken (art. 5)

Acht categorieën verboden AI:
a) subliminale/manipulatieve technieken
b) uitbuiting van kwetsbaarheden
c) social scoring
d) risicobeoordeling strafbare feiten op basis van profilering
e) ongerichte scraping gezichtsherkenningsdatabanken
f) emotieherkenning op werkplek/in onderwijs
g) biometrische categorisering op gevoelige kenmerken
h) biometrische identificatie op afstand in real time (met uitzonderingen voor rechtshandhaving)

### Verplichtingen gebruiksverantwoordelijken (art. 26)

Twaalf leden met verplichtingen voor gebruiksverantwoordelijken van hoog-risico AI:
1. Gebruik conform gebruiksaanwijzingen
2. Menselijk toezicht door bekwame personen
3. Organisatievrijheid bij uitvoering toezicht
4. Inputdata relevant en representatief houden
5. Monitoren werking, melden incidenten aan aanbieder en markttoezichtautoriteit
6. Logs bewaren (min. 6 maanden)
7. Werknemers informeren over AI-gebruik
8. **Overheidsinstanties**: registratieverplichtingen naleven (art. 49); niet-geregistreerde systemen niet gebruiken
9. DPIA-informatie van aanbieder gebruiken voor gegevensbeschermingseffectbeoordeling (AVG art. 35)
10. Biometrische identificatie: voorafgaande toestemming rechterlijke instantie
11. Natuurlijke personen informeren dat AI op hen wordt toegepast
12. Samenwerking met bevoegde autoriteiten

### Grondrechteneffectbeoordeling (art. 27)

**Verplicht voor publiekrechtelijke organen** en particuliere entiteiten die openbare diensten verlenen, vóór ingebruikname van hoog-risico AI (art. 6 lid 2). De beoordeling bestaat uit zes elementen:

a) beschrijving van de processen waarbij het AI-systeem wordt gebruikt
b) periode en frequentie van gebruik
c) categorieën personen die gevolgen ondervinden
d) specifieke risico's op schade voor die personen
e) uitvoering van menselijk toezicht
f) maatregelen bij het voordoen van risico's, inclusief interne governance en klachtenregelingen

Aanvullende bepalingen:
- Hergebruik van eerdere beoordelingen mogelijk bij soortgelijke gevallen (lid 2)
- Resultaten melden aan markttoezichtautoriteit (lid 3)
- Aanvulling op DPIA (AVG art. 35), geen vervanging (lid 4)
- AI-bureau ontwikkelt sjabloon/vragenlijst, eventueel geautomatiseerd (lid 5)

### Hoog-risico AI-systemen (bijlage III)

Acht categorieën, waarvan gemeenterelevant:
1. **Biometrie**: identificatie op afstand, categorisering, emotieherkenning
2. **Kritieke infrastructuur**: veiligheidscomponenten bij verkeer, water, gas, elektriciteit
3. **Onderwijs**: toelating, evaluatie leerresultaten, onderwijsniveau-beoordeling, monitoring gedrag studenten
4. **Werkgelegenheid**: werving/selectie, arbeidsbeslissingen, prestatiemonitoring
5. **Publieke diensten en uitkeringen**: beoordeling aanspraken op overheidsuitkeringen/-diensten; kredietwaardigheid; verzekeringen; noodoproepen/triage
6. **Rechtshandhaving**: slachtofferrisico, leugendetectie, bewijsbeoordeling, recidiverisico, profilering
7. **Migratie en asiel**: risicobeoordeling, asielaanvragen, identificatie
8. **Rechtsbedeling en democratie**: ondersteuning rechtspraak, beïnvloeding verkiezingen

## Kernbegrippen

- **Grondrechteneffectbeoordeling** — verplichte beoordeling door overheden vóór inzet hoog-risico AI, met 6 verplichte elementen. Eigen levenscyclus (uitvoeren → melden → actualiseren). Verwant aan maar aanvullend op [[DPIA]].
- **Ernstig incident** — incident door AI-systeem met ernstige gevolgen (overlijden, grondrechtenschending, milieuschade). Meldplicht aan aanbieder en markttoezichtautoriteit.
- **Hoog-risico AI-systeem** — AI-systeem dat valt onder bijlage III of art. 6. Bepalend voor welke verplichtingen gelden.

## Relevantie voor bedrijfsarchitectuur

Deze bron levert de wettelijke grondslag voor twee potentiële BO's:

1. **Grondrechteneffectbeoordeling** — art. 27 definieert 6 verplichte elementen, waarmee het concreet genoeg is om de 6 BO-criteria te toetsen. Het heeft eigen attributen (proces, frequentie, categorieën, risico's, toezicht, maatregelen), een levenscyclus (uitvoeren → melden → actualiseren) en relaties (met AI-systeem, met DPIA).

2. **Ernstig incident** — nieuw begrip met meldplicht. Verwant aan datalek (AVG) maar specifiek voor AI-systemen. Potentieel BO bij rijkere bronnen die het meldingsproces beschrijven.

De hoog-risico categorieën in bijlage III raken direct aan gemeentelijke domeinen: publieke diensten en uitkeringen (punt 5a), onderwijs (punt 3), werkgelegenheid (punt 4).

## Citaten

> "een op een machine gebaseerd systeem dat is ontworpen om met verschillende niveaus van autonomie te werken en dat na het inzetten ervan aanpassingsvermogen kan vertonen" (art. 3 lid 1)

> "gebruiksverantwoordelijken die publiekrechtelijke organen zijn of particuliere entiteiten zijn die openbare diensten verlenen [...] voeren een beoordeling uit van de gevolgen voor de grondrechten die het gebruik van een dergelijk systeem kan opleveren" (art. 27 lid 1)

> "Het AI-bureau ontwikkelt een sjabloon voor een vragenlijst, onder meer via een geautomatiseerd instrument, om gebruiksverantwoordelijken te helpen hun verplichtingen uit hoofde van dit artikel op vereenvoudigde wijze na te komen." (art. 27 lid 5)

> "AI-systemen die bedoeld zijn om door of namens overheidsinstanties te worden gebruikt om te beoordelen of natuurlijke personen in aanmerking komen voor essentiële overheidsuitkeringen en -diensten" (bijlage III punt 5a)

## Bronnen
- [[Sources/Onderwerpen/Informatiesamenleving/eu-ai-verordening-2024-1689]]
