---
type: ggm-beleidsdomein
naam: RSGBPlus
definitie: "Het subdomein dat gegevens omvat over gemeentelijke basisgegevens, gebaseerd op het Referentiemodel Stelsel van Gemeentelijke Basisgegevens (RSGB) v2.0.2, aangevuld met specifieke uitbreidingen voor lokaal gebruik en aanvullingen uit RSGB v3.0."
taakveld: "99 Kern"
aantal_entiteiten: 135
---

# GGM Beleidsdomein: RSGBPlus

Beleidsdomein binnen taakveld "99 Kern" (zie ../structuur-ggm.md).

## Entiteiten

### Kern:Personen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **AdresBuitenland** | Toevoeging uit stelselcatalogus | datumAanvangAdresBuitenland, datumInschrijvingGemeente, datumVestigingNederland, gemeenteVanInschrijving, landAdresBuitenland, landWaarvandaanIngeschreven, omschrijvingVanDeAangifteAdreshouding, adresregelBuitenland1, adresregelBuitenland2, adresregelBuitenland3 | Nee | GGM |
| **Huishouden** | Een duurzame samenlevingsvorm van een of meer natuurlijke personen binnen een VERBLIJFSOBJECT, STANDPLAATS of LIGPLAATS. | huishoudensoort, huishoudennummer, huishoudengrootte, datumBeginGeldigheidHuishouden, datumEindeGeldigheidHuishouden, relatie, relatie | Nee | GGM |
| **IngeschrevenPersoon** | Een INGEZETENE of NIET-INGEZETENE | adresHerkomst, anummer, beschrijvingLocatie, burgerlijkeStaat, indicatieGeheim, gemeenteVanInschrijving, landWaarvandaanIngeschreven, landWaarnaarVertrokken, datumInschrijvingGemeente, datumBeginGeldigheidVerblijfplaats, signaleringReisdocument, buitenlandsReisdocument, datumVestigingNederland, datumVertrekUitNederland, redenOpschortingBijhouding, datumOpschortingBijhouding, ingezetene, datumEindeGeldigheidVerblijfsplaats, redenEindeBewoning, verblijfstitel, ouder1, gezinsrelatie, ouder2, partnerID | Ja | GGM |
| **Ingezetene** | Een individueel menselijk wezen, ingeschreven in het Nederlands Bevolkingsregister. | aanduidingUitgeslotenKiesrecht, aanduidingEuropeesKiesrecht, indicatieCurateleregister, indicatieGezagMinderjarige, datumVerkrijgingVerblijfstitel, datumVerliesVerblijfstitel, indicatieBlokkering | Nee | GGM |
| **Nationaliteit** | De hoedanigheid van tot een bepaalde natie te behoren. Het wettelijk onderdaan zijn van een bepaalde staat (staatsburgerschap). Nationale oorsprong. De rechtsverhouding tussen de betrokkene en de staat. | omschrijving, Nationaliteitcode, Datum ingang geldigheid, Datum einde geldigheid, Datum opnamen, Datum verlies nationaliteit, redenVerliesNLNationaliteit, redenVerkrijgingNLNationaliteit, Buitenlandse nationaliteit | Nee | GGM |
| **NatuurlijkPersoon** | Een INGESCHREVEN PERSOON of ANDER NATUURLIJK PERSOON | aanduidingNaamgebruik, geslachtsnaamAanschrijving, voornamen, academischeTitel, datumGeboorte, geboorteplaats, geslachtsnaam, overlijdensplaats, voorlettersAanschrijving, datumOverlijden, geboorteland, geslachtsaanduiding, landOverlijden, voornamenAanschrijving, voorvoegselGeslachtsnaam, aanhefAanschrijving, adellijkeTitelOfPredikaat, burgerservicenummer, handlichting, achternaam, nationaliteit, bijzonderNederlanderschap, anummer, indicatieOverleden, IndicatieAfschermingPersoonsgegevens | Ja | GGM |
| **NietNatuurlijkPersoon** | Een INGESCHREVEN NIET-NATUURLIJK PERSOON of een ANDER BUITENLANDS NIET-NATUURLIJK PERSOON | NNPID, statutaireNaam, datumAanvang, rechtsvorm, datumEinde, statutaireZetel, datumVoortzetting, faxnummer, KVKnummer, ingeschreven, RSINNummer, datumUitschrijving, websiteURL, inOprichting | Ja | GGM |
| **Rechtspersoon** | Een NATUURLIJK PERSOON of een NIET-NATUURLIJK PERSOON | adresBinnenland, adresBuitenland, rekeningnummer, emailadres, faxnummer, identificatie, naam, KVKnummer, rechtsvorm, telefoonnummer, adresCorrespondentie | Ja | GGM |
| **Verblijfstitel** | Rechtsgrond op basis waarvan men bevoegd is in een land te verblijven. Opmerkingen obv Key2Burgerzaken: De verblijfstitel heeft een ingangs- en vervaldatum, datum geldig en een opname datum RSGB3.0 onderkent alleen Datum einde en Datum ingang. Dat is onvoldoende om volgorde en geldigheid in tijd correct te bepalen | aanduidingVerblijfstitel, datumBeginGeldigheidVerblijfstitel, Verblijfstitel code, Datum begin, Datum einde, Datum Opname | Nee | GGM |

### Kern:Overige geo objecten op hoofdlijnen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **BegroeidTerreindeel** | Kleinste functioneel onafhankelijk stukje van een terrein dat er binnen het objecttype Terrein van NEN 3610 wordt onderscheiden, met aaneengesloten homogene vegetatie. | identificatie, status, relatieveHoogteligging, fysiekVoorkomen, plusFysiekVoorkomen, kruinlijngeometrie, geometrie, LOD0Geometrie, opTalud, datumBeginGeldigheid, datumEindeGeldigheid | Nee | GGM |
| **FunctioneelGebied** | Begrensd en benoemd gebied dat door een functionele eenheid beschreven wordt. | identificatieFunctioneelGebied, statusFunctioneelGebied, naamFunctioneelGebied, geometrieFunctioneelGebied, datumBeginGeldigheidFunctioneelGebied, datumEindeGeldigheidFunctioneelGebied | Nee | GGM |
| **Gebouwinstallatie** | Een component aan de buitenzijde van een gebouw, die het aanzicht van het gebouw mede bepaalt. | identificatieGebouwinstallatie, statusGebouwinstallatie, geometrieGebouwinstallatie, typeGebouwinstallatie, LOD0GeometrieGebouwinstallatie, relatieveHoogteliggingGebouwinstallatie, datumBeginGeldigheidGebouwinstallatie, datumEindeGeldigheidGebouwinstallatie | Nee | GGM |
| **Inrichtingselement** | Ruimtelijk object al dan niet ter detaillering dan wel ter inrichting van de overige benoemde ruimtelijke objecten of een ander inrichtingselement. | identificatieInrichtingselement, statusInrichtingselement, geometrieInrichtingselement, typeInrichtingselement, plusTypeInrichtingselement, relatieveHoogteliggingInrichtingselement, LOD0GeometrieInrichtingselement, datumBeginGeldigheidInrichtingselement, datumEindeGeldigheidInrichtingselement | Nee | GGM |
| **OnbegroeidTerreindeel** | Kleinste functioneel onafhankelijk stukje van een terrein, dat er binnen het objecttype Terrein van NEN 3610 wordt onderscheiden, zonder aaneengesloten vegetatie. | identificatie, status, relatieveHoogteligging, fysiekVoorkomen, plusFysiekVoorkomen, geometrie, kruinlijngeometrie, onbegroeidTerreindeelOpTalud, datumBeginGeldigheid, datumEindeGeldigheid | Nee | GGM |
| **OverigBouwwerk** | Met de aarde verbonden duurzaam bouwwerk, dat niet valt onder de definities van een pand of kunstwerk. | identificatieOverigBouwwerk, statusOverigBouwwerk, relatieveHoogteliggingOverigBouwwerk, geometrieOverigBouwwerk, LOD0GeometrieOverigBouwwerk, LOD1GeometrieOverigBouwwerk, LOD2GeometrieOverigBouwwerk, lod3GeometrieOverigBouwwerk, datumBeginGeldigheidOverigBouwwerk, datumEindeGeldigheidOverigBouwwerk | Nee | GGM |
| **OverigeGeoObjecten** | *OverigeGeoObjecten* zijn geo-objecttypen binnen een gemeentelijk gegevensmodel die **niet onder de standaard geo-objectcategorieën vallen maar toch ruimtelijke objectinformatie bevatten**, zoals aanvullende of aanvullende geografische entiteiten buiten de reguliere standaardobjecten. | *(geen attributen)* | Nee | GGM |
| **OverigeScheiding** | Kunstmatig, meestal lineair obstakel met een werende functie, met kleinere afmetingen dan toegestaan voor opname in de BGT. | identificatieOverigeScheiding, statusOverigeScheiding, relatieveHoogteliggingOverigeScheiding, geometrieOverigeScheiding, typeOverigeScheiding, LOD0GeometrieOverigeScheiding, LOD1GeometrieOverigeScheiding, LOD2GeometrieOverigeScheiding, lod3GeometrieOverigeScheiding, datumBeginGeldigheidOverigeScheiding, datumEindeGeldigheidOverigeScheiding | Nee | GGM |
| **Scheiding** | Kunstmatig, meestal lineair obstakel met een werende functie. | identificatieScheiding, statusScheiding, relatieveHoogteliggingScheiding, geometrieScheiding, LOD0GeometrieScheiding, LOD1GeometrieScheiding, LOD2GeometrieScheiding, lod3GeometrieScheiding, datumBeginGeldigheidScheiding, datumEindeGeldigheidScheiding | Nee | GGM |
| **Vegetatieobject** | Solitair vegetatieobject of lijn- of vlakvormige groep gelijksoortige vegetatieobjecten met een beperkte omvang. | identificatieVegetatieobject, statusVegetatieobject, typeVegetatieobject, relatieveHoogteliggingVegetatieobject, geometrieVegetatieobject, LOD0GeometrieVegetatieobject, datumBeginGeldigheidVegetatieobject, datumEindeGeldigheidVegetatieobject | Nee | GGM |

### Diagram Adresaanduiding en BAG

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Adresaanduiding** | De adresaanduiding van het WOZ-OBJECT | straatnaam, gemeentenaam, huisnummer, huisletter, huisnummertoevoeging, postcode, BAGID | Nee | GGM |

### Diagram Gebied Vestiging en Adres

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Briefadres** | Een briefadres is een adres waar door de overheid verzonden stukken voor een persoon in ontvangst wordt genomen. | datumAanvang, datumEinde, omschrijvingAangifte, adresFunctie | Nee | GGM |
| **Gebied** | Een aaneengesloten gedeelte van een wijk, waarvan de grenzen zo veel mogelijk gebaseerd zijn op topografische elementen. | gebiedcode, identificatieIMGeoBRT, naam, geometrie, datumBeginGeldigheidBuurt, datumEindeGeldigheidGebied, gebiedsoort | Nee | GGM |
| **Vestiging** | Een gebouw of complex van gebouwen waar duurzame uitoefening van de activiteiten van een onderneming of rechtspersoon plaatsvindt. | vestigingsnummer, handelsnaam, verkorteNaam, datumAanvang, datumEinde, datumVoortzetting, toevoegingAdres, fulltimeWerkzameMannen, parttimeWerkzameMannen, fulltimeWerkzameVrouwen, parttimeWerkzameVrouwen, commercieleVestiging, totaalWerkzamePersonen | Nee | NHR |

### Tenaamstelling

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Aantekening** | Een Aantekening is een aanvulling op de registratie van een registergoed met betrekking tot feiten die gevolgen kunnen hebben voor de uitoefening van de rechten op dit registergoed. | aard, begrenzing, betreftGedeelteVanPerceel, datumEinde, datumEindeRecht, identificatie, omschrijving | Nee | GGM |
| **Tenaamstelling** | Een TENAAMSTELLING vormt de relatie tussen een Recht en een Persoon en geeft aan welk recht, met uitzondering van hypotheek en beslag, door een Persoon wordt uitgeoefend op een Kadastraal object. | identificatieTenaamstelling, aandeelInRecht, verkregenNamensSamenwerkingsverband, exploitantcode, datumBeginGeldigheid, datumEindeGeldigheid, burgerlijkeStaatTenTijdeVanVerkrijging, verklaringInzakeDerdenBescherming | Nee | BRK |

### Overige geo objecten op hoofdlijnen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Kunstwerkdeel** | Onderdeel van een civiel-technisch werk voor de infrastructuur van wegen, water, spoorbanen, waterkeringen en/of leidingen. | identificatieKunstwerkdeel, statusKunstwerkdeel, relatieveHoogteliggingKunstwerkdeel, geometrieKunstwerkdeel, LOD0GeometrieKunstwerkdeel, LOD1GeometrieKunstwerkdeel, LOD2GeometrieKunstwerkdeel, lod3GeometrieKunstwerkdeel, datumBeginGeldigheidKunstwerkdeel, datumEindeGeldigheidKunstwerkdeel | Nee | GGM |
| **OndersteunendWaterdeel** | Object dat in het kader van de waterhuishouding periodiek gedeeltelijk of geheel met water is bedekt. | identificatie, status, geometrie, relatieveHoogteligging, type, plusType, datumBeginGeldigheid, datumEindeGeldigheid | Nee | GGM |
| **OndersteunendWegdeel** | Een deel van de weg dat niet primair bedoeld is voor gebruik door het verkeer. | identificatie, status, geometrie, relatieveHoogteligging, kruinlijngeometrie, LOD0Geometrie, functie, plusFunctie, fysiekVoorkomen, plusFysiekVoorkomen, opTalud, datumBeginGeldigheid, datumEindeGeldigheid | Nee | GGM |
| **Overbruggingsdeel** | Onderdeel van een beweegbare of vaste verbinding tussen twee punten, die door water, een weg of anderszins gescheiden zijn, dat essentieel is voor de constructie. | identificatieOverbruggingsdeel, statusOverbruggingsdeel, relatieveHoogteliggingOverbruggingsdeel, typeOverbruggingsdeel, hoortBijTypeOverbrugging, overbruggingIsBeweegbaar, geometrieOverbruggingsdeel, LOD0GeometrieOverbruggingsdeel, datumBeginGeldigheidOverbruggingsdeel, datumEindeGeldigheidOverbruggingsdeel | Nee | GGM |
| **Spoor** | De as van het spoor, dat wil zeggen het midden van twee stalen staven op een onderling vaste afstand, waarover trein, tram, of sneltram rijdt. | identificatieSpoor, statusSpoor, relatieveHoogteliggingSpoor, geometrieSpoor, LOD0GeometrieSpoor, datumBeginGeldigheidSpoor, datumEindeGeldigheidSpoor | Nee | GGM |
| **Tunneldeel** | Onderdeel van een kunstmatig aangelegde, kokervormige onderdoorgang, dat essentieel is voor de constructie. | identificatieTunneldeel, statusTunneldeel, relatieveHoogteliggingTunneldeel, geometrieTunneldeel, LOD0GeometrieTunneldeel, datumBeginGeldigheidTunneldeel, datumEindeGeldigheidTunneldeel | Nee | GGM |
| **Waterdeel** | Kleinste functioneel onafhankelijk stukje water met gelijkblijvende, homogene eigenschappen en relaties dat er binnen het objecttype Water van NEN 3610 wordt onderscheiden. | identificatieWaterdeel, statusWaterdeel, relatieveHoogteliggingWaterdeel, geometrieWaterdeel, typeWaterdeel, plusTypeWaterdeel, datumBeginGeldigheidWaterdeel, datumEindeGeldigheidWaterdeel | Nee | GGM |
| **Wegdeel** | Kleinste functioneel onafhankelijk stukje van een NEN 3610 Weg, met gelijkblijvende homogene eigenschappen en relaties en primair bedoeld voor gebruik door weg-, spoor- en vliegverkeer te land | identificatieWegdeel, statusWegdeel, relatieveHoogteliggingWegdeel, geometrieWegdeel, kruinlijngeometrieWegdeel, LOD0GeometrieWegdeel, functieWegdeel, plusFunctieWegdeel, fysiekVoorkomenWegdeel, plusFysiekVoorkomenWegdeel, wegdeelOpTalud, datumBeginGeldigheidWegdeel, datumEindeGeldigheidWegdeel | Nee | GGM |

### Detaillering adressen, gebouwen en terreinen op hoofdlijnen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **OverigBenoemdTerrein** | Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen onbebouwd terrein of een gedeelte daarvan, geen standplaats of gedeelte van een ligplaats zijnde, dat bestemd is voor het gedurende langere tijd verrichten van een maatschappelijke activiteit. | overigBenoemdTerreinIdentificatie, gebruiksdoelOverigBenoemdTerrein | Nee | GGM |
| **OverigGebouwdObject** | De kleinste eenheid van gebruik, geen verblijfsobject zijnde, binnen een bij de totstandkoming functioneel en bouwkundig constructief zelfstandige eenheid die direct en duurzaam met de aarde is verbonden. | overigGebouwdObjectIdentificatie, bouwjaar, indicatiePlanobject | Nee | GGM |
| **OverigeAdresseerbaarObjectAanduiding** | Een door de gemeenteraad als zodanig toegekende aanduiding van een overig gebouwd object of een overig benoemd terrein. | Identificatiecode | Nee | Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie). |

### Detaillering Kadastrale Onroerende Zaken en Rechten op hoofdlijnen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Appartementsrecht** | Een KADASTRALE ONROERENDE ZAAK dat een aandeel is in de goederen die in de splitsing zijn betrokken, dat de bevoegdheid omvat tot het uitsluitend gebruik van bepaalde gedeelten van het gebouw die blijkens hun inrichting bestemd zijn of worden om als afzonderlijk geheel te worden gebruikt (art. 5:106 lid 4 BW). | *(geen attributen)* | Nee | BRK |
| **Appartementsrechtsplitsing** | Het recht op een stuk grond of op een gebouw met toebehoren op de daarbij behorende grond met toebehoren is gesplitst in appartementsrechten. | ddentificatieAppartementsrechtsplitsing, typeSplitsing | Nee | BRK |
| **KadastraalPerceel** | Een KADASTRALE ONROERENDE ZAAK dat een kadastraal geïdentificeerd en met kadastrale grenzen begrensd deel van het Nederlands grondgebied betreft (art. 1 lid 1 Kadasterwet). | begrenzingPerceel, indicatieDeelperceel, omschrijvingDeelperceel, groottePerceel, aanduidingSoortGrootte, plaatscoordinatenPerceel | Nee | BRK. |
| **KadastraleOnroerendeZaak** | Een geregistreerd goed waarvoor bij overdracht of vestiging van rechten inschrijving in de openbare registers van het Kadaster is vereist zijnde een KADASTRAAL PERCEEL of een APPARTEMENTSRECHT. | kadastraleGemeentecode, landInrichtingRenteBedrag, landInrichtingRenteEindejaar, perceelnummer, kadastraleGemeente, sectie, appartementsrechtvolgnummer, datumBeginGeldigheid, datumEindeGeldigheid, oppervlakte, identificatie, locatieOmschrijving, koopsom, koopjaar, cultuurcodeOnbebouwd, ligging, valutacode, begrenzing, oud, oud | Ja | BRK |
| **KadastraleOnroerendeZaakAantekening** | Aanduiding van het feit, genoemd in een Stuk, dat betrekking heeft op een onroerende zaak en dat gevolgen kan hebben voor de uitoefening van rechten op de onroerende zaak. | kadasterIdentificatieAantekening, aardAantekeningKadastraalObject, beschrijvingAantekeningKadastraalObject, datumBeginAantekeningKadastraalObject, datumEindeAantekeningKadastraalObject | Nee | BRK |
| **ZakelijkRecht** | Het eigendom van, of een beperkt recht van een natuurlijk of niet-natuurlijk persoon (PERSOON) op, een onroerende zaak (met uitzondering van hypotheken en beslagen). | identificatieZakelijkRecht, aardZakelijkRecht, datumIngangRecht, datumEindeRecht, toelichtingBewaarder | Nee | BRK |
| **Zekerheidsrecht** | Een zekerheidsrecht is een beperkt recht (hypotheek) of een beperking (beslag). | identificatieZekerheidsrecht, omschrijvingBetrokkenRecht, typeZekerheidsrecht, aandeelInBetrokkenRecht, datumIngangRecht, datumEindeRecht | Nee | BRK |

### Detaillering subjecten op hoofdlijnen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **MaatschappelijkeActiviteit** | Een verband tussen één of meer personen met voldoende mate van zelfstandigheid, inbreng van arbeid of middelen, winstoogmerk en extern optreden (i.g.v. een onderneming) dan wel een in een organisatorisch verband, dat toebehoort aan een niet-natuurlijk persoon welke registratieplichtig is, uitgeoefende activiteit die niet valt onder de criteria voor onderneming of bedrijfsmatigheid welke adresseerbaar is middels ofwel een vestiging ofwel het adres van een bepaalde vertegenwoordiger (i.g.v. een niet-ondernemings-activiteit). | KVKnummer, datumAanvang, datumEindeGeldig, indicatieEconomischActief, statutaireNaam, rechtsvorm, URL, RSIN, adresBinnenland, adresCorrespondentie, telefoonnummer, datumFaillisement | Nee | NHR |
| **Reisdocument** | Een document dat vereist is voor reizen naar het buitenland | soort, reisdocumentnummer, datumUitgifte, autoriteitVanAfgifte, datumIngangDocument, datumEindeGeldigheidDocument, datumInhoudingOfVermissing, aanduidingInhoudingVermissing | Nee | BRP |

### Detaillering WOZ-objecttypen op hoofdlijnen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **WOZ-Waarde** | De op grond van de Wet WOZ vastgestelde waarde van het WOZ-object naar de genoemde waardepeildatum. | datumWaardepeiling, vastgesteldeWaarde, datumPeilingToestand, statusBeschikking | Nee | GGM |
| **WOZ-deelobject** | Aanduiding van afzonderlijke elementen (delen van het object, bijzondere waarderelevante factoren) die voor de onderbouwing van de vastgestelde waarde van belang zijn. | WOZDeelobjectNummer, codeWOZDeelobject, statusWOZDeelobject, datumBeginGeldigheidDeelobject, datumEindeGeldigheidDeelobject | Nee | Gegevenswoordenboek WOZ |
| **WOZ-object** | De onroerende zaak waarvan op grond van de Wet WOZ de waarde moet worden bepaald en vastgesteld. | WOZObjectnummer, geometrieWOZObject, statusWOZObject, grondoppervlakte, gebruikscode, soortobjectcode, vastgesteldeWaarde, datumWaardepeiling, datumBeginGeldigheidWOZObject, datumEindeGeldigheidWOZObject | Nee | BRWOZ |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **AanduidingVerblijfsrecht** | Aanduiding in verband met het verblijfsrecht van de vreemdeling. | verblijfsrechtnummer, verblijfsrechtomschrijving, datumAanvangGeldigheidVerblijfsrecht, datumEindeGeldigheidVerblijfsrecht | Nee | BRP |
| **AardAantekening** | Een opsomming van de diverse aarden van de aantekeningen zoals door de Dienst Kadaster is onderscheiden. | codeAardAantekening, naamAardAantekening, datumBeginGeldigheidAardAantekening, datumEindeGeldigheidAardAantekening | Nee | GGM |
| **AardFiliatie** | Een opsomming van redenen waarom kadastrale onroerende zaken aan elkaar gerelateerd kunnen zijn | codeAardFiliatie, naamAardFiliatie, datumBeginGeldigheidAardFiliatie, datumEindeGeldigheidAardFiliatie | Nee | GGM |
| **AardZakelijkRecht** | Een opsomming van de diverse aarden van het zakelijk rechten zoals door de Dienst Kadaster is onderscheiden. | codeAardZakelijkRecht, naamAardZakelijkRecht, datumBeginGeldigheidAardZakelijkRecht, datumEindeGeldigheidAardZakelijkRecht | Nee | GGM |
| **AcademischeTitel** | Een formeel via het Staatsblad gepubliceerde aanduiding van een wetenschappelijke of andere graad van opleiding welke bij aanschrijving voorafgaat aan de voornamen (dan wel de daarvan afgeleide naamgegevens) dan wel volgt op de achternaam. | codeAcademischeTitel, omschrijvingAcademischeTitel, positieAcademischeTitelTOVNaam, datumBeginGeldigheidTitel, datumEindeGeldigheidTitel | Nee | GGM |
| **AdresseerbaarObjectAanduiding** | Een door het bevoegde gemeentelijke orgaan als zodanig toegekende aanduiding van een VERBLIJFSOBJECT, een STANDPLAATS of een LIGPLAATS. | identificatie | Nee | BAG |
| **AkrKadastraleGemeentecode** | De door de Dienst Kadaster onderkende AKR codes voor kadastrale gemeenten | codeAKRKadadastraleGemeentecode, AKRCode, datumBeginGeldigheidAKRCode, datumEindeGeldigheidAKRCode | Nee | BRK |
| **AutoriteitAfgifteNederlandsReisdocument** | Een opsomming van de diverse coderingen van de autoriteiten die een Nederlands reisdocument kunnen afgegeven | code, omschrijving, datumBeginGeldigheidAutoriteitVanAfgifte, datumEindeGeldigheidAutoriteitVanAfgifte | Nee | BRP |
| **BenoemdObject** | Een GEBOUWD OBJECT of een BENOEMD TERREIN | identificatie, datumBeginGeldigheid, datumEindeGeldigheid, geometriePunt, geometrieVlak | Ja | KING |
| **BenoemdTerrein** | Een STANDPLAATS, LIGPLAATS, of een OVERIG BENOEMD TERREIN. | identificatie | Ja | Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie). |
| **Buurt** | Een aaneengesloten gedeelte van een wijk, waarvan de grenzen zo veel mogelijk gebaseerd zijn op topografische elementen. | buurtcode, identificatieIMGeoBRT, buurtnaam, buurtgeometrie, datumBeginGeldigheidBuurt, datumEindeGeldigheidBuurt, identificatie | Nee | GFO BG |
| **CorrespondentieadresBuitenland** | De gegevens over het buitenlands correspondentie (-post)adres in het buitenland | adresBuitenland1, adresBuitenland2, adresBuitenland3, adresBuitenland4, adresBuitenland5, adresBuitenland6, landCorrespondentieadres | Nee | GGM |
| **CultuurcodeBebouwd** | De mogelijke cultuurcodes bebouwd conform de waardelijst Cultuurcode Bebouwd van het Kadaster | code, naamCultuurcodeBebouwd, datumBeginGeldigheidCultuurcodeBebouwd, datumEindeGeldigheidCultuurcodeBebouwd | Nee | BRK |
| **CultuurcodeOnbebouwd** | De mogelijke cultuurcodes bebouwd conform de waardelijst Cultuurcode Bebouwd van het Kadaster | code, naamCultuurcodeOnbebouwd, datumBeginGeldigheidCultuurcodeOnbebouwd, datumEindeGeldigheidCultuurcodeOnbebouwd | Nee | BRK |
| **DetailleringAdressenGebouwenEnTerreinen** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **DetailleringKadastraleOnroerendZaken** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **DetailleringSubjecten** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **DetailleringWOZObjecttypen** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **GeboorteIngeschrevenNatuurlijkPersoon** | Gegevens over de geboorte van de INGESCHREVEN NATUURLIJK PERSOON. | datumGeboorte, gemeenteGeboorte, buitenlandsePlaatsGeboorte, buitenlandseRegioGeboorte, landOfGebiedGeboorte, omschrijvingLocatieGeboorte | Nee | GGM |
| **GeboorteIngeschrevenPersoon** | Gegevens over de geboorte van de ingeschreven persoon. | datumGeboorte, geboorteplaats, geboorteland | Nee | GGM |
| **GebouwdObject** | Een VERBLIJFSOBJECT of een OVERIG GEBOUWD OBJECT | bouwkundigeBestemmingActueel, statusVoortgangBouw, brutoInhoud, oppervlakteObject, inwinningOppervlakte, identificatie | Ja | Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie). |
| **Gemeente** | Een gedeelte van het grondgebied van Nederland, ingesteld op basis van artikel 123 van de Grondwet. | gemeentecode, gemeentenaam, gemeentenaamNEN, gemeenteGeometrie, datumBeginGeldigheidGemeente, datumEindeGeldigheidGemeente, identificatie | Nee | Door KING toegevoegd objecttype, ontleend aan het GFO BG (maakt geen deel uit van enige basisregistratie). |
| **HandelsnamenMaatschappelijkeActiviteit** | {nog niet in NHR uitgewerkt} | handelsnaam, verkorteNaam, volgorde | Nee | GGM |
| **HandelsnamenVestiging** | {nog niet in NHR uitgewerkt} | handelsnaam, verkorteNaam, volgorde | Nee | GGM |
| **KadastraleGemeente** | De mogelijke onderscheiden gedeeltes van het grondgebied van Nederland, volgens de Dienst Kadaster en de Openbare Registers, zoals nader omschreven in het Kadasterbesluit | kadastraleGemeentecode, naam, datumBeginGeldigheidKadastraleGemeente, datumEindeGeldigheidKadastraleGemeente | Nee | BRK |
| **KoopsomKadastraleOnroerendeZaak** | Het in een ter inschrijving aangeboden stuk vermelde bedrag, waarvoor 1 of meer onroerende zaken zijn verkregen. | koopsom, datumTransactie | Nee | GGM |
| **Land** | Een gedeelte van de wereld met een eigen bestuur, waarvan de soevereiniteit in ieder geval door Nederland is erkend. | landcode, landnaam, datumIngangLand, datumEindeLand, landcodeISOTweeletterig, datumEindeFictief, landcodeISODrieletterig | Nee | GGM |
| **LandOfgebied** | Een gedeelte van de wereld met een eigen bestuur, waarvan de soevereiniteit in ieder geval door Nederland is erkend. | landcode, landnaam, datumIngangLand, datumEindeLand, landcodeISO | Nee | GFO BG |
| **Ligplaats** | Definitie Een ligplaats is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen plaats in het water al dan niet aangevuld met een op de oever aanwezig terrein of een gedeelte daarvan, die bestemd is voor het permanent afmeren van een voor woon-, bedrijfsmatige of recreatieve doeleinden geschikt drijvend object Beschrijving Een plaats in het water met soms ook een (deel van een) terrein op de oever. Deze plaats moet kunnen worden gebruikt door een drijvend object dat langere tijd daar wordt vastgemaakt. Het drijvende object moet geschikt zijn om in te wonen, om een bedrijf in te hebben of om voor plezier in te verblijven. Bijvoorbeeld een woonboot. De gemeente mag zeggen of er voor de BAG ergens een ligplaats komt. | ligplaatsidentificatie, indicatieGeconstateerdeLigplaats, ligplaatsstatus, inOnderzoek, datumDocument, documentNummer | Nee | GGM |
| **LocatieKadastraleOnroerendeZaak** | Deze wordt gebruikt om één of meer locatieaanduiding(en) van een onroerende zaak weer te geven. | locatieOmschrijving, aardCultuurBebouwd | Nee | GGM |
| **LocatieaanduidingAdresWOZObject** | Nadere aanduiding van het WOZ-object middels een locatieomschrijving van ADRESSEERBAAR OBJECT AANDUIDING. | locatieOmschrijving | Nee | GGM |
| **MigratieIngeschrevenNatuurlijkPersoon** | Om gegevens vast te leggen over immigratie en emigratie. | soortMigratie, redenWijzigingMigratie, aangeverMigratie | Nee | GGM |
| **NaamAanschrijvingNatuurlijkPersoon** | De naamgegevens waarmee de persoon heeft aangegeven aangeschreven te willen worden | geslachtsnaamAanschrijving, voorlettersAanschrijving, voornamenAanschrijving, aanhefAanschrijving | Nee | GGM |
| **NaamNatuurlijkPersoon** | Gegevens over de naam van de natuurlijk persoon | voornamen, geslachtsnaam, voorvoegselGeslachtsnaam, adellijkeTitelOfPredikaat | Nee | GGM |
| **NaamgebruikNatuurlijkPersoon** | De naamgegevens waarmee de persoon heeft aangegeven aangeschreven te willen worden | adellijkeTitelNaamgebruik, geslachtsnaamstamNaamgebruik, aanhefAanschrijving | Nee | GGM |
| **Nationaliteit** | De hoedanigheid van tot een bepaalde natie te behoren. | codeNationaliteit, nationaliteitOmschrijving, datumBeginGeldigheidNationaliteit, datumEindeGeldigheidNationaliteit | Nee | GGM |
| **NationaliteitIngeschrevenNatuurlijkPersoon** | Gegevens over de nationaliteit. | nationaliteit, redenVerkrijging, redenVerlies, buitenlandsPersoonsnummer | Nee | GGM |
| **NederlandseNationaliteitIngeschrevenPersoon** | Gegevens over de nationaliteit. | aanduidingBijzonderNederlanderschap, redenVerkrijgingNederlandseNationaliteit, redenVerliesNederlandseNationaliteit, nationaliteit | Nee | GGM |
| **Nummeraanduiding** | Een door het bevoegde gemeentelijke orgaan als zodanig toegekende aanduiding van een VERBLIJFSOBJECT, een STANDPLAATS of een LIGPLAATS. | huisletter, huisnummer, huisnummertoevoeging, postcode, datumBeginGeldigheidNummeraanduiding, DatumEindeGeldigheidNummeraanduiding, status, geconstateerd, identificatie, typeAdresseerbaarObject, inOnderzoek | Ja | Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie). |
| **ObjecttypeA** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **ObjecttypeB** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **ObjecttypeC** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **ObjecttypeD** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **ObjecttypeE** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **ObjecttypeF** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **ObjecttypeG** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **Onbestemd Adres** | *Onbestemd Adres* is een adres-aanduiding die officieel door een bevoegde gemeentelijke instantie is vastgelegd, maar waarbij niet kan worden vastgesteld dat het een regulier woon- of verblijfsadres betreft. | huisletter, huisnummer, huisnummertoevoeging, postcode, straatnaam | Nee | GGM |
| **OntbindingHuwelijk/geregistreerdPartnerschap** | Gegevens over het ontbonden huwelijk of geregistreerd partnerschap. | redenEinde, datumEinde, gemeenteEinde, buitenlandsePlaatsEinde, buitenlandseRegioEinde, landOfGebiedEinde, omschrijvingLocatieEinde | Nee | GGM |
| **OpenbareRuimte** | Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorziene buitenruimte die binnen één woonplaats is gelegen | IdentificatiecodeOpenbareRuimte, identificatieIMGeoOPR, statusOpenbareRuimte, naamOpenbareRuimte, indicatieGeconstateerdeOpenbareRuimte, typeOpenbareRuimte, straatnaam, huisnummerrangeEvenNummers, HuisnummerrangeOnevenNummers, huisnummerrangeEvenEnOnevenNummers, labelNaamOpenbareRuimte, openbareRuimteGeometrie, wegsegment, datumBeginGeldigheidOpenbareRuimte, datumEindeGeldigheidOpenbareRuimte, inOnderzoek | Nee | BAG |
| **OverigImgeo** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **OverlijdenIngeschrevenNatuurlijkPersoon** | Gegevens over het overlijden van de ingeschreven natuurlijk persoon. | datumOverlijden, gemeenteOverlijden, buitenlandsePlaatsOverlijden, buitenlandseRegioOverlijden, omschrijvingLocatieOverlijden, landOfGebiedOverlijden | Nee | GGM |
| **OverlijdenIngeschrevenPersoon** | Gegevens over het overlijden van de ingeschreven persoon. | datumOverlijden, overlijdensplaats, landOverlijden | Nee | GGM |
| **Pand** | De kleinste bij de totstandkoming functioneel en bouwkundig-constructief zelfstandige eenheid die direct en duurzaam met de aarde is verbonden en betreedbaar en afsluitbaar is. | pandidentificatie, pandstatus, statusVoortgangBouw, oorspronkelijkBouwjaarPand, oppervlaktePand, brutoInhoudPand, indicatieGeconstateerdPand, hoogsteBouwlaagPand, laagsteBouwlaagPand, pandgeometrieBovenaanzicht, inwinningGeometrieBovenaanzicht, pandgeometrieMaaiveld, inwinningGeometrieMaaiveld, relatieveHoogteliggingPand, LOD1GeometriePand, LOD2GeometriePand, lod3GeometriePand, identificatieBGTPND, indicatiePlanobject, labelNummeraanduidingreeks, datumBeginGeldigheidPand, datumEindeGeldigheidPand, geometriePunt | Nee | BAG |
| **Partij** | Een PARTIJ die bij de centrale voorzieningen van de BRP bekend is. | code, naam, soort, verstrekkingsbeperkingMogelijk, datumAanvangGeldigheidPartij, datumEindeGeldigheidPartij | Nee | BRP |
| **Postadres** | De gegevens die tezamen een postbusadres of antwoordnummeradres vormen | postcodePostadres, postadresType, postbusOfAntwoordnummer | Nee | GGM |
| **Provincie** | Een gedeelte van de wereld met een eigen bestuur, waarvan de soevereiniteit in ieder geval door Nederland is erkend. | provinciecode, provincienaam, datumIngangProvincie, datumEindeProvincie, hoofdstad, oppervlakte, oppervlakteLand | Nee | GFO BG |
| **RedenVerkrijgingNationaliteit** | Tabel waarin de redenen staan voor opname van de Nederlandse nationaliteit. | redennummerVerkrijging, omschrijvingVerkrijging, datumAanvangGeldigheidVerkrijging, datumEindeGeldigheidVerkrijging | Nee | BRP |
| **RedenVerliesNationaliteit** | Tabel waarin de redenen staan voor beëindiging van de Nederlandse nationaliteit. | redennummerVerlies, omschrijvingVerlies, datumAanvangGeldigheidVerlies, datumEindeGeldigheidVerlies | Nee | BRP |
| **Reisdocumentsoort** | Een opsomming van de modellen van de Nederlandse reisdocumenten. | reisdocumentcode, reisdocumentOmschrijving, datumBeginGeldigheidReisdocumentsoort, datumEindeGeldigheidReisdocumentsoort | Nee | GGM |
| **Rekeningnummer** | De gegevens inzake de bankrekening waarmee het SUBJECT in de regel financieel communiceert. | IBAN, BIC | Nee | GGM |
| **SBIActiviteit** | De hiërarchische indeling van economische activiteiten conform SBI (Standaard Bedrijfsindeling). | SBICode, naamActiviteit, datumIngangSBIActiviteit, datumEindeSBIActiviteit, hoofdniveau, hoofdniveauOmschrijving, SBIGroep, SBIGroepOmschrijving | Nee | GGM |
| **SBIActiviteitVestiging** | Aanduiding van de activiteit (en) van een vestiging conform de Standaard BedrijfsIndeling | indicatieHoofdactiviteit, SBICode | Nee | GGM |
| **SamengesteldeNaamNatuurlijkPersoon** | Gegevens over de naam van de NATUURLIJK PERSOON | voornamen, voorvoegsel, scheidingsteken, geslachtsnaamstam, predicaat, adellijkeTitel, namenreeks | Nee | GGM |
| **SluitingOfAangaanHuwelijkOfGeregistreerdPartnerschap** | Gegevens over het gesloten huwelijk of het aangegane geregistreerd partnerschap. | datumAanvang, gemeenteAanvang, buitenlandsePlaatsAanvang, landOfGebiedAanvang, buitenlandseRegioAanvang, omschrijvingLocatieAanvang | Nee | GGM |
| **SoortFunctioneelGebied** | Gegevens over het soort functioneel gebied. | indicatiePlusBRPopulatie, typeFunctioneelGebied | Nee | GGM |
| **SoortGrootte** | Een opsomming van de soorten grootte zoals die kunnen voorkomen in een aktetekst van het Kadaster en aanduiden op welke wijze de grootte van een perceel is vastgesteld conform de waardelijst SoortGrootte van het Kadaster | codeSoortGrootte, naamSoortGrootte, datumBeginGeldigheidSoortGrootte, datumEindeGeldigheidSoortGrootte | Nee | GGM |
| **SoortKunstwerk** | Gegevens over het soort kunstwerk. | indicatiePlusBRPopulatie, typeKunstwerk | Nee | GGM |
| **SoortOverigBouwwerk** | Gegevens over het soort overig bouwwerk. | indicatiePlusBRPopulatie, typeOverigBouwwerk | Nee | GGM |
| **SoortScheiding** | Gegevens over de soort scheiding | indicatiePlusBRPopulatie, typeScheiding | Nee | GGM |
| **SoortSpoor** | Gegevens over het soort spoor. | indicatiePlusBRPopulatie, functieSpoor | Nee | GGM |
| **SoortWOZObject** | De mogelijke codes waarin een soort object kan worden uitgedrukt conform de uniforme soort objectcodelijst van de Waarderingskamer | soortobjectcode, naamSoortObjectcode, opmerkingenSoortObjectcode, datumBeginGeldigheidSoortObjectcode, datumEindeGeldigheidSoortObjectcode | Nee | GGM |
| **SplitsingstekeningReferentie** | Verwijzing naar de splitsingstekening behorende bij de APPARTEMENTSRECHTSPLITSING | identificatieTekening, bronorganisatie, datumCreatie, titel | Nee | GGM |
| **Standplaats** | Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen terrein of gedeelte daarvan dat bestemd is voor het permanent plaatsen van een niet direct en niet duurzaam met de aarde verbonden en voor woon -, bedrijfsmatige, of recreatieve doeleinden geschikte ruimte. | standplaatsidentificatie, indicatieGeconstateerdeStandplaats, standplaatsstatus | Nee | GGM |
| **Valuta** | De hoedanigheid van tot een bepaalde natie te behoren. | valutacode, naam, datumBeginGeldigheid, datumEindeGeldigheid | Nee | GGM |
| **Valutasoort** | De mogelijke munteenheden waarin een geldbedrag kan worden uitgedrukt conform de waardelijst Valutasoort van het Kadaster | valutacode, naamValuta, datumBeginGeldigheidValutasoort, datumEindeGeldigheidValutasoort | Nee | GGM |
| **VerblijfBuitenland** | De gegevens over het verblijf in het buitenland | adresregelBuitenland1, adresregelBuitenland2, adresregelBuitenland3, adresregelBuitenland4, adresregelBuitenland5, adresregelBuitenland6, landOfGebiedVerblijfadres | Nee | GGM |
| **VerblijfBuitenlandSubject** | De gegevens over het verblijf in het buitenland | adresBuitenland1, adresBuitenland2, adresBuitenland3, landVerblijfadres | Nee | GGM |
| **VerblijfadresIngeschrevenNatuurlijkPersoon** | De gegevens over het verblijf en adres van de INGESCHREVEN NATUURLIJK PERSOON | adresHerkomst, beschrijvingLocatie | Nee | GGM |
| **VerblijfadresIngeschrevenPersoon** | De gegevens over het verblijf en adres van de INGESCHREVEN PERSOON | adresHerkomst, beschrijvingLocatie | Nee | GGM |
| **Verblijfsobject** | De kleinste binnen één of meer panden gelegen en voor woon -, bedrijfsmatige, of recreatieve doeleinden geschikte eenheid van gebruik die ontsloten wordt via een eigen afsluitbare toegang vanaf de openbare weg, een erf of een gedeelde verkeersruimte, onderwerp kan zijn van goederenrechtelijke rechtshandelingen en in functioneel opzicht zelfstandig is. | verblijfsobjectidentificatie, verblijfsobjectstatus, indicatieGeconstateerdVerblijfsobject, hoogsteBouwlaagVerblijfsobject, laagsteBouwlaagVerblijfsobject, toegangBouwlaagVerblijfsobject, soortWoonobject, aantalKamers, inOnderzoek, ontsluitingVerdieping | Nee | BAG |
| **VerblijfsrechtIngeschrevenNatuurlijkPersoon** | De gegevens om het verblijfsrecht vast te leggen. | aanduidingVerblijfsrecht, datumAanvangVerblijfsrecht, datumVoorzienEindeVerblijfsrecht, datumMededelingVerblijfsrecht | Nee | GGM |
| **Verblijfstitel** | Rechtsgrond op basis waarvan men bevoegd is in een land te verblijven. | datumAanvangGeldigheidVerblijfstitel, datumEindeGeldigheidVerblijfstitel, verblijfstitelNumeriek, verblijfstitelOmschrijving | Nee | GGM |
| **VerstrekkingsbeperkingPartieelIngeschrevenNatuurlijkPersoon** | Een INGESCHREVEN NATUURLIJK PERSOON kan voor één of meerdere partijen kiezen voor wie een verstrekkingsbeperking geldt. | partij, omschrijvingDerde, gemeenteVerordening | Nee | GGM |
| **WOZ-Deelobjectcode** | De mogelijke codes waarin een soort object kan worden uitgedrukt conform de uniforme deelobjectcodelijst van de Waarderingskamer | deelobjectcode, naamDeelobjectcode, datumBeginGeldigheidDeelojectcode, datumEindeGeldigheidDeelobjectcode | Nee | GGM |
| **Wijk** | Een aaneengesloten gedeelte van het grondgebied van een gemeente, waarvan de grenzen zo veel mogelijk zijn gebaseerd op sociaal-geografische kenmerken. | wijkcode, identificatieIMGeoWYK, wijknaam, geometrieWijk, datumBeginGeldigheidWijk, datumEindeGeldigheidWijk, identificatie | Nee | GFO BG |
| **Woonplaats** | Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorzien gedeelte van het grondgebied van de gemeente. | woonplaatsIdentificatie, woonplaatsNaam, woonplaatsNaamNEN, indicatieGeconstateerdeWoonplaats, woonplaatsStatus, geometrieWoonplaats, datumBeginGeldigheidWoonplaats, datumEindeGeldigheidWoonplaats, inOnderzoek | Nee | BAG |

## Overervingshiërarchie

```
AdresseerbaarObject (abstract)
    └── BenoemdTerrein
    └── OverigBenoemdTerrein
    └── OverigGebouwdObject
```

```
AdresseerbaarObjectAanduiding (abstract)
    └── Ligplaats
    └── OverigGebouwdObject
    └── Standplaats
    └── Verblijfsobject
```

```
BenoemdObject (abstract)
    └── BenoemdTerrein
    └── GebouwdObject
```

```
BenoemdTerrein (abstract)
    └── Ligplaats
    └── Standplaats
```

```
GebouwdObject (abstract)
    └── OverigGebouwdObject
    └── Verblijfsobject
```

```
Geo-Object (abstract)
    └── BegroeidTerreindeel
    └── FunctioneelGebied
    └── Gebouwinstallatie
    └── Inrichtingselement
    └── Kunstwerkdeel
    └── OnbegroeidTerreindeel
    └── OndersteunendWaterdeel
    └── OndersteunendWegdeel
    └── Overbruggingsdeel
    └── OverigBenoemdTerrein
    └── OverigBouwwerk
    └── OverigeScheiding
    └── Pand
    └── Scheiding
    └── Spoor
    └── Tunneldeel
    └── Vegetatieobject
    └── Waterdeel
    └── Wegdeel
```

```
IngeschrevenPersoon (abstract)
    └── Client
    └── Ingezetene
    └── Leerling
    └── Ouder Of Verzorger
```

```
Ingezetene (abstract)
    └── Collegelid
    └── Raadslid
```

```
KadastraleOnroerendeZaak (abstract)
    └── Appartementsrecht
    └── KadastraalPerceel
```

```
NatuurlijkPersoon (abstract)
    └── Bezoeker
    └── Historisch Persoon 
    └── IngeschrevenPersoon
    └── Partner
    └── Projectleider
    └── Relatie
    └── Sollicitant
    └── Vreemdeling
```

```
NietNatuurlijkPersoon (abstract)
    └── Onderwijsinstituut
    └── Projectontwikkelaar
    └── School
    └── Schuldhulporganisatie
    └── Sportvereniging
```

```
Nummeraanduiding (abstract)
    └── OverigeAdresseerbaarObjectAanduiding
```

```
Object (abstract)
    └── BenoemdObject
    └── KadastraleOnroerendeZaak
    └── Nummeraanduiding
    └── Onbestemd Adres
```

```
ObjecttypeC (abstract)
    └── ObjecttypeA
```

```
Rechtspersoon (abstract)
    └── Belanghebbende
    └── Betrokkene
    └── Bevoegd Gezag
    └── Debiteur
    └── Eigenaar
    └── Gemachtigde
    └── Grondbeheerder
    └── Huurder
    └── Indiener
    └── Initiatiefnemer
    └── Lener
    └── Leverancier
    └── Museumrelatie
    └── NatuurlijkPersoon
    └── NietNatuurlijkPersoon
    └── Pachter
    └── Rechthebbende
    └── Schuldeiser
    └── Signaalpartner
    └── Uitgever
```

```
Vestiging (abstract)
    └── Hotel
    └── Verkooppunt
```

```
ZakelijkRecht (abstract)
    └── Zakelijk Recht
```

## Relatiediagrammen

### Kern:Personen

```
AanvraagOfMelding [1..*] ──── Rechtspersoon [0..1] (melder)
Aanwezige Deelnemer [0..1] ──── NatuurlijkPersoon [0..1] (is)
Betrokkene [0..1] ──── NatuurlijkPersoon [1] (is)
Betrokkene [0..1] ──── NietNatuurlijkPersoon [1] (is)
Contact [0..*] ──── NatuurlijkPersoon [0..*] (met)
Gemeentebegrafenis [0..1] ──── NatuurlijkPersoon [1] (heeft)
Gezagsverhouding [0..2] ──── IngeschrevenPersoon [1] (betreft)
Huishouden [0..1] ──── IngeschrevenPersoon [1..*] (heeft)
Indiener [0..1] ──── Rechtspersoon [0..1] (is)
Informering [0..*] ──── NatuurlijkPersoon [1] (informering)
IngeschrevenPersoon [1..*] ──── Briefadres [0..1]
IngeschrevenPersoon [0..1] ──── Gezagsverhouding [0..*] (gezaghebbende)
IngeschrevenPersoon [1] ──── IngeschrevenPersoon [1] (Ouder 2)
IngeschrevenPersoon [1] ──── IngeschrevenPersoon [1] (Ouder 1)
IngeschrevenPersoon [1] ──── Inkomensvoorziening [0..*] (heeft uitkering)
IngeschrevenPersoon [0..*] ──── Nummeraanduiding [0..1] (heeft als adres)
IngeschrevenPersoon  ──── Regeling 
IngeschrevenPersoon [1] ──── Reisdocument [0..*] (is verstrekt aan)
Ingezetene [0..*] ──── Verblijfstitel [0..1] (heeft)
Kandidaat [0..*] ──── NatuurlijkPersoon [1] (betreft)
MaatschappelijkeActiviteit [0..*] ──── NatuurlijkPersoon [1..] (is functionaris van)
MaatschappelijkeActiviteit [0..1] ──── Rechtspersoon [1] (heeft als eigenaar)
Melding [0..*] ──── NatuurlijkPersoon [0..1] (melder)
NatuurlijkPersoon [1..*] ──── Huishouden [0..1] (maakt onderdeel uit van)
NatuurlijkPersoon [1] ──── Nationaliteit [1..*] (heeft)
NatuurlijkPersoon [2..*] ──── Sociale Groep [0..*] (maakt deel uit van)
NietNatuurlijkPersoon [0..1] ──── Gezagsverhouding [0..*] (gezaghebbende)
NietNatuurlijkPersoon [0..*] ──── NatuurlijkPersoon [0..*] (contactpersoon)
NietNatuurlijkPersoon [1] ──── Vestiging [0..*] (heeft)
Object [0..1] ──── Huishouden [1] (is)
Object [0..1] ──── Ingezetene [1] (Is)
Object [0..1] ──── NatuurlijkPersoon [0..*] (is)
Object [0..1] ──── NietNatuurlijkPersoon [0..*] (is)
Parkeervergunning [*] ──── Ingezetene [1]
Parkeervergunning [0..*] ──── Rechtspersoon [1] (houder)
Rechtspersoon [1] ──── AdresBuitenland [0..1] (heeft)
Rechtspersoon [1..*] ──── KadastraleMutatie [0..*] (betrokkenen)
Rechtspersoon [1] ──── Objectrelatie [0..*] (heeft)
Rechtspersoon [0..1] ──── Rapportagemoment [0..*] (projectleider)
Rechtspersoon [0..1] ──── Subsidie [0..*] (aanvrager)
Rechtspersoon [1] ──── Tenaamstelling [0..*] (heeft)
Rechtspersoon [1] ──── WOZ-Belang [1..*] (heeft)
Sociale Relatie [0..*] ──── NatuurlijkPersoon [2..*] (heeft)
Subsidie [0..*] ──── Rechtspersoon [0..1] (verstrekker)
Taak [0..*] ──── Rechtspersoon [0..1] (projectleider)
Vastgoed Contract [0..*] ──── Rechtspersoon [1] (heeft)
Vroegsignaalzaak [0..*] ──── NietNatuurlijkPersoon [1] (opgepaktDoor)
Zorgmelding [0..*] ──── NatuurlijkPersoon [0..*] (betrokkenen)
Zorgmelding [0..*] ──── NatuurlijkPersoon [1] (betreft)
```

### Kern:Overige geo objecten op hoofdlijnen

```
FunctioneelGebied [0..*] ──── SoortFunctioneelGebied [1]
Object [0..1] ──── Inrichtingselement [0..*] (is)
OverigBouwwerk [0..*] ──── SoortOverigBouwwerk [1]
OverigGebouwdObject [0..1] ──── OverigBouwwerk [0..1] (heeft als equivalent)
Scheiding [0..*] ──── SoortScheiding [1]
```

### Diagram Adresaanduiding en BAG

```
Adresaanduiding [0..1] ──── Nummeraanduiding [0..1] (verwijst naar)
```

### Diagram Gebied Vestiging en Adres

```
Briefadres [0..*] ──── Nummeraanduiding [1]
Contact [0..*] ──── Vestiging [0..1] (bij)
Gebied [0..1] ──── Buurt [0..1] (komt overeen)
IngeschrevenPersoon [1..*] ──── Briefadres [0..1]
NietNatuurlijkPersoon [1] ──── Vestiging [0..*] (heeft)
Nummeraanduiding [0..*] ──── Gebied [0..*] (ligt in)
Nummeraanduiding [1] ──── Vestiging [0..*] (heeft als locatie-adres)
Vestiging [0..*] ──── AdresseerbaarObject [0..1] (heeft nevenlocatie in of op)
Vestiging [0..*] ──── AdresseerbaarObject [0..1] (heeft hoofdlocatie in of op)
Vestiging [0..*] ──── BenoemdObject [0..*] (heeft nevenlocatie in of op)
Vestiging [0..*] ──── BenoemdObject [0..1] (heeft hoofdlocatie in of op)
Vestiging [0..*] ──── MaatschappelijkeActiviteit [1] (uitoefening van activiteiten)
Vestiging [0..1] ──── MaatschappelijkeActiviteit [0..1] (is hoofdvestiging van)
Vestiging [1] ──── SBIActiviteitVestiging [1..*]
Vestiging [1] ──── Werkgelegenheid [0..1] (heeft)
```

### Tenaamstelling

```
Rechtspersoon [1] ──── Tenaamstelling [0..*] (heeft)
Tenaamstelling [1] ──── Aantekening [0..*]
Tenaamstelling [0..*] ──── ZakelijkRecht [1] (heeft betrekking op)
ZakelijkRecht [0..*] ──── Tenaamstelling [0..*] (is beperkt tot)
Zekerheidsrecht [0..*] ──── Tenaamstelling [0..1] (bezwaart)
```

### Overige geo objecten op hoofdlijnen

```
Kunstwerkdeel [0..*] ──── SoortKunstwerk [1]
Object [0..1] ──── Kunstwerkdeel [0..*] (is)
Object [0..1] ──── Waterdeel [0..*] (is)
Spoor [0..*] ──── SoortSpoor [1]
Stremming [0..*] ──── Wegdeel [0..*] (betreft)
```

### Detaillering adressen, gebouwen en terreinen op hoofdlijnen

```
OverigBenoemdTerrein [0..1] ──── OverigeAdresseerbaarObjectAanduiding [1] (heeft als officieel adres)
OverigGebouwdObject [0..1] ──── OverigBouwwerk [0..1] (heeft als equivalent)
OverigGebouwdObject [0..1] ──── OverigeAdresseerbaarObjectAanduiding [0..1] (heeft als officieel adres)
Sportpark [0..1] ──── OverigBenoemdTerrein [1] (ligt op)
Veld [0..1] ──── OverigBenoemdTerrein [1] (ligt op)
```

### Detaillering Kadastrale Onroerende Zaken en Rechten op hoofdlijnen

```
Appartementsrechtsplitsing [1] ──── SplitsingstekeningReferentie [1..*]
Beschermde Status [1] ──── KadastraleOnroerendeZaak [0..*] (betreft)
KadastraleMutatie [0..*] ──── KadastraleOnroerendeZaak [0..*] (betreft)
KadastraleMutatie [1] ──── ZakelijkRecht [0..*] (heeft betrekking op)
KadastraleOnroerendeZaak [1..*] ──── Adresaanduiding [0..*] (heeft adres)
KadastraleOnroerendeZaak [1] ──── CultuurOnbebouwd [0..*] (heeft)
KadastraleOnroerendeZaak [1] ──── KadastraleOnroerendeZaak [0..*] (gerelateerd)
KadastraleOnroerendeZaak [0..*] ──── KadastraleOnroerendeZaak [0..*] (is ontstaan uit andere kadastrale onroerende zaak bij)
KadastraleOnroerendeZaak [1] ──── KoopsomKadastraleOnroerendeZaak [0..1]
KadastraleOnroerendeZaak [1] ──── LocatieKadastraleOnroerendeZaak [1..*]
KadastraleOnroerendeZaakAantekening [0..*] ──── KadastraleOnroerendeZaak [1] (heeft betrekking op)
KpBetrokkenBij [0..*] ──── Appartementsrechtsplitsing [1]
KpBetrokkenBij [0..*] ──── ZakelijkRecht [1] (is betrokken bij)
KpOnstaanUit [0..*] ──── Appartementsrechtsplitsing [1]
KpOnstaanUit [0..*] ──── ZakelijkRecht [1] (is ontstaan uit)
Locatieonroerendezaak [0..*] ──── KadastraleOnroerendeZaak [1] (heeft adres)
Object [0..1] ──── KadastraalPerceel [0..*] (is)
Object [0..1] ──── KadastraleOnroerendeZaak [0..*] (is)
Tenaamstelling [0..*] ──── ZakelijkRecht [1] (heeft betrekking op)
Vastgoedobject [0..*] ──── KadastraalPerceel [0..*] (betreft)
Vastgoedobject [0..*] ──── KadastraleOnroerendeZaak [0..*] (betreft)
WOZ-object [0..*] ──── KadastraleOnroerendeZaak [0..*] (bevat)
ZakelijkRecht [1..*] ──── KadastraleOnroerendeZaak [0..1] (rust op)
ZakelijkRecht [0..*] ──── Tenaamstelling [0..*] (is beperkt tot)
ZakelijkRecht [0..1] ──── ZakelijkRecht [0..*] (is belast met)
Zekerheidsrecht [0..*] ──── KadastraleOnroerendeZaak [0..1] (rust op)
Zekerheidsrecht [0..*] ──── Tenaamstelling [0..1] (bezwaart)
```

### Detaillering subjecten op hoofdlijnen

```
IngeschrevenPersoon [1] ──── Reisdocument [0..*] (is verstrekt aan)
MaatschappelijkeActiviteit [0..*] ──── NatuurlijkPersoon [1..] (is functionaris van)
MaatschappelijkeActiviteit [0..1] ──── Rechtspersoon [1] (heeft als eigenaar)
Object [0..1] ──── MaatschappelijkeActiviteit [0..*] (is)
Vestiging [0..*] ──── MaatschappelijkeActiviteit [1] (uitoefening van activiteiten)
Vestiging [0..1] ──── MaatschappelijkeActiviteit [0..1] (is hoofdvestiging van)
```

### Detaillering WOZ-objecttypen op hoofdlijnen

```
LocatieaanduidingWozObject [1] ──── WOZ-object [1] (heeft)
WOZ-Waarde [0..*] ──── WOZ-object [1] (is voor)
WOZ-deelobject [1..*] ──── AdresseerbaarObject [0..1] (bestaat uit)
WOZ-deelobject [0..*] ──── Pand [0..1] (bestaat uit)
WOZ-deelobject [1..*] ──── WOZ-object [1] (is onderdeel van)
WOZ-object [0..*] ──── KadastraleOnroerendeZaak [0..*] (bevat)
WOZ-object [0..*] ──── OpenbareRuimte [0..1] (ligt aan)
WOZ-object [1] ──── WOZ-Belang [1..*] (heeft)
```

### Overig

```
Adresaanduiding [0..1] ──── Nummeraanduiding [0..1] (verwijst naar)
Appartementsrechtsplitsing [1] ──── SplitsingstekeningReferentie [1..*]
Areaal [0..*] ──── Buurt [1..*] (ligt in)
Areaal [0..*] ──── Wijk [1..*] (valt binnen)
Asielstatushouder [0..*] ──── Gemeente [0..1] (is gekoppeld aan )
BenoemdObject [1..*] ──── BenoemdObject [0..*] (is ontstaan uit / overgegaan in)
Beschermde Status [0..1] ──── OpenbareRuimte [0..*] (betreft)
Beschermde Status [0..1] ──── Pand [0..*] (betreft)
Binnenlocatie [0..*] ──── Verblijfsobject [0..1] (is gevestigd in)
Binnenlocatie [0..*] ──── Wijk [1] (bedient)
Briefadres [0..*] ──── Nummeraanduiding [1]
Buurt [1..*] ──── Wijk [1] (ligt in)
FunctioneelGebied [0..*] ──── SoortFunctioneelGebied [1]
Gebied [0..1] ──── Buurt [0..1] (komt overeen)
GeboorteIngeschrevenNatuurlijkPersoon [0..*] ──── Woonplaats [0..1] (heeft plaatsgevonden in)
GeboorteIngeschrevenNatuurlijkPersoon [0..*] ──── Woonplaats [0..1] (heeft plaatsgevonden in )
GebouwdObject [1] ──── Gebruiksdoel [1..*] (heeft)
GebouwdObject [1] ──── Winkelvloeroppervlak [0..1] (heeft)
GebouwdObject [1..] ──── gebruiksdoel [1..*] (heeft)
Gemeente [1..*] ──── Gemeente [0..*] (is overgegaan in)
Huishouden [0..*] ──── Nummeraanduiding [1] (heeft als adres)
KadastraleOnroerendeZaak [1] ──── KoopsomKadastraleOnroerendeZaak [0..1]
KadastraleOnroerendeZaak [1] ──── LocatieKadastraleOnroerendeZaak [1..*]
Kunstwerkdeel [0..*] ──── SoortKunstwerk [1]
Nummeraanduiding [1] ──── AdresseerbaarObjectAanduiding [0..1] (heeft als hoofdadres)
Nummeraanduiding [1..*] ──── AdresseerbaarObjectAanduiding [0..*] (heeft als nevenadres)
Nummeraanduiding [0..*] ──── Buurt [0..1] (ligt in)
Nummeraanduiding [0..*] ──── Gebied [0..*] (ligt in)
Nummeraanduiding [0..*] ──── OpenbareRuimte [1] (ligt aan)
Nummeraanduiding [0..*] ──── Woonplaats [0..1] (ligt in)
Object [0..1] ──── Buurt [0..*] (is)
Object [0..1] ──── Ligplaats [0..*] (is)
Object [0..1] ──── OpenbareRuimte [0..*] (is)
Object [0..1] ──── Pand [0..*] (is)
Object [0..1] ──── Standplaats [0..*] (is)
ObjecttypeA [1] ──── ObjecttypeB [0..*] (naam1 (werkwoord))
ObjecttypeD [0..*] ──── ObjecttypeB [1..*] (naam2 (werkwoord))
ObjecttypeE [0..*] ──── ObjecttypeF [1] (naam3)
ObjecttypeE [0..*] ──── ObjecttypeG [1] (naam4)
OntbindingHuwelijk/geregistreerdPartnerschap [0..*] ──── Woonplaats [0..1] (is ontbonden in)
OpenbareRuimte [1] ──── Buurt [1] (ligt in)
OpenbareRuimte [1..*] ──── Woonplaats [1..] (ligt in)
OverigBouwwerk [0..*] ──── SoortOverigBouwwerk [1]
OverlijdenIngeschrevenNatuurlijkPersoon [0..*] ──── Woonplaats [0..1] (heeft plaatsegevonden in)
OverlijdenIngeschrevenNatuurlijkPersoon [0..*] ──── Woonplaats [0..1] (heeft plaatsgevonden in)
Pand [0..*] ──── Buurt [0..1] (zonder verblijfsobject ligt in)
Postadres [0..*] ──── Woonplaats [1] (heeft als correspondentieadres postadres in)
Scheiding [0..*] ──── SoortScheiding [1]
Schuldhulptraject [0..*] ──── Gemeente [1] (onder verantwoordelijkheid van)
SluitingOfAangaanHuwelijkOfGeregistreerdPartnerschap [0..*] ──── Woonplaats [0..1] (is gesloten/aangegaan in)
SluitingOfAangaanHuwelijkOfGeregistreerdPartnerschap [0..*] ──── Woonplaats [0..1] (is gesloten/aangegaan in )
Spoor [0..*] ──── SoortSpoor [1]
Vastgoedobject [0..1] ──── Pand [0..1] (betreft)
VerblijfadresIngeschrevenNatuurlijkPersoon [0..*] ──── AdresseerbaarObject [0..1] (is ingeschreven op)
VerblijfadresIngeschrevenNatuurlijkPersoon [0..*] ──── AdresseerbaarObjectAanduiding [0..1] (is ingeschreven op)
VerblijfadresIngeschrevenNatuurlijkPersoon [0..*] ──── Ligplaats [0..1] (verblijft op)
VerblijfadresIngeschrevenNatuurlijkPersoon [0..*] ──── Standplaats [0..1] (verblijft op)
VerblijfadresIngeschrevenNatuurlijkPersoon [0..*] ──── Verblijfsobject [0..1] (verblijft in)
VerblijfadresIngeschrevenNatuurlijkPersoon [0..*] ──── Woonplaats [0..1] (verblijft op)
VerblijfadresIngeschrevenNatuurlijkPersoon [0..*] ──── Woonplaats [0..1] (verblijft op locatie in)
Verblijfsobject [0..*] ──── Pand [1..*] (maakt deel uit van)
Vestiging [0..*] ──── BenoemdObject [0..*] (heeft nevenlocatie in of op)
Vestiging [0..*] ──── BenoemdObject [0..1] (heeft hoofdlocatie in of op)
Vestiging [0..*] ──── Nummeraanduiding [1] (heeft als locatie-adres)
Vestiging [1] ──── SBIActiviteitVestiging [1..*]
Wijk [1..*] ──── Gemeente [1] (ligt in)
Wijk [1..*] ──── Woonplaats [1] (ligt in)
Woonplaats [1..*] ──── Gemeente [1] (ligt in)
```

## Observaties

- Dit beleidsdomein bevat 135 entiteiten.
- Entiteiten zijn gegroepeerd in 11 diagramgroepen: Kern:Personen (9), Kern:Overige geo objecten op hoofdlijnen (10), Diagram Adresaanduiding en BAG (1), Diagram Gebied Vestiging en Adres (3), Tenaamstelling (2), Overige geo objecten op hoofdlijnen (8), Detaillering adressen, gebouwen en terreinen op hoofdlijnen (3), Detaillering Kadastrale Onroerende Zaken en Rechten op hoofdlijnen (7), Detaillering subjecten op hoofdlijnen (2), Detaillering WOZ-objecttypen op hoofdlijnen (3), Overig (87).
- Er zijn 87 generalisatierelaties aanwezig.
- 9 entiteiten zijn abstract.
