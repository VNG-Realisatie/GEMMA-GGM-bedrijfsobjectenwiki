# Projectcontext

## Waarom dit project bestaat

Het GEMMA-bedrijfsobjectenmodel is een gefilterde kopie van het GGM (Gemeentelijk Gegevensmodel), maar die filtering gebeurde zonder expliciete criteria. Deze wiki voert de filtering opnieuw uit — onderbouwd en herleidbaar — en vormt zo het besliskader voor welke entiteiten bedrijfsobjecten worden.

## Doel in vier stappen

1. **Bronnen lezen en samenvatten** — beleidsdocumenten, proposities, verordeningen → bronsamenvattingen.
2. **Onderwerpoverzicht opbouwen** — begrippen identificeren, typeren en beoordelen als BO-kandidaat.
3. **Elementen afleiden** — per kandidaat: GGM matchen en een pagina aanmaken met onderbouwing (bedrijfsobject, actor of rol).
4. **Hiaten signaleren** — GGM-entiteiten zonder BO, BO's zonder GGM-grondslag, correcties terugmelden aan het GGM-team.

Resultaat per onderwerp: beslisdocumenten waarvan de metadata als properties naar het GEMMA ArchiMate-model gaat.

## Herleidbaarheidsketen

```
Sources/  →  Wiki/Bronsamenvattingen/  →  Wiki/Bedrijfsobjecten/
(immutabele bron)   (schakelstuk)          (beslisdocument)
```

Het onderwerpoverzicht organiseert per onderwerp de begrippen en hun beoordeling. Elke bewering in de wiki is via deze keten terug te voeren op een originele bron.

## Werkwijze

De wiki wordt **onderwerp voor onderwerp** opgebouwd: per onderwerp het volledige proces (bronnen → samenvattingen → onderwerpoverzicht → elementen) afronden voordat het volgende onderwerp start. GGM-dekkingsanalyse gebeurt centraal per taakveld/beleidsdomein (zie [../workflows/onderhoudscyclus.md](../workflows/onderhoudscyclus.md)), omdat wiki-onderwerpen en GGM-beleidsdomeinen niet 1-op-1 overlappen.

## Onderhoudscyclus

Na de initiële opbouw wordt het model onderhouden bij:

- **Nieuwe GGM-releases** — entiteiten hertoetsen, frontmatter verversen, dekking herberekenen.
- **Nieuwe onderwerpen** — bronnen toevoegen, onderwerpoverzicht uitbreiden, elementen afleiden.

## Rol van de LLM

De LLM is het **eerste filter**: hij leest, structureert en beoordeelt, binnen een getrapt autonomiemodel — bronnen worden eerst besproken, eenduidige begrippen zelfstandig afgehandeld, twijfelgevallen voorgelegd. De mens (het GEMMA-team) selecteert bronnen, beslist twijfelgevallen en stelt vast. Zie [ai-richtlijnen.md](ai-richtlijnen.md).

## GGM als bron én validatie

- **Invoer** — het GGM levert beleidsdomeinen en kandidaat-entiteiten.
- **Validatie** — elk uit bronnen afgeleid BO wordt getoetst tegen het GGM; verschillen worden gedocumenteerd.
- **Feedbackloop** — hiaten, duplicaten en definitieverschillen gaan als terugmelding naar het GGM-team.
