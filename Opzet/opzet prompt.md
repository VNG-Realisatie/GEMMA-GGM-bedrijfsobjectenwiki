# Prompt: ontwerp LLM-wiki voor afleiden GEMMA ArchiMate-elementen uit beleidsdocumenten

Ontwerp een logische, LLM-onafhankelijke wiki-opzet waarmee uit beleidsdocumenten en andere bronnen GEMMA ArchiMate-elementen kunnen worden afgeleid.

## Context

De wiki wordt gebruikt als analyse- en curatieomgeving voor het GEMMA ArchiMate-model.

Belangrijke uitgangspunten:

- Het GEMMA ArchiMate-model is de formele bron van waarheid voor definitieve architectuurelementen.
- De wiki bevat analyse, onderbouwing, besluitvorming en voorstellen voor nieuwe of gewijzigde GEMMA-elementen.
- Elementen worden vanuit de wiki geëxporteerd naar het GEMMA ArchiMate-model.
- Er mag geen dubbele vastlegging ontstaan tussen wiki en ArchiMate-model.
- De wiki moet onafhankelijk zijn van een specifieke LLM (ChatGPT, Claude, lokale LLM, etc.).
- De aanpak moet uitbreidbaar zijn naar verschillende ArchiMate-elementtypen.

## Hoofdkeuzes

Gebruik deze ontwerpkeuzes:

1. Werk niet vanuit een generiek begrippenmodel naar ArchiMate-elementen.
   - Een begrip is alleen inputmateriaal.
   - Niet ieder begrip leidt tot een architectuurelement.

2. Gebruik ArchiMate-typegerichte analyse.
   - Zoek niet eerst alle concepten.
   - Analyseer per elementtype welke kandidaten aanwezig zijn.

3. Gebruik één centrale pagina voor kandidaat-elementen.
   - Deze pagina bevat:
     - bronanalyse;
     - typeanalyse;
     - modelleerbesluit;
     - voorgesteld ArchiMate-element.
   - Maak geen aparte permanente analysepagina en elementpagina met overlappende informatie.

4. Het definitieve GEMMA ArchiMate-model blijft de permanente registratie van goedgekeurde elementen.

## Gewenste processtappen

Werk de volgende stappen uit:

Bronnen
↓
Onderwerpen
↓
Type-extractie
↓
Kandidaat-elementen
↓
Beoordeling en modellering
↓
Export naar GEMMA ArchiMate-model

Beschrijf per stap:

- doel;
- gebruikte LLM-skill;
- input;
- output;
- wat permanent wordt vastgelegd.

## Permanente pagina's

Gebruik minimaal deze paginatypen:

### Source

Doel:
- vastleggen van oorspronkelijke bronnen.

Bevat:

- metadata;
- bronlocatie;
- samenvatting;
- relevante passages;
- gekoppelde onderwerpen.

Geen ArchiMate-analyse.

---

### Topic

Doel:
- groeperen van bronnen rond een domein of onderwerp.

Bevat:

- omschrijving onderwerp;
- gekoppelde bronnen;
- relevante termen;
- relevante ArchiMate-elementtypen.

Geen definitieve elementdefinities.

---

### ElementCandidate

Dit is de centrale analysepagina.

Bevat:

- naam;
- bronverwijzingen;
- gevonden termen en synoniemen;
- context;
- gekozen ArchiMate-type;
  - er mogen meerdere type gekozen worden. Bijvoorbeeld een inwoner is een actor of rol waarover ook informatie wordt bijgehouden. dus ook een bedrijfsobject
- type-specifieke beoordeling;
- alternatieve typen;
- motivatie;
- voorgestelde definitie;
- voorgestelde relaties;
- status:
  - kandidaat;
  - review;
  - goedgekeurd;
  - afgewezen.

Na goedkeuring wordt deze informatie geëxporteerd naar GEMMA.

---

## Type-specifieke analyse

Werk templates uit voor minimaal:

### Business Object

Criteria:

- wordt informatie over vastgelegd?
- heeft identiteit?
- heeft levenscyclus?
- heeft eigenschappen?

### Business Actor

Criteria:

- zelfstandige partij?
- voert gedrag uit?
- verantwoordelijkheid?

### Business Role

Criteria:

- verantwoordelijkheid of positie?
- vervulbaar door meerdere actoren?
- gedrag gekoppeld?

### Business Process

Criteria:

- activiteiten;
- trigger;
- resultaat;
- begin/einde.

### Business Function

Criteria:

- stabiele capaciteit;
- organisatie-onafhankelijk;
- ondersteunt processen.

Maak uitbreiding naar andere ArchiMate-typen eenvoudig.

## Gewenste output

Geef:

1. procesmodel;
2. pagina-opbouw;
3. templates;
4. mappenstructuur;
5. exportmodel naar ArchiMate;
6. richtlijnen om dubbeling te voorkomen;
7. voorbeeld met:
   - een Business Object;
   - een Business Actor;
   - een Business Role.

Houd analyse en definitieve architectuur duidelijk gescheiden.
