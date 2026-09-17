---
type: element
naam: Gebruiksrecht
onderwerp: [Basisregistraties]
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

bo_definitie: "Besluit, melding of gegevens van een bestuursorgaan gericht op het winnen of benutten van ondergrondse hulpbronnen, het opslaan van stoffen, of het geschikt maken van de bodemkwaliteit, geregistreerd in de BRO."
bo_toelichting: "Gebruiksrechten omvatten vergunningen, meldingen en gegevens die de gemeente als bevoegd gezag of bronhouder afgeeft of ontvangt over activiteiten in de ondergrond. Voorbeelden: grondwateronttrekkingsvergunning, melding bodemsanering, beschikking bodemkwaliteit."
bo_subtypes: []
bo_synoniemen: []
bo_homoniemen:
  - bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/brk/zakelijk-recht|Zakelijk Recht]]"
    ggm_entiteit: Zakelijk Recht
    ggm_guid:
    ggm_beleidsdomein: BRK
    toelichting: "BRK Zakelijk Recht gaat over eigendom/hypotheek op onroerende zaken; BRO Gebruiksrecht gaat over activiteiten in de ondergrond — ander concept"
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Constructie]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: "Gebruiksrecht kan betrekking hebben op een constructie (bijv. winningsput)"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding|Aanvraag of melding]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een gebruiksrecht ontstaat uit een besluit op aanvraag/melding"
bedrijfsprocessen:
  - "Vergunningverlening grondwater"
  - "Bodemsanering"
bedrijfsfuncties:
  - "Vergunningverlening, toezicht en handhaving"
  - "Bodembeheer"
---

# Gebruiksrecht

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Identiteit | ✅ | Eigen BRO-identificatiecode, type, locatie, houder |
| Levenscyclus | ✅ | Verlening, wijziging voorschriften, intrekking |
| Eigenaarschap | ✅ | Gemeente is bronhouder (als bevoegd gezag) of afnemer |
| Relaties | ✅ | Gekoppeld aan constructies, verkenningen, besluiten |
| Meervoud | ✅ | Tientallen per gemeente (grondwateronttrekkingen, saneringen) |

## Beschrijving

Een Gebruiksrecht is een besluit, melding of gegevensverstrekking van een bestuursorgaan gericht op activiteiten in de ondergrond: het winnen van grondwater, het opslaan van stoffen, het saneren van verontreinigde bodem, of het graven met milieukundige begeleiding.

De gemeente is betrokken als bevoegd gezag (vergunningverlening grondwateronttrekking, beschikking bodemkwaliteit) en als bronhouder (aanlevering van het gebruiksrecht aan de BRO). Het gebruiksrecht bevat de ruimtelijke begrenzing of het volume in de ondergrond, de houder, en eventuele voorschriften en beperkingen.

Alle authentieke gegevens per gebruiksrecht (art. 20 Wet BRO): identificatiecode, type, locatie, ruimtelijke begrenzing/volume, houder (KvK), meetresultaten, voorschriften.

## Naamkeuze

De term "Gebruiksrecht" in de Wet BRO heeft een andere betekenis dan "Zakelijk Recht" in de BRK. BRO-Gebruiksrecht betreft activiteiten in de ondergrond (winnen, opslaan, saneren); BRK-Zakelijk Recht betreft eigendom en hypotheek op onroerende zaken.

## Procesbron

Wettelijke grondslag: art. 9 en 20 Wet BRO. De gemeente verleent grondwateronttrekkingsvergunningen, neemt saneringsmeldingen in ontvangst, en registreert beschikkingen bodemkwaliteit.

## Relaties

| Relatie | BO | Richting | Beschrijving | Bron |
|---|---|---|---|---|
| associatie | [[Constructie]] | ↔ | Gebruiksrecht op een constructie (bijv. winningsput) | Wet BRO |
| associatie | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | ← | Gebruiksrecht ontstaat uit besluit op aanvraag/melding | cross-domein |

## Terugmelding GGM

GGM-hiaat: BRO-objecttypen niet in het GGM gemodelleerd.

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/wet-bro]]
