---
type: analyse
titel: "Entiteitendekking — totaaloverzicht"
datum: 2026-07-07
---

# Entiteitendekking — totaaloverzicht

916 GGM-entiteiten. Dekking: 827 gedekt (90%), 89 niet gedekt. 104 BO's zonder GGM-entiteit. 310 BO's totaal.

*Bijgewerkt 2026-07-07 (ronde 1): herbeoordeling Sociaal Domein Generiek — Bankrekening/Hypotheek/Motorvoertuig/Onroerend goed consistent gerouteerd via Vermogenscomponent → Profiel → Client, waarmee 2 hiaten zijn opgeheven.*

*Bijgewerkt 2026-07-07 (ronde 2): ingest van Boek 1 BW Titel 17 en Wet studiefinanciering 2000 legde een bredere routeringsinconsistentie in de hele Inkomstencomponent-tak bloot (Primair + Secundair inkomstencomponent en subtypen, plus Onderhoudsplicht/-verhouding) — 17 hiaten opgeheven. Zie [[Wiki/Analyses/entiteitendekking/6-sociaal-domein]] voor details.*

*Bijgewerkt 2026-07-07 (ronde 3): herbeoordeling Beheer Openbare Ruimte — 8 kunstwerk-achtige subtypen (Brug, Flyover, Kademuur, Keermuur, Tunnelobject, Viaduct, Overbruggingsobject, Scheiding) alsnog gekoppeld aan de bestaande BO Kunstwerk via de GGM-hiërarchie, 3 verkeerd gekoppelde entiteiten (Klimplant, SolitairePlant, Omgevingsvergunning) gecorrigeerd, en Sportterrein herkend als vermoedelijke tweede GGM-representatie van de bestaande BO Sportpark (taakveld 5) in plaats van een echt hiaat — 7 hiaten opgeheven. Zie [[Wiki/Analyses/entiteitendekking/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing]] voor details.*

*Bijgewerkt 2026-07-07 (ronde 4): herbeoordeling 99 Kern (BAG/RGBZPlus/RSGBPlus) — 8 route-fouten via abstracte tussenstations gecorrigeerd (Huishouden, Rechtspersoon, AdresBuitenland, Nationaliteit, plus 3 RGBZ rol-attributen die ten onrechte aan Wijk hingen), 8 RSGB/BAG-naamduplicaten direct aan hun eigen BAG-BO gekoppeld in plaats van een willekeurig ander BO, 8 BRP-persoonsdetails gekoppeld aan Ingeschreven Persoon op basis van het Logisch Ontwerp BRP 2025.Q1 (GGM zelf mist de relatie, teruggemeld als #93), en 13 generieke bouwstenen (99-Kern geo/media-typen, RGBZ historie-/kwaliteitsindicatoren) van een misleidend specifiek naar een neutraal "generieke bouwsteen"-label gezet — 12 hiaten opgeheven. Zie [[Wiki/Analyses/entiteitendekking/99-kern]] voor details.*

| Taakveld | Beleidsdomein | GGM-entiteiten | Entiteiten met BO | Entiteiten ondersteunend aan BO | Niet gedekt | Dekking | BO zonder GGM-entiteit |
|---|---|---|---|---|---|---|---|
| **Totaal** | | 916 | 206 | 621 | 89 (10%) | 90% | 104 (BO's totaal: 310) |
| **[[Wiki/Analyses/entiteitendekking/0-bestuur-politiek-en-ondersteuning\|0 Bestuur, Politiek en Ondersteuning]]** | Griffie | 13 | 3 | 10 | 0 | 100% | |
|  | | | | | | | 5 |
| **[[Wiki/Analyses/entiteitendekking/1-veiligheid-en-vergunningen\|1 Veiligheid en Vergunningen]]** | 1 Veiligheid en Vergunningen | 30 | 7 | 22 | 1 | 97% | |
|  | | | | | | | 5 |
| **[[Wiki/Analyses/entiteitendekking/2-verkeer-vervoer-en-waterstaat\|2 Verkeer, Vervoer en Waterstaat]]** | Mobiliteit | 7 | 4 | 3 | 0 | 100% | |
|  | Parkeren | 13 | 9 | 4 | 0 | 100% | |
|  | | | | | | | 16 |
| **[[Wiki/Analyses/entiteitendekking/3-economie\|3 Economie]]** | 3 Economie | 6 | 1 | 5 | 0 | 100% | |
|  | | | | | | | 6 |
| **[[Wiki/Analyses/entiteitendekking/4-onderwijs\|4 Onderwijs]]** | Leerplicht en Leerlingenvervoer | 15 | 5 | 10 | 0 | 100% | |
|  | Onderwijs | 12 | 5 | 5 | 2 | 83% | |
|  | | | | | | | 1 |
| **[[Wiki/Analyses/entiteitendekking/5-sport-cultuur-en-recreatie\|5 Sport, Cultuur en Recreatie]]** | Erfgoed | 42 | 4 | 35 | 3 | 93% | |
|  | Musea | 30 | 2 | 26 | 2 | 93% | |
|  | Sport | 9 | 6 | 1 | 2 | 78% | |
|  | | | | | | | 2 |
| **[[Wiki/Analyses/entiteitendekking/6-sociaal-domein\|6 Sociaal Domein]]** | Dak- en thuislozen | 1 | 1 | 0 | 0 | 100% | |
|  | Gemeentebegrafenissen | 1 | 1 | 0 | 0 | 100% | |
|  | Generiek Jeugd en Wmo | 27 | 6 | 21 | 0 | 100% | |
|  | Inburgering | 35 | 15 | 20 | 0 | 100% | |
|  | Inkomen | 88 | 8 | 59 | 21 | 76% | |
|  | Jeugdbescherming en reclassering | 4 | 1 | 3 | 0 | 100% | |
|  | Schulden | 32 | 10 | 19 | 3 | 91% | |
|  | Sociaal Domein Generiek | 55 | 3 | 38 | 14 | 75% | |
|  | Sociale Teams | 9 | 1 | 8 | 0 | 100% | |
|  | Werk | 33 | 3 | 29 | 1 | 97% | |
|  | | | | | | | 10 |
| **[[Wiki/Analyses/entiteitendekking/7-volksgezondheid-en-milieu\|7 Volksgezondheid en Milieu]]** | Afval | 16 | 4 | 12 | 0 | 100% | |
|  | | | | | | | 31 |
| **[[Wiki/Analyses/entiteitendekking/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing\|8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing]]** | Beheer Openbare Ruimte | 81 | 18 | 41 | 22 | 73% | |
|  | Bouwen en Wonen | 7 | 2 | 5 | 0 | 100% | |
|  | Omgevingswet | 31 | 6 | 25 | 0 | 100% | |
|  | | | | | | | 3 |
| **[[Wiki/Analyses/entiteitendekking/9-interne-organisatie\|9 Interne Organisatie]]** | Financien | 24 | 10 | 14 | 0 | 100% | |
|  | HR | 31 | 11 | 20 | 0 | 100% | |
|  | ICT | 35 | 10 | 16 | 9 | 74% | |
|  | Inkoop | 20 | 7 | 13 | 0 | 100% | |
|  | Organisatie-indeling | 2 | 1 | 1 | 0 | 100% | |
|  | Subsidies | 9 | 0 | 9 | 0 | 100% | |
|  | Vastgoed | 27 | 5 | 21 | 1 | 96% | |
|  | | | | | | | 9 |
| **[[Wiki/Analyses/entiteitendekking/10-dienstverlening\|10 Dienstverlening]]** | 10 Dienstverlening | 16 | 3 | 12 | 1 | 94% | |
|  | | | | | | | 10 |
| **[[Wiki/Analyses/entiteitendekking/99-kern\|99 Kern]]** | 99 Kern | 10 | 0 | 10 | 0 | 100% | |
|  | BAG | 13 | 10 | 2 | 1 | 92% | |
|  | RGBZPlus | 37 | 10 | 27 | 0 | 100% | |
|  | RSGBPlus | 95 | 14 | 75 | 6 | 94% | |
|  | | | | | | | 6 |
