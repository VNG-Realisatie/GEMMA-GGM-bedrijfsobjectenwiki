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
