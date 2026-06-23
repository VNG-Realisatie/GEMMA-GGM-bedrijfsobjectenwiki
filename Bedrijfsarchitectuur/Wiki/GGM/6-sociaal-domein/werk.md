---
type: ggm-beleidsdomein
naam: Werk
definitie: "Het informatiedomein dat gegevens omvat over de ondersteuning van mensen bij het vinden en behouden van werk, gebaseerd op de Participatiewet en gericht op het bevorderen van arbeidsparticipatie."
taakveld: "6 Sociaal Domein"
aantal_entiteiten: 33
---

# GGM Beleidsdomein: Werk

### Detaildiagram Werk

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Arbeidsmarktkwalificaties** | Een verzameling formele en informele kwalificaties, vaardigheden en eigenschappen die relevant zijn voor de inzetbaarheid van een persoon op de arbeidsmarkt. | KlantTypering, Code taalbeheersing mondeling, Code taalbeheersing schriftelijk, Code werk en denkniveau, ToelichtingArbeidsmarktKwalificaties | Nee | GGM |
| **Arbeidsperiode** | Een aaneengesloten periode waarin een persoon arbeid heeft verricht, met begin- en einddatum. | Datum aanvang arbeidsperiode, Datum einde arbeidsperiode, Gemiddeld aantal uur per week, Functienaam, Functieomschrijving, Contact persoon, Contact email, Contact telefoon | Nee | GGM |
| **Arbeidsverhouding** | Een relatie waarin sprake is van afspraken tussen een werknemer en een werkgever over het verrichten van arbeid. | Datum aanvraag arbeidsverhouding, Datum einde arbeidsverhouding | Nee | GGM |
| **Arbeidsvermogen** | Een inschatting van wat iemand op basis van fysieke, mentale en sociale capaciteiten aan arbeid kan verrichten. | CodeArbeidsvermogen | Nee | GGM |
| **Bemiddelingsberoep** | Het beoogde beroep waarvoor een persoon wordt begeleid of bemiddeld in een traject. | ToelichtingBeroep | Nee | GGM |
| **Bemiddelingstraject** | Een traject waarin een persoon begeleid wordt naar passend werk, bijvoorbeeld door een gemeente of uitvoeringsinstantie. | DatumBemiddeling, OmschrijvingContactbemiddeling, OmschrijvingStatusbemiddeling, OmschrijvingResultaatbemiddeling, DatumVacature, IndicatiePlaatsing | Nee | GGM |
| **BeschikbaarVoorArbeid** | Een indicatie of iemand op dit moment inzetbaar is voor arbeid, los van begeleiding of ondersteuning. | StartdatumBeschikbaarheid, DagBeschikbaarheid, AantalUrenpwBeschikbaar, Interval opzegtermijn, WaardeOpzegtermijn, StartdagBeschikbaarheid, EinddatumBeschikbaarheid, EindtijdDagBeschikbaarheid, ToelichtingBeschikbaarheid, Indicatie nog werkzaam | Nee | GGM |
| **BeschikbaarVoorBemiddeling** | Een indicatie dat een persoon beschikbaar is voor bemiddeling richting arbeid, waarbij wordt gekeken naar inzetbaarheid, bereidheid en eventuele beperkingen. | IndicatieDirectBemiddelbaar, DatumEinde | Nee | GGM |
| **DoelReintegratievoorziening** | Het beoogde effect van een ingezette voorziening, bijvoorbeeld toeleiding naar werk, dagbesteding of maatschappelijke participatie. | CodeDoelReintegratievoorziening | Nee | GGM |
| **Doelgroepenregister** | Een landelijk register waarin mensen met een afstand tot de arbeidsmarkt worden opgenomen, vaak ten behoeve van loonkostensubsidie of andere voorzieningen. | IndicatieDoelgroepenRegister, AdviesUWV, Baanafspraak | Nee | GGM |
| **Flexibliteit** | De mate waarin een persoon flexibel inzetbaar is qua werktijden, werkplek of werkzaamheden. | IngeschrevenbijUitzendbureau, IndicatieBereidBuitenBeroepswens, IndicatieBereidheidZoekenOnderNiveau, IndicatieBereidheidZwaarWerk, IndicatieBereidheidOnregelmatigWerk | Nee | GGM |
| **Loonkostensubsidie** | Een tegemoetkoming aan een werkgever voor het in dienst nemen van een werknemer met verminderde loonwaarde. | PercentageLoonwaardeWML | Nee | GGM |
| **Mobiliteit** | De bereikbaarheid van werkplekken voor een persoon, afhankelijk van vervoermiddel, rijbewijs en fysieke mogelijkheden. | IndicatieBereidheidVerhuizen, MaximaleReistijd, ToelichtingMaximaleReistijd, CodeVervoermiddel, ToelichtingVervoermiddel | Nee | GGM |
| **Ontheffing** | Een formele vrijstelling van verplichtingen rond arbeidsparticipatie, zoals beschikbaarheid of tegenprestatie, op basis van persoonlijke of juridische gronden. | RedenAanvraag, AanvraagdatumOntheffing, Ontheffingsbesluit, MotivatieOntheffingsbesluit, SoortOntheffing, IngangsdatumOntheffing, EinddatumOntheffing, ResultaatInstrumentbeoordeling, OntheffenVerplichtingen, VersieNummerAanvraag, BijlagenBijAanvraag, BijlagenBijOntheffingsbesluit, HerzieningsdatumOntheffing, MotivatieHerzieningsbesluit, BijlagenBijHerzieningsbesluit | Nee | GGM |
| **Opleiding** | Een formeel of informeel leertraject dat een persoon heeft gevolgd met als doel het verwerven van kennis, vaardigheden of competenties. | Opleidingstype, Instituutnaam, DatumAanvang, DatumEinde, CodeStatusOpleiding, IndicatieDiploma, DatumDiploma, CodeNiveauOpleiding, Opleidingsrichting, CodeLeerwegMBO, AantalJarenOpleiding, CodeTijdsBeslagOpleiding, IndicatieDeeltijdopleiding, ToelichtingBeeindigenOpleiding, Indicatiebuitenlandseopleiding, ToelichtingOpleiding | Nee | GGM |
| **Opleidingsnaam** | De naam waarmee een gevolgde opleiding aangeduid wordt. Dit kan een officiële (gecodeerde) of vrije tekst zijn. | naamOpleiding | Nee | GGM |
| **OpleidingsnaamGecodeerd** | Een OpleidingsnaamGecodeerd is een versleutelde/coderende aanduiding van de naam van een opleiding zoals vastgelegd in onderwijs-microdata, bedoeld om de opleiding te identificeren zonder de volledige tekstuele naam direct in de dataset op te nemen. | CodeOpleidingsnaam, OmschrijvingOpleidingsnaam, CodeSoortOpleidingsnaam, IndicatieOpleidingsnaamActief | Nee | GGM |
| **OpleidingsnaamOngecodeerd** | *OpleidingsnaamOngecodeerd* is de tekstuele naam van een opleiding zoals geregistreerd in CBS-onderwijsdata, weergegeven zonder codering om de opleidingsidentificatie leesbaar te maken. | naamOpleidingOngecodeerd | Nee | GGM |
| **Opleidingsniveau** | Het abstractieniveau waarop de opleiding is ingeschaald, vaak gebaseerd op landelijke of Europese onderwijsclassificaties. | CodeOpleidingsniveauClient | Nee | GGM |
| **Reintegratievoorziening** | Een voorziening of dienst die wordt ingezet om de kansen van een persoon op arbeidsparticipatie te vergroten. | RegistratienummerReintegratievoorziening, DatumStartVoorlopigeToekenning, DatumStart, DatumVerwachtEinde, DatumEinde, DatumIngebruikname, DatumInname, DatumEindeVerlengdeBeslistermijn, CodeType, Omschrijving, OmschrijvingType, ToelichtingOmschrijving | Nee | GGM |
| **Rijbewijs /Certificaat** | Een door een bevoegde instantie afgegeven document dat aangeeft dat een persoon bevoegd is tot het besturen van bepaalde typen voertuigen. | CodeSoortRijbewijs, NummerCertificaat, NaamCertificaat, GeldigVanaf, GeldigTot, VerstrekkendePartij, Beschrijving, IndicatieGeldigheidRijbewijs | Nee | GGM |
| **Taalbeheersing** | Het Europese of Nederlandse taalniveau (zoals A1 t/m C2) waarop de taalvaardigheid van een persoon is ingeschaald. | Taalcode, Taalnaam, Moedertaal, Leesvaardigheid, Schrijfvaardigheid, Spreekvaardigheid | Nee | GGM |
| **TaalbeheersingNederlands** | De mate waarin een persoon de Nederlandse taal beheerst, inclusief mondelinge en schriftelijke vaardigheden. | OntheffingTaaleis, SpreeksvaardigheidNederlands, LuistervaardigheidNederlands, LeesvaardigheidNederlands, SchrijfvaardigheidNederlands, GespreksvaardigheidNederlands | Nee | GGM |
| **Vaardigheidsvaststelling** | Het proces waarin specifieke vaardigheden van een persoon worden beoordeeld of gemeten, vaak ter ondersteuning van een werkprofiel of plaatsingsbeslissing. | datumLaatsteVaststelling, Indicatie mate van vaardigheid | Nee | GGM |
| **Voorkeur** | Voorkeur is een door de klant geuite wens of voorkeur met betrekking tot werk, opleiding of ondersteuning, waarmee bij de invulling van het re-integratie- of participatietraject rekening kan worden gehouden voor zover dit past binnen de wettelijke kaders en mogelijkheden van de gemeente. | BrancheCode, BrancheNaam, SoortBaan, SoortWerk, GegevensWerklocatie, Vervoermiddel, ToelichtingVervoersmiddel, BezitPersoonlijkeOVkaart, NummerOVK, VerloopdatumOVK | Nee | GGM |
| **VrijstellingArbeidsplicht** | Geeft aan of en waarom iemand tijdelijk of structureel is vrijgesteld van de plicht om arbeid te verrichten. | IndicatieVrijstelling, CodeVrijstelling, DatumStart, DatumEinde, CodeRedenVrijheidstelling | Nee | GGM |
| **Werkervaring** | Eerdere functies of werkzaamheden van een persoon, inclusief sector, duur en aard van de werkzaamheden. | Aantal jaren werkzaam in beroep, Toelichting beroep | Nee | GGM |
| **Werkzaamheden als mantelzorger** | Activiteiten die een persoon uitvoert in de rol van mantelzorger, buiten een formele arbeidsverhouding, maar met mogelijke invloed op beschikbaarheid voor arbeid. | Mantelzorgverkalring verstrekt, Mantelzorgovereenkomst afgesloten, Hulp bij medicatie, Toezicht houden, Verzorgde actviteiten, Vervoer en begeleiding, Andere mantelzorgtaken, Te bespreken mantelzorgtaken, Omschrijving andere mantelzorgtaken | Nee | GGM |
| **Werkzaamheden anders dan in arbeidsverhouding** | Taken of activiteiten die een persoon verricht zonder dat sprake is van een formele arbeidsovereenkomst, zoals vrijwilligerswerk of mantelzorg. | Code maatschappelijke context, Omschrijving werkzaamheden, Datum aanvang werkzaamheden, Datum einde werkzaamheden, Omschrijving reden einde werkzaamheden, aantalUrenGemiddeldWeek, Functienaam, PersoonOrganisatieWaarbij, Bedrag netto inkomsten uit Wadia | Nee | GGM |
| **Werkzoekende** | Een generiek werkprofiel van een persoon waarin diens arbeidspositie, bemiddelbaarheid en begeleidingsbehoefte worden vastgelegd, als basis voor begeleiding naar arbeid. | DatumAanvangWerkzoekende, DatumEindeWerkzoekende | Ja | GGM |
| **ZelfredzaamheidScore** | Een gekwantificeerde weergave van het niveau van zelfstandigheid van een persoon op meerdere levensgebieden, vaak volgens de methodiek van de ZRM (Zelfredzaamheidsmatrix). | Domein van Zelfredzaamheid, ZRM score, DatumBeoordeling, KenmerkBeoordelaar, IndicatieHulpAanwezig, Woongemeente | Nee | GGM |

### Diagram Client en Werkzoekende

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Doelgroep** | Een specifieke groep personen met gedeelde kenmerken (zoals afstand tot de arbeidsmarkt) die in aanmerking komt voor bepaalde voorzieningen of aangepaste begeleiding. | naam, omschrijving | Nee | GGM |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Bemiddelingsactiviteit** | Een activiteit in het kader van arbeidstoeleiding waarbij de gemeente of uitvoeringsinstantie gericht handelt om de persoon in contact te brengen met een werkgever of werkplek. | DatumBemiddeling, OmschrijvingSoortContactbemiddeling, OmschrijvingSatutsBemiddeling, OmschrijvingResultaatBemiddeling, DatumVerwijzingVacature, IndicatiePlaatsing | Nee | GGM |

## Overervingshiërarchie

```
Client (abstract)
    └── Werkzoekende
```

```
Opleidingsnaam (abstract)
    └── OpleidingsnaamGecodeerd
    └── OpleidingsnaamOngecodeerd
```

```
Werkzaamheden anders dan in arbeidsverhouding (abstract)
    └── Werkzaamheden als mantelzorger
```

## Relatiediagrammen

```
Arbeidsverhouding [1..1] ──── Arbeidsperiode [1..*]
Arbeidsverhouding [0..*] ──── Werkzoekende [1..1]
Bemiddelingsberoep [0..*] ──── Werkzoekende [1..1]
Opleiding [1..1] ──── Opleidingsnaam [1..1]
OpleidingsnaamGecodeerd [0..*] ──── OpleidingsnaamGecodeerd [1..1]
Opleidingsniveau [1..1] ──── Opleiding [0..*]
Reintegratievoorziening [0..1] ──── Loonkostensubsidie [0..1]
Werkzoekende [1..1] ──── Arbeidsmarktkwalificaties [1..*]
Werkzoekende [1..1] ──── Arbeidsvermogen [1..*]
Werkzoekende [1..1] ──── Bemiddelingstraject [0..*]
Werkzoekende [1..1] ──── BeschikbaarVoorArbeid [0..1]
Werkzoekende [1..1] ──── BeschikbaarVoorBemiddeling [0..*]
Werkzoekende [1..1] ──── DoelReintegratievoorziening [0..1]
Werkzoekende [1..1] ──── Doelgroepenregister [1..*]
Werkzoekende [1..1] ──── Flexibliteit [0..1]
Werkzoekende [1..1] ──── Mobiliteit [0..1]
Werkzoekende [1..1] ──── Ontheffing [0..1]
Werkzoekende [1..1] ──── Opleidingsniveau [0..1]
Werkzoekende [1..1] ──── Reintegratievoorziening [0..*]
Werkzoekende [1..1] ──── Rijbewijs /Certificaat [0..*]
Werkzoekende [1..1] ──── Taalbeheersing [1..*]
Werkzoekende [1..1] ──── TaalbeheersingNederlands [1..1]
Werkzoekende [1..1] ──── Voorkeur [0..*]
Werkzoekende [`1..`1] ──── VrijstellingArbeidsplicht [0..1] (`1)
Werkzoekende [1..1] ──── Werkervaring [0..*]
Werkzoekende [1..1] ──── Werkzaamheden anders dan in arbeidsverhouding [0..*]
Werkzoekende [`1..`1] ──── ZelfredzaamheidScore [1..*] (`1)
```

## Observaties

- Dit beleidsdomein bevat 33 Objecttype-entiteiten (+ 25 Enumeraties).
- Entiteiten zijn gegroepeerd in 2 diagramgroepen: Detaildiagram Werk (31), Diagram Client en Werkzoekende (2).
- Er zijn 4 generalisatierelaties aanwezig.
