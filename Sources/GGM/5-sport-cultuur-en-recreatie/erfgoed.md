---
type: ggm-beleidsdomein
naam: Erfgoed
taakveld: "5 Sport, Cultuur en Recreatie"
aantal_entiteiten: 44
---

# GGM Beleidsdomein: Erfgoed

Beleidsdomein binnen taakveld "5 Sport, Cultuur en Recreatie" (zie ../structuur-ggm.md).

## Entiteiten

### Erfgoed: Archeologie Domeinmodel

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Archeologiebesluit** | Een professioneel oordeel dat gebaseerd is op algemeen aanvaarde wetenschap ten aanzien van de archeologie | *(geen attributen)* | Nee | GGM |
| **Artefact** | De benaming voor ieder verplaatsbaar object dat door de mens is vervaardigd, bewerkt en/of gebruikt. | projectCD, putnummer, vondstnummer, artefectnummer, datering, maten, type, beschrijving, determinatieniveau, naam, doosnummer, tekeningnummer, dianummer, fotonummer, restauratieWenselijk, exposabel, conserveren, key, keyPut, keyMagazijnplaatsing, keyDoos, dateringComplex, opmerkingen, functie, origine, literatuur, herkomst, keyVondst | Nee | GGM |
| **Artefactsoort** | Typering van artefacten | code, naam, omschrijving | Nee | GGM |
| **Doos** | Een afsluitbaar object waar iets in wordt opgeborgen of verpakt. | projectCD, doosnummer, inhoud, herkomst, key, keyMagazijnlocatie | Nee | GGM |
| **Kaart** | De geografische weergave van een gedeelte van het aardoppervlak | naam, omschrijving, content | Nee | GGM |
| **Magazijnlocatie** | Locatie van een magazijn | vaknummer, volgletter, key, stelling | Nee | GGM |
| **Magazijnplaatsing** | Het ergens neerzetten van een object in een magazijn. | uitgeleend, beschrijving, datumGeplaatst, key, keyDoos, keyMagazijnlocatie, projectCD, herkomst | Nee | GGM |
| **Project** | Geheel van activiteiten uitgevoerd in een tijdelijk samenwerkingsverband gericht op het binnen bepaalde randvoorwaarden (bv. tijd, geld) bereiken van een vooraf gedefinieerd resultaat. | projectCD, naam, datumStart, datumEinde, naamcode, toponiem, locatie, coordinaten, jaarVan, jaarTot, trefwoorden | Nee | GGM |
| **Put** | Grondspoor, veelal verstevigd en gefundeerd aangelegd, bedoeld voor de tijdelijke opslag van danwel water (waterput) danwel uitwerpselen en afval (beerput). | projectCD, putnummer, key | Nee | GGM |
| **Spoor** | Een blijk van eerdere aanwezigheid. | projectCD, putnummer, vlaknummer, spoornummer, hoogteBoven, hoogteOnder, aard, datering, datum, vorm, beschrijving, key, keyVlak | Nee | GGM |
| **Stelling** | Een systeem om goederen op te slaan die worden vervoerd en opgeslagen op pallets, in bundels of per stuk.(Wikipedia) | stellingcode, inhoud | Nee | GGM |
| **Vindplaats** | Een plek waar men iets gevonden heeft. | projectcode, locatie, vindplaatsOmschrijving, gemeente, datering, begindatering, einddatering, aard, onderzoek, mobilia, depot, documentatie, bibliografie, beschrijving | Nee | GGM |
| **Vlak** | Plat, oneindig oppervlak of variëteit zonder enige kromming. | projectCD, putnummer, vlaknummer, diepteVan, diepteTot, key, keyPut | Nee | GGM |
| **Vondst** | Overblijfsel, voorwerp of ander spoor van menselijke aanwezigheid in het verleden afkomstig van een archeologisch monument | projectCD, vondstnummer, putnummer, vlaknummer, spoornummer, vullingnummer, omstandigheden, omschrijving, key, keyVulling, datum, XCoordinaat, YCoordinaat | Nee | GGM |
| **Vulling** | Dunne wegeringsplank gebruikt om de ruimte tussen de bovenste kimweger en de onderste balkweger op te vullen (Sopers, 1974). | projectCD, putnummer, vlaknummer, spoornummer, vullingnummer, grondsoort, kleur, structuur, key, keySpoor | Nee | GGM |
| **boring** | Een verticale grondmonstername binnen een project De gegevens over het geheel van activiteiten, voor zover relevant voor het onderzoek, dat tot doel heeft door boren een gat in de ondergrond te maken om monsters uit de ondergrond te nemen en/of metingen aan de ondergrond te doen. Een middel om door boren of steken toegang te krijgen tot de ondergrond om bijvoorbeeld geroerde en/of ongeroerde monsters aan de ondergrond te ontlenen voor nader onderzoek. | *(geen attributen)* | Nee | GGM |
| **locatie** | Een specifieke plaats | locatiePunt | Nee | GGM |

### Archief Model

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Archiefstuk** | Bijeengebrachte informatie, ongeacht het medium, die wordt gecreëerd, ontvangen en gearchiveerd door een bureau, een instelling, een organisatie of een individu met het oog op het nakomen van wettelijke verplichtingen of het uitvoeren van zakelijke transacties.(AAT) | trefwoorden, openbaarheidsbeperking, inventarisnummer, omvang, beschrijving, uiterlijkeVorm | Nee | GGM |
| **Depot** | Plaats waar iets bewaard wordt. | naam, omschrijving | Nee | GGM |
| **DigitaalBestand** | Bestand dat uitsluitend met behulp van besturingsprogrammatuur of toepassingsprogrammatuur geraadpleegd kunnen worden | naam, omschrijving, mimetype, blob | Nee | GGM |
| **Kast** | Object met een permanent karakter dat dient om iets in te bergen en te beschermen. | kastnummer | Nee | GGM |
| **Plank** | Deel, plaat; stuk hout breder dan het dik is en langer dan breed. | planknummer | Nee | GGM |
| **Stelling** | Een systeem om goederen op te slaan die worden vervoerd en opgeslagen op pallets, in bundels of per stuk.(Wikipedia) | stellingnummer | Nee | GGM |
| **Uitgever** | Iemand die iets op de markt brengt; iemand die iets uitgeeft | *(geen attributen)* | Nee | GGM |
| **Vindplaats** | Een plek waar men iets gevonden heeft. | *(geen attributen)* | Nee | GGM |

### Archief Relaties met Kern

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Bezoeker** | Een persoon die iemand of iets bezoekt. | *(geen attributen)* | Nee | GGM |
| **Rechthebbende** | Een rechthebbende is iemand die rechten heeft op een goed. | *(geen attributen)* | Nee | GGM |

### Archief Aanvragen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Aanvraag** | (officieel) verzoek, iets (officieel) vragen aan een bevoegde macht. | datumtijd | Nee | GGM |

### Archief Model Indeling

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Archief** | De bewaarplaats van belangrijke gegevens die zijn vastgelegd in documentvorm alsook de verzameling van documenten die voor een bepaald doel vervaardigd zijn. | naam, omschrijving, openbaarheidsbeperking, archiefnummer | Nee | GGM |
| **Archiefcategorie** | Typologie van een archief conform landelijke indeling | naam, omschrijving, nummer | Nee | GGM |
| **Indeling** | Onderwerpen groeperen in samenhangende categorieën. | naam, nummer, omschrijving, indelingsoort | Nee | GGM |
| **Index** | *(geen definitie in GGM)* | indexnaam, indexwaarde | Nee | GGM |
| **Nadere Toegang** | De bevoegdheid om gegevens te raadplegen, bepaalde plaatsen te betreden of een bepaalde taak uit te oefenen. | *(geen attributen)* | Nee | GGM |
| **Ordeningsschema** | Ordening om archief en collecties beter vindbaar en bruikbaar voor betrokkenen. | naam, text | Nee | GGM |

### Generieke entiteiten Erfgoed

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Auteur** | De persoon die verantwoordelijk is voor de inhoud van een (digitaal) document | datumGeboorte, datumOverlijden | Nee | GGM |
| **Erfgoed Object** | Uit het verleden geërfde materiële en immateriële objecten | titel, omschrijving, dateringVanaf, dateringTot | Nee | GGM |
| **Historisch Persoon ** | Natuurlijk persoon waarvan informatie beschikbaar is uit het verleden. | naam, datumGeboorte, datumOverlijden, omschrijving, woondeOp, beroep, publiekToegankelijk | Nee | GGM |
| **Objectclassificatie** | Systematische identificatie en ordening van objecten in categorieën overeenkomstig logisch gestructureerde conventies, methoden en procedureregels weergegeven in een classificatiesysteem. | naam, omschrijving | Nee | GGM |

### Diagram Monumenten

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Beschermde Status** | Status van de bescherming van een monument. Een monument / erfgoed is een overblijfsel van kunst, cultuur, architectuur of nijverheid dat van algemeen belang wordt geacht vanwege de historische, volkskundige, artistieke, wetenschappelijke, industrieel-archeologische of andere sociaal-culturele waarde. Vormen van monument / erfgoed met de status rijks- provinciaal- of gemeentelijke monument / erfgoed zijn beschermd op grond van een besluit van respectievelijk het Ministerie OCW, de provincie of de gemeente, | rijksmonumentcode, gemeentelijkMonumentCode, datumInschrijvingRegister, naam, type, gezichtscode, complex, opmerkingen, bronnen, omschrijving | Nee | GGM |

### Diagram Monumenten Detail

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Ambacht** | Beroep waarbij een handwerker met gereedschap eindproducten maakt. | jaarAmbachtVanaf, jaarAmbachtTot, ambachtsoort | Nee | GGM |
| **Bouwactiviteit** | Het bouwen van een bouwwerk. | bouwjaarVan, bouwjaarTot, indicatie, bouwjaarklasse, omschrijving | Nee | GGM |
| **Bouwstijl** | Trant van bouwen met bepaalde kenmerken in een bepaalde periode. In de betrokken tijdperken waren het geen levende voorstellingen; het zijn later geformuleerde (generaliserende) geschiedkundige constructies. Doelbewust komt deze tendens op sedert c. 1830. (Haslinghuis) | hoofdstijl, substijl, zuiverheid, toelichting | Nee | GGM |
| **Bouwtype** | Typering van een bouwstijl | hoofdcategorie, subcategorie, toelichting | Nee | GGM |
| **OorspronkelijkeFunctie** | De functie van een object na bouw of oplevering | hoofdfunctie, functiesoort, hoofdcategorie, subcategorie, functie, verbijzondering, toelichting | Nee | GGM |

## Overervingshiërarchie

```
Document (abstract)
    └── Archiefstuk
```

```
Erfgoed Object (abstract)
    └── Archiefstuk
    └── Museumobject
```

```
Historisch Persoon  (abstract)
    └── Auteur
```

```
NatuurlijkPersoon (abstract)
    └── Bezoeker
    └── Historisch Persoon 
```

```
Rechtspersoon (abstract)
    └── Rechthebbende
    └── Uitgever
```

## Relatiediagrammen

### Erfgoed: Archeologie Domeinmodel

```
Artefact [0..*] ──── Artefactsoort [1] (is van soort)
Artefact [0..*] ──── Doos [0..1] (zit in)
Artefact [0..*] ──── Magazijnplaatsing [0..1] (vindbaar op)
Doos [0..*] ──── Magazijnlocatie [1] (staat op)
Magazijnplaatsing [0..1] ──── Doos [0..*] (zit in)
Magazijnplaatsing [0..*] ──── Magazijnlocatie [0..1] (staat op)
Magazijnplaatsing [0..*] ──── Project [0..1] (hoort bij)
Project [1] ──── Archeologiebesluit [0..*] (heeft)
Project [1] ──── Put [0..*] (heeft)
Project [1] ──── boring [0..*] (heeft)
Project [0..*] ──── locatie [1..*] (wordt begrensd door)
Put [1] ──── Vlak [0..*] (heeft)
Put [0..*] ──── locatie [1..*] (heeft locatie)
Spoor [1] ──── Vulling [0..*] (heeft)
Stelling [1] ──── Magazijnlocatie [0..*] (heeft)
Vindplaats [0..1] ──── Project [1] (hoort bij)
Vlak [1] ──── Spoor [0..*] (heeft)
Vondst [0..1] ──── Artefact [0..*] (bevat)
Vulling [1] ──── Vondst [0..*] (heeft)
```

### Archief Model

```
Aanvraag [0..*] ──── Archiefstuk [0..*] (voor)
Archiefstuk [0..*] ──── Archief [1] (is onderdeel van)
Archiefstuk [1] ──── DigitaalBestand [0..*] (heeft)
Archiefstuk [1] ──── Nadere Toegang [0..1] (heeft)
Archiefstuk [0..*] ──── Ordeningsschema [0..*] (heeft)
Archiefstuk [0..*] ──── Periode [1..*] (stamt uit)
Archiefstuk [0..*] ──── Uitgever [0..1] (heeft)
Archiefstuk [0..*] ──── Vindplaats [1] (heeft)
Depot [1] ──── Stelling [0..*] (heeft)
Indeling [0..1] ──── Archiefstuk [0..*] (valt binnen)
Kast [0..1] ──── Plank [0..*] (heeft)
Stelling [1] ──── Kast [0..*] (heeft)
Vindplaats [0..*] ──── Depot [1] (is te vinden in)
Vindplaats [0..*] ──── Kast [1] (is te vinden in)
Vindplaats [0..*] ──── Plank [1] (is te vinden in)
Vindplaats [0..*] ──── Stelling [0..1] (is te vinden in)
```

### Archief Relaties met Kern

```
Archief [0..*] ──── Rechthebbende [0..1] (heeft)
Bezoeker [1] ──── Aanvraag [0..*] (doet)
```

### Archief Aanvragen

```
Aanvraag [0..*] ──── Archiefstuk [0..*] (voor)
Bezoeker [1] ──── Aanvraag [0..*] (doet)
```

### Archief Model Indeling

```
Archief [0..*] ──── Archiefcategorie [0..*] (valt binnen)
Archief [0..*] ──── Periode [1..*] (stamt uit)
Archief [0..*] ──── Rechthebbende [0..1] (heeft)
Archiefstuk [0..*] ──── Archief [1] (is onderdeel van)
Archiefstuk [1] ──── Nadere Toegang [0..1] (heeft)
Archiefstuk [0..*] ──── Ordeningsschema [0..*] (heeft)
Indeling [0..*] ──── Archief [1] (hoort bij)
Indeling [0..1] ──── Archiefstuk [0..*] (valt binnen)
Indeling [1] ──── Indeling [0..*] (valt binnen)
Nadere Toegang [1] ──── Index [1..*] (wordt beschreven)
```

### Generieke entiteiten Erfgoed

```
Erfgoed Object [0..*] ──── Objectclassificatie [0..*] (valt binnen)
Foto [0..*] ──── Erfgoed Object [0..*] (betreft)
Historisch Persoon  [0..*] ──── Erfgoed Object [0..*] (speelt rol in)
Museumobject [0..*] ──── Historisch Persoon  [0..*] (heeft verbinding)
Tentoonstelling [0..*] ──── Historisch Persoon  [0..*] (is gewijd aan)
Video-opname [0..*] ──── Erfgoed Object [0..*] (betreft)
```

### Diagram Monumenten

```
Beschermde Status [0..*] ──── Ambacht [0..*] (monument ambacht)
Beschermde Status [0..*] ──── Bouwactiviteit [0..*] (monument bouwactiviteit)
Beschermde Status [0..*] ──── Bouwstijl [0..*] (monument bouwstijl)
Beschermde Status [0..*] ──── Bouwtype [0..*] (monument bouwtype)
Beschermde Status [1] ──── Foto [0..*] (monument fotos)
Beschermde Status [1] ──── KadastraleOnroerendeZaak [0..*] (betreft)
Beschermde Status [0..*] ──── OorspronkelijkeFunctie [0..*] (monument functie)
Beschermde Status [0..1] ──── OpenbareRuimte [0..*] (betreft)
Beschermde Status [0..1] ──── Pand [0..*] (betreft)
```

### Diagram Monumenten Detail

```
Beschermde Status [0..*] ──── Ambacht [0..*] (monument ambacht)
Beschermde Status [0..*] ──── Bouwactiviteit [0..*] (monument bouwactiviteit)
Beschermde Status [0..*] ──── Bouwstijl [0..*] (monument bouwstijl)
Beschermde Status [0..*] ──── Bouwtype [0..*] (monument bouwtype)
Beschermde Status [0..*] ──── OorspronkelijkeFunctie [0..*] (monument functie)
```

## Observaties

- Dit beleidsdomein bevat 44 entiteiten.
- Entiteiten zijn gegroepeerd in 8 diagramgroepen: Erfgoed: Archeologie Domeinmodel (17), Archief Model (8), Archief Relaties met Kern (2), Archief Aanvragen (1), Archief Model Indeling (6), Generieke entiteiten Erfgoed (4), Diagram Monumenten (1), Diagram Monumenten Detail (5).
- Er zijn 8 generalisatierelaties aanwezig.
