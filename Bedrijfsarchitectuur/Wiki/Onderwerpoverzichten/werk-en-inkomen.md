---
type: onderwerp
naam: werk en inkomen
status: in-behandeling
verwerkingsdatum: 2026-06-27
bronnen_count: 3
begrippen_count: 25
bo_count: 8
---

# Werk en Inkomen

Gemeentelijke uitvoering van de Participatiewet: het bevorderen van arbeidsdeelname voor mensen met arbeidsvermogen, het verstrekken van bijstandsuitkeringen, loonkostensubsidies en re-integratievoorzieningen, en het bieden van beschut werk. Wettelijke grondslag: Participatiewet (2015), Wet SUWI (2001, samenwerking UWV-SVB-gemeenten), Wet sociale werkvoorziening (aflopend, richting nul rond 2048). GGM-beleidsdomein Werk (taakveld 6 Sociaal Domein) bevat 33 Objecttype-entiteiten; beleidsdomein Inkomen (overkoepelend, 89 entiteiten) dekt de inkomensvoorzieningen. Het SGR 19.0 (BKWI) definieert het gegevensmodel voor de SUWI-keten (~260 klassen, ~930 attributen).

## Begrippen

| Begrip                                                                                             | Type           | Omschrijving                                                                      | BO? | Data-object | Reden                                                               | Voorbeelden                                        | GGM |
| -------------------------------------------------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------- | --- | ----------- | ------------------------------------------------------------------- | -------------------------------------------------- | --- |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/loonkostensubsidie\|Loonkostensubsidie]]             | object         | Tegemoetkoming aan werkgever voor verschil loonwaarde en WML                      | ✅   | ja          | 6/6 criteria, exact match                                           | LKS €10.000/jr bij 50% loonwaarde                  | ja  |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/re-integratievoorziening\|Re-integratievoorziening]] | object         | Voorziening gericht op vergroten arbeidskansen werkzoekende                       | ✅   | ja          | 6/6 criteria, exact match, 12 attributen                            | Scholingstraject, werkstage, bemiddeling           | ja  |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]]  | object         | Regeling die voorziet in inkomen conform landelijke wetgeving                     | ✅   | ja          | 6/6 criteria, exact match                                           | Bijstandsuitkering, bijzondere bijstand            | ja  |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/draagkracht\|Draagkracht]]        | object         | Berekend deel inkomen/vermogen beschikbaar voor eigen kosten                      | ✅   | ja          | 6/6 criteria, exact match                                           | Draagkrachtbeoordeling 2025                        | ja  |
| beschutte werkplek                                                                                 | object         | Werkplek in aangepaste omstandigheden met indicatie UWV                           | ❌   | ja          | Arrangement van LKS + begeleiding + werkplek; geen apart GGM-object | Beschut werkplek sociaal ontwikkelbedrijf          | nee |
| loonwaarde                                                                                         | object         | Vastgestelde productieve waarde werknemer als % van WML                           | ❌   | ja          | Attribuut van Loonkostensubsidie, geen eigen levenscyclus           | 50% WML, 70% WML                                   | ja  |
| doelgroepenregister                                                                                | object         | Landelijk register personen met arbeidsbeperking (banenafspraak)                  | ❌   | ja          | UWV beheert; gemeente gebruikt als verdeelmaatstaf                  | Inschrijving doelgroep Participatiewet             | ja  |
| bijstandsbudget                                                                                    | instrument     | Gebudgetteerd budget (BUIG) voor bijstandsuitkeringen en LKS                      | ❌   | nee         | Financieringsstroom Rijk→gemeente, geen data-object                 | BUIG 2025, €7,3 mld landelijk                      | nee |
| cluster participatie                                                                               | instrument     | Fictief budget in AU gemeentefonds voor uitvoering/re-integratie                  | ❌   | nee         | Verdeelsystematiek, geen data-object                                | €4,0 mld landelijk (2024)                          | nee |
| integratie-uitkering participatie                                                                  | instrument     | Tijdelijke uitkering in gemeentefonds voor Wsw en beschut werk                    | ❌   | nee         | Financieringsstroom, geen data-object                               | €2,1 mld landelijk (2024)                          | nee |
| vangnetuitkering                                                                                   | instrument     | Financiële regeling bij >7,5% tekort op bijstandsbudget                           | ❌   | nee         | Rijksregeling, niet gemeentelijk geregistreerd                      | Vangnet 2024, toetsingscommissie                   | nee |
| macrobudget                                                                                        | instrument     | Landelijk totaalbudget berekend als volume × prijs                                | ❌   | nee         | Berekeningsconcept, geen data-object                                | Macrobudget bijstand 2025                          | nee |
| impulsbudget                                                                                       | instrument     | 10-jarig budget transitie sociaal ontwikkelbedrijven (2025-2034)                  | ❌   | nee         | Tijdelijke DU, geen data-object                                     | €35 mln in 2025, via DU                            | nee |
| infrastructurele opslag                                                                            | instrument     | Rijksbijdrage voor niet-beschut-werk banen bij SOB's                              | ❌   | nee         | Financieringsstroom, geen data-object                               | Oplopend tot €35,9 mln structureel                 | nee |
| [[Wiki/Actoren/sociaal-ontwikkelbedrijf|Sociaal ontwikkelbedrijf]] | actor | Organisatie voor werkplekken/begeleiding arbeidsbeperking | ❌ | nee | Actor — structurele opdrachtrelatie met de gemeente; vastgelegd als actor-pagina | Senzer, WSD, Empatec | nee |
| banenafspraak                                                                                      | instrument     | Afspraak kabinet en sociale partners voor banen arbeidsbeperking                  | ❌   | nee         | Beleidskader, geen data-object                                      | —                                                  | nee |
| nieuwe doelgroep                                                                                   | doelgroep      | Ex-Wsw/Wajong personen nu in Participatiewet                                      | ❌   | nee         | Classificatie, geen data-object                                     | Groeit tot stabilisatie ~2048                      | nee |
| wsw-dienstbetrekking                                                                               | object         | Dienstbetrekking onder aangepaste omstandigheden (Wsw)                            | ❌   | ja          | Aflopende regeling (→nul 2048), geen actieve BO-status              | Wsw-medewerker SE 0,8                              | ja  |
| bijzondere bijstand                                                                                | object         | Verstrekking voor kosten uit bijzondere omstandigheden                            | ❌   | ja          | Subtype van Inkomensvoorziening                                     | Bijzondere bijstand medische kosten                | ja  |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]]                         | object         | Generiek werkprofiel met arbeidspositie, bemiddelbaarheid en begeleidingsbehoefte | ✅   | ja          | 6/6 criteria, exact match (abstract), 25+ componenten               | Werkzoekende met trajectplan en 3 voorzieningen    | ja  |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/trajectplan\|Trajectplan]]                           | object         | Overkoepelend plan dat re-integratieactiviteiten per werkzoekende organiseert     | ✅   | ja          | 6/6 criteria, GGM-hiaat, SGR-klasse                                 | Trajectplan met scholing + werkstage + bemiddeling | nee |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/instrument\|Instrument]]                             | object         | Beschikbare dienst/tool voor toeleiding naar werk of participatie                 | ✅   | ja          | 6/6 criteria, GGM-hiaat, Dennis & Eva catalogus-item                | Loonkostenvoordeel, jobcoaching, proefplaatsing    | nee |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/vacature-arbeidsmarkt\|Vacature (arbeidsmarkt)]]      | object         | Openstaande arbeidsplaats bij werkgever voor matching met werkzoekenden via VUM   | ✅   | ja          | 6/6 criteria, GGM-hiaat, homoniem Vacature (HR) #87                 | Vacature magazijnmedewerker via VUM                | nee |
| suwinet/GeVS                                                                                       | infrastructuur | Gezamenlijke elektronische voorzieningen voor SUWI-gegevensuitwisseling           | ❌   | nee         | Infrastructuur, geen data-object                                    | Suwinet-Inkijk, Suwinet-Inlezen                    | nee |
| VUM                                                                                                | programma      | Verbeteren Uitwisseling Matchingsgegevens over regiogrenzen                       | ❌   | nee         | Procesverbetering, geen data-object                                 | VUM werkzoekendeprofiel, VUM vacatureprofiel       | nee |

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/Werk en Inkomen/factsheet-bijzondere-bijstand|Factsheet Bijzondere Bijstand (Divosa, 2024)]]
- [[Wiki/Bronsamenvattingen/Werk en Inkomen/handreiking-explicitering-budgetten-participatiewet-wsw|Handreiking Explicitering budgetten Participatiewet en Wsw (Berenschot, 2025)]]
- [[Wiki/Bronsamenvattingen/Werk en Inkomen/wet-suwi-en-sgr|Wet SUWI en Gegevensregister SUWI 19.0 (BKWI)]]

## Nog te verwerken bronnen

Geen openstaande bronnen.

## Cross-domein

- [[Wiki/Onderwerpoverzichten/schulden-en-armoede|Schulden en armoede]] — bijstandsgerechtigden hebben vaak ook schuldenproblematiek; bijzondere bijstand en schuldhulpverlening raken elkaar
- [[Wiki/Onderwerpoverzichten/arbeidszaken|Arbeidszaken]] — homoniem [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/vacature|Vacature]] (HR) vs. [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/vacature-arbeidsmarkt|Vacature (arbeidsmarkt)]] (Werk): gemeente als werkgever vs. gemeente als arbeidsmarktbemiddelaar
- GGM-beleidsdomein Inkomen (89 entiteiten) — overkoepelend domein met sub-domeinen Diensten, Model Inkomen, Normafwijking, Reden aanvraag, Terug- en invordering
- GGM-beleidsdomein Werk (33 entiteiten) — [[Werkzoekende]] als centraal object met uitgebreid profiel (arbeidsmarktkwalificaties, bemiddeling, opleiding, etc.)

## Openstaande vragen

- Beschutte werkplek: mogelijk apart BO als er rijkere bronnen beschikbaar komen over de gemeentelijke registratie van indicaties en taakstelling
- GGM Werk-domein bevat 33 entiteiten waarvan nu 5 als BO vastgesteld (Werkzoekende, Re-integratievoorziening, Loonkostensubsidie + 2 uit Inkomen); bij nadere bronnen kunnen meer entiteiten BO-kandidaat worden
- GGM-hiaten Trajectplan (#85) en Instrument (#86) teruggemeld
