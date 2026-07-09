---
type: element
naam: Inkomensvoorziening
onderwerp: [werk en inkomen]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Inkomensvoorziening
ggm_guid: EAID_07784236_3AA6_45e5_8253_7D088C4020B0
ggm_uml_type: Class
ggm_beleidsdomein: Model Inkomen
ggm_taakveld: Inkomen
ggm_diagram: [Diagram Basismodel Inkomen, In- en uitstroom inkomensvoorziening]
ggm_diagram_ids: [EAID_9CEE3C86_9B9F_472f_A104_61FFC01DAC5A, EAID_390FED22_863F_46c6_8DAF_DBFEABC77AA8]
ggm_definitie: "Een regeling die zorg draag voor een inkomen confom de landelijke wetgeving"
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst: GGM

ggm_gemma_naam:
ggm_gemma_guid: "id-07784236-3aa6-45e5-8253-7d088c4020b0"
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type:
ggm_gemma_url:
ggm_gemma_bron:
ggm_gemma_alternate_name:

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Inkomensvoorziening** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Component** (detail) — Detailgegeven
  - **ComponentSoort** (classificatie) — Typering/referentietabel
  - **Huisvestingsoort** (classificatie) — Typering/referentietabel
  - **Inkomensvoorzieningsoort** (detail) — Detailgegeven (geassocieerd met BO)
  - **RedenBlokkering** (classificatie) — Typering/referentietabel
  - **RedenInstroom** (classificatie) — Typering/referentietabel
  - **RedenUitstroom** (classificatie) — Typering/referentietabel
  - **UitkeringsRun** (detail) — Detailgegeven (weinig attributen)
bo_definitie: "Een aan een inwoner toegekende financiële regeling die voorziet in inkomen of noodzakelijke kosten, zowel structureel (bijstandsuitkering, individuele inkomenstoeslag) als tijdelijk (energietoeslag, TONK)."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Client]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Client heeft inkomensvoorziening"
  - type: associatie
    bedrijfsobject: "[[Beschikking]]"
    richting: naar-dit-BO
    kardinaliteit: "1..1"
    beschrijving: "Beschikking kent inkomensvoorziening toe"
bedrijfsprocessen: [bijzondere bijstandsverlening, uitkeringsadministratie, draagkrachtbeoordeling]
bedrijfsfuncties: [inkomensondersteuning, minimabeleid]
---

## BO-criteria toetsing

| Criterium | Toets |
|---|---|
| Identificeerbaar | ✅ Unieke toekenning per persoon met ingangsdatum, einddatum en bedrag |
| Levenscyclus | ✅ Aanvraag → beoordeling → beschikking → toekenning → beëindiging |
| Eigendom/verantwoordelijkheid | ✅ Gemeente is verantwoordelijk voor toekenning en administratie |
| Bestuurlijk relevant | ✅ €615M landelijk (2021); ~7% van inkomensregelingen, ~67% van minimabeleid |
| Relaties | ✅ Met Client, Beschikking, Inkomensvoorzieningsoort, Component |
| Persistent | ✅ Geregistreerd in BUS (Bijstandsuitkeringenstatistiek), CBS-rapportages |

## Beschrijving

Een inkomensvoorziening is een door de gemeente toegekende financiële regeling aan een inwoner die onvoldoende middelen heeft om in de noodzakelijke kosten van bestaan te voorzien. De voorziening wordt verstrekt als gift, geldlening of in natura, en kan eenmalig of periodiek zijn.

De gemeente beoordeelt het recht op basis van draagkracht, voorliggende voorzieningen en bijzondere omstandigheden. De uitvoering is geregeld in de Participatiewet (artikelen 35, 36, 36b) en aanvullende regelgeving.

Het Rijk legt regelmatig tijdelijke inkomensregelingen bij gemeenten neer (TONK voor covid, energietoeslag voor energiecrisis). Deze worden via dezelfde administratieve processen afgehandeld en onder bestaande clusters geboekt, maar hebben doorgaans afwijkende voorwaarden (bijv. geen vermogenstoets bij energietoeslag).

In 2021 bedroegen de landelijke uitgaven aan bijzondere bijstand €615 miljoen, een stijging van 57% ten opzichte van 2010. De grootste kostenpost is beschermingsbewind (~1/3 van de uitgaven).

## Subtypes

Herkende specialisaties van Inkomensvoorziening. Gevonden in bronnen en/of GGM. Geen apart BO.

- **Bijstandsuitkering** — periodieke uitkering voor levensonderhoud (Participatiewet, algemene bijstand)
- **Bijzondere bijstand** — eenmalige of periodieke verstrekking voor kosten uit bijzondere omstandigheden (art. 35 Pw); individueel of categoriaal
- **Individuele inkomenstoeslag** — jaarlijkse toeslag bij langdurig minimuminkomen zonder perspectief op verbetering (art. 36 Pw; vervangt langdurigheidstoeslag sinds 2015)
- **Studietoeslag** — toeslag voor studenten met beperking (art. 36b Pw; sinds 1-4-2022 zelfstandige uitkering)
- **Energietoeslag** — categoriale bijzondere bijstand voor gestegen energiekosten (2022-2023); ~90% bereik door eenvoudig aanvraagproces en geen vermogenstoets
- **TONK** — Tijdelijke Ondersteuning Noodzakelijke Kosten (covid, Q1-Q3 2021); geboekt op cluster 'voorzieningen voor wonen'
- **Collectieve aanvullende zorgverzekering** — categoriale bijstand in de vorm van premiesubsidie voor aanvullende zorgverzekering (gemeentepolis)
- **IOAW-uitkering** — Wet inkomensvoorziening oudere en gedeeltelijk arbeidsongeschikte werkloze werknemers
- **IOAZ-uitkering** — Wet inkomensvoorziening oudere en gedeeltelijk arbeidsongeschikte gewezen zelfstandigen
- **Bbz** — Besluit bijstandverlening zelfstandigen

## GGM-bron

> "Een regeling die zorg draag voor een inkomen confom de landelijke wetgeving"
> — GGM, entiteit *Inkomensvoorziening*, beleidsdomein Model Inkomen

**Matchsterkte:** exact — de GGM-entiteit beschrijft precies het concept van een toegekende inkomensregeling.

**Attributen (GGM):** ingangsdatum, einddatum, toekenningsdatum, bedrag, eenmalig, groep, administratieveEinddatum, administratieveStartdatum, betalingsmomentcode, code, datumToekenning, indicatieBlokkering, indicatieStudietoeslag, indicatieUitkeringSplitsen, indicatieUitkeringsspecificatie, verstrekkingsvorm, verwerktTotEnMetDatum

## BO-definitie

De GGM-definitie wijkt inhoudelijk af van het gemeentelijke gebruik van dit begrip. De BO-definitie is gebaseerd op de bronnen.

## Relaties

| Gerelateerd BO | Relatie | Richting | Bron |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | heeft voorziening | Client → Inkomensvoorziening | GGM |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | resulteert in | Beschikking → Inkomensvoorziening | Bron + GGM (Diensten) |

## Bedrijfsprocessen

- **Bijzondere bijstandsverlening**: aanvraag → draagkrachtbeoordeling → beschikking → verstrekking → clusterboeking
- **Uitkeringsadministratie**: periodieke betalingen, beëindiging, blokkering
- **Minimabeleid**: beleidsvorming, budgettering, verantwoording (CBS, Divosa Benchmark)

## Bedrijfsfuncties

- Inkomensondersteuning
- Minimabeleid
- Financiële administratie

## Bronnen

- [[Wiki/Bronsamenvattingen/Werk en Inkomen/factsheet-bijzondere-bijstand]]
- [[Wiki/Bronsamenvattingen/Werk en Inkomen/handreiking-explicitering-budgetten-participatiewet-wsw]]

## Terugmelding GGM

De GGM-definitie ("zorg draag voor een inkomen confom de landelijke wetgeving") bevat twee typefouten ("draag" → "draagt", "confom" → "conform") en is te beperkt: bijzondere bijstand voorziet niet in inkomen maar in bijzondere kosten. Voorgestelde correctie: "Een aan een inwoner toegekende financiële regeling op grond van de Participatiewet of aanvullende wetgeving, die voorziet in inkomen of noodzakelijke kosten van bestaan."
