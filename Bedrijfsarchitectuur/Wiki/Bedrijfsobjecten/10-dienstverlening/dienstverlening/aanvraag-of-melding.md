---
type: bedrijfsobject
naam: Aanvraag of melding
domein:
- Dienstverlening
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: AanvraagOfMelding
ggm_guid: EAID_8E6BAEF8_1878_400f_9244_23575BD41EAB
ggm_uml_type: Class
ggm_beleidsdomein: 10 Dienstverlening
ggm_taakveld: 10 Dienstverlening
ggm_diagram:
- Diagram Vergunningen en Meldingen
- Brede Handhaving
- Diagram Aanvragen
- Zaken en Besluiten
- Verkamering en Woonoverlast
- Diagram Beslissingen Leerplicht
- AanvraagOfMelding
- Zorgmelding
- Zorgmelding Detail
- Diagram Afval Meldingen
- MOR 2.0
- Entiteiten Dienstverlening
- Dienstverlening en Klanten
- Entiteiten Klantcontact
ggm_diagram_ids:
- EAID_BB52C835_0B2D_4164_AC9D_9D6EDBD7E267
- EAID_EC84A03C_FC04_401a_8263_7809B74179F8
- EAID_A2BA1F0D_8428_42fc_80D6_7184F243D268
- EAID_B039478A_DAF7_458f_A7C7_E4744EC08DBF
- EAID_26A453D9_47AF_487e_854B_3B4BC6D6A308
- EAID_5F3782EB_C416_461c_A9FA_40991A7F0165
- EAID_96845001_991F_4bd6_9249_FBE26A26AC4C
- EAID_7D74F8FB_7AF2_4fb6_B951_C78139A17FCF
- EAID_157F610A_619E_4d1a_BB45_5C1F55178944
- EAID_B3CC7874_57AA_4aeb_BF3F_98A64E9D76E5
- EAID_48B6C3F9_CCF1_4794_8252_FC6543409B78
- EAID_1D7802F4_3458_4bb4_8431_16C7F85473FC
- EAID_5901286A_E9EF_4360_9CE6_32B6FDE1C970
ggm_definitie: 'Komt overeen met een VJV

  Bron: GEM_VJV (Distinct op REQ_ID) ID: REQ_ID'
ggm_toelichting: ''
ggm_synoniemen: ''
ggm_herkomst: ''
ggm_gemma_naam: AanvraagOfMelding
ggm_gemma_guid: f14fa1cf-f2c7-4bd6-862d-28ff1616a882
ggm_gemma_definitie: 'Komt overeen met een VJV

  Bron: GEM_VJV (Distinct op REQ_ID) ID: REQ_ID'
ggm_gemma_toelichting: ''
ggm_gemma_synoniemen: ''
ggm_gemma_type: business-object
ggm_gemma_url: https://gemmaonline.nl/index.php/GEMMA/id-f14fa1cf-f2c7-4bd6-862d-28ff1616a882
ggm_gemma_bron: ''
ggm_gemma_alternate_name: AanvraagOfMelding (Dienstverlening)

ggm_duplicaat_entiteiten:
  - "EAID_66E2B5BA_44A0_4fde_AE33_E211EE4832C2"

analyse_ggm_dekking: |
  Dit BO is de hernoeming van GGM-entiteit **AanvraagOfMelding**. Daarnaast is **AanvraagOfMelding** (beleidsdomein Leerplicht en Leerlingenvervoer) als vermoedelijk duplicaat gekoppeld — zie ggm_duplicaat_entiteiten. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **AOMStatus** (detail) — Detailgegeven (geassocieerd met BO)
  - **AanvraagVrijstelling** (detail) — Subtype AanvraagOfMelding; te granulair
  - **Aanvraagdata** (detail) — Detailgegeven (geassocieerd met BO)
  - **BOA** (detail) — Detailgegeven (weinig attributen)
  - **Combibon** (detail) — Detailgegeven (weinig attributen)
  - **Fietsregistratie** (detail) — Detailgegeven (weinig attributen)
  - **Formuliersoort** (classificatie) — Typering/referentietabel
  - **Formuliersoortveld** (detail) — Detailgegeven
  - **Indiener** (detail) — Detailgegeven (geassocieerd met BO)
  - **MOR-AanvraagOfMelding** (detail) — Detailgegeven (weinig attributen)
  - **MORAanvraagOfMelding** (detail) — Detailgegeven
  - **Onderwerp** (detail) — Detailgegeven (geassocieerd met BO)
  - **VOMAanvraagOfMelding** (detail) — Detailgegeven
  - **VTH-Melding** (detail) — Detailgegeven
  - **VTHAanvraagOfMelding** (detail) — Detailgegeven (weinig attributen)
  - **Verlofaanvraag** (detail) — Subtype AanvraagOfMelding; te granulair
  - **WABOAanvraagOfMelding** (detail) — Detailgegeven
  - **Waarneming** (detail) — Detailgegeven (weinig attributen)
  - **WoonfraudeAanvraagOfMelding** (detail) — Detailgegeven
  - **WoonoverlastAanvraagOfMelding** (detail) — Detailgegeven (weinig attributen)
bo_definitie: "Komt overeen met een VJV Bron: GEM_VJV (Distinct op REQ_ID) ID: REQ_ID"
bo_toelichting: ''
bedrijfsprocessen:
- Zaakafhandeling
- Klantcontactregistratie
- Meldingenbeheer
bedrijfsfuncties:
- Dienstverlening
- Klantcontactcentrum
bo_relaties:
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak|Zaak]]"
  richting: van-dit-BO
  kardinaliteit: 0..*
  beschrijving: kan leiden tot een zaak
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document|Document]]"
  richting: van-dit-BO
  kardinaliteit: 0..*
  beschrijving: heeft documenten
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/product-of-dienst|Product of dienst]]'
  richting: naar-dit-BO
  kardinaliteit: 0..*
  beschrijving: betreft (via klantcontact)
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/balieafspraak|Balieafspraak]]'
  richting: naar-dit-BO
  kardinaliteit: 0..*
  beschrijving: kan ontstaan uit klantcontact na balieafspraak
---

## BO-criteria toetsing

| Criterium | Toepassing |
|---|---|
| Betekenis binnen domein | ✅ Kernobject van alle gemeentelijke dienstverlening |
| Herkenbaar voor experts | ✅ Elke gemeente registreert aanvragen en meldingen |
| Eigen bestaan | ✅ Bestaat onafhankelijk van de zaak die eruit kan volgen |
| Meervoud | ✅ Duizenden per gemeente per jaar |
| Levenscyclus | ✅ Ingediend → in behandeling → afgehandeld |
| Relaties | ✅ Met zaak, document, indiener, onderwerp, formulier |

Score: 6/6 — duidelijk een bedrijfsobject.

## Beschrijving

De aanvraag of melding is het startpunt van gemeentelijke dienstverlening. Inwoners, ondernemers of organisaties dienen een verzoek in (aanvraag) of signaleren een situatie (melding). Dit kan via alle kanalen: balie, telefoon, e-mail, webformulier, app. De gemeente registreert elke aanvraag of melding en bepaalt of er een zaak van wordt gemaakt.

In de praktijk onderscheiden gemeenten aanvragen (gericht op een product of dienst) en meldingen (signalering van een situatie, bijv. een kapotte lantaarnpaal of overlast). Het GGM modelleert beide als één abstracte hiërarchie met domeinspecifieke specialisaties.

## GGM-bron

> "Komt overeen met een VJV" (GGM definitie, Model Dienstverlening)

- **Entiteit:** AanvraagOfMelding
- **Beleidsdomein:** Model Dienstverlening (taakveld 10)
- **Matchsterkte:** sterk
- **Attributen:** afgehandeld, kanaal, soort, datumAfhandeling, categorie, identificatie, onderwerp, status, subcategorie, datumAanmaak

### Generalisatiekeuze

Het GGM kent 11 specialisaties van AanvraagOfMelding, verspreid over meerdere domeinen:

- **MOR-AanvraagOfMelding** (Dienstverlening) — melding openbare ruimte
- **AOMMeldingWmoJeugd**, **AOM_AanvraagWmoJeugd** — sociaal domein
- **VTH-Melding** — vergunningen, toezicht en handhaving
- **WoonfraudeAanvraagOfMelding**, **WoonoverlastAanvraagOfMelding** — wonen
- **VOMAanvraagOfMelding** — omgevingswet
- **Zorgmelding** — zorg en veiligheid

**Beslissing:** het BO wordt gedefinieerd op het **generieke niveau** (AanvraagOfMelding). De specialisaties horen inhoudelijk bij hun eigen domein en worden daar beoordeeld als dat domein wordt verwerkt. Op bedrijfsniveau is "aanvraag of melding" het herkenbare concept; de specialisaties zijn varianten in het registratiesysteem.

## Subtypes

Herkende specialisaties van Aanvraag of melding. Gevonden in bronnen en/of GGM. Geen apart BO.

- **VTHAanvraagOfMelding** — aanvraag of melding voor vergunning, toezicht of handhaving in de fysieke leefomgeving
- **WABOAanvraagOfMelding** — aanvraag of melding in het kader van de Wet algemene bepalingen omgevingsrecht
- **VTH-Melding** — signaalmelding met betrekking tot vergunningen, toezicht en handhaving
- **Bouwmelding (Wkb)** — melding vier weken vóór bouwstart onder de Wet kwaliteitsborging, met risicobeoordeling door kwaliteitsborger
- **Handhavingsverzoek** — verzoek van burger of bedrijf aan de gemeente om handhavend op te treden bij een vermoedelijke overtreding; moet altijd worden behandeld
- **MORAanvraagOfMelding** — melding openbare ruimte
- **WoonfraudeAanvraagOfMelding** — melding of aanvraag van woonfraude
- **WoonoverlastAanvraagOfMelding** — melding of aanvraag met betrekking tot woonoverlast

## Relaties

| Gerelateerd BO | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| zaakdossier | → | 0..* | kan leiden tot een zaak | GGM: AanvraagOfMelding → Zaak |
| informatieobject | → | 0..* | heeft documenten | GGM: AanvraagOfMelding → Document |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/product-of-dienst\|product-of-dienst]] | ← | 0..* | betreft (indirect via klantcontact) | GGM: Klantcontact → ProductOfDienst |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/balieafspraak\|balieafspraak]] | ← | 0..* | kan ontstaan uit klantcontact na afspraak | GGM: Klantcontact → AanvraagOfMelding |


## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/rgbz-informatiemodel]]
- [[Wiki/Bronsamenvattingen/Standaarden/ztc2-informatiemodel]]
- [[Wiki/Bronsamenvattingen/Dienstverlening/raadgever-inkoop-en-aanbesteden]]
- [[Wiki/Bronsamenvattingen/Dienstverlening/hand-out-overheidsbrede-dienstverlening]]
- [[Wiki/Bronsamenvattingen/Dienstverlening/overheidsbrede-startscan]]
- [[Wiki/Bronsamenvattingen/Dienstverlening/rubriek-dienstverlening]]
- [[Wiki/Bronsamenvattingen/Dienstverlening/online-dienstverlening]]
- [[Wiki/Bronsamenvattingen/Dienstverlening/digitale-toegankelijkheid]]
- [[Wiki/Bronsamenvattingen/Dienstverlening/inkoop-en-aanbesteden]]
- [[Wiki/Bronsamenvattingen/Omgevingswet/uitvoeringsbeleid-vth-delft]]

## Terugmelding GGM

De definitie "Komt overeen met een VJV" is een systeemreferentie, geen inhoudelijke definitie. Suggestie: vervang door een beschrijvende definitie op bedrijfsniveau.
