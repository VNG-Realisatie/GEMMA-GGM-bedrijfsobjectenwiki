---
type: bedrijfsobject
naam: Datalek
onderwerp: [Informatiesamenleving]
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

bo_definitie: "Inbreuk in verband met persoonsgegevens: ongeoorloofde toegang, verstrekking, verlies, vernietiging of wijziging van persoonsgegevens."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/verwerkingsactiviteit|Verwerkingsactiviteit]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Datalek treedt op bij een verwerkingsactiviteit"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak|Zaak]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Datalek kan als zaak worden behandeld"
bedrijfsprocessen: [Privacy-compliance, Incidentbeheer]
bedrijfsfuncties: [Informatievoorziening, Privacy, Informatiebeveiliging]
---

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Betekenis | Inbreuk in verband met persoonsgegevens (art. 4 lid 12 AVG) |
| Herkenbaarheid | De gemeente herkent dit als zelfstandig ding — "we hebben een datalek gehad" |
| Eigen bestaan | Verplichte attributen: feiten, aard inbreuk, oorzaak, betrokken gegevens, ontdekkingsmoment, maatregelen, meldtekst |
| Meervoud | Gemeente heeft meerdere datalekken per jaar |
| Levenscyclus | Ontdekking → onderzoek → risico-inschatting → melding AP (72u) → evt. melding betrokkenen → afsluiting → bewaring (min. 1 jaar) |
| Relaties | Met verwerkingsactiviteit (waar lek optrad), AP (melding), betrokkenen (informeren), FG (advies) |

Resultaat: 6/6 — BO.

## Beschrijving

Een datalek is een inbreuk in verband met persoonsgegevens: iemand heeft toegang tot persoonsgegevens zonder dat dit mag of de bedoeling is. Dit omvat ongeoorloofde toegang, verstrekking, verlies, vernietiging of wijziging van persoonsgegevens (art. 4 lid 12 AVG). Voorbeelden: e-mail naar verkeerd adres, kwijtgeraakte USB-stick, laptopdiefsal, inzage door onbevoegde medewerker, onbeschikbaarheid door systeemstoring.

De gemeente is verplicht een administratie bij te houden van **alle** datalekken, ook niet-gemelde. Per incident legt de gemeente vast:
- feiten en aard van de inbreuk
- oorzaak
- betrokken gegevens
- ontdekkingsmoment
- wijze van dichten
- meldtekst aan betrokkenen (indien gemeld)

Minimale bewaartermijn: 1 jaar.

Bij een datalek dat risico oplevert voor rechten en vrijheden: melding bij de AP binnen 72 uur (art. 33 AVG). Bij hoog risico: ook betrokkenen informeren (art. 34 AVG). De risico-inschatting gebeurt via een kans × impact matrix.

Bij een datalek bij een verwerker (externe partij) is de gemeente als verwerkingsverantwoordelijke verantwoordelijk voor de meldplicht. Afspraken hierover worden vastgelegd in de verwerkersovereenkomst.

## Procesbron

Wettelijke grondslag: art. 33-34 Verordening (EU) 2016/679 (AVG), art. 4 lid 12 (definitie).

Zie [[Wiki/Bronsamenvattingen/Informatiesamenleving/factsheet-datalekken-ibd|Factsheet Datalekken — IBD]] voor het gemeentelijke perspectief: meldproces, registratieplicht, risicoafweging, stroomschema.

## Relaties

| Relatie | Richting | Beschrijving |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/verwerkingsactiviteit\|Verwerkingsactiviteit]] | naar-dit-BO | Datalek treedt op bij een verwerkingsactiviteit |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] | naar-dit-BO | Datalek kan als zaak worden behandeld |

Buiten wiki-scope (geen BO):
- **AP** — ontvangt melding binnen 72 uur
- **Betrokkenen** — worden geïnformeerd bij hoog risico
- **FG** — adviseert bij risico-inschatting
- **Verwerker** — informeert gemeente bij datalek in opdracht

## Bedrijfsprocessen

- **Privacy-compliance** — meldplicht datalekken
- **Incidentbeheer** — opsporen, onderzoeken, dichten van datalekken

## Bedrijfsfuncties

- **Informatievoorziening** — eigenaar systemen
- **Privacy** — FG en privacyteam
- **Informatiebeveiliging** — CISO, IBD-contact

## Bronnen

- [[Wiki/Bronsamenvattingen/Informatiesamenleving/factsheet-datalekken-ibd]]

## Terugmelding GGM

Geen GGM-entiteit gevonden. Het GGM bevat geen privacy-/AVG-gerelateerde entiteiten.

Teruggemeld als #71 in [[Wiki/Analyses/ggm-terugmeldingen]].
