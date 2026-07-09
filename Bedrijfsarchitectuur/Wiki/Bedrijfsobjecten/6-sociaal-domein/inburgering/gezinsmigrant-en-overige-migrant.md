---
type: element
naam: Gezinsmigrant en Overige migrant
onderwerp:
- Asiel en Integratie
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Gezinsmigrant en Overige migrant
ggm_guid: EAID_526489DC_4D57_4e6d_8338_5F7C898162F6
ggm_uml_type: Class
ggm_beleidsdomein: Inburgering
ggm_taakveld: 6 Sociaal Domein
ggm_diagram:
- Inburgering
- Relaties Sociaal Domein tot Kern
ggm_diagram_ids:
- EAID_96927C60_9F7B_4e67_806A_02EE0191983D
- EAID_D7287848_8118_4aab_8823_D555A599063C
ggm_definitie: 'Object Inburgeraar is gespecialiseerd in Asielstatushouder en Gezinsmigrant en Overige Migrant.

  Gezinsmigrant en Overige Migrant heeft geen kenmerken en is bedoeld om relaties te leggen met objecten die alleen van toepassing zijn voor Gezinsmigrant en Overige Migrant zoals bijvoorbeeld: object Aanvraag
  Sociale Lening. Hetzelfde geldt ook voor object Asielstatushouder, deze heeft overigens wel kenmerken.'
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:
ggm_gemma_naam: Gezinsmigrant en Overige migrant
ggm_gemma_guid:
ggm_gemma_definitie: 'Object Inburgeraar is gespecialiseerd in Asielstatushouder en Gezinsmigrant en Overige Migrant.

  Gezinsmigrant en Overige Migrant heeft geen kenmerken en is bedoeld om relaties te leggen met objecten die alleen van toepassing zijn voor Gezinsmigrant en'
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-61601c33-5b61-4bab-9191-e7eb1b1bca07"
ggm_gemma_bron:
ggm_gemma_alternate_name:
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Gezinsmigrant en Overige migrant** als directe tegenhanger. De gemeentelijke praktijkscope is beperkt tot het subtype Gezinsmigrant.
bo_definitie: "Inburgeraar die niet via de asielketen maar via gezinshereniging of een andere migratiereden inburgeringsplichtig is."
bo_toelichting: "GGM bundelt twee migrantcategorieën (Gezinsmigrant en Overige migrant) in één lege specialisatie van Inburgeraar, uitsluitend bedoeld om relaties te leggen (bijv. Aanvraag Sociale Lening). De gemeentelijke bronnen beschrijven uitsluitend gezinsmigranten; over 'overige migrant' bevatten de bronnen geen informatie."
bo_subtypes:
  - naam: "Gezinsmigrant"
    omschrijving: "Inburgeringsplichtige die verblijf heeft op grond van gezinshereniging; de enige praktijkscope van dit BO binnen de gemeente."
    ggm_entiteit: "Gezinsmigrant en Overige migrant"
    ggm_guid: EAID_526489DC_4D57_4e6d_8338_5F7C898162F6
    ggm_attribuut: ""
  - naam: "Overige migrant"
    omschrijving: "Andere migratiereden dan gezinshereniging of asiel; door de GGM-entiteit voorzien maar niet beschreven in de gemeentelijke bronnen."
    ggm_entiteit: "Gezinsmigrant en Overige migrant"
    ggm_guid: EAID_526489DC_4D57_4e6d_8338_5F7C898162F6
    ggm_attribuut: ""
bo_relaties:
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/brede-intake|Brede Intake]]"
  richting: van-dit-BO
  kardinaliteit: "1"
  beschrijving: Doorloopt een brede intake
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/pip|PIP]]"
  richting: van-dit-BO
  kardinaliteit: "1"
  beschrijving: Krijgt een persoonlijk plan inburgering en participatie
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringsplicht|Inburgeringsplicht]]"
  richting: van-dit-BO
  kardinaliteit: "1"
  beschrijving: Heeft een inburgeringsplicht
---

# Gezinsmigrant en Overige migrant

Inburgeraar die niet via de asielketen maar via gezinshereniging of een andere migratiereden inburgeringsplichtig is. De gemeentelijke praktijk (en dus dit BO) beperkt zich tot de subtype Gezinsmigrant; over "overige migrant" is in de bronnen niets gevonden.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus
- ✅ Heeft relaties met andere concepten

**Score: 6/6**, maar in de gemeentelijke praktijk is dit BO uitsluitend gevuld via de subtype Gezinsmigrant.

## Subtypes

Herkende specialisaties van Gezinsmigrant en Overige migrant. Geen apart BO — de GGM-entiteit zelf bundelt beide al in één lege specialisatie.

- **Gezinsmigrant** — inburgeringsplichtige die verblijf heeft op grond van gezinshereniging; de enige praktijkscope van dit BO binnen de gemeente.
- **Overige migrant** — andere migratiereden dan gezinshereniging of asiel; door de GGM-entiteit voorzien maar niet beschreven in de gemeentelijke bronnen.

## GGM-bron

> Object Inburgeraar is gespecialiseerd in Asielstatushouder en Gezinsmigrant en Overige Migrant. Gezinsmigrant en Overige Migrant heeft geen kenmerken en is bedoeld om relaties te leggen met objecten die alleen van toepassing zijn voor Gezinsmigrant en Overige Migrant.

- **Entiteit:** Gezinsmigrant en Overige migrant
- **Beleidsdomein:** Inburgering (taakveld 6 — Sociaal Domein)
- **Attributen:** *(geen)*
- **Overerving:** Inburgeraar (abstract) → Gezinsmigrant en Overige migrant
- **Matchsterkte:** exact — dit BO is de GGM-entiteit zelf; de gemeentelijke praktijkscope is beperkt tot de subtype Gezinsmigrant

## BO-definitie

De GGM-definitie is een technische UML-toelichting over de overervingsstructuur ("Object Inburgeraar is gespecialiseerd in..."), geen inhoudelijke definitie. De BO-definitie beschrijft wat een gezinsmigrant is vanuit de Wet inburgering.

## Relaties

- → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/brede-intake|brede-intake]] — doorloopt een brede intake [1]
- → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/pip|pip]] — krijgt een PIP vastgesteld [1]
- → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringsplicht|inburgeringsplicht]] — heeft een inburgeringsplicht [1]

## Bronnen

- [[Wiki/Bronsamenvattingen/Inburgering en Asielopvang/asielopvangwijzer]]
- [[Wiki/Bronsamenvattingen/Inburgering en Asielopvang/coa-dienstverleningsgids]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-asielopvang]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-inburgering]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-opvang-oekraine]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-rubriek-asiel]]
