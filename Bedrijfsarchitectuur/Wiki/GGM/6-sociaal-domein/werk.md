---
type: ggm-beleidsdomein
naam: Werk
definitie: "Het informatiedomein dat gegevens omvat over de ondersteuning van mensen bij het vinden en behouden van werk, gebaseerd op de Participatiewet en gericht op het bevorderen van arbeidsparticipatie."
taakveld: "6 Sociaal Domein"
aantal_entiteiten: 33
---

# GGM Beleidsdomein: Werk

Beleidsdomein binnen taakveld "6 Sociaal Domein" (zie ../structuur-ggm.md).

## Entiteiten

### Diagram Client en Werkzoekende

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Doelgroep** | <font color="#0e0e0e">Een specifieke groep personen met gedeelde kenmerken (zoals afstand tot de arbeidsmarkt) die in aanmerking komt voor bepaalde voorzieningen of aangepaste begeleiding.</font> | naam, omschrijving | Nee | GGM |
| **Werkzoekende** | <font color="#0e0e0e">Een generiek werkprofiel van een persoon waarin diens arbeidspositie, bemiddelbaarheid en begeleidingsbehoefte worden vastgelegd, als basis voor begeleiding naar arbeid.</font> | DatumAanvangWerkzoekende, DatumEindeWerkzoekende | Ja | GGM |

### Detaildiagram Werk

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Arbeidsmarktkwalificaties** | <font color="#0e0e0e">Een verzameling formele en informele kwalificaties, vaardigheden en eigenschappen die relevant zijn voor de inzetbaarheid van een persoon op de arbeidsmarkt.</font> | KlantTypering, Code taalbeheersing mondeling, Code taalbeheersing schriftelijk, Code werk en denkniveau, ToelichtingArbeidsmarktKwalificaties | Nee | GGM |
| **Arbeidsperiode** | <font color="#0e0e0e">Een aaneengesloten periode waarin een persoon arbeid heeft verricht, met begin- en einddatum.</font> | Datum aanvang arbeidsperiode, Datum einde arbeidsperiode, Gemiddeld aantal uur per week, Functienaam, Functieomschrijving, Contact persoon, Contact email, Contact telefoon | Nee | GGM |
| **Arbeidsverhouding** | <font color="#0e0e0e">Een relatie waarin sprake is van afspraken tussen een werknemer en een werkgever over het verrichten van arbeid.</font> | Datum aanvraag arbeidsverhouding, Datum einde arbeidsverhouding | Nee | GGM |
| **Arbeidsvermogen** | <font color="#0e0e0e">Een inschatting van wat iemand op basis van fysieke, mentale en sociale capaciteiten aan arbeid kan verrichten.</font> | CodeArbeidsvermogen | Nee | GGM |
| **Bemiddelingsberoep** | <font color="#0e0e0e">Het beoogde beroep waarvoor een persoon wordt begeleid of bemiddeld in een traject.</font> | ToelichtingBeroep | Nee | GGM |
| **Bemiddelingstraject** | <font color="#0e0e0e">Een traject waarin een persoon begeleid wordt naar passend werk, bijvoorbeeld door een gemeente of uitvoeringsinstantie.</font> | DatumBemiddeling, OmschrijvingContactbemiddeling, OmschrijvingStatusbemiddeling, OmschrijvingResultaatbemiddeling, DatumVacature, IndicatiePlaatsing | Nee | GGM |
| **BeschikbaarVoorArbeid** | <font color="#0e0e0e">Een indicatie of iemand op dit moment inzetbaar is voor arbeid, los van begeleiding of ondersteuning.</font> | StartdatumBeschikbaarheid, DagBeschikbaarheid, AantalUrenpwBeschikbaar, Interval opzegtermijn, WaardeOpzegtermijn, StartdagBeschikbaarheid, EinddatumBeschikbaarheid, EindtijdDagBeschikbaarheid, ToelichtingBeschikbaarheid, Indicatie nog werkzaam | Nee | GGM |
| **BeschikbaarVoorBemiddeling** | <font color="#0e0e0e">Een indicatie dat een persoon beschikbaar is voor bemiddeling richting arbeid, waarbij wordt gekeken naar inzetbaarheid, bereidheid en eventuele beperkingen.</font> | IndicatieDirectBemiddelbaar, DatumEinde | Nee | GGM |
| **DoelReintegratievoorziening** | <font color="#0e0e0e">Het beoogde effect van een ingezette voorziening, bijvoorbeeld toeleiding naar werk, dagbesteding of maatschappelijke participatie.</font> | CodeDoelReintegratievoorziening | Nee | GGM |
| **Doelgroepenregister** | <font color="#0e0e0e">Een landelijk register waarin mensen met een afstand tot de arbeidsmarkt worden opgenomen, vaak ten behoeve van loonkostensubsidie of andere voorzieningen.</font> | IndicatieDoelgroepenRegister, AdviesUWV, Baanafspraak | Nee | GGM |
| **Flexibliteit** | <font color="#0e0e0e">De mate waarin een persoon flexibel inzetbaar is qua werktijden, werkplek of werkzaamheden.</font> | IngeschrevenbijUitzendbureau, IndicatieBereidBuitenBeroepswens, IndicatieBereidheidZoekenOnderNiveau, IndicatieBereidheidZwaarWerk, IndicatieBereidheidOnregelmatigWerk | Nee | GGM |
| **Loonkostensubsidie** | <font color="#0e0e0e">Een tegemoetkoming aan een werkgever voor het in dienst nemen van een werknemer met verminderde loonwaarde.</font> | PercentageLoonwaardeWML | Nee | GGM |
| **Mobiliteit** | <font color="#0e0e0e">De bereikbaarheid van werkplekken voor een persoon, afhankelijk van vervoermiddel, rijbewijs en fysieke mogelijkheden.</font> | IndicatieBereidheidVerhuizen, MaximaleReistijd, ToelichtingMaximaleReistijd, CodeVervoermiddel, ToelichtingVervoermiddel | Nee | GGM |
| **Ontheffing** | <font color="#0e0e0e">Een formele vrijstelling van verplichtingen rond arbeidsparticipatie, zoals beschikbaarheid of tegenprestatie, op basis van persoonlijke of juridische gronden.</font> | RedenAanvraag, AanvraagdatumOntheffing, Ontheffingsbesluit, MotivatieOntheffingsbesluit, SoortOntheffing, IngangsdatumOntheffing, EinddatumOntheffing, ResultaatInstrumentbeoordeling, OntheffenVerplichtingen, VersieNummerAanvraag, BijlagenBijAanvraag, BijlagenBijOntheffingsbesluit, HerzieningsdatumOntheffing, MotivatieHerzieningsbesluit, BijlagenBijHerzieningsbesluit | Nee | GGM |
| **Opleiding** | <font color="#0e0e0e">Een formeel of informeel leertraject dat een persoon heeft gevolgd met als doel het verwerven van kennis, vaardigheden of competenties.</font> | Opleidingstype, Instituutnaam, DatumAanvang, DatumEinde, CodeStatusOpleiding, IndicatieDiploma, DatumDiploma, CodeNiveauOpleiding, Opleidingsrichting, CodeLeerwegMBO, AantalJarenOpleiding, CodeTijdsBeslagOpleiding, IndicatieDeeltijdopleiding, ToelichtingBeeindigenOpleiding, Indicatiebuitenlandseopleiding, ToelichtingOpleiding | Nee | GGM |
| **Opleidingsnaam** | <font color="#0e0e0e">De naam waarmee een gevolgde opleiding aangeduid wordt. Dit kan een offici&#235;le (gecodeerde) of vrije tekst zijn.</font> | naamOpleiding | Nee | GGM |
| **OpleidingsnaamGecodeerd** | Een OpleidingsnaamGecodeerd is een versleutelde/coderende aanduiding van de naam van een opleiding zoals vastgelegd in onderwijs-microdata, bedoeld om de opleiding te identificeren zonder de volledige tekstuele naam direct in de dataset op te nemen. | CodeOpleidingsnaam, OmschrijvingOpleidingsnaam, CodeSoortOpleidingsnaam, IndicatieOpleidingsnaamActief | Nee | GGM |
| **OpleidingsnaamOngecodeerd** | *OpleidingsnaamOngecodeerd* is de tekstuele naam van een opleiding zoals geregistreerd in CBS-onderwijsdata, weergegeven zonder codering om de opleidingsidentificatie leesbaar te maken. | naamOpleidingOngecodeerd | Nee | GGM |
| **Opleidingsniveau** | <font color="#0e0e0e">Het abstractieniveau waarop de opleiding is ingeschaald, vaak gebaseerd op landelijke of Europese onderwijsclassificaties.</font> | CodeOpleidingsniveauClient | Nee | GGM |
| **Reintegratievoorziening** | <font color="#0e0e0e">Een voorziening of dienst die wordt ingezet om de kansen van een persoon op arbeidsparticipatie te vergroten.</font> | RegistratienummerReintegratievoorziening, DatumStartVoorlopigeToekenning, DatumStart, DatumVerwachtEinde, DatumEinde, DatumIngebruikname, DatumInname, DatumEindeVerlengdeBeslistermijn, CodeType, Omschrijving, OmschrijvingType, ToelichtingOmschrijving | Nee | GGM |
| **Rijbewijs /Certificaat** | <font color="#0e0e0e">Een door een bevoegde instantie afgegeven document dat aangeeft dat een persoon bevoegd is tot het besturen van bepaalde typen voertuigen.</font> | CodeSoortRijbewijs, NummerCertificaat, NaamCertificaat, GeldigVanaf, GeldigTot, VerstrekkendePartij, Beschrijving, IndicatieGeldigheidRijbewijs | Nee | GGM |
| **Taalbeheersing** | <font color="#0e0e0e">Het Europese of Nederlandse taalniveau (zoals A1 t/m C2) waarop de taalvaardigheid van een persoon is ingeschaald.</font> | Taalcode, Taalnaam, Moedertaal, Leesvaardigheid, Schrijfvaardigheid, Spreekvaardigheid | Nee | GGM |
| **TaalbeheersingNederlands** | <font color="#0e0e0e">De mate waarin een persoon de Nederlandse taal beheerst, inclusief mondelinge en schriftelijke vaardigheden.</font> | OntheffingTaaleis, SpreeksvaardigheidNederlands, LuistervaardigheidNederlands, LeesvaardigheidNederlands, SchrijfvaardigheidNederlands, GespreksvaardigheidNederlands | Nee | GGM |
| **Vaardigheidsvaststelling** | <font color="#0e0e0e">Het proces waarin specifieke vaardigheden van een persoon worden beoordeeld of gemeten, vaak ter ondersteuning van een werkprofiel of plaatsingsbeslissing.</font> | datumLaatsteVaststelling, Indicatie mate van vaardigheid | Nee | GGM |
| **Voorkeur** | <font color="#0e0e0e"><b>Voorkeur</b></font><font color="#0e0e0e"> is een door de klant geuite wens of voorkeur met betrekking tot werk, opleiding of ondersteuning, waarmee bij de invulling van het re-integratie- of participatietraject rekening kan worden gehouden voor zover dit past binnen de wettelijke kaders en mogelijkheden van de gemeente.</font> | BrancheCode, BrancheNaam, SoortBaan, SoortWerk, GegevensWerklocatie, Vervoermiddel, ToelichtingVervoersmiddel, BezitPersoonlijkeOVkaart, NummerOVK, VerloopdatumOVK | Nee | GGM |
| **VrijstellingArbeidsplicht** | <font color="#0e0e0e">Geeft aan of en waarom iemand tijdelijk of structureel is vrijgesteld van de plicht om arbeid te verrichten.</font> | IndicatieVrijstelling, CodeVrijstelling, DatumStart, DatumEinde, CodeRedenVrijheidstelling | Nee | GGM |
| **Werkervaring** | <font color="#0e0e0e">Eerdere functies of werkzaamheden van een persoon, inclusief sector, duur en aard van de werkzaamheden.</font> | Aantal jaren werkzaam in beroep, Toelichting beroep | Nee | GGM |
| **Werkzaamheden als mantelzorger** | <font color="#0e0e0e">Activiteiten die een persoon uitvoert in de rol van mantelzorger, buiten een formele arbeidsverhouding, maar met mogelijke invloed op beschikbaarheid voor arbeid.</font> | Mantelzorgverkalring verstrekt, Mantelzorgovereenkomst afgesloten, Hulp bij medicatie, Toezicht houden, Verzorgde actviteiten, Vervoer en begeleiding, Andere mantelzorgtaken, Te bespreken mantelzorgtaken, Omschrijving andere mantelzorgtaken | Nee | GGM |
| **Werkzaamheden anders dan in arbeidsverhouding** | <font color="#0e0e0e">Taken of activiteiten die een persoon verricht zonder dat sprake is van een formele arbeidsovereenkomst, zoals vrijwilligerswerk of mantelzorg.</font> | Code maatschappelijke context, Omschrijving werkzaamheden, Datum aanvang werkzaamheden, Datum einde werkzaamheden, Omschrijving reden einde werkzaamheden, aantalUrenGemiddeldWeek, Functienaam, PersoonOrganisatieWaarbij, Bedrag netto inkomsten uit Wadia | Nee | GGM |
| **ZelfredzaamheidScore** | <font color="#0e0e0e">Een gekwantificeerde weergave van het niveau van zelfstandigheid van een persoon op meerdere levensgebieden, vaak volgens de methodiek van de ZRM (Zelfredzaamheidsmatrix).</font> | Domein van Zelfredzaamheid, ZRM score, DatumBeoordeling, KenmerkBeoordelaar, IndicatieHulpAanwezig, Woongemeente | Nee | GGM |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Bemiddelingsactiviteit** | <font color="#0e0e0e">Een activiteit in het kader van arbeidstoeleiding waarbij de gemeente of uitvoeringsinstantie gericht handelt om de persoon in contact te brengen met een werkgever of werkplek.</font> | DatumBemiddeling, OmschrijvingSoortContactbemiddeling, OmschrijvingSatutsBemiddeling, OmschrijvingResultaatBemiddeling, DatumVerwijzingVacature, IndicatiePlaatsing | Nee | GGM |

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

### Diagram Client en Werkzoekende

```
Arbeidsverhouding [0..*] ──── Werkzoekende [1]
Bemiddelingsberoep [0..*] ──── Werkzoekende [1]
Client [0..*] ──── Doelgroep [0..*] (valt binnen)
Werkzoekende [1] ──── Arbeidsmarktkwalificaties [1..*]
Werkzoekende [1] ──── Arbeidsvermogen [1..*]
Werkzoekende [1] ──── Bemiddelingstraject [0..*]
Werkzoekende [1] ──── BeschikbaarVoorArbeid [0..1]
Werkzoekende [1] ──── BeschikbaarVoorBemiddeling [0..*]
Werkzoekende [1] ──── DoelReintegratievoorziening [0..1]
Werkzoekende [1] ──── Doelgroepenregister [1..*]
Werkzoekende [1] ──── Flexibliteit [0..1]
Werkzoekende [1] ──── Mobiliteit [0..1]
Werkzoekende [1] ──── Ontheffing [0..1]
Werkzoekende [1] ──── Opleidingsniveau [0..1]
Werkzoekende [1] ──── Reintegratievoorziening [0..*]
Werkzoekende [1] ──── Rijbewijs /Certificaat [0..*]
Werkzoekende [1] ──── Taalbeheersing [1..*]
Werkzoekende [1] ──── TaalbeheersingNederlands [1]
Werkzoekende [1] ──── Voorkeur [0..*]
Werkzoekende [`1] ──── VrijstellingArbeidsplicht [0..1]
Werkzoekende [1] ──── Werkervaring [0..*]
Werkzoekende [1] ──── Werkzaamheden anders dan in arbeidsverhouding [0..*]
Werkzoekende [`1] ──── ZelfredzaamheidScore [1..*]
```

### Detaildiagram Werk

```
Arbeidsverhouding [1] ──── Arbeidsperiode [1..*]
Arbeidsverhouding [0..*] ──── Werkzoekende [1]
Bemiddelingsberoep [0..*] ──── Werkzoekende [1]
Opleiding [1] ──── Opleidingsnaam [1]
OpleidingsnaamGecodeerd [0..*] ──── OpleidingsnaamGecodeerd [1] (heeft synoniem)
Opleidingsniveau [1] ──── Opleiding [0..*]
Reintegratievoorziening [0..1] ──── Loonkostensubsidie [0..1]
Werkzoekende [1] ──── Arbeidsmarktkwalificaties [1..*]
Werkzoekende [1] ──── Arbeidsvermogen [1..*]
Werkzoekende [1] ──── Bemiddelingstraject [0..*]
Werkzoekende [1] ──── BeschikbaarVoorArbeid [0..1]
Werkzoekende [1] ──── BeschikbaarVoorBemiddeling [0..*]
Werkzoekende [1] ──── DoelReintegratievoorziening [0..1]
Werkzoekende [1] ──── Doelgroepenregister [1..*]
Werkzoekende [1] ──── Flexibliteit [0..1]
Werkzoekende [1] ──── Mobiliteit [0..1]
Werkzoekende [1] ──── Ontheffing [0..1]
Werkzoekende [1] ──── Opleidingsniveau [0..1]
Werkzoekende [1] ──── Reintegratievoorziening [0..*]
Werkzoekende [1] ──── Rijbewijs /Certificaat [0..*]
Werkzoekende [1] ──── Taalbeheersing [1..*]
Werkzoekende [1] ──── TaalbeheersingNederlands [1]
Werkzoekende [1] ──── Voorkeur [0..*]
Werkzoekende [`1] ──── VrijstellingArbeidsplicht [0..1]
Werkzoekende [1] ──── Werkervaring [0..*]
Werkzoekende [1] ──── Werkzaamheden anders dan in arbeidsverhouding [0..*]
Werkzoekende [`1] ──── ZelfredzaamheidScore [1..*]
```

## Observaties

- Dit beleidsdomein bevat 33 entiteiten.
- Entiteiten zijn gegroepeerd in 3 diagramgroepen: Diagram Client en Werkzoekende (2), Detaildiagram Werk (30), Overig (1).
- Er zijn 4 generalisatierelaties aanwezig.
- 1 entiteit is abstract.
