---
type: bedrijfsobject
naam: Werkzoekende
onderwerp: [werk en inkomen]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Werkzoekende
ggm_guid: EAID_24A45AF2_13FF_491d_9E3D_F8D8113F28E1
ggm_uml_type: Class
ggm_beleidsdomein: Werk
ggm_taakveld: "6 Sociaal Domein"
ggm_diagram: [Detaildiagram Werk, Diagram Client en Werkzoekende]
ggm_diagram_ids: [EAID_F93A23D7_BF68_46e0_A6D4_96508ACED81E, EAID_793F0822_F942_4948_A3EA_24C60FCAB576]
ggm_definitie: "Een generiek werkprofiel van een persoon waarin diens arbeidspositie, bemiddelbaarheid en begeleidingsbehoefte worden vastgelegd, als basis voor begeleiding naar arbeid."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: GGM

ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""

bo_definitie: "Een generiek werkprofiel van een persoon waarin diens arbeidspositie, bemiddelbaarheid en begeleidingsbehoefte worden vastgelegd, als basis voor begeleiding naar arbeid."
bo_toelichting: "Centraal object in het domein Werk en Inkomen. Specialisatie van [[Client]]. Het werkprofiel omvat arbeidsmarktkwalificaties, taalbeheersing, opleiding, werkervaring, mobiliteit, beschikbaarheid en bemiddelingstrajecten."
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Client]]"
    richting: naar-dit-BO
    kardinaliteit: ""
    beschrijving: "specialisatie van Client"
  - type: associatie
    bedrijfsobject: "[[Re-integratievoorziening]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "ontvangt re-integratievoorziening(en)"
  - type: associatie
    bedrijfsobject: "[[Loonkostensubsidie]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "via re-integratievoorziening"
  - type: associatie
    bedrijfsobject: "[[Inkomensvoorziening]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "ontvangt inkomensvoorziening(en)"
bedrijfsprocessen: [intake werkzoekende, re-integratiebeoordeling, arbeidstoeleiding, VUM-matching]
bedrijfsfuncties: [arbeidsparticipatie, re-integratie, werkgeversdienstverlening]
---

## BO-criteria toetsing

| Criterium | Toets |
|---|---|
| Betekenis binnen domein | ✅ Centraal concept in Werk en Inkomen; kern van alle arbeidstoeleidingsprocessen |
| Herkenbaar voor domeinexperts | ✅ Kernbegrip voor klantmanagers, werkcoaches en beleidsmedewerkers |
| Eigen bestaan | ✅ Persoon met uitgebreid werkprofiel (25+ componenten) |
| Meervoud | ✅ Honderden tot duizenden per gemeente |
| Levenscyclus | ✅ Inschrijving → actief zoekend → bemiddeld → geplaatst/uitgeschreven |
| Relaties | ✅ Client, Re-integratievoorziening, Loonkostensubsidie, Inkomensvoorziening |

Score: **6/6**

## Beschrijving

Een werkzoekende is een persoon die begeleid wordt naar arbeid door de gemeente of UWV. De gemeente bouwt per werkzoekende een werkprofiel op met arbeidsmarktkwalificaties, taalbeheersing, opleiding, werkervaring, mobiliteit en beschikbaarheid. Op basis van dit profiel worden re-integratievoorzieningen ingezet en vindt matching met vacatures plaats.

In het SUWI-domein is de werkzoekende het centrale uitwisselingsobject: het SGR modelleert alle arbeidstoeleidingsgegevens rond dit profiel. Via VUM (Verbeteren Uitwisseling Matchingsgegevens) worden werkzoekendeprofielen gedeeld over regio- en organisatiegrenzen heen voor betere matching.

## GGM-componenten

GGM-entiteiten die onderdeel zijn van Werkzoekende. Gemodelleerd als aparte entiteiten in het GGM (voor gedetailleerde profielopbouw) maar vormen geen zelfstandig bedrijfsobject.

- **Arbeidsmarktkwalificaties** — klantypering, taalbeheersing mondeling/schriftelijk, werk- en denkniveau
- **Arbeidsvermogen** — inschatting van fysieke, mentale en sociale arbeidscapaciteit
- **Bemiddelingstraject** — traject waarin de persoon begeleid wordt naar passend werk
- **Bemiddelingsberoep** — beoogd beroep voor bemiddeling
- **Bemiddelingsactiviteit** — concrete activiteit om persoon in contact te brengen met werkgever
- **BeschikbaarVoorArbeid** — inzetbaarheid voor arbeid met dagen/uren/opzegtermijn
- **BeschikbaarVoorBemiddeling** — beschikbaarheid voor bemiddeling richting arbeid
- **Mobiliteit** — bereikbaarheid werkplekken, bereidheid verhuizen, vervoermiddel
- **Flexibliteit** — bereidheid tot onregelmatig werk, zwaar werk, onder niveau
- **Voorkeur** — wensen t.a.v. branche, soort baan, werklocatie
- **Opleiding** — gevolgde opleidingen met niveau, status, diploma
- **Werkervaring** — eerdere functies en werkzaamheden
- **Taalbeheersing** — taalniveau per taal (lezen, schrijven, spreken)
- **TaalbeheersingNederlands** — specifiek Nederlands (spreek-, luister-, lees-, schrijf-, gespreksvaardigheid)
- **ZelfredzaamheidScore** — zelfstandigheid op meerdere levensgebieden (ZRM)
- **Doelgroepenregister** — indicatie opname in landelijk register arbeidsbeperking
- **Ontheffing** — vrijstelling van verplichtingen rond arbeidsparticipatie
- **VrijstellingArbeidsplicht** — tijdelijke of structurele vrijstelling van arbeidsplicht
- **DoelReintegratievoorziening** — beoogd effect van ingezette voorziening
- **Vaardigheidsvaststelling** — beoordeling specifieke vaardigheden
- **Rijbewijs /Certificaat** — rijbewijscategorieën en certificaten

## GGM-bron

> "Een generiek werkprofiel van een persoon waarin diens arbeidspositie, bemiddelbaarheid en begeleidingsbehoefte worden vastgelegd, als basis voor begeleiding naar arbeid."

- **Entiteit:** Werkzoekende
- **Beleidsdomein:** Werk (taakveld 6 Sociaal Domein)
- **Attributen:** DatumAanvangWerkzoekende, DatumEindeWerkzoekende
- **Abstract:** Ja (superklasse van Client)
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| specialisatie van [[Client]] | naar dit BO | — | GGM |
| ontvangt [[Re-integratievoorziening\|Re-integratievoorziening]] | van dit BO | 0..* | GGM |
| via [[Loonkostensubsidie]] | van dit BO | 0..* | GGM |
| ontvangt [[Inkomensvoorziening]] | van dit BO | 0..* | bron |

## Bronnen

- [[Wiki/Bronsamenvattingen/Werk en Inkomen/wet-suwi-en-sgr]]
