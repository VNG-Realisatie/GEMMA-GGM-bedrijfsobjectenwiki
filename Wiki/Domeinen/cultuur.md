---
type: domein
naam: Cultuur
status: afgerond
verwerkingsdatum: 2026-06-19
bronnen_count: 5
begrippen_count: 18
bo_count: 3
---

# Cultuur

Gemeentelijk domein voor kunst, cultuur en erfgoed. Gemeenten faciliteren culturele voorzieningen, voeren cultuurbeleid, en beheren erfgoed (monumenten, archieven, musea). Het cultuurbeleid is overwegend beleidsmatig; de concrete registratieobjecten zitten in het erfgoeddomein.

In het GGM valt dit onder taakveld **5 Sport, Cultuur en Recreatie** met beleidsdomeinen **Erfgoed** (44 entiteiten) en **Musea** (32 entiteiten). Er is geen apart "Cultuur"-beleidsdomein in het GGM — cultuurbeleid wordt niet als data gemodelleerd.

## Begrippen

| Begrip | Type | Omschrijving | BO? | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|
| [[monument]] | object | Beschermd onroerend erfgoed met rijks-, provinciaal of gemeentelijke status | ✅ | 6/6 criteria, exact match (Beschermde Status) | Rijksmonument, gemeentelijk monument, beschermd gezicht | ja |
| [[archiefstuk]] | object | Gearchiveerde informatie ongeacht medium, beheerd door gemeentearchief | ✅ | 6/6 criteria, exact match | Raadsbesluit in archief, historisch document, digitaal bestand | ja |
| [[museumobject]] | object | Object met cultuurhistorische waarde in museale collectie | ✅ | 6/6 criteria, exact match | Schilderij, archeologisch artefact, historisch gebruiksvoorwerp | ja |
| archeologische vindplaats | object | Locatie met archeologische waarde | ❌ | Wel GGM-entiteit maar nationaal geregistreerd (ARCHIS), niet primair gemeentelijk | Opgraving binnenstad, Romeinse vondstlocatie | ja |
| culturele voorziening | object | Organisatie/faciliteit die cultuur faciliteert | ❌ | Niet als dataobject geregistreerd; is facilitaire/organisatorische entiteit | Theater, podium, broedplaats, muziekschool | nee |
| bibliotheek | object | Gemeentelijke voorziening voor kennis en cultuur | ❌ | Voorziening, niet als erfgoedobject geregistreerd | Openbare bibliotheek, vestiging | nee |
| cultuurbeleid | thema | Gemeentelijk beleid voor cultureel aanbod | ❌ | Beleidsmatig, geen object | Cultuurvisie, cultuuragenda | nee |
| cultuurwaarde | waarde | Intrinsieke, maatschappelijke en economische waarde van cultuur | ❌ | Normatief concept | — | nee |
| cultuureducatie | thema | Cultureel onderwijs binnen en buiten school | ❌ | Activiteit/proces | CmK, cultuur op school | nee |
| cultuurparticipatie | thema | Deelname aan culturele activiteiten | ❌ | Activiteit/proces | Amateurkunst, koorlidmaatschap | nee |
| fair pay | instrument | Eerlijke beloning cultuurprofessionals | ❌ | Beleidsinstrument | Fair Practice Code, culturele codes | nee |
| ringenmodel | instrument | Differentiatie culturele voorzieningen naar gemeenteomvang | ❌ | Beleidsinstrument/classificatie | Kernachtig/uitgebreid/alomvattend pakket | nee |
| culturele centrumfunctie | thema | Mate waarin gemeente cultuur verzorgt voor regio | ❌ | Classificatie van gemeenten | G40 als cultureel centrum | nee |
| creatieve cyclus | thema | Keten: leren → produceren → presenteren → interesseren | ❌ | Conceptueel model | — | nee |
| culturele basisinfrastructuur | thema | Lokale voorzieningen voor cultuureducatie en -participatie | ❌ | Strategisch concept | — | nee |
| basisinfrastructuur (bis) | instrument | Rijksinstrument voor meerjarige cultuursubsidies | ❌ | Rijksinstrument, niet gemeentelijk | Rijksgesubsidieerde orkesten, musea | nee |
| Erfgoedwet | instrument | Integrale wetgeving (2016) voor erfgoed, musea, archeologie | ❌ | Wet/governance | — | nee |
| cultuurfinanciering | thema | Systematiek van publieke bekostiging van cultuur | ❌ | Beleidsmatig | Gemeentefonds-aandeel cultuur (€2 mrd) | nee |

## GGM-entiteitendekking

| GGM-beleidsdomein | Entiteiten | BO | Niet-BO | Niet beoordeeld | Reden niet beoordeeld |
|---|---|---|---|---|---|
| Monumenten | 6 | 1 | 5 | 0 | — |
| Archief | 8 | 1 | 3 | 4 | Geen beleidsbron over archieflogistiek (Depot, Kast, Plank, Stelling) |
| Archeologie | 17 | 0 | 0 | 17 | Geen beleidsbron; opgravingsdetails vermoedelijk te granulair voor BO |
| Generiek Erfgoed | 4 | 0 | 1 | 3 | Erfgoed Object is abstract parent; Historisch Persoon, Objectclassificatie, Auteur niet beoordeeld |
| Musea | 32 | 1 | 9 | 22 | Prinsenhof-specifieke entiteiten (verkoop, events); geen museale beleidsbron |

**Totaal: 67 GGM-entiteiten, 3 BO, 18 niet-BO, 46 niet beoordeeld (69%)**

## GGM-dekkingsanalyse

### Erfgoed (taakveld 5, 44 entiteiten)

Het GGM modelleert erfgoed zeer gedetailleerd in vier subdomeinen:

- **Monumenten** (6 entiteiten): Beschermde Status → [[monument]]. De 5 niet-BO's (Bouwstijl, Bouwtype, Bouwactiviteit, Ambacht, OorspronkelijkeFunctie) zijn classificaties/kenmerken van een monument, geen zelfstandige objecten.
- **Archief** (8 entiteiten): Archiefstuk → [[archiefstuk]]. Archief, Vindplaats, Ordeningsschema zijn containers/classificaties (niet-BO). Depot, Kast, Plank, Stelling zijn opslaglogistiek — niet beoordeeld, vermoedelijk te operationeel.
- **Archeologie** (17 entiteiten): Artefact, Vondst, Put, Spoor, Vindplaats, Project, Boring, Vlak, Vulling, etc. **Volledig niet beoordeeld** — er zijn geen VNG-beleidsbronnen die het archeologisch werkveld beschrijven. Bij toevoeging van bronnen over gemeentelijk archeologiebeleid (bijv. archeologische beleidskaart, selectiebesluit) kunnen hier BO's uit komen.
- **Generiek Erfgoed** (4 entiteiten): Erfgoed Object is abstract parent van [[archiefstuk]] en [[museumobject]] — geen eigen BO. Historisch Persoon, Objectclassificatie en Auteur zijn niet beoordeeld.

### Musea (taakveld 5, 32 entiteiten)

Museumobject → [[museumobject]]. Het overgrote deel van dit domein is **Prinsenhof-specifiek** (Balieverkoop, Winkelvoorraaditem, Omzetgroep, Productgroep, Entreekaart, etc.) — operationele museum-entiteiten die niet op bedrijfsobjectniveau thuishoren. Entiteiten als Collectie, Tentoonstelling, Bruikleen en Programma zijn wél herkenbaar maar niet beoordeeld tegen beleidsbronnen. Bij toevoeging van museale beleidsbronnen (bijv. collectiebeleid, Erfgoedwet-uitvoering) kunnen hier meer BO's uit komen.

### Cultuurbeleid

Het GGM bevat **geen** beleidsdomein voor cultuurbeleid. Begrippen als cultuurvisie, cultuurfinanciering, ringenmodel zijn governance en beleid — structureel buiten GGM-scope (zie [[Wiki/Analyses/ggm-dekkingspatroon]]).

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/Cultuur/kunst-en-cultuur|Kunst en cultuur]] — VNG-overzicht cultuurbeleid
- [[Wiki/Bronsamenvattingen/Cultuur/propositie-cultuur|Propositie Samen cultuur borgen]] — VNG-propositie vier pijlers cultuurbeleid
- [[Wiki/Bronsamenvattingen/Cultuur/architectuur-en-erfgoed|Architectuur en erfgoed]] — VNG-overzicht erfgoed, monumenten, archeologie
- [[Wiki/Bronsamenvattingen/Cultuur/bibliotheekwerk|Bibliotheekwerk]] — VNG-overzicht bibliotheekwerk
- [[Wiki/Bronsamenvattingen/Cultuur/toelichting-ringenmodel|Toelichting ringenmodel]] — VNG-actualisering ringenmodel 2.0

## Nog te verwerken bronnen

- [Sources/Onderwerpen VNG/Cultuur/sport.md](Sources/Onderwerpen%20VNG/Cultuur/sport.md) — apart domein, niet relevant voor cultuur

## Openstaande vragen

- **46 van 67 GGM-entiteiten (69%) zijn niet beoordeeld** wegens ontbrekende beleidsbronnen. Het domein is afgerond op basis van de beschikbare VNG-bronnen, maar die beschrijven cultuurbeleid — niet het erfgoed- en musea-werkveld zelf. Bij toevoeging van domeinspecifieke bronnen (archeologiebeleid, collectiebeleid, archiefbeleid) zullen vermoedelijk meer BO's naar voren komen.
- **Archeologie** (17 entiteiten) is volledig onbeoordeeld. Gemeenten hebben een archeologische beleidskaart en nemen selectiebesluiten — daar zitten waarschijnlijk registratieobjecten in.
- **Musea** — Collectie, Tentoonstelling en Bruikleen zijn herkenbare begrippen die bij museale beleidsbronnen alsnog BO kunnen worden.

## Terugmeldingen richting GGM

Geen terugmeldingen. De drie BO's hebben exacte GGM-matches. Het ontbreken van een cultuurbeleid-domein in het GGM is structureel (GGM modelleert data, niet governance).
