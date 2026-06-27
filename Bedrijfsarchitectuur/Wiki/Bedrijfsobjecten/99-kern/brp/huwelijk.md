---
type: bedrijfsobject
naam: Huwelijk
onderwerp: [Basisregistraties, BRP]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: SluitingOfAangaanHuwelijkOfGeregistreerdPartnerschap
ggm_guid: EAID_28A0D7C0_DABF_403b_B263_22F424032A28
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram: ["HUWELIJK/GEREGISTREERD PARTNERSCHAP", "Huishouden en Huwelijk"]
ggm_diagram_ids: []
ggm_definitie: "Gegevens over het gesloten huwelijk of het aangegane geregistreerd partnerschap."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: "GGM"

ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""

ggm_duplicaat_entiteiten: []

bo_definitie: "Een in de BRP geregistreerd huwelijk of geregistreerd partnerschap tussen twee personen, inclusief sluiting en eventuele ontbinding."
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Ingeschreven Persoon]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Persoon heeft huwelijken/partnerschappen (BRP categorie 05)"
  - type: associatie
    bedrijfsobject: "[[Woonplaats]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Plaats van sluiting of ontbinding"
bedrijfsprocessen: [Huwelijksvoltrekking, Registratie geregistreerd partnerschap, Echtscheiding]
bedrijfsfuncties: [Burgerzakenloket, Bevolkingsadministratie]
---

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Herkenbaar in dagelijks werk | ✅ | Huwelijk/partnerschap is een kernproces van burgerzaken |
| Eigenaar/houder | ✅ | Gemeente registreert in BRP, ambtenaar van de burgerlijke stand voltrekt |
| Levenscyclus | ✅ | Sluiting/aangaan → actueel → ontbinding (scheiding, overlijden, nietigverklaring) |
| Meervoudig | ✅ | Een persoon kan meerdere opeenvolgende verbintenissen hebben (cat. 05 is 0,n) |
| Gegevens | ✅ | Partnergegevens, datum/plaats sluiting, datum/plaats/reden ontbinding, soort verbintenis |
| Relaties met andere BO's | ✅ | [[Ingeschreven Persoon]] (beide partners), [[Woonplaats]] (plaats sluiting) |

## Beschrijving

Een Huwelijk is de registratie in de BRP van een huwelijk of geregistreerd partnerschap. BRP-categorie 05 bevat de gegevens van de partner (identificatie, naam, geboorte, geslacht), de sluiting (datum, plaats, land) en eventuele ontbinding (datum, plaats, land, reden). De soort verbintenis (huwelijk of geregistreerd partnerschap) wordt apart geregistreerd.

Een persoon kan meerdere opeenvolgende verbintenissen hebben. Bij ontbinding wordt de categorie niet verwijderd maar aangevuld met ontbindingsgegevens; de actuele stapel representeert de huidige of laatst beëindigde verbintenis, historische stapels de eerdere.

## Subtypes

Herkende specialisaties van Huwelijk. Geen apart BO.

- **Huwelijk (burgerlijk)** — verbintenis gesloten voor de ambtenaar van de burgerlijke stand
- **Geregistreerd partnerschap** — verbintenis geregistreerd bij de ambtenaar van de burgerlijke stand (BRP element 15.10 Soort verbintenis)

## GGM-componenten

GGM-entiteiten die onderdeel zijn van Huwelijk. Het GGM splitst de verbintenis in twee gebeurtenisentiteiten; het BO representeert de volledige verbintenis inclusief levenscyclus.

- **OntbindingHuwelijk/geregistreerdPartnerschap** — gegevens over de ontbinding: redenEinde, datumEinde, gemeenteEinde, buitenlandsePlaatsEinde, landOfGebiedEinde (7 attributen)

## GGM-bron

> "Gegevens over het gesloten huwelijk of het aangegane geregistreerd partnerschap."

- **GGM-entiteit:** SluitingOfAangaanHuwelijkOfGeregistreerdPartnerschap
- **Beleidsdomein:** RSGBPlus
- **Attributen (6):** datumAanvang, gemeenteAanvang, buitenlandsePlaatsAanvang, landOfGebiedAanvang, buitenlandseRegioAanvang, omschrijvingLocatieAanvang
- **Matchsterkte:** exact — het GGM modelleert sluiting en ontbinding als aparte entiteiten; het BO bundelt deze als levenscyclus van één verbintenis, conform de BRP-categorie 05

## BO-definitie

De GGM-definitie beschrijft alleen de sluitingsgegevens. De GEMMA-definitie is breder: "Een in de BRP geregistreerd huwelijk of geregistreerd partnerschap tussen twee personen, inclusief sluiting en eventuele ontbinding." Dit weerspiegelt de BRP-registratie waarin sluiting en ontbinding samen in één categorie staan.

## Relaties

| Gerelateerd BO | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | ← | 0..* | Persoon heeft huwelijken/partnerschappen | BRP cat. 05 |
| [[Wiki/Bedrijfsobjecten/99-kern/bag/woonplaats\|Woonplaats]] | → | 0..1 | Plaats van sluiting of ontbinding | GGM |

## Bedrijfsprocessen

- Huwelijksvoltrekking (ondertrouw → voltrekking → registratie in BRP)
- Registratie geregistreerd partnerschap
- Verwerking echtscheiding/ontbinding (na rechterlijke uitspraak)
- Omzetting huwelijk ↔ geregistreerd partnerschap

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/logisch-ontwerp-brp-2025q1]]
