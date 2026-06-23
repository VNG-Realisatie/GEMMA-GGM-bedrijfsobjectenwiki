---
type: analyse
titel: "GGM-hiaten: het belastingendomein ontbreekt als conceptueel model"
datum: 2026-06-17
aanleiding: Mapping van gemeentelijke beleidsbegrippen uit VNG-bronnen op het GGM v2.5.1
status: in opbouw
---

# GGM-hiaten: het belastingendomein

## Samenvatting

Bij het mappen van begrippen uit gemeentelijke belastingdocumenten (VNG) op het Gemeentelijk Gegevensmodel (GGM v2.5.1, Gemeente Delft) blijkt dat het GGM **geen conceptueel model heeft voor het belastingendomein**. De belastingheffing — een van de kernprocessen van elke gemeente — is niet als samenhangend domein gemodelleerd.

De hiaat is niet op elk abstractieniveau even problematisch. Dat het GGM geen normatieve waarden of strategische doelen modelleert is logisch — dat is niet de functie van een informatiemodel. Dat het GGM geen operationele objecten kent voor het heffingsproces (aanslag, tarief, maatstaf) is het eigenlijke hiaat.

## Wat het GGM wél heeft

Het GGM is opgebouwd uit taakvelden (afgeleid van IV3) en beleidsdomeinen daaronder (zie [[GGM-indeling]]). Het belastingendomein wordt indirect geraakt via twee beleidsdomeinen:

| Beleidsdomein | Taakveld | Dekking | Wat het modelleert |
|---|---|---|---|
| **[[Wiki/Onderwerpoverzichten/financien\|financien]]** | 9 Interne Organisatie | Boekhoudkundig | Begrotingen, facturen, kostenplaatsen, taakvelden, bankrekeningen — de *financiële administratie*, niet de belastingheffing zelf |
| **[[Wiki/Onderwerpoverzichten/terug-en-invordering\|terug-en-invordering]]** | 6 Sociaal Domein → Inkomen | Invorderingsproces | Vorderingen, aflossing, kwijtschelding, beslag — het *innen* van vorderingen, niet het *opleggen* van aanslagen |

Daarnaast bestaat er een `enum_Belasting` enumeratie en gerelateerde classificaties (`BelastingklasseNieuw`, `BelastingklasseOud`), maar deze zijn niet ingebed in een domeinmodel.

## Begrippen per abstractieniveau

### Strategisch — geen GGM-match verwacht

Strategische begrippen drukken beleidsdoelen uit. Het GGM hoeft deze niet te modelleren, maar ze geven context aan welke operationele objecten er zouden moeten zijn.

| Begrip | Type | GGM-status | Toelichting |
|---|---|---|---|
| **belastingmix** | doel | Geen entiteit | Gekozen combinatie van belastingen en tarieven — stuurt welke operationele objecten nodig zijn |

### Tactisch — gedeeltelijk GGM-match verwacht

Tactische begrippen organiseren het werk: instrumenten, thema's, doelgroepen. Het GGM raakt dit niveau via beleidsdomeinen en actoren, maar dekt het voor belastingen niet.

| Begrip | Type | GGM-status | Toelichting |
|---|---|---|---|
| **gemeentelijke-belasting** | thema | Geen entiteit, geen taxonomie | Overkoepelend begrip; GGM kent geen belastingentypologie |
| **algemene-belasting** | instrument | Geen entiteit | Classificatie binnen belastingtypologie |
| **bestemmingsbelasting** | instrument | Geen entiteit | Classificatie binnen belastingtypologie |
| **retributie** | instrument | Geen entiteit | Classificatie binnen belastingtypologie |
| **leges** | instrument | Geen entiteit | Subcategorie van retributie |
| **belastinggebied** | instrument | Geen entiteit | Wettelijke begrenzing van heffingsmogelijkheden |
| **belastingverordening** | instrument | Geen entiteit | Juridische grondslag — centraal object in het heffingsproces |
| **kostendekkend-tarief** | instrument | Geen entiteit | Business rule: opbrengsten ≤ kosten |
| **kwijtschelding** | thema | **Deels**: GGM "Kwijtschelding" (T&I) | GGM-context is sociaal domein, niet belastinginvordering |

### Operationeel — GGM-match verwacht, grotendeels afwezig

Operationele begrippen duiden objecten, actoren en doelgroepen die in processen worden gebruikt en in informatiesystemen worden geregistreerd. Hier zit het eigenlijke GGM-hiaat.

| Begrip | Type | GGM-status | Toelichting |
|---|---|---|---|
| **belastingaanslag** | object | **Hiaat** — "Vordering" (T&I) is anders georiënteerd | Kern van het heffingsproces; ontbreekt volledig |
| **heffingsmaatstaf** | object | **Hiaat** — deels geraakt via WOZ-OBJECT (RSGB) | Grondslag waarop belastingschuld wordt bepaald |
| **woonlasten** | object | **Hiaat** — samengesteld begrip | OZB + rioolheffing + afvalstoffenheffing per huishouden |
| **algemene-middelen** | object | **Hiaat** | Niet-gelabelde opbrengsten, vrij inzetbaar |
| **belastingplichtige** | doelgroep | **Deels**: "Debiteur" (Financien) is breder | Persoon die belasting moet betalen |
| **heffingsambtenaar** | actor | **Hiaat** | Wettelijke rol, legt aanslagen op — bevoegdheid uit AWR |
| **invorderingsambtenaar** | actor | **Hiaat** | Wettelijke rol, int aanslagen — bevoegdheid uit AWR |

### Overzicht hiaten per niveau

| Niveau | Begrippen | Verwachte GGM-match | Feitelijke match | Hiaat |
|---|---|---|---|---|
| Strategisch | 1 | Niet verwacht | 0 | — |
| Tactisch | 9 | Gedeeltelijk | 1 (deels) | Belastingtypologie en instrumenten ontbreken |
| Operationeel | 7 | Volledig | 1 (deels) | **Heffingsproces ontbreekt volledig** |

Het patroon is helder: het GGM mist het complete heffingsdomein. De tactische hiaten (geen belastingtypologie) en operationele hiaten (geen aanslag, tarief, maatstaf) hangen samen — zonder domeinmodel is er ook geen structuur om objecten in te plaatsen.

## Kandidaat-entiteiten voor een GGM-belastingendomein

Alleen operationele objecten zijn kandidaat voor GGM-entiteiten. Tactische instrumenten (belastingverordening, belastinggebied) worden pas kandidaat als het GGM ook regelgeving gaat modelleren.

| Kandidaat-entiteit | Begripstype | Toelichting | Relatie met bestaand GGM |
|---|---|---|---|
| **Belasting** | object | Abstracte entiteit met typering (algemeen/bestemming/retributie) | Zou kunnen verwijzen naar Begroting/Taakveld in Financien |
| **Belastingaanslag** | object | Het concrete heffingsbesluit richting een belastingplichtige | Sluit aan op Vordering in Terug-en-invordering |
| **Belastingplichtige** | doelgroep | Persoon of organisatie die belasting verschuldigd is | Sluit aan op Debiteur in Financien |
| **Tarief** | object | Bedrag of percentage per belastingsoort | Niet gemodelleerd — essentieel voor berekening aanslag |
| **Heffingsmaatstaf** | object | Grondslag waarop de heffing wordt berekend (WOZ-waarde, oppervlakte, etc.) | Deels geraakt via WOZ-OBJECT/WOZ-WAARDE in RSGB |

| Kandidaat-rol | Begripstype | Toelichting |
|---|---|---|
| **Heffingsambtenaar** | actor | Legt aanslagen op, beslist op bezwaar — bevoegdheid uit AWR |
| **Invorderingsambtenaar** | actor | Int aanslagen, verleent kwijtschelding — bevoegdheid uit AWR |

Tactische begrippen als belastingverordening en belastinggebied zijn relevant voor de bedrijfsarchitectuur maar niet per se kandidaat voor GGM-entiteiten — ze beschrijven het kader waarbinnen operationele objecten functioneren.

## Structureel hiaat

Het GGM is opgebouwd uit taakvelden (afgeleid van IV3) met daaronder beleidsdomeinen (zie [[GGM-indeling]]). De kern is gebaseerd op RSGB (basisgegevens) en RGBZ (zaakgericht werken), aangevuld met domeinmodellen. Het belastingendomein valt tussen drie stoelen:

1. **Kern (taakveld 99) / RSGB** levert basisgegevens (personen, objecten, WOZ) die als grondslag dienen voor de heffing, maar modelleert de heffing zelf niet.
2. **Financien (beleidsdomein onder taakveld 9)** modelleert de boekhoudkundige verwerking van opbrengsten, maar niet de belastingheffing als proces.
3. **Terug- en invordering (beleidsdomein onder taakveld 6 → Inkomen)** modelleert het innen, maar begint pas nadat een aanslag is opgelegd. Bovendien is dit domein gepositioneerd onder het Sociaal Domein/Inkomen, terwijl belastinginvordering een breder toepassingsgebied heeft.

Het ontbrekende stuk is het **heffingsproces**: van belastingverordening → tarief → heffingsmaatstaf → aanslag → belastingplichtige. Dit is het domein dat gemeentelijke belastingapplicaties (zoals Centric Belastingen, PinkRoccade Heffingen) ondersteunen, maar dat niet in het GGM als conceptueel model is uitgewerkt.

## Procesmodel (ontbrekend in GGM)

Op basis van de verwerkte VNG-bronnen is het volgende procesmodel te reconstrueren:

```
Gemeenteraad
  └─ stelt vast → Belastingverordening
                    ├─ definieert → Belastingplichtige (wie betaalt)
                    ├─ definieert → Heffingsmaatstaf (waarover)
                    ├─ definieert → Tarief (hoeveel)
                    └─ definieert → Vrijstellingen

Heffingsambtenaar
  └─ past toe → Belastingverordening
                  └─ resulteert in → Belastingaanslag
                                      └─ gericht aan → Belastingplichtige

Invorderingsambtenaar
  └─ int → Belastingaanslag
            ├─ betaling
            ├─ aanmaning → dwangbevel
            └─ Kwijtschelding (bij onvermogen)
```

## Overlap met GGM Terug-en-invordering

Het GGM beleidsdomein Terug-en-invordering modelleert een vergelijkbaar invorderingsproces (Vordering → Aflossing → Kwijtschelding) maar dan specifiek voor het sociaal domein (terugvordering bijstand). De structuurovereenkomst suggereert dat een generalisatie mogelijk is:

| Belastingendomein | Terug-en-invordering (GGM) | Overeenkomst |
|---|---|---|
| Belastingaanslag | Vordering | Eis tot betaling van bedrag |
| Betaling | Aflossing | Ontvangst van verschuldigd bedrag |
| Kwijtschelding | Kwijtschelding | Kwijtschelding restant |
| Aanmaning/dwangbevel | Interventie | Escalatie bij niet-betaling |

## Aanbeveling

Overweeg een nieuw beleidsdomein **"Belastingen"** (of "Heffingen") onder taakveld 9 (Interne Organisatie) of als apart taakveld, met:

- Een abstracte entiteit **Belasting** met typering (algemeen/bestemming/retributie)
- Entiteiten voor **Belastingaanslag**, **Tarief**, **Heffingsmaatstaf**, **Belastingverordening**
- Relaties naar bestaande GGM-entiteiten: Debiteur, Vordering, Begroting, Taakveld, WOZ-OBJECT
- Generalisatie van het invorderingsproces zodat het zowel belastinginvordering als bijstandsterugvordering dekt

## Bronnen

- VNG: Belastingtypen, Belastinggebied, Belastingpolitiek, Belastingverordening, Bevoegdhedenverdeling, Invordering en kwijtschelding, Kostendekkende tarieven, Wettelijke grenzen
- GGM v2.5.1, Gemeente Delft (github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel)

## Update 2026-06-18: WOZ-bedrijfsobjecten en Financiën-hiaten

### WOZ: match gevonden

De verwerking van de Raadgever WOZ leverde twee bedrijfsobjecten op met directe GGM-match:

| Bedrijfsobject | GGM-entiteit | GGM-beleidsdomein | Status |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/woz-object\|woz-object]] | WOZ-object | RSGBPlus (taakveld 99 Kern) | **Match** — attributen en relaties dekken het bedrijfsperspectief |
| [[Wiki/Bedrijfsobjecten/99-kern/woz-waarde-bo\|woz-waarde-bo]] | WOZ-Waarde | RSGBPlus (taakveld 99 Kern) | **Match** — inclusief beschikkingsaspect (statusBeschikking) |

De WOZ-beschikking is geen apart bedrijfsobject: het GGM modelleert het als attribuut van WOZ-Waarde, en op bedrijfsniveau is de beschikking niet onderscheidbaar van de waardebepaling.

Dit bevestigt het patroon: het GGM dekt de **basisregistratie-kant** (WOZ-object, WOZ-Waarde, WOZ-Belang) goed, maar de **heffingsketen** (waarde → tarief → aanslag → belastingplichtige) ontbreekt nog steeds.

### Financiën-domein: procesmodel ontbreekt

De verwerking van vier Raadgever-bronnen over gemeentefinanciën (inkomstenbronnen, begrotingscyclus, financiële verordening, financiële conditie) levert een vergelijkbaar patroon op als bij Belastingen: het GGM dekt de **objecten** (Begroting, Kostenplaats, Factuur, etc.) maar niet de **processen en instrumenten**.

#### Begrippen zonder GGM-match (Financiën)

| Begrip | Type | Niveau | GGM-status | Toelichting |
|---|---|---|---|---|
| **gemeentefonds** | instrument | tactisch | **Hiaat** | Hoofdinkomstenbron; niet gemodelleerd |
| **algemene-uitkering** | instrument | tactisch | **Hiaat** | Component gemeentefonds |
| **specifieke-uitkering** | instrument | tactisch | **Hiaat** | Geoormerkte rijksmiddelen |
| **begrotingscyclus** | thema | operationeel | **Hiaat** (proces) | Kadernota→begroting→jaarrekening; objecten bestaan wel |
| **budgetrecht** | instrument | tactisch | **Hiaat** | Kernbevoegdheid raad; governance, niet data |
| **financiele-verordening** | instrument | tactisch | **Hiaat** | Art. 212 Gemeentewet; regelgeving niet gemodelleerd |
| **kadernota** | object | operationeel | **Hiaat** | Voorjaarsnota; niet als documenttype gemodelleerd |
| **solvabiliteitsratio** | object | operationeel | **Hiaat** (afgeleid) | Kengetal; afleidbaar uit balansgegevens |
| **netto-schuldquote** | object | operationeel | **Hiaat** (afgeleid) | Kengetal; afleidbaar uit balansgegevens |
| **onbenutte-belastingcapaciteit** | object | operationeel | **Hiaat** (afgeleid) | Kengetal; afleidbaar uit OZB-opbrengst + art. 12-tarief |

#### Wat het GGM wél dekt (Financiën)

Het GGM beleidsdomein Financien (taakveld 9, 24 entiteiten) dekt de **boekhoudkundige objecten** goed:

| GGM-entiteit | Bedrijfsobject | Dekking |
|---|---|---|
| Begroting | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/begroting\|begroting]] | Product van de begrotingscyclus |
| Begrotingregel | *(niet als BO)* | Te granulair |
| Taakveld | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/taakveld\|taakveld]] | IV3-indeling |
| Doelstelling | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/doelstelling\|doelstelling]] | W-vragen ("wat bereiken") |
| Product | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/product\|product]] | P×Q-sturing |
| Kostenplaats | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/kostenplaats\|kostenplaats]] | Interne toerekening |
| Factuur, Inkooporder, Werkorder | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/factuur\|factuur]], [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/inkooporder\|inkooporder]], [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/werkorder\|werkorder]] | Operationele objecten |
| Debiteur | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/debiteur\|debiteur]] | Wie moet betalen |
| Activa | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/activa\|activa]] | Bezittingen op de balans |

#### Structureel patroon

Het GGM volgt consistent hetzelfde patroon over domeinen heen:

| Laag | Belastingen | Financiën | GGM-dekking |
|---|---|---|---|
| Basisregistratie-objecten | WOZ-object, WOZ-Waarde, Rechtspersoon | — | **Goed** |
| Boekhoudkundige objecten | — | Begroting, Kostenplaats, Factuur | **Goed** |
| Procesmodel | Heffingsproces (verordening→aanslag) | Begrotingscyclus (kadernota→jaarrekening) | **Ontbreekt** |
| Instrumenten/governance | Belastingverordening, belastingmix | Financiële verordening, budgetrecht | **Ontbreekt** |
| Inkomstenbronnen | — | Gemeentefonds, uitkeringen | **Ontbreekt** |
| Kengetallen | — | Solvabiliteit, schuldquote | **Ontbreekt** (afleidbaar) |

Het GGM modelleert **wat er in systemen staat** (objecten), niet **hoe processen verlopen** (instrumenten, cycli) of **hoe gestuurd wordt** (governance). Dit is logisch voor een informatiemodel, maar voor de bedrijfsarchitectuur zijn juist de procesmodellen en governance-instrumenten essentieel.

#### Aanbeveling Financiën

De kengetallen (solvabiliteitsratio, netto schuldquote, onbenutte belastingcapaciteit) zijn **afleidbaar** uit bestaande GGM-objecten (Begroting, Activa, Debiteur) en hoeven niet als entiteiten te worden gemodelleerd. Ze zijn wel relevant als **business intelligence indicators** in de bedrijfsarchitectuur.

De begrotingscyclus en governance-instrumenten (financiële verordening, budgetrecht) vallen buiten de scope van het GGM als informatiemodel maar zijn essentieel voor de ArchiMate-laag (business processes, business rules).

## Update 2026-06-22: GGM-matches gevonden, hiaten bijgesteld

Bij de volledige ingest van alle Belastingen-bronnen (22 bronnen totaal) zijn twee GGM-matches gevonden die eerder als hiaten waren genoteerd:

| Bedrijfsobject | GGM-entiteit | GGM-beleidsdomein | Taakveld | Status |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/heffing\|Heffing]] | Heffing | RGBZPlus | 99 Kern | **Match** — generieke entiteit "verplichting tot betaling" |
| [[Wiki/Bedrijfsobjecten/99-kern/heffingsverordening\|Heffingsverordening]] | Heffingsverordening | 1 Veiligheid en Vergunningen | 1 VTH | **Match** — exacte definitie belastingverordening |

**Bijstelling hiaat-analyse:** het GGM heeft wél kernentiteiten voor het heffingsproces (Heffing, Heffingsverordening, Heffinggrondslag), maar deze zitten verspreid over RGBZPlus (99 Kern) en VTH (taakveld 1), niet in een samenhangend domeinmodel. Het structurele hiaat is daarmee verfijnd: niet "het heffingsproces ontbreekt volledig" maar "het heffingsproces is niet als samenhangend domein gemodelleerd".

De eerder geïdentificeerde Kandidaat-entiteit "Belastingaanslag" blijkt te mappen op de bestaande GGM-entiteit Heffing. De Kandidaat-entiteit "Belastingverordening" op Heffingsverordening. De overige kandidaten (Belasting als abstractie, Tarief, Belastingplichtige als doelgroep) blijven ongedekt.

## Status

Alle Belastingen-bronnen zijn verwerkt. Domein afgerond met 22 bronnen, 46 begrippen, 9 BO's.
