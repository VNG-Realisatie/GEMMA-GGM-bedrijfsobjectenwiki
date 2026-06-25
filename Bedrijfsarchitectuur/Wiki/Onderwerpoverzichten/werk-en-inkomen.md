---
type: domein
naam: Werk en Inkomen
status: afgerond
verwerkingsdatum: 2026-06-25
bronnen_count: 1
begrippen_count: 15
bo_count: 2
---

# Werk en Inkomen

Gemeentelijke uitvoering van inkomensondersteuning op grond van de Participatiewet: bijstandsverlening, bijzondere bijstand, individuele inkomenstoeslag, en tijdelijke inkomensregelingen (TONK, energietoeslag). Het domein omvat de keten van aanvraag via draagkrachtbeoordeling en beschikking naar verstrekking.

## Begrippentabel

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]] | object | Toegekende financiële regeling die voorziet in inkomen of noodzakelijke kosten | ✅ | ja | 6/6 criteria; exact GGM-match; overkoepelt structurele en tijdelijke regelingen | Bijstandsuitkering, individuele inkomenstoeslag, energietoeslag | ja |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/draagkracht\|Draagkracht]] | object | Berekend vermogen van inwoner om zelf in kosten te voorzien | ✅ | ja | 6/6 criteria; exact GGM-match; bepalend voor recht op bijzondere bijstand | Draagkrachtberekening met inkomen en vermogen | ja |
| bijzondere bijstand | object | Verstrekking voor kosten uit bijzondere omstandigheden (art. 35 Pw) | subtype | ja | Subtype van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]] | Vergoeding koelkast, medische kosten | ja |
| individuele inkomenstoeslag | object | Jaarlijkse toeslag bij langdurig minimuminkomen (art. 36 Pw) | subtype | ja | Subtype van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]] | Toeslag €400/jaar | ja |
| energietoeslag | object | Categoriale bijstandsregeling voor energiekosten (2022-2023) | subtype | ja | Subtype van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]]; tijdelijk | Energietoeslag €1300 | nee |
| TONK | object | Tijdelijke Ondersteuning Noodzakelijke Kosten (covid, 2021) | subtype | ja | Subtype van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]]; tijdelijk | TONK-uitkering woonlasten | nee |
| collectieve zorgverzekering | object | Premiesubsidie aanvullende zorgverzekering (gemeentepolis) | subtype | ja | Subtype van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]]; categoriale bijstand | Gemeentepolis met uitgebreide dekking | nee |
| beschermingsbewind | object | Rechterlijk opgelegde vermogensbescherming; kosten via bijzondere bijstand | ❌ | ja | Rechterlijke maatregel, niet door gemeente opgelegd; kosten worden wél via bijzondere bijstand vergoed | Schuldenbewind, toestandsbewind | nee |
| verstrekkingsvorm | classificatie | Wijze van uitkering: gift, lening, natura | ❌ | ja | Classificatie, geen zelfstandig object | Om niet, geldlening, in natura | ja |
| cluster bijzondere bijstand | classificatie | CBS-indeling in 12 kostensoorten | ❌ | ja | Registratieclassificatie, geen zelfstandig object | Directe levensbehoeften, financiële transacties, voorzieningen wonen | nee |
| voorliggende voorziening | object | Bestaande regeling die recht op bijzondere bijstand uitsluit | ❌ | ja | Toetsingsconcept in beoordeling, niet zelfstandig geregistreerd | Zorgtoeslag, huurtoeslag | ja |
| draagkrachtregime | object | Van toepassing zijnd regime op de draagkracht | ❌ | ja | Classificatie/parameter van Draagkracht, niet zelfstandig BO | Regime met initiële en resterende draagkracht | ja |
| niet-gebruik | meting | Percentage doelgroep dat geen gebruik maakt van regeling | ❌ | nee | Statistisch gegeven, geen object | 43% niet-gebruik bijzondere bijstand | nee |
| inkomensgrens / norminkomen | parameter | Inkomensdrempel voor recht op categoriale bijstand (bijv. 110% minimum) | ❌ | nee | Beleidsparameter, geen object | 110% bijstandsnorm | nee |
| kwijtschelding gemeentelijke belastingen | object | Ontheffing van gemeentelijke heffingen voor minima | ❌ | ja | Hoort bij belastingdomein, niet bij bijzondere bijstand | Kwijtschelding rioolheffing | nee |

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/Werk en Inkomen/factsheet-bijzondere-bijstand|Factsheet Bijzondere Bijstand]] — Divosa/BMC/Stimulansz, mei 2024: feiten en cijfers bijzondere bijstand 2010-2022

## Niet-relevante bronnen

7 bronnen verplaatst naar `Sources/Onderwerpen/Werk en Inkomen/Niet-relevant/`: arbeidsmarktbeleid, inkomensondersteuning-alleenverdieners, migratie-en-werk, participatiewet-in-balans, rubriek-werk-inkomen-en-sociale-zekerheid, werk-en-inkomen-toezicht-en-handhaving, wet-sociale-werkvoorziening-wsw. Alle dunne VNG-portaalpagina's zonder objectdefinities.

## Nog te verwerken bronnen

Voor verdere verdieping zijn inhoudelijke beleidsdocumenten nodig, met name:
- Gemeentelijke beleidsregels bijzondere bijstand (een specifieke gemeente)
- Verordening individuele inkomenstoeslag
- Uitvoeringsbeleid minimaregelingen

## Openstaande vragen

- Beschermingsbewind is de grootste kostenpost (1/3 van alle bijzondere bijstand) maar wordt niet door de gemeente opgelegd — is dit op termijn een apart BO vanuit het schuldendomein?
- Het GGM modelleert het Inkomen-domein via vijf beleidsdomeinen (Diensten, Model Inkomen, Normafwijking, Reden aanvraag, plus Sociaal Domein Generiek) met veel procesdetail. Bij verwerking van uitvoeringsbeleid zullen meer GGM-entiteiten beoordeeld kunnen worden.
- De relatie tussen Inkomensvoorziening (Model Inkomen) en Dienst (Diensten) in het GGM is onduidelijk — zijn dit hetzelfde concept of complementair?

## Terugmeldingen richting GGM

Zie [[Wiki/Analyses/ggm-terugmeldingen]]:
- **Inkomensvoorziening**: definitie bevat typefouten en is te beperkt (dekt niet bijzondere kosten)
- **Draagkracht**: definitie bevat vraagtekens en informeel taalgebruik
- **Periodiek dienst Bijz. bijstand**: GGM markeert deze zelf als redundant — bevestigd door analyse
