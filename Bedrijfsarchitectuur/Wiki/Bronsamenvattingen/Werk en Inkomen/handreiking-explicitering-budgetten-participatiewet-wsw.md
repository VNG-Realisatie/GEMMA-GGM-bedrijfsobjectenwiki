---
type: bronsamenvatting
titel: Handreiking Explicitering budgetten Participatiewet en Wsw
onderwerp: [werk en inkomen]
datum_ingest: 2026-06-25
---

# Handreiking Explicitering budgetten Participatiewet en Wsw

Handreiking van Berenschot (april 2025), in opdracht van Cedris, Divosa, VNG en het ministerie van SZW. Beschrijft de financieringssystematiek van de Participatiewet en de Wsw: hoe de rijksmiddelen worden berekend, verdeeld over gemeenten en hoe gemeentelijk beleid doorwerkt in de budgetten.

## Samenvatting

Gemeenten ontvangen via drie kanalen financiële middelen voor de uitvoering van de Participatiewet en de Wsw (totaal circa €13,4 mld in 2024):

1. **Bijstandsbudget (BUIG)** — €7,3 mld. Budget voor bijstandsuitkeringen en loonkostensubsidies. Verdeling afhankelijk van gemeentegrootte: objectief (>40.000 inwoners), historisch (<15.000 inwoners), of een mix. Het budget is gebudgetteerd: gemeenten ontvangen een vast budget, niet een vergoeding van werkelijke uitgaven. Overschotten zijn vrij besteedbaar; tekorten moeten uit eigen middelen worden aangevuld. Vangnetregeling boven 7,5% tekort.

2. **Cluster Participatie in de algemene uitkering gemeentefonds** — €4,0 mld. Fictief budget voor uitvoering, re-integratie, begeleiding en minimabeleid. Berekend via vier maatstaven: bijstandsontvangers (driejarig gemiddelde), loonkostensubsidies, huishoudens met laag inkomen, en doelgroepenregister. Basisbedrag per eenheid × uitkeringsfactor (1,42 in 2024). Per extra [[Loonkostensubsidie]] ontvangt de gemeente €7.355 in het gemeentefonds.

3. **Integratie-uitkering Participatie** — €2,1 mld. Twee deelbudgetten: Wsw (krimpend, meerjarig gefixeerd macrobudget, verdeling op basis van gerealiseerd aantal SE's + blijfkans) en beschut werk (groeiend, taakstelling per gemeente, €11.296 per werkplek). Daarnaast: infrastructurele opslag (vanaf 2025, oplopend tot €35,9 mln structureel) en impulsbudget (10 jaar, €35 mln in 2025, via decentralisatie-uitkering).

De handreiking beschrijft per financieringskanaal gedetailleerd de doorwerking van gemeentelijk beleid via scenario's: uitstroom uit bijstand, inzet van loonkostensubsidie, doorstroom naar regulier werk, en "niets doen". De conclusie: het loont financieel voor grotere gemeenten om via re-integratie en loonkostensubsidies de bijstandsafhankelijkheid te verlagen. Voor kleinere gemeenten (historische verdeling) werken besparingen met vertraging door in een lager budget.

## Kernbegrippen

- **[[Loonkostensubsidie]]** — tegemoetkoming aan werkgever voor het verschil tussen loonwaarde en minimumloon bij werknemer met beperkte loonwaarde (Participatiewet). Budget historisch verdeeld (realisatie t-1), volledig gecompenseerd met één jaar vertraging.
- **[[Re-integratievoorziening]]** — voorziening gericht op het ontwikkelen en aan het werk helpen van werkzoekenden: scholing, werkervaring, bemiddeling, jobcoaching. Gefinancierd uit cluster Participatie.
- **[[Inkomensvoorziening]]** — bijstandsuitkering als subtype; gefinancierd uit het bijstandsbudget (BUIG).
- **Beschutte werkplek** — werkplek in aangepaste omstandigheden voor inwoners met indicatie beschut werk (UWV). Taakstelling per gemeente (ministeriële regeling); financiering via drie kanalen (LKS + IU Participatie + cluster Participatie). Verwachte groei: 3 Wsw'ers eruit → 1 beschut werker erin.
- **Doelgroepenregister** — landelijk register (UWV) van personen met arbeidsbeperking onder de banenafspraak. Maatstaf voor verdeling cluster Participatie (€1.488 per inschrijving) en infrastructurele opslag.
- **Bijstandsbudget / BUIG** — gebudgetteerd budget (begroting SZW) voor bijstandsuitkeringen en loonkostensubsidies. Drie publicatiemomenten: voorlopig (oktober t-1), nader voorlopig (mei), definitief (oktober).
- **Cluster Participatie** — fictief budget in de algemene uitkering gemeentefonds voor uitvoering, re-integratie, begeleiding en minimabeleid. Basisbedragen periodiek herijkt; uitkeringsfactor als vermenigvuldiger.
- **Integratie-uitkering Participatie** — tijdelijke uitkering in het gemeentefonds voor Wsw en beschut werk. Wsw-deel krimpt (richting nul rond 2048); beschut-werkdeel groeit.
- **Vangnetuitkering** — financiële regeling voor gemeenten met >7,5% tekort op bijstandsbudget; vergoedt helft tekort 7,5%-12,5% en alles boven 12,5%.
- **Macrobudget** — landelijk totaalbudget, berekend als volume × prijs, met correcties voor conjunctuur en rijksbeleid.
- **Sociaal ontwikkelbedrijf** — organisatie die werkplekken en begeleiding biedt aan mensen met afstand tot de arbeidsmarkt; opvolger van de traditionele SW-bedrijven. Circa 60% heeft geen duidelijk takenpakket; impulsbudget beoogt transitie te ondersteunen.
- **Nieuwe doelgroep** — personen die vóór 2015 in Wsw of Wajong zouden zijn terechtgekomen, nu Participatiewet. Groeit structureel tot stabilisatie rond 2048.
- **Loonwaarde** — vastgestelde productieve waarde van een werknemer met beperking, als percentage van het minimumloon. Bepaald door gecertificeerde loonwaardedeskundige.
- **Banenafspraak** — afspraak kabinet en sociale partners om banen te creëren voor mensen met arbeidsbeperking.
- **Impulsbudget** — 10-jarig budget (2025-2034) voor transitie sociaal ontwikkelbedrijven. Verdeeld via DU op basis van doelgroepenregister, uitgekeerd aan grootste gemeente per samenwerkingsverband.
- **Infrastructurele opslag** — rijksbijdrage (vanaf 2025) voor banen van personen die niet onder beschut werk vallen maar wel aangewezen zijn op sociaal ontwikkelbedrijf-infrastructuur.

## Relevantie voor bedrijfsarchitectuur

Deze bron levert:

1. **BO-grondslag voor Loonkostensubsidie** — prominentste nieuw concept. GGM-entiteit in domein Werk (1 attribuut). De handreiking toont dat LKS een centraal instrument is met eigen administratie, rapportage (SiSa) en budgetsystematiek. Sterke BO-kandidaat.
2. **BO-grondslag voor Re-integratievoorziening** — GGM-entiteit in domein Werk (12 attributen). De handreiking beschrijft re-integratie als een van de vier kostencategorieën (naast uitvoering, begeleiding, minimabeleid). Sterke BO-kandidaat.
3. **Verrijking Inkomensvoorziening** — bijstandsuitkering als subtype krijgt financiële context: budgetteringssystematiek, verdeelmodel, vangnet.
4. **Begrippen voor onderwerpoverzicht** — financieringsmechanismen (BUIG, cluster Participatie, IU Participatie) en doelgroepbegrippen (nieuwe doelgroep, doelgroepenregister) die het Werk en Inkomen-domein structureren.
5. **Cross-domein** — beschut werk verbindt domein Werk met Wsw (aflopend) en sociaal ontwikkelbedrijven (transformatie).

## Citaten

> "Gemeenten hebben in financieel opzicht belang bij een zo gunstig mogelijk saldo. Dat betekent dat zoveel mogelijk mensen in hun eigen onderhoud kunnen voorzien en niet afhankelijk zijn van een bijstandsuitkering." (Berenschot, 2025 — over bijstandsbudget als prikkel)

> "Bij het maken van beleid is het belangrijk dat gemeenten zich realiseren dat via het gemeentefonds middelen worden verstrekt voor de uitvoering, re-integratie, begeleiding en het minimabeleid." (Berenschot, 2025 — over cluster Participatie)

> "De loonkostensubsidie compenseert het verschil tussen de loonwaarde van de werknemer en het wettelijk minimumloon." (Berenschot, 2025 — definitie loonkostensubsidie)

> "Gemeenten zijn verplicht om personen met een positief advies beschut werk van het UWV, een beschutte werkplek aan te bieden zolang het aantal zoals neergelegd in een ministeriële regeling nog niet is bereikt." (Berenschot, 2025 — taakstelling beschut werk)

> "Ongeveer 60% van de sociaal ontwikkelbedrijven geeft aan geen duidelijk takenpakket te hebben en 46% mist een helder toekomstperspectief." (Berenschot, 2025 — urgentie transitie)

## Bronnen

- [[Sources/Onderwerpen/Werk en Inkomen/handreiking-explicitering-budgetten-participatiewet-wsw]]
