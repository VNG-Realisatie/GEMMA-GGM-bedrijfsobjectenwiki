---
type: onderwerp
naam: informatiesystemen
status: afgerond
verwerkingsdatum: 2026-06-29
bronnen_count: 3
begrippen_count: 21
bo_count: 12
---

IT-infrastructuur, applicatiebeheer en IT-dienstverlening vanuit gemeentelijk perspectief. Het onderwerp omvat het beheer van het applicatielandschap, de CMDB-structuur (configuration items), IT-inkoopvoorwaarden (GIBIT) en IT-servicemanagement.

| Begrip | Begripstype | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/applicatie\|Applicatie]] | object | Softwaretoepassing gericht op ondersteuning van eindgebruikers | ✅ | ja | 6/6 criteria, GGM exact | Zaaksysteem, BAG-applicatie | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/dataproduct\|Dataproduct]] | object | Concreet resultaat van datagedreven werken | ✅ | ja | 6/6 criteria, GGM-hiaat | Armoede-dashboard, wijkmonitor | nee |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/koppeling\|Koppeling]] | object | Systematiek voor uitwisseling van data tussen systemen | ✅ | ja | 6/6 criteria, GGM exact | StUF-koppeling, API-koppeling | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/licentie\|Licentie]] | object | Gebruiksrecht op ICT-product of -dienst | ✅ | ja | 6/6 criteria, GGM exact | Office-licentie, Oracle-licentie | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/server\|Server]] | object | Computer die in een netwerk een ondersteunende taak vervult | ✅ | ja | 6/6 criteria, GGM exact, 8 attributen | Mailserver, databaseserver | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/database\|Database]] | object | Applicatiecomponent die een gestructureerde dataset bevat | ✅ | ja | 6/6 criteria, GGM exact, 7 attributen | Oracle-database, SQL-database | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/software\|Software]] | object | Computerprogrammatuur met bijbehorende data | ✅ | ja | 5/6 criteria, GGM exact, specialisaties Standaard/Maatwerk/Derden | Besturingssysteem, middleware | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/hardware\|Hardware]] | object | Fysieke IT-componenten of onderdelen | ✅ | ja | 5/6 criteria, GGM exact | Werkstations, printers, thin clients | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/netwerkcomponent\|Netwerkcomponent]] | object | Hardware- of softwareonderdeel voor netwerkcommunicatie | ✅ | ja | 5/6 criteria, GGM exact (typo: Nertwerkcomponent) | Firewall, switch, router | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/storing-ict\|Storing (ICT)]] | object | Verlies van de mogelijkheid van een ICT-component om volgens specificatie te werken | ✅ | ja | 5/6 criteria, GGM exact, homoniem met BOR | E-mailstoring, netwerkstoring | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/wijzigingsverzoek\|Wijzigingsverzoek]] | object | Aanvraag voor wijziging aan het applicatielandschap | ✅ | ja | 5/6 criteria, GGM exact | Change request, RFC | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/sla\|Service Level Agreement]] | governance-instrument | Nadere overeenkomst met onderhoudsnormen voor ICT-prestatie | ✅ | nee | 6/6 criteria, GGM-hiaat (governance) | SLA met TOPdesk-leverancier | nee |
| CMDB-item | object | Generiek configuratie-item in de CMDB | ❌ | ja | Abstract GGM-construct; concrete specialisaties zijn BO's | — | ja |
| Linkbaar CMDB-item | object | Abstract CMDB-item dat kan worden gekoppeld | ❌ | ja | Abstract GGM-construct; specialisaties Applicatie, Database, Server zijn BO's | — | ja |
| applicatielandschap | thema | Geheel van systemen, software, koppelingen en infrastructuur | ❌ | nee | Thema, geen object | — | nee |
| informatiebeheerplan | governance-instrument | Overzichtsinstrument voor de informatiehuishouding | ❌ | nee | Governance-proces, geen concreet IT-object | — | nee |
| acceptatieprocedure | thema | Procedure voor formele goedkeuring van ICT-prestatie | ❌ | nee | Proces, geen object | — | nee |
| exit-plan | governance-instrument | Plan van aanpak voor migratie bij beëindiging | ❌ | nee | Procesinstrument, geen object | — | nee |
| update | object | Opvolgende versie met herstelde gebreken | ❌ | ja | Eigenschap van Versie (GGM-component bij Applicatie) | Patch, bugfix | ja |
| upgrade | object | Opvolgende versie met nieuwe functionaliteiten | ❌ | ja | Eigenschap van Versie (GGM-component bij Applicatie) | Major release | ja |
| beschikbaarheid | waarde | Mate waarin ICT-prestatie daadwerkelijk beschikbaar is | ❌ | nee | Meetwaarde, geen object | Uptime 99,5% | nee |

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/informatiesystemen/gibit-2025|GIBIT 2025 — Gemeentelijke Inkoop bij IT Toolbox]]
- [[Wiki/Bronsamenvattingen/informatiesystemen/cmdb-en-informatiebeheer|CMDB & Informatiebeheerplan]]

## Terugmeldingen richting GGM

- Typefout "Nertwerkcomponent" → moet zijn "Netwerkcomponent" — zie [[Wiki/Analyses/ggm-terugmeldingen]]
