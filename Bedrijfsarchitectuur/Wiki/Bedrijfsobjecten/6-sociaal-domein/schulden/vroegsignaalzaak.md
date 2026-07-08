---
type: bedrijfsobject
naam: Vroegsignaalzaak
onderwerp: [schulden en armoede]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Vroegsignaalzaak
ggm_guid: EAID_1AA67F0D_3B94_48a3_A037_A2ACC6D61CF0
ggm_uml_type: Class
ggm_beleidsdomein: Vroegsignalering
ggm_taakveld: "Schulden"
ggm_diagram: [Vroegsignalering, Vroegsignalering Details, Vroegsignalering Klein]
ggm_definitie: "Een Vroegsignaalzaak is procesmatige eenheid binnen de gemeentelijke organisatie waarin de behandeling van één of meerdere vroegsignalen is ondergebracht."
ggm_herkomst: GGM

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Vroegsignaalzaak** als directe tegenhanger.
bo_definitie: "Een Vroegsignaalzaak is procesmatige eenheid binnen de gemeentelijke organisatie waarin de behandeling van één of meerdere vroegsignalen is ondergebracht."
bo_toelichting: ''
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[vroegsignaal]]"
    richting: naar-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Zaak bevat een of meer vroegsignalen"
  - type: associatie
    bedrijfsobject: "[[contactpoging]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Zaak heeft contactpogingen"
bedrijfsprocessen: [vroegsignalering]
bedrijfsfuncties: [financiële hulpverlening]
---

## BO-criteria toetsing

6/6 criteria. Procesmatige eenheid (specialisatie van Zaak in GGM) met eigen resultaat, data en contactpogingen. Eigen levenscyclus (aangemaakt bij signaal → contactpogingen → afgesloten met resultaat).

## Beschrijving

Een vroegsignaalzaak bundelt één of meer vroegsignalen van dezelfde inwoner en bevat alle handelingen die de gemeente verricht: beoordeling, contactpogingen (telefoon, huisbezoek, brief, digitaal), en eventuele toeleiding naar schuldhulpverlening.

## GGM-componenten

GGM-entiteiten die onderdeel zijn van de vroegsignaalzaak. Gemodelleerd als aparte entiteiten voor DDAS-rapportage maar vormen geen zelfstandig bedrijfsobject.

- **AanleverendeOrganisatie** — organisatie die data aanlevert aan het CBS (gemeente of gemandateerde partij). Naam, KvK-nummer.

## GGM-bron

> "Een Vroegsignaalzaak is procesmatige eenheid binnen de gemeentelijke organisatie waarin de behandeling van één of meerdere vroegsignalen is ondergebracht."

- **Entiteit:** Vroegsignaalzaak (specialisatie van Zaak)
- **Beleidsdomein:** Vroegsignalering (taakveld Schulden)
- **Attributen:** resultaat, matchingsdatum, startdatum_matchingperiode, datum_opgepakt, einddatum_matchingperiode
- **Matchsterkte:** exact

## Relaties

| Type | Bedrijfsobject | Kardinaliteit | Beschrijving |
|---|---|---|---|
| associatie | [[vroegsignaal\|Vroegsignaal]] | 1..* | Bundelt signalen |
| associatie | [[contactpoging\|Contactpoging]] | 0..* | Heeft contactpogingen |

## Bronnen
- [[Wiki/Bronsamenvattingen/Schulden en Armoede/beleidsplan-schuldhulpverlening-den-haag-2024-2028]]
- [[Wiki/Bronsamenvattingen/Schulden en Armoede/vroegsignaleringsaanpak-gemeenten-divosa-2024]]
