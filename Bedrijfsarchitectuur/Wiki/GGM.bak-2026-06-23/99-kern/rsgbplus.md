---
type: ggm-beleidsdomein
naam: RSGBPlus
definitie: "Het subdomein dat gegevens omvat over gemeentelijke basisgegevens, gebaseerd op het Referentiemodel Stelsel van Gemeentelijke Basisgegevens (RSGB) v2.0.2, aangevuld met specifieke uitbreidingen voor lokaal gebruik en aanvullingen uit RSGB v3.0."
taakveld: "99 Kern"
aantal_entiteiten: 128
---

# GGM Beleidsdomein: RSGBPlus

### (Zaak)objecten

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Huishouden** | Een duurzame samenlevingsvorm van een of meer natuurlijke personen binnen een VERBLIJFSOBJECT, STANDPLAATS of LIGPLAATS. | huishoudensoort, huishoudennummer, huishoudengrootte, datumBeginGeldigheidHuishouden, datumEindeGeldigheidHuishouden, relatie, relatie | Nee | GGM |
| **Ingezetene** | Een individueel menselijk wezen, ingeschreven in het Nederlands Bevolkingsregister. | aanduidingUitgeslotenKiesrecht, aanduidingEuropeesKiesrecht, indicatieCurateleregister, indicatieGezagMinderjarige, datumVerkrijgingVerblijfstitel, datumVerliesVerblijfstitel, indicatieBlokkering | Nee | GGM |

### AANDUIDING ADRES OBJECT

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **LocatieaanduidingAdresWOZObject** | Nadere aanduiding van het WOZ-object middels een locatieomschrijving van ADRESSEERBAAR OBJECT AANDUIDING. | locatieOmschrijving | Nee | GGM |
| **WOZ-object** | De onroerende zaak waarvan op grond van de Wet WOZ de waarde moet worden bepaald en vastgesteld. | WOZObjectnummer, geometrieWOZObject, statusWOZObject, grondoppervlakte, gebruikscode, soortobjectcode, vastgesteldeWaarde, datumWaardepeiling, datumBeginGeldigheidWOZObject, datumEindeGeldigheidWOZObject | Nee | GGM |

### AANDUIDING LOCATIE OVERIG GEBOUWD OBJECT

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **OverigGebouwdObject** | De kleinste eenheid van gebruik, geen verblijfsobject zijnde, binnen een bij de totstandkoming functioneel en bouwkundig constructief zelfstandige eenheid die direct en duurzaam met de aarde is verbonden. | overigGebouwdObjectIdentificatie, bouwjaar, indicatiePlanobject | Nee | GGM |

### ADRESSEERBAAR OBJECT AANDUIDING

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **OverigeAdresseerbaarObjectAanduiding** | Een door de gemeenteraad als zodanig toegekende aanduiding van een overig gebouwd object of een overig benoemd terrein. | Identificatiecode | Nee | Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie). |
| **Vestiging** | Een gebouw of complex van gebouwen waar duurzame uitoefening van de activiteiten van een onderneming of rechtspersoon plaatsvindt. | vestigingsnummer, handelsnaam, verkorteNaam, datumAanvang, datumEinde, datumVoortzetting, toevoegingAdres, fulltimeWerkzameMannen, parttimeWerkzameMannen, fulltimeWerkzameVrouwen, parttimeWerkzameVrouwen, commercieleVestiging, totaalWerkzamePersonen | Nee | GGM |

### APPARTEMENTRECHTSPLITSING

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Appartementsrechtsplitsing** | Het recht op een stuk grond of op een gebouw met toebehoren op de daarbij behorende grond met toebehoren is gesplitst in appartementsrechten. | ddentificatieAppartementsrechtsplitsing, typeSplitsing | Nee | GGM |
| **NietNatuurlijkPersoon** | Een INGESCHREVEN NIET-NATUURLIJK PERSOON of een ANDER BUITENLANDS NIET-NATUURLIJK PERSOON | NNPID, statutaireNaam, datumAanvang, rechtsvorm, datumEinde, statutaireZetel, datumVoortzetting, faxnummer, KVKnummer, ingeschreven, RSINNummer, datumUitschrijving, websiteURL, inOprichting | Ja | GGM |
| **SplitsingstekeningReferentie** | Verwijzing naar de splitsingstekening behorende bij de APPARTEMENTSRECHTSPLITSING | identificatieTekening, bronorganisatie, datumCreatie, titel | Nee | GGM |
| **ZakelijkRecht** | Het eigendom van, of een beperkt recht van een natuurlijk of niet-natuurlijk persoon (PERSOON) op, een onroerende zaak (met uitzondering van hypotheken en beslagen). | identificatieZakelijkRecht, aardZakelijkRecht, datumIngangRecht, datumEindeRecht, toelichtingBewaarder | Nee | GGM |

### ARK codes kadastrale gemeenten referenties

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **AkrKadastraleGemeentecode** | De door de Dienst Kadaster onderkende AKR codes voor kadastrale gemeenten | codeAKRKadadastraleGemeentecode, AKRCode, datumBeginGeldigheidAKRCode, datumEindeGeldigheidAKRCode | Nee | GGM |

### Aanduiding verblijfsrecht

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **AanduidingVerblijfsrecht** | Aanduiding in verband met het verblijfsrecht van de vreemdeling. | verblijfsrechtnummer, verblijfsrechtomschrijving, datumAanvangGeldigheidVerblijfsrecht, datumEindeGeldigheidVerblijfsrecht | Nee | GGM |
| **VerblijfsrechtIngeschrevenNatuurlijkPersoon** | De gegevens om het verblijfsrecht vast te leggen. | aanduidingVerblijfsrecht, datumAanvangVerblijfsrecht, datumVoorzienEindeVerblijfsrecht, datumMededelingVerblijfsrecht | Nee | GGM |

### Aard aantekeningen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **AardAantekening** | Een opsomming van de diverse aarden van de aantekeningen zoals door de Dienst Kadaster is onderscheiden. | codeAardAantekening, naamAardAantekening, datumBeginGeldigheidAardAantekening, datumEindeGeldigheidAardAantekening | Nee | GGM |

### Aard zakelijke rechten referenties

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **AardZakelijkRecht** | Een opsomming van de diverse aarden van het zakelijk rechten zoals door de Dienst Kadaster is onderscheiden. | codeAardZakelijkRecht, naamAardZakelijkRecht, datumBeginGeldigheidAardZakelijkRecht, datumEindeGeldigheidAardZakelijkRecht | Nee | GGM |

### Archief Relaties met Kern

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **NatuurlijkPersoon** | Een INGESCHREVEN PERSOON of ANDER NATUURLIJK PERSOON | aanduidingNaamgebruik, geslachtsnaamAanschrijving, voornamen, academischeTitel, datumGeboorte, geboorteplaats, geslachtsnaam, overlijdensplaats, voorlettersAanschrijving, datumOverlijden, geboorteland, geslachtsaanduiding, landOverlijden, voornamenAanschrijving, voorvoegselGeslachtsnaam, aanhefAanschrijving, adellijkeTitelOfPredikaat, burgerservicenummer, handlichting, achternaam, nationaliteit, bijzonderNederlanderschap, anummer, indicatieOverleden, IndicatieAfschermingPersoonsgegevens | Ja | GGM |
| **Rechtspersoon** | Een NATUURLIJK PERSOON of een NIET-NATUURLIJK PERSOON | adresBinnenland, adresBuitenland, rekeningnummer, emailadres, faxnummer, identificatie, naam, KVKnummer, rechtsvorm, telefoonnummer, adresCorrespondentie | Ja | GGM |

### BEGROEID TERREINDEEL

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **BegroeidTerreindeel** | Kleinste functioneel onafhankelijk stukje van een terrein dat er binnen het objecttype Terrein van NEN 3610 wordt onderscheiden, met aaneengesloten homogene vegetatie. | identificatie, status, relatieveHoogteligging, fysiekVoorkomen, plusFysiekVoorkomen, kruinlijngeometrie, geometrie, LOD0Geometrie, opTalud, datumBeginGeldigheid, datumEindeGeldigheid | Nee | GGM |

### BENOEMD OBJECT

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **KadastraleOnroerendeZaak** | Een geregistreerd goed waarvoor bij overdracht of vestiging van rechten inschrijving in de openbare registers van het Kadaster is vereist zijnde een KADASTRAAL PERCEEL of een APPARTEMENTSRECHT. | kadastraleGemeentecode, landInrichtingRenteBedrag, landInrichtingRenteEindejaar, perceelnummer, kadastraleGemeente, sectie, appartementsrechtvolgnummer, datumBeginGeldigheid, datumEindeGeldigheid, oppervlakte, identificatie, locatieOmschrijving, koopsom, koopjaar, cultuurcodeOnbebouwd, ligging, valutacode, begrenzing, oud, oud | Ja | GGM |
| **WOZ-deelobject** | Aanduiding van afzonderlijke elementen (delen van het object, bijzondere waarderelevante factoren) die voor de onderbouwing van de vastgestelde waarde van belang zijn. | WOZDeelobjectNummer, codeWOZDeelobject, statusWOZDeelobject, datumBeginGeldigheidDeelobject, datumEindeGeldigheidDeelobject | Nee | Gegevenswoordenboek WOZ |

### BRK

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Appartementsrecht** | Een KADASTRALE ONROERENDE ZAAK dat een aandeel is in de goederen die in de splitsing zijn betrokken, dat de bevoegdheid omvat tot het uitsluitend gebruik van bepaalde gedeelten van het gebouw die blijkens hun inrichting bestemd zijn of worden om als afzonderlijk geheel te worden gebruikt (art. 5:106 lid 4 BW). | *(geen attributen)* | Nee | GGM |
| **KadastraalPerceel** | Een KADASTRALE ONROERENDE ZAAK dat een kadastraal geïdentificeerd en met kadastrale grenzen begrensd deel van het Nederlands grondgebied betreft (art. 1 lid 1 Kadasterwet). | begrenzingPerceel, indicatieDeelperceel, omschrijvingDeelperceel, groottePerceel, aanduidingSoortGrootte, plaatscoordinatenPerceel | Nee | GGM |
| **Tenaamstelling** | Een TENAAMSTELLING vormt de relatie tussen een Recht en een Persoon en geeft aan welk recht, met uitzondering van hypotheek en beslag, door een Persoon wordt uitgeoefend op een Kadastraal object. | identificatieTenaamstelling, aandeelInRecht, verkregenNamensSamenwerkingsverband, exploitantcode, datumBeginGeldigheid, datumEindeGeldigheid, burgerlijkeStaatTenTijdeVanVerkrijging, verklaringInzakeDerdenBescherming | Nee | GGM |

### Burgerzaken

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **IngeschrevenPersoon** | Een INGEZETENE of NIET-INGEZETENE | adresHerkomst, anummer, beschrijvingLocatie, burgerlijkeStaat, indicatieGeheim, gemeenteVanInschrijving, landWaarvandaanIngeschreven, landWaarnaarVertrokken, datumInschrijvingGemeente, datumBeginGeldigheidVerblijfplaats, signaleringReisdocument, buitenlandsReisdocument, datumVestigingNederland, datumVertrekUitNederland, redenOpschortingBijhouding, datumOpschortingBijhouding, ingezetene, datumEindeGeldigheidVerblijfsplaats, redenEindeBewoning, verblijfstitel, ouder1, gezinsrelatie, ouder2, partnerID | Ja | GGM |
| **Reisdocument** | Een document dat vereist is voor reizen naar het buitenland | soort, reisdocumentnummer, datumUitgifte, autoriteitVanAfgifte, datumIngangDocument, datumEindeGeldigheidDocument, datumInhoudingOfVermissing, aanduidingInhoudingVermissing | Nee | GGM |

### Codes cultuur onbebouwd referenties

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **CultuurcodeOnbebouwd** | De mogelijke cultuurcodes bebouwd conform de waardelijst Cultuurcode Bebouwd van het Kadaster | code, naamCultuurcodeOnbebouwd, datumBeginGeldigheidCultuurcodeOnbebouwd, datumEindeGeldigheidCultuurcodeOnbebouwd | Nee | GGM |

### Cultuur codes bebouwd referenties

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **CultuurcodeBebouwd** | De mogelijke cultuurcodes bebouwd conform de waardelijst Cultuurcode Bebouwd van het Kadaster | code, naamCultuurcodeBebouwd, datumBeginGeldigheidCultuurcodeBebouwd, datumEindeGeldigheidCultuurcodeBebouwd | Nee | GGM |
| **LocatieKadastraleOnroerendeZaak** | Deze wordt gebruikt om één of meer locatieaanduiding(en) van een onroerende zaak weer te geven. | locatieOmschrijving, aardCultuurBebouwd | Nee | GGM |

### Deelobjectcodereferenties

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **WOZ-Deelobjectcode** | De mogelijke codes waarin een soort object kan worden uitgedrukt conform de uniforme deelobjectcodelijst van de Waarderingskamer | deelobjectcode, naamDeelobjectcode, datumBeginGeldigheidDeelojectcode, datumEindeGeldigheidDeelobjectcode | Nee | GGM |

### Detaillering Kadastrale Onroerende Zaken en Rechten met attributen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **KadastraleOnroerendeZaakAantekening** | Aanduiding van het feit, genoemd in een Stuk, dat betrekking heeft op een onroerende zaak en dat gevolgen kan hebben voor de uitoefening van rechten op de onroerende zaak. | kadasterIdentificatieAantekening, aardAantekeningKadastraalObject, beschrijvingAantekeningKadastraalObject, datumBeginAantekeningKadastraalObject, datumEindeAantekeningKadastraalObject | Nee | GGM |
| **Zekerheidsrecht** | Een zekerheidsrecht is een beperkt recht (hypotheek) of een beperking (beslag). | identificatieZekerheidsrecht, omschrijvingBetrokkenRecht, typeZekerheidsrecht, aandeelInBetrokkenRecht, datumIngangRecht, datumEindeRecht | Nee | GGM |

### Detaillering WOZ-objecttypen met attributen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **OverigBenoemdTerrein** | Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen onbebouwd terrein of een gedeelte daarvan, geen standplaats of gedeelte van een ligplaats zijnde, dat bestemd is voor het gedurende langere tijd verrichten van een maatschappelijke activiteit. | overigBenoemdTerreinIdentificatie, gebruiksdoelOverigBenoemdTerrein | Nee | Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie). |
| **WOZ-Waarde** | De op grond van de Wet WOZ vastgestelde waarde van het WOZ-object naar de genoemde waardepeildatum. | datumWaardepeiling, vastgesteldeWaarde, datumPeilingToestand, statusBeschikking | Nee | GGM |

### Detaillering adressen, gebouwen en terreinen op hoofdlijnen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **FunctioneelGebied** | Begrensd en benoemd gebied dat door een functionele eenheid beschreven wordt. | identificatieFunctioneelGebied, statusFunctioneelGebied, naamFunctioneelGebied, geometrieFunctioneelGebied, datumBeginGeldigheidFunctioneelGebied, datumEindeGeldigheidFunctioneelGebied | Nee | GGM |

### Detaillering subjecten met attributen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **MaatschappelijkeActiviteit** | Een verband tussen één of meer personen met voldoende mate van zelfstandigheid, inbreng van arbeid of middelen, winstoogmerk en extern optreden (i.g.v. een onderneming) dan wel een in een organisatorisch verband, dat toebehoort aan een niet-natuurlijk persoon welke registratieplichtig is, uitgeoefende activiteit die niet valt onder de criteria voor onderneming of bedrijfsmatigheid welke adresseerbaar is middels ofwel een vestiging ofwel het adres van een bepaalde vertegenwoordiger (i.g.v. een niet-ondernemings-activiteit). | KVKnummer, datumAanvang, datumEindeGeldig, indicatieEconomischActief, statutaireNaam, rechtsvorm, URL, RSIN, adresBinnenland, adresCorrespondentie, telefoonnummer, datumFaillisement | Nee | GGM |

### Diagram Adresaanduiding en BAG

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Adresaanduiding** | De adresaanduiding van het WOZ-OBJECT | straatnaam, gemeentenaam, huisnummer, huisletter, huisnummertoevoeging, postcode, BAGID | Nee | GGM |

### Diagram Gebied Vestiging en Adres

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Briefadres** | Een briefadres is een adres waar door de overheid verzonden stukken voor een persoon in ontvangst wordt genomen. | datumAanvang, datumEinde, omschrijvingAangifte, adresFunctie | Nee | GGM |
| **Gebied** | Een aaneengesloten gedeelte van een wijk, waarvan de grenzen zo veel mogelijk gebaseerd zijn op topografische elementen. | gebiedcode, identificatieIMGeoBRT, naam, geometrie, datumBeginGeldigheidBuurt, datumEindeGeldigheidGebied, gebiedsoort | Nee | GGM |
| **Gebied** | Een aaneengesloten gedeelte van een wijk, waarvan de grenzen zo veel mogelijk gebaseerd zijn op topografische elementen. | gebiedcode, identificatieIMGeoBRT, naam, geometrie, datumBeginGeldigheidBuurt, datumEindeGeldigheidGebied, gebiedsoort | Nee | GGM |

### Diagram IMBOR vs IMGeo

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Inrichtingselement** | Ruimtelijk object al dan niet ter detaillering dan wel ter inrichting van de overige benoemde ruimtelijke objecten of een ander inrichtingselement. | identificatieInrichtingselement, statusInrichtingselement, geometrieInrichtingselement, typeInrichtingselement, plusTypeInrichtingselement, relatieveHoogteliggingInrichtingselement, LOD0GeometrieInrichtingselement, datumBeginGeldigheidInrichtingselement, datumEindeGeldigheidInrichtingselement | Nee | GGM |

### FUNCTIONEEL GEBIED

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **SoortFunctioneelGebied** | Gegevens over het soort functioneel gebied. | indicatiePlusBRPopulatie, typeFunctioneelGebied | Nee | GGM |

### GEBOUWINSTALLATIE

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Gebouwinstallatie** | Een component aan de buitenzijde van een gebouw, die het aanzicht van het gebouw mede bepaalt. | identificatieGebouwinstallatie, statusGebouwinstallatie, geometrieGebouwinstallatie, typeGebouwinstallatie, LOD0GeometrieGebouwinstallatie, relatieveHoogteliggingGebouwinstallatie, datumBeginGeldigheidGebouwinstallatie, datumEindeGeldigheidGebouwinstallatie | Nee | GGM |

### HUWELIJK/GEREGISTREERD PARTNERSCHAP

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **OntbindingHuwelijk/geregistreerdPartnerschap** | Gegevens over het ontbonden huwelijk of geregistreerd partnerschap. | redenEinde, datumEinde, gemeenteEinde, buitenlandsePlaatsEinde, buitenlandseRegioEinde, landOfGebiedEinde, omschrijvingLocatieEinde | Nee | GGM |
| **SluitingOfAangaanHuwelijkOfGeregistreerdPartnerschap** | Gegevens over het gesloten huwelijk of het aangegane geregistreerd partnerschap. | datumAanvang, gemeenteAanvang, buitenlandsePlaatsAanvang, landOfGebiedAanvang, buitenlandseRegioAanvang, omschrijvingLocatieAanvang | Nee | GGM |

### Hoofdobjecten IMGeo en Beheerobjecten 

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Kunstwerkdeel** | Onderdeel van een civiel-technisch werk voor de infrastructuur van wegen, water, spoorbanen, waterkeringen en/of leidingen. | identificatieKunstwerkdeel, statusKunstwerkdeel, relatieveHoogteliggingKunstwerkdeel, geometrieKunstwerkdeel, LOD0GeometrieKunstwerkdeel, LOD1GeometrieKunstwerkdeel, LOD2GeometrieKunstwerkdeel, lod3GeometrieKunstwerkdeel, datumBeginGeldigheidKunstwerkdeel, datumEindeGeldigheidKunstwerkdeel | Nee | GGM |
| **OnbegroeidTerreindeel** | Kleinste functioneel onafhankelijk stukje van een terrein, dat er binnen het objecttype Terrein van NEN 3610 wordt onderscheiden, zonder aaneengesloten vegetatie. | identificatie, status, relatieveHoogteligging, fysiekVoorkomen, plusFysiekVoorkomen, geometrie, kruinlijngeometrie, onbegroeidTerreindeelOpTalud, datumBeginGeldigheid, datumEindeGeldigheid | Nee | GGM |
| **OndersteunendWaterdeel** | Object dat in het kader van de waterhuishouding periodiek gedeeltelijk of geheel met water is bedekt. | identificatie, status, geometrie, relatieveHoogteligging, type, plusType, datumBeginGeldigheid, datumEindeGeldigheid | Nee | GGM |
| **OndersteunendWegdeel** | Een deel van de weg dat niet primair bedoeld is voor gebruik door het verkeer. | identificatie, status, geometrie, relatieveHoogteligging, kruinlijngeometrie, LOD0Geometrie, functie, plusFunctie, fysiekVoorkomen, plusFysiekVoorkomen, opTalud, datumBeginGeldigheid, datumEindeGeldigheid | Nee | GGM |
| **Overbruggingsdeel** | Onderdeel van een beweegbare of vaste verbinding tussen twee punten, die door water, een weg of anderszins gescheiden zijn, dat essentieel is voor de constructie. | identificatieOverbruggingsdeel, statusOverbruggingsdeel, relatieveHoogteliggingOverbruggingsdeel, typeOverbruggingsdeel, hoortBijTypeOverbrugging, overbruggingIsBeweegbaar, geometrieOverbruggingsdeel, LOD0GeometrieOverbruggingsdeel, datumBeginGeldigheidOverbruggingsdeel, datumEindeGeldigheidOverbruggingsdeel | Nee | GGM |
| **OverigBouwwerk** | Met de aarde verbonden duurzaam bouwwerk, dat niet valt onder de definities van een pand of kunstwerk. | identificatieOverigBouwwerk, statusOverigBouwwerk, relatieveHoogteliggingOverigBouwwerk, geometrieOverigBouwwerk, LOD0GeometrieOverigBouwwerk, LOD1GeometrieOverigBouwwerk, LOD2GeometrieOverigBouwwerk, lod3GeometrieOverigBouwwerk, datumBeginGeldigheidOverigBouwwerk, datumEindeGeldigheidOverigBouwwerk | Nee | GGM |
| **OverigeScheiding** | Kunstmatig, meestal lineair obstakel met een werende functie, met kleinere afmetingen dan toegestaan voor opname in de BGT. | identificatieOverigeScheiding, statusOverigeScheiding, relatieveHoogteliggingOverigeScheiding, geometrieOverigeScheiding, typeOverigeScheiding, LOD0GeometrieOverigeScheiding, LOD1GeometrieOverigeScheiding, LOD2GeometrieOverigeScheiding, lod3GeometrieOverigeScheiding, datumBeginGeldigheidOverigeScheiding, datumEindeGeldigheidOverigeScheiding | Nee | GGM |
| **Scheiding** | Kunstmatig, meestal lineair obstakel met een werende functie. | identificatieScheiding, statusScheiding, relatieveHoogteliggingScheiding, geometrieScheiding, LOD0GeometrieScheiding, LOD1GeometrieScheiding, LOD2GeometrieScheiding, lod3GeometrieScheiding, datumBeginGeldigheidScheiding, datumEindeGeldigheidScheiding | Nee | GGM |
| **Spoor** | De as van het spoor, dat wil zeggen het midden van twee stalen staven op een onderling vaste afstand, waarover trein, tram, of sneltram rijdt. | identificatieSpoor, statusSpoor, relatieveHoogteliggingSpoor, geometrieSpoor, LOD0GeometrieSpoor, datumBeginGeldigheidSpoor, datumEindeGeldigheidSpoor | Nee | GGM |
| **Tunneldeel** | Onderdeel van een kunstmatig aangelegde, kokervormige onderdoorgang, dat essentieel is voor de constructie. | identificatieTunneldeel, statusTunneldeel, relatieveHoogteliggingTunneldeel, geometrieTunneldeel, LOD0GeometrieTunneldeel, datumBeginGeldigheidTunneldeel, datumEindeGeldigheidTunneldeel | Nee | GGM |
| **Vegetatieobject** | Solitair vegetatieobject of lijn- of vlakvormige groep gelijksoortige vegetatieobjecten met een beperkte omvang. | identificatieVegetatieobject, statusVegetatieobject, typeVegetatieobject, relatieveHoogteliggingVegetatieobject, geometrieVegetatieobject, LOD0GeometrieVegetatieobject, datumBeginGeldigheidVegetatieobject, datumEindeGeldigheidVegetatieobject | Nee | GGM |
| **Waterdeel** | Kleinste functioneel onafhankelijk stukje water met gelijkblijvende, homogene eigenschappen en relaties dat er binnen het objecttype Water van NEN 3610 wordt onderscheiden. | identificatieWaterdeel, statusWaterdeel, relatieveHoogteliggingWaterdeel, geometrieWaterdeel, typeWaterdeel, plusTypeWaterdeel, datumBeginGeldigheidWaterdeel, datumEindeGeldigheidWaterdeel | Nee | GGM |
| **Wegdeel** | Kleinste functioneel onafhankelijk stukje van een NEN 3610 Weg, met gelijkblijvende homogene eigenschappen en relaties en primair bedoeld voor gebruik door weg-, spoor- en vliegverkeer te land | identificatieWegdeel, statusWegdeel, relatieveHoogteliggingWegdeel, geometrieWegdeel, kruinlijngeometrieWegdeel, LOD0GeometrieWegdeel, functieWegdeel, plusFunctieWegdeel, fysiekVoorkomenWegdeel, plusFysiekVoorkomenWegdeel, wegdeelOpTalud, datumBeginGeldigheidWegdeel, datumEindeGeldigheidWegdeel | Nee | GGM |

### INGESCHREVEN NATUURLIJK  PERSOON

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **GeboorteIngeschrevenNatuurlijkPersoon** | Gegevens over de geboorte van de INGESCHREVEN NATUURLIJK PERSOON. | datumGeboorte, gemeenteGeboorte, buitenlandsePlaatsGeboorte, buitenlandseRegioGeboorte, landOfGebiedGeboorte, omschrijvingLocatieGeboorte | Nee | GGM |
| **MigratieIngeschrevenNatuurlijkPersoon** | Om gegevens vast te leggen over immigratie en emigratie. | soortMigratie, redenWijzigingMigratie, aangeverMigratie | Nee | GGM |
| **NationaliteitIngeschrevenNatuurlijkPersoon** | Gegevens over de nationaliteit. | nationaliteit, redenVerkrijging, redenVerlies, buitenlandsPersoonsnummer | Nee | GGM |
| **OverlijdenIngeschrevenNatuurlijkPersoon** | Gegevens over het overlijden van de ingeschreven natuurlijk persoon. | datumOverlijden, gemeenteOverlijden, buitenlandsePlaatsOverlijden, buitenlandseRegioOverlijden, omschrijvingLocatieOverlijden, landOfGebiedOverlijden | Nee | GGM |
| **VerblijfadresIngeschrevenNatuurlijkPersoon** | De gegevens over het verblijf en adres van de INGESCHREVEN NATUURLIJK PERSOON | adresHerkomst, beschrijvingLocatie | Nee | GGM |
| **VerstrekkingsbeperkingPartieelIngeschrevenNatuurlijkPersoon** | Een INGESCHREVEN NATUURLIJK PERSOON kan voor één of meerdere partijen kiezen voor wie een verstrekkingsbeperking geldt. | partij, omschrijvingDerde, gemeenteVerordening | Nee | GGM |

### Inburgering

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Gemeente** | Een gedeelte van het grondgebied van Nederland, ingesteld op basis van artikel 123 van de Grondwet. | gemeentecode, gemeentenaam, gemeentenaamNEN, gemeenteGeometrie, datumBeginGeldigheidGemeente, datumEindeGeldigheidGemeente, identificatie | Nee | Door KING toegevoegd objecttype, ontleend aan het GFO BG (maakt geen deel uit van enige basisregistratie). |

### KADASTRALE ONROERENDE ZAAK

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **KoopsomKadastraleOnroerendeZaak** | Het in een ter inschrijving aangeboden stuk vermelde bedrag, waarvoor 1 of meer onroerende zaken zijn verkregen. | koopsom, datumTransactie | Nee | GGM |

### KADASTRALE ONROERENDE ZAAK FILIATIE

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **AardFiliatie** | Een opsomming van redenen waarom kadastrale onroerende zaken aan elkaar gerelateerd kunnen zijn | codeAardFiliatie, naamAardFiliatie, datumBeginGeldigheidAardFiliatie, datumEindeGeldigheidAardFiliatie | Nee | GGM |

### KUNSTWERKDEEL

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **SoortKunstwerk** | Gegevens over het soort kunstwerk. | indicatiePlusBRPopulatie, typeKunstwerk | Nee | GGM |

### KVK

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **SBIActiviteit** | De hiërarchische indeling van economische activiteiten conform SBI (Standaard Bedrijfsindeling). | SBICode, naamActiviteit, datumIngangSBIActiviteit, datumEindeSBIActiviteit, hoofdniveau, hoofdniveauOmschrijving, SBIGroep, SBIGroepOmschrijving | Nee | GGM |
| **SBIActiviteitVestiging** | Aanduiding van de activiteit (en) van een vestiging conform de Standaard BedrijfsIndeling | indicatieHoofdactiviteit, SBICode | Nee | GGM |

### Kadastrale gemeenten referenties

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **KadastraleGemeente** | De mogelijke onderscheiden gedeeltes van het grondgebied van Nederland, volgens de Dienst Kadaster en de Openbare Registers, zoals nader omschreven in het Kadasterbesluit | kadastraleGemeentecode, naam, datumBeginGeldigheidKadastraleGemeente, datumEindeGeldigheidKadastraleGemeente | Nee | GGM |

### Kern:Personen

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **AdresBuitenland** | Toevoeging uit stelselcatalogus | datumAanvangAdresBuitenland, datumInschrijvingGemeente, datumVestigingNederland, gemeenteVanInschrijving, landAdresBuitenland, landWaarvandaanIngeschreven, omschrijvingVanDeAangifteAdreshouding, adresregelBuitenland1, adresregelBuitenland2, adresregelBuitenland3 | Nee | GGM |
| **Nationaliteit** | De hoedanigheid van tot een bepaalde natie te behoren. Het wettelijk onderdaan zijn van een bepaalde staat (staatsburgerschap). Nationale oorsprong. De rechtsverhouding tussen de betrokkene en de staat. | omschrijving, Nationaliteitcode, Datum ingang geldigheid, Datum einde geldigheid, Datum opnamen, Datum verlies nationaliteit, redenVerliesNLNationaliteit, redenVerkrijgingNLNationaliteit, Buitenlandse nationaliteit | Nee | GGM |
| **Verblijfstitel** | Rechtsgrond op basis waarvan men bevoegd is in een land te verblijven. Opmerkingen obv Key2Burgerzaken: De verblijfstitel heeft een ingangs- en vervaldatum, datum geldig en een opname datum RSGB3.0 onderkent alleen Datum einde en Datum ingang. Dat is onvoldoende om volgorde en geldigheid in tijd correct te bepalen | aanduidingVerblijfstitel, datumBeginGeldigheidVerblijfstitel, Verblijfstitel code, Datum begin, Datum einde, Datum Opname | Nee | GGM |

### Landen referentielijst

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **LandOfgebied** | Een gedeelte van de wereld met een eigen bestuur, waarvan de soevereiniteit in ieder geval door Nederland is erkend. | landcode, landnaam, datumIngangLand, datumEindeLand, landcodeISO | Nee | GGM |
| **VerblijfBuitenland** | De gegevens over het verblijf in het buitenland | adresregelBuitenland1, adresregelBuitenland2, adresregelBuitenland3, adresregelBuitenland4, adresregelBuitenland5, adresregelBuitenland6, landOfGebiedVerblijfadres | Nee | GGM |

### NATUURLIJK PERSOON

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **NaamgebruikNatuurlijkPersoon** | De naamgegevens waarmee de persoon heeft aangegeven aangeschreven te willen worden | adellijkeTitelNaamgebruik, geslachtsnaamstamNaamgebruik, aanhefAanschrijving | Nee | GGM |
| **SamengesteldeNaamNatuurlijkPersoon** | Gegevens over de naam van de NATUURLIJK PERSOON | voornamen, voorvoegsel, scheidingsteken, geslachtsnaamstam, predicaat, adellijkeTitel, namenreeks | Nee | GGM |

### OVERIG BOUWWERK

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **SoortOverigBouwwerk** | Gegevens over het soort overig bouwwerk. | indicatiePlusBRPopulatie, typeOverigBouwwerk | Nee | GGM |

### Partij

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Partij** | Een PARTIJ die bij de centrale voorzieningen van de BRP bekend is. | code, naam, soort, verstrekkingsbeperkingMogelijk, datumAanvangGeldigheidPartij, datumEindeGeldigheidPartij | Nee | GGM |

### REISDOCUMENT

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **AutoriteitAfgifteNederlandsReisdocument** | Een opsomming van de diverse coderingen van de autoriteiten die een Nederlands reisdocument kunnen afgegeven | code, omschrijving, datumBeginGeldigheidAutoriteitVanAfgifte, datumEindeGeldigheidAutoriteitVanAfgifte | Nee | BRP |

### Reden verkrijging nationaliteit

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **RedenVerkrijgingNationaliteit** | Tabel waarin de redenen staan voor opname van de Nederlandse nationaliteit. | redennummerVerkrijging, omschrijvingVerkrijging, datumAanvangGeldigheidVerkrijging, datumEindeGeldigheidVerkrijging | Nee | GGM |

### Reden verlies nationaliteit

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **RedenVerliesNationaliteit** | Tabel waarin de redenen staan voor beëindiging van de Nederlandse nationaliteit. | redennummerVerlies, omschrijvingVerlies, datumAanvangGeldigheidVerlies, datumEindeGeldigheidVerlies | Nee | GGM |

### Reidoscumentsoorten referenties

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Reisdocumentsoort** | Een opsomming van de modellen van de Nederlandse reisdocumenten. | reisdocumentcode, reisdocumentOmschrijving, datumBeginGeldigheidReisdocumentsoort, datumEindeGeldigheidReisdocumentsoort | Nee | GGM |

### SCHEIDING

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **SoortScheiding** | Gegevens over de soort scheiding | indicatiePlusBRPopulatie, typeScheiding | Nee | GGM |

### SPOOR

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **SoortSpoor** | Gegevens over het soort spoor. | indicatiePlusBRPopulatie, functieSpoor | Nee | GGM |

### SUBJECT

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **CorrespondentieadresBuitenland** | De gegevens over het buitenlands correspondentie (-post)adres in het buitenland | adresBuitenland1, adresBuitenland2, adresBuitenland3, adresBuitenland4, adresBuitenland5, adresBuitenland6, landCorrespondentieadres | Nee | GGM |
| **Postadres** | De gegevens die tezamen een postbusadres of antwoordnummeradres vormen | postcodePostadres, postadresType, postbusOfAntwoordnummer | Nee | GGM |
| **Rekeningnummer** | De gegevens inzake de bankrekening waarmee het SUBJECT in de regel financieel communiceert. | IBAN, BIC | Nee | GGM |

### Soorten grootte referenties

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **SoortGrootte** | Een opsomming van de soorten grootte zoals die kunnen voorkomen in een aktetekst van het Kadaster en aanduiden op welke wijze de grootte van een perceel is vastgesteld conform de waardelijst SoortGrootte van het Kadaster | codeSoortGrootte, naamSoortGrootte, datumBeginGeldigheidSoortGrootte, datumEindeGeldigheidSoortGrootte | Nee | GGM |

### Tekenwijze

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **ObjecttypeA** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **ObjecttypeB** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **ObjecttypeC** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **ObjecttypeD** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **ObjecttypeE** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **ObjecttypeF** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |
| **ObjecttypeG** | *(geen definitie in GGM)* | *(geen attributen)* | Nee | GGM |

### Tenaamstelling

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Aantekening** | Een Aantekening is een aanvulling op de registratie van een registergoed met betrekking tot feiten die gevolgen kunnen hebben voor de uitoefening van de rechten op dit registergoed. | aard, begrenzing, betreftGedeelteVanPerceel, datumEinde, datumEindeRecht, identificatie, omschrijving | Nee | GGM |

### Valutasoorten referenties

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **Valutasoort** | De mogelijke munteenheden waarin een geldbedrag kan worden uitgedrukt conform de waardelijst Valutasoort van het Kadaster | valutacode, naamValuta, datumBeginGeldigheidValutasoort, datumEindeGeldigheidValutasoort | Nee | GGM |

### Vastgoed WOZ

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **SoortWOZObject** | De mogelijke codes waarin een soort object kan worden uitgedrukt conform de uniforme soort objectcodelijst van de Waarderingskamer | soortobjectcode, naamSoortObjectcode, opmerkingenSoortObjectcode, datumBeginGeldigheidSoortObjectcode, datumEindeGeldigheidSoortObjectcode | Nee | GGM |

### Verkamering en Woonoverlast

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **BenoemdObject** | Een GEBOUWD OBJECT of een BENOEMD TERREIN | identificatie, datumBeginGeldigheid, datumEindeGeldigheid, geometriePunt, geometrieVlak | Ja | GGM |
| **Onbestemd Adres** | *Onbestemd Adres* is een adres-aanduiding die officieel door een bevoegde gemeentelijke instantie is vastgelegd, maar waarbij niet kan worden vastgesteld dat het een regulier woon- of verblijfsadres betreft. | huisletter, huisnummer, huisnummertoevoeging, postcode, straatnaam | Nee | GGM |

### Overig

| Entiteit | Definitie | Attributen | Abstract | Herkomst |
|---|---|---|---|---|
| **AcademischeTitel** | Een formeel via het Staatsblad gepubliceerde aanduiding van een wetenschappelijke of andere graad van opleiding welke bij aanschrijving voorafgaat aan de voornamen (dan wel de daarvan afgeleide naamgegevens) dan wel volgt op de achternaam. | codeAcademischeTitel, omschrijvingAcademischeTitel, positieAcademischeTitelTOVNaam, datumBeginGeldigheidTitel, datumEindeGeldigheidTitel | Nee | GGM |
| **AdresseerbaarObjectAanduiding** | Een door het bevoegde gemeentelijke orgaan als zodanig toegekende aanduiding van een VERBLIJFSOBJECT, een STANDPLAATS of een LIGPLAATS. | identificatie | Nee | GGM |
| **BenoemdTerrein** | Een STANDPLAATS, LIGPLAATS, of een OVERIG BENOEMD TERREIN. | identificatie | Ja | Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie). |
| **Buurt** | Een aaneengesloten gedeelte van een wijk, waarvan de grenzen zo veel mogelijk gebaseerd zijn op topografische elementen. | buurtcode, identificatieIMGeoBRT, buurtnaam, buurtgeometrie, datumBeginGeldigheidBuurt, datumEindeGeldigheidBuurt, identificatie | Nee | GGM |
| **GeboorteIngeschrevenPersoon** | Gegevens over de geboorte van de ingeschreven persoon. | datumGeboorte, geboorteplaats, geboorteland | Nee | GGM |
| **GebouwdObject** | Een VERBLIJFSOBJECT of een OVERIG GEBOUWD OBJECT | bouwkundigeBestemmingActueel, statusVoortgangBouw, brutoInhoud, oppervlakteObject, inwinningOppervlakte, identificatie | Ja | Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie). |
| **HandelsnamenMaatschappelijkeActiviteit** | {nog niet in NHR uitgewerkt} | handelsnaam, verkorteNaam, volgorde | Nee | GGM |
| **HandelsnamenVestiging** | {nog niet in NHR uitgewerkt} | handelsnaam, verkorteNaam, volgorde | Nee | GGM |
| **Land** | Een gedeelte van de wereld met een eigen bestuur, waarvan de soevereiniteit in ieder geval door Nederland is erkend. | landcode, landnaam, datumIngangLand, datumEindeLand, landcodeISOTweeletterig, datumEindeFictief, landcodeISODrieletterig | Nee | GGM |
| **Ligplaats** | Definitie Een ligplaats is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen plaats in het water al dan niet aangevuld met een op de oever aanwezig terrein of een gedeelte daarvan, die bestemd is voor het permanent afmeren van een voor woon-, bedrijfsmatige of recreatieve doeleinden geschikt drijvend object Beschrijving Een plaats in het water met soms ook een (deel van een) terrein op de oever. Deze plaats moet kunnen worden gebruikt door een drijvend object dat langere tijd daar wordt vastgemaakt. Het drijvende object moet geschikt zijn om in te wonen, om een bedrijf in te hebben of om voor plezier in te verblijven. Bijvoorbeeld een woonboot. De gemeente mag zeggen of er voor de BAG ergens een ligplaats komt. | ligplaatsidentificatie, indicatieGeconstateerdeLigplaats, ligplaatsstatus, inOnderzoek, datumDocument, documentNummer | Nee | GGM |
| **NaamAanschrijvingNatuurlijkPersoon** | De naamgegevens waarmee de persoon heeft aangegeven aangeschreven te willen worden | geslachtsnaamAanschrijving, voorlettersAanschrijving, voornamenAanschrijving, aanhefAanschrijving | Nee | GGM |
| **NaamNatuurlijkPersoon** | Gegevens over de naam van de natuurlijk persoon | voornamen, geslachtsnaam, voorvoegselGeslachtsnaam, adellijkeTitelOfPredikaat | Nee | GGM |
| **Nationaliteit** | De hoedanigheid van tot een bepaalde natie te behoren. | codeNationaliteit, nationaliteitOmschrijving, datumBeginGeldigheidNationaliteit, datumEindeGeldigheidNationaliteit | Nee | GGM |
| **NederlandseNationaliteitIngeschrevenPersoon** | Gegevens over de nationaliteit. | aanduidingBijzonderNederlanderschap, redenVerkrijgingNederlandseNationaliteit, redenVerliesNederlandseNationaliteit, nationaliteit | Nee | GGM |
| **Nummeraanduiding** | Een door het bevoegde gemeentelijke orgaan als zodanig toegekende aanduiding van een VERBLIJFSOBJECT, een STANDPLAATS of een LIGPLAATS. | huisletter, huisnummer, huisnummertoevoeging, postcode, datumBeginGeldigheidNummeraanduiding, DatumEindeGeldigheidNummeraanduiding, status, geconstateerd, identificatie, typeAdresseerbaarObject, inOnderzoek | Ja | Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie). |
| **OpenbareRuimte** | Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorziene buitenruimte die binnen één woonplaats is gelegen | IdentificatiecodeOpenbareRuimte, identificatieIMGeoOPR, statusOpenbareRuimte, naamOpenbareRuimte, indicatieGeconstateerdeOpenbareRuimte, typeOpenbareRuimte, straatnaam, huisnummerrangeEvenNummers, HuisnummerrangeOnevenNummers, huisnummerrangeEvenEnOnevenNummers, labelNaamOpenbareRuimte, openbareRuimteGeometrie, wegsegment, datumBeginGeldigheidOpenbareRuimte, datumEindeGeldigheidOpenbareRuimte, inOnderzoek | Nee | GGM |
| **OverlijdenIngeschrevenPersoon** | Gegevens over het overlijden van de ingeschreven persoon. | datumOverlijden, overlijdensplaats, landOverlijden | Nee | GGM |
| **Pand** | De kleinste bij de totstandkoming functioneel en bouwkundig-constructief zelfstandige eenheid die direct en duurzaam met de aarde is verbonden en betreedbaar en afsluitbaar is. | pandidentificatie, pandstatus, statusVoortgangBouw, oorspronkelijkBouwjaarPand, oppervlaktePand, brutoInhoudPand, indicatieGeconstateerdPand, hoogsteBouwlaagPand, laagsteBouwlaagPand, pandgeometrieBovenaanzicht, inwinningGeometrieBovenaanzicht, pandgeometrieMaaiveld, inwinningGeometrieMaaiveld, relatieveHoogteliggingPand, LOD1GeometriePand, LOD2GeometriePand, lod3GeometriePand, identificatieBGTPND, indicatiePlanobject, labelNummeraanduidingreeks, datumBeginGeldigheidPand, datumEindeGeldigheidPand, geometriePunt | Nee | GGM |
| **Provincie** | Een gedeelte van de wereld met een eigen bestuur, waarvan de soevereiniteit in ieder geval door Nederland is erkend. | provinciecode, provincienaam, datumIngangProvincie, datumEindeProvincie, hoofdstad, oppervlakte, oppervlakteLand | Nee | GGM |
| **Standplaats** | Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen terrein of gedeelte daarvan dat bestemd is voor het permanent plaatsen van een niet direct en niet duurzaam met de aarde verbonden en voor woon -, bedrijfsmatige, of recreatieve doeleinden geschikte ruimte. | standplaatsidentificatie, indicatieGeconstateerdeStandplaats, standplaatsstatus | Nee | GGM |
| **Valuta** | De hoedanigheid van tot een bepaalde natie te behoren. | valutacode, naam, datumBeginGeldigheid, datumEindeGeldigheid | Nee | GGM |
| **VerblijfBuitenlandSubject** | De gegevens over het verblijf in het buitenland | adresBuitenland1, adresBuitenland2, adresBuitenland3, landVerblijfadres | Nee | GGM |
| **VerblijfadresIngeschrevenPersoon** | De gegevens over het verblijf en adres van de INGESCHREVEN PERSOON | adresHerkomst, beschrijvingLocatie | Nee | GGM |
| **Verblijfsobject** | De kleinste binnen één of meer panden gelegen en voor woon -, bedrijfsmatige, of recreatieve doeleinden geschikte eenheid van gebruik die ontsloten wordt via een eigen afsluitbare toegang vanaf de openbare weg, een erf of een gedeelde verkeersruimte, onderwerp kan zijn van goederenrechtelijke rechtshandelingen en in functioneel opzicht zelfstandig is. | verblijfsobjectidentificatie, verblijfsobjectstatus, indicatieGeconstateerdVerblijfsobject, hoogsteBouwlaagVerblijfsobject, laagsteBouwlaagVerblijfsobject, toegangBouwlaagVerblijfsobject, soortWoonobject, aantalKamers, inOnderzoek, ontsluitingVerdieping | Nee | GGM |
| **Verblijfstitel** | Rechtsgrond op basis waarvan men bevoegd is in een land te verblijven. | datumAanvangGeldigheidVerblijfstitel, datumEindeGeldigheidVerblijfstitel, verblijfstitelNumeriek, verblijfstitelOmschrijving | Nee | GGM |
| **Wijk** | Een aaneengesloten gedeelte van het grondgebied van een gemeente, waarvan de grenzen zo veel mogelijk zijn gebaseerd op sociaal-geografische kenmerken. | wijkcode, identificatieIMGeoWYK, wijknaam, geometrieWijk, datumBeginGeldigheidWijk, datumEindeGeldigheidWijk, identificatie | Nee | GGM |
| **Woonplaats** | Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorzien gedeelte van het grondgebied van de gemeente. | woonplaatsIdentificatie, woonplaatsNaam, woonplaatsNaamNEN, indicatieGeconstateerdeWoonplaats, woonplaatsStatus, geometrieWoonplaats, datumBeginGeldigheidWoonplaats, datumEindeGeldigheidWoonplaats, inOnderzoek | Nee | GGM |

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
    └── Ingezetene
```

```
KadastraleOnroerendeZaak (abstract)
    └── Appartementsrecht
    └── KadastraalPerceel
```

```
NatuurlijkPersoon (abstract)
    └── IngeschrevenPersoon
```

```
Nummeraanduiding (abstract)
    └── OverigeAdresseerbaarObjectAanduiding
    └── OverigeAdresseerbaarObjectAanduiding
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
    └── NatuurlijkPersoon
    └── NietNatuurlijkPersoon
```

## Relatiediagrammen

```
Adresaanduiding ──── Nummeraanduiding
Appartementsrechtsplitsing ──── SplitsingstekeningReferentie
BenoemdObject ──── BenoemdObject (De verwijzing naar vervallen BENOEMD(e) OBJECT(en) waaruit het BENOEMD OBJECT is ontstaan en naar BENOEMD(e) OBJECT (en) waarin een vervallen BENOEMD OBJECT is overgegaan.)
Briefadres [0..*] ──── Nummeraanduiding [1..1]
Buurt ──── Wijk (De wijk waarin de buurt is gelegen.)
FunctioneelGebied ──── SoortFunctioneelGebied
Gebied [0..1] ──── Buurt [0..1]
GeboorteIngeschrevenNatuurlijkPersoon ──── Woonplaats
Gemeente ──── Gemeente (De nieuwe GEMEENTE waarin de GEMEENTE bij zijn opheffing c.q. na herindeling is overgegaan.)
Huishouden ──── IngeschrevenPersoon
IngeschrevenPersoon [1..*] ──── Briefadres [0..1]
IngeschrevenPersoon [1..1] ──── IngeschrevenPersoon [1..1]
IngeschrevenPersoon ──── Reisdocument
Ingezetene ──── Verblijfstitel (De verwijzing naar de VERBLIJFSTITEL die aangeeft over welke verblijfsrechtelijke status de ingezetene beschikt.)
KadastraleOnroerendeZaak [1..1] ──── KadastraleOnroerendeZaak [0..*]
KadastraleOnroerendeZaak ──── KadastraleOnroerendeZaak (De verwijzing naar andere KADASTRALE ONROERENDE ZAAKen waaruit de KADASTRALE ONROERENDE ZAAK is ontstaan.)
KadastraleOnroerendeZaak ──── KoopsomKadastraleOnroerendeZaak
KadastraleOnroerendeZaak ──── LocatieKadastraleOnroerendeZaak
KadastraleOnroerendeZaakAantekening ──── KadastraleOnroerendeZaak (De KADASTRALE ONROERENDE ZAAK waarbij de AANTEKENING geplaatst is.)
Kunstwerkdeel ──── SoortKunstwerk
MaatschappelijkeActiviteit ──── NatuurlijkPersoon (nog niet in NHR uitgewerkt)
MaatschappelijkeActiviteit ──── Rechtspersoon
NatuurlijkPersoon [1..1] ──── Nationaliteit [1..*]
NietNatuurlijkPersoon ──── NatuurlijkPersoon
NietNatuurlijkPersoon ──── Vestiging
Nummeraanduiding ──── AdresseerbaarObjectAanduiding (De unieke aanduiding van de Nummeraanduiding die in het kader van de Basisregistratie Adressen en Gebouwen is aangemerkt als het hoofdadres van een adresseerbaar object.)
Nummeraanduiding ──── Buurt (De BUURT waarin een BENOEMD OBJECT is gelegen.)
Nummeraanduiding ──── Gebied
Nummeraanduiding ──── OpenbareRuimte (De unieke aanduiding van een OPENBARE RUIMTE waaraan het object, waaraan de ADRESSEERBAAR OBJECT AANDUIDING is toegekend, is gelegen.)
Nummeraanduiding ──── Woonplaats (De unieke aanduiding van de WOONPLAATS waarbinnen het object, waaraan de ADRESSEERBAAR OBJECT AANDUIDING is toegekend, is gelegen.)
ObjecttypeA ──── ObjecttypeB
ObjecttypeD ──── ObjecttypeB
ObjecttypeE ──── ObjecttypeF
ObjecttypeE ──── ObjecttypeG
OntbindingHuwelijk/geregistreerdPartnerschap ──── Woonplaats (De woonplaats van een door het bevoegde gemeentelijk orgaan als zodanig aangewezen gedeelte van het gemeentelijk grondgebied waar het huwelijk is ontbonden, dan wel het geregistreerd partnerschap is beëindigd.)
OpenbareRuimte ──── Woonplaats (Unieke aanduiding van de woonplaats waarbinnen een OPENBARE RUIMTE is gelegen.)
OverigBenoemdTerrein ──── OverigeAdresseerbaarObjectAanduiding (De OVERIGE ADRESSEERBAAR OBJECT AANDUIDING waaronder het officiële adres is opgenomen.)
OverigBouwwerk ──── SoortOverigBouwwerk
OverigGebouwdObject ──── OverigBouwwerk (Een OVERIG BOUWWERK dat een equivalent is van een OVERIG GEBOUWD OBJECT.)
OverigGebouwdObject ──── OverigeAdresseerbaarObjectAanduiding (De OVERIGE ADRESSEERBAAR OBJECT AANDUIDING waaronder het officiële adres is opgenomen.)
OverlijdenIngeschrevenNatuurlijkPersoon ──── Woonplaats (De naam van een door het bevoegde gemeentelijk orgaan als zodanig aangewezen gedeelte van het gemeentelijk grondgebied waar de persoon is overleden.)
Postadres ──── Woonplaats (De woonplaats die behoort bij het postadres van het SUBJECT)
Rechtspersoon [1..1] ──── AdresBuitenland [0..1]
Rechtspersoon ──── Tenaamstelling
Scheiding ──── SoortScheiding
SluitingOfAangaanHuwelijkOfGeregistreerdPartnerschap ──── Woonplaats (De naam van een door het bevoegde gemeentelijk orgaan als zodanig aangewezen gedeelte van het gemeentelijk grondgebied waar het huwelijk is gesloten of het geregistreerd partnerschap is aangegaan.)
Spoor ──── SoortSpoor
Tenaamstelling [1..1] ──── Aantekening [0..*]
Tenaamstelling ──── ZakelijkRecht (Een verwijzing naar het recht dat door een persoon wordt uitgeoefend op een kadastrale onroerende zaak.)
VerblijfadresIngeschrevenNatuurlijkPersoon ──── AdresseerbaarObjectAanduiding (De NUMMERAANDUIDING bij het ADRESSEERBAAR OBJECT waarin de INGESCHREVEN NATUURLIJK PERSOON verblijft en die hij/zij gekozen heeft als inschrijvingsadres.)
VerblijfadresIngeschrevenNatuurlijkPersoon ──── Ligplaats (De LIGPLAATS behorende bij het woonadres van de persoon)
VerblijfadresIngeschrevenNatuurlijkPersoon ──── Standplaats (De STANDPLAATS behorende bij het woonadres van de persoon)
VerblijfadresIngeschrevenNatuurlijkPersoon ──── Verblijfsobject (Het VERBLIJFSOBJECT behorende bij het woonadres van de persoon)
VerblijfadresIngeschrevenNatuurlijkPersoon ──── Woonplaats
Verblijfsobject ──── Pand (De unieke aanduidingen van de PANDEN waarvan het VERBLIJFSOBJECT onderdeel uitmaakt.)
Vestiging ──── BenoemdObject (De BENOEMDe OBJECTen waarin zich de gedeelten van een VESTIGING bevinden die niet beschouwd worden als hoofdlocatie voor de uitvoering van de activiteiten van deze VESTIGING.)
Vestiging ──── MaatschappelijkeActiviteit (De MAATSCHAPPELIJKE ACTIVITEIT die activiteiten uitoefent voor een VESTIGING)
Vestiging ──── Nummeraanduiding (De ADRESSEERBAAR OBJECT AANDUIDING bij het BENOEMD OBJECT waarin de VESTIGING (één van) haar lokatie(s) heeft en die bij inschrijving gekozen is als vestigingssadres.)
Vestiging ──── SBIActiviteitVestiging
WOZ-Waarde ──── WOZ-object (De aan het WOZ-OBJECT gerelateerde WOZ-WAARDEn)
WOZ-deelobject ──── WOZ-object (De unieke aanduidingen van de WOZ-DEELOBJECTen waaruit het WOZ-OBJECT bestaat.)
WOZ-object [0..*] ──── KadastraleOnroerendeZaak [0..*]
WOZ-object ──── KadastraleOnroerendeZaak (De unieke aanduidingen van de KADASTRALE ONROERENDE ZAAKen opgenomen in de Basis Registratie Kadaster die geheel of gedeeltelijk deel uitmaken van het WOZ-OBJECT.)
Wijk ──── Gemeente (De gemeente waarin de wijk is gelegen.)
Woonplaats ──── Gemeente (De GEMEENTE waarin de WOONPLAATS is gelegen.)
ZakelijkRecht ──── KadastraleOnroerendeZaak (Een verwijzing naar de KADASTRALE ONROERENDE ZAAK waarop het ZAKELIJK RECHT betrekking heeft.)
ZakelijkRecht ──── Tenaamstelling (Verwijzing naar de TENAAMSTELLING waarop het ZAKELIJK RECHT beperking heeft.)
ZakelijkRecht ──── ZakelijkRecht (Verwijzing naar het ZAKELIJK RECHT waarmee het onderhavige ZAKELIJK RECHT is belast.)
Zekerheidsrecht ──── KadastraleOnroerendeZaak (De KADASTRAAL ONROERENDE ZAAK waarop een ZEKERHEIDSRECHT rust.)
Zekerheidsrecht ──── Tenaamstelling (De TENAAMSTELLING waarop een ZEKERHEIDSRECHT rust.)
```

## Observaties

- Dit beleidsdomein bevat 128 Objecttype-entiteiten (+ 71 Enumeraties, 7 diagramhulpobjecten zonder stereotype).
- Entiteiten zijn gegroepeerd in 151 diagramgroepen: (Zaak)objecten (2), AANDUIDING ADRES OBJECT (2), AANDUIDING LIGGING OBJECT (1), AANDUIDING LOCATIE OVERIG GEBOUWD OBJECT (1), ADRESSEERBAAR OBJECT AANDUIDING (4), APPARTEMENTRECHTSPLITSING (4), ARK codes kadastrale gemeenten referenties (1), Aanduiding verblijfsrecht (2), Aard aantekeningen (1), Aard zakelijke rechten referenties (2), Adresseerbare Objecten (1), Archief Relaties met Kern (2), BEGROEID TERREINDEEL (1), BENOEMD OBJECT (3), BRK (8), Betrokkene (2), Burgerzaken (3), Codes cultuur onbebouwd referenties (2), Cultuur codes bebouwd referenties (2), Deelobjectcodereferenties (2), Detaillering Kadastrale Onroerende Zaken en Rechten met attributen (11), Detaillering Kadastrale Onroerende Zaken en Rechten op hoofdlijnen (11), Detaillering Subjecten  (5), Detaillering WOZ-objecttypen met attributen (15), Detaillering WOZ-objecttypen op hoofdlijnen (15), Detaillering abstracte en concrete adres & gebouw objecttypen (3), Detaillering adressen, gebouwen en terreinen met attributen (3), Detaillering adressen, gebouwen en terreinen op hoofdlijnen (4), Detaillering concreten en abstracte  Kadastrale Onroerende Zaken objecttypen (3), Detaillering subjecten met attributen (8), Detaillering subjecten op hoofdlijnen (9), Diagram Adresaanduiding en BAG (1), Diagram Economie (4), Diagram Gebied Vestiging en Adres (6), Diagram Griffie (3), Diagram IMBOR vs IMGeo (1), Diagram Inkoop Inhuur (1), Diagram Monumenten (1), Diagram Sportbeleid (1), Diagram Sportbeleid Locaties (1), Diagram Vergunningen en Meldingen (1), Dienstverlening en Klanten (2), FUNCTIONEEL GEBIED (2), GEBOUWINSTALLATIE (1), Gemeente Begrafenissen (2), Generieke entiteiten Erfgoed (1), Gezag (2), HUWELIJK/GEREGISTREERD PARTNERSCHAP (3), Hoofdobjecten IMGeo en Beheerobjecten  (18), Huishouden en Huwelijk (4), INGESCHREVEN NATUURLIJK  PERSOON (9), INRICHTINGSELEMENT (1), Inburgering (2), Ingeschreven natuurlijk persoon (2), KADASTRAAL ONROERENDE ZAAK AANTEKENING (3), KADASTRAAL PERCEEL (1), KADASTRALE ONROERENDE ZAAK (6), KADASTRALE ONROERENDE ZAAK FILIATIE (2), KUNSTWERKDEEL (2), KVK (7), Kadastrale gemeenten referenties (2), Kern: Detaillering in Subjecten (5), Kern:Gemeente Wijk en buurt (1), Kern:Overige geo objecten op hoofdlijnen (9), Kern:Personen (9), Kern:Verwijzing naar Personen  (3), LIGPLAATS (1), Landen referentielijst (6), MAATSCHAPPELIJKE ACTIVITEIT (3), MOR 2.0 (1), Meldingen Graafwerkzaamheden (1), Model Parkeren (1), NATUURLIJK PERSOON (5), NHR (7), NIET-NATUURLIJK PERSOON (2), NUMMERAANDUIDING (3), ONBEGROEID TERREINDEEL (1), ONDERSTEUNEND WATERDEEL (1), ONDERSTEUNEND WEGDEEL (1), OPENBARE RUIMTE (2), OVERBRUGGINSDEEL (1), OVERIG BENOEMD TERREIN (2), OVERIG BOUWWERK (3), OVERIG GEBOUWD OBJECT (3), OVERIGE ADRESSEERBAAR OBJECT AANDUIDING (3), OVERIGE SCHEIDING (1), Objecten bij Vergunningaanvraag (8), Omgevingswet Verzoeken (IMAM) (1), Onderwijs: Relaties met Kern (2), Overige geo objecten met attributen (17), Overige geo objecten op hoofdlijnen (17), PAND (1), PERSOON (4), POC Vastgoed  (3), Partij (2), Prinsenhof Collectie (1), Prinsenhof Events en Relaties (1), REISDOCUMENT (3), Reden verkrijging nationaliteit (2), Reden verlies nationaliteit (2), Reidoscumentsoorten referenties (2), Relatie BRP en BAG (3), Relaties Sociaal Domein tot Kern (3), Relaties met Kern (2), Relaties tot kern details (3), Ruimte Adressen, gebouwen en terreinen (3), Ruimte WOZ en Benoemd Object (6), SCHEIDING (2), SPOOR (2), STANDPLAATS (1), SUBJECT (5), Schouwrondes Beheersobjecten (1), Schuldhulp Client (2), Schuldhulp Hoofdlijnen (2), Schuldhulp Schuldhulporganisatie (1), Sociaal Domein Beschikking en Voorziening: Domain Objects (3), Sociale Relaties (2), Soorten grootte referenties (2), Subject (1), Subsidies (1), TENAAMSTELLING (3), TUNNELDEEL (1), Tekenwijze (7), Tenaamstelling (2), VEGETATIEOBJECT (1), VERBLIJFSOBJECT (1), VESTIGING (4), Valutasoorten referenties (1), Vastgoed Domeinmodel  (2), Vastgoed Leveranciers (1), Vastgoed Relaties met Kern  (1), Vastgoed WOZ (6), Vastgoed verankering RSGB IMBAG (13), Verkamering en Woonoverlast (4), Verkeer en Vervoer: Stremmingen (1), Voorvoegsel referenties (2), Vroegsignalering (4), Vroegsignalering Details (1), Vroegsignalering Klein (2), WATERDEEL (1), WEGDEEL (1), WOONPLAATS (1), WOZ-DEELOBJECT (3), WOZ-OBJECT (6), WOZ-WAARDE (2), Woningbouwprojecten (2), ZAKELIJK RECHT (4), ZAKELIJK RECHT PERSOON (2), ZEKERHEIDSRECHT (4), Zorgmelding (3), mGBA (5).
- Er zijn 46 generalisatierelaties aanwezig.
