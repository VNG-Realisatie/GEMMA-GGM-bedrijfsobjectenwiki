---
type: bedrijfsobject
naam: Geluidgevoelig gebouw
domein: [geluid]
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

gemma_definitie: "Gebouw waarvoor wettelijke geluidnormen gelden, zoals een woning, school of zorginstelling."
bronnen:
  - [[Wiki/Bronsamenvattingen/geluid/beleidsnota-geluid-en-trillingen]]
relaties:
  - type: associatie
    bedrijfsobject: [[Geluidbron]]
    richting: van-dit-BO
    kardinaliteit: "*..*"
    beschrijving: Wordt belast door geluidbronnen
  - type: associatie
    bedrijfsobject: [[Stil gebied]]
    richting: naar-dit-BO
    kardinaliteit: "*..*"
    beschrijving: Kan grenzen aan een stil gebied
bedrijfsprocessen: [ruimtelijke planvorming, vergunningverlening, maatregelenonderzoek]
bedrijfsfuncties: [ruimtelijke ordening, milieubeheer, bouwen en wonen]
---

## BO-criteria toetsing

| Criterium | Toepassing |
|---|---|
| Betekenis binnen het domein | Ja — de bescherming van geluidgevoelige gebouwen is het kerndoel van het geluidbeleid |
| Herkenbaar voor domeinexperts | Ja — wettelijk begrip uit de Omgevingswet, dagelijks gebruikt bij plantoetsing |
| Eigen bestaan | Ja — een gebouw is geluidgevoelig onafhankelijk van specifieke geluidbronnen |
| Meervoud | Ja — duizenden geluidgevoelige gebouwen in de gemeente |
| Eigen levenscyclus | Ja — status verandert bij functiewijziging (kantoor→woning), sloop of nieuwbouw |
| Relaties | Ja — met geluidbronnen, geluidzones, geluidschermen, luwe gevels |

## Beschrijving

Een geluidgevoelig gebouw is een gebouw waarvoor de Omgevingswet en het Besluit kwaliteit leefomgeving (Bkl) geluidnormen stellen. Dit betreft woningen, onderwijsgebouwen, gezondheidszorggebouwen en kinderopvanglocaties. Bij nieuwe geluidgevoelige gebouwen in geluidbelaste gebieden stelt de gemeente Utrecht aanvullende eisen:

- Elke nieuwe woning moet een geluidluwe gevel krijgen (alle bronsoorten onder standaardwaarde)
- Minimaal 30% van de verblijfsruimten aan de luwe zijde
- Ten minste één buitenruimte met geluid maximaal 5 dB boven de standaardwaarde
- Slaapkamers bij voorkeur aan de luwe zijde

> "Elke nieuwe woning moet een geluidluwe zijde krijgen; een gevel is luw als deze voor alle bronsoorten voldoet aan de standaardwaarde." (Beleidsnota §1.4)

Bij vervangende nieuwbouw en transformatie gelden dezelfde grenswaarden als bij nieuwbouw, met een 5 dB soepelere eis voor de luwe gevel.

## Procesbron

Het GGM modelleert gebouwen (Pand, Gebouw, Verblijfsobject) maar niet de geluidgevoeligheidsclassificatie. De aanduiding "geluidgevoelig" is een beleidsmatige kwalificatie op basis van de functie van het gebouw. Zie [[Wiki/Bronsamenvattingen/geluid/beleidsnota-geluid-en-trillingen|Beleidsnota Geluid en Trillingen]].

## Relaties

- Belast door → [[Geluidbron]] (ontvangt geluid van bronnen)
- Beschermd door → [[Geluidscherm]] (scherm vermindert geluidbelasting)
- Ligt in/nabij → [[Stil gebied]] (gebouwen profiteren van stille gebieden)
- Ligt in → [[Geluidzone]] (gebouwen binnen een geluidzone hebben aanvullende bescherming)

## Terugmelding GGM

Potentieel hiaat: het GGM kent Gebouw en Pand, maar niet de classificatie als "geluidgevoelig" met bijbehorende normen en eisen. Nader te beoordelen of dit een apart dataobject is of een attribuut op bestaande gebouwentiteiten.
