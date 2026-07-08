---
type: element
naam: Gebiedsaanwijzing
onderwerp: [Omgevingswet]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Gebiedsaanwijzing
ggm_guid: EAID_503BD06E_E063_46f2_8B43_BF75A143D6C4
ggm_uml_type: Class
ggm_beleidsdomein: Omgevingswet
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram:
  - "Omgevingswet Juridische Regels (CIMOW)"
  - "Omgevingswet Verzoek Activiteit op Locatie"
ggm_diagram_ids:
  - EAID_0AC65EDC_5C77_4fd6_8548_98FCF09F72D0
  - EAID_30B09C29_F649_4248_97FC_35A5F9331BBF
ggm_definitie: "Functie of een Beperkingengebied, met een verwijzing naar locatie, veelal een gebied, waarbij aangegeven wordt hoe het gebied beschouwd wordt vanuit de bijbehorende regels."
ggm_toelichting: "Voorbeeld: bebouwde kom."
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
  Dit BO heeft de GGM-entiteit **Gebiedsaanwijzing** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Beperkingsgebied** (detail) — Detailgegeven (weinig attributen)
  - **Functie** (detail) — Detailgegeven (weinig attributen)
bo_definitie: "Aanwijzing van een specifiek gebied in het omgevingsplan met een type, naam en locatie die aangeeft hoe het gebied beschouwd wordt vanuit de bijbehorende regels."
bo_toelichting: "Gebiedsaanwijzingen komen in twee vormen: Functies (wat mag in dit gebied, bijv. wonen, bedrijvigheid) en Beperkingsgebieden (welke beperkingen gelden, bijv. bij een gasleiding). Elk heeft een type uit een waardelijst, een groep en een koppeling aan locatie(s)."
bo_subtypes: []
bo_synoniemen: []
bo_homoniemen: []
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "Functie"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Functie is subtype van Gebiedsaanwijzing"
  - type: generalisatie
    bedrijfsobject: "Beperkingsgebied"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Beperkingsgebied is subtype van Gebiedsaanwijzing"
  - type: associatie
    bedrijfsobject: "[[Juridische Regel]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "RegelVoorIedereen en Instructieregel beschrijven gebiedsaanwijzing"
  - type: associatie
    bedrijfsobject: "[[Activiteit]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: "Gekoppeld via juridische regels en locaties"
bedrijfsprocessen:
  - "Omgevingsplanvorming"
bedrijfsfuncties:
  - "Ruimtelijke ordening"
---

# Gebiedsaanwijzing

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Identiteit | ✅ | Eigen NEN3610-identificatie, type, naam, groep |
| Levenscyclus | ✅ | Kan worden aangemaakt, gewijzigd en beëindigd in het DSO |
| Eigenaarschap | ✅ | Gemeente beheert als bronhouder in het omgevingsplan |
| Relaties | ✅ | Gekoppeld aan locaties, juridische regels, activiteiten |
| Meervoud | ✅ | Vele per omgevingsplan (functies, beperkingsgebieden) |
| Registratie | ✅ | Geregistreerd in DSO/LVBB met NEN3610-ID |

## Beschrijving

Een Gebiedsaanwijzing wijst een specifiek gebied aan in het omgevingsplan en geeft aan hoe dat gebied beschouwd wordt vanuit de regels. De gemeente gebruikt gebiedsaanwijzingen om het grondgebied functioneel in te delen.

Er zijn twee subtypes:
- **Functie** — samenhangende verzameling rollen die een gebied vervult (bijv. woonfunctie, bedrijfsfunctie, centrumgebied, groenstructuur)
- **Beperkingsgebied** — gebied waar vanwege een aanwezig werk of object beperkingen gelden voor activiteiten (bijv. beschermingszone gasleiding, geluidszone industrieterrein)

Elke gebiedsaanwijzing heeft een type (uit een waardelijst), een groep, een naam en een locatieaanduiding (geometrie). Juridische regels verwijzen naar gebiedsaanwijzingen om aan te geven in welk type gebied de regel geldt.

## Subtypes

Herkende specialisaties van Gebiedsaanwijzing. Gevonden in GGM. Geen apart BO.

- **Functie** — samenhangende verzameling rollen die een gebied vervult; attributen: naam, groep
- **Beperkingsgebied** — gebied waar vanwege aanwezig werk of object beperkingen gelden; attributen: naam, groep

## GGM-bron

> "Functie of een Beperkingengebied, met een verwijzing naar locatie, veelal een gebied, waarbij aangegeven wordt hoe het gebied beschouwd wordt vanuit de bijbehorende regels." (GGM, Omgevingswet)

- **Entiteit:** Gebiedsaanwijzing
- **Beleidsdomein:** Omgevingswet
- **Attributen:** NEN3610ID, groep, naam
- **Matchsterkte:** exact

## Relaties

| Relatie | BO | Richting | Beschrijving | Bron |
|---|---|---|---|---|
| generalisatie | Functie | ↓ | Subtype: samenhangende verzameling rollen | GGM |
| generalisatie | Beperkingsgebied | ↓ | Subtype: beperkingen bij werk/object | GGM |
| associatie | [[Juridische Regel]] | ← | Instructieregel/RegelVoorIedereen beschrijft gebiedsaanwijzing | GGM |
| associatie | [[Activiteit]] | ↔ | Gekoppeld via juridische regels en locaties | GGM |
| associatie | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/aandachtsgebied\|Aandachtsgebied]] | ← | Aandachtsgebied (gevaarlijke stoffen) is een Beperkingsgebied (partieel) | cross-domein |
| associatie | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/voorschriftengebied\|Voorschriftengebied]] | ← | Voorschriftengebied is een Beperkingsgebied (partieel) | cross-domein |
| associatie | BOR FunctioneelGebied | ↔ | BOR FunctioneelGebied ([[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/speelterrein\|Speelterrein]], Sportterrein, [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/rioleringsgebied\|Rioleringsgebied]]) ≈ Functie-subtype in omgevingsplan; conceptuele overlap, technisch ander model (IMBOR vs IMOW) | cross-domein |
| associatie | [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/geluid/geluidbron\|Geluidbron]] | ← | Geluidzones rond geluidbronnen zijn Beperkingsgebieden | cross-domein |

## Bedrijfsprocessen

- **Omgevingsplanvorming** — gemeente wijst gebieden aan en koppelt functies/beperkingen

## Bronnen

- [[Wiki/Bronsamenvattingen/Omgevingswet/imow-informatiemodel-omgevingswet]]
