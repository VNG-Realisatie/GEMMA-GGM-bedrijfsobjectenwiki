---
type: domein
naam: maatschappelijke ondersteuning
status: afgerond
verwerkingsdatum: 2026-06-22
bronnen_count: 8
begrippen_count: 25
bo_count: 9
---

# Maatschappelijke Ondersteuning

Gemeentelijke uitvoering van de Wmo 2015 en de Jeugdwet: ondersteuning, zorg en hulp aan inwoners met beperkingen, psychische problemen, opgroei- en opvoedproblemen. Het domein omvat de keten van melding/aanvraag via beschikking en toewijzing naar levering, zowel voor volwassenen (Wmo) als jeugdigen (Jeugdwet).

## Begrippentabel

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | object | Formeel besluit gemeente op aanvraag/melding Wmo/Jeugdwet | ✅ | ja | 6/6 criteria, exact match | Wmo-beschikking huishoudelijke hulp | ja |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/voorziening\|Voorziening]] | object | Middel voor ondersteuning/hulp; subtypes: maatwerkvoorziening, jeugdhulp, algemeen | ✅ | ja | 6/6 criteria, exact match | Rolstoel, huishoudelijke hulp, ambulante jeugdhulp | ja |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/toewijzing\|Toewijzing]] | object | Opdracht gemeente aan zorgaanbieder voor levering voorziening | ✅ | ja | 6/6 criteria, exact match | Toewijzing ambulante behandeling | ja |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/levering\|Levering]] | object | Daadwerkelijk geleverde zorg/ondersteuning | ✅ | ja | 6/6 criteria, exact match | 10 uur begeleiding per maand | ja |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/pgb-toekenning\|PGB-Toekenning]] | object | Toekenning persoonsgebonden budget | ✅ | ja | 6/6 criteria, exact match | PGB-budget €15.000 | ja |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | object | Inwoner die gebruik maakt van gemeentelijke ondersteuning | ✅ | ja | 6/6 criteria, cross-cutting sociaal domein | Wmo-cliënt, jeugdhulp-cliënt | ja |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/jeugdbescherming-en-reclassering/zorgmelding\|Zorgmelding]] | object | Melding over veiligheid/ontwikkeling kind bij gemeente of Veilig Thuis | ✅ | ja | 6/6 criteria, exact match | Melding vermoedens kindermishandeling | ja |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociale-teams/sociaalteamdossier\|SociaalTeamDossier]] | object | Geïntegreerd dossier van buurtteam per cliënt/gezin | ✅ | ja | 6/6 criteria, exact match | Buurtteamdossier gezin Jansen | ja |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/dak-en-thuislozen/dakloosheid\|Dakloosheid]] | object | Registratie dakloosheidsstatus van een cliënt | ✅ | ja | 6/6 criteria, exact match | Dakloosheidsregistratie met briefadres | ja |
| melding/aanvraag Wmo-Jeugd | object | Intake bij sociaal team; twee GGM-entiteiten | ❌ | ja | Gedekt door generiek [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of Melding]] | Wmo-melding, jeugdhulpaanvraag | ja |
| beschikte voorziening | object | Voorziening waarover een beschikking is gedaan | ❌ | ja | Koppeltabel tussen Beschikking en Voorziening, geen zelfstandig BO | — | ja |
| declaratie | object | Opgave van te vergoeden kosten door leverancier | ❌ | ja | Financieel-administratief, niet op bestuurlijk niveau | Declaratie zorgaanbieder | ja |
| beperking | object | Stoornis/conditie die functioneren belemmert | ❌ | ja | Eigenschap van beoordeling, niet zelfstandig BO | ICF-beperking mobiliteit | ja |
| leverancier (zorgaanbieder) | actor | Organisatie die zorg/ondersteuning levert | ❌ | ja | Actor, geen object; cross-cutting | Zorginstelling, thuiszorgorganisatie | ja |
| huishouden | object | Persoon of groep die een huishouden voert | ❌ | ja | Cross-cutting sociaal domein, eenheid voor beoordeling | Eenoudergezin | ja |
| buurtteam | actor | Lokaal team voor generalistische basishulp | ❌ | nee | Organisatievorm (actor), geen data-object | Buurtteam Jeugd en Gezin Overvecht | ja (Team) |
| mantelzorger | actor | Persoon die zorgt voor naaste met ziekte/beperking | ❌ | nee | Rol, geen data-object | — | nee |
| beschermd wonen | thema | Woonvorm met intensieve begeleiding | ❌ | nee | Type voorziening (Voorzieningsoort), geen apart BO | — | nee |
| pleegzorg | thema | Opvang in pleeggezin als jeugdhulpvorm | ❌ | nee | Type voorziening (Voorzieningsoort), geen apart BO | Netwerkpleegzorg, bestandspleegzorg | nee |
| collectief werken | thema | Groepsgerichte hulp als norm | ❌ | nee | Werkwijze/methodiek, geen object | BuKoJou jongerengroep | nee |
| pedagogische basis | thema | Netwerk van voorzieningen en relaties rond kinderen | ❌ | nee | Beleidsconcept, geen object | School, sport, welzijn, buurt | nee |
| Veilig Thuis | actor | Regionaal advies/meldpunt huiselijk geweld | ❌ | nee | Externe organisatie, niet gemeentelijk geregistreerd | — | nee |
| woonzorgvisie | instrument | Gemeentelijk beleidsplan wonen+zorg | ❌ | nee | Governance-instrument, geen data-object | — | nee |
| aandachtsgroep | doelgroep | Groep met specifieke woonbehoeften | ❌ | nee | Doelgroep, geen object | Ouderen, GGZ-cliënten | nee |
| respijtzorg | object | Tijdelijke overname mantelzorg | ❌ | nee | Type voorziening, geen apart BO | Logeeropvang | nee |

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/beleidsnota-jeugd-utrecht|Beleidsnota Jeugd — Samen opgroeien, samen opvoeden 2025-2034]] — Gemeente Utrecht: jeugdbeleid, acht opgaven, buurtteams, collectief werken
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/beleidsregels-jeugdhulp-oost-gelre|Beleidsregels Jeugdhulp 2025 — gemeente Oost Gelre]] — Verordening: procedure, vormen jeugdhulp, PGB
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/aanpak-dakloosheid|Aanpak Dakloosheid]] — VNG: landelijke aanpak, Eerst een Thuis
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/beschermd-thuis|Beschermd Thuis]] — VNG: transitie beschermd wonen → ambulant
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/kindermishandeling-en-huiselijk-geweld|Kindermishandeling en huiselijk geweld]] — VNG: Veilig Thuis, jeugdbescherming
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/maatwerkvoorzieningen-wmo|Maatwerkvoorzieningen Wmo]] — VNG: hulpmiddelen, woningaanpassingen, vervoer
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/vrijwilligerswerk-en-mantelzorgondersteuning|Vrijwilligerswerk en mantelzorgondersteuning]] — VNG: mantelzorg, informele zorg
- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/wonen-voor-aandachtsgroepen|Wonen voor aandachtsgroepen]] — VNG: woonzorgvisie, aandachtsgroepen

## Niet-relevante bronnen

8 bronnen verplaatst naar `Sources/Onderwerpen/Maatschappelijke Ondersteuning/Niet-relevant/`: rubriekpagina, abonnementstarief-wmo, financien-wmo, inkoop-wmo-en-jeugdwet, regionale-samenwerking, re-integratie-ex-gedetineerden, verward-onbegrepen-gedrag, mensenhandel.

## Openstaande vragen

- Kinderbeschermingsmaatregelen (OTS, gezagsbeëindiging) zijn juridische instrumenten die de gemeente registreert maar niet zelf oplegt — is dit een BO of alleen een processtap?
- Het GGM modelleert Beschikking twee keer (Generiek Jeugd en Wmo én Diensten) met iets andere attributen — consolidatie nodig?
- Collectief werken als nieuwe leveringsvorm past niet in het huidige Voorzieningsoort-model; signaleren als potentieel GGM-hiaat?

## Terugmeldingen richting GGM

Zie [[Wiki/Analyses/ggm-terugmeldingen]]:
- **Jeugdhulpvormen als entiteiten:** Het GGM modelleert jeugdhulpvormen (pleegzorg, gezinshuiszorg, residentieel verblijf) alleen via productcodes in Voorzieningsoort. Overweeg expliciete entiteiten of een enumeratie.
- **Kinderbeschermingsmaatregel:** OTS en gezagsbeëindiging ontbreken als entiteiten; alleen Zorgmelding en Zorgelijke Situatie zijn gemodelleerd.
