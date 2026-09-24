---
type: element
naam: Natuurlijk Persoon
onderwerp: [Basisregistraties, RSGBPlus]
archimate_type: business-object
grondslag: ggm-entiteit

# GGM-velden
ggm_entiteit: NatuurlijkPersoon
ggm_guid: EAID_9F4E12E4_B228_4931_AC83_1B1F60958A89
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram:
  - "Kern:Personen"
  - "Diagram Griffie"
  - "Sociaal Domein Beschikking en Voorziening: Domain Objects"
  - "Relatie BRP en BAG"
ggm_diagram_ids: []
ggm_definitie: "Een INGESCHREVEN PERSOON of ANDER NATUURLIJK PERSOON"
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

# GEMMA-waarden
ggm_gemma_naam: NatuurlijkPersoon
ggm_gemma_guid: "cd27cd50-1721-4870-a292-ea0f24d1ada4"
ggm_gemma_definitie: "Een INGESCHREVEN PERSOON of ANDER NATUURLIJK PERSOON"
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-cd27cd50-1721-4870-a292-ea0f24d1ada4"
ggm_gemma_bron:
ggm_gemma_alternate_name:

ggm_duplicaat_entiteiten: []

analyse_ggm_dekking: ""
bo_definitie: "Individueel menselijk wezen, ingeschreven in de Basisregistratie Personen of anderszins van belang voor de gemeentelijke taakuitoefening."
bo_toelichting: "Natuurlijk Persoon is de persoonskant-specialisatie van [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/rechtspersoon|Rechtspersoon]] (het complement van [[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon|Niet-Natuurlijk Persoon]], de organisatiekant). De verzameling omvat zowel personen die ingeschreven zijn in de BRP (GBA/RNI) — zie [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon|Ingeschreven Persoon]] — als andere natuurlijke personen, woonachtig in binnen- of buitenland, die niet in de BRP staan maar wel relevant zijn voor de gemeente (bijvoorbeeld buitenlanders die belastingplichtig zijn voor een gemeentelijke belasting)."
bo_subtypes:
  - naam: Ander Natuurlijk Persoon
    omschrijving: "Natuurlijk persoon, niet ingeschreven in de BRP (GBA/RNI), woonachtig in Nederland of het buitenland, van belang voor de gemeentelijke taakuitoefening"
    ggm_entiteit: NatuurlijkPersoon
    ggm_guid: EAID_9F4E12E4_B228_4931_AC83_1B1F60958A89
    ggm_attribuut: ""
bo_via_kandidaten: []
bo_synoniemen: []
bo_homoniemen: []
element_tegenhangers: []
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/rechtspersoon|Rechtspersoon]]"
    richting: naar-dit-BO
    kardinaliteit:
    beschrijving: "Natuurlijk Persoon is de persoonskant-specialisatie van Rechtspersoon; Niet-Natuurlijk Persoon is de organisatiekant"
  - type: generalisatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon|Ingeschreven Persoon]]"
    richting: van-dit-BO
    kardinaliteit:
    beschrijving: "Ingeschreven Persoon is de BRP-specialisatie van Natuurlijk Persoon"
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

| Criterium | Oordeel |
|---|---|
| Heeft betekenis binnen het onderwerp | ✅ Generalisatiewortel van elke individuele persoon waarmee de gemeente te maken heeft |
| Herkenbaar voor domeinexperts | ✅ "Natuurlijk persoon" (tegenover niet-natuurlijk persoon/rechtspersoon) is standaard juridisch begrip |
| Heeft een eigen bestaan binnen het onderwerp | ✅ Bestaat onafhankelijk van de vraag of iemand wel of niet in de BRP is ingeschreven |
| Kan in meervoud bestaan | ✅ Elke ingezetene en elke relevante niet-ingeschrevene |
| Heeft een eigen levenscyclus | ✅ Geboorte/overlijden (Ingeschreven Persoon) resp. eigen begin/einde-registratie (Ander Natuurlijk Persoon) |
| Heeft relaties met andere concepten | ✅ Rechtspersoon (generalisatie), Ingeschreven Persoon (specialisatie), en via Rechtspersoon dezelfde domeinrollen als Niet-Natuurlijk Persoon |

6/6 — sterke BO. Consistent met de eerder herziene beoordeling van [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/rechtspersoon|Rechtspersoon]]: dit sluit de asymmetrie met de al bestaande [[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon|Niet-Natuurlijk Persoon]] (dezelfde structuurpositie, wél al een BO).

## Beschrijving

Natuurlijk Persoon is de RSGB-generalisatie van [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon|Ingeschreven Persoon]] (personen met een persoonslijst in de BRP) en Ander Natuurlijk Persoon (personen die niet in de BRP staan maar wel relevant zijn voor de gemeente, zoals in het buitenland woonachtige belastingplichtigen). Het is, samen met [[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon|Niet-Natuurlijk Persoon]], een van de twee specialisaties van [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/rechtspersoon|Rechtspersoon]].

De gemeente heeft in vrijwel elk domein met natuurlijke personen te maken — als ingezetene, vergunningaanvrager, belastingplichtige, functionaris van een niet-natuurlijk persoon, betrokkene in het sociaal domein — waarbij het merendeel via Ingeschreven Persoon loopt. Ander Natuurlijk Persoon vangt de resterende gevallen op: personen die de gemeente relevant vindt zonder dat zij (nog) in de BRP staan.

## Specialisaties

| Specialisatie | Omschrijving | GGM-entiteit |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | Persoon met persoonslijst in de BRP | Ingezetene (via IngeschrevenPersoon) |

Ander Natuurlijk Persoon heeft geen eigen GGM-entiteit (alleen tekstueel beschreven in RSGB Deel II, niet als aparte klasse gemodelleerd) en is daarom als subtype vastgelegd, niet als aparte BO-pagina — zie `bo_subtypes`.

## GGM-bron

> "Een INGESCHREVEN PERSOON of ANDER NATUURLIJK PERSOON"

- **Entiteit:** NatuurlijkPersoon
- **Package:** RSGB Model > Model Kern RSGB
- **Attributen:** burgerservicenummer, achternaam, geslachtsnaam, voornamen, geslachtsaanduiding, datumGeboorte, geboorteplaats, geboorteland, datumOverlijden, overlijdensplaats, landOverlijden, nationaliteit, academischeTitel, adellijkeTitelOfPredikaat, e.a.
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | BO | Beschrijving | Bron |
|---|---|---|---|---|
| specialisatie van | → | [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/rechtspersoon\|Rechtspersoon]] | Persoonskant van Rechtspersoon | GGM |
| specialisatie | ← | [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | BRP-registratie van Natuurlijk Persoon | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/rsgb-deel-ii-specificaties]]
