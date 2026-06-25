---
type: bedrijfsobject
naam: Zekerheidsrecht
onderwerp: [Basisregistraties, BRK]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Zekerheidsrecht
ggm_guid: EAID_3397A5B5_E789_46e6_8559_C528EA55F830
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram:
  - "Detaillering Kadastrale Onroerende Zaken en Rechten op hoofdlijnen"
  - "Detaillering Kadastrale Onroerende Zaken en Rechten met attributen"
  - "ZEKERHEIDSRECHT"
ggm_diagram_ids:
  - EAID_0A286E07_9DEF_46a8_AC66_469F5A70564E
  - EAID_FF8B8883_467A_422e_A894_C513307057AF
  - EAID_AE0CCD75_E232_45fb_82A3_BF38667D26EC
ggm_definitie: "Een zekerheidsrecht is een beperkt recht (hypotheek) of een beperking (beslag)."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""

ggm_gemma_naam: Zekerheidsrecht
ggm_gemma_guid: 0f33d06b-3e1f-4693-87af-2a5a9b739219
ggm_gemma_definitie: "Een zekerheidsrecht is een beperkt recht (hypotheek) of een beperking (beslag)."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: business-object
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-0f33d06b-3e1f-4693-87af-2a5a9b739219"
ggm_gemma_bron: "BRK"
ggm_gemma_alternate_name: ""

ggm_duplicaat_entiteiten: []

gemma_definitie: "Een hypotheek of beslag op een onroerende zaak, geregistreerd in de BRK."
relaties:
  - type: associatie
    bedrijfsobject: "[[Kadastraal Perceel]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Een zekerheidsrecht rust op een kadastraal perceel of appartementsrecht"
  - type: associatie
    bedrijfsobject: "[[Appartementsrecht]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Een zekerheidsrecht rust op een kadastraal perceel of appartementsrecht"
  - type: associatie
    bedrijfsobject: "[[Stukdeel]]"
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Een zekerheidsrecht is gebaseerd op een of meer stukdelen"
bedrijfsprocessen:
  - Dwanginvordering
  - Fiscaal beslag
  - Eigendomsverificatie
bedrijfsfuncties:
  - Belastingheffing
  - Handhaving
---

## BO-criteria toetsing

6/6 criteria. Zekerheidsrecht is een concreet registratieobject met eigen identificatie, eigen levenscyclus (vestiging → doorhaling/opheffing), meervoudig (meerdere hypotheken/beslagen per object), en relaties met kadastrale objecten en personen. De gemeente kan zelf fiscaal beslag leggen bij belastingschuld.

## Beschrijving

Een zekerheidsrecht is een hypotheek of beslag op een onroerende zaak. In de BRK wordt onderscheid gemaakt tussen hypothecaire zekerheidsstelling (door een hypotheeknemer, meestal een bank) en zekerheidsstelling inzake beslag (door een beslaglegger). De gemeente is relevant als beslaglegger: bij onbetaalde gemeentelijke belastingen kan de gemeente fiscaal beslag leggen op een onroerende zaak via een dwangbevel. Daarnaast raadpleegt de gemeente zekerheidsrechten bij eigendomsverificatie.

## Subtypes

Herkende specialisaties van Zekerheidsrecht. Gevonden in de BRK Catalogus en GGM. Geen apart BO.

- **ZekerheidsstellingHypothecair** — hypotheekrecht, gevestigd door een hypotheeknemer (meestal bank)
- **ZekerheidsstellingInzakeBeslag** — beslag op een onroerende zaak door een beslaglegger (gemeente, belastingdienst, deurwaarder)

## GGM-bron

> "Een zekerheidsrecht is een beperkt recht (hypotheek) of een beperking (beslag)."

- **Entiteit:** Zekerheidsrecht
- **Beleidsdomein:** RSGBPlus (99 Kern)
- **Attributen:** identificatieZekerheidsrecht, omschrijvingBetrokkenRecht, typeZekerheidsrecht, aandeelInBetrokkenRecht, datumIngangRecht, datumEindeRecht
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | BO | Kardinaliteit | Bron |
|---|---|---|---|---|
| rust op | van-dit-BO | [[Kadastraal Perceel]] / [[Appartementsrecht]] | 1 | GGM |
| gebaseerd op | van-dit-BO | [[Stukdeel]] | 1..* | BRK Catalogus |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-brk]]
