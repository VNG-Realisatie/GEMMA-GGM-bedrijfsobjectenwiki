---
type: domein
naam: Belastingen
status: in-behandeling
verwerkingsdatum: 2026-06-19
bronnen_count: 11
begrippen_count: 40
bo_count: 7
---

# Domein: Belastingen

Gemeentelijke belastingen, heffingen en retributies — de fiscale kant van de gemeentelijke huishouding. Het GGM kent geen apart beleidsdomein voor belastingen; relevante entiteiten zitten verspreid over RSGBPlus (WOZ), Financien, Parkeren en VTH.

## Begrippen

### Belastingtypen

| Begrip | Type | Omschrijving | BO? | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|
| gemeentelijke belasting | thema | Overkoepelend begrip voor alle gemeentelijke heffingen | ❌ | Overkoepelend thema, geen object | — | nee |
| algemene belasting | thema | Belasting waarvan opbrengsten naar algemene middelen vloeien | ❌ | Classificatie, geen object | OZB, hondenbelasting | nee |
| bestemmingsbelasting | thema | Belasting waarvan opbrengsten bestemd zijn voor specifieke taken | ❌ | Classificatie, geen object | Afvalstoffenheffing, BIZ | nee |
| retributie | thema | Heffing als vergoeding voor individueel voordeel (dienst of gebruik) | ❌ | Classificatie, geen object | Leges, marktgeld | nee |
| leges | object | Retributie voor gemeentelijke dienstverlening (vergunningen, documenten) | ❌ | Subtype retributie, geen eigen bestaan los van dienst | Bouwvergunning, paspoort | nee |
| onroerendezaakbelasting (OZB) | object | Belasting op eigendom/gebruik onroerende zaken, grootste eigen inkomstenbron | ❌ | Eén OZB per gemeente, geen meervoud; instantie van belastingtype | OZB-eigenaar woning | nee |
| parkeerbelasting | object | Belasting op parkeren (incidenteel + vergunning), regulerend karakter | ❌ | Eén regeling per gemeente; instanties zijn aanslagen/vergunningen | Straatparkeren, vergunning | nee |
| precariobelasting | object | Belasting voor gebruik openbare grond | ❌ | Eén regeling per gemeente | Terras, kabel, luifel | ja: Precario |
| reclamebelasting | object | Belasting op openbare aankondigingen, vaak voor ondernemersfonds | ❌ | Eén regeling per gemeente | Gevelreclame, uithangbord | nee |
| hondenbelasting | object | Belasting voor het houden van een hond | ❌ | Eén regeling per gemeente | Eerste hond, tweede hond | nee |
| BIZ-bijdrage | instrument | Bestemmingsbelasting op verzoek ondernemers voor bedrijveninvesteringszone | ❌ | Governance-instrument, niet het object zelf | BIZ Winkelstraat 2025 | nee |
| afvalstoffenheffing | object | Bestemmingsheffing voor inzameling huishoudelijk afval | ❌ | Eén regeling per gemeente | Vast tarief, diftar | nee |
| reinigingsrecht | object | Retributie voor niet-verplichte afvalinzameling (bedrijven) | ❌ | Subtype retributie | Bedrijfsafval container | nee |
| riool- en waterzorgheffing | object | Heffing voor gemeentelijke watertaken (afvoer, grondwater, droogte) | ❌ | Eén regeling per gemeente | Rioolheffing 2025 | nee |
| toeristenbelasting | object | Heffing op verblijf niet-ingezetenen | ❌ | Eén regeling per gemeente | Hotelnacht, camping | nee |
| forensenbelasting | object | Heffing op langdurig verblijf niet-ingezetenen (>90 dagen) | ❌ | Eén regeling per gemeente | Tweede woning | nee |
| vermakelijkhedenretributie | object | Retributie voor vermakelijkheden die gemeentelijke voorzieningen gebruiken | ❌ | Subtype retributie | Festival, evenement | nee |

### Objecten en processen

| Begrip | Type | Omschrijving | BO? | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|
| belastingaanslag | object | Individuele vaststelling van het belastingbedrag door de heffingsambtenaar | ✅ | 6/6 criteria, GGM-hiaat (procesobject) | OZB-aanslag 2025, naheffing parkeren | nee |
| belastingverordening | instrument | Juridische grondslag voor individuele belastingplicht | ✅ | Eigen levenscyclus, governance-object | OZB-verordening 2025, Legesverordening | nee |
| [[Wiki/Bedrijfsobjecten/99-kern/woz-object]] | object | Onroerende zaak waarvan de WOZ-waarde wordt vastgesteld | ✅ | 6/6 criteria, exact GGM-match | Woning Dorpsstraat 1, kantoor | ja |
| [[Wiki/Bedrijfsobjecten/99-kern/woz-waarde-bo]] | object | Vastgestelde marktwaarde van een WOZ-object per waardepeildatum | ✅ | 6/6 criteria, exact GGM-match | WOZ-waarde 2025: €350.000 | ja |
| belastingplichtige | actor | Persoon die belasting moet betalen | ❌ | Rol van een persoon, geen apart registratie-object | Eigenaar woning, hondenbezitter | nee |
| heffingsmaatstaf | object | Maatstaf waarmee de belastingschuld wordt bepaald | ❌ | Eigenschap van verordening, geen eigen bestaan | WOZ-waarde, oppervlakte, aantal honden | nee |
| tarief | object | Bedrag of percentage per eenheid heffingsmaatstaf | ❌ | Eigenschap van verordening, geen eigen bestaan | 0,1% van WOZ-waarde | nee |
| woz-beschikking | object | Formele bekendmaking WOZ-waarde aan belanghebbende | ❌ | Onderdeel van het WOZ-proces, niet zelfstandig registreerbaar | WOZ-beschikking 2025 | nee |
| onroerende zaak | object | Object van OZB-heffing en WOZ-waardering (BW-begrip) | ❌ | Juridisch begrip, het BO is WOZ-object | Woning, grond, kantoor | ja: via WOZ-object |
| woonlasten | thema | OZB + rioolheffing + afvalstoffenheffing per huishouden | ❌ | Aggregaat, geen object | €900/jaar gemiddeld | nee |

### Juridisch kader en actoren

| Begrip | Type | Omschrijving | BO? | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|
| belastinggebied | thema | Het geheel aan wettelijke heffingsmogelijkheden van gemeenten | ❌ | Beleidsmatig, geen object | Gesloten stelsel Gemeentewet | nee |
| belastingmix | thema | De gekozen combinatie van belastingen en tarieven | ❌ | Beleidskeuze, geen object | — | nee |
| kostendekkend tarief | thema | Principe dat opbrengsten de kosten niet mogen overschrijden | ❌ | Rechtsbeginsel, geen object | Max 100% dekking retributies | nee |
| kostenonderbouwing | thema | Verplichte verantwoording kosten bij lokale heffingen | ❌ | Proces, geen object | BBV-rapportage | nee |
| kruissubsidiering | thema | Overschot ene activiteit dekt tekort andere binnen heffing | ❌ | Beleidsmatig principe | Binnen legesverordening | nee |
| onbenutte belastingcapaciteit | thema | Verschil tussen feitelijke en maximale OZB-opbrengst | ❌ | Kengetal, geen object | — | nee |
| algemene middelen | thema | Niet-gelabelde gemeentelijke opbrengsten | ❌ | Financieel begrip, geen object | — | nee |
| heffingsambtenaar | actor | Legt belastingaanslagen op | ❌ | Rol, geen registratie-object | — | nee |
| invorderingsambtenaar | actor | Int belastingaanslagen | ❌ | Rol, geen registratie-object | — | nee |
| waarderingskamer | actor | Toezichthouder op WOZ-uitvoering | ❌ | Externe organisatie, buiten gemeentelijk perspectief | — | nee |

### GGM Parkeren (gerelateerde BO-kandidaten)

| Begrip | Type | Omschrijving | BO? | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|
| [[naheffingsaanslag]] | object | Aanslag bij niet/te weinig betalen parkeerbelasting | ✅ | 6/6 criteria, exact GGM-match (Naheffing) | Parkeerboete €70 | ja |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeervergunning]] | object | Vergunning om te parkeren in aangewezen gebied | ✅ | 6/6 criteria, exact GGM-match | Bewonersvergunning zone A | ja |
| [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeerrecht]] | object | Recht op parkeren na betaling | ✅ | 6/6 criteria, exact GGM-match | Parkeerticket 2 uur | ja |

## GGM-dekkingsanalyse

Het GGM heeft geen beleidsdomein "Belastingen". Relevante entiteiten per GGM-domein:

| GGM-domein | Relevante entiteiten | Status |
|---|---|---|
| RSGBPlus (99 Kern) | WOZ-object, WOZ-Waarde, WOZ-deelobject, SoortWOZObject | WOZ-object en WOZ-Waarde → BO |
| Vastgoed (9 Int. Org.) | WOZ-Belang, LocatieaanduidingWozObject | Technische tussenentiteiten |
| Financien (9 Int. Org.) | Debiteur, Kostenplaats | Debiteur → BO (in domein Financien) |
| Parkeren (2 V&V) | Naheffing, Parkeerrecht, Parkeervergunning, Parkeerzone, Parkeervlak | 3 → BO |
| VTH (1 Veiligheid) | Heffing, Heffingsverordening, Heffinggrondslag, Precario | Generieke heffing-entiteiten, niet belastingspecifiek |

**Structureel hiaat:** het heffingsproces (verordening → maatstaf → tarief → aanslag → invordering) is niet als samenhangend domein gemodelleerd in het GGM. De BO's Belastingaanslag en Belastingverordening zijn procesobject resp. governance-object zonder GGM-grondslag.

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/Belastingen/belastingtypen|belastingtypen]] — Drie typen gemeentelijke belastingen
- [[Wiki/Bronsamenvattingen/Belastingen/belastinggebied|belastinggebied]] — Reikwijdte belastinggebied, gesloten stelsel
- [[Wiki/Bronsamenvattingen/Belastingen/belastingpolitiek|belastingpolitiek]] — Beleidskeuzes bij de belastingmix
- [[Wiki/Bronsamenvattingen/Belastingen/belastingverordening|belastingverordening]] — De verordening als juridisch instrument
- [[Wiki/Bronsamenvattingen/Belastingen/bevoegdhedenverdeling|bevoegdhedenverdeling]] — Rollen raad, college, ambtenaren
- [[Wiki/Bronsamenvattingen/Belastingen/invordering-en-kwijtschelding|invordering-en-kwijtschelding]] — Invorderingsproces en kwijtscheldingsbeleid
- [[Wiki/Bronsamenvattingen/Belastingen/kostendekkende-tarieven|kostendekkende-tarieven]] — Kostendekkendheidsbeginsel
- [[Wiki/Bronsamenvattingen/Belastingen/wettelijke-grenzen|wettelijke-grenzen]] — Juridische grenzen en rechtsbeginselen
- [[Wiki/Bronsamenvattingen/Belastingen/raadgever-gemeentelijke-belastingen|raadgever-gemeentelijke-belastingen]] — Belastingmix, typen, grenzen
- [[Wiki/Bronsamenvattingen/Belastingen/raadgever-kostenonderbouwing|raadgever-kostenonderbouwing]] — Tariefverschillen en kostenonderbouwingsplicht
- [[Wiki/Bronsamenvattingen/Belastingen/raadgever-woz|raadgever-woz]] — WOZ-waarde, taxatie, Waarderingskamer

## Nog te verwerken bronnen

Specifieke belastingtype-pagina's (inhoud is verwerkt in de begrippentabel hierboven; bronsamenvattingen nog aan te maken):

- Sources/Onderwerpen/Belastingen/Onroerendezaakbelastingen.md
- Sources/Onderwerpen/Belastingen/Parkeerbelastingen.md
- Sources/Onderwerpen/Belastingen/Precariobelasting.md
- Sources/Onderwerpen/Belastingen/Reclamebelasting.md
- Sources/Onderwerpen/Belastingen/Hondenbelasting.md
- Sources/Onderwerpen/Belastingen/BIZ-bijdrage.md
- Sources/Onderwerpen/Belastingen/Retributies.md
- Sources/Onderwerpen/Belastingen/Reinigingsheffingen (afvalstoffenheffing en reinigingsrechten).md
- Sources/Onderwerpen/Belastingen/Riool- en waterzorgheffing.md
- Sources/Onderwerpen/Belastingen/Toeristische heffingen.md

## Openstaande acties

- BO-pagina's aanmaken voor: Belastingaanslag (procesobject), Belastingverordening (governance-object), Naheffingsaanslag, Parkeervergunning, Parkeerrecht
- Bronsamenvattingen aanmaken voor de 10 onverwerkte bronnen
- Terugmelding GGM: ontbreken beleidsdomein Belastingen als samenhangend domein
