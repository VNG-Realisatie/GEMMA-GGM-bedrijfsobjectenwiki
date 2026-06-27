---
type: bedrijfsobject
naam: Stuk
onderwerp: [Basisregistraties, BRK]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: ""
ggm_guid: ""
ggm_uml_type: ""
ggm_beleidsdomein: ""
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

ggm_duplicaat_entiteiten: []

bo_definitie: "Een brondocument dat is ingeschreven in de openbare registers van het Kadaster en de grondslag vormt voor bijwerking van de BRK."
bo_relaties:
  - type: compositie
    bedrijfsobject: "[[Stukdeel]]"
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Een stuk omvat een of meer stukdelen"
  - type: associatie
    bedrijfsobject: "[[Publiekrechtelijke Beperking]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een stuk kan de grondslag zijn voor publiekrechtelijke beperkingen"
bedrijfsprocessen:
  - WKPB-registratie
  - Eigendomsverificatie
  - Kadastrale recherche
bedrijfsfuncties:
  - Vastgoedbeheer
  - Handhaving
---

## BO-criteria toetsing

6/6 criteria. Stuk is een concreet document in de openbare registers met eigen identificatie (deel-en-nummer, authentiek gegeven), eigen levenscyclus (inschrijving), meervoudig, en relaties met stukdelen, rechten en kadastrale objecten. De gemeente biedt zelf WKPB-besluiten ter inschrijving aan.

## Beschrijving

Een stuk is een brondocument dat wordt ingeschreven in de openbare registers van het Kadaster. Alle rechtswijzigingen in de BRK (overdracht, hypotheek, splitsing, beperking) zijn traceerbaar naar ingeschreven stukken. Er zijn twee soorten:

- **Ter Inschrijving Aangeboden Stuk** — doorgaans een notariële akte (akte van levering, hypotheekakte, splitsingsakte) of een WKPB-besluit van een bestuursorgaan
- **Kadasterstuk** — intern correctiestuk van het Kadaster, aangemaakt naar aanleiding van een klacht, bezwaar of fout

De gemeente biedt als WKPB-bronhouder zelf stukken (beperkingsbesluiten) ter inschrijving aan bij het Kadaster. Authentieke gegevens van een stuk zijn het deel-en-nummer en het tijdstip van aanbieding.

## Subtypes

Herkende specialisaties van Stuk. Gevonden in de BRK Catalogus. Geen apart BO.

- **TerInschrijvingAangebodenStuk** — extern aangeboden document, meestal notariële akte of WKPB-besluit
- **Kadasterstuk** — intern correctiestuk van het Kadaster

## GGM-bron

Geen GGM-match gevonden. Stuk is een **GGM-hiaat**.

## Relaties

| Relatie | Richting | BO | Kardinaliteit | Bron |
|---|---|---|---|---|
| omvat | van-dit-BO | [[Stukdeel]] | 1..* | BRK Catalogus |
| grondslag voor | naar-dit-BO | [[Publiekrechtelijke Beperking]] | 0..* | BRK Catalogus |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-brk]]

## Terugmelding GGM

Stuk ontbreekt als objecttype in het GGM. Data-object met authentieke gegevens (deel-en-nummer, tijdstip aanbieding) en eigen identificatie. Brondocument waarop alle BRK-bijwerkingen traceren. Past in beleidsdomein RSGBPlus (99 Kern). Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
