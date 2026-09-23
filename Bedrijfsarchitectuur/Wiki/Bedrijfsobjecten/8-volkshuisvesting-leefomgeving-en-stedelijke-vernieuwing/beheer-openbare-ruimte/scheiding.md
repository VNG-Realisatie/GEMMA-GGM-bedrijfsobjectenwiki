---
type: element
naam: Scheiding
onderwerp: [Beheer Openbare Ruimte]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Scheiding"
ggm_guid: EAID_C538C222_0FA4_43EE_BF06_9512A484A57
ggm_uml_type: Class
ggm_beleidsdomein: "Beheer Openbare Ruimte"
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram: [Hoofdobjecten IMBOR en Geo-object]
ggm_diagram_ids: [EAID_E3EBD7A0_35C4_4bf4_BD01_6D97AD0B8BF3]
ggm_definitie: "Kunstmatig, meestal lineair obstakel met een werende functie."
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
  - entiteit: Scheiding
    guid: EAID_A637379F_6E1D_47aa_AE75_3E22FE0DC814
    beleidsdomein: RSGBPlus
    taakveld: "99 Kern"
    afwijkende_attributen: "RSGBPlus gebruikt domein-geprefixte namen (identificatieScheiding, statusScheiding, geometrieScheiding met LOD0-3-varianten, datumBeginGeldigheidScheiding/datumEindeGeldigheidScheiding — topografische BGT-registratievelden). Beheer Openbare Ruimte (IMBOR) heeft beheerattributen: aanleghoogte, breedte, hoogte, lengte, scheidingMateriaal, verplaatsbaar, leverancier, objectnummer, jaarOnderhoudUitgevoerd."

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Scheiding** (beleidsdomein Beheer Openbare Ruimte) als directe tegenhanger. Daarnaast is **Scheiding** (beleidsdomein RSGBPlus, BGT) als duplicaat gekoppeld — zie ggm_duplicaat_entiteiten.
bo_definitie: "Kunstmatig, meestal lineair obstakel met een werende functie, zoals een hekwerk of keermuur, dat de gemeente in de openbare ruimte beheert."
bo_toelichting:
bo_relaties: []
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis binnen het beheerdomein (afscherming en afbakening in de openbare ruimte), herkenbaar voor domeinexperts (hekwerk, keermuur, afrastering), eigen bestaan (zelfstandig beheerobject met objectnummer), meervoud (talrijke scheidingen per gemeente), eigen levenscyclus (aanleg, onderhoud, vervanging — jaarOnderhoudUitgevoerd), relaties (materiaal, afmetingen, leverancier).

## Beschrijving

Een scheiding is een kunstmatig, meestal lineair obstakel met een werende functie — bijvoorbeeld een hekwerk, keermuur of afrastering — dat de gemeente in de openbare ruimte plaatst en onderhoudt.

Dit begrip komt in het GGM twee keer voor met identieke definitie: als IMBOR-beheerobject in Beheer Openbare Ruimte (dit BO, gekozen als primair omdat het de beheer-/onderhoudscontext van dit domein is) en als topografisch registratieobject in RSGBPlus/BGT (zie GGM-duplicaten). Beide GUID's zijn tot nu toe zonder BO-pagina; dit is de eerste vastlegging.

## GGM-bron

> "Kunstmatig, meestal lineair obstakel met een werende functie." (GGM, entiteit Scheiding, beleidsdomein Beheer Openbare Ruimte)

- **Entiteit:** Scheiding
- **Beleidsdomein:** Beheer Openbare Ruimte (taakveld 8)
- **Attributen:** aanleghoogte, breedte, hoogte, jaarOnderhoudUitgevoerd, lengte, leverancier, objectnaam, objectnummer, oppervlakte, scheidingMateriaal, verplaatsbaar
- **Matchsterkte:** exact

## GGM-duplicaten

De GGM-entiteit "Scheiding" komt voor in 2 beleidsdomeinen:

| Beleidsdomein | GUID | Status |
|---|---|---|
| **Beheer Openbare Ruimte** | `EAID_C538C222_0FA4_43EE_BF06_9512A484A57` | **primair** — gekozen omdat dit BO de beheer-/onderhoudscontext beschrijft waarin de gemeente over scheidingen praat |
| RSGBPlus (BGT) | `EAID_A637379F_6E1D_47aa_AE75_3E22FE0DC814` | duplicaat — topografische registratievariant (identieke definitie), zie ook [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bgt-1.2|Gegevenscatalogus BGT 1.2]] |

Attribuutverschil: RSGBPlus draagt BGT-registratievelden (status, geometrie in LOD0-3, geldigheidsdatums); Beheer Openbare Ruimte draagt fysieke beheerattributen (materiaal, afmetingen, leverancier, onderhoudsjaar).

Teruggemeld als #100 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## Relaties

Geen relaties met andere BO's in de wiki op dit moment.

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bgt-1.2]]
