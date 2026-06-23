---
type: ggm-beleidsdomein
naam: Archeologie
definitie: "Het informatiedomein dat gegevens omvat over archeologische opgravingen, onderzoeken en besluitvorming, gericht op het behoud, de bescherming en de ontsluiting van archeologisch erfgoed binnen de kaders van de Erfgoedwet."
taakveld: "Erfgoed"
aantal_entiteiten: 17
---

# GGM Beleidsdomein: Archeologie

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

## Relatiediagrammen

```
Artefact [0..*] ──── Artefactsoort [1..1] (is van soort)
Artefact [0..*] ──── Doos [0..1] (zit in)
Artefact [0..*] ──── Magazijnplaatsing [0..1] (vindbaar op)
Doos [0..*] ──── Magazijnlocatie [1..1] (staat op)
Magazijnplaatsing [0..1] ──── Doos [0..*] (zit in)
Magazijnplaatsing [0..*] ──── Magazijnlocatie [0..1] (staat op)
Magazijnplaatsing [0..*] ──── Project [0..1] (hoort bij)
Project [1..1] ──── Archeologiebesluit [0..*] (heeft)
Project [1..1] ──── Put [0..*] (heeft)
Project [1..1] ──── boring [0..*] (heeft)
Project [0..*] ──── locatie [1..*] (wordt begrensd door)
Put [1..1] ──── Vlak [0..*] (heeft)
Put [0..*] ──── locatie [1..*] (heeft locatie)
Spoor [1..1] ──── Vulling [0..*] (heeft)
Stelling [1..1] ──── Magazijnlocatie [0..*] (heeft)
Vindplaats [0..1] ──── Project [1] (hoort bij)
Vlak [1..1] ──── Spoor [0..*] (heeft)
Vondst [0..1] ──── Artefact [0..*] (bevat)
Vulling [1..1] ──── Vondst [0..*] (heeft)
```

## Observaties

- Dit beleidsdomein bevat 17 Objecttype-entiteiten.
- Entiteiten zijn gegroepeerd in 1 diagramgroepen: Erfgoed: Archeologie Domeinmodel (17).
