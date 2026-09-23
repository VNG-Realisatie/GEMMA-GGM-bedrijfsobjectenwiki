---
type: element
naam: Collegelid
onderwerp: [bestuur]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Collegelid
ggm_guid: EAID_7B9EDDFD_57F7_4ff2_938F_FDFA3B503DA8
ggm_uml_type: Class
ggm_beleidsdomein: Griffie
ggm_taakveld: "0 Bestuur, Politiek en Ondersteuning"
ggm_definitie: "Iemand die behoort het college van burgemeester en wethouders"
ggm_herkomst: GGM
ggm_duplicaat_entiteiten: []
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Collegelid** als directe tegenhanger.
bo_definitie: "Iemand die behoort tot het college van burgemeester en wethouders."
bo_toelichting:
element_tegenhangers:
  - element: "[[Wiki/Rollen/collegelid|Collegelid (rol)]]"
    archimate_type: business-role
    toelichting: "Dit bedrijfsobject legt de gegevens vast over de gelijknamige rol."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/griffie/aanwezige-deelnemer|Aanwezige Deelnemer]]"
    richting: bidirectioneel
    kardinaliteit: "0..1"
    beschrijving: Een collegelid kan als aanwezige deelnemer geregistreerd worden bij een vergadering
  - type: associatie
    bedrijfsobject: "[[Wiki/Rollen/indiener|Indiener]]"
    richting: bidirectioneel
    kardinaliteit: "0..1"
    beschrijving: Een collegelid kan de rol van indiener vervullen (bijv. bij een raadsvoorstel)
---

# Collegelid

De vastgelegde gegevens over een collegelid: naam, titel, fractie, portefeuille en datum van aanstelling en uittreding.

De handelende kant van dit begrip is vastgelegd als rol [[Wiki/Rollen/collegelid|Collegelid (rol)]].

## BO-criteria toetsing

6/6 criteria: herkenbaar begrip met eigen registratie (voornaam, achternaam, titel, fractie, portefeuille, datumAanstelling, datumUittreding), meervoud, eigen levenscyclus en relaties binnen het domein.

## GGM-bron

> "Iemand die behoort het college van burgemeester en wethouders"

- **Entiteit:** Collegelid
- **Beleidsdomein:** Griffie (taakveld 0 Bestuur, Politiek en Ondersteuning)
- **Attributen:** voornaam, achternaam, titel, fractie, portefeuille, datumAanstelling, datumUittreding
- **Matchsterkte:** exact

## Relaties

| Relatie | Bedrijfsobject | Toelichting |
|---|---|---|
| Kan zijn | [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/griffie/aanwezige-deelnemer\|Aanwezige Deelnemer]] | Registratie van aanwezigheid bij een collegevergadering (GGM: "is") |
| Kan zijn | [[Wiki/Rollen/indiener\|Indiener]] | Bij het indienen van een raadsvoorstel (GGM: "is") |

**Openstaand:** het GGM modelleert Collegelid als generalisatie van **Ingezetene**, zelfde patroon als [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/griffie/raadslid|Raadslid]]. Ingezetene heeft nog geen eigen wiki-pagina; niet beoordeeld in deze sessie.

## Bronnen

- [[Wiki/Bronsamenvattingen/Bestuur/gemeentewet-wettekst]] — Gemeentewet art. 34-41b (benoeming, vereisten, incompatibiliteiten collegelid)