---
type: element
naam: Appartementsrecht
onderwerp: [Basisregistraties, BRK]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Appartementsrecht
ggm_guid: EAID_869E0A04_A663_4839_970D_7FB82DF6C317
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram:
  - "BRK"
  - "Ruimte WOZ en Benoemd Object"
  - "Detaillering Kadastrale Onroerende Zaken en Rechten op hoofdlijnen"
  - "Detaillering concreten en abstracte Kadastrale Onroerende Zaken objecttypen"
ggm_diagram_ids:
  - EAID_DF9CEAAD_E574_40b3_970B_DC558AB579D0
  - EAID_F9683FD0_4AA1_40c0_A132_4EA8F639B371
  - EAID_0A286E07_9DEF_46a8_AC66_469F5A70564E
  - EAID_2BA6CA76_17FC_4afc_82AD_9DF0DC891587
ggm_definitie: "Een KADASTRALE ONROERENDE ZAAK dat een aandeel is in de goederen die in de splitsing zijn betrokken, dat de bevoegdheid omvat tot het uitsluitend gebruik van bepaalde gedeelten van het gebouw die blijkens hun inrichting bestemd zijn of worden om als afzonderlijk geheel te worden gebruikt (art. 5:106 lid 4 BW)."
ggm_toelichting: "Een aandeel in een recht op een gebouw en daarmee onlosmakelijk verbonden het uitsluitend gebruiksrecht van een bepaald privé-gedeelte in dat gebouw. Dat kan ook een garage of een parkeerplaats zijn. Een splitsing in appartementsrechten komt tot stand door inschrijving van een notariële akte van splitsing bij het kadaster. Elke splitsing kent een Vereniging van Eigenaren (VVE)."
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam: Appartementsrecht
ggm_gemma_guid: "b84fbae7-cecd-4c24-96cb-427a00d862c6"
ggm_gemma_definitie: "Een KADASTRALE ONROERENDE ZAAK dat een aandeel is in de goederen die in de splitsing zijn betrokken, dat de bevoegdheid omvat tot het uitsluitend gebruik van bepaalde gedeelten van het gebouw die blijkens hun inrichting bestemd zijn of worden om als afzonderlijk geheel te worden gebruikt (art. 5:106 lid 4 BW)."
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-b84fbae7-cecd-4c24-96cb-427a00d862c6"
ggm_gemma_bron: "BRK"
ggm_gemma_alternate_name:

ggm_duplicaat_entiteiten: []

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Appartementsrecht** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **KadastraleOnroerendeZaakAantekening** (detail) — Detailgegeven
  - **KoopsomKadastraleOnroerendeZaak** (detail) — Detailgegeven
  - **LocatieKadastraleOnroerendeZaak** (detail) — Detailgegeven
bo_definitie: "Een KADASTRALE ONROERENDE ZAAK dat een aandeel is in de goederen die in de splitsing zijn betrokken, dat de bevoegdheid omvat tot het uitsluitend gebruik van bepaalde gedeelten van het gebouw die blijkens hun inrichting bestemd zijn of worden om als afzonderlijk geheel te worden gebruikt (art. 5:106 lid 4 BW)."
bo_toelichting:
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Appartementsrecht]]"
    richting: naar-dit-BO
    kardinaliteit:
    beschrijving: "Specialisatie van KadastraleOnroerendeZaak (abstract)"
  - type: associatie
    bedrijfsobject: "[[Zakelijk Recht]]"
    richting: naar-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Op een appartementsrecht rusten een of meer zakelijke rechten"
  - type: associatie
    bedrijfsobject: "[[Zekerheidsrecht]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Op een appartementsrecht kan een zekerheidsrecht rusten"
  - type: associatie
    bedrijfsobject: "[[WOZ-object]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een appartementsrecht kan onderdeel zijn van een WOZ-object"
bedrijfsprocessen:
  - WOZ-taxatie
  - OZB-heffing
  - VvE-toezicht
bedrijfsfuncties:
  - Belastingheffing
  - Volkshuisvesting
---

## BO-criteria toetsing

6/6 criteria. Appartementsrecht is een concreet registratieobject met eigen kadastrale aanduiding (inclusief appartementsrechtvolgnummer), eigen levenscyclus (ontstaan door splitsingsakte, beëindigd door opheffing splitsing), meervoudig, en relaties met zakelijke rechten, personen en WOZ-objecten.

## Beschrijving

Een appartementsrecht geeft de eigenaar het exclusieve gebruiksrecht van een privé-gedeelte in een gesplitst gebouw (woning, kantoor, garage, parkeerplaats). Het ontstaat door inschrijving van een notariële splitsingsakte bij het Kadaster. Elke splitsing kent een Vereniging van Eigenaren (VvE). De gemeente gebruikt appartementsrechten voor WOZ-waardering, OZB-heffing en VvE-toezicht.

## Generalisatie

Appartementsrecht is een specialisatie van KadastraleOnroerendeZaak (abstract in GGM). De hiërarchie: **KadastraleOnroerendeZaak** → [[Kadastraal Perceel]] / **Appartementsrecht**. Beide specialisaties delen kadastrale aanduiding en relaties met zakelijke rechten.

## GGM-componenten

GGM-entiteiten die onderdeel zijn van Appartementsrecht. Gemodelleerd als aparte entiteiten in het GGM maar vormen geen zelfstandig bedrijfsobject.

- **Appartementsrechtsplitsing** — het recht op grond of gebouw is gesplitst in appartementsrechten. Onderscheidt hoofdsplitsing en ondersplitsing.
- **SplitsingstekeningReferentie** — verwijzing naar de splitsingstekening behorende bij de splitsing.

## GGM-bron

> "Een KADASTRALE ONROERENDE ZAAK dat een aandeel is in de goederen die in de splitsing zijn betrokken, dat de bevoegdheid omvat tot het uitsluitend gebruik van bepaalde gedeelten van het gebouw die blijkens hun inrichting bestemd zijn of worden om als afzonderlijk geheel te worden gebruikt (art. 5:106 lid 4 BW)."

- **Entiteit:** Appartementsrecht
- **Beleidsdomein:** RSGBPlus (99 Kern)
- **Attributen:** *(geen eigen attributen; erft van KadastraleOnroerendeZaak)*
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | BO | Kardinaliteit | Bron |
|---|---|---|---|---|
| rust op | naar-dit-BO | [[Zakelijk Recht]] | 1..* | GGM |
| rust op | naar-dit-BO | [[Zekerheidsrecht]] | 0..* | GGM |
| WOZ-koppeling | naar-dit-BO | [[WOZ-object]] | 0..* | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-brk]]
