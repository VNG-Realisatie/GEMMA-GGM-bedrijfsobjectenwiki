---
type: analyse
titel: "Entiteitendekking: 1 Veiligheid en Vergunningen"
datum: 2026-07-07
taakveld: "1 Veiligheid en Vergunningen"
beleidsdomeinen:
  - 1 Veiligheid en Vergunningen
totaal_entiteiten: 30
totaal_bo: 12
totaal_matches: 7
totaal_hiaten: 5
---

# Entiteitendekking: 1 Veiligheid en Vergunningen

## Beoordeling

1 beleidsdomeinen, 30 GGM-entiteiten. Dekking: 29 van 30 (97%) — 7 met BO, 22 ondersteunend, 1 niet gedekt. 5 BO's zonder GGM-entiteit.

Niet-BO entiteiten: 2× abstract, 2× classificatie, 2× component, 17× detail.

Het dominante patroon in dit taakveld is de aanvraag/melding-familie: MORAanvraagOfMelding, VOMAanvraagOfMelding, VTH-Melding, WABOAanvraagOfMelding, WoonfraudeAanvraagOfMelding en WoonoverlastAanvraagOfMelding zijn stuk voor stuk kanaal- of wetgevingsspecifieke varianten van dezelfde onderliggende [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] (VOM = Vergunning, Ontheffing of Melding; WABO/MOR/Woonfraude/Woonoverlast zijn wettelijke of proces-specifieke labels voor hetzelfde intaketype). VOMAanvraagOfMelding en VTH-Melding zijn daarbij zelf weer boventype van respectievelijk VTHAanvraagOfMelding/WABOAanvraagOfMelding en Combibon/Fietsregistratie/Waarneming — een tweetrapshiërarchie onder de generieke BO. Dat verklaart waarom het GGM hier met zes tot acht entiteiten modelleert wat de wiki bewust als één BO vastlegt: het zijn geen zelfstandige objecten maar registratievarianten van hetzelfde grondpatroon. Kosten en Leges_Grondslag vormen een tweede, kleiner cluster: financiële detailgegevens (tarief, bedrag, grondslag, accordering) die de leges- en heffingscomponent van een [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/vth-zaak\|VTH-zaak]] beschrijven, in lijn met de generieke BO's Heffinggrondslag/Heffingsverordening die dit taakveld al met 99 Kern deelt. Vordering wijkt hiervan af: met een eigen volgnummer, een goedkeurings- en exportstatus (geaccordeerd, geëxporteerd) én een eigen regel-entiteit (Vorderingregel) fungeert het niet als een attribuutachtig kenmerk maar als een gegenereerd financieel deeldossier binnen de VTH-zaak — vergelijkbaar met hoe Factuur/Factuurregel of Begroting/Begrotingregel elders in het GGM zijn opgebouwd. Vordering is daarom hier als component (van VTH-zaak) geherclassificeerd in plaats van detail; het krijgt geen eigen BO-status omdat de financiële afhandeling van een zaak al via Heffing/Heffinggrondslag (99 Kern) is gedekt en een aparte Vordering-BO dat zou dupliceren.

Functioneel is de dekking hoog (97%); alleen Precario (belastingsoort zonder attributen) heeft geen bereikbaar BO, wat past bij een klein modelleergat rond precariobelasting dat niet expliciet aan Heffing/Heffinggrondslag is gekoppeld. De vijf BO's zonder GGM-tegenhanger (Evenementenlocatie, Evenementenvergunning, Handhavingsbesluit, Register (omgevingsplan), Welstandsadvies) zijn stuk voor stuk procesobjecten — besluiten, registers en adviezen die uit het VTH-proces voortkomen maar geen apart data-object in het GGM hebben. Geen van deze vijf is als ggm-hiaat gemarkeerd: het GGM legt hier terecht de nadruk op de aanvraag/zaak/inspectie-kant van vergunningverlening en toezicht, en laat de procesuitkomsten (besluiten, adviezen) aan de wiki over, net als bij taakveld 10 Dienstverlening waar procesobjecten (Klacht, Woo-verzoek, DPIA) evenmin een GGM-tegenhanger hebben.

Naamconflicten zijn hier vooral zichtbaar bij de BO-matches, niet bij de Naamoverlap-kolom van de niet-BO entiteiten: VTHzaak, OpenbareActiviteit en Vaartuig zijn in de wiki hernoemd naar respectievelijk VTH-zaak, Evenement en Woonboot — leesbare Nederlandse namen voor generieke GGM-termen, geen inhoudelijk conflict. Vordering verdient hier aandacht omdat de naam op zichzelf een generiek juridisch begrip suggereert (een schuldvordering), terwijl de GGM-context de betekenis beperkt tot leges-/heffingvorderingen binnen een VTH-zaak; dat onderscheid is relevant mocht een breder begrip "vordering" elders in de wiki (bijvoorbeeld bij invordering van gemeentelijke belastingen) alsnog als BO worden vastgelegd.

## 1 Veiligheid en Vergunningen

30 entiteiten, 7 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|Bevinding]] | [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/bevinding\|Bevinding]] ✅ | — |  | Exact match |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|Heffinggrondslag]] | [[Wiki/Bedrijfsobjecten/99-kern/heffinggrondslag\|Heffinggrondslag]] ✅ | — |  | Exact match |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|Heffingsverordening]] | [[Wiki/Bedrijfsobjecten/99-kern/heffingsverordening\|Heffingsverordening]] ✅ | — |  | Exact match |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|Inspectie]] | [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/inspectie\|Inspectie]] ✅ | — |  | Exact match |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|OpenbareActiviteit]] | [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/evenementen/evenement\|Evenement]] ✅ | synoniem |  | BO hernoemd: Evenement |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|VTHzaak]] | [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/vth-zaak\|VTH-zaak]] ✅ | synoniem |  | BO hernoemd: VTH-zaak |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|Vaartuig]] | [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/woonboot\|Woonboot]] ✅ | synoniem |  | BO hernoemd: Woonboot |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|Producttype]] | classificatie | typering [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaaktype\|Zaaktype]] | Typering/referentietabel |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|SubProducttype]] | classificatie | typering [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/vth-zaak\|VTH-zaak]] | Typering/referentietabel |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|Vorderingregel]] | component | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/heffing\|Heffing]] | Component |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|AOMStatus]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|Activiteit Omgevingswet]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/vth-zaak\|VTH-zaak]] | Detailgegeven |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|BOA]] | detail | via VTH-Melding → [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/monument\|Monument]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|Combibon]] | detail | via VTH-Melding → [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|Fietsregistratie]] | detail | via VTH-Melding → [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|Grondslag]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|Indiener]] | detail | via Rechtspersoon → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeervergunning\|Parkeervergunning]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|Kosten]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/vth-zaak\|VTH-zaak]] | Detailgegeven |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|Leges_Grondslag]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/vth-zaak\|VTH-zaak]] | Detailgegeven |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|Ligplaatsontheffing]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/ontheffing\|Ontheffing]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|MORAanvraagOfMelding]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Detailgegeven |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|Precario]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|VOMAanvraagOfMelding]] | abstract | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Boventype VTHAanvraagOfMelding, WABOAanvraagOfMelding |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|VTH-Melding]] | abstract | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Boventype Combibon, Fietsregistratie, Waarneming |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|VTHAanvraagOfMelding]] | detail | via VOMAanvraagOfMelding → [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|Vordering]] | component | beschrijft [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/vth-zaak\|VTH-zaak]] | Component |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|WABOAanvraagOfMelding]] | detail | via VOMAanvraagOfMelding → [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Detailgegeven |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|Waarneming]] | detail | via VTH-Melding → [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|WoonfraudeAanvraagOfMelding]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Detailgegeven |
| [[Wiki/GGM/1-veiligheid-en-vergunningen/1-veiligheid-en-vergunningen\|WoonoverlastAanvraagOfMelding]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Detailgegeven (weinig attributen) |

## BO's zonder GGM-entiteit

BO's waarvoor geen overeenkomstige GGM-entiteit bestaat. Data-objecten worden als hiaat teruggemeld aan het GGM-team; overige BO's bestaan alleen in GEMMA.

| BO | Data-object | Grondslag | Status |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/evenementen/evenementenlocatie\|Evenementenlocatie]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/evenementen/evenementenvergunning\|Evenementenvergunning]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/handhavingsbesluit\|Handhavingsbesluit]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/register-omgevingsplan\|Register (omgevingsplan)]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/welstandsadvies\|Welstandsadvies]] | nee | procesobject | **Alleen GEMMA-BO** |
