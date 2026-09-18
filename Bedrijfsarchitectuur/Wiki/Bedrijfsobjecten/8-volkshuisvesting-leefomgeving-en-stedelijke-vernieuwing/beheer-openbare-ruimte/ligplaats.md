---
type: element
naam: Ligplaats
onderwerp: [Beheer Openbare Ruimte, Wonen, Basisregistraties, BAG]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Ligplaats
ggm_guid: EAID_785E3B69_19DA_4952_84A8_592965B9229A
ggm_uml_type: Class
ggm_beleidsdomein: BAG
ggm_taakveld: "99 Kern"
ggm_diagram: ["Objecten bij Vergunningaanvraag", "BAG", "LIGPLAATS", "Ruimte Adressen, gebouwen en terreinen"]
ggm_diagram_ids: ["EAID_C9CE09B7_32EF_40eb_9C82_7FD6EDEA1D9E", "EAID_53E16E43_EDF1_4b47_B0DD_C77D8FEFCCA3", "EAID_B3A1E688_38D0_4763_8396_CA1F19AD3EF6", "EAID_7561B00D_273B_425a_B2FE_1C3AE499ED2E"]
ggm_definitie: "Een ligplaats is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen plaats in het water al dan niet aangevuld met een op de oever aanwezig terrein of een gedeelte daarvan, die bestemd is voor het permanent afmeren van een voor woon-, bedrijfsmatige of recreatieve doeleinden geschikt drijvend object."
ggm_toelichting:
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

ggm_duplicaat_entiteiten:
  - entiteit: Ligplaats
    guid: EAID_F4978264_32A5_4e70_97A8_D142B64400A8
    beleidsdomein: RSGBPlus
    taakveld: "99 Kern"
    afwijkende_attributen: "RSGBPlus gebruikt domein-geprefixte namen (ligplaatsidentificatie, ligplaatsstatus, indicatieGeconstateerdeLigplaats); minder attributen, geen geometrie/versie/documentvelden; voegt inOnderzoek toe"

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Ligplaats** als directe tegenhanger. Daarnaast is **Ligplaats** (beleidsdomein RSGBPlus) als vermoedelijk duplicaat gekoppeld — zie ggm_duplicaat_entiteiten.
bo_definitie: "Een ligplaats is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen plaats in het water al dan niet aangevuld met een op de oever aanwezig terrein of een gedeelte daarvan, die bestemd is voor het permanent afmeren van een voor woon-, bedrijfsmatige of recreatieve doeleinden geschikt drijvend object."
bo_toelichting:
bo_subtypes:
  - naam: "Reserveligplaats"
    omschrijving: "Tijdelijke ligplaats voor noodgevallen zoals kade-onderhoud of verplaatsing."
    ggm_entiteit: Ligplaats
    ggm_guid: EAID_785E3B69_19DA_4952_84A8_592965B9229A
    ggm_attribuut: type
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Waterobject]]"
    richting: bidirectioneel
    kardinaliteit:
    beschrijving: "Ligplaats bevindt zich in een waterobject/vaarweg"
  - type: associatie
    bedrijfsobject: "[[Vaartuig]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Een ligplaats kan bezet zijn door een vaartuig (in de praktijk: woonboot)"
  - type: generalisatie
    bedrijfsobject: "[[AdresseerbaarObject]]"
    richting: van-dit-BO
    kardinaliteit:
    beschrijving: "Ligplaats is een specialisatie van Adresseerbaar Object (BAG)"
bedrijfsprocessen: [Ligplaats aanwijzen, Ligplaatsvergunningverlening, Havenbeheer, Toezicht en handhaving stadswater, Ligplaats opheffen]
bedrijfsfuncties: [Havendienst, BAG-beheer, Vergunningverlening, Handhaving]
---

## BO-criteria toetsing

| Criterium                                 | Van toepassing? | Toelichting                                                                    |
| ----------------------------------------- | --------------- | ------------------------------------------------------------------------------ |
| Heeft betekenis binnen het domein         | ✅               | Centraal begrip in havenbeheer, stadswatersbeleid en woonbotenbeleid           |
| Is herkenbaar voor domeinexperts          | ✅               | Standaardbegrip in havenbeheer, BAG, vergunningverlening en handhaving         |
| Heeft een eigen bestaan binnen het domein | ✅               | Elke ligplaats heeft een locatie, een vergunninghouder en een type vaartuig    |
| Kan in meervoud bestaan                   | ✅               | 482 recreatieve + 37 commerciële ligplaatsvergunningen, 334 woonboten          |
| Heeft een eigen levenscyclus              | ✅               | Aanwijzing → vergunningverlening → in gebruik → toezicht → eventueel opheffing |
| Heeft relaties met andere concepten       | ✅               | [[Waterobject]], [[Vaartuig]], Nummeraanduiding                                |

Score: 6/6.

## Beschrijving

Een ligplaats is een door de gemeente aangewezen plaats in het water, al dan niet aangevuld met een oeverterrein, bestemd voor het permanent afmeren van een drijvend object voor woon-, bedrijfsmatige of recreatieve doeleinden. Ligplaatsen zijn adresseerbare objecten in de BAG.

De gemeente Utrecht beheert ligplaatsen via de Havenverordening en Havenatlas. Er zijn:
- **334 woonboten** met ligplaatsvergunning (stabiel bestand)
- **482 recreatieve ligplaatsvergunningen** (maximaal bereikt, 70% emissievrij)
- **37 commerciële ligplaatsvergunningen** (passagiersschepen, rondvaartboten)
- **3 reserveligplaatsen** voor noodgevallen (Kruisvaart en Merwedekanaal)

Het ligplaatsenregime is gebaseerd op een vergunningstelsel: zonder ligplaatsvergunning mag geen ligplaats worden ingenomen. De Havenatlas bevat per locatie het aantal, de situering en de maatvoering (rooilijn, maximale hoogte). Nieuwe recreatieve vergunningen worden alleen aan emissievrije vaartuigen uitgegeven.

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| Reserveligplaats | Tijdelijke ligplaats voor noodgevallen (3 stuks in Utrecht) | Ligplaats |

## GGM-bron

> "Een ligplaats is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen plaats in het water al dan niet aangevuld met een op de oever aanwezig terrein of een gedeelte daarvan, die bestemd is voor het permanent afmeren van een voor woon-, bedrijfsmatige of recreatieve doeleinden geschikt drijvend object."
— GGM-entiteit: Ligplaats, beleidsdomein BAG, taakveld 99 Kern

**Matchsterkte: exact.** De GGM BAG-definitie komt volledig overeen met het concept uit het woonbotenbeleid en de Beleidsnota Stadswater.

**GGM-attributen:** identificatie, geconstateerd, status, documentdatum, documentnummer, versie, geometrie, beginGeldigheid, eindGeldigheid, datumIngang, datumEinde.

**GGM-relaties:**
- Ligplaats → AdresseerbaarObject (generalisatie)
- VerblijfadresIngeschrevenNatuurlijkPersoon → Ligplaats (associatie)

## GGM-duplicaten

De GGM-entiteit "Ligplaats" komt voor in 2 beleidsdomeinen:

| Beleidsdomein | GUID | Status |
|---|---|---|
| **BAG** | `EAID_785E3B69_19DA_4952_84A8_592965B9229A` | **primair** — BAG is de bronregistratie voor adresseerbare objecten |
| RSGBPlus | `EAID_F4978264_32A5_4e70_97A8_D142B64400A8` | duplicaat — zelfde concept met domein-geprefixte attribuutnamen (ligplaatsidentificatie, ligplaatsstatus) en minder attributen (geen geometrie, versie, documentvelden); voegt inOnderzoek toe |

Teruggemeld als #59 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## Relaties

| Relatie | Bedrijfsobject | Richting | Bron |
|---|---|---|---|
| associatie | [[Waterobject]] | bidirectioneel | Beleidsnota Stadswater |
| associatie | [[Vaartuig]] | naar-dit-BO | Woonbotenbeleid 2007 |
| generalisatie | AdresseerbaarObject | van-dit-BO | GGM BAG |

## Bedrijfsprocessen

- **Ligplaats aanwijzen**: opnemen in Havenatlas en BAG
- **Ligplaatsvergunningverlening**: verlening, wijziging en intrekking voor recreatieve, commerciële en woonbootligplaatsen
- **Havenbeheer**: beheer van ligplaatszones, op-en-afstapplaatsen en laad-en-losplekken
- **Toezicht en handhaving**: controle op naleving ligplaatsregels en Havenverordening
- **Ligplaats opheffen**: intrekken bij infrastructuurwijziging of beleidswijziging

## Bedrijfsfuncties

- Havendienst
- BAG-beheer
- Vergunningverlening
- Handhaving


## Subtypes

- **Reserveligplaats** — Tijdelijke ligplaats voor noodgevallen zoals kade-onderhoud of verplaatsing.

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bag-2018]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/bomenbeleid-utrecht]]
- [[Wiki/Bronsamenvattingen/Milieu/groenstructuurplan-utrecht-2007]]
- [[Wiki/Bronsamenvattingen/Milieu/actualisatie-groenstructuurplan-2017-2030]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/nota-beheer-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kadernota-kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/openbare-ruimte-bing]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/visie-speelruimte-utrecht]]
