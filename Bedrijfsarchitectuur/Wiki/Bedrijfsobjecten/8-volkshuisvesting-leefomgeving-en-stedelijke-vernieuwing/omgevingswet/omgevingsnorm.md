---
type: element
naam: Omgevingsnorm
onderwerp: [Omgevingswet]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Omgevingsnorm
ggm_guid: EAID_F90F8E5E_7402_4c44_AC69_91A4175E5D47
ggm_uml_type: Class
ggm_beleidsdomein: Omgevingswet
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram:
  - "Omgevingswet Juridische Regels (CIMOW)"
ggm_diagram_ids:
  - EAID_0AC65EDC_5C77_4fd6_8548_98FCF09F72D0
ggm_definitie: "Een norm over de fysieke leefomgeving die in een kwantitatieve of kwalitatieve waarde wordt uitgedrukt en geen omgevingswaarde is."
ggm_toelichting: "Bijvoorbeeld: maximum bouwhoogte, maximum aantal parkeerplaatsen, maximum geluidbelasting, maximum aantal bezoekers."
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

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Omgevingsnorm** als directe tegenhanger.
bo_definitie: "Norm in het omgevingsplan die in kwantitatieve of kwalitatieve waarden wordt uitgedrukt als referentiepunt voor activiteiten in de fysieke leefomgeving."
bo_toelichting: "Omgevingsnormen bevatten normwaarden per locatie, zodat per gebied verschillende eisen kunnen gelden. Ze zijn gekoppeld aan juridische regels (RegelVoorIedereen) die beschrijven wat juridisch geldt."
bo_subtypes: []
bo_synoniemen: []
bo_homoniemen: []
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "Norm"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Omgevingsnorm is subtype van abstracte Norm"
  - type: associatie
    bedrijfsobject: "[[Juridische Regel]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "RegelVoorIedereen beschrijft omgevingsnorm"
bedrijfsprocessen:
  - "Omgevingsplanvorming"
bedrijfsfuncties:
  - "Ruimtelijke ordening"
---

# Omgevingsnorm

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Identiteit | ✅ | Eigen NEN3610-identificatie, naam, type, eenheid, groep |
| Levenscyclus | ✅ | Kan worden aangemaakt, gewijzigd en beëindigd in het DSO |
| Eigenaarschap | ✅ | Gemeente stelt vast in het omgevingsplan |
| Relaties | ✅ | Bevat normwaarden per locatie, gekoppeld aan juridische regels |
| Meervoud | ✅ | Meerdere per omgevingsplan (bouwhoogte, parkeren, geluid, etc.) |
| Registratie | ✅ | Geregistreerd in DSO/LVBB met NEN3610-ID |

## Beschrijving

Een Omgevingsnorm legt kwantitatieve of kwalitatieve waarden vast als referentiepunt voor handelen in de fysieke leefomgeving. De gemeente stelt omgevingsnormen vast in het omgevingsplan om per locatie aan te geven welke eisen gelden.

Elke omgevingsnorm bevat een of meer normwaarden, elk met een eigen locatie. Zo kan de maximum bouwhoogte in het centrum 20 meter zijn en in een woonwijk 10 meter — beide als normwaarde binnen dezelfde omgevingsnorm "bouwhoogte".

Normwaarden kunnen kwantitatief (getal + eenheid), kwalitatief (tekst) of verwijzend naar de regeltekst zijn.

Voorbeelden: maximum bouwhoogte, maximum aantal parkeerplaatsen, maximum geluidbelasting, minimale waterberging, maximum bebouwingspercentage.

## GGM-componenten

GGM-entiteiten die onderdeel zijn van Omgevingsnorm. Gemodelleerd als aparte entiteiten in het GGM maar vormen geen zelfstandig bedrijfsobject.

- **Normwaarde** — individuele kwantitatieve of kwalitatieve waarde van een norm, met eigen locatieaanduiding; attributen: kwalitatieveWaarde, kwantitatieveWaardeOmvang, kwantitatieveWaardeEenheid

## GGM-bron

> "Een norm over de fysieke leefomgeving die in een kwantitatieve of kwalitatieve waarde wordt uitgedrukt en geen omgevingswaarde is." (GGM, Omgevingswet)

- **Entiteit:** Omgevingsnorm
- **Beleidsdomein:** Omgevingswet
- **Attributen:** naam, omgevingsnormGroep
- **Matchsterkte:** exact

## Relaties

| Relatie | BO | Richting | Beschrijving | Bron |
|---|---|---|---|---|
| generalisatie | Norm (abstract) | ↑ | Omgevingsnorm is subtype van Norm | GGM |
| compositie | Normwaarde | ↓ | Bevat normwaarden per locatie | GGM |
| associatie | [[Juridische Regel]] | ← | RegelVoorIedereen beschrijft omgevingsnorm | GGM |
| associatie | [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/geluid/geluidbron\|Geluidbron]] | ← | Geluidnormen (max dB per bronsoort) zijn omgevingsnormen in het omgevingsplan | cross-domein |
| associatie | BOR Beheerobjecten | ← | Bouwhoogte, parkeereis, groenpercentage zijn omgevingsnormen die gelden bij BOR-objecten | cross-domein |

## Bedrijfsprocessen

- **Omgevingsplanvorming** — gemeente stelt normen vast per locatie

## Bronnen

- [[Wiki/Bronsamenvattingen/Omgevingswet/imow-informatiemodel-omgevingswet]]
