---
type: element
naam: Publiekrechtelijke Beperking
onderwerp: [Basisregistraties, BRK]
archimate_type: business-object
grondslag: procesobject

ggm_entiteit:
ggm_guid:
ggm_uml_type:
ggm_beleidsdomein:
ggm_taakveld:
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie:
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

ggm_duplicaat_entiteiten: []

bo_definitie: "Een door een bestuursorgaan opgelegde beperking op een onroerende zaak, ingeschreven in de BRK-PB."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Kadastraal Perceel]]"
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Een publiekrechtelijke beperking beperkt een of meer kadastrale objecten"
  - type: associatie
    bedrijfsobject: "[[Stuk]]"
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Een publiekrechtelijke beperking is gebaseerd op ingeschreven brondocumenten (besluiten)"
bedrijfsprocessen:
  - Monumentaanwijzing
  - Milieubeperking
  - Voorkeursrecht Wvg
  - WKPB-registratie
bedrijfsfuncties:
  - Ruimtelijke ordening
  - Erfgoed
  - Milieu
  - Handhaving
---

## BO-criteria toetsing

6/6 criteria. Publiekrechtelijke beperking is een concreet besluit van een bestuursorgaan, met eigen levenscyclus (oorspronkelijk besluit → wijziging → beëindiging/herroeping), meervoudig, eigen identificatie in BRK-PB, en relaties met kadastrale objecten en stukken. De gemeente is zelf bronhouder voor gemeentelijke beperkingen.

## Beschrijving

Een publiekrechtelijke beperking is een door een bestuursorgaan opgelegd besluit dat de rechten op een onroerende zaak beperkt. Sinds de wetswijziging WKPB van 2020 schrijven alle bestuursorganen — waaronder gemeenten — hun beperkingsbesluiten in bij de BRK-PB (Publiekrechtelijke Beperkingen). De gemeente is bronhouder voor gemeentelijke beperkingen zoals:
- Aanwijzing als gemeentelijk monument
- Milieuverordeningen
- Voorkeursrecht gemeente (Wvg)
- Sloopverbod

Andere bestuursorganen (provincie, waterschap, rijk) leggen ook beperkingen op die op kadastrale objecten in de gemeente rusten. Het werkingsgebied van een beperking kan worden aangeduid via BRK-objecten (percelen), BAG-objecten, BGT-objecten of een vrije contour (GML).

De essentialia van een beperkingsbesluit zijn: grondslag (wetsartikel), bestuursorgaan, werkingsgebied, ingangsdatum en eventueel beëindigingsdatum.

## GGM-bron

Geen GGM-match gevonden. Publiekrechtelijke Beperking is een **GGM-hiaat**.

Het GGM modelleert wel een `KadastraleOnroerendeZaakAantekening` (EAID_0BC18F79) die publiekrechtelijke beperkingen als aantekeningtype kan bevatten, maar de Publiekrechtelijke Beperking zelf — met eigen levenscyclus, werkingsgebied en bronhouderschapsrol — is niet als apart objecttype gemodelleerd.

## Relaties

| Relatie | Richting | BO | Kardinaliteit | Bron |
|---|---|---|---|---|
| beperkt | van-dit-BO | [[Kadastraal Perceel]] / [[Appartementsrecht]] | 1..* | BRK Catalogus |
| gebaseerd op | van-dit-BO | [[Stuk]] | 1..* | BRK Catalogus |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-brk]]

## Terugmelding GGM

Publiekrechtelijke Beperking ontbreekt als objecttype in het GGM. Data-object met eigen identificatie, levenscyclus en bronhouderschapsrol (gemeente). Wettelijke basis: WKPB / Kadasterwet. Past in beleidsdomein RSGBPlus (99 Kern). Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
