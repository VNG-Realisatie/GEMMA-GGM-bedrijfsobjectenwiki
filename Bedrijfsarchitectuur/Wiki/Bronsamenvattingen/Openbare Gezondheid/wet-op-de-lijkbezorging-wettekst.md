---
type: bronsamenvatting
titel: "Wet op de lijkbezorging — volledige wettekst"
onderwerp: [Openbare Gezondheid]
datum_ingest: 2026-09-23
---

# Wet op de lijkbezorging — volledige wettekst

Volledige wettekst van de Wet op de lijkbezorging (Wlb, BWBR0005009, versie 2025-07-01, wetten.overheid.nl). Regelt wat mag en moet gebeuren met een lijk (begraving, crematie of andere lijkbezorging), met expliciete gemeentelijke taken en bevoegdheden.

## Samenvatting

**Lijkschouwing en identificatie (art. 3-10a)** — burgemeester en wethouders benoemen een of meer **gemeentelijke lijkschouwers** (uitsluitend forensisch artsen, ingeschreven in een register). De behandelende arts of de gemeentelijke lijkschouwer schouwt het lijk en geeft een verklaring van overlijden af; bij twijfel aan een natuurlijke doodsoorzaak, bij levensbeëindiging op verzoek, of bij een overleden minderjarige volgt een aparte procedure met melding aan officier van justitie resp. regionale toetsingscommissie.

**Verlof tot begraving/crematie (art. 11-15)** — geen begraving of crematie zonder schriftelijk, kosteloos verlof van de ambtenaar van de burgerlijke stand; dat verlof wordt alleen verleend op basis van een verklaring van overlijden of een verklaring van geen bezwaar van de officier van justitie.

**Termijn (art. 16-17)** — begraving/crematie tussen 36 uur en de zesde werkdag na overlijden; de burgemeester kan een andere termijn stellen.

**Overheidszorg (art. 20-22a)** — als niemand voorziet in lijkschouwing/lijkbezorging, draagt de burgemeester daar zorg voor (grondslag voor het bestaande BO Gemeentebegrafenis); kosten komen ten laste van de gemeente, met verhaal op nalatenschap/onderhoudsplichtigen. Bij een besmet lijk kan de burgemeester na GGD-advies maatregelen treffen.

**Begraving (art. 23-48)** — begraving geschiedt op een begraafplaats, in een **algemeen graf** (houder van de begraafplaats bepaalt wie erin wordt begraven) of een **particulier graf** (een **uitsluitend recht op een graf**, voor onbepaalde tijd of minimaal tien jaar, schriftelijk gevestigd, verlengbaar, vervalt bij verwaarloosd onderhoud na een vastgelegde procedure). Elke gemeente heeft verplicht minstens één **gemeentelijke begraafplaats** (art. 33); daarnaast bestaan **bijzondere begraafplaatsen** (kerkgenootschappen, privaatrechtelijke rechtspersonen). De houder van een begraafplaats houdt een openbaar register van begraven lijken. Sluiting en opheffing van begraafplaatsen zijn apart geregeld (art. 43-48), met een verplichte grafrust van twintig jaar na sluiting.

**Crematie (art. 49-66b)** — crematie geschiedt in een **crematorium** (eveneens gemeentelijk of bijzonder, met vergelijkbare vestigings- en registerregels als begraafplaatsen). Na crematie bergt de houder de as in een asbus; deze wordt bijgezet, verstrooid, aan een nabestaande ter beschikking gesteld, of naar het buitenland verzonden. Ruiming van een asbus kan niet eerder dan tien jaar na berging.

**Bijzondere wijzen van lijkbezorging (art. 67-70)** — ontleding voor wetenschap/onderwijs, met eigen verlofprocedure van de burgemeester.

**Bijzondere bepalingen (art. 71-79)** — balseming/conservering, sectie, vervoer bij niet-natuurlijke dood: telkens aparte verlof-/toestemmingsregimes, veelal via de officier van justitie.

## Kernbegrippen

- **Gemeentelijke lijkschouwer** — door B&W benoemde forensisch arts die lijkschouwingen verricht en meldingen doet aan officier van justitie of regionale toetsingscommissie.
- **Verklaring van overlijden** — document van behandelend arts of gemeentelijke lijkschouwer, voorwaarde voor het verlof tot begraving/crematie.
- **Verlof tot begraving of crematie** — schriftelijk, kosteloos document van de ambtenaar van de burgerlijke stand; zonder dit verlof mag niet worden begraven of gecremeerd.
- **Begraafplaats** — gemeentelijk (verplicht, minimaal één per gemeente) of bijzonder (kerkgenootschap/rechtspersoon); met openbaar register van begraven lijken.
- **Algemeen graf** — graf waarin de houder van de begraafplaats bepaalt wie wordt begraven.
- **Particulier graf / grafrecht** — uitsluitend recht op een graf, schriftelijk gevestigd, looptijd ≥10 jaar of onbepaald, verlengbaar, vervalt bij verwaarlozing via vastgelegde procedure.
- **Crematorium** — gemeentelijk of bijzonder, analoog geregeld aan begraafplaatsen; met openbaar register van gecremeerde lijken.
- **Asbus** — bevat de as na crematie; wordt bijgezet, verstrooid, meegegeven of geëxporteerd.
- **Ruiming** — verwijderen van een graf (na ≥10 jaar) of asbus (na ≥10 jaar) door de houder.

## Relevantie voor bedrijfsarchitectuur

GGM-controle: geen van bovenstaande begrippen komt voor in `ggm_parsed.json` (gecontroleerd op "graf", "begraaf", "crematorium", "lijkschouw", "asbus", "lijkbezorg" — alleen Gemeentebegrafenis en de OverlijdenIngeschrevenPersoon-attributen bestaan al). Dit is dus een onbezet GGM-hiaat, niet gedekt door Beheer Openbare Ruimte/IMBOR (geen treffer in dat onderwerpoverzicht).

Kandidaat-BO's/rollen (zie BO-beoordeling per element):
- **Grafrecht** — eigen levenscyclus (vestiging, verlenging, verval), attributen (looptijd, type), eigen register.
- **Begraafplaats** — wettelijk verplichte gemeentelijke voorziening met eigen register en sluitingsprocedure.
- **Crematorium** — analoog aan Begraafplaats.
- **Lijkschouw** — proces met resultaatdocument (verklaring van overlijden / verslag aan OvJ).
- **Gemeentelijk lijkschouwer** — rol (vergelijkbaar met eerdere rol BOA: door bevoegd gezag benoemde, gekwalificeerde functionaris).
- **Verlof tot begraving of crematie** — formeel document, voorwaarde voor uitvoering.
- Bestaand BO **Gemeentebegrafenis** — verrijkt met grondslag art. 20-22.

## Citaten

> "Burgemeester en wethouders verschaffen gelegenheid tot het doen schouwen van lijken. Zij benoemen een of meer gemeentelijke lijkschouwers." (art. 4)

> "Geen begraving of crematie van een lijk geschiedt zonder schriftelijk verlof van de ambtenaar van de burgerlijke stand, dat kosteloos wordt afgegeven." (art. 11)

> "Een gemeente heeft voor zich of met een of meer andere gemeenten tezamen tenminste een gemeentelijke begraafplaats, tenzij gedeputeerde staten van deze verplichting tijdelijk ontheffing hebben verleend." (art. 33)

> "Een uitsluitend recht op een graf, welke vorm aan dit recht ook wordt gegeven, kan uitsluitend schriftelijk worden gevestigd. Het recht kan voor onbepaalde tijd of voor een bepaalde tijd van ten minste tien jaar worden verleend." (art. 28 lid 1)

> "De crematoria worden onderscheiden in gemeentelijke en bijzondere." (art. 51 lid 1)

## Bronnen
- [[Sources/Onderwerpen/Openbare Gezondheid/wet-op-de-lijkbezorging-wettekst]]
