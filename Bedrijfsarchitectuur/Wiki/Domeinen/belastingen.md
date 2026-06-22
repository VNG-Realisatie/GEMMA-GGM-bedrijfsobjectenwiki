---
type: domein
naam: Belastingen
status: afgerond
verwerkingsdatum: 2026-06-22
bronnen_count: 22
begrippen_count: 45
bo_count: 9
---

# Domein: Belastingen

Gemeentelijke belastingen, heffingen en retributies — de fiscale kant van de gemeentelijke huishouding. Het GGM kent geen apart beleidsdomein voor belastingen; relevante entiteiten zitten verspreid over RSGBPlus (WOZ), Financien, Parkeren en VTH.

## Begrippen

### Belastingtypen

|Begrip|Type|Omschrijving|BO?| Data-object |Reden|Voorbeelden|GGM|
|---|---|---|---|---|---|---|---|
|gemeentelijke belasting|thema|Overkoepelend begrip voor alle gemeentelijke heffingen| ❌ | nee |Overkoepelend thema, geen object|—|nee|
|algemene belasting|thema|Belasting waarvan opbrengsten naar algemene middelen vloeien| ❌ | nee |Classificatie, geen object|OZB, hondenbelasting|nee|
|bestemmingsbelasting|thema|Belasting waarvan opbrengsten bestemd zijn voor specifieke taken| ❌ | nee |Classificatie, geen object|Afvalstoffenheffing, BIZ|nee|
|retributie|thema|Heffing als vergoeding voor individueel voordeel (dienst of gebruik)| ❌ | nee |Classificatie, geen object|Leges, marktgeld|nee|
|leges|object|Retributie voor gemeentelijke dienstverlening (vergunningen, documenten)| ❌ | ja |Subtype retributie, geen eigen bestaan los van dienst|Bouwvergunning, paspoort|nee|
|onroerendezaakbelasting (OZB)|object|Belasting op eigendom/gebruik onroerende zaken, grootste eigen inkomstenbron| ❌ | ja |Eén OZB per gemeente, geen meervoud; instantie van belastingtype|OZB-eigenaar woning|nee|
|parkeerbelasting|object|Belasting op parkeren (incidenteel + vergunning), regulerend karakter| ❌ | ja |Eén regeling per gemeente; instanties zijn aanslagen/vergunningen|Straatparkeren, vergunning|nee|
|precariobelasting|object|Belasting voor gebruik openbare grond| ❌ | ja |Eén regeling per gemeente|Terras, kabel, luifel|ja: Precario|
|reclamebelasting|object|Belasting op openbare aankondigingen, vaak voor ondernemersfonds| ❌ | ja |Eén regeling per gemeente|Gevelreclame, uithangbord|nee|
|hondenbelasting|object|Belasting voor het houden van een hond| ❌ | ja |Eén regeling per gemeente|Eerste hond, tweede hond|nee|
|BIZ-bijdrage|instrument|Bestemmingsbelasting op verzoek ondernemers voor bedrijveninvesteringszone| ❌ | nee |Governance-instrument, niet het object zelf|BIZ Winkelstraat 2025|nee|
|afvalstoffenheffing|object|Bestemmingsheffing voor inzameling huishoudelijk afval| ❌ | ja |Eén regeling per gemeente|Vast tarief, diftar|nee|
|reinigingsrecht|object|Retributie voor niet-verplichte afvalinzameling (bedrijven)| ❌ | ja |Subtype retributie|Bedrijfsafval container|nee|
|riool- en waterzorgheffing|object|Heffing voor gemeentelijke watertaken (afvoer, grondwater, droogte)| ❌ | ja |Eén regeling per gemeente|Rioolheffing 2025|nee|
|toeristenbelasting|object|Heffing op verblijf niet-ingezetenen| ❌ | ja |Eén regeling per gemeente|Hotelnacht, camping|nee|
|forensenbelasting|object|Heffing op langdurig verblijf niet-ingezetenen (>90 dagen)| ❌ | ja |Eén regeling per gemeente|Tweede woning|nee|
|vermakelijkhedenretributie|object|Retributie voor vermakelijkheden die gemeentelijke voorzieningen gebruiken| ❌ | ja |Subtype retributie|Festival, evenement|nee|
|roerende-zaakbelasting|object|OZB-variant voor woonboten en drijvende bedrijfsruimten| ❌ | ja |Variant van OZB, eén regeling per gemeente|Woonboot, drijvend kantoor|nee|
|watertoeristenbelasting|object|Variant toeristenbelasting gekoppeld aan ligplaatsen| ❌ | ja |Variant van toeristenbelasting|Ligplaats jachthaven|nee|
|marktgeld|object|Retributie voor innemen standplaats op dag-/weekmarkten| ❌ | ja |Subtype retributie|Standplaats weekmarkt|nee|
|havengeld|object|Retributie voor gebruik waterwegen, havens, bruggen, sluizen| ❌ | ja |Subtype retributie|Liggeld, sluis schutten|nee|
|lijkbezorgingsrechten|object|Retributie voor gebruik gemeentelijke begraafplaats of crematorium| ❌ | ja |Subtype retributie|Grafrecht, crematie|nee|

### Objecten en processen

|Begrip|Type|Omschrijving|BO?| Data-object |Reden|Voorbeelden|GGM|
|---------------------------------------------------------------|---|----------|--------------------------------------------------------------------------|---|-----------------------------------------------------------------|--------------------------------------|------------------|
|[[Wiki/Bedrijfsobjecten/99-kern/heffing\|Heffing (belastingaanslag)]]|object|Individuele vaststelling van het belastingbedrag door de heffingsambtenaar| ✅ | ja |6/6 criteria, exact GGM-match|OZB-aanslag 2025, naheffing parkeren|ja: Heffing|
|[[Wiki/Bedrijfsobjecten/99-kern/heffingsverordening\|Heffingsverordening]]|instrument|Juridische grondslag voor individuele belastingplicht| ✅ | ja |Eigen levenscyclus, exact GGM-match|OZB-verordening 2025, Legesverordening|ja: Heffingsverordening|
|[[Wiki/Bedrijfsobjecten/99-kern/woz-object\|WOZ-object]]|object|Onroerende zaak waarvan de WOZ-waarde wordt vastgesteld| ✅ | ja |6/6 criteria, exact GGM-match|Woning Dorpsstraat 1, kantoor|ja|
|[[Wiki/Bedrijfsobjecten/99-kern/woz-waarde-bo\|WOZ-waarde]]|object|Vastgestelde marktwaarde van een WOZ-object per waardepeildatum| ✅ | ja |6/6 criteria, exact GGM-match|WOZ-waarde 2025: €350.000|ja|
|belastingplichtige|actor|Persoon die belasting moet betalen| ❌ | nee |Rol van een persoon, geen zelfstandig concept|Eigenaar woning, hondenbezitter|nee|
|heffingsmaatstaf|object|Maatstaf waarmee de belastingschuld wordt bepaald| ❌ | ja |Eigenschap van verordening, geen eigen bestaan|WOZ-waarde, oppervlakte, aantal honden|nee|
|tarief|object|Bedrag of percentage per eenheid heffingsmaatstaf| ❌ | ja |Eigenschap van verordening, geen eigen bestaan|0,1% van WOZ-waarde|nee|
|woz-beschikking|object|Formele bekendmaking WOZ-waarde aan belanghebbende| ❌ | ja |Onderdeel WOZ-proces, geen zelfstandig bestaan los van WOZ-object|WOZ-beschikking 2025|nee|
|onroerende zaak|object|Object van OZB-heffing en WOZ-waardering (BW-begrip)| ❌ | ja |Juridisch begrip, het BO is WOZ-object|Woning, grond, kantoor|ja: via WOZ-object|
|woonlasten|thema|OZB + rioolheffing + afvalstoffenheffing per huishouden| ❌ | nee |Aggregaat, geen object|€900/jaar gemiddeld|nee|

### Juridisch kader en actoren

|Begrip|Type|Omschrijving|BO?| Data-object |Reden|Voorbeelden|GGM|
|---|---|---|---|---|---|---|---|
|belastinggebied|thema|Het geheel aan wettelijke heffingsmogelijkheden van gemeenten| ❌ | nee |Beleidsmatig, geen object|Gesloten stelsel Gemeentewet|nee|
|belastingmix|thema|De gekozen combinatie van belastingen en tarieven| ❌ | nee |Beleidskeuze, geen object|—|nee|
|kostendekkend tarief|thema|Principe dat opbrengsten de kosten niet mogen overschrijden| ❌ | nee |Rechtsbeginsel, geen object|Max 100% dekking retributies|nee|
|kostenonderbouwing|thema|Verplichte verantwoording kosten bij lokale heffingen| ❌ | nee |Proces, geen object|BBV-rapportage|nee|
|kruissubsidiering|thema|Overschot ene activiteit dekt tekort andere binnen heffing| ❌ | nee |Beleidsmatig principe|Binnen legesverordening|nee|
|onbenutte belastingcapaciteit|thema|Verschil tussen feitelijke en maximale OZB-opbrengst| ❌ | nee |Kengetal, geen object|—|nee|
|algemene middelen|thema|Niet-gelabelde gemeentelijke opbrengsten| ❌ | nee |Financieel begrip, geen object|—|nee|
|heffingsambtenaar|actor|Legt belastingaanslagen op| ❌ | nee |Rol, geen zelfstandig concept|—|nee|
|invorderingsambtenaar|actor|Int belastingaanslagen| ❌ | nee |Rol, geen zelfstandig concept|—|nee|
|waarderingskamer|actor|Toezichthouder op WOZ-uitvoering| ❌ | nee |Externe organisatie, buiten gemeentelijk perspectief|—|nee|

### GGM Parkeren (gerelateerde BO-kandidaten)

|Begrip|Type|Omschrijving|BO?| Data-object |Reden|Voorbeelden|GGM|
|---|---|---|---|---|---|---|---|
|[[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/naheffing\|Naheffing]]|object|Aanslag bij niet/te weinig betalen parkeerbelasting| ✅ | ja |6/6 criteria, exact GGM-match (Naheffing)|Parkeerboete €70|ja|
|[[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeervergunning\|Parkeervergunning]]|object|Vergunning om te parkeren in aangewezen gebied| ✅ | ja |6/6 criteria, exact GGM-match|Bewonersvergunning zone A|ja|
|[[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeerrecht\|Parkeerrecht]]|object|Recht op parkeren na betaling| ✅ | ja |6/6 criteria, exact GGM-match|Parkeerticket 2 uur|ja|

## GGM-dekkingsanalyse

Het GGM heeft geen beleidsdomein "Belastingen". Relevante entiteiten per GGM-domein:

| GGM-domein | Relevante entiteiten | Status |
|---|---|---|
| RSGBPlus (99 Kern) | WOZ-object, WOZ-Waarde, WOZ-deelobject, SoortWOZObject | WOZ-object en WOZ-Waarde → BO |
| Vastgoed (9 Int. Org.) | WOZ-Belang, LocatieaanduidingWozObject | Technische tussenentiteiten |
| Financien (9 Int. Org.) | Debiteur, Kostenplaats | Debiteur → BO (in domein Financien) |
| Parkeren (2 V&V) | Naheffing, Parkeerrecht, Parkeervergunning, Parkeerzone, Parkeervlak | 3 → BO |
| VTH (1 Veiligheid) | Heffing, Heffingsverordening, Heffinggrondslag, Precario | Heffing en Heffingsverordening → BO; Heffinggrondslag is tussenentiteit; Precario bevestigd |

**Opmerking:** het heffingsproces (verordening → maatstaf → tarief → aanslag → invordering) is niet als samenhangend domein gemodelleerd in het GGM, maar de kernentiteiten Heffing en Heffingsverordening bestaan wel in GGM VTH/Kern en zijn nu als BO vastgelegd.

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/Belastingen/belastingtypen|Belastingtypen]] — Drie typen gemeentelijke belastingen
- [[Wiki/Bronsamenvattingen/Belastingen/belastinggebied|Belastinggebied]] — Reikwijdte belastinggebied, gesloten stelsel
- [[Wiki/Bronsamenvattingen/Belastingen/belastingpolitiek|Belastingpolitiek]] — Beleidskeuzes bij de belastingmix
- [[Wiki/Bronsamenvattingen/Belastingen/belastingverordening|Belastingverordening]] — De verordening als juridisch instrument
- [[Wiki/Bronsamenvattingen/Belastingen/bevoegdhedenverdeling|Bevoegdhedenverdeling]] — Rollen raad, college, ambtenaren
- [[Wiki/Bronsamenvattingen/Belastingen/invordering-en-kwijtschelding|Invordering en kwijtschelding]] — Invorderingsproces en kwijtscheldingsbeleid
- [[Wiki/Bronsamenvattingen/Belastingen/kostendekkende-tarieven|Kostendekkende tarieven]] — Kostendekkendheidsbeginsel
- [[Wiki/Bronsamenvattingen/Belastingen/wettelijke-grenzen|Wettelijke grenzen]] — Juridische grenzen en rechtsbeginselen
- [[Wiki/Bronsamenvattingen/Belastingen/raadgever-gemeentelijke-belastingen|Raadgever Gemeentelijke belastingen]] — Belastingmix, typen, grenzen
- [[Wiki/Bronsamenvattingen/Belastingen/raadgever-kostenonderbouwing|Raadgever Kostenonderbouwing van lokale heffingen]] — Tariefverschillen en kostenonderbouwingsplicht
- [[Wiki/Bronsamenvattingen/Belastingen/raadgever-woz|Raadgever Wet waardering onroerende zaken (WOZ)]] — WOZ-waarde, taxatie, Waarderingskamer
- [[Wiki/Bronsamenvattingen/Belastingen/onroerendezaakbelastingen|Onroerendezaakbelastingen]] — OZB: twee belastingen, WOZ-waarde, vrijstellingen, roerende-zaakbelasting
- [[Wiki/Bronsamenvattingen/Belastingen/parkeerbelastingen|Parkeerbelastingen]] — Incidenteel/vergunningparkeren, naheffing, wielklem, mobiel parkeren
- [[Wiki/Bronsamenvattingen/Belastingen/precariobelasting|Precariobelasting]] — Gebruik openbare grond, gedoogplicht
- [[Wiki/Bronsamenvattingen/Belastingen/reclamebelasting|Reclamebelasting]] — Openbare aankondigingen, ondernemersfonds
- [[Wiki/Bronsamenvattingen/Belastingen/hondenbelasting|Hondenbelasting]] — Houderschap, gezinshond, jurisprudentie
- [[Wiki/Bronsamenvattingen/Belastingen/biz-bijdrage|BIZ-bijdrage]] — Wet BIZ, draagvlakmeting, uitvoeringsovereenkomst
- [[Wiki/Bronsamenvattingen/Belastingen/retributies|Retributies]] — Leges, marktgeld, havengeld, lijkbezorgingsrechten, Wet markt en overheid
- [[Wiki/Bronsamenvattingen/Belastingen/reinigingsheffingen|Reinigingsheffingen]] — Afvalstoffenheffing en reinigingsrechten, tariefvormen
- [[Wiki/Bronsamenvattingen/Belastingen/riool-en-waterzorgheffing|Riool- en waterzorgheffing]] — Watertaken, collectief goed, verbreding heffingsgrondslag
- [[Wiki/Bronsamenvattingen/Belastingen/toeristische-heffingen|Toeristische heffingen]] — Toeristenbelasting, forensenbelasting, watertoeristenbelasting
- [[Wiki/Bronsamenvattingen/Belastingen/beleidsregels-gemeentelijke-belastingen-dfm|Beleidsregels DFM]] — Aanwijzing belastingplichtige, ambtshalve vermindering, uitvoeringsregeling

## Openstaande acties

- Terugmelding GGM: ontbreken beleidsdomein Belastingen als samenhangend domein
