---
type: analyse
titel: "Entiteitendekking: 7 Volksgezondheid en Milieu"
datum: 2026-07-07
taakveld: "7 Volksgezondheid en Milieu"
beleidsdomeinen:
  - Afval
totaal_entiteiten: 16
totaal_bo: 35
totaal_matches: 4
totaal_hiaten: 31
---

# Entiteitendekking: 7 Volksgezondheid en Milieu

## Beoordeling

Dit taakveld heeft in het GGM maar één beleidsdomein: Afval, met 16 entiteiten en volledige dekking (16/16, 100%). De niet-BO entiteiten volgen het bekende patroon — 2× classificatie (Containertype, Melding: typering/referentietabel), 1× component (Prijsregel, onderdeel van Grondstofstroom) en 9× detail: vrijwel allemaal operationele gebeurtenissen en meetgegevens rond inzameling (Categorie, Ophaalmoment, Pas, Rit, Route, Storting, Vuilniswagen, Vulgraadmeting, Locatie), die terecht geen zelfstandig BO vormen maar attribuut- of gebeurtenisniveau blijven bij Container, Milieustraat of Grondstofstroom.

De echte bevinding zit in de omvang van het GGM-hiaat: 31 BO's zonder GGM-entiteit tegenover slechts 4 matches — verreweg de scherpste onbalans van alle taakvelden (elders blijft dit meestal onder de 10-15). De oorzaak is structureel: het GGM in dit taakveld dekt uitsluitend het afvalinzamelingsproces (containers, ophaalmomenten, grondstofstromen, milieustraat), terwijl de wiki BO's bevat uit vijf andere beleidsdomeinen die in het GGM volledig ontbreken: Milieu breder (Afvalstoffenverordening, Bodemenergiesysteem, Bodemkwaliteitskaart, Bodemverontreiniging, Grondstoffendepot, Grondverzet, Grondwatermeetpunt, Inzamelcontract, Luchtkwaliteitsmeetpunt, Materiaalpasspoort, Milieuzone, Ontheffing (milieuzone), Rookvrije zone, Saneringsplan, Sloopregeling, Upcyclecentrum, Verwerkingscontract, Vuurwerkvrije zone, Walstroompunt), Dierenwelzijn (Dierenweide, Hulpbehoevend dier, Kinderboerderij, Visrecht), Geluid (Geluidbron, Geluidgevoelig gebouw, Geluidzone, Stil gebied), Energie en Klimaat (Koelteplek, Opwekgebied, Warmtenet) en Openbare Gezondheid (Infectieziektemelding). Dit zijn overwegend procesobjecten en governance-objecten, dus formele terugmelding als data-hiaat is niet dwingend, maar het patroon is veelzeggend: het GGM heeft dit taakveld nauwelijks gemodelleerd buiten de kernafvalketen, terwijl de wiki op basis van gemeentelijke bronnen een veel breder palet aan volksgezondheid- en milieuonderwerpen beschrijft.

Twee naamconflicten zijn zichtbaar via hernoeming: GGM-entiteit Fractie is vastgelegd als [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/grondstofstroom\|Grondstofstroom]] (preciezere, in de afvalsector gangbare term dan het generieke "Fractie"), en GGM-entiteit Prijsafspraak is vastgelegd als [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/afvalstoffenheffing\|Afvalstoffenheffing]] (de juridisch-formele belastingterm). Beide hernoemingen verduidelijken eerder dan dat ze een homoniemprobleem oplossen; er zijn geen kruisverwijzingen naar BO's in andere domeinen gesignaleerd.

## Afval

16 entiteiten, 4 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/7-volksgezondheid-en-milieu/afval\|Container]] | [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/container\|Container]] ✅ | — |  | Exact match |
| [[Wiki/GGM/7-volksgezondheid-en-milieu/afval\|Fractie]] | [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/grondstofstroom\|Grondstofstroom]] ✅ | synoniem |  | BO hernoemd: Grondstofstroom |
| [[Wiki/GGM/7-volksgezondheid-en-milieu/afval\|Milieustraat]] | [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/milieustraat\|Milieustraat]] ✅ | — |  | Exact match |
| [[Wiki/GGM/7-volksgezondheid-en-milieu/afval\|Prijsafspraak]] | [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/afvalstoffenheffing\|Afvalstoffenheffing]] ✅ | synoniem |  | BO hernoemd: Afvalstoffenheffing |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/7-volksgezondheid-en-milieu/afval\|Containertype]] | classificatie | typering [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/container\|Container]] | Typering/referentietabel |
| [[Wiki/GGM/7-volksgezondheid-en-milieu/afval\|Melding]] | classificatie | typering [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Typering/referentietabel |
| [[Wiki/GGM/7-volksgezondheid-en-milieu/afval\|Prijsregel]] | component | beschrijft [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/grondstofstroom\|Grondstofstroom]] | Component |
| [[Wiki/GGM/7-volksgezondheid-en-milieu/afval\|Categorie]] | detail | via Melding → [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/grondstofstroom\|Grondstofstroom]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/7-volksgezondheid-en-milieu/afval\|Locatie]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/container\|Container]] | Generiek kern-concept (Vastgoedobject); cross-domein |
| [[Wiki/GGM/7-volksgezondheid-en-milieu/afval\|Ophaalmoment]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/container\|Container]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/7-volksgezondheid-en-milieu/afval\|Pas]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/milieustraat\|Milieustraat]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/7-volksgezondheid-en-milieu/afval\|Rit]] | detail | via Ophaalmoment → [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/container\|Container]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/7-volksgezondheid-en-milieu/afval\|Route]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/grondstofstroom\|Grondstofstroom]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/7-volksgezondheid-en-milieu/afval\|Storting]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/grondstofstroom\|Grondstofstroom]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/7-volksgezondheid-en-milieu/afval\|Vuilniswagen]] | detail | via Containertype → [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/container\|Container]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/7-volksgezondheid-en-milieu/afval\|Vulgraadmeting]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/container\|Container]] | Detailgegeven (geassocieerd met BO) |

## BO's zonder GGM-entiteit

BO's waarvoor geen overeenkomstige GGM-entiteit bestaat. Data-objecten worden als hiaat teruggemeld aan het GGM-team; overige BO's bestaan alleen in GEMMA.

| BO | Data-object | Grondslag | Status |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/afvalstoffenverordening\|Afvalstoffenverordening]] | nee | governance-object | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/bodemenergiesysteem\|Bodemenergiesysteem]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/bodemkwaliteitskaart\|Bodemkwaliteitskaart]] | nee | governance-object | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/bodemverontreiniging\|Bodemverontreiniging]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/dierenwelzijn/dierenweide\|Dierenweide]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/geluid/geluidbron\|Geluidbron]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/geluid/geluidgevoelig-gebouw\|Geluidgevoelig gebouw]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/geluid/geluidzone\|Geluidzone]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/grondstoffendepot\|Grondstoffendepot]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/grondverzet\|Grondverzet]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/grondwatermeetpunt\|Grondwatermeetpunt]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/dierenwelzijn/hulpbehoevend-dier\|Hulpbehoevend dier]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/infectieziektemelding\|Infectieziektemelding]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/inzamelcontract\|Inzamelcontract]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/dierenwelzijn/kinderboerderij\|Kinderboerderij]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/energie-en-klimaat/koelteplek\|Koelteplek]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/luchtkwaliteitsmeetpunt\|Luchtkwaliteitsmeetpunt]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/materiaalpasspoort\|Materiaalpasspoort]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/milieuzone\|Milieuzone]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/ontheffing-milieuzone\|Ontheffing (milieuzone)]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/energie-en-klimaat/opwekgebied\|Opwekgebied]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/rookvrije-zone\|Rookvrije zone]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/saneringsplan\|Saneringsplan]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/sloopregeling\|Sloopregeling]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/geluid/stil-gebied\|Stil gebied]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/upcyclecentrum\|Upcyclecentrum]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/verwerkingscontract\|Verwerkingscontract]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/dierenwelzijn/visrecht\|Visrecht]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/vuurwerkvrije-zone\|Vuurwerkvrije zone]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/walstroompunt\|Walstroompunt]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/energie-en-klimaat/warmtenet\|Warmtenet]] | nee | procesobject | **Alleen GEMMA-BO** |
