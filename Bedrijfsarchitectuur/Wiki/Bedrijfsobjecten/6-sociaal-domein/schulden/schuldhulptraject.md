---
type: bedrijfsobject
naam: Schuldhulptraject
onderwerp: [schulden en armoede]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Schuldhulptraject
ggm_guid: EAID_839017B2_0F95_42d0_AB2B_E873636340DA
ggm_uml_type: Class
ggm_beleidsdomein: Schuldhulpverlening
ggm_taakveld: "Schulden"
ggm_diagram: [Schuldhulp Hoofdlijnen, Schuldhulp Client, Schuldhulp Schuldhulporganisatie, Schuldhulpproces]
ggm_definitie: "Samenstel van achtereenvolgens uit te voeren en onderling samenhangende deelhandelingen of van opeenvolgende stadia in een proces, voorgesteld als een route die via opeenvolgende bestemmingen naar de eindbestemming voert."
ggm_herkomst: GGM

ggm_gemma_naam: ""
ggm_gemma_guid: "id-839017b2-0f95-42d0-ab2b-e873636340da"
ggm_gemma_definitie: ""
ggm_gemma_type: ""

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Schuldhulptraject** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Aanmelding** (detail) — Procesfase van Schuldhulptraject
  - **Begeleiding** (detail) — Detailgegeven (geassocieerd met BO)
  - **Begeleidingssoort** (classificatie) — Typering/referentietabel
  - **Crisisinterventie** (detail) — Procesfase van Schuldhulptraject
  - **InformatieEnAdvies** (detail) — Detailgegeven (geassocieerd met BO)
  - **Intake** (detail) — Procesfase van Schuldhulptraject
  - **Nazorg** (detail) — Procesfase van Schuldhulptraject
  - **Oplossing** (detail) — Onderdeel van Schuldhulptraject, 1:1 met traject
  - **Oplossingssoort** (classificatie) — Typering/referentietabel
  - **PlanVanAanpak** (detail) — Detailgegeven (geassocieerd met BO)
  - **Schuldhulporganisatie** (detail) — Detailgegeven (geassocieerd met BO)
  - **Stabilisatie** (detail) — Procesfase van Schuldhulptraject
  - **Uitstroom** (detail) — Detailgegeven (geassocieerd met BO)
  - **VoorlopigeVoorziening** (detail) — Detailgegeven (geassocieerd met BO)
bo_definitie: "Samenstel van achtereenvolgens uit te voeren en onderling samenhangende deelhandelingen of van opeenvolgende stadia in een proces, voorgesteld als een route die via opeenvolgende bestemmingen naar de eindbestemming voert."
bo_toelichting: ''
bo_subtypes: []
bo_relaties:
  - type: compositie
    bedrijfsobject: "[[schuld]]"
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Traject bevat een of meer schulden"
  - type: associatie
    bedrijfsobject: "[[schuldregeling]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Traject kan leiden tot een schuldregeling"
  - type: associatie
    bedrijfsobject: "[[moratorium]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Traject kan moratorium(s) bevatten"
  - type: associatie
    bedrijfsobject: "[[wsnp-traject]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Bij falen minnelijk traject doorverwijzing naar WSNP"
  - type: associatie
    bedrijfsobject: "[[client]]"
    richting: naar-dit-BO
    kardinaliteit: "1..2"
    beschrijving: "Traject voor één of twee cliënten"
bedrijfsprocessen: [schuldhulpverlening, vroegsignalering]
bedrijfsfuncties: [financiële hulpverlening]
---

## BO-criteria toetsing

6/6 criteria:
1. **Betekenis** — centraal concept in schuldhulpverlening, wettelijk verankerd in Wgs
2. **Herkenbaar** — elke schuldhulpverlener kent het traject als eenheid
3. **Eigen bestaan** — bestaat onafhankelijk van individuele fasen
4. **Meervoud** — duizenden trajecten per jaar (Den Haag: ~2.800 instroom)
5. **Levenscyclus** — aanmelding → intake → stabilisatie → schuldregeling → nazorg → uitstroom
6. **Relaties** — met Schuld, Schuldregeling, Cliënt, Schuldeiser, Moratorium

## Beschrijving

Het schuldhulptraject is het centrale procesverloop dat een inwoner met problematische schulden doorloopt. Het traject begint bij de aanmelding (via Helpdesk Geldzaken, vroegsignalering of eigen initiatief) en doorloopt achtereenvolgens intake, stabilisatie, schuldregeling en nazorg. De wettelijke grondslag is de Wet gemeentelijke schuldhulpverlening (Wgs, 2012/2021).

Een traject heeft een totaalschuldbedrag bij aanvang, een toekenningsdatum en een start/einddatum. Het streefresultaat is dat de inwoner na maximaal 18 maanden schuldregeling en 6 maanden nazorg schuldenvrij is.

## GGM-componenten

GGM-entiteiten die onderdeel zijn van het schuldhulptraject. In het GGM gemodelleerd als aparte entiteiten (voor DDAS-rapportage aan het CBS) maar vormen geen zelfstandig bedrijfsobject — het zijn procesfasen binnen het traject.

- **Aanmelding** — startmoment, kan persoonlijk, schriftelijk, digitaal of telefonisch. Bevat vlag crisisinterventie.
- **Intake** — fase tussen eerste gesprek en plan van aanpak. Inventarisatie instrumenten en gegevens.
- **Stabilisatie** — inkomsten en uitgaven in evenwicht brengen; schuldenrust bieden.
- **Nazorg** — ondersteuning na afronding traject, minimaal 6 maanden. Doel: recidivepreventie.
- **Uitstroom** — beëindiging van het traject. Vastlegging reden en datum beëindigingsbeschikking.
- **Crisisinterventie** — afwending acute situatie (huisuitzetting, afsluiting energie/water, opzegging zorgverzekering).
- **InformatieEnAdvies** — activiteiten gericht op zelfstandig financieel evenwicht zonder verdere dienstverlening.
- **PlanVanAanpak** — document met hulpvraag, voorgestelde ondersteuning, voorwaarden en beslagvrije voet.
- **VoorlopigeVoorziening** — tijdelijke beschermingsregeling (betalingsregelingen, uitstel, budgetbeheer) tot start schuldregeling.
- **Begeleiding** — doorlopende ondersteuning tijdens het traject, met soort (budgetcoaching, beschermingsbewind, etc.).
- **Oplossing** — resultaat van de schuldregeling: saneringskrediet, schuldbemiddeling, herfinanciering of 0-aanbod. Met vrij te laten bedrag (vtlb).
- **Schuldhulporganisatie** — gemeente of gemandateerde organisatie die het traject uitvoert.

## GGM-bron

> "Samenstel van achtereenvolgens uit te voeren en onderling samenhangende deelhandelingen of van opeenvolgende stadia in een proces, voorgesteld als een route die via opeenvolgende bestemmingen naar de eindbestemming voert."

- **Entiteit:** Schuldhulptraject
- **Beleidsdomein:** Schuldhulpverlening (taakveld Schulden, 6 Sociaal Domein)
- **Attributen:** omschrijving, startdatum, einddatum, toekenningsdatum, totaalSchuldbedragBijAanvangSchuld
- **Matchsterkte:** exact

## Relaties

| Type | Bedrijfsobject | Kardinaliteit | Beschrijving |
|---|---|---|---|
| compositie | [[schuld]] | 1..* | Traject bevat schulden |
| associatie | [[schuldregeling]] | 0..1 | Kan leiden tot schuldregeling |
| associatie | [[moratorium]] | 0..* | Kan moratorium(s) bevatten |
| associatie | [[wsnp-traject]] | 0..1 | Doorverwijzing bij falen minnelijk traject |
| associatie | [[client\|Cliënt]] | 1..2 | Voor één of twee cliënten |
| associatie | [[schuldeiser]] | 0..* | Via schulden gerelateerd aan schuldeisers |

## Bronnen
- [[Wiki/Bronsamenvattingen/Schulden en Armoede/beleidsplan-schuldhulpverlening-den-haag-2024-2028]]
- [[Wiki/Bronsamenvattingen/Schulden en Armoede/vng-schulden-en-armoede]]
