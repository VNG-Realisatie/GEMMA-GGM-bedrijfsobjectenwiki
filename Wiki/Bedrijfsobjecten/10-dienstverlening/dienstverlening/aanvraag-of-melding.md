---
type: bedrijfsobject
naam: Aanvraag of melding
domein: [Dienstverlening]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: AanvraagOfMelding
ggm_guid: "EAID_8E6BAEF8_1878_400f_9244_23575BD41EAB"
ggm_uml_type: Class
ggm_beleidsdomein: "10 Dienstverlening"
ggm_taakveld: "10 Dienstverlening"
ggm_diagram: ["Entiteiten Dienstverlening", "Dienstverlening en Klanten", "Entiteiten Klantcontact", "Diagram Aanvragen, Zaken en Besluiten", "AanvraagOfMelding"]
ggm_diagram_ids: ["EAID_48B6C3F9_CCF1_4794_8252_FC6543409B78", "EAID_1D7802F4_3458_4bb4_8431_16C7F85473FC", "EAID_5901286A_E9EF_4360_9CE6_32B6FDE1C970", "EAID_A2BA1F0D_8428_42fc_80D6_7184F243D268", "EAID_5F3782EB_C416_461c_A9FA_40991A7F0165"]
ggm_definitie: "Komt overeen met een VJV"
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: "GGM"

ggm_gemma_naam: AanvraagOfMelding
ggm_gemma_guid: "f14fa1cf-f2c7-4bd6-862d-28ff1616a882"
ggm_gemma_definitie: "Komt overeen met een VJV"
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: business-object
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-f14fa1cf-f2c7-4bd6-862d-28ff1616a882"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: "AanvraagOfMelding (Dienstverlening)"

gemma_definitie: "Verzoek of signaal van een inwoner, ondernemer of organisatie aan de gemeente, gericht op het verkrijgen van een dienst, product of het melden van een situatie."
bronnen:
  - "[[Wiki/Bronsamenvattingen/Dienstverlening/hand-out-overheidsbrede-dienstverlening]]"
  - "[[Wiki/Bronsamenvattingen/Dienstverlening/rubriek-dienstverlening]]"
  - "[[Wiki/Bronsamenvattingen/Standaarden/rgbz-informatiemodel]]"
relaties:
  - type: associatie
    bedrijfsobject: "[[zaakdossier]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "kan leiden tot een zaak"
  - type: associatie
    bedrijfsobject: "[[informatieobject]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "heeft documenten"
  - type: associatie
    bedrijfsobject: "[[product-of-dienst]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "betreft (via klantcontact)"
  - type: associatie
    bedrijfsobject: "[[balieafspraak]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "kan ontstaan uit klantcontact na balieafspraak"
bedrijfsprocessen: [Zaakafhandeling, Klantcontactregistratie, Meldingenbeheer]
bedrijfsfuncties: [Dienstverlening, Klantcontactcentrum]
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

## BO-definitie

De GGM-definitie ("Komt overeen met een VJV") is een technische referentie naar het bronsysteem (VJV = Vraag, Ja/Nee, Verzoek), niet een bedrijfsdefinitie. De GEMMA-definitie is daarom afwijkend en beschrijvend geformuleerd:

> **Verzoek of signaal van een inwoner, ondernemer of organisatie aan de gemeente, gericht op het verkrijgen van een dienst, product of het melden van een situatie.**

## Relaties

| Gerelateerd BO | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[zaakdossier]] | → | 0..* | kan leiden tot een zaak | GGM: AanvraagOfMelding → Zaak |
| [[informatieobject]] | → | 0..* | heeft documenten | GGM: AanvraagOfMelding → Document |
| [[product-of-dienst]] | ← | 0..* | betreft (indirect via klantcontact) | GGM: Klantcontact → ProductOfDienst |
| [[balieafspraak]] | ← | 0..* | kan ontstaan uit klantcontact na afspraak | GGM: Klantcontact → AanvraagOfMelding |

## Terugmelding GGM

De definitie "Komt overeen met een VJV" is een systeemreferentie, geen inhoudelijke definitie. Suggestie: vervang door een beschrijvende definitie op bedrijfsniveau.
