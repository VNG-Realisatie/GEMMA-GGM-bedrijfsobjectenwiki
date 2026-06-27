---
type: bedrijfsobject
naam: Woonboot
domein: [Wonen]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Vaartuig
ggm_guid: EAID_D12123D3_D62D_4978_B7D4_8405F00A0D6A
ggm_uml_type: Class
ggm_beleidsdomein: VTH
ggm_taakveld: "1 Veiligheid en Vergunningen"
ggm_diagram: ["Objecten bij Vergunningaanvraag"]
ggm_diagram_ids: ["EAID_C9CE09B7_32EF_40eb_9C82_7FD6EDEA1D9E"]
ggm_definitie: "Een zee- of binnenvaartuig, tot de vaart gebruikt of bestemd, daaronder begrepen drijvende werktuigen, zoals baggerwerktuigen, kranen, bokken, elevators, alsmede woonschepen, glijboten en ponten."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam: Vaartuig
ggm_gemma_guid: 3d86eebe-43ff-498e-9f8c-7c77a35f8730
ggm_gemma_definitie: "Een zee- of binnenvaartuig, tot de vaart gebruikt of bestemd, daaronder begrepen drijvende werktuigen, zoals baggerwerktuigen, kranen, bokken, elevators, alsmede woonschepen, glijboten en ponten."
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: business-object
ggm_gemma_url: https://gemmaonline.nl/index.php/GEMMA2/0.9/id-3d86eebe-43ff-498e-9f8c-7c77a35f8730
ggm_gemma_bron:
ggm_gemma_alternate_name:

bo_definitie: "Drijvend object bestemd voor permanente bewoning op een aangewezen ligplaats, met gemeentelijke vergunningplicht voor situering en maatvoering."
bo_subtypes:
  - naam: "Woonark"
    omschrijving: "Betonnen bak met opbouw in het water, niet varend."
    ggm_entiteit: Vaartuig
    ggm_guid: EAID_D12123D3_D62D_4978_B7D4_8405F00A0D6A
    ggm_attribuut: type
  - naam: "Varend schip"
    omschrijving: "Schip met originele romp, ontworpen om te varen. Bij vervanging door een ark geldt max 18 meter."
    ggm_entiteit: Vaartuig
    ggm_guid: EAID_D12123D3_D62D_4978_B7D4_8405F00A0D6A
    ggm_attribuut: type
  - naam: "Historisch schip"
    omschrijving: "Woonboot of bedrijfsvaartuig ≥50 jaar oud, met beschermingsregime in aangewezen zones."
    ggm_entiteit: Vaartuig
    ggm_guid: EAID_D12123D3_D62D_4978_B7D4_8405F00A0D6A
    ggm_attribuut: type
  - naam: "Schark"
    omschrijving: Historisch schip met originele romp en (deels) vervangen eenlaags houten opbouw.
    ggm_entiteit: Vaartuig
    ggm_guid: EAID_D12123D3_D62D_4978_B7D4_8405F00A0D6A
    ggm_attribuut: type
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Ligplaats]]"
    richting: van-dit-BO
    kardinaliteit: "1..1"
    beschrijving: "Een woonboot neemt een ligplaats in"
bedrijfsprocessen: [ligplaatsvergunning verlenen, maatvoering toetsen, handhaving woonboten, vervanging woonboot beoordelen]
bedrijfsfuncties: [Havendienst, Vergunningverlening, Handhaving]
---

## BO-criteria toetsing

| # | Criterium | |
|---|---|---|
| 1 | Heeft betekenis binnen het domein | ✅ |
| 2 | Is herkenbaar voor domeinexperts | ✅ |
| 3 | Heeft een eigen bestaan | ✅ |
| 4 | Kan in meervoud bestaan | ✅ |
| 5 | Heeft een eigen levenscyclus | ✅ |
| 6 | Heeft relaties met andere concepten | ✅ |

**Score: 6/6.** Concreet object met 334 exemplaren in Utrecht, eigen levenscyclus (bouw, verhoging, vervanging, verwijdering), eigen maatvoeringsregels en vergunningenregime.

## Beschrijving

Een woonboot is een drijvend object bestemd voor permanente bewoning. De gemeente reguleert woonboten via de Havenverordening en Havenatlas. Voor het innemen van een [[Ligplaats]] of voor vergroting is een ligplaatsvergunning vereist.

De maatvoering is gebonden aan regels:
- **Hoogte**: maximaal 4 meter (was 3,50 m), mits minimaal 5 meter tussenruimte aan één zijde
- **Lengte**: bij vervanging maximaal 18 meter (uitzondering: varende schepen mogen door varende schepen met gelijke of kortere lengte)
- **Breedte**: bepaald door een rooilijn in het water (5–8 m uit oeverlijn), vastgelegd in de Havenatlas

Er zijn circa 334 woonboten in de gemeente Utrecht. Het bestand is al 15+ jaar stabiel.

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| Woonark | Betonnen bak met opbouw in het water, niet varend | Vaartuig |
| Varend schip | Schip ontworpen om te varen; bij vervanging door ark geldt max 18 m | Vaartuig |
| Historisch schip | Woonboot of bedrijfsvaartuig ≥50 jaar oud, met beschermingsregime in drie zones | Vaartuig |
| Schark | Historisch schip met originele romp en vervangen houten opbouw | Vaartuig |

Historische schepen worden beschermd in drie aangewezen zones: Keulsekade (Merwedekanaal), Vechtdijk (Vecht) en Oosterkade (Vaartsche Rijn). Bij vervanging in deze zones geldt dat historische boten altijd door historische boten worden vervangen.

## GGM-bron

> "Een zee- of binnenvaartuig, tot de vaart gebruikt of bestemd, daaronder begrepen drijvende werktuigen, zoals baggerwerktuigen, kranen, bokken, elevators, alsmede woonschepen, glijboten en ponten."
— GGM-entiteit: Vaartuig, beleidsdomein VTH, taakveld 1 Veiligheid en Vergunningen

**Matchsterkte: sterk.** Vaartuig is de generalisatie; de definitie noemt "woonschepen" expliciet. Het GGM kent geen apart objecttype voor woonboten — Vaartuig is het brede containerbegrip. De GGM-attributen (naamVaartuig, registratienummer, kleur, lengte, breedte, hoogte) sluiten goed aan op de maatvoeringskenmerken uit het woonbotenbeleid.

## BO-definitie

De GGM-definitie van Vaartuig is breder dan het BO Woonboot: het omvat ook baggerwerktuigen, kranen, bokken, elevators, glijboten en ponten. Het BO Woonboot beperkt zich tot drijvende objecten bestemd voor permanente bewoning (inclusief historische bedrijfsvaartuigen die als woonboot worden gebruikt).

**GEMMA-definitie:** Drijvend object bestemd voor permanente bewoning op een aangewezen ligplaats, met gemeentelijke vergunningplicht voor situering en maatvoering.

## Relaties

| Relatie | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Ligplaats]] | van-dit-BO | 1..1 | Een woonboot neemt een ligplaats in | beleidsbronnen |

## Bedrijfsprocessen

- Ligplaatsvergunning verlenen
- Maatvoering toetsen (hoogte, lengte, breedte)
- Vervanging woonboot beoordelen
- Handhaving woonboten

## Bedrijfsfuncties

- Havendienst
- Vergunningverlening
- Handhaving


## Subtypes

- **Woonark** — Betonnen bak met opbouw in het water, niet varend.
- **Varend schip** — Schip met originele romp, ontworpen om te varen. Bij vervanging door een ark geldt max 18 meter.
- **Historisch schip** — Woonboot of bedrijfsvaartuig ≥50 jaar oud, met beschermingsregime in aangewezen zones.
- **Schark** — Historisch schip met originele romp en (deels) vervangen eenlaags houten opbouw.

## Bronnen

- [[Wiki/Bronsamenvattingen/Wonen/beleidsnota-wonen-utrecht]]
- [[Wiki/Bronsamenvattingen/Wonen/huisvestingsverordening-utrecht]]
- [[Wiki/Bronsamenvattingen/Wonen/nadere-regel-huisvestingsverordening]]
- [[Wiki/Bronsamenvattingen/Wonen/beleidsregel-huisvestingsverordening]]
- [[Wiki/Bronsamenvattingen/Wonen/actieplan-betaalbare-koopwoningen]]
- [[Wiki/Bronsamenvattingen/Wonen/actieplan-middenhuur]]
- [[Wiki/Bronsamenvattingen/Wonen/werkwijze-extra-woningen]]
- [[Wiki/Bronsamenvattingen/Wonen/woonboten-utrecht]]
- [[Wiki/Bronsamenvattingen/Wonen/woonbotenbeleid-utrecht-2007]]
- [[Wiki/Bronsamenvattingen/Wonen/historische-schepen-utrecht-2015]]
