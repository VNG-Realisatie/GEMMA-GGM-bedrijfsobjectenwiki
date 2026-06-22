---
type: bedrijfsobject
naam: Geluidzone
domein: [geluid]
archimate_type: "business-object"
grondslag: procesobject
ggm_entiteit: ""
ggm_beleidsdomein: ""
ggm_guid: ""
ggm_uml_type: ""
ggm_taakveld: ""
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: ""
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "Afgebakend gebied rond een industrieterrein waarbinnen de cumulatieve geluideffecten van alle bedrijven worden beheerst via omgevingswaarden."
bedrijfsprocessen: [vergunningverlening, omgevingsplan, geluidkartering]
bedrijfsfuncties: [milieubeheer, ruimtelijke ordening]
relaties:
  - type: associatie
    bedrijfsobject: "[[Geluidbron]]"
    richting: "naar-dit-BO"
    kardinaliteit: "1..*"
    beschrijving: Industriële geluidbronnen liggen binnen de zone
  - type: associatie
    bedrijfsobject: "[[Geluidgevoelig gebouw]]"
    richting: "naar-dit-BO"
    kardinaliteit: "*..*"
    beschrijving: Geluidgevoelige gebouwen binnen of nabij de zone worden beschermd
---

## BO-criteria toetsing

| Criterium | Toepassing |
|---|---|
| Betekenis binnen het domein | Ja — beheersing van cumulatief industriegeluid is wettelijke verplichting |
| Herkenbaar voor domeinexperts | Ja — wettelijk begrip, overgenomen uit Wet geluidhinder naar Omgevingswet |
| Eigen bestaan | Ja — een geluidzone bestaat als afgebakend gebied met eigen grenswaarden |
| Meervoud | Ja — de gemeente heeft meerdere industrieterreinen met geluidzones |
| Eigen levenscyclus | Ja — zones worden vastgesteld, gewijzigd (bij uitbreiding terrein) of opgeheven |
| Relaties | Ja — met industrieterreinen, geluidbronnen, geluidgevoelige gebouwen, omgevingsplan |

## Beschrijving

Een geluidzone is een afgebakend gebied rond een industrieterrein waar zogeheten "grote lawaaimakers" zijn toegestaan. Binnen de zone worden de cumulatieve geluideffecten van alle bedrijven samen beheerst. De grenswaarden worden als omgevingswaarden in het omgevingsplan vastgelegd.

Met de overgang naar de Omgevingswet is de rekenmethodiek gewijzigd, wat in sommige situaties tot iets meer geluidruimte voor bedrijven leidt. De gemeente ziet vooralsnog geen aanleiding om het systeem te wijzigen.

> "Voor de wat grotere industrieterreinen, waar zogeheten 'grote lawaaimakers' mogen komen, geldt een systeem dat als doel heeft om de cumulatieve geluideffecten van alle bedrijven bij elkaar beheersbaar te houden." (Beleidsnota §2.3)

Bedrijven met informatie- of meldingsplichten moeten voldoen aan maximaal 50 dB(A) etmaalwaarde op 50 meter.

## Procesbron

Artefact dat in de wet- en regelgeving voor industriegeluid centraal staat. Het GGM kent Parkeerzone als vergelijkbaar concept (afgebakend gebied met specifieke regels) maar heeft geen Geluidzone. Zie [[Wiki/Bronsamenvattingen/geluid/beleidsnota-geluid-en-trillingen|Beleidsnota Geluid en Trillingen]].

## Relaties

- Bevat → [[Geluidbron]] (industriële bronnen liggen binnen de zone)
- Beschermt → [[Geluidgevoelig gebouw]] (gebouwen binnen/nabij de zone worden beschermd)


## Bronnen

- [[Wiki/Bronsamenvattingen/geluid/beleidsnota-geluid-en-trillingen]]

## Terugmelding GGM

Potentieel hiaat: het GGM kent Parkeerzone maar geen Geluidzone. Structureel vergelijkbaar concept (afgebakend gebied met specifieke normen). Nader te beoordelen of terugmelding zinvol is.
