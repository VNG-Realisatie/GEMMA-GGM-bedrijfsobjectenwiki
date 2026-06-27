---
type: bedrijfsobject
naam: Loonkostensubsidie
onderwerp: [werk en inkomen]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Loonkostensubsidie
ggm_guid: EAID_F600A89B_EE8E_4b86_949E_F15E9328EB83
ggm_uml_type: Class
ggm_beleidsdomein: Werk
ggm_taakveld: "6 Sociaal Domein"
ggm_diagram: [Detaildiagram Werk]
ggm_diagram_ids: [EAID_F93A23D7_BF68_46e0_A6D4_96508ACED81E]
ggm_definitie: "Een tegemoetkoming aan een werkgever voor het in dienst nemen van een werknemer met verminderde loonwaarde."
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

bo_definitie: "Een tegemoetkoming aan een werkgever voor het in dienst nemen van een werknemer met verminderde loonwaarde."
bo_toelichting: ''
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Re-integratievoorziening]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Re-integratievoorziening kan gepaard gaan met loonkostensubsidie"
  - type: associatie
    bedrijfsobject: "[[Client]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Client (werkzoekende) ontvangt werk met loonkostensubsidie"
bedrijfsprocessen: [loonwaardebepaling, toekenning loonkostensubsidie, betaling loonkostensubsidie, SiSa-verantwoording]
bedrijfsfuncties: [arbeidsparticipatie, inkomensondersteuning]
---

## BO-criteria toetsing

| Criterium | Toets |
|---|---|
| Identificeerbaar | ✅ Per werknemer/werkgever, met loonwaardepercentage en bedrag |
| Levenscyclus | ✅ Loonwaardebepaling → toekenning → periodieke betaling → beëindiging (bij regulier werk of uitstroom) |
| Eigendom/verantwoordelijkheid | ✅ Gemeente verstrekt, betaalt en registreert; rapporteert via SiSa aan Rijksoverheid |
| Bestuurlijk relevant | ✅ Onderdeel van €7,3 mld bijstandsbudget; centraal instrument Participatiewet; saldo beïnvloedt gemeentebegroting |
| Relaties | ✅ Met Werkzoekende/Client, Re-integratievoorziening, werkgever, Doelgroepenregister |
| Persistent | ✅ Geregistreerd in gemeentelijke administratie, CBS re-integratiestatistiek, SiSa-verantwoording |

## Beschrijving

Een loonkostensubsidie is een tegemoetkoming die de gemeente betaalt aan een werkgever die iemand met een arbeidsbeperking in dienst neemt. De subsidie compenseert het verschil tussen de door een gecertificeerde loonwaardedeskundige vastgestelde loonwaarde van de werknemer en het wettelijk minimumloon.

De loonkostensubsidie is een centraal instrument in de Participatiewet. Het budget wordt historisch verdeeld: het gemeentelijk aandeel in enig jaar is gelijk aan de uitgaven aan loonkostensubsidies in het vorige jaar gedeeld door de macro-uitgaven in het vorige jaar. Hierdoor worden uitgaven met één jaar vertraging volledig gecompenseerd. Per extra loonkostensubsidie ontvangt de gemeente ook €7.355 via het cluster Participatie in het gemeentefonds voor uitvoerings- en begeleidingskosten.

Voor grotere gemeenten (>40.000 inwoners) levert de inzet van loonkostensubsidies een structureel financieel voordeel op: de bespaarde bijstandsuitkering (gemiddeld €18.000) wordt slechts gedeeltelijk (gemiddeld 1/3) gecorrigeerd in het bijstandsbudget, terwijl de loonkostensubsidie volledig wordt gecompenseerd.

De loonkostensubsidie wordt ook verstrekt voor medewerkers op een beschutte werkplek. In dat geval ontvangt de gemeente via drie kanalen middelen: de loonkostensubsidie zelf, de integratie-uitkering Participatie, en het cluster Participatie.

## GGM-bron

> "Een tegemoetkoming aan een werkgever voor het in dienst nemen van een werknemer met verminderde loonwaarde."
> — GGM, entiteit *Loonkostensubsidie*, beleidsdomein Werk

**Matchsterkte:** exact — de GGM-entiteit beschrijft precies het concept van de loonkostensubsidie op grond van de Participatiewet.

**Attributen (GGM):** PercentageLoonwaardeWML

## Relaties

| Gerelateerd BO | Relatie | Richting | Bron |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/re-integratievoorziening\|Re-integratievoorziening]] | kan gepaard gaan met | Re-integratievoorziening → Loonkostensubsidie | GGM |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | ontvangt werk met | Client → Loonkostensubsidie | GGM (via Werkzoekende) |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]] | kan aanvullen | Loonkostensubsidie → Inkomensvoorziening | Bron (bij aanvullende bijstandsuitkering) |

## Bedrijfsprocessen

- **Loonwaardebepaling**: gecertificeerde loonwaardedeskundige stelt loonwaarde vast als percentage van WML
- **Toekenning loonkostensubsidie**: gemeente besluit op aanvraag werkgever, berekent subsidiebedrag
- **Betaling loonkostensubsidie**: periodieke betaling aan werkgever
- **SiSa-verantwoording**: opgave uitgaven aan loonkostensubsidies bij Rijksoverheid

## Bedrijfsfuncties

- Arbeidsparticipatie
- Inkomensondersteuning
- Financiële administratie

## Bronnen

- [[Wiki/Bronsamenvattingen/Werk en Inkomen/handreiking-explicitering-budgetten-participatiewet-wsw]]

## Terugmelding GGM

De GGM-entiteit heeft slechts één attribuut (PercentageLoonwaardeWML). In de praktijk registreren gemeenten meer: bedrag, ingangsdatum, einddatum, loonwaardebepaling, betaalperiode, werkgever. De entiteit zou gebaat zijn bij uitbreiding. Daarnaast ontbreekt een expliciete relatie met Werkgever als actor.
