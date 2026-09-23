---
type: element
naam: Signaalpartner
onderwerp: [schulden en armoede]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Signaalpartner
ggm_guid: EAID_3643CF44_EFAA_4939_9AEB_ACA8D8EE11F9
ggm_uml_type: Class
ggm_beleidsdomein: Vroegsignalering
ggm_taakveld: "Schulden"
ggm_diagram: [Vroegsignalering, Vroegsignalering Details, Vroegsignalering Klein]
ggm_definitie: "Een signaalpartner is een organisatie die op grond van artikel 2.2.1 van de Wet gemeentelijke schuldhulpverlening (Wgs) bevoegd is om signalen van betalingsachterstanden door te geven aan de gemeente met het doel vroegtijdige hulpverlening bij schulden mogelijk te maken."
ggm_herkomst: GGM

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Signaalpartner** als directe tegenhanger.
bo_definitie: "Een signaalpartner is een organisatie die op grond van artikel 2.2.1 van de Wet gemeentelijke schuldhulpverlening (Wgs) bevoegd is om signalen van betalingsachterstanden door te geven aan de gemeente met het doel vroegtijdige hulpverlening bij schulden mogelijk te maken."
bo_toelichting:
bo_subtypes: []
element_tegenhangers:
  - element: "[[Wiki/Actoren/signaalpartner|Signaalpartner (actor)]]"
    archimate_type: business-actor
    toelichting: "Dit bedrijfsobject legt de gegevens vast over de gelijknamige actor."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[vroegsignaal]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Signaalpartner verzendt vroegsignalen"
bedrijfsprocessen: [vroegsignalering]
bedrijfsfuncties: [financiële hulpverlening]
---

## BO-criteria toetsing

6/6 criteria. Actor met wettelijke grondslag (Wgs art. 2.2.1), eigen registratie (type), meerdere instanties, eigen levenscyclus (aansluiting, signaallevering, beëindiging).

## Beschrijving

Signaalpartners zijn dienstverleners met een maatschappelijk belang die wettelijk verplicht zijn betalingsachterstanden te melden bij de gemeente: zorgverzekeraars, energieleveranciers, drinkwaterbedrijven en woningverhuurders. Zij vormen het startpunt van het vroegsignaleringsproces.

De handelende kant van dit begrip is vastgelegd als actor [[Wiki/Actoren/signaalpartner|Signaalpartner (actor)]].

## GGM-bron

> "Een signaalpartner is een organisatie die op grond van artikel 2.2.1 van de Wgs bevoegd is om signalen van betalingsachterstanden door te geven aan de gemeente."

- **Entiteit:** Signaalpartner (specialisatie van [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/rechtspersoon|Rechtspersoon]])
- **Beleidsdomein:** Vroegsignalering (taakveld Schulden)
- **Attributen:** type
- **Matchsterkte:** exact

## Relaties

| Type | Bedrijfsobject | Kardinaliteit | Beschrijving |
|---|---|---|---|
| associatie | [[vroegsignaal\|Vroegsignaal]] | 0..* | Verzendt signalen |

## Bronnen
- [[Wiki/Bronsamenvattingen/Schulden en Armoede/beleidsplan-schuldhulpverlening-den-haag-2024-2028]]
- [[Wiki/Bronsamenvattingen/Schulden en Armoede/vroegsignaleringsaanpak-gemeenten-divosa-2024]]
