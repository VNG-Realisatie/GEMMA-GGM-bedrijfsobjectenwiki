---
type: bedrijfsobject
naam: Omgevingswaarde
onderwerp: [Omgevingswet]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Omgevingswaarde
ggm_guid: EAID_6B1F7274_19A7_4349_835E_85CBEFFEE35A
ggm_uml_type: Class
ggm_beleidsdomein: Omgevingswet
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram:
  - "Omgevingswet Juridische Regels (CIMOW)"
ggm_diagram_ids:
  - EAID_0AC65EDC_5C77_4fd6_8548_98FCF09F72D0
ggm_definitie: "Een norm die voor (een onderdeel van) de fysieke leefomgeving de gewenste staat of kwaliteit, de toelaatbare belasting door activiteiten en/of de toelaatbare concentratie of depositie van stoffen als beleidsdoel vastlegt."
ggm_toelichting: "Bijvoorbeeld: streefwaarden of maximaal toelaatbare waarden voor luchtkwaliteit, kwaliteit van oppervlaktewater, grondwater of zwemwater."
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
  Dit BO heeft de GGM-entiteit **Omgevingswaarde** als directe tegenhanger.
bo_definitie: "Norm in het omgevingsplan die de gewenste staat of kwaliteit van de fysieke leefomgeving als beleidsdoel vastlegt."
bo_toelichting: "Omgevingswaarden zijn zelfbindend voor het bestuursorgaan dat ze vaststelt — ze scheppen verplichtingen voor het bevoegd gezag, niet voor burgers. Structureel identiek aan Omgevingsnorm maar met een ander juridisch karakter: beleidsdoel vs. regulering."
bo_subtypes: []
bo_synoniemen: []
bo_homoniemen: []
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "Norm"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Omgevingswaarde is subtype van abstracte Norm"
  - type: associatie
    bedrijfsobject: "[[Juridische Regel]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Omgevingswaarderegel beschrijft omgevingswaarde"
bedrijfsprocessen:
  - "Omgevingsplanvorming"
  - "Monitoring leefomgeving"
bedrijfsfuncties:
  - "Ruimtelijke ordening"
---

# Omgevingswaarde

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Identiteit | ✅ | Eigen NEN3610-identificatie, naam, type, eenheid, groep |
| Levenscyclus | ✅ | Kan worden aangemaakt, gewijzigd en beëindigd in het DSO |
| Eigenaarschap | ✅ | Gemeente stelt vast in het omgevingsplan |
| Relaties | ✅ | Bevat normwaarden per locatie, gekoppeld aan omgevingswaarderegels |
| Meervoud | ✅ | Meerdere per omgevingsplan (luchtkwaliteit, waterkwaliteit, geluid) |
| Registratie | ✅ | Geregistreerd in DSO/LVBB met NEN3610-ID |

## Beschrijving

Een Omgevingswaarde legt de gewenste staat of kwaliteit van de fysieke leefomgeving vast als beleidsdoel. Anders dan een [[Omgevingsnorm]] (die regels stelt voor burgers/bedrijven) is een Omgevingswaarde zelfbindend voor het bestuursorgaan: het bevoegd gezag verplicht zichzelf om de vastgelegde kwaliteit na te streven.

Technisch is de structuur identiek aan [[Omgevingsnorm]]: normwaarden per locatie, kwantitatief of kwalitatief. Het verschil zit in het juridische karakter: omgevingswaarden worden beschreven door Omgevingswaarderegels (gericht op het eigen bevoegd gezag), terwijl omgevingsnormen worden beschreven door RegelsVoorIedereen.

Voorbeelden: maximaal toelaatbare geluidbelasting in een gebied, streefwaarde luchtkwaliteit (PM10, NO2), kwaliteit oppervlaktewater, grondwaterkwaliteit.

## GGM-bron

> "Een norm die voor (een onderdeel van) de fysieke leefomgeving de gewenste staat of kwaliteit, de toelaatbare belasting door activiteiten en/of de toelaatbare concentratie of depositie van stoffen als beleidsdoel vastlegt." (GGM, Omgevingswet)

- **Entiteit:** Omgevingswaarde
- **Beleidsdomein:** Omgevingswet
- **Attributen:** naam, omgevingswaardeGroep
- **Matchsterkte:** exact

## Relaties

| Relatie | BO | Richting | Beschrijving | Bron |
|---|---|---|---|---|
| generalisatie | Norm (abstract) | ↑ | Omgevingswaarde is subtype van Norm | GGM |
| compositie | Normwaarde | ↓ | Bevat normwaarden per locatie | GGM |
| associatie | [[Juridische Regel]] | ← | Omgevingswaarderegel beschrijft omgevingswaarde | GGM |
| associatie | [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/geluid/geluidbron\|Geluidbron]] | ← | Geluidproductieplafonds zijn omgevingswaarden | cross-domein |
| associatie | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/waterobject\|Waterobject]] | ← | Waterkwaliteitsdoelen zijn omgevingswaarden | cross-domein |

## Bedrijfsprocessen

- **Omgevingsplanvorming** — gemeente legt beleidsdoelen vast
- **Monitoring leefomgeving** — meten of waarden gehaald worden

## Bronnen

- [[Wiki/Bronsamenvattingen/Omgevingswet/imow-informatiemodel-omgevingswet]]
