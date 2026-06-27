---
type: bedrijfsobject
naam: Toepasbare Regel
onderwerp: [Omgevingswet]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Toepasbare Regel
ggm_guid: EAID_10C06EB3_F94A_4005_9C66_0DAE61B96192
ggm_uml_type: Class
ggm_beleidsdomein: Omgevingswet
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram:
  - "Omgevingswet Toepasbare Regels"
  - "Omgevingswet Verzoek Activiteit op Locatie"
ggm_diagram_ids:
  - EAID_B9209AD2_0648_4482_BB24_135F27C2FECC
  - EAID_30B09C29_F649_4248_97FC_35A5F9331BBF
ggm_definitie: "Vanwege de leesbaarheid wordt gewerkt met de term Toepasbare regel ipv regelbeheersobject. Een regelbeheerobject heeft een koppeling met een samenhangende set met regels om een afleiding te kunnen doen."
ggm_toelichting: ""
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam:
ggm_gemma_guid:
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type:
ggm_gemma_url:
ggm_gemma_bron:
ggm_gemma_alternate_name:

ggm_duplicaat_entiteiten: []

bo_definitie: "Vertaling van juridische regels naar interactieve vragenbomen waarmee burgers en bedrijven in het DSO kunnen bepalen of zij een vergunning nodig hebben, een melding moeten doen of aan maatregelen moeten voldoen."
bo_toelichting: "De gemeente maakt toepasbare regels aan om haar juridische regels uit het omgevingsplan toegankelijk te maken voor initiatiefnemers via het Omgevingsloket. Elke toepasbare regel is gekoppeld aan een activiteit en een of meer juridische regels."
bo_subtypes: []
bo_synoniemen:
  - naam: Regelbeheerobject
    context: "Technische naam in CIM-OW/STTR"
bo_homoniemen: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Activiteit]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Toepasbare regel betreft activiteit"
  - type: associatie
    bedrijfsobject: "[[Juridische Regel]]"
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Toepasbare regel komt voort uit juridische regel"
bedrijfsprocessen:
  - "Omgevingsplanvorming"
  - "Digitale dienstverlening"
bedrijfsfuncties:
  - "Ruimtelijke ordening"
  - "Dienstverlening"
---

# Toepasbare Regel

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Identiteit | ✅ | Eigen NEN3610-achtige identificatie, naam, omschrijving, domein |
| Levenscyclus | ✅ | Begin- en eindegeldigheid, gekoppeld aan juridische regels |
| Eigenaarschap | ✅ | Gemeente maakt en beheert toepasbare regels voor het omgevingsplan |
| Relaties | ✅ | Gekoppeld aan activiteit(en) en juridische regel(s), bevat uitvoeringsregels |
| Meervoud | ✅ | Tientallen per omgevingsplan (per activiteit een of meer) |
| Registratie | ✅ | Aangeleverd als ToepasbareRegelBestand aan het DSO |

## Beschrijving

Een Toepasbare Regel vertaalt juridische regels uit het omgevingsplan naar interactieve vragenbomen waarmee burgers en bedrijven via het Omgevingsloket (DSO) kunnen bepalen wat zij mogen, moeten of nodig hebben. Het beantwoordt vragen als: "Heb ik een vergunning nodig voor het verbouwen van mijn kozijn?" of "Wat moet ik aanleveren bij een melding voor lozing?"

De gemeente maakt toepasbare regels aan per activiteit. Elk bevat uitvoeringsregels die bepalen hoe de benodigde informatie wordt uitgevraagd (via vragen aan de initiatiefnemer of bevraging van een registratie).

Er zijn drie subtypes die verschillende conclusies opleveren:
- **Conclusie** — antwoord op de vraag of een vergunning of melding nodig is
- **Indieningsvereisten** — welke gegevens/bijlagen bij een aanvraag of melding moeten worden aangeleverd
- **Maatregelen** — welke handelingen moeten worden uitgevoerd om aan voorschriften te voldoen

## Subtypes

Herkende specialisaties van Toepasbare Regel. Gevonden in GGM. Geen apart BO.

- **Conclusie** — antwoord op de check: wel of geen vergunning/melding nodig
- **Indieningsvereisten** — set informatie die bij een aanvraag/melding moet worden aangeleverd
- **Maatregelen** — handelingen die iemand moet uitvoeren om aan voorschriften te voldoen

## GGM-componenten

GGM-entiteiten die onderdeel zijn van Toepasbare Regel. Geen zelfstandig bedrijfsobject.

- **ToepasbareRegelBestand** — bestand met aangeleverde toepasbare regels; attributen: datumStart, datumEindeGeldigheid
- **Uitvoeringsregel** — bepaalt hoe de benodigde informatie wordt uitgevraagd; attributen: naam, omschrijving, regel

## GGM-bron

> "Vanwege de leesbaarheid wordt gewerkt met de term Toepasbare regel ipv regelbeheersobject. Een regelbeheerobject heeft een koppeling met een samenhangende set met regels om een afleiding te kunnen doen." (GGM, Omgevingswet)

- **Entiteit:** Toepasbare Regel
- **Beleidsdomein:** Omgevingswet
- **Attributen:** naam, omschrijving, domein, toestemming, soortAansluitpunt, datumBeginGeldigheid, datumEindeGeldigheid
- **Matchsterkte:** exact

## Relaties

| Relatie | BO | Richting | Beschrijving | Bron |
|---|---|---|---|---|
| associatie | [[Activiteit]] | → | Betreft activiteit | GGM |
| associatie | [[Juridische Regel]] | → | Komt voort uit juridische regel | GGM |

## Bedrijfsprocessen

- **Omgevingsplanvorming** — gemeente maakt toepasbare regels bij juridische regels
- **Digitale dienstverlening** — burgers/bedrijven gebruiken vragenbomen in het Omgevingsloket

## Bronnen

- [[Wiki/Bronsamenvattingen/Omgevingswet/imow-informatiemodel-omgevingswet]]
