---
type: analyse
titel: GGM Terugmeldingen
datum: 2026-06-19
aanleiding: Centraal overzicht van bevindingen uit BO-toetsing die aan het GGM-team teruggekoppeld moeten worden
---

# GGM Terugmeldingen

Bevindingen uit de BO-toetsing per domein. Elk item is een verschil tussen het GGM en het GEMMA bedrijfsobjectenmodel dat teruggekoppeld moet worden aan het GGM-beheerteam.

## Overzicht

| # | Domein | Entiteit | Type | Bevinding | Status |
|---|--------|----------|------|-----------|--------|
| 1 | Asiel en Integratie | — | hiaat | Asielopvangfase volledig ontbreekt in GGM (opvanglocatie, bestuursovereenkomst, exploitatievorm) | open |
| 2 | Asiel en Integratie | Gezinsmigrant en Overige migrant | definitie | GGM-definitie is modelbeschrijving ("Object Inburgeraar is gespecialiseerd in..."), geen begripsdefinitie | open |
| 3 | Asiel en Integratie | Inburgeringsplicht | definitie | GGM-definitie is technische beschrijving ("Bevat de uitkomst Leerbaarheidstoets..."), geen begripsdefinitie | open |
| 4 | Bestuur | Stembureau | hiaat | Registratieobject voor fysieke locaties waar stemmingen plaatsvinden (adres, capaciteit, toegankelijkheid); dataobject vergelijkbaar met BAG-locatie maar met verkiezings-specifieke properties | open |
| 5 | Bestuur | Gemeenschappelijke Regeling | hiaat | Registratieobject voor juridische samenwerkingsentiteiten (Wgr) met eigen bestuur, personeelssterkte, begroting, deelnemers; dataobject zou onder Bestuur of Interne Organisatie passen | open |
| 6 | Milieu | — | hiaat | Taakveld 7 mist beleidsdomein Bodem/Grondwater/Milieu. Alleen Afval is gemodelleerd. Het hele domein van gemeentelijk bodembeheer (wettelijke taak) ontbreekt: bodemkwaliteitskaarten, verontreinigingsregistratie, saneringsplannen, grondwatermonitoring, grondverzet, bodemenergiesystemen. | open |
| 7 | Milieu | Bodemkwaliteitskaart | hiaat | Wettelijk verplicht instrument (Besluit kwaliteit leefomgeving) met vastgestelde bodemkwaliteit per zone. Elke gemeente kan dit opstellen; basis voor beoordeling grondhergebruik. Governance-object, zou onder taakveld 7 passen. | open |
| 8 | Milieu | Bodemverontreiniging | hiaat | Registratie van verontreinigingslocaties (type stoffen, omvang, diepte, saneringsstatus). Gemeente is bevoegd gezag. Vergelijkbaar met hoe BAG locaties modelleert maar dan voor milieu. Zou onder taakveld 7 passen. | open |
| 9 | Milieu | Saneringsplan | hiaat | Registratieobject dat gemeenten als bevoegd gezag opstellen en beheren (Wbb art. 39/55e). Twee vormen: gevalgericht en gebiedsgericht. Zou onder taakveld 7 passen. | open |
| 10 | Milieu | Grondwatermeetpunt | hiaat | Fysiek meetpunt (peilbuis) in monitoringsnetwerk voor grondwaterkwaliteit. GGM heeft wel Filterput (BOR) maar dat is een drainageobject, geen milieumeetpunt. Zou onder taakveld 7 passen. | open |
| 11 | Milieu | Grondverzet | hiaat | Meldingsplichtige grondverplaatsing (Besluit bodemkwaliteit) met herkomst, bestemming, kwaliteit, volume. Gemeente beoordeelt en houdt toezicht. Zou onder taakveld 7 passen. | open |
| 12 | Milieu | Bodemenergiesysteem | hiaat | Vergunningsplichtige WKO-installatie in de ondergrond. Registratie met locatie, capaciteit, diepte. Raakt zowel taakveld 7 (milieu) als energiedomein. | open |
| 13 | Economie | Standplaats | scope | GGM-entiteit Standplaats staat onder beleidsdomein Musea (taakveld 5). Het is echter een breed APV-concept dat primair onder Economie (taakveld 3) hoort. Ontbreken attributen voor branchering, type (dag/seizoen/incidenteel), vergunningsstatus. | open |
| 14 | Economie | Warenmarkt | hiaat | Registreerbaar dataobject dat ontbreekt in het GGM: georganiseerde periodieke verkoop op aangewezen locatie, gereguleerd via Marktverordening. Eigenschappen: locatie, frequentie, type, branchering, aantal kramen. Zou onder taakveld 3 Economie passen. | open |
| 15 | Energie en Klimaat | — | hiaat | Taakveld 7 mist een beleidsdomein Energie/Klimaat. Alleen Afval is gemodelleerd. Het hele domein van de gemeentelijke energietransitie ontbreekt: warmtenetten, opwekgebieden, warmteprogramma. Vergelijkbaar met het ontbreken van Bodem/Milieu onder hetzelfde taakveld. | open |
| 16 | Energie en Klimaat | Warmtenet | hiaat | Fysieke warmte-infrastructuur voor levering aan gebouwen. Registreerbare eigenschappen: locatie (tracé), capaciteit, eigenaar/exploitant, aangesloten gebouwen, warmtebronnen, status. Wettelijke grondslag via Wcw. Zou onder een nieuw beleidsdomein Energie (taakveld 7) passen. | open |
| 17 | Energie en Klimaat | Opwekgebied | hiaat | Aangewezen locatie voor grootschalige energieopwek. Registreerbare eigenschappen: locatie (geometrie), type opwek (zon/wind), capaciteit (MW), status, relatie met omgevingsplan en RES. Wettelijke grondslag via Omgevingswet. Zou onder een nieuw beleidsdomein Energie (taakveld 7) passen. | open |
| 18 | Evenementen | OpenbareActiviteit | definitie | Definitie "Activiteit in het publieke domein" is te breed (omvat ook betogingen, markten). Entiteit mist relaties met locatie en vergunning. Attributen te beperkt voor gemeentelijke praktijk (ontbreekt: omvang, type, beoordelingsresultaat). | open |
| 19 | Evenementen | Evenementenlocatie | hiaat | Aangewezen fysieke locatie voor evenementen met eigen profiel (kaders voor dagen, omvang, geluid, rustperiodes). GGM kent generieke Locatie-entiteiten maar geen evenementenlocatie. Registreerbare eigenschappen: locatie (geometrie), type ondergrond, maximale capaciteit, geluidsnorm, rustperiode. Zou onder taakveld 1 of een nieuw beleidsdomein Evenementen passen. | open |
| 20 | Evenementen | Evenementenvergunning | hiaat | Vergunning voor het organiseren van een evenement. GGM kent vergunningen alleen als domeinspecifieke entiteiten (Omgevingsvergunning, Parkeervergunning, Ligplaatsontheffing) zonder overkoepelend concept. Registreerbare eigenschappen: organisator, locatie, datum, voorwaarden, status. Bredere vraag: er ontbreekt een generiek vergunningsconcept in het GGM. | open |
| 21 | Mobiliteit | Parkeerzone (GEMMA-naam) | definitie | GEMMA-naam in het GGM is "Perkeerzone" (typefout). Moet "Parkeerzone" zijn. GUID: e5293eea-47b8-4091-8ac3-b28139a17c9f | open |
| 22 | Mobiliteit | — | hiaat | Taakveld 2 mist de functionele mobiliteitslaag. GGM Mobiliteit (7 entiteiten) modelleert alleen verkeersmanagement (stremmingen, gladheid, verkeersbesluiten). Routes, knooppunten, haltes, hubs en zones ontbreken volledig. | open |
| 23 | Mobiliteit | Hoofdfietsroute | hiaat | Aangewezen fietsroute met kwaliteitseisen. Gemeente registreert: route (geometrie), kwaliteitsklasse, type (doorstroom/bestemming). Fijnmazig netwerk van ~50 routes. Zou onder beleidsdomein Mobiliteit passen. | open |
| 24 | Mobiliteit | OV-knooppunt | hiaat | Multimodaal overstappunt op kruising van OV-verbindingen. Gemeente registreert: locatie, type, modaliteiten, voorzieningen. Benoemde locaties (Overvecht, Lunetten, USP, etc.). Zou onder beleidsdomein Mobiliteit passen. | open |
| 25 | Mobiliteit | OV-lijn | hiaat | Tram- of buslijn met route, dienstregeling en frequentie. Gemeente/concessieverlener registreert: lijnnummer, route, frequentie, type (tram/bus/HOV). Zou onder beleidsdomein Mobiliteit passen. | open |
| 26 | Mobiliteit | Halte | hiaat | Fysieke OV-voorziening waar reizigers in- en uitstappen. Gemeente registreert: locatie, type, voorzieningen, toegankelijkheid. Zou onder beleidsdomein Mobiliteit passen. | open |
| 27 | Mobiliteit | P+R-locatie | hiaat | Parkeer-en-reisvoorziening voor overstap auto naar OV/fiets. Gemeente registreert: locatie, capaciteit, OV-aansluiting, tarief. Zou onder beleidsdomein Mobiliteit passen. | open |
| 28 | Mobiliteit | Mobiliteitshub | hiaat | Multimodaal overstappunt met deelvoertuigen en voorzieningen. Gemeente registreert: locatie, type (XL/buurt), aangeboden modaliteiten, voorzieningen. Zou onder beleidsdomein Mobiliteit passen. | open |
| 29 | Mobiliteit | Laadpaal | hiaat | Oplaadvoorziening voor elektrische voertuigen. Gemeente registreert: locatie, type (normaal/snellader), vermogen, exploitant. Verschilt van GGM Installatie (BOR) in functionele betekenis. Zou onder beleidsdomein Mobiliteit of Parkeren passen. | open |
| 30 | Mobiliteit | Logistieke Route | hiaat | Voorkeursroute voor goederenvervoer met kwaliteitseisen. Gemeente registreert: route (geometrie), type (I/II), kwaliteitseisen. 3-jaarlijkse actualisatie. Zou onder beleidsdomein Mobiliteit passen. | open |
| 31 | Mobiliteit | Laad- en Losplaats | hiaat | Aangewezen locatie voor laden en lossen van goederen. Gemeente registreert: locatie, type, venstertijden, beperkingen. Zou onder beleidsdomein Mobiliteit passen. | open |
| 32 | Mobiliteit | Stadsdistributiepunt | hiaat | Overslaglocatie voor bundeling en distributie van goederen. Gemeente registreert: locatie, capaciteit, modaliteiten, bestemming. Zou onder beleidsdomein Mobiliteit passen. | open |
| 33 | Mobiliteit | Zero-emissiezone | hiaat | Zone waar alleen emissieloze voertuigen mogen opereren. Gemeente registreert: geometrie, ingangsdatum, voertuigcategorieën, handhavingsregime. Juridische grondslag via verkeersbesluit. Zou onder beleidsdomein Mobiliteit passen. | open |
| 34 | Mobiliteit | Overslagpunt | hiaat | Locatie voor overslag van goederen tussen weg, water en spoor. Gemeente registreert: locatie, modaliteiten, capaciteit. Zou onder beleidsdomein Mobiliteit passen. | open |
| 35 | Mobiliteit | Bouwlogistiek Centrum | hiaat | Tijdelijke hub voor gebundelde aanvoer van bouwmaterialen. Gemeente registreert: locatie, bouwproject, capaciteit, looptijd. Zou onder beleidsdomein Mobiliteit passen. | open |
| 36 | Milieu | — | hiaat | Taakveld 7 mist beleidsdomein Luchtkwaliteit. Gemeenten beheren milieuzones, luchtkwaliteitsmeetpunten, rookvrije zones en vuurwerkvrije zones als dataobjecten. Vergelijkbaar met het ontbreken van Bodem/Milieu en Energie onder hetzelfde taakveld. | open |
| 37 | Milieu | Milieuzone | hiaat | Afgebakend gebied met emissieklasse-eisen per voertuigcategorie. Vergelijkbaar met Parkeerzone (Parkeren) qua opzet. Juridische grondslag via verkeersbesluit. Registreerbare eigenschappen: grenzen, voertuigcategorie, emissieklasse-eis, ingangsdatum. Zou onder Mobiliteit (taakveld 2) of Luchtkwaliteit (taakveld 7) passen. NB: Zero-emissiezone (#33) is subtype van milieuzone. | open |
| 38 | Milieu | Luchtkwaliteitsmeetpunt | hiaat | Fysieke meetlocatie voor luchtverontreinigende stoffen. Vergelijkbaar met Verkeerstelling (Mobiliteit) qua opzet. Registreerbare eigenschappen: locatie, type meting (NO2/PM), beheerder, meetreeksen. Zou onder een nieuw beleidsdomein Luchtkwaliteit (taakveld 7) passen. | open |
| 39 | Milieu | Vuurwerkvrije zone | hiaat | Aangewezen zone met vuurwerkverbod. Registreerbare eigenschappen: geometrie, aanwijzingsbesluit, ingangsdatum. Zou onder taakveld 1 (Veiligheid) of taakveld 7 (Milieu) passen. | open |
| 40 | Milieu | Rookvrije zone | hiaat | Aangewezen zone waar roken niet is toegestaan. Registreerbare eigenschappen: locatie, type (bushalte/speelplek/sportlocatie), ingangsdatum. Zou onder taakveld 7 (Volksgezondheid/Milieu) passen. | open |
| 41 | Milieu | Walstroompunt | hiaat | Fysiek aansluitpunt voor walstroom aan vaarweg/kade. Registreerbare eigenschappen: locatie, capaciteit, status, eigenaar. Zou onder Mobiliteit (taakveld 2) of Luchtkwaliteit (taakveld 7) passen. | open |
| 42 | Milieu | — | structuur | GGM mist een generiek herbruikbaar "Zone"-concept. Parkeerzone (Parkeren) is de enige zone-entiteit. Milieuzones, rookvrije zones, vuurwerkvrije zones en geluidzones gebruiken hetzelfde patroon (geometrie + regels + handhaving) maar zijn niet gestandaardiseerd. | open |
| 43 | Milieu | — | structuur | GGM mist een generiek "Ontheffing"-concept. Domeinspecifieke varianten bestaan (Ligplaatsontheffing, Ontheffing Inburgering, Ontheffing Werk) zonder gemeenschappelijk supertype. VOMAanvraagOfMelding (VTH) is te breed. | open |

## Typen

| Type | Betekenis |
|---|---|
| **hiaat** | Concept ontbreekt volledig in het GGM |
| **definitie** | Entiteit bestaat maar definitie is onjuist, onvolledig of geen begripsdefinitie |
| **structuur** | Modellering is onhandig (verkeerde overerving, ontbrekende relatie, verkeerde granulariteit) |
| **scope** | Entiteit hoort niet in dit beleidsdomein of ontbreekt in een ander |

## Status

| Status | Betekenis |
|---|---|
| **open** | Bevinding vastgesteld, nog niet teruggekoppeld |
| **gemeld** | Teruggekoppeld aan GGM-beheerteam |
| **opgelost** | Verwerkt in een nieuwe GGM-release |
| **afgewezen** | Teruggekoppeld maar niet overgenomen, met reden |
