---
type: ggm-beleidsdomein
naam: Monumenten
definitie: "Het informatiedomein dat gegevens omvat over de aanwijzing, bescherming en instandhouding van monumenten, inclusief gebouwen, objecten en landschappen, die van cultuurhistorische, wetenschappelijke of esthetische waarde zijn."
taakveld: "5 Sport, Cultuur en Recreatie"
aantal_entiteiten: 6
---

# GGM Beleidsdomein: Monumenten

Onderdeel van beleidsdomein **Erfgoed** binnen taakveld "5 Sport, Cultuur en Recreatie" (zie ../structuur-ggm.md).

## Entiteiten

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Ambacht** | Beroep waarbij een handwerker met gereedschap eindproducten maakt. | jaarAmbachtVanaf, jaarAmbachtTot, ambachtsoort | Nee | GGM |
| **Beschermde Status** | Status van de bescherming van een monument. Een monument / erfgoed is een overblijfsel van kunst, cultuur, architectuur of nijverheid dat van algemeen belang wordt geacht vanwege de historische, volkskundige, artistieke, wetenschappelijke, industrieel-archeologische of andere sociaal-culturele waarde. Vormen van monument / erfgoed met de status rijks- provinciaal- of gemeentelijke monument / erfgoed zijn beschermd op grond van een besluit van respectievelijk het Ministerie OCW, de provincie of de gemeente, | rijksmonumentcode, gemeentelijkMonumentCode, datumInschrijvingRegister, naam, type, gezichtscode, complex, opmerkingen, bronnen, omschrijving | Nee | GGM |
| **Bouwactiviteit** | Het bouwen van een bouwwerk. | bouwjaarVan, bouwjaarTot, indicatie, bouwjaarklasse, omschrijving | Nee | GGM |
| **Bouwstijl** | Trant van bouwen met bepaalde kenmerken in een bepaalde periode. In de betrokken tijdperken waren het geen levende voorstellingen; het zijn later geformuleerde (generaliserende) geschiedkundige constructies. Doelbewust komt deze tendens op sedert c. 1830. (Haslinghuis) | hoofdstijl, substijl, zuiverheid, toelichting | Nee | GGM |
| **Bouwtype** | Typering van een bouwstijl | hoofdcategorie, subcategorie, toelichting | Nee | GGM |
| **OorspronkelijkeFunctie** | De functie van een object na bouw of oplevering | hoofdfunctie, functiesoort, hoofdcategorie, subcategorie, functie, verbijzondering, toelichting | Nee | GGM |

## Overervingshiërarchie

Geen overervingshiërarchie aanwezig in dit beleidsdomein.

## Relatiediagrammen

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

## Observaties

- Dit beleidsdomein bevat 6 entiteiten.
