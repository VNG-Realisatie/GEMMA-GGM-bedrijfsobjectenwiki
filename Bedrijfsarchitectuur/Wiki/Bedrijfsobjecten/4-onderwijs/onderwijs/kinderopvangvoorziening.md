---
type: element
naam: Kinderopvangvoorziening
onderwerp: [onderwijs]
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

bo_definitie: "Locatie waar kinderopvang wordt geboden, geregistreerd in het Landelijk Register Kinderopvang."
bo_toelichting:
bo_subtypes:
  - naam: Kinderdagverblijf (KDV)
    omschrijving: "Dagopvang voor kinderen die nog niet naar de basisschool gaan"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: Buitenschoolse opvang (BSO)
    omschrijving: "Opvang voor schoolgaande kinderen buiten schooltijden"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: Gastouderopvang
    omschrijving: "Opvang door geregistreerde gastouder aan huis"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: Tussenschoolse opvang
    omschrijving: "Opvang tussen de middag voor schoolgaande kinderen, vaak via de school; geen recht op kinderopvangtoeslag"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: Tussenschoolse opvang
    omschrijving: "Opvang tussen de middag voor schoolgaande kinderen, vaak georganiseerd via de school; in tegenstelling tot de andere subtypes geen recht op kinderopvangtoeslag"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[School]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Kinderopvang kan gehuisvest zijn in een schoolgebouw"
bedrijfsprocessen: [Toezicht kinderopvang, Registratie kinderopvang]
bedrijfsfuncties: [Onderwijsbeleid]
---

## BO-criteria toetsing

6/6 criteria: heeft betekenis (ja — wettelijk kader Wet kinderopvang), herkenbaar (ja — GGD-inspecteurs, beleidsmedewerkers), eigen bestaan (ja — zelfstandige locatie met eigen registratie), meervoud (ja — honderden per gemeente), levenscyclus (ja — aanvraag, registratie, inspectie, handhaving, uitschrijving), relaties (ja — met school, LRK, GGD).

## Beschrijving

Een kinderopvangvoorziening is een locatie waar kinderopvang wordt geboden conform de Wet kinderopvang. De gemeente registreert elke voorziening in het Landelijk Register Kinderopvang (LRK), laat jaarlijks inspectie uitvoeren door de GGD en handhaaft bij kwaliteitsgebreken. Sinds 2018 zijn alle peuterspeelzalen juridisch omgezet naar kinderdagverblijven. Per wijk registreert de gemeente het aantal KDV's, BSO's en VVE-locaties.

## Specialisaties

| Specialisatie | Omschrijving | GGM-entiteit |
|---|---|---|
| Kinderdagverblijf (KDV) | Dagopvang voor kinderen 0-4 jaar | — |
| Buitenschoolse opvang (BSO) | Opvang voor schoolgaande kinderen buiten schooltijden | — |
| Gastouderopvang | Opvang door geregistreerde gastouder aan huis | — |
| Tussenschoolse opvang | Opvang tussen de middag voor schoolgaande kinderen, vaak via de school; geen recht op kinderopvangtoeslag | — |

## Procesbron

Dit BO ontstaat in het proces van registratie en toezicht kinderopvang. De Wet kinderopvang verplicht gemeenten tot registratie in het LRK en toezicht via de GGD. Er is geen GGM-entiteit voor kinderopvangvoorzieningen.

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Beschrijving |
|---|---|---|---|---|
| [[School]] | associatie | naar-dit-BO | 0..1 | Kinderopvang kan gehuisvest zijn in een schoolgebouw |

## Bedrijfsprocessen

- Registratie kinderopvang — aanvraag, opname in LRK, wijzigingen
- Toezicht kinderopvang — jaarlijkse GGD-inspectie, handhaving bij overtredingen

## Bedrijfsfuncties

- Onderwijsbeleid

## Bronnen

- [[Wiki/Bronsamenvattingen/Onderwijs/kinderopvang-toezicht]]
- [[Wiki/Bronsamenvattingen/Onderwijs/soorten-kinderopvang]]
- [[Wiki/Bronsamenvattingen/Onderwijs/kindcentra]]

## Terugmelding GGM

Kinderopvangvoorziening is een data-object zonder GGM-entiteit. De gemeente registreert voorzieningen in het LRK, houdt toezicht en handhaaft. Dit past in GGM taakveld 4 Onderwijs, beleidsdomein Onderwijs. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
