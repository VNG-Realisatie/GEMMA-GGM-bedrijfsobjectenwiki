---
type: element
naam: Balieafspraak
domein:
- Dienstverlening
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Balieafspraak
ggm_guid: EAID_631FEEF1_88D3_4d18_ADB2_BF999068493E
ggm_uml_type: Class
ggm_beleidsdomein: 10 Dienstverlening
ggm_taakveld: 10 Dienstverlening
ggm_diagram:
- Afspraken en Klantcontacten
- Entiteiten Klantcontact
ggm_diagram_ids:
- EAID_282A4979_0BBC_4448_B71C_0CE64829083B
- EAID_5901286A_E9EF_4360_9CE6_32B6FDE1C970
ggm_definitie: Balieafspraken zijn afspraken voor een klantcontact. Dit ongeacht of deze werkelijk heeft plaatsgevonden of gaat plaatsvinden, soms liggen deze in de toekomst of is iemand niet op komen dagen,
  of iets anders waardoor het klantcontact nog niet heeft plaatsgevonden.
ggm_toelichting: Dit ongeacht of deze werkelijk heeft plaatsgevonden of gaat plaatsvinden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact nog
  niet heeft plaatsgevonden.
ggm_synoniemen: ''
ggm_herkomst: ''
ggm_gemma_naam: Balieafspraak
ggm_gemma_guid: 8fd2ff34-a208-4924-bec3-b5ee7e5e7a18
ggm_gemma_definitie: Balieafspraken zijn afspraken voor een klantcontact. Dit ongeacht of deze werkelijk heeft plaatsgevonden of gaat plaatsvinden, soms liggen deze in de toekomst of is iemand niet op komen
  dagen, of iets anders waardoor het klantcontact nog niet heeft plaats
ggm_gemma_toelichting: Dit ongeacht of deze werkelijk heeft plaatsgevonden of gaat plaatsvinden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact
  nog niet heeft plaatsgevonden.
ggm_gemma_synoniemen: ''
ggm_gemma_type: business-object
ggm_gemma_url: https://gemmaonline.nl/index.php/GEMMA/id-8fd2ff34-a208-4924-bec3-b5ee7e5e7a18
ggm_gemma_bron: ''
ggm_gemma_alternate_name: ''
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Balieafspraak** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Afspraakstatus** (detail) — Detailgegeven (geassocieerd met BO)
bo_definitie: "Balieafspraken zijn afspraken voor een klantcontact. Dit ongeacht of deze werkelijk heeft plaatsgevonden of gaat plaatsvinden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact nog niet heeft plaatsgevonden."
bo_toelichting: ''
bedrijfsprocessen:
- Afsprakenbeheer
- Klantcontactregistratie
- Balieplanning
bedrijfsfuncties:
- Dienstverlening
- Klantcontactcentrum
bo_relaties:
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/product-of-dienst|Product of dienst]]'
  richting: van-dit-BO
  kardinaliteit: 0..*
  beschrijving: betreft een product of dienst
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak|Zaak]]"
  richting: van-dit-BO
  kardinaliteit: 0..1
  beschrijving: heeft betrekking op een zaak
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding|Aanvraag of melding]]'
  richting: van-dit-BO
  kardinaliteit: 0..*
  beschrijving: kan uitmonden in een aanvraag of melding (via klantcontact)
---

## BO-criteria toetsing

| Criterium | Toepassing |
|---|---|
| Betekenis binnen domein | ✅ Centraal in fysieke dienstverlening aan de balie |
| Herkenbaar voor experts | ✅ Elke gemeente met een balie plant en registreert afspraken |
| Eigen bestaan | ✅ Bestaat onafhankelijk — een afspraak is er ook als de inwoner niet verschijnt |
| Meervoud | ✅ Honderden tot duizenden per maand per gemeente |
| Levenscyclus | ✅ Aangemaakt → gepland → uitgevoerd / no-show / geannuleerd |
| Relaties | ✅ Met medewerker, product/dienst, zaak, locatie, klantcontact |

Score: 6/6 — duidelijk een bedrijfsobject.

## Beschrijving

Een balieafspraak is een geplande of ongeplande afspraak voor een klantcontact aan de gemeentelijke balie. De afspraak wordt geregistreerd ongeacht of het contact daadwerkelijk plaatsvindt — ook no-shows en annuleringen zijn balieafspraken. Gemeenten gebruiken afspraaksystemen om wachttijden te beheersen en capaciteit te plannen.

In de context van overheidsbrede dienstverlening zijn balieafspraken het registratiepunt voor fysieke contacten met inwoners, inclusief contacten waarbij via professionallijnen wordt doorgeschakeld naar uitvoeringsorganisaties.

## GGM-bron

> "Balieafspraken zijn afspraken voor een klantcontact. Dit ongeacht of deze werkelijk heeft plaatsgevonden of gaat plaatsvinden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact nog niet heeft plaatsgevonden." (GGM definitie)

- **Entiteit:** Balieafspraak
- **Beleidsdomein:** Model Dienstverlening (taakveld 10)
- **Matchsterkte:** exact
- **Attributen:** starttijdGepland, tijdAangemaakt, toelichting, tijdsduurGepland, wachttijdTotaal, eindtijdGepland, wachttijdVoorStartAfspraak, wachttijdNaStartAfspraak, werkelijkeTijdsduur, notitie

## Relaties

| Gerelateerd BO | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/product-of-dienst\|product-of-dienst]] | → | 0..* | betreft | GGM: Balieafspraak → ProductOfDienst |
| zaakdossier | → | 0..1 | heeft betrekking op | GGM: Balieafspraak → Zaak |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|aanvraag-of-melding]] | → | 0..* | kan uitmonden in (via klantcontact) | GGM: Balieafspraak → Klantcontact → AanvraagOfMelding |

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
