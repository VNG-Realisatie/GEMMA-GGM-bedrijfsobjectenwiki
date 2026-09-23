---
type: element
naam: Tunneldeel
onderwerp: [Basisregistraties, BGT]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Tunneldeel
ggm_guid: EAID_EE07AE43_1825_4377_9984_9636AB015C11
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram: ["Hoofdobjecten IMGeo en Beheerobjecten", "Overige geo objecten op hoofdlijnen", "Overige geo objecten met attributen", "TUNNELDEEL"]
ggm_diagram_ids: ["EAID_4896574A_C4DD_4b27_A3B9_4481F4B29CCB", "EAID_66FB74D4_C7D8_40b2_8512_B690FC8B2575", "EAID_AF86D21D_8F8E_4f0d_A1FA_FE7824E99EAD", "EAID_224C01A6_60E9_4eed_A869_90E9F9412C4E"]
ggm_definitie: "Onderdeel van een kunstmatig aangelegde, kokervormige onderdoorgang, dat essentieel is voor de constructie."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst: BGT

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

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Tunneldeel** als directe tegenhanger.
bo_definitie: "Onderdeel van een kunstmatig aangelegde, kokervormige onderdoorgang dat essentieel is voor de constructie."
bo_toelichting:
bo_relaties: []
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis binnen de BGT (registratie van tunnelconstructies), herkenbaar voor domeinexperts (fietstunnel, wegtunnel), eigen bestaan (zelfstandig geregistreerd bouwwerkdeel), meervoud (meerdere tunnels per gemeente), eigen levenscyclus (datumBeginGeldigheid/datumEindeGeldigheid), relaties (geometrie).

## Beschrijving

Een tunneldeel is een essentieel onderdeel van een kunstmatig aangelegde, kokervormige onderdoorgang — bijvoorbeeld een fiets- of wegtunnel. Het is een concreet subtype van het abstracte BGT-objecttype OverigeConstructie, naast [[Wiki/Bedrijfsobjecten/99-kern/bgt/overbruggingsdeel|Overbruggingsdeel]] en [[Wiki/Bedrijfsobjecten/99-kern/bgt/kunstwerkdeel|Kunstwerkdeel]].

## GGM-bron

> "Onderdeel van een kunstmatig aangelegde, kokervormige onderdoorgang, dat essentieel is voor de constructie." (GGM, entiteit Tunneldeel, beleidsdomein RSGBPlus)

- **Entiteit:** Tunneldeel
- **Beleidsdomein:** RSGBPlus (taakveld 99 Kern)
- **Attributen:** identificatieTunneldeel, statusTunneldeel, relatieveHoogteliggingTunneldeel, geometrieTunneldeel, datumBeginGeldigheidTunneldeel, datumEindeGeldigheidTunneldeel
- **Matchsterkte:** exact

## Relaties

Geen relaties met andere BO's in de wiki op dit moment, buiten de gedeelde afkomst uit het abstracte objecttype OverigeConstructie.

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bgt-1.2]]
