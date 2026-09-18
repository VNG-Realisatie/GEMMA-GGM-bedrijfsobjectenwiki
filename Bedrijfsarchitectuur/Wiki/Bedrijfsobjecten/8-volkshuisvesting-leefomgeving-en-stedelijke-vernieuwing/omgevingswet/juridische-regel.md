---
type: element
naam: Juridische Regel
onderwerp: [Omgevingswet]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Juridische Regel
ggm_guid: EAID_DDFF98D8_99FF_47b5_82D1_7FF2376750D6
ggm_uml_type: Class
ggm_beleidsdomein: Omgevingswet
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram:
  - "Omgevingswet Juridische Regels (CIMOW)"
  - "Omgevingswet Juridsiche regels en Idealisatie en Thema (CIMOW)"
  - "Omgevingswet Toepasbare Regels"
  - "Omgevingswet Verzoek Activiteit op Locatie"
ggm_diagram_ids:
  - EAID_0AC65EDC_5C77_4fd6_8548_98FCF09F72D0
  - EAID_BC0AA5E1_51A9_4e23_918C_FFABECCFE304
  - EAID_B9209AD2_0648_4482_BB24_135F27C2FECC
  - EAID_30B09C29_F649_4248_97FC_35A5F9331BBF
ggm_definitie: "De beschrijving van een regel met juridische werkingskracht. Een regel betreft binnen de Omgevingswet veelal activiteiten, en/of normen en/of functies en/of beperkingengebieden."
ggm_toelichting: "https://geonovum.github.io/TPOD/CIMOW/CIMOW_v2.1.0.pdf"
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
  Dit BO heeft de GGM-entiteit **Juridische Regel** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Idealisatie** (detail) — Detailgegeven (geassocieerd met BO)
  - **Instructieregel** (onderdeel) — Onderdeel (naamindicatie)
  - **Normwaarde** (detail) — Component van Omgevingsnorm / Omgevingswaarde
  - **Omgevingsdocument** (classificatie) — GGM-classificatie, geen zelfstandig gemeentelijk concept
  - **Omgevingswaarderegel** (onderdeel) — Onderdeel (naamindicatie)
  - **Regel voor Iedereen** (detail) — Detailgegeven (geassocieerd met BO)
  - **Regeltekst** (detail) — Component van Juridische Regel
  - **Thema** (detail) — Detailgegeven (geassocieerd met BO)
bo_definitie: "Regel met juridische werkingskracht in een omgevingsdocument, die activiteiten, normen, gebiedsaanwijzingen of omgevingswaarden beschrijft."
bo_toelichting: "Juridische regels zijn de bouwstenen van het omgevingsplan. Elke regel is gekoppeld aan een regeltekst (artikel/lid), een locatie en optioneel aan activiteiten, gebiedsaanwijzingen of normen. Er zijn drie subtypes met verschillende adressaten."
bo_subtypes: []
bo_via_kandidaten:
  - ggm_entiteit: "Normwaarde"
    ggm_guid: "EAID_58656D46_644B_4779_A473_739C5636BA0A"
    reden: "Een normwaarde wordt uitgedrukt via een juridische regel, die normen/omgevingswaarden beschrijft (expliciet in de GGM-definitie van Juridische Regel)."
bo_synoniemen: []
bo_homoniemen: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Activiteit]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "RegelVoorIedereen beschrijft activiteit"
  - type: associatie
    bedrijfsobject: "[[Gebiedsaanwijzing]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "RegelVoorIedereen/Instructieregel beschrijft gebiedsaanwijzing"
  - type: associatie
    bedrijfsobject: "[[Omgevingsnorm]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "RegelVoorIedereen beschrijft omgevingsnorm"
  - type: associatie
    bedrijfsobject: "[[Omgevingswaarde]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Omgevingswaarderegel beschrijft omgevingswaarde"
  - type: associatie
    bedrijfsobject: "[[Toepasbare Regel]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Toepasbare regel komt voort uit juridische regel"
bedrijfsprocessen:
  - "Omgevingsplanvorming"
bedrijfsfuncties:
  - "Ruimtelijke ordening"
---

# Juridische Regel

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Identiteit | ✅ | Eigen NEN3610-identificatie, omschrijving, thema |
| Levenscyclus | ✅ | Volgt het omgevingsdocument (inwerkingtreding, beëindiging) |
| Eigenaarschap | ✅ | Gemeente formuleert regels in het omgevingsplan |
| Relaties | ✅ | Centraal koppelobject: verbindt activiteiten, gebiedsaanwijzingen, normen, locaties |
| Meervoud | ✅ | Honderden per omgevingsplan |
| Registratie | ✅ | Geregistreerd in DSO/LVBB als OW-object |

## Beschrijving

Een Juridische Regel is de beschrijving van een regel met juridische werkingskracht in een omgevingsdocument. Het is het centrale koppelobject in het IMOW: elke regel verbindt een regeltekst (artikel/lid) met een locatie en optioneel met activiteiten, gebiedsaanwijzingen en normen.

Er zijn drie subtypes met verschillende adressaten:

- **RegelVoorIedereen** — regel die voor alle personen/organisaties geldt. Kan activiteiten, gebiedsaanwijzingen en omgevingsnormen beschrijven.
- **Instructieregel** — regel gericht op een ander bevoegd gezag (bijv. gemeente instrueert zichzelf of provincie instrueert gemeente). Kan gebiedsaanwijzingen beschrijven.
- **Omgevingswaarderegel** — regel gericht op het eigen bevoegd gezag. Beschrijft omgevingswaarden als beleidsdoel.

Elke juridische regel heeft een idealisatie (exact of indicatief) die aangeeft hoe de locatiebegrenzing moet worden geïnterpreteerd, en een thema dat de grondgedachte weergeeft.

## Subtypes

Herkende specialisaties van Juridische Regel. Gevonden in GGM. Geen apart BO.

- **Regel voor Iedereen** — regel die voor alle personen/organisaties geldt; kan activiteiten, gebiedsaanwijzingen en omgevingsnormen beschrijven; attribuut: activiteitRegelKwalificatie
- **Instructieregel** — regel gericht op ander bevoegd gezag of extern omgevingsdocument; attributen: instructieregelInstrument, instructieregelTaakuitoefening
- **Omgevingswaarderegel** — regel gericht op het eigen bevoegd gezag; attributen: naam, groep

## GGM-componenten

GGM-entiteiten die onderdeel zijn van Juridische Regel. Gemodelleerd als aparte entiteiten maar vormen geen zelfstandig bedrijfsobject.

- **Regeltekst** — kleinste zelfstandige eenheid van juridische regels (artikel/lid); koppelt STOP-tekst aan OW-objecten; attributen: tekst, identificatie, omschrijving
- **Idealisatie** — hoe de locatiebegrenzing wordt geïnterpreteerd (exact of indicatief); attributen: naam, omschrijving
- **Thema** — kernachtige weergave van de grondgedachte achter een regel; attributen: naam, omschrijving; hiërarchisch (subthema's)

## GGM-bron

> "De beschrijving van een regel met juridische werkingskracht. Een regel betreft binnen de Omgevingswet veelal activiteiten, en/of normen en/of functies en/of beperkingengebieden." (GGM, Omgevingswet)

- **Entiteit:** Juridische Regel
- **Beleidsdomein:** Omgevingswet
- **Attributen:** omschrijving, thema, regeltekst, datumStart, datumEindeGeldigheid, datumInWerking, datumBekend
- **Matchsterkte:** exact

## Relaties

| Relatie | BO | Richting | Beschrijving | Bron |
|---|---|---|---|---|
| associatie | [[Activiteit]] | → | RegelVoorIedereen beschrijft activiteit | GGM |
| associatie | [[Gebiedsaanwijzing]] | → | RegelVoorIedereen/Instructieregel beschrijft gebiedsaanwijzing | GGM |
| associatie | [[Omgevingsnorm]] | → | RegelVoorIedereen beschrijft omgevingsnorm | GGM |
| associatie | [[Omgevingswaarde]] | → | Omgevingswaarderegel beschrijft omgevingswaarde | GGM |
| associatie | [[Toepasbare Regel]] | → | Toepasbare regel komt voort uit juridische regel | GGM |

## Bedrijfsprocessen

- **Omgevingsplanvorming** — gemeente formuleert regels voor het omgevingsplan

## Bronnen

- [[Wiki/Bronsamenvattingen/Omgevingswet/imow-informatiemodel-omgevingswet]]
