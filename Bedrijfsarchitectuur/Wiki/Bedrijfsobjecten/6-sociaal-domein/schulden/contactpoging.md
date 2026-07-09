---
type: element
naam: Contactpoging
onderwerp: [schulden en armoede]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Contactpoging
ggm_guid: EAID_C7000EFD_826C_4e47_BD80_075A6EF4E558
ggm_uml_type: Class
ggm_beleidsdomein: Vroegsignalering
ggm_taakveld: "Schulden"
ggm_diagram: [Vroegsignalering, Vroegsignalering Details, Vroegsignalering Klein]
ggm_diagram_ids: [EAID_07334A5A_E2F0_41ce_8510_B41BAF6876BD, EAID_6D5829BF_AF12_4464_9EAD_E336DEFDF442, EAID_AFFABC16_BCDB_44c6_8E2F_C3D8C49884A5]
ggm_definitie: "Een Contactpoging is de actie die de gemeente onderneemt om in contact te treden met de inwoner naar aanleiding van een vroegsignaal."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst: GGM

ggm_gemma_naam:
ggm_gemma_guid:
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type:
ggm_gemma_url:
ggm_gemma_bron:
ggm_gemma_alternate_name:

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Contactpoging** als directe tegenhanger.
bo_definitie: "Een Contactpoging is de actie die de gemeente onderneemt om in contact te treden met de inwoner naar aanleiding van een vroegsignaal."
bo_toelichting:
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[vroegsignaalzaak]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Vroegsignaalzaak heeft contactpogingen"
bedrijfsprocessen: [vroegsignalering]
bedrijfsfuncties: [financiële hulpverlening]
---

## BO-criteria toetsing

6/6 criteria. Actie met eigen attributen (soort, bereikt, datum, dagdeel). Meerdere pogingen per zaak. Eigen levenscyclus (gepland → uitgevoerd → resultaat). Divosa-onderzoek toont aan dat het aantal contactpogingen de meest bepalende factor is voor het bereik van inwoners (+11 procentpunt per extra poging).

## Beschrijving

Een contactpoging is de actie die de gemeente onderneemt om in contact te treden met een inwoner naar aanleiding van een vroegsignaal. Contactpogingen maken onderdeel uit van een [[vroegsignaalzaak]] en kunnen verschillende vormen aannemen: brief, telefoon, huisbezoek, WhatsApp, sms of e-mail. Van elke poging wordt vastgelegd wanneer deze is gedaan, op welke wijze en wat het resultaat was.

Uit landelijk onderzoek onder 167 gemeenten (Divosa, 2024) blijkt dat het aantal contactpogingen de sterkste voorspeller is van het bereik. Gemeenten maken operationele keuzes over het type, de timing (dag/avond/weekend) en het maximum aantal pogingen.

## GGM-bron

> "Een Contactpoging is de actie die de gemeente onderneemt om in contact te treden met de inwoner naar aanleiding van een vroegsignaal. Een contactpoging maakt onderdeel uit van de vroegsignaalzaak en kan verschillende vormen aannemen, zoals een telefoongesprek, huisbezoek, brief of digitaal bericht. Van elke contactpoging wordt vastgelegd wanneer deze is gedaan, op welke wijze, met welk doel en wat het resultaat was."

- **Entiteit:** Contactpoging
- **Beleidsdomein:** Vroegsignalering (taakveld Schulden)
- **Attributen:** soort, bereikt, datum, dagdeel
- **Matchsterkte:** exact

## Relaties

| Type | Bedrijfsobject | Kardinaliteit | Beschrijving |
|---|---|---|---|
| associatie | [[vroegsignaalzaak\|Vroegsignaalzaak]] | 0..* | Onderdeel van zaak |

## Bronnen
- [[Wiki/Bronsamenvattingen/Schulden en Armoede/vroegsignaleringsaanpak-gemeenten-divosa-2024]]
- [[Wiki/Bronsamenvattingen/Schulden en Armoede/beleidsplan-schuldhulpverlening-den-haag-2024-2028]]
