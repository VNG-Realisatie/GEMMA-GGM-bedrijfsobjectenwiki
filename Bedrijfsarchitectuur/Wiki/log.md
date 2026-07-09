# Wiki Log

## [2026-07-09] fix | Frontmatter-stijl wiki-breed genormaliseerd (vervolg op enum-fix, plus een echte bug)

- **Aanleiding:** gebruiker wees erop dat de enum-quote-fix (zie entry hieronder) de frontmatter niet consistenter maakte — vergelijking van `handhavingsbesluit.md` en `stembureau.md` liet zien dat vrijwel elk veld een eigen quote-stijl had (`""`, `''`, blanco, letterlijke `'~'`), naast een veldnaam-inconsistentie (`domein` vs `onderwerp`, 206 vs 216 bestanden).
- **Audit vond ook een echte correctheidsbug, geen stijlkwestie:** `bedrijfsobject: [[naam]]` zonder quotes in `bo_relaties` parseert in YAML als een **geneste lijst** (`[['naam']]`) i.p.v. de bedoelde string — elke tool die dit veld leest krijgt kapotte data. Trof 4 relaties in `woo-verzoek.md` en `klacht.md`. `templates/element.md` gaf zelf het ongequote voorbeeld — ook gecorrigeerd.
- **Canonieke stijl vastgesteld (met gebruiker):** lege waarde → blanco (niet `""`/`''`/`~`); niet-lege tekstwaarden → dubbele quotes (niet enkele); `domein:` → `onderwerp:` (conform template).
- **Script:** `tools/migrate_frontmatter_style.py` (nieuw, herbruikbaar/idempotent) — normaliseert lege scalars, quote-stijl (GGM-velden, `bo_toelichting`, geforceerd bij `bo_definitie` en `bo_relaties.bedrijfsobject`/`kardinaliteit`), lege lijsten (`bedrijfsprocessen`/`bedrijfsfuncties` → `[]`), en de veldnaam-rename.
- **Bug tijdens eerste versie ontdekt en gerepareerd vóór toepassing:** een naïeve regel-voor-regel aanpak corrumpeerde 19 bestanden met multi-line frontmatter-waarden (een al bestaand content-artefact: sommige `ggm_definitie`-velden bevatten multi-line quoted of HTML-houdende plain scalars). Script herschreven met lookahead-detectie die zulke velden ongemoeid laat, plus een verplichte post-write YAML-parse-en-semantische-vergelijking (oud vs. nieuw, met normalisatie voor het opzettelijke type-verschil `1` → `"1"`) die een bestand terugdraait i.p.v. wegschrijft als er ook maar iets niet klopt.
- **Resultaat:** 411 van 422 bestanden gewijzigd, 0 aborts, 0 ongeldige YAML, 0 non-string `bedrijfsobject`-waarden (was 4). 3 bestanden met een pre-existing multi-line `ggm_definitie`/`ggm_toelichting`-artefact bewust ongemoeid gelaten (`boom.md`, `faunapassage.md`, `voorbereiding-op-inburgering.md`) — dat is een apart, ouder content-issue (mogelijk een dubbele "Toelichting:"-tekst in de XMI-import), niet in scope van deze stijl-opschoning.
- **Bronscripts bijgewerkt** zodat de oude stijl niet terugkomt bij de volgende regeneratie: `tools/generate_ggm_enrich_bo.py` schrijft nu blanco i.p.v. `""` voor lege velden, en `onderwerp` i.p.v. `domein` (leest beide, schrijft alleen `onderwerp`); `bo_relaties.bedrijfsobject`/`kardinaliteit` altijd dubbel gequote.
- **`templates/element.md`** kreeg een nieuwe sectie "Frontmatter-stijl" die de conventie expliciet vastlegt (was nooit gedocumenteerd — vandaar de drift). **`lint.md`** uitgebreid met een check hierop.
- **Verificatie:** `entiteitendekking.py --all` opnieuw gedraaid — identieke rapporten, geen regressie. Script is idempotent (herhaalde dry-run: 0 wijzigingen).

## [2026-07-09] fix | Gequote enum-waarden genormaliseerd (lint-nawerk)

- **Aanleiding:** één van de twee resterende "bewust niet (nog) gedaan"-items uit de lint-audit van [2026-07-09] — 78 (inmiddels 143, door nieuwe actor/rol-pagina's) element-pagina's hadden `grondslag`, `archimate_type` en/of `ggm_uml_type` als gequote string i.p.v. bare YAML-waarde, in strijd met `templates/element.md`.
- **Fix:** script over `Wiki/Bedrijfsobjecten/`, `Wiki/Actoren/`, `Wiki/Rollen/` — `grondslag:`/`archimate_type:` unquoted, lege `ggm_uml_type: ""`/`''` genormaliseerd naar blanco. 143 bestanden gewijzigd (259 regels).
- **Verificatie:** alle 422 frontmatters parsen nog als geldige YAML; `entiteitendekking.py --all` opnieuw gedraaid — identieke rapporten, geen regressie.
- **Nog open:** bronnenketen-achterstand (42+19 nog niet geïngeste bronnen, zie `ToDo/ingest-backlog.md`) — dat is een inhoudelijke ingest-klus, geen lint-fix, bewust niet meegenomen.

## [2026-07-09] fix | Resterende 5 generalisatie/specialisatie-gevallen afgehandeld + ambiguïteitsbug gevonden

- **Aanleiding:** vervolg op de vorige log-entry; de gebruiker koos per geval hoe de resterende 5 kandidaten opgelost moesten worden, en breidde CLAUDE.md-regel 11 uit: generalisatiekeuzes altijd per geval voorleggen, ook na een eerder "geldt overal"-antwoord.
- **Ontdekking:** voor 3 van de 5 gevallen (Horecabedrijf/Vestiging, Risicobron/Activiteit, Aandachtsgebied+Voorschriftengebied/Gebiedsaanwijzing) bleek de generieke GGM-naam-pagina (`vestiging.md`, `activiteit.md`, `gebiedsaanwijzing.md`) al te bestaan uit eerder werk, maar met een **ambiguïteitsbug**: de GGM-guid stond op zowel de generieke pagina als de specifieke pagina, waardoor `entiteitendekking.py`'s `_bo_first`-tiebreak willekeurig (bestandsvolgorde-afhankelijk) de specifieke pagina liet "winnen" i.p.v. de generieke — bijv. GGM-entiteit "Vestiging" matchte naar `Horecabedrijf.md` i.p.v. `vestiging.md`.
- **Horecabedrijf → Vestiging (C-stijl, bestond al):** Horecabedrijf blijft eigen Specialisatie-pagina; `grondslag` → `ggm-afgeleid`, ggm-velden leeggemaakt, generalisatie-relatie met correcte richting (`naar-dit-BO`) toegevoegd. Vestiging.md kreeg de symmetrische relatie terug.
- **Risicobron → Activiteit (C-stijl, bestond al):** zelfde fix. `ggm_duplicaat_entiteiten` (die de Musea-homoniem "Activiteit" ten onrechte als duplicaat van Risicobron registreerde) verwijderd — dit repareerde en passant een foutieve matchketen in het Musea-cluster (Activiteitsoort, Museumrelatie, Programma, Programmasoort, Reservering, Rondleiding matchten voorheen allemaal ten onrechte naar Risicobron).
- **Aandachtsgebied + Voorschriftengebied → Gebiedsaanwijzing (B-stijl, samengevoegd):** beide pagina's verwijderd; hun inhoud (incl. sub-subtypes Brand-/Explosie-/Gifwolkaandachtsgebied en Brand-/Explosievoorschriftengebied) toegevoegd als geneste Subtypes onder Gebiedsaanwijzing → Beperkingsgebied. Risicobron's relaties naar beide omgezet naar relaties met Gebiedsaanwijzing. Onderwerpoverzicht `gevaarlijke-stoffen.md` bijgewerkt (bo_count 3→1), openstaande vraag over dit onderwerp opgelost.
- **Gezinsmigrant → "Gezinsmigrant en Overige migrant" (B-stijl):** hernoemd (bestand → `gezinsmigrant-en-overige-migrant.md`); Gezinsmigrant en het niet-gedocumenteerde "Overige migrant" als Subtypes vastgelegd. Alle kruisverwijzingen (Brede Intake, Inburgeringsplicht, 2 onderwerpoverzichten, index.md) bijgewerkt.
- **Verificatie:** `entiteitendekking.py --all` opnieuw gedraaid; alle 4 generieke pagina's (Vestiging, Activiteit, Gebiedsaanwijzing, Gezinsmigrant en Overige migrant) matchen nu correct "Exacte match" i.p.v. de vorige willekeurige specifieke pagina. `git status` na regeneratie bevestigt geen onverwachte bestandswijzigingen buiten de eigen bewerkingslijst.
- **CLAUDE.md**: regel 11 uitgebreid met expliciete verwijzing naar dit type beslissing (generalisatie/specialisatie-naamskeuzes altijd per geval voorleggen).

## [2026-07-09] fix | Generalisatie/specialisatie-gevallen uit de Naamkeuze-lintbevindingen

- **Aanleiding:** de lint-audit signaleerde 23 BO's zonder `## Naamkeuze`-sectie waar `naam` ≠ `ggm_entiteit`. Bij nadere beoordeling bleek een deel hiervan geen naamkeuze te zijn maar een generalisatie/specialisatie-relatie (GGM-entiteit is breder of smaller dan het BO-begrip) — al correct gedocumenteerd via de bestaande `## GGM-bron`/matchsterkte-sectie, niet via Naamkeuze (dat is uitsluitend voor homoniem-disambiguatie, zie `templates/element.md`).
- **Vaartuig/Woonboot** (bewuste uitzondering): `Wiki/Bedrijfsobjecten/.../vth/woonboot.md` hernoemd naar `vaartuig.md` (naam: Vaartuig, matcht nu exact met de GGM-entiteit); Woonboot gedocumenteerd als Subtype (geen eigen pagina) binnen die pagina, met de bestaande subtypes (Woonark, Varend schip, Historisch schip, Schark) genest onder Woonboot. Alle kruisverwijzingen bijgewerkt (Ligplaats, 3 bronsamenvattingen, index.md, onderwerpoverzicht Wonen).
- **Evenement**: eerst ook hernoemd naar OpenbareActiviteit, daarna **teruggedraaid** op verzoek van de gebruiker — Evenement is een zelfstandig, breed gedragen beleidsbegrip (eigen reserveringskalender, beoordelingscriteria, vergunningenproces) en hoort niet hernoemd te worden naar de abstractere GGM-naam. Dit scherpte het onderscheidingscriterium aan: alleen hernoemen wanneer de specifieke term geen eigen identiteit heeft los van "de volledige praktijkscope van deze GGM-entiteit".
- **Rioolleiding/Leiding**: nieuwe pagina `leiding.md` aangemaakt (matcht exact met GGM-entiteit Leiding); Rioolleiding blijft een **eigen pagina** (Specialisatie, niet Subtype — voldoet zelfstandig aan de 6 BO-criteria) met een generalisatie-relatie terug naar Leiding (`grondslag: ggm-afgeleid`, geen eigen ggm_entiteit meer). Onderwerpoverzicht Milieu en index.md bijgewerkt (bo_count 35→36).
- **Overige 5 kandidaten** (Horecabedrijf, Aandachtsgebied, Voorschriftengebied, Risicobron, Gezinsmigrant): ongewijzigd gelaten — zelfde redenering als Evenement, zijn zelfstandige beleidsbegrippen.
- **`lint.md` gecorrigeerd**: de Naamkeuze-check verwees niet naar de bestaande definitie in `templates/element.md` (homoniem-disambiguatie) en was te breed geformuleerd. Nu expliciet uitgezonderd: generalisatie/specialisatie-afwijkingen horen bij `## GGM-bron`, niet bij `## Naamkeuze`.
- **Bijvangst:** tijdens deze sessie bleken `raadsstuk.md` en `Wiki/GGM/.../griffie.md` buiten alle tool-aanroepen om gewijzigd (waarschijnlijk een editor-artefact) — `raadsstuk.md` was teruggezet naar het oude `type: bedrijfsobject`. Beide hersteld via `git checkout`; rapporten geregenereerd en geverifieerd (geen regressie).

## [2026-07-09] lint | Wiki-brede consistentiecheck: 4 parallelle Haiku-scans + verificatie + fixes

- **Aanleiding:** `/lint` uitgevoerd over de hele wiki na de actoren/rollen-migratie, om te controleren of de schemawijziging en de ~180 nieuwe/gewijzigde pagina's geen frontmatter-/structuurfouten hebben geïntroduceerd.
- **Aanpak:** 4 parallelle Haiku-subagents (Bedrijfsobjecten, Actoren/Rollen, bronnenketen Sources↔Bronsamenvattingen, onderwerpoverzichten/analyses/structuur), gevolgd door eigen steekproefverificatie — een deel van de Haiku-bevindingen bleek bij controle vals (zie [[feedback_lint-haiku-verificatie]] in memory).
- **Gerepareerd:**
  - `grondslag: ggm-hiaat` (ongeldige enum) → `procesobject` op `Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/informatieobject.md`.
  - `grondslag: ggm-entiteit` zonder ggm_entiteit/ggm_guid → `procesobject` op 3 gedocumenteerde GGM-hiaten in BRK: `stuk.md`, `stukdeel.md`, `publiekrechtelijke-beperking.md`.
  - 81 actor/rol-pagina's kregen een ontbrekend `bo_definitie`-veld in de frontmatter (track1/track2-generatorscripts vulden dit nooit; definitie stond alleen als proza in de body) — gecondenseerd tot ≤160 tekens per pagina, overgenomen uit de bestaande body-tekst.
  - 2 verouderde `## GGM-dekking`-secties verwijderd uit `Onderwerpoverzichten/vastgoed.md` en `informatiesystemen.md` (dekking zit centraal in `Wiki/Analyses/ggm-dekking.md`).
  - 2 ontbrekende wiki-link-aliassen toegevoegd (`Wiki/Rollen/belanghebbende.md`, `Wiki/Actoren/organisatorische-eenheid.md`).
  - `tools/entiteitendekking.py --all` opnieuw gedraaid ter verificatie — geen regressie, de 3 BRK-hiaten en informatieobject.md correct als "Alleen GEMMA-BO" geclassificeerd.
- **Bewust niet (nog) gedaan:** 23 ontbrekende `## Naamkeuze`-secties (waar `naam` ≠ `ggm_entiteit`), 78 BO's met gequote (maar functioneel correcte) enum-waarden, en de bestaande bronnenketen-achterstand (42+19 nog niet geïngeste bronnen in 13 onderwerpen) — dit zijn stijl-/backlogkwesties, geen fouten geïntroduceerd door de actoren/rollen-migratie.

## [2026-07-09] fix | Track 2-triage gecorrigeerd na review: Loonwaardedeskundige geschrapt, Leerling heroverwogen

- **Aanleiding:** de gebruiker controleerde de zelfstandige track 2-triagebeslissingen (33 uitsluitingen + 7 inclusies zonder vooraf overleg) en vroeg om twee correcties.
- **Loonwaardedeskundige** (rol) verwijderd: `Wiki/Rollen/loonwaardedeskundige.md` geschrapt, referentie uit `Wiki/index.md` verwijderd, backlog aangepast.
- **Leerling** heroverwogen: bij nader inzien geen doelgroep-achtig grensgeval maar een operationele rol (hoedanigheid van ingeschreven zijn bij een school, met eigen rechten/plichten in leerlingenvervoer, VVE en herschikking, los van de generieke rol Indiener). Nieuwe pagina [[Wiki/Rollen/leerling]] — bleek bovendien een GGM-match te hebben via de al bestaande BO-pagina `Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/leerling.md` (exact match, taakveld 4 Onderwijs): twee-pagina-patroon toegepast met `element_tegenhangers` over en weer, gedeelde `ggm_guid`. `Wiki/Onderwerpoverzichten/onderwijs.md` en `Wiki/index.md` bijgewerkt. Rapporten geregenereerd — geen wijziging in matchtelling (entiteit was al gedekt via de BO, rol is nu tegenhanger).
- **Ook afgerond (zelfde sessie):** GGD-actorpagina en de generieke BO Gemeenschappelijke Regeling kruisverwezen (GGD is één van de expliciete voorbeelden op die BO-pagina).


## [2026-07-09] update | Onderwerpoverzichten bijgewerkt met actor/rol-verwijzingen

- **Aanleiding:** de begrippentabellen van 12 onderwerpoverzichten bevatten al rijen voor termen die tijdens dit traject een actor/rol-pagina kregen (bv. raadslid, burgemeester, heffingsambtenaar, GGD) — aangemaakt vóórdat het onderscheid actor/rol bestond, met reden-teksten als "rol, geen ding" zonder verwijzing naar enige pagina.
- **Bijgewerkt (12 bestanden, ~30 rijen):** `bestuur.md` (raadslid, collegelid, burgemeester, griffier, secretaris, rekenkamer, ombudsman), `basisregistraties.md` (bronhouder, afnemer, terugmelder, dataleverancier, belanghebbende, heffingsambtenaar — stelselrollen-tabel + WOZ-tabel), `belastingen.md` (belastingplichtige, heffingsambtenaar, invorderingsambtenaar), `informatiesamenleving.md` (Woo-contactpersoon, gebruiksverantwoordelijke, aanbieder, AI compliance officer, FG, CISO), `maatschappelijke-ondersteuning.md` (aanbieder/zorgaanbieder, buurtteam, mantelzorger, Veilig Thuis), `omgevingswet.md` (kwaliteitsborger, initiatiefnemer, bevoegd gezag), `onderwijs.md` (leerplichtambtenaar, vervoerder), `openbare-gezondheid.md` (GGD), `vastgoed.md` (eigenaar, huurder), `welstand.md` (Commissie Welstand en Monumenten), `werk-en-inkomen.md` (sociaal ontwikkelbedrijf), `wonen.md` (woningcorporatie), `cultuur.md` (gemeentearchivaris → Archivaris).
- **Aanpak:** elke rij kreeg een wiki-link naar de nieuwe actor/rol-pagina en een bijgewerkte Reden-tekst; Type-kolom gecorrigeerd van "actor"/"governance" naar "rol" waar de uiteindelijke classificatie dat was (bv. raadslid, collegelid, griffier, secretaris, heffingsambtenaar, belastingplichtige zijn rol, geen actor). Buurtteam kreeg een verwijzing naar de fold-in op Organisatorische eenheid i.p.v. een eigen pagina. BO?/Data-object-kolommen ongewijzigd gelaten waar die al correct waren.
- **Bewust niet gedaan:** geen nieuwe rijen toegevoegd voor actor/rol-pagina's die nog nergens in een begrippentabel voorkwamen (het merendeel van de 79 track 2-pagina's, gevonden via bronsamenvattingen-sweep buiten de reguliere ingest-workflow om) — dat zou neerkomen op het met terugwerkende kracht opnieuw doorlopen van 34 onderwerpoverzichten, wat buiten de scope van deze correctieslag valt.


## [2026-07-09] fix | 4 nieuwe ambiguïteiten door actor/rol-matching opgelost

- **Aanleiding:** de Fase 4-regeneratie na track 1 introduceerde 4 nieuwe "ter discussie"-ambiguïteiten doordat nieuwe actor/rol-pagina's als extra padkandidaten meetelden in de graph-search: Raadscommissie (Vergadering/Raadslid), Pachter (Eigenaar/Huurder/Vastgoedobject), Sociale Groep/Sociale Relatie (5 ongerelateerde BO's, via de nieuwe BO Aanwezige Deelnemer) en Taak (10 ongerelateerde BO's, via de nieuwe rol Indiener).
- **Raadscommissie en Pachter**: bleken zelf onterecht als `detail` geclassificeerd terwijl ze eigen GGM-entiteiten zijn met een heldere definitie (resp. "groep raadsleden die raadsbesluitvorming voorbereidt" en "persoon met pachtovereenkomst voor landbouwgrond") — geen van de aangeboden kandidaten was een goede structurele match. Opgelost met eigen pagina's: [[Wiki/Actoren/raadscommissie]] (actor, analoog aan de al bestaande Werkgeverscommissie) en [[Wiki/Rollen/pachter]] (rol, verwant aan maar onderscheiden van Erfpachter/Huurder).
- **Sociale Groep, Sociale Relatie, Taak**: bron van de ambiguïteit was extreme genericiteit (Taak: "Een samenhangende set activiteiten", 0 attributen), niet actor/rol-specifiek — de nieuwe actor/rol-pagina's maakten alleen een al bestaand probleem zichtbaarder. Toegevoegd aan `GENERIC_BUILDING_BLOCKS` in `tools/entiteitendekking.py`, net als de al bestaande generieke termen (Locatie, Punt, Periode, ...).
- **Resultaat na regeneratie:** de 4 doelambiguïteiten (5 rijen) zijn weg; 29 pre-existing, niet-actor/rol-gerelateerde "ter discussie"-items blijven ongewijzigd staan (buiten scope van deze fix). Index bijgewerkt met de 2 nieuwe pagina's.


## [2026-07-09] audit | audit-actoren track 2: 79 actor-/rolpagina's uit bronsamenvattingen-sweep (governance-hiaten)

- **Aanleiding:** track 2 van `/audit-actoren` — actoren/rollen die wél in bronnen genoemd worden maar niet in het GGM zitten. 4 subagents doorzochten in golf 1 alle 218 bronsamenvattingen (34 onderwerpmappen), gebalanceerd verdeeld in 4 clusters van ~55 bestanden. Resultaat: ~95 ruwe kandidaten, vastgelegd in `ToDo/audit-actoren-track2-kandidaten.md`.
- **Triage (met gebruiker voor de 5 belangrijkste merge-vragen + 1 escalatie, de rest op basis van de criteria in [[Wiki/GEMMA/actoren-en-rollen]] en het gemeentelijk perspectief):**
  - 6 merges/samenvoegingen opgelost: Gemeentearchivaris+Archivaris/Directeur-archivaris → één pagina "Archivaris"; Werkgever (onafhankelijk gevonden in Arbeidszaken én Werk en Inkomen) → één pagina; Aanbieder (AI/zorg-jeugdhulp/deelmobiliteit) → één generieke rol-pagina met 3 voorbeelden; Woningcorporatie → actor-pagina (externe partij, wel directe prestatieafspraken); WOZ-belanghebbende → fold-in op bestaande Belanghebbende-pagina; GGD → actor-pagina (mede-eigenaarschap via GR rechtvaardigt eigen pagina naast de generieke BO Gemeenschappelijke regeling, ondanks dat de bron zelf "ketenpartner" zegt).
  - Buurtteam → fold-in op bestaande Organisatorische eenheid-pagina (specialisatie, geen apart begrip).
  - 33 kandidaten uitgesloten met reden (te generiek/doelgroep-achtig, te dun bronmateriaal, civielrechtelijk/indirect, of pure externe/justitiële context) — volledige lijst met redenen in de backlog.
- **Aangemaakt:** 23 actor-pagina's (`Wiki/Actoren/`) en 56 rol-pagina's (`Wiki/Rollen/`), platte structuur, elk met criteria-toetsing tegen de ArchiMate-vragenlijsten, `grondslag: governance-object` of `procesobject` (geen GGM-match — dit zijn per definitie governance-hiaten) en bronvermelding naar de bronsamenvatting(en) waarin het begrip is gesignaleerd.
- **Index bijgewerkt:** `Wiki/index.md`-secties Actoren en Rollen aangevuld met alle 79 nieuwe pagina's plus één-zins-omschrijving.
- **Niet gedaan:** GGM-matching voor deze pagina's — dat is hier niet van toepassing, want track 2 bestaat per definitie uit niet-GGM-geankerde begrippen. `entiteitendekking`/`export_ggm_csv` hoeven dus niet opnieuw te draaien voor dekkingseffect; wel geverifieerd dat beide scripts de nieuwe pagina's foutloos inlezen (aantal element-pagina's 101 → correct, geen crashes op de ontbrekende ggm_guid-velden).


## [2026-07-09] fix+rapportage | Actoren/rollen tellen mee in de dekking: matchlogica, multi-GUID en regeneratie

- **`tools/entiteitendekking.py`:** scant nu `Wiki/Actoren/` en `Wiki/Rollen/` naast `Wiki/Bedrijfsobjecten/`. GUID-index is geen last-write-wins meer: meerdere pagina's mogen dezelfde `ggm_guid` dragen (twee-pagina-patroon), de business-object-pagina is primair en tegenhangers worden geregistreerd. Bijvangst: drie al bestaande stille GUID-botsingen tussen BO's zichtbaar gemaakt (Aandachtsgebied↔Voorschriftengebied/Gebiedsaanwijzing, Risicobron↔Activiteit, Horecabedrijf↔Vestiging). Entiteitstype actor/rol is niet langer automatisch n.v.t.: eerst matchen; ongematcht → `⚠️ geen actor/rol-pagina` + review.md; alleen gecureerde buiten-scope-gevallen (nieuwe `NVT_ACTOR_ROL`-set in het script) krijgen nog n.v.t. Skill-doc bijgewerkt.
- **`tools/export_ggm_csv.py`:** exporteert alle element-pagina's; bij een gedeelde GUID een rij per pagina; nieuwe kolom `archimate_type`. Export geverifieerd: 1378 rijen (1364 entiteiten + tegenhanger-pagina's), 23 actor/rol-rijen, geen overschreven rijen. **`tools/generate_ggm_enrich_bo.py`** scant ook de nieuwe mappen.
- **Rapporten geregenereerd (12 taakvelden):** n.v.t. 59 → 40, gedekt 694 → 709 (absoluut +15), noemer 858 → 877, dekking blijft 81%. Raadslid/Collegelid/Aanwezige Deelnemer/Indiener e.a. matchen nu via de normale route i.p.v. handmatige n.v.t.-correcties. Niet gedekt 164 → 168: de nieuwe element-pagina's doen mee als padkandidaten en leggen 4 nieuwe echte ambiguïteiten bloot (o.a. Raadscommissie: Vergadering vs. Raadslid; Pachter: Eigenaar/Huurder/Vastgoedobject) — af te handelen via de bestaande `bo_via_kandidaten`-curatie.


## [2026-07-09] audit | audit-actoren track 1: 18 actor/rol-pagina's + 6 BO-tegenhangers uit entiteitendekking-rapporten

- **Aanleiding:** eerste run van de nieuwe skill `/audit-actoren` (track 1): grep over de 12 entiteitendekking-rapporten op rijen met entiteitstype actor/rol en dekking n.v.t. leverde 18 unieke GGM-entiteiten op die nog geen pagina hadden.
- **Typeringsbesluiten (met gebruiker):** Raadslid/Collegelid = **rol** (lidmaatschap is een verantwoordelijkheid, de persoon is de actor); Ondernemer = **actor** (zelfstandig handelende partij, cf. Inwoner); Eigenaar/Huurder/Belanghebbende/Vervoerder = **rol** (hoedanigheden). Eindstand: 2 actoren (Bevoegd Gezag, Ondernemer), 16 rollen.
- **Aangemaakt:** 2 pagina's in `Wiki/Actoren/`, 16 in `Wiki/Rollen/`, elk met `ggm_guid` (dekking) en criteria-toetsing tegen [[Wiki/GEMMA/actoren-en-rollen|Actoren en rollen]]. Voor de 6 kandidaten met substantiële GGM-attributen óók een BO-tegenhanger (twee-pagina-patroon, `element_tegenhangers` beide kanten op): raadslid, collegelid, aanwezige-deelnemer (griffie), contactpersoon (schulden), opdrachtgever, opdrachtnemer (financien).
- **GGM-duplicaten geregistreerd:** Indiener (griffie + Model VTH), Contactpersoon (Schuldhulpverlening + Vroegsignalering).
- **GGM-datakwaliteit gesignaleerd:** definitie van Grondbeheerder is gebrekkig ("Beheerder van grondgrondbeheer., oplossing voor duurzaam landbeheer en voedselproductie") — eigen definitie gebruikt, terugmelding type `definitie` aangewezen. Taalfouten in definities van Raadslid ("behoort de gemeenteraad"), Collegelid, Indiener ("meldiing"), Aanwezige Deelnemer ("eencollege-") opgeschoond in bo_definitie conform definitieregels.
- **Vervolg:** entiteitendekking.py bijwerken (multi-map GUID-index, scan Actoren/Rollen, n.v.t.-regel), rapporten regenereren, daarna track 2 (bronsamenvattingen-sweep).


## [2026-07-08] ontwerp | Actoren en rollen als volwaardige elementen: element-schema, Wiki/Actoren en Wiki/Rollen

- **Aanleiding:** actoren/rollen werden inconsistent behandeld — soms als BO vastgelegd (2× `archimate_type: business-actor`, 4× "(actor)"-annotatie in index.md), bij entiteitendekking altijd n.v.t. Besloten (goedgekeurd plan): actoren en rollen krijgen eigen pagina's naast bedrijfsobjecten.
- **Schema-wijzigingen:**
  - Frontmatter `type: bedrijfsobject` → `type: element` op alle 314 BO-pagina's (gescript). `archimate_type` uitgebreid met `business-actor`/`business-role` en is nu de enige drager van het specifieke elementtype.
  - Nieuwe platte mappen `Wiki/Actoren/` en `Wiki/Rollen/`. Twee-pagina-patroon: een begrip dat actor/rol én BO is krijgt twee pagina's met cross-links via nieuw frontmatter-veld `element_tegenhangers`; beide mogen dezelfde `ggm_guid` dragen.
  - Skills hernoemd: `/assess-bo` → `/assess-element`, `/write-bo` → `/write-element`; `templates/bedrijfsobject.md` → `templates/element.md`. Alle verwijzingen bijgewerkt (ingest, audit-definities, bo-coverage, coverage, entiteitendekking, lint, onderwerpoverzicht-template, CLAUDE.md).
  - Scripts bijgewerkt op de nieuwe type-waarde: `entiteitendekking.py`, `export_ggm_csv.py`, `generate_ggm_enrich_bo.py`. Dry-run bevestigt: alle 314 pagina's worden nog gevonden.
- **Nieuwe naslagpagina:** [[Wiki/GEMMA/actoren-en-rollen|Actoren en rollen]] — ArchiMate-definities (Business Actor / Business Role) met elk 6 diagnostische vragen plus beslisvraag (wie handelt vs. in welke verantwoordelijkheid). Doelgroep is expliciet géén actor/rol maar een BO-classificatie; `assess-element` Stap 2-tabel hierop gecorrigeerd. Nieuwe Stap 2b (actor/rol-toets) in assess-element en Stap 11 (actor/rol-pagina's) in write-element.
- **Bestaande mismatches gemigreerd (4):** medewerker, organisatorische-eenheid, schuldeiser en signaalpartner hebben nu elk een actor-pagina in `Wiki/Actoren/` naast hun BO-pagina (BO-frontmatter gecorrigeerd naar `business-object`, cross-links beide kanten op). Index uitgebreid met secties Actoren en Rollen.
- **Vervolg:** nieuwe skill `audit-actoren` (retrofit-sweep over entiteitendekking-rapporten + bronsamenvattingen), daarna entiteitendekking.py-matching op actor/rol-pagina's en rapportregeneratie.


## [2026-07-08] fix | n.v.t.-entiteiten telden stilzwijgend mee als "ondersteunend aan BO"

- **Aanleiding:** vraag hoe de n.v.t.-dekking geteld wordt, legde bloot dat `n.v.t.` (abstract/proces/actor/rol — entiteiten die nooit kandidaat zijn voor een BO-match) in de statistiekregels meetelde als "ondersteunend aan BO", puur omdat de tekst geen `⚠️` bevat (`ondersteunend = sum(... if '⚠️' not in dekking)`). Dat vertekende het dekkingspercentage: bij `0-bestuur-politiek-en-ondersteuning.md` bleken 4 van de 9 "ondersteunend"-entiteiten eigenlijk n.v.t. te zijn (Aanwezige Deelnemer, Collegelid, Indiener, Raadslid).
- **Fix:** nieuwe aparte telling `nvt` in `process_beleidsdomein()`, uitgesloten uit `ondersteunend`. Dekkingspercentage overal herberekend als `(met BO + ondersteunend) / (totaal − n.v.t.)` in plaats van `/ totaal` — in `_bd_stats_line`, de taakveld-Beoordeling, en `totaaloverzicht.md` (nieuwe kolom "n.v.t." toegevoegd aan de tabel, kopregel en hiaten-rij aangepast op de extra kolom).
- **Resultaat na regeneratie:** totale dekking 82% (753/917, met n.v.t. impliciet meegeteld) → 81% (694/858 relevante) — vergelijkbaar getal, maar nu een eerlijke noemer die alleen daadwerkelijk BO-relevante entiteiten meet. Skill-doc (`.claude/commands/entiteitendekking.md`, sectie Totaaloverzicht/Rapportstructuur) bijgewerkt met de nieuwe kolom en berekeningswijze.

## [2026-07-08] triage | 44 van de 72 "ter discussie"-ambiguïteiten opgelost via bo_via_kandidaten

- **Aanleiding:** vervolg op het dekking-herontwerp hieronder. De 72 entiteiten die na regeneratie als `⚠️ ter discussie` gemarkeerd stonden, zijn stuk voor stuk beoordeeld: GGM-definitie van de entiteit vergeleken met de `bo_definitie` van elke kandidaat-BO.
- **Bug gevonden tijdens triage-voorbereiding:** kandidaten werden niet gededupliceerd op BO-pagina — twee GGM-GUID's die via `ggm_duplicaat_entiteiten` aan dezelfde BO-pagina hangen (bijv. Buurt in RSGBPlus én BAG) telden als twee aparte kandidaten. Gefixt in `compute_dekking` (dedupliceren op `bo_by_guid[...]['path']` vóór scoring) — loste `Geo-Object` meteen op (was Pand vs. Pand) en maakte `Areaal`'s Buurt/Wijk-ambiguïteit correct 2-weg i.p.v. 4-weg.
- **Uitkomst van de triage (72 items):**
  - **44 — eenduidige winnaar:** geregistreerd via `bo_via_kandidaten` op de gekozen BO-pagina's (31 pagina's geraakt, sommige met meerdere entries — bijv. Schuldhulptraject kreeg er 5: Begeleiding, Begeleidingssoort, Oplossing, Oplossingssoort, Stabilisatie — stuk voor stuk fasen/activiteiten van het traject, niet van de regeling).
  - **7 — inherente unie/boventype, bewust niet geforceerd:** AdresseerbaarObject, AdresseerbaarObjectAanduiding, VerblijfadresIngeschrevenNatuurlijkPersoon (eigen definitie zegt letterlijk "X, Y, of Z"), Norm ("Omgevingswaarde of omgevingsnorm"), Beheerobject, FunctioneelGebied, CMDB-item, Erfgoed Object — deze BOventypen omvatten al hun kandidaten, een enkele winnaar zou onterecht zijn.
  - **10 — geen enkele kandidaat past goed:** Leveringscomponent/-type/-specificatie, Sociale Groep/Relatie, Sector/Subsidie/Taak, Reservering/Zaal, Logboek, Areaal (ecologisch "areaal" ≠ Buurt/Wijk), AdresBuitenland, Huishouden, Nationaliteit (attribuut van NatuurlijkPersoon, geen van beide kandidaten past), Beslissing (generiek) — blijven `⚠️ ter discussie` staan, geen bo_via_kandidaten geregistreerd om geen valse zekerheid te creëren.
- **GGM-datakwaliteitsbevindingen tijdens triage (niet gefixt, alleen gesignaleerd):** `Risicobron`'s documentatie is woordelijk identiek aan die van `Activiteit Omgevingswet` (copy-paste-fout in het GGM); `Linkbaar CMDB-item`'s documentatie luidt letterlijk "Niet opnemen"; `Kandidaat` (Inkoop-domein) heeft een HR-context-definitie ("iemand die een baan wil"); `Belijning` (Sport-domein) se definitie beschrijft verkeersbelijning, niet sportvelden; `Loopbaanstap`'s definitie lijkt eveneens uit een HR-context gekopieerd ondanks Onderwijs-domein.
- **Resultaat na regeneratie:** `⚠️ ter discussie`-items 72 → 28 (de 7 boventype- + 10 geen-match-gevallen, plus enkele niet apart getelde randgevallen); `review.md` 321 → 289 regels; totale dekking 77% → 82%.

## [2026-07-08] ontwerp+fix | Dekking-vinden herontworpen: kandidaten verzamelen + scoren i.p.v. één BFS

- **Aanleiding:** vervolg op de sibling-hop-fix hieronder. Verificatie van die fix legde een verwant geval bloot (`Normwaarde` viel terug op `via Locatie → Activiteit`, een generieke bouwsteen als tussenstation) — dezelfde soort fout via associaties i.p.v. generalisatie. Op verzoek eerst een ontwerp vastgelegd (plan `/home/mark/.claude/plans/imperative-launching-bachman.md`) met vier manieren om dekking te vinden, geordend naar betrouwbaarheid (directe match → generalisatie-omhoog → aggregatie-omhoog → associaties), vóór verdere code-wijzigingen.
- **Empirische verificatie van `classify_entity`** (nog niet eerder tegen de dataset getoetst): regels tegen alle 954 GGM-entiteiten gedraaid. Vier gebreken gevonden en gefixt:
  - **D1:** de `onderdeel`-naamgok ("regel"/"sluiting" als kale substring) gaf fout-positieven op `Maatregel*`-familie (6×), `Uitsluitingsgrond`, `Regeling`/`Regeltekst`/`Toepasbare Regel`/`Uitvoeringsregel` (juridische "regel"-betekenis, niet "regel-als-onderdeel") en `Aanwezige Deelnemer` (via "deel" in "Deelnemer"). Opgelost met een expliciete `ONDERDEEL_UITZONDERINGEN`-lijst.
  - **D2/D3:** `ROLE_SUFFIXES` miste `houder/eigenaar/indiener/contactpersoon`, `PROCESS_WORDS` miste `aanvraag/melding/beschikking` — ondanks tientallen entiteiten in de dataset die hierop gebouwd zijn (`AanvraagOfMelding`-, `Melding`-, `Beschikking`-families). Beide toegevoegd; ~30 entiteiten verschuiven van `detail` naar `rol`/`proces` (dus instant `n.v.t.`).
  - **D4:** regel "≤4 attrs zonder BO-associatie" (209 entiteiten, 31% van alles) kreeg `confidence='medium'` en werd dus niet naar `review.md` gerouteerd, terwijl er even weinig structureel signaal is als bij de `low`-vangnetregel. Nu ook `low`.
- **Bevinding B — domeinspecifieke exceptie verwijderd:** `find_excluded_ids()` beschermde geo-afstammelingen met `beleidsdomein == 'BAG'` van uitsluiting (hardcoded domeinnaam). Onderzoek: `Geo-Object` heeft maar 20 generalisatie-kinderen, en de enige BAG-entiteit (`Pand`) was toch al beschermd via `eid in bo_by_guid` — de BAG-clause deed in de praktijk niets. Vervangen door `eid in specialisatie_by_guid` — generiek, geen domeinlabel, gebruikt dezelfde curatie-registry als elders.
- **Kernherontwerp — `bfs_to_bo` vervangen door `RelationGraph.gather_dekking_candidates()` + `_score_candidates()`:** in plaats van één ongelimiteerde BFS die bij de eerste hit stopt (`hits[0]`, stille tie-break), nu twee fasen:
  1. **Kandidaten verzamelen:** (a) generalisatie-omhoog-keten (enkelvoudig, deterministisch — elke entiteit heeft precies één ouder), (b) eigen generalisatie-kinderen (alleen vanaf de startentiteit, depth 1), (c) **alleen als (a)/(b) niets vinden**: associaties, hard begrensd tot 2 hops, nooit chainend voorbij de eigen buurt van de startentiteit.
  2. **Kandidaten scoren:** minste hops wint, dan zelfde beleidsdomein, dan naam-overlap-bevestiging (CamelCase-woord gedeeld met de kandidaat-BO). Blijven er na alle drie criteria nog kandidaten gelijk staan, dan is dat een **echte ambiguïteit** — geen automatische keuze meer, resultaat wordt `⚠️ ter discussie tussen [[BO1]] / [[BO2]]` (match_kind `ambigu`, altijd naar `review.md` ongeacht classify_entity-confidence).
  - **Nieuwe curatie-registry `bo_via_kandidaten`** (BO-frontmatter, analoog aan `bo_subtypes`): een mens kan een ambigue uitkomst permanent beslechten; `compute_dekking` checkt dit als stap 0, vóór alle heuristiek, zodat een eenmaal gekozen winnaar niet elke run opnieuw "ter discussie" toont.
- **Bijvangst tijdens verificatie:** de "5 legitieme 2-hop associatieketens" die de vorige fix nog goedkeurde (bijv. `Kast via VLogInfo → Verkeerstelling`) bleken bij nadere inspectie **3-hop kettingen** (`Kast → VLogInfo → Sensor → Verkeerstelling`) die door de path-weergave (alleen `path[0]` getoond) leken op 2 hops — het nieuwe ontwerp verwerpt deze terecht ook (`⚠️ geen BO bereikbaar`).
- **Resultaat na regeneratie:** 72 entiteiten wiki-breed nu expliciet `⚠️ ter discussie` (voorheen stil opgelost, vaak fout); `review.md` van 97 → 450 regels (D4 + ambiguïteit maken eerder verborgen onzekerheid zichtbaar); totale dekking 91% (oorspronkelijk, met sibling-hop-bug) → 77% (na beide fixes) — dit legt reële hiaten en ambiguïteiten bloot die eerder achter overmoedige `via X →`-teksten schuilgingen. `entiteitendekking_sync_bo.py` (stap 5, BO-frontmatter-sync) nog niet gedraaid.

## [2026-07-08] fix | bfs_to_bo volgde generalisatie-richting niet consequent (sibling-hop-bug)

- **Aanleiding:** vraag over Leidingelement/Leiding in domein 8 legde bloot dat `via Beheerobject → Waterobject` klopt noch structureel — Leidingelement en Waterobject zijn beide slechts generalisatie-kinderen van het abstracte Beheerobject, geen relatie tot elkaar. Kwantificering toonde dat dit **alle 29** `via X →`-regels in de hele wiki betrof: elke ene volgde exact hetzelfde patroon (eerst omhoog via `gen_parent` naar een gedeeld boventype, dan weer omlaag/zijwaarts naar een willekeurige neef die toevallig al een BO had), geen enkele was een echte specialisatie-keten van de entiteit zelf.
- **Grondoorzaak:** `bfs_to_bo()` in `tools/entiteitendekking.py` verkende bij elke node zowel `gen_parent` (omhoog) als `gen_children` (omlaag) en `assoc` (zijwaarts), ongeacht hoe die node bereikt was — een omhoog-stap gevolgd door een omlaag- of zijwaartse stap levert een neef/cousin op, geen structurele dekking.
- **Twee iteraties, één principe:** afdaling via `gen_children` mag alleen vanaf de startentiteit zelf (nooit na enige hop); zodra de wandeling via `gen_parent` omhoog is gegaan, mag alleen verder omhoog worden gevolgd (geen associaties meer) — "volg specialisaties tot je een BO vindt, vanuit specialisatie niet doorgaan naar associaties". Eerste iteratie loste alleen de omhoog-dan-omlaag-hop op maar liet omhoog-dan-associatie-ketens (Bak → Beheerobject → Melding → Medewerker) en zijwaarts-dan-omlaag (Logboek → [assoc] → Beheerobject → Waterobject) toe; tweede iteratie sloot beide.
- **Resultaat na regeneratie (`entiteitendekking.py --all`):** van 29 naar 5 `via`-regels, en de resterende 5 zijn legitieme 2-hop associatieketens tussen entiteiten met weinig generalisatie-kinderen (0-5), geen sibling-artefacten meer. Leidingelement valt nu terug op de naam-heuristiek en matcht correct op Rioolleiding (synoniem "Leiding").
- **Dekkingscijfers dalen navenant** (waren kunstmatig hoog door de bug): totaal 91%→87% (836→799 gedekt), Beheer Openbare Ruimte (domein 8) 96%→73% — dit legt ~19 eerder verborgen echte hiaten in dat beleidsdomein bloot. `totaaloverzicht.md` en 8 taakveldrapporten geregenereerd (`analyse_ggm_dekking`-sync naar BO-pagina's nog niet gedraaid).

## [2026-07-08] taxonomie | "Type dekking" volledig herzien: Hernoemd, Specialisatie, Onderdeel

- **Aanleiding:** vervolg op de Rioolput/Put-fix hieronder — gebruiker vroeg een complete, functionele inventarisatie van alle relatietypen tussen een GGM-entiteit en een BO ("subtypen en generalisaties moeten correct weergegeven worden, net als duplicaten, homoniemen en synoniemen"), in plaats van losse patches. Uitgewerkt in twee planningsrondes (functionele taxonomie eerst, techniek pas daarna).
- **Taxonomie vastgesteld:** A — Dit ís het BO (Exacte match, **Hernoemd** [voegt de oude "synoniem" en "duplicaat" samen — dekking gaat uit van het GGM, of een concept nu één keer onder een andere naam of dubbel gemodelleerd is, is dekking-technisch hetzelfde geval], Homoniem); B1 — specialisatie tussen twee eigen BO's (geen apart label); B2 — **Specialisatie** zonder eigen BO (redactionele keuze, geen BO-criteria-tekort); C — geen zelfstandig BO, getoetst aan de zes BO-criteria (**Onderdeel**, Detail, Classificatie, Rol, Proces, Abstract, Generieke bouwsteen, Geen BO bereikbaar).
- **Drie concrete fixes in `tools/entiteitendekking.py`:**
  1. **Hernoemd-fusie**: `ggm_duplicaat_entiteiten`-registraties en letterlijke naamswijzigingen kregen voorheen allebei `entiteitstype: synoniem` met tekst "BO hernoemd: X" — misleidend voor duplicaten (geen hernoeming, een dubbele modellering). Nu apart gelabeld met eigen tekst ("Hernoemd naar X (dubbel gemodelleerd in GGM, zie ggm_duplicaat_entiteiten)"). Bijvangst: Sportterrein-regel in taakveld 8 toont nu `hernoemd` i.p.v. `synoniem`.
  2. **Specialisatie (B2)**: `bo_subtypes`-registraties met `ggm_attribuut: generalisatie` (bijv. Brug/Viaduct/Flyover/Rioolput als kind van Kunstwerk/Put) werden nooit gelezen door `compute_dekking()` — vielen terug op de generieke graph-search, die soms de verkeerde/geen BO vond (de "Brug via Overbruggingsobject → Faunapassage"-bug: Overbruggingsobject zelf is geen BO, dus de zoektocht kwam toevallig uit bij sibling Ecoduct/Faunapassage i.p.v. Kunstwerk). Nieuwe registratie `specialisatie_by_guid`, gecheckt als hoogste-prioriteitsstap vóór alle heuristieken.
  3. **Onderdeel** (nieuw, structureel): van de 87 echte Aggregation-relaties in het GGM werden er voorheen slechts 2 herkend (via een fragiele naam-heuristiek op "deel"/"regel"/etc.). Nieuwe `_walk_aggregation_to_bo()` loopt de aggregatie-keten (deel→geheel) omhoog tot een BO gevonden wordt. **Tijdens verificatie bleek de bestaande `agg_parent`-richting in `RelationGraph` averechts** (bevat-relaties zoals "Beschikking bevat Onderdeel beschikking" hebben source=geheel/target=deel, niet andersom) — nieuw `agg_whole`-dict toegevoegd met de juiste deel→geheel-richting. Resultaat na fix: 19 correcte matches (bijv. Aflossing/Betaalcomponent/Correctie → Vordering; Krediethypotheek/Leenbijstand → Debiteur).
- **`tools/entiteitendekking_sync_bo.py`**: één regel (`is_synoniem`-check van `'synoniem'` naar `'hernoemd'`) — de rest van het script leidt duplicaat/via-status al onafhankelijk af via GUID-vergelijking.
- **Regeneratie:** `entiteitendekking.py --all` (12 taakveldrapporten, matches ongewijzigd op 233 — specialisatie/onderdeel tellen zoals hun al-werkende buren als "ondersteunend", geen statistiekverschuiving) + `entiteitendekking_sync_bo.py` (28 BO's bijgewerkt, o.a. kunstwerk.md, put.md, vordering.md, debiteur.md, aflossingsplan.md, draagkracht.md, aflossing.md).
- **Niet opgelost, gesignaleerd:** GGM-entiteit "Beschikking" en "Vordering" bestaan elk dubbel in het GGM (andere beleidsdomeinen, andere GUID's) — al zichtbaar via de bestaande naam-duplicaat-heuristiek ("vermoedelijk duplicaat — zie ggm_duplicaat_entiteiten" op beschikking.md/vordering.md), niet nieuw geïntroduceerd door deze fix maar wel blootgelegd tijdens verificatie.

## [2026-07-08] fix | BO Rioolput hernoemd naar Put + compute_dekking bugfix

- **Aanleiding:** gebruiker signaleerde een verwarrende regel in `Wiki/Analyses/entiteitendekking/8-...md`: "Rioolput | beschrijft Rioolput". Onderzoek wees uit dat GGM-entiteit "Put" (niet-abstract, generalisatie-ouder van Aansluitput/Drainageput/Filterput/Infiltratieput/**Rioolput**) was hernoemd naar BO-naam "Rioolput" — een naam die zelf al bezet was door één van de eigen generalisatie-kinderen. De hernoeming was destijds nodig om te disambigueren van een GGM-homoniem "Put" in beleidsdomein Archeologie.
- **compute_dekking()-bugfix** (`tools/entiteitendekking.py`): de naam-duplicaat-stap liep vóór de graph-search en matchte via `bo_by_name`'s dubbele indexering (op zowel BO-naam als `ggm_entiteit`) op elke naamgelijkenis, ook toevallige. Daardoor werd het echte generalisatie-kind Rioolput ten onrechte als "duplicaat" gelabeld i.p.v. "graph", en werd de Archeologie-Put — al expliciet als homoniem (ander concept) geregistreerd in `bo_homoniemen` — tegenstrijdig ook als "vermoedelijk duplicaat" gepresenteerd. Fix: graph-search vóór naam-duplicaat-check, plus uitsluiting van entiteiten die al als `bo_homoniemen` geregistreerd staan.
- **Herstel bij de bron:** in plaats van de BO-naam aan te passen is de disambiguatie omgedraaid — de BO behoudt zijn letterlijke GGM-naam "Put" (`git mv rioolput.md → put.md`, `naam: Put`), Rioolput is toegevoegd als 4e subtype (naast Drainageput/Filterput/Infiltratieput, was eerder ontbrekend), en `bo_homoniemen`/`## Naamkeuze` documenteren nu dat een toekomstige Archeologie-Put-pagina de naam "Archeologieput" moet gebruiken (niet "Rioolput").
- **Cross-referenties bijgewerkt:** `kolk.md`, `rioolleiding.md` (2x), `Wiki/index.md`, Bronsamenvatting `gwr-twenterand-2024-2028.md`.
- **Regeneratie:** `entiteitendekking.py --all` (12 taakveldrapporten) + `entiteitendekking_sync_bo.py` (`analyse_ggm_dekking` op 15 BO's herzien door de compute_dekking-fix, waarvan Put zelf ook door de hernoeming).
- **Bekend, niet opgelost:** `kolk.md` registreert zichzelf als generalisatie-kind van Put ("Kolk is een specialisatie van Put"), maar `put.md` registreert Kolk terug als gewone associatie — inconsistent relatietype tussen beide kanten, buiten scope van deze fix.

## [2026-07-08] opruiming | ggm-vergelijking skill en analyses verwijderd

- **Aanleiding:** `/entiteitendekking` vervangt `/ggm-vergelijking` volledig (uniforme analyse per taakveld/beleidsdomein sinds eerdere migratie) — de oude skill en bijbehorende per-onderwerp analyses waren dode gewichten.
- **Verwijderd:** skill `.claude/commands/ggm-vergelijking.md`, script `tools/ggm_vergelijking_prep.py`, map `Wiki/Analyses/ggm-vergelijking/` (32 onderwerpanalyses) en `Wiki/Analyses/ggm-vergelijkingen.md` (totaaloverzicht).
- **Referenties opgeschoond:** dode links in `Wiki/index.md` verwijderd; kruisverwijzingen naar `/ggm-vergelijking` in `bo-coverage.md`, `domain-status.md`, `assess-bo.md`, `coverage.md` en `ingest.md` omgezet naar `/entiteitendekking`. Historische "vervangt ..."-notities in `CLAUDE.md` en `entiteitendekking.py`/`.md` ongewijzigd gelaten (lineage, geen dode link).

## [2026-07-07] herbeoordeling | Entiteitendekking 99 Kern (BAG/RGBZPlus/RSGBPlus) — 12 hiaten opgeheven

- **Aanleiding:** gebruiker vroeg dezelfde herbeoordeling als bij Beheer Openbare Ruimte voor het 99-Kern-taakveld (BAG, RGBZPlus, RSGBPlus), met specifieke aandacht voor RSGB.
- **Verificatie tegen daadwerkelijke GGM-relaties** (`Wiki/GGM/99-kern/*.md`, `ggm_parsed.json`), vijf categorieën bevindingen:
  - **Route-fouten via abstracte tussenstations (4 rijen):** Huishouden, Rechtspersoon, AdresBuitenland en Nationaliteit hingen via een ver cross-domein BO (Woonboot, Parkeervergunning, Gemeentebegrafenis) terwijl een directe GGM-relatie naar Ingeschreven Persoon resp. Niet-Natuurlijk Persoon binnen hetzelfde domein bestond. Rechtspersoon was bovendien inconsistent getypeerd (Entiteitstype "detail", Beoordeling zei "abstract") — nu consistent "abstract".
  - **RGBZ rol-attributen ten onrechte aan Wijk gekoppeld (3 rijen):** AfwijkendBuitenlandsCorrespondentieadresRol, AfwijkendCorrespondentiePostadresRol en ContactpersoonRol zijn volgens hun eigen GGM-documentatie letterlijk gegevens "van BETROKKENE in zijn/haar ROL in de ZAAK" — gekoppeld via Betrokkene naar Medewerker/Organisatorische eenheid.
  - **RSGB/BAG-naamduplicaten niet doorgevoerd in de tabel (8 rijen):** Ligplaats, OpenbareRuimte, Verblijfsobject, Wijk, Woonplaats, Gemeente, Buurt en Standplaats stonden al in de proza-tekst als "dubbele modelpositie" van een bestaande BAG-BO benoemd, maar de Dekking-kolom wees nog naar een willekeurig ander BO. Nu direct naar de eigen BAG-tegenhanger gekoppeld. Standplaats en Gemeente ontbraken zelfs in de proza-opsomming — toegevoegd.
  - **BRP-persoonscluster (8 rijen), échte GGM-hiaat:** MigratieIngeschrevenNatuurlijkPersoon, NaamgebruikNatuurlijkPersoon, NationaliteitIngeschrevenNatuurlijkPersoon, SamengesteldeNaamNatuurlijkPersoon, VerblijfsrechtIngeschrevenNatuurlijkPersoon, VerstrekkingsbeperkingPartieelIngeschrevenNatuurlijkPersoon, NaamAanschrijvingNatuurlijkPersoon en NaamNatuurlijkPersoon zijn in de GGM-XMI volledig geïsoleerd (geen enkele relatie), in tegenstelling tot hun zustertak "...IngeschrevenPersoon" die wél correct routeert. Onderbouwd vanuit **Logisch Ontwerp BRP 2025.Q1** (RvIG, al aanwezig en eerder gebruikt voor Ingeschreven Persoon/Reisdocument/Huwelijk) — bevestigt dat dit reguliere gegevenscategorieën "van de ingeschrevene" zijn (§2.1.4.9 Naamgebruik groep 61, categorie 10/60 Verblijfstitel, rubriek 35.95.13 Verstrekkingsbeperking). Gekoppeld aan Ingeschreven Persoon; teruggemeld als #93 (type structuur) omdat de GGM-relatie zelf ontbreekt.
  - **Generieke bouwstenen met misleidende Dekking (13 rijen):** 99-Kern geo/media-typen (Locatie, Punt, Lijn, Gebied + groep-varianten, Foto, Periode, Video-opname) en RGBZ-metadata (FormeleHistorie, MaterieleHistorie, StrijdigheidOfNietigheid) wijzen naar tientallen BO's, niet naar één. Dekking-tekst genormaliseerd naar "generieke bouwsteen — gebruikt door meerdere BO's" in plaats van één toevallig doel-BO.
- **Niet gewijzigd — echte resterende hiaten (7):** BinnenlandsAdres (BAG), CorrespondentieadresBuitenland, Land, Provincie, Rekeningnummer, VerblijfBuitenland, VerblijfBuitenlandSubject.
- **Resultaat:** RGBZPlus: niet gedekt 4→0 (dekking 89%→100%). RSGBPlus: niet gedekt 14→6 (dekking 85%→94%). Taakveld 99 Kern totaal: niet gedekt 19→7 (dekking 88%→95%). Totaaloverzicht: 101→89 niet gedekt (89%→90%).
- **Bijgewerkt:** [[Wiki/Analyses/entiteitendekking/99-kern]] (tabelcorrecties, Beoordeling-tekst, tellingen), [[Wiki/Analyses/entiteitendekking/totaaloverzicht]], [[Wiki/Analyses/ggm-terugmeldingen]] (#93, type structuur).

## [2026-07-07] herbeoordeling | Entiteitendekking 8 Volkshuisvesting — Beheer Openbare Ruimte, 7 hiaten opgeheven

- **Aanleiding:** gebruiker vroeg herbeoordeling van de niet-gedekte GGM-entiteiten in Beheer Openbare Ruimte — vermoeden dat detailobjecten ten onrechte ongekoppeld stonden.
- **Verificatie tegen GGM-Generalization-hiërarchie** (`Wiki/GGM/8-volkshuisvesting-leefomgeving/beheer-openbare-ruimte.md`) en de bestaande BO-pagina [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/kunstwerk|Kunstwerk]] (die al documenteert dat Brug/Viaduct/Flyover/Kademuur/Keermuur bewust als Kunstwerk-subtype zijn opgenomen, ook al zijn dit GGM-kinderen van Overbruggingsobject resp. Scheiding, niet van Kunstwerk zelf):
  - **8 entiteiten alsnog gekoppeld** aan de bestaande BO Kunstwerk (Brug, Flyover, Kademuur, Keermuur, Tunnelobject, Viaduct als detail; Overbruggingsobject en Scheiding als abstract met verwijzing naar hun gedekte GGM-kinderen, waaronder Ecoduct → Faunapassage en Geluidscherm → eigen BO). Dit waren geen echte hiaten maar tabelkoppelingen die niet waren ingevuld ondanks dat de onderbouwing al in de Beoordeling-tekst en op de BO-pagina stond.
  - **5 verkeerd gekoppelde entiteiten gecorrigeerd:** Klimplant en SolitairePlant (waren aan Woningbouwplan gekoppeld, horen als Vegetatieobject-subtype bij Boom), Omgevingsvergunning (Dekking wees naar Woningbouwplan terwijl de Beoordeling-kolom al "Vergunningen en ontheffingen" aangaf), Fietsparkeervoorziening (was aan WMO-Voorziening gekoppeld; is een Meubilair-subtype, al eerder afgewezen als BO onder de naam "fietsenrek" in het onderwerpoverzicht) en Fase/Oplevering (was aan WMO-Levering gekoppeld zonder enige onderbouwing; geen GGM-definitie beschikbaar, gemarkeerd als 🔍 verificatie nodig).
- **Niet gewijzigd:** het beheerproces-cluster (Storing, Inspectie, Schouwronde, Onderhoud, Logboek, Taak) blijft een governance-/procesgat, geen BO-hiaat.
- **Sportterrein nader onderzocht via `/assess-bo` met Beleidsnota Sport en Bewegen 2025-2032:** haalt 6/6 BO-criteria (elf met naam genoemde sportparken, eigen levenscyclus, relaties), maar bij GGM-matching (`/write-bo` stap 4b) bleek Sportterrein (taakveld 8, Model IMBOR) vermoedelijk een tweede GGM-representatie van de al bestaande BO [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/sport/sportpark|Sportpark]] (taakveld 5, beleidsdomein Sport) — Sportpark noemt "Sportterrein" zelfs expliciet als eigen GGM-synoniem. Geen nieuwe BO-pagina aangemaakt (zou een echte duplicaat zijn geworden); in plaats daarvan gekoppeld aan Sportpark en teruggemeld. Ambigu blijft of Sportterrein (attributen veldnummer/sportcomplex) eerder het individuele-veld-niveau betreft (BO Veld) — expliciet **ter discussie** gelaten, niet gegokt.
- **Resultaat:** Beheer Openbare Ruimte: niet gedekt 29→22, ondersteunend 34→41 (dekking 64%→73%). Taakveld 8: niet gedekt 29→22 (dekking 76%→82%). Totaaloverzicht: 108→101 niet gedekt (88%→89%).
- **Bijgewerkt:** [[Wiki/Analyses/entiteitendekking/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing]] (tabelcorrecties, Beoordeling-tekst, tellingen), [[Wiki/Analyses/entiteitendekking/totaaloverzicht]], [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/sport/sportpark]] (ggm_duplicaat_entiteiten, GGM-duplicaten-sectie), [[Wiki/Analyses/ggm-terugmeldingen]] (#92, type duplicaat).
- **Gecontroleerd maar geen actie nodig:** GWR Twenterand (2026-06-26 geïngest) bleek al correct in de bronnenlijst van het onderwerpoverzicht Milieu opgenomen, niet ontbrekend zoals aanvankelijk vermoed.

## [2026-07-07] redactie | Entiteitendekking 6 Sociaal Domein — ingekort

- **Actie:** de Beoordeling-sectie en tabelannotaties van [[Wiki/Analyses/entiteitendekking/6-sociaal-domein]] herschreven om alleen de huidige stand te beschrijven (classificatie, dekkingsroute en onderbouwing), zonder change-log-taal ("herbeoordeling 2026-07-07", "ronde 1/2", "route gecorrigeerd/toegevoegd", "hiaat opgeheven"). De onderliggende onderbouwing (GGM-Generalization-verificatie, brongrondslag, cross-links tussen Inkomen/Sociaal Domein Generiek) is behouden, alleen de historische framing is verwijderd. Geen inhoudelijke wijzigingen aan classificaties, routes of tellingen.

## [2026-07-07] ingest | Boek 1 BW Titel 17 (Levensonderhoud) en Wet studiefinanciering 2000 — Onderhoudsplicht/Studiefinanciering opgelost

- **Aanleiding:** vervolg op de her-mining hieronder — voor Onderhoudsplicht/-verhouding en Studiefinanciering was geen bruikbare bron gevonden in `sgr-19-gegevensregister-suwi.md`; aanbeveling was gerichte nieuwe bronnen te zoeken.
- **Bronnen toegevoegd:** `Sources/Onderwerpen/Werk en Inkomen/burgerlijk-wetboek-boek-1-titel-17-levensonderhoud.md` (art. 392-408, opgehaald via curl van wetten.overheid.nl) en `wet-studiefinanciering-2000-bwbr0011453.md` (Hoofdstuk 1-2 volledig + kernartikelen Hoofdstuk 3). Beide zijn selectieve uittreksels, geen volledige wetteksten.
- **Onverwachte bevinding (verificatie tegen `ggm_parsed.json`):** bij het herclassificeren van Studiefinanciering bleek de hele `Inkomstencomponent`-tak (Primair + Secundair inkomstencomponent en subtypen) dezelfde dekkingsroute te missen die `Vermogenscomponent` al wel had sinds de vorige herbeoordeling — en twee Primair-subtypen (`Ander inkomen`, `Hobby`) plus de complete `Secundair inkomstencomponent`-familie (`Dertiende maand`, `Heffingskorting`, `Inkomstenvermindering`, `Vergoeding`, `Vakantiegeld`) waren nooit aan hun bovenliggend type gekoppeld. Alles geverifieerd via de daadwerkelijke GGM-Generalization-relaties (niet aangenomen).
- **Onderhoudsplicht/Onderhoudsverhouding:** blijven `detail`, geen BO — civielrechtelijke verhouding, geen gemeentelijke taak. Krijgen wel een route (via Profiel → Client) op basis van de GGM-documentatie zelf ("opgenomen in het profiel van de klant"). Expliciet onderscheiden van Alimentatie (verhaal-aan-gemeente vs. rechtstreeks-aan-cliënt) — een eerder overwogen cross-link tussen beide bleek bij verificatie onjuist en is niet doorgevoerd.
- **Studiefinanciering:** herclassificeerd van `detail` naar `component`-subtype van Primair inkomstencomponent (DUO kent toe, gemeente registreert alleen — zelfde patroon als Uitkering/Pensioen). Cross-gelinkt met Inkomen's `Gestopte studiefinanciering`.
- **Resultaat:** 17 hiaten opgeheven in Sociaal Domein Generiek (bovenop de 2 uit de eerdere herbeoordeling). Taakveld 6: niet gedekt 56→39, ondersteunend 180→197. Totaaloverzicht: 88% dekking (was 86%).
- **Bijgewerkt:** [[Wiki/Analyses/entiteitendekking/6-sociaal-domein]] (Beoordeling-paragrafen, tabelcorrecties, tellingen), [[Wiki/Analyses/entiteitendekking/totaaloverzicht]], nieuwe bronsamenvattingen [[Wiki/Bronsamenvattingen/Werk en Inkomen/burgerlijk-wetboek-boek-1-titel-17-levensonderhoud]] en [[Wiki/Bronsamenvattingen/Werk en Inkomen/wet-studiefinanciering-2000]], [[Wiki/index.md]].

## [2026-07-07] analyse | Her-mining sgr-19-gegevensregister-suwi.md (vermogenstoets/Onderhoudsplichtige/Studiefinanciering)

- **Aanleiding:** vervolg op de herbeoordeling Inkomen/Sociaal Domein Generiek hieronder — aanbeveling was om `sgr-19-gegevensregister-suwi.md` opnieuw te doorlopen voordat nieuwe bronnen gezocht worden voor Studiefinanciering/Onderhoudsplicht/vermogenstoets-detail.
- **Bevinding:** de deelmodel-diagrammen (Figuren) in dit document zijn OCR-garbled en onbruikbaar, maar de prozabeschrijvingen erboven zijn schoon en bruikbaar. RDW (§4.10) en Kadaster (§4.11) bevestigen expliciet de vermogenstoets-functie van voertuig- resp. onroerendezaakgegevens. Onderhoudsplichtige blijkt bij nadere lezing slechts een rolnaam (SuwiML-tag, geen eigen attributen); Studiefinanciering komt alleen voor als dossiernaam zonder deelmodel. Beide blijven dus een hiaat — hermining loste dit niet op, een nieuwe bron is nodig.
- **Bijgewerkt:** [[Wiki/Bronsamenvattingen/Werk en Inkomen/wet-suwi-en-sgr]] (Samenvatting, Kernbegrippen, Relevantie-sectie), [[Wiki/Analyses/entiteitendekking/6-sociaal-domein]] (sectie "Ontbrekende bronnen" bijgewerkt met resultaat).

## [2026-07-07] analyse | Herbeoordeling Inkomen & Sociaal Domein Generiek (entiteitendekking)

- **Aanleiding:** gebruiker signaleerde overlap tussen de beleidsdomeinen Inkomen en Sociaal Domein Generiek in [[Wiki/Analyses/entiteitendekking/6-sociaal-domein]] en vroeg om herbeoordeling van niet-gedekte entiteiten op duplicaten/synoniemen/homoniemen.
- **Dekkingscorrectie (vermogen):** Bankrekening, Hypotheek, Motorvoertuig en Onroerend goed consistent gerouteerd via Vermogenscomponent → Profiel → Client — de vraag is "is dit een vermogensbestanddeel van de cliënt", niet "bestaat dit object elders in GEMMA voor een andere bedrijfsfunctie" (Voertuig-BO en WOZ-object zijn beide gecontroleerd en afgewezen als route: kentekenregistratie resp. OZB-heffing, geen relatie met Client). 2 hiaten opgeheven (Hypotheek, Onroerend goed); Bankrekening/Motorvoertuig kregen een correctere route. Taakveld 6: niet gedekt 58→56, ondersteunend 178→180; totaaloverzicht.md en frontmatter bijgewerkt.
- **Concept-duplicatie gedocumenteerd (inkomen):** `Component` (Inkomen), `Inkomstencomponent` (Sociaal Domein Generiek) en `Inkomen` (Schulden) bleken bij nader inzien hetzelfde concept — "de bronnen waaruit iemands inkomen bestaat" — drie keer los gemodelleerd voor drie uitvoeringscontexten (cliëntprofiel/uitkeringsberekening/WSNP-leefsituatie), in plaats van drie functioneel-verschillende homoniemen. Reden-aanvraag-subtypes (Gestopt betaald werk e.d.) zijn de beëindiging van dezelfde inkomstenbronnen als Primair-inkomstencomponent-subtypes (Betaald werk e.d.) — nu expliciet cross-gelinkt in de tabellen. Geen nieuwe BO's aangemaakt; kandidaat voor toekomstige `/assess-bo`-afweging zodra een bron bestaat.
- **Ontbrekende bronnen geïdentificeerd:** geen bron voor Stadspas, Loonbeslag/Beslag op inkomen, Reden-aanvraag-beëindigingsgebeurtenissen, Vermogen/Inkomstencomponent als onderwerp, Normafwijking. Wel (niet-gedistilleerde) bron voor Studiefinanciering/Onderhoudsplicht/vermogenstoets-detail in `sgr-19-gegevensregister-suwi.md` en voor Boete in `wet-suwi-bwbr0013060.md` (UWV-context) — aanbevolen eerst te hermijnen voordat nieuwe bronnen gezocht worden.
- **Bijgewerkt:** [[Wiki/Analyses/entiteitendekking/6-sociaal-domein]] (Beoordeling-paragrafen Inkomen/Sociaal Domein Generiek/Cross-domein observaties, nieuwe sectie "Ontbrekende bronnen", tabelcorrecties), [[Wiki/Analyses/entiteitendekking/totaaloverzicht]] (tellingen).

## [2026-07-07] analyse | Entiteitendekking — volledige refresh alle taakvelden

- **Actie:** `tools/entiteitendekking.py --all` opnieuw gedraaid; alle 12 taakveldrapporten + `totaaloverzicht.md` + `review.md` in `Wiki/Analyses/entiteitendekking/` geregenereerd.
- **Cijfers:** 916 GGM-entiteiten, 206 met BO (23%), 583 ondersteunend, 127 niet gedekt (14%), 104 BO's zonder GGM-entiteit (310 BO's totaal). Totaalrij toegevoegd aan `totaaloverzicht.md` (het script genereert deze zelf nog niet) en geverifieerd tegen kolomsommen.
- **Review:** 105 low-confidence classificaties beoordeeld met domeinkennis; 59 items geherclassificeerd (vooral detail → component/abstract/classificatie/proces), 46 bevestigd als 'detail' met verfijnde onderbouwing. Grootste clusters: 8 Volkshuisvesting/Beheer Openbare Ruimte (25×, kunstwerk- en meubilair-subtypen, verzamelobjecten), 6 Sociaal Domein (14×, inkomstenbron-componenten), 5 Sport-Cultuur/Erfgoed (7×, opgravings- en opslagketen).
- **Inhoudelijke beoordeling** geschreven voor alle 12 rapporten (structurele patronen, functionele dekking, cross-domein observaties, naamconflicten). Zie [[Wiki/index.md]] voor de per-taakveld kernpunten.
- **Opvallende signalen:**
  - Mogelijke definitiefouten in de GGM-bron zelf bij `Vlak` en `Vulling` (Erfgoed) — aanbevolen terug te koppelen aan het GEMMA-team.
  - `Subsidie`/`Subsidieaanvraag`/`Subsidiebeschikking` (9 Interne Organisatie) vormen een zelfstandig cluster zonder eigen BO ondanks schijndekking — kandidaat voor `/assess-bo Subsidie`.
  - `Ligplaats`, `OpenbareRuimte`, `Woonplaats` (99 Kern/RSGBPlus) zijn modelduplicaten van de BAG-BO's, geen gemiste BO-kandidaten.
  - 7 Volksgezondheid en Milieu heeft de scherpste onbalans: GGM modelleert alleen de afvalketen, vijf andere beleidsdomeinen (Milieu, Dierenwelzijn, Geluid, Energie en Klimaat, Openbare Gezondheid) hebben geen GGM-tegenhanger.
- **Index:** `Wiki/index.md` bijgewerkt met alle 12 rapporten + totaaloverzicht (was alleen 9 Interne Organisatie).

## [2026-07-07] ingest | Informatiebeheer — Overheidsinformatiemodel

- **Bron:** Nationaal Archief kennisbank (5 pagina's: overheidsinformatiemodel, informatiehuishouding, ruwe gegevensobject, gegevensobject, informatieobject, metagegevens)
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Informatiebeheer/overheidsinformatiemodel|Overheidsinformatiemodel]]
- **Nieuw BO:** [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/informatieobject|Informatieobject]] — 6/6 criteria, GGM-hiaat; tweede fase in informatielevenscyclus (Document → Informatieobject → Archiefstuk)
- **BO bijgewerkt:** [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document|Document]] — lifecycle-correctie (Document ≠ synoniem van Informatieobject), levenscyclustabel 3 fasen, relatie naar Informatieobject toegevoegd
- **BO bijgewerkt:** [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archiefstuk|Archiefstuk]] — relatie naar Informatieobject als voorgaande fase toegevoegd
- **GGM-hiaat:** Informatieobject ontbreekt in GGM; de overgang Document → gearchiveerd object wordt niet als eigen entiteit gemodelleerd; terugmelding opgenomen in BO-pagina
- **Analyse:** gegevensobject geen nieuw BO; GGM-Metagegevens-package bevat modelleerpatronen (FormeleHistorie etc.), niet NA-metagegevens

## [2026-06-30] analyse | Entiteitendekking 9 Interne Organisatie

- **Pagina:** [[Wiki/Analyses/entiteitendekking/9-interne-organisatie|Entiteitendekking 9 Interne Organisatie]]
- **Scope:** 7 beleidsdomeinen (Financien, HR, ICT, Inkoop, Organisatie-indeling, Subsidies, Vastgoed), 148 GGM-entiteiten
- **Resultaat:** 44 BO-matches (30%), 94 ondersteunend, 10 niet gedekt, 9 BO-hiaten
- **ICT-specifiek:** 35 entiteiten, 10 BO-matches. Meta-model (MIM) entiteiten correct als detail geclassificeerd. CMDB-hiërarchie abstracte constructen. Niche-entiteiten (Inventaris, Toegangsmiddel, Vervoersmiddel, Telefoniegegevens) onvoldoende uitgewerkt in GGM.
- **Beoordeling:** verrijkt met structurele patronen, cross-domein observaties
- **Index:** bijgewerkt

## [2026-06-29] ingest | Informatiesystemen

- **Bronnen:** 3 (GIBIT 2025, CMDB TechTarget, VNG Handreiking Informatiebeheerplan)
- **Bronsamenvattingen:** 2 (GIBIT 2025, CMDB & Informatiebeheerplan gebundeld)
- **Nieuwe BO's:** 10 — Koppeling, Licentie, Server, Database, Software, Hardware, Netwerkcomponent, Storing (ICT), Wijzigingsverzoek, Service Level Agreement
- **Bestaande BO's bijgewerkt:** Applicatie (Koppeling, Database, Server, Licentie verplaatst van GGM-componenten naar relaties)
- **GGM-dekking:** 9 GGM exact, 1 governance-object (SLA, GGM-hiaat)
- **Homoniem:** Storing (ICT) vs. Storing (BOR) — geambigueerd met suffix
- **GGM-terugmelding:** typefout "Nertwerkcomponent" → "Netwerkcomponent"
- **Onderwerpoverzicht:** [[Wiki/Onderwerpoverzichten/informatiesystemen]] aangemaakt (21 begrippen, 12 BO's)
- **Index:** bijgewerkt met 10 nieuwe BO's en 2 bronsamenvattingen

## [2026-06-28] analyse | GGM-vergelijking Basisregistraties

- **Pagina:** [[Wiki/Analyses/ggm-vergelijking/ggm-vergelijking-basisregistraties|GGM-vergelijking Basisregistraties]]
- **Scope:** BAG (13 entiteiten) + RSGBPlus (78 in scope na filtering), totaal 91 unieke GGM-entiteiten
- **Registraties:** BAG, BRP, BRK, NHR, WOZ, BRO
- **Resultaat:** 24 van 30 BO's hebben GGM-match (80%); 6 hiaten (3× BRK-brondocumenten, 3× BRO)
- **RSGBPlus-scoping:** 21 IMGeo/BGT-entiteiten en 7 tekenwijze-hulpobjecten buiten scope; 10 BAG-duplicaten en ~12 interne varianten geconsolideerd
- **Structureel patroon:** RSGBPlus modelleert op genormaliseerd dataniveau; BO Ingeschreven Persoon absorbeert 12 detail-entiteiten (sterkste voorbeeld RSGB-normalisatie)
- **Hiaten:** BRO volledig absent in GGM (structurele lacune); BRK-brondocumenten (Stuk, Stukdeel) en Publiekrechtelijke Beperking (gemeente is bronhouder WKPB) ontbreken
- **0 BO-hiaten:** alle detail/component-entiteiten hebben dekkingsketen naar een BO
- **Totaaloverzicht** [[Wiki/Analyses/ggm-vergelijkingen|ggm-vergelijkingen]] bijgewerkt
- **Index** bijgewerkt

## [2026-06-28] analyse | GGM-vergelijking Asiel en Integratie

- **Pagina:** [[Wiki/Analyses/ggm-vergelijking/ggm-vergelijking-asiel-en-integratie|GGM-vergelijking Asiel en Integratie]]
- **Scope:** GGM-beleidsdomein Inburgering (35 entiteiten) vs. onderwerpoverzicht asiel en integratie (43 begrippen, 17 BO's)
- **Resultaat:** 15 BO's met GGM-match (88%), 2 entiteit-hiaten (Opvanglocatie, Bestuursovereenkomst — asielopvangfase), 0 BO-hiaten. Structurele dekking compleet.
- **Bevinding:** GGM dekt Wi2021-inburgeringstraject uitstekend (35 entiteiten, alle exact match); asielopvangfase (Spreidingswet 2024) structureel niet in GGM
- **Index:** analyse-pagina toegevoegd
- **Totaaloverzicht:** [[Wiki/Analyses/ggm-vergelijkingen|GGM-vergelijkingen]] bijgewerkt

## [2026-06-28] analyse | GGM-vergelijking Cultuur

- **Pagina:** [[Wiki/Analyses/ggm-vergelijking/ggm-vergelijking-cultuur|GGM-vergelijking Cultuur]]
- **Scope:** GGM-beleidsdomeinen Archeologie (17), Archief (18), Generieke Entiteiten Erfgoed (3), Monumenten (6), Musea (30) = 74 entiteiten vs. onderwerpoverzicht cultuur (49 begrippen, 8 BO's)
- **Resultaat:** 7 BO's met GGM-match (88%), 1 entiteit-hiaat (Orgel — roerend erfgoed), 0 BO-hiaten. Structurele dekking compleet.
- **Bevinding:** Musea-domein sterk Prinsenhof-gekleurd (22 van 30 entiteiten); erfgoed/archief/monumenten functioneel compleet
- **Index:** beschermde-status verwijderd (geconsolideerd met Monument), Collectie toegevoegd onder Musea
- **Totaaloverzicht:** [[Wiki/Analyses/ggm-vergelijkingen|GGM-vergelijkingen]] bijgewerkt

## [2026-06-28] analyse | GGM-vergelijking Financiën + totaaloverzicht

- **Pagina:** [[Wiki/Analyses/ggm-vergelijking/ggm-vergelijking-financien|GGM-vergelijking Financiën]]
- **Scope:** GGM-beleidsdomein Financien (24 entiteiten) vs. onderwerpoverzicht financien (29 begrippen, 14 BO's)
- **Resultaat:** 10 BO's met GGM-match (71%), 4 entiteit-hiaten (balans/verantwoording), 1 BO-hiaat (Grootboek — 5 orphan-entiteiten zonder parent-BO)
- **Totaaloverzicht:** [[Wiki/Analyses/ggm-vergelijkingen|GGM-vergelijkingen]] aangemaakt met alle 33 onderwerpen, structurele en functionele dekkingskolommen
- **Skill bijgewerkt:** `/ggm-vergelijking` — dekking-kolom in tabel 2, BO-hiaten met bronsuggesties in beoordeling, stap 5 totaaloverzicht bijwerken

## [2026-06-28] ingest | BBV en begrippenlijst gemeentebegroting (2 bronnen)

- **Bronnen:** [[Wiki/Bronsamenvattingen/Financien/besluit-begroting-en-verantwoording|Besluit begroting en verantwoording (BBV)]], [[Wiki/Bronsamenvattingen/Financien/begrippenlijst-gemeentebegroting|Begrippenlijst gemeentebegroting]]
- **Nieuwe BO's:** 4 — [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/reserve|Reserve]] (GGM-hiaat #88), [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/financiele-voorziening|Financiële Voorziening]] (GGM-hiaat #89, homoniem met Wmo-Voorziening), [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/verbonden-partij|Verbonden Partij]] (GGM-hiaat #90), [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/jaarrekening|Jaarrekening]] (GGM-hiaat #91)
- **Nieuwe begrippen:** 9 — reserve, financiële voorziening, verbonden partij, jaarrekening, programma, deelneming, bouwgrond in exploitatie, kapitaalgoed, weerstandsvermogen
- **Homoniem opgelost:** Voorziening (Wmo) ↔ Financiële Voorziening (BBV) — ondersteuning/hulp vs. balanspost verplichtingen/risico's
- **GGM-terugmeldingen:** #88 Reserve, #89 Financiële Voorziening (hiaat + homoniem), #90 Verbonden Partij, #91 Jaarrekening
- **Onderwerpoverzicht:** financien bijgewerkt (20→29 begrippen, 10→14 BO's), kolom "Type" → "Begripstype", instrument → governance-instrument
- **Skills bijgewerkt:** assess-bo (begripstype), ggm-vergelijking (entiteitstype), bo-coverage, domain-status, coverage, ingest, onderwerpoverzicht-template

## [2026-06-27] ingest | Wet SUWI en SGR 19.0 (2 bronnen)

- **Bronnen:** [[Wiki/Bronsamenvattingen/Werk en Inkomen/wet-suwi-en-sgr|Wet SUWI en Gegevensregister SUWI 19.0]] (gebundelde bronsamenvatting van wettekst + SGR datamodel)
- **Nieuwe BO's:** 4 — [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende|Werkzoekende]] (GGM exact, abstract, 25+ componenten), [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/trajectplan|Trajectplan]] (GGM-hiaat #85), [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/instrument|Instrument]] (GGM-hiaat #86, Dennis & Eva catalogus-item), [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/vacature-arbeidsmarkt|Vacature (arbeidsmarkt)]] (GGM-hiaat, homoniem HR-Vacature #87)
- **Nieuwe begrippen:** 6 — werkzoekende, trajectplan, instrument, vacature (arbeidsmarkt), Suwinet/GeVS, VUM
- **Homoniem opgelost:** Vacature (HR) ↔ Vacature (arbeidsmarkt) — gemeente als werkgever vs. gemeente als arbeidsmarktbemiddelaar; cross-links aangebracht
- **GGM-terugmeldingen:** #85 Trajectplan (hiaat), #86 Instrument (hiaat), #87 Vacature (homoniem + hiaat Werk-domein)
- **Onderwerpoverzicht:** werk-en-inkomen bijgewerkt (19→25 begrippen, 4→8 BO's)

## [2026-06-27] ingest | iStandaarden iWmo/iJw/iEb (3 bronnen)

- **Bronnen:** [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/procesbeschrijving-ijw-3.1|Procesbeschrijving iJw 3.1]], [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/informatiemodel-gizo|GIZO conceptversie]], functionele uitwerking iWmo/iJw 3.1 (→ Niet-relevant)
- **Nieuwe BO's:** 2 — [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/zorgdeclaratie|Zorgdeclaratie]] (GGM exact, homoniem HR-Declaratie), [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/eigen-bijdrage|Eigen bijdrage]] (GGM exact)
- **Nieuwe begrippen:** 8 — declaratieregel/prestatie, melding eigen bijdrage, VOT, VOW, regiebericht, uitvoeringsvariant, productafspraak
- **Verrijkt:** Toewijzing, Levering, Beschikking (procesbeschrijving + GIZO als bronnen)
- **Homoniem opgelost:** Declaratie (HR) ↔ Zorgdeclaratie (Sociaal Domein) — cross-links aangebracht
- **Herbeoordeling:** declaratie was ❌ ("financieel-administratief"), nu ✅ op basis van GGM+GIZO
- **Totaal domein:** 15 BO's, 40 begrippen, 12 bronnen

## [2026-06-27] ingest | Regeling inburgering 2021

- **Bron:** [[Wiki/Bronsamenvattingen/Asiel en Integratie/regeling-inburgering-2021|Regeling inburgering 2021]] (Rijksoverheid, BWBR0045574)
- **Nieuwe BO's:** 2 — [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/vrijstelling|Vrijstelling]] (GGM exact), [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/ontheffing|Ontheffing]] (GGM exact)
- **Nieuwe begrippen:** 5 — examenonderdeel, sociale lening, deskundigenverklaring, inburgeringsdiploma, verlengingsgrond
- **Verrijkt:** Examen (examenprocedures), Inburgeringstermijn (verlengingsgronden), MAP (urennorm), Leerroute (Z-route)
- **Homoniemen:** Vrijstelling (Leerplicht), Ontheffing (Werk) — andere concepten in andere GGM-domeinen
- **Totaal domein:** 17 BO's, 43 begrippen, 8 bronnen

## [2026-06-27] analyse | BO-dekking batch-beoordeling

- **Scope:** Alle 954 GGM Objecttype-entiteiten beoordeeld
- **Resultaat:** 192 BO's, 114 verwerkt (subtypes/componenten), 326 niet-BO, 195 BO-kandidaat (bron nodig), 127 ter discussie
- **Top-5 domeinen met BO-kandidaten:** Werk (19), Inburgering (19), RSGBPlus (13), HR (11), Generiek Jeugd en Wmo (11)
- **Bronnen-opportuniteiten:** per beleidsdomein suggesties voor brontype om kandidaten te beoordelen
- **Output:** [[Wiki/Analyses/bo-dekking|BO-dekking]] (rapport + JSON)

## [2026-06-27] ingest | Basisregistraties — BRO verwerkt

- **Bronnen:** 2 bronnen verwerkt:
  - [[Wiki/Bronsamenvattingen/Standaarden/wet-bro|Wet BRO]] (Rijksoverheid, BWBR0037095) — volledige wettekst
  - [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bro-gld|BRO Catalogus GLD]] (Geonovum) — grondwaterstandonderzoek
- **3 nieuwe BO's (alle GGM-hiaat):**
  - [[Wiki/Bedrijfsobjecten/99-kern/bro/verkenning|Verkenning]] — waarneming opbouw ondergrond (art. 19)
  - [[Wiki/Bedrijfsobjecten/99-kern/bro/constructie|Constructie]] — werk in de ondergrond (art. 21)
  - [[Wiki/Bedrijfsobjecten/99-kern/bro/gebruiksrecht|Gebruiksrecht]] — besluit/melding winnen/opslaan/bodemkwaliteit (art. 20)
- **13 nieuwe begrippen:** 4 BRO-subtypes (GMW, GMN, GLD, GAR), authentiek model, 6 stelselrollen (bronhouder, afnemer, terugmelder, dataleverancier, registratiehouder, beheerder LV), normwaarde, regeltekst
- **Stelselrollen** als cross-cutting actoren toegevoegd aan begrippentabel Basisregistraties (bronhouder, afnemer, terugmelder, dataleverancier, registratiehouder, beheerder)

## [2026-06-27] ingest | Omgevingswet — IMOW, Bbl, Wkb, Bal verwerkt

- **Bronnen:** 5 nieuwe bronnen opgehaald, 4 verwerkt als bronsamenvatting, 1 naar Niet-relevant:
  - [[Wiki/Bronsamenvattingen/Omgevingswet/imow-informatiemodel-omgevingswet|IMOW v3.0.1]] (Geonovum) — informatiemodel DSO objecttypen
  - [[Wiki/Bronsamenvattingen/Omgevingswet/besluit-bouwwerken-leefomgeving|Bbl]] (Rijksoverheid) — technische bouwvoorschriften, Wkb, meldingen
  - [[Wiki/Bronsamenvattingen/Omgevingswet/wkb-iplo-toelichting|Wkb IPLO]] (IPLO + 3 subpagina's) — kwaliteitsborging, gevolgklassen
  - [[Wiki/Bronsamenvattingen/Omgevingswet/besluit-activiteiten-leefomgeving|Bal]] (Rijksoverheid) — structuur rijksregels
  - Beleidsplan Omgevingsrecht Bernheze → Niet-relevant (bevestigt VTH Delft)
- **6 nieuwe BO's (alle exact GGM-match):**
  - [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/activiteit|Activiteit]] — gereguleerd handelen/nalaten in de fysieke leefomgeving
  - [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/gebiedsaanwijzing|Gebiedsaanwijzing]] — aanwijzing gebied met type/naam/locatie
  - [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/omgevingsnorm|Omgevingsnorm]] — norm met waarden per locatie
  - [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/omgevingswaarde|Omgevingswaarde]] — beleidsdoel fysieke leefomgeving
  - [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/juridische-regel|Juridische Regel]] — regel met juridische werkingskracht
  - [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/toepasbare-regel|Toepasbare Regel]] — vragenbomen voor DSO/Omgevingsloket
- **15 nieuwe begrippen** in onderwerpoverzicht (meldingen, energielabel, gevolgklasse, borgingsplan, etc.)
- **Signaleringen:** Activiteit is homoniem met Activiteit (Musea) in GGM. GGM Omgevingswet-domein nu 17 van 31 entiteiten beoordeeld.

## [2026-06-27] ingest | Dienstverlening — ZTC2 begeleidend document verwerkt

- **Bron:** [[Sources/Onderwerpen/Dienstverlening/ztc2-begeleidend-document|ZTC2 Begeleidend document v2.1]] (KING, 2014) — gedownload en geconverteerd via convert_pdf
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Standaarden/ztc2-informatiemodel|ZTC2 Informatiemodel]] aangevuld met context, gebruik, beheermodel en relaties met andere bouwstenen
- **BO bijgewerkt:** [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaaktype|Zaaktype]] — context over omvang (~300 attrs/rels per zaaktype) en centraal/decentraal beheer
- **Geen nieuwe BO's** — configuratie-objecttypen (Roltype, Zaakobjecttype, Eigenschap) zijn onderdelen van Zaaktype

## [2026-06-27] ingest | Dienstverlening — 7 nieuwe BO's uit RGBZPlus

- **Bron:** bestaande [[Wiki/Bronsamenvattingen/Standaarden/rgbz-informatiemodel|RGBZ bronsamenvatting]] (geen nieuwe bronnen)
- **Nieuwe BO's:** [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/besluit|Besluit]], [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/klantcontact|Klantcontact]], [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/betaling|Betaling]], [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/bedrijfsproces|Bedrijfsproces]], [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/medewerker|Medewerker]] (actor), [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/organisatorische-eenheid|Organisatorische eenheid]] (actor), [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaaktype|Zaaktype]]
- **Niet-BO:** ZAAK-Origineel (duplicaat van Zaak), Statustype (attribuut/modelleringskeuze), Status (voortgangsindicatie op Zaak), Besluittype (typering bij Besluit)
- **Onderwerpoverzicht:** [[Wiki/Onderwerpoverzichten/dienstverlening|Dienstverlening]] bijgewerkt — 27 begrippen, 13 BO's
- **Bestaande BO bijgewerkt:** [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak|Zaak]] — relaties naar nieuwe BO's (was: placeholders)
- **Aanleiding:** `/bo-coverage` analyse toonde 9 sterke kandidaten in RGBZPlus

## [2026-06-27] coverage | GGM-dekkingsanalyse gegenereerd

- **Script:** `tools/coverage_analysis.py` — volledige analyse van alle 44 beleidsdomeinen
- **Resultaat:** [[Wiki/Analyses/ggm-dekking|ggm-dekking.md]] — 954 objecttype-entiteiten, 181 BO's, 644 niet beoordeeld
- **Beleidsdomeinen zonder bronnen:** 17 (o.a. Griffie, Dak- en thuislozen, Inkomen/Diensten, Inkomen/Normafwijking, Inkomen/Reden aanvraag, Subsidies, 99 Kern)

## [2026-06-27] ingest | erfgoed — 4 bronnen verwerkt, 1 nieuw BO, 1 duplicaat opgelost

- **Bronnen:** Erfgoedwet BWBR0037521 (wetten.overheid.nl), GR Regionaal Archief Rivierenland 2024 (lokaleregelgeving), Besluit Informatiebeheer GR Cure 2021 (officielebekendmakingen), Beleidsplan Westfries Archief 2024-2027 (PDF). 2 bronnen naar Niet-relevant (portaalpagina erfgoedbeleid Utrecht, lijst beeldbepalende panden).
- **Bronsamenvattingen:** [[Wiki/Bronsamenvattingen/erfgoed/erfgoedwet|Erfgoedwet]], [[Wiki/Bronsamenvattingen/erfgoed/gr-regionaal-archief-rivierenland|GR Rivierenland]], [[Wiki/Bronsamenvattingen/erfgoed/besluit-informatiebeheer-gr-cure|Besluit Informatiebeheer Cure]], [[Wiki/Bronsamenvattingen/erfgoed/beleidsplan-westfries-archief|Beleidsplan WFA]]
- **Onderwerpoverzicht:** [[Wiki/Onderwerpoverzichten/cultuur|Cultuur]] bijgewerkt — 49 begrippen, 8 BO's
- **Nieuw BO:** Collectie (GGM exact, Erfgoedwet art. 2.8-2.11 als wettelijke grondslag)
- **Duplicaat opgelost:** Monument/Beschermde Status — zelfde GGM-entiteit (EAID_32C02923). Monument behouden als primair BO, Beschermde Status verwijderd.
- **Beoordeeld als niet-BO:** beschermd cultuurgoed (Minister-bevoegdheid), beschermde verzameling (status op Collectie), tentoonstelling (operationeel), bruikleen (operationeel), eDepot (infrastructuur), pre-eDepot (tussenvorm)
- **GGM-terugmelding:** eDepot ontbreekt als concept in GGM (alleen fysiek Depot)
- **BO's bijgewerkt:** Monument, Archiefstuk, Museumobject — bronverwijzingen aangevuld met erfgoed-bronsamenvattingen

## [2026-06-27] ingest | Informatiesamenleving — 4 bronnen (2 verwerkt, 2 niet-relevant), 3 nieuwe BO's

- **Bronnen:** Informatiebeleidsplan Nunspeet 2024-2028 (PDF), Beleid I en ICT BEL Combinatie 2020-2024 (PDF), Begroting Rotterdam IV 2026 (web → niet-relevant), Informatiebeveiligingsbeleid Heumen 2024-2028 (lokaleregelgeving → niet-relevant)
- **Bronsamenvattingen:** [[Wiki/Bronsamenvattingen/Informatiesamenleving/informatiebeleidsplan-nunspeet|Nunspeet]], [[Wiki/Bronsamenvattingen/Informatiesamenleving/beleid-informatie-ict-bel-combinatie|BEL Combinatie]]
- **Onderwerpoverzicht:** [[Wiki/Onderwerpoverzichten/informatiesamenleving|Informatiesamenleving]] — 36 begrippen, 10 BO's
- **Nieuwe BO's:** 3 — Applicatie (GGM exact, ICT-domein taakveld 9), Verwerkersovereenkomst (governance-object, GGM-hiaat, relatie privacy-BO's), Dataproduct (procesobject, GGM-hiaat)
- **GGM-terugmeldingen:** #82 Verwerkersovereenkomst hiaat, #83 Dataproduct hiaat
- **GGM-dekking ICT:** Applicatie is eerste BO uit GGM ICT-domein (35 entiteiten); 7 entiteiten als GGM-component bij Applicatie

## [2026-06-26] ingest | Inkoop — 3 bronnen, 8 BO's

- **Bronnen:** VNG Model Inkoop- en Aanbestedingsbeleid 2025 (PDF), Inkoop- en aanbestedingsbeleid OVER-gemeenten (PDF, bgr-2023-799), Inkoop- en aanbestedingsbeleid West-Betuwe 2024-2027 (lokaleregelgeving.overheid.nl)
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Inkoop/inkoop-en-aanbestedingsbeleid|Gemeentelijk inkoop- en aanbestedingsbeleid]] — gebundelde samenvatting van 3 bronnen
- **Onderwerpoverzicht:** [[Wiki/Onderwerpoverzichten/inkoop|Inkoop]] — 17 begrippen, 8 BO's
- **Nieuwe BO's:** 8 — Aanbesteding (GGM exact), Contract (GGM exact), Leverancier (GGM exact, 2 duplicaten), Gunning (GGM exact), Offerte (GGM exact, 3 duplicaten), Inschrijving (GGM exact, homoniem Onderwijs), Inkooppakket (GGM exact), Marktconsultatie (procesobject, GGM-hiaat)
- **GGM-terugmeldingen:** #78 Leverancier duplicaat, #79 Offerte duplicaat, #80 Inschrijving homoniem, #81 Marktconsultatie hiaat
- **GGM-dekking Inkoop:** 7 van 20 entiteiten → BO, 8 → GGM-component/subtype, 5 → referentiedata/formulier

## [2026-06-26] ingest | Vastgoed — 2 bronnen, 7 BO's

- **Bronnen:** Actualisatie Vastgoedstrategie Amsterdam (PDF, ~1.000 panden), Beleidsplan Gemeentelijk Vastgoed Hulst 2020-2024 (lokale regelgeving, ~50 gebouwen)
- **Bronsamenvattingen:** [[Wiki/Bronsamenvattingen/Vastgoed/vastgoedstrategie-amsterdam|Vastgoedstrategie Amsterdam]], [[Wiki/Bronsamenvattingen/Vastgoed/beleidsplan-vastgoed-hulst|Beleidsplan Vastgoed Hulst]]
- **Onderwerpoverzicht:** [[Wiki/Onderwerpoverzichten/vastgoed|Vastgoed]] — 18 begrippen, 7 BO's
- **Nieuwe BO's:** 6 — Vastgoedobject (GGM exact), Verhuurbare Eenheid (GGM exact), Vastgoedcontract (GGM exact), MJOP (GGM exact), Werkbon (GGM exact), Algemeenbelangbesluit (governance-object, GGM-hiaat)
- **Bijgewerkt:** Inspectie — uitgebreid met vastgoedcontext, GGM-duplicaat Vastgoed-domein, relaties naar Vastgoedobject en MJOP
- **GGM-dekking Vastgoed:** 6 van 27 entiteiten → BO, 6 → GGM-component, 3 → actor/rol, rest → enumeratie/verankering

## [2026-06-26] coverage | GGM-dekkingsanalyse gegenereerd

- **Output:** [[Wiki/Analyses/ggm-dekking|GGM-dekkingsanalyse]]
- **Scope:** alle 44 beleidsdomeinen, 954 objecttype-entiteiten
- **Resultaat:** 167 BO's vastgelegd, 37 als begrip gevonden (niet-BO), 688 niet beoordeeld
- **Beleidsdomeinen zonder bronnen:** 18 (o.a. Griffie, ICT, Inkoop, Subsidies, diverse Inkomen-subdomeinen)

## [2026-06-26] ingest | Maatschappelijke Ondersteuning — Wmo 2015

- **Bron:** Wet maatschappelijke ondersteuning 2015 (wetten.overheid.nl, BWBR0035362 per 2026-01-01)
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/wmo-2015|Wmo 2015 (BWBR0035362)]]
- **Nieuwe BO's:** 0 — alle kernconcepten al vastgelegd uit eerdere bronnen
- **Verrijkt:** 6 bestaande BO's (Beschikking, Voorziening, Toewijzing, Levering, PGB-Toekenning, Client) met Wmo 2015 als wettelijke grondslag

## [2026-06-26] ingest | Informatiesamenleving — BIO2

- **Bron:** Baseline Informatiebeveiliging Overheid 2 (BIO2 v1.3 definitief, BZK/CIP, januari 2026)
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Informatiesamenleving/bio2-baseline-informatiebeveiliging|BIO2]]
- **Begrippen:** 6 nieuwe (ISMS, VvT, risicoregister, informatiebeveiligingsbeleid, ICV, CISO) — alle governance/instrument, geen BO's
- **Nieuwe BO's:** 0 — bron bevat uitsluitend governance-instrumenten, processen en actoren
- **Context:** verrijkt bestaande BO's Datalek (meldplicht CSIRT, bewaartermijn 3 jaar) en DPIA (risicoafweging nieuwe systemen)

## [2026-06-26] ingest | Maatschappelijke Ondersteuning — Jeugdwet

- **Bron:** Jeugdwet (wetten.overheid.nl, BWBR0034925 per 2024-01-01)
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/jeugdwet|Jeugdwet (BWBR0034925)]]
- **Begrippen:** 7 nieuwe (hulpverleningsplan, kinderbeschermingsmaatregel, machtiging gesloten jeugdhulp, pleegcontract, familiegroepsplan, verwijsindex risicojongeren, dossier jeugdhulp)
- **Nieuwe BO's:** 4 — Hulpverleningsplan (procesobject, GGM-hiaat), Kinderbeschermingsmaatregel (procesobject, GGM-hiaat), Machtiging Gesloten Jeugdhulp (procesobject, GGM-hiaat), Pleegcontract (contract, GGM-hiaat)
- **Verrijkt:** 6 bestaande BO's (Beschikking, Voorziening, Toewijzing, Levering, PGB-Toekenning, Zorgmelding) met Jeugdwet als aanvullende bron
- **GGM-terugmeldingen:** #74–#77 (4 hiaten in beleidsdomein Jeugdbescherming en reclassering / Generiek Jeugd en Wmo)
- **Openstaande vraag opgelost:** Kinderbeschermingsmaatregel is nu BO (Jeugdwet art. 2.4 geeft gemeentelijke verantwoordelijkheid)

## [2026-06-26] ingest | Bestuur — Gemeentewet + positionering Griffier

- **Bronnen:** Gemeentewet wettekst (wetten.overheid.nl, BWBR0005416); Op weg naar gelijkwaardige verhoudingen (NVvR, functieprofiel Griffier)
- **Bronsamenvattingen:**
  - [[Wiki/Bronsamenvattingen/Bestuur/gemeentewet-wettekst|Gemeentewet (wettekst)]]
  - [[Wiki/Bronsamenvattingen/Bestuur/positionering-griffier|Positionering Griffier]]
- **Begrippen:** 10 nieuwe (raadsstuk, vergadering, stemming, raadslid, collegelid, burgemeester, griffier, secretaris, rekenkamer, ombudsman)
- **Nieuwe BO's:** 3 — Raadsstuk (GGM exact, Griffie), Vergadering (GGM exact, Griffie), Stemming (GGM exact, Griffie)
- **GGM-dekking:** beleidsdomein Griffie (13 entiteiten): 3 BO's, 6 GGM-componenten (Agendapunt, Aanwezige Deelnemer, Video-opname, Categorie, Dossier, Indiener), 4 actoren (Raadslid, Collegelid, Raadscommissie, Programma/Taakveld)
- **Onderwerpoverzicht Bestuur:** bronnen_count 10→12, begrippen_count 14→24, bo_count 4→7 (5 Politiek + 3 Griffie, maar totaal domein = 7 BO's want Partijsubsidie telt ook)

## [2026-06-26] coverage | GGM-dekkingsanalyse geregenereerd

- **Output:** [[Wiki/Analyses/ggm-dekking|GGM-dekkingsanalyse]]
- **Scope:** 954 Objecttype-entiteiten over 44 beleidsdomeinen
- **Stand:** 167 BO's vastgelegd, 74 niet-BO (9 generalisatie, 18 subtype, 42 component, 5 begrippentabel), 713 niet beoordeeld
- **Zonder bronnen:** 19 beleidsdomeinen (o.a. Griffie, ICT, Inkoop, Subsidies, Vastgoed, Kern, meerdere Sociaal Domein subdomeinen)

## [2026-06-26] ingest | Beheer OR — Amsterdam beheerplan + VNG natuur/groen

- **Bronnen:** Integraal beheerplan openbare ruimte Amsterdam 2023-2026 (35 p.); Factsheet informatiebronnen natuur en groen (VNG, verwijzingsdocument)
- **Bronsamenvattingen:**
  - [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/beheerplan-or-amsterdam-2023-2026|Integraal beheerplan OR Amsterdam]]
  - [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/factsheet-informatiebronnen-natuur-groen|Informatiebronnen natuur en groen (VNG)]]
- **Begrippen:** 5 nieuwe (brandkraan, steiger, wegtunnel, fietsenrek, watertappunt)
- **Nieuwe BO's:** geen — nieuwe objecten zijn subtypes of hebben onvoldoende brondiepte
- **Bestaande BO's bevestigd:** Boom (260k), Groenobject, Waterobject (29k ha), Ligplaats (3k), Kunstwerk (1851 bruggen), Verhardingsobject (3k ha), Verkeerslicht (400 VRI), Verlichtingsobject (128k), Speeltoestel (7.4k), Geluidscherm (19.5 km), Laadpaal (3.3k)
- **Onderwerpoverzicht BOR:** bronnen_count 8→10, begrippen_count 32→37

## [2026-06-26] ingest | Omgevingswet — register bij omgevingsplan, 1 nieuw BO

- **Bron:** Het omgevingsplan en een register (VNG, PDF, april 2026, 10 p.)
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Omgevingswet/factsheet-omgevingsplan-register|Het omgevingsplan en een register (VNG)]]
- **Begrippen:** 3 nieuwe (register omgevingsplan, statisch register, dynamisch register)
- **Nieuwe BO's (1):**
  - [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/register-omgevingsplan|Register (omgevingsplan)]] — procesobject, GGM-hiaat, 6/6 criteria, meervoud per gemeente
- **GGM-terugmeldingen:** #73 Register (omgevingsplan) (hiaat)
- **Onderwerpoverzicht:** bronnen_count 2→3, begrippen_count 19→22, bo_count 4→5

## [2026-06-26] ingest | Ruimte Wonen en Mobiliteit — 7 niet-relevant

- **Bronnen:** 7 VNG-portaalpagina's → Niet-relevant (bouwregelgeving, klimaatadaptatie-en-water, landelijk-gebied, rubriek-ruimte-wonen-en-mobiliteit, ruimtelijke-ordening, vergunningverlening-toezicht-en-handhaving, wabo-omgevingsvergunning)
- **Nieuwe BO's:** geen
- **Backlog:** sectie Ruimte Wonen en Mobiliteit afgerond (~~doorgestreept~~)

## [2026-06-26] ingest | Beheer OR — GWR Twenterand, 1 nieuw BO

- **Bron:** Gemeentelijk Water- en Rioleringsplan 2024-2028 (gemeente Twenterand)
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/gwr-twenterand-2024-2028|GWR Twenterand 2024-2028]]
- **Begrippen:** 4 nieuwe (rioolleiding, IBA, drukriolering, GWR)
- **Nieuwe BO's (1):**
  - [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/rioolleiding|Rioolleiding]] — GGM Leiding exact, 13 attributen, subtypes vuilwater/hemelwater/gemengd/persleiding
- **Bestaande BO's bevestigd:** Gemaal, Kolk, Rioolheffing (areaalcijfers Twenterand)
- **Onderwerpoverzicht milieu:** bronnen_count 10→11, begrippen_count 68→72, bo_count 34→35

## [2026-06-26] ingest | Omgevingswet — planketen + 9 niet-relevant

- **Bronnen:** Factsheet Omgevingsvisie (VNG, PDF 2018); 9 VNG-portaalpagina's → niet-relevant
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Omgevingswet/factsheet-omgevingsvisie-vng|Factsheet Omgevingsvisie (VNG)]]
- **Niet-relevant (9):** digitaal-stelsel-omgevingswet-dso, gemeenteraad-en-de-omgevingswet, monitoringsinitiatieven-omgevingswet-en-wkb, participatie-onder-de-omgevingswet, planketen-omgevingswet, rubriek-omgevingswet, veranderopgave-omgevingswet, vergunningverlening-toezicht-en-handhaving-onder-de-omgevingswet, wet-kwaliteitsborging-voor-het-bouwen-wkb
- **Begrippen:** 5 nieuwe (omgevingsvisie GOVI, programma Ow, planketen, zienswijze, omgevingsdocument)
- **Nieuwe BO's:** geen — alle begrippen zijn instrumenten/governance
- **Onderwerpoverzicht:** bronnen_count 1→2, begrippen_count 14→19
- **Backlog:** sectie Omgevingswet afgerond (~~doorgestreept~~)

## [2026-06-26] ingest | Informatiesamenleving — Algoritmeregister, 1 nieuw BO

- **Bronnen:** Handleiding Publicatiestandaard Algoritmeregister (BZK); Rapportage Algoritmerisico's Nederland (AP, → niet-relevant)
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Informatiesamenleving/handleiding-publicatiestandaard-algoritmeregister|Handleiding Publicatiestandaard Algoritmeregister]]
- **Niet-relevant:** rapportage-algoritmerisicos-nederland (AP, beleidsanalyse)
- **Begrippen:** 2 nieuwe begrippen (algoritmeregister, publicatiecategorie)
- **Nieuwe BO's (1):**
  - [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/algoritmeregister|Algoritmeregister]] — procesobject, GGM-hiaat, 6/6 criteria, Publicatiestandaard BZK
- **GGM-terugmeldingen:** #72 Algoritmeregister (hiaat)
- **Onderwerpoverzicht:** bronnen_count 7→8, begrippen_count 25→27, bo_count 6→7
- **bo_count:** +1

## [2026-06-26] ingest | Informatiesamenleving — Datalekken IBD, 1 nieuw BO

- **Bron:** Factsheet Datalekken (IBD, versie 2.0, augustus 2024)
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Informatiesamenleving/factsheet-datalekken-ibd|Factsheet Datalekken — IBD]]
- **Begrippen:** 3 nieuwe begrippen (datalek, beveiligingsincident, verwerkersovereenkomst)
- **Nieuwe BO's (1):**
  - [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/datalek|Datalek]] — procesobject, GGM-hiaat, 6/6 criteria, art. 33-34 AVG
- **GGM-terugmeldingen:** #71 Datalek (hiaat)
- **Onderwerpoverzicht:** bronnen_count 6→7, begrippen_count 22→25, bo_count 5→6
- **bo_count:** +1

## [2026-06-26] ingest | Informatiesamenleving — AVG/DPIA, 2 nieuwe BO's

- **Bronnen:** AVG art. 30, 35, 36 (EU); DPIA-toelichting (AP); DPIA-gids (EDPB, → niet-relevant)
- **Bronsamenvattingen:**
  - [[Wiki/Bronsamenvattingen/Informatiesamenleving/avg-verwerkingsregister-dpia|AVG — Verwerkingsregister en DPIA]]
  - [[Wiki/Bronsamenvattingen/Informatiesamenleving/dpia-ap|DPIA — Autoriteit Persoonsgegevens]]
- **Niet-relevant:** dpia-edpb-gids (EDPB, te beknopt)
- **Begrippen:** 5 nieuwe begrippen (DPIA, verwerkingsactiviteit, verwerkingsregister, voorafgaande raadpleging, FG)
- **Nieuwe BO's (2):**
  - [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/dpia|DPIA]] — procesobject, GGM-hiaat, 6/6 criteria, art. 35 AVG
  - [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/verwerkingsactiviteit|Verwerkingsactiviteit]] — procesobject, GGM-hiaat, 6/6 criteria, art. 30 AVG
- **GGM-terugmeldingen:** #69 DPIA (hiaat), #70 Verwerkingsactiviteit (hiaat)
- **Onderwerpoverzicht:** bronnen_count 4→6, begrippen_count 17→22, bo_count 3→5
- **bo_count:** +2

## [2026-06-26] ingest | Informatiesamenleving — EU AI-verordening, 1 nieuw BO

- **Bron:** Verordening (EU) 2024/1689 — AI-verordening (selectie art. 3-5, 26-27, bijlage III)
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Informatiesamenleving/eu-ai-verordening|Verordening (EU) 2024/1689]]
- **Begrippen:** 1 nieuw begrip (ernstig incident — potentieel BO)
- **Nieuwe BO's (1):**
  - [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/grondrechteneffectbeoordeling|Grondrechteneffectbeoordeling]] — procesobject, GGM-hiaat, 6/6 criteria, art. 27 AI-verordening
- **GGM-terugmeldingen:** #68 Grondrechteneffectbeoordeling (hiaat)
- **Onderwerpoverzicht:** bronnen_count 3→4, begrippen_count 16→17, bo_count 2→3
- **bo_count:** +1

## [2026-06-26] ingest | Informatiesamenleving — VNG factsheet AI-verordening + BZK niet-relevant

- **Bronnen:** Uitvoeringsanalyse Digital Decade AI-verordening (VNG, 2025, 4p factsheet); Algoritmekader AI-verordening in het kort (BZK)
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Informatiesamenleving/factsheet-ai-verordening-vng|Uitvoeringsanalyse Digital Decade AI-verordening]]
- **Niet-relevant:** algoritmekader-ai-verordening-kort (BZK, te beknopt)
- **Begrippen:** 3 nieuwe begrippen (gebruiksverantwoordelijke, aanbieder, AI compliance officer — alle actoren/rollen, geen BO's)
- **Nieuwe BO's:** 0
- **Correctie:** "registratie"-taal verwijderd uit begrippentabel en beoordelingssectie (feedback: registreren is geen BO-criterium)
- **Onderwerpoverzicht:** bronnen_count 2→3, begrippen_count 13→16
- **bo_count:** ongewijzigd (2)

## [2026-06-26] ingest | Informatiesamenleving — AI-verordening AP

- **Bron:** AI-verordening overzichtspagina (Autoriteit Persoonsgegevens)
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Informatiesamenleving/ai-verordening-ap|AI-verordening — Autoriteit Persoonsgegevens]]
- **Begrippen:** 4 nieuwe begrippen in onderwerpoverzicht (AI-systeem, risicogroep, grondrechteneffectbeoordeling, AI-geletterdheid)
- **Nieuwe BO's:** 0 (bron onvoldoende concreet over gemeentelijke registraties)
- **Signalering:** grondrechteneffectbeoordeling als nieuw potentieel BO (verwant aan DPIA); algoritmeregister bevestigd
- **Onderwerpoverzicht:** bronnen_count 1→2, begrippen_count 9→13
- **bo_count:** ongewijzigd (2)

## [2026-06-26] ingest | Informatiesamenleving — Handreiking Woo, 2 nieuwe BO's

- **Bron:** Handreiking "De Wet open overheid in de gemeentelijke praktijk" (VNG/Pels Rijcken, 2025, 110 pagina's)
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Informatiesamenleving/handreiking-woo-gemeentelijke-praktijk|Handreiking Woo in de gemeentelijke praktijk]]
- **Begrippen:** 9 begrippen in onderwerpoverzicht (2 BO's + 7 niet-BO's: actieve openbaarmaking, informatiecategorie, Woo-contactpersoon, uitzonderingsgrond, convenant, geheimhouding, beschikking)
- **Nieuwe BO's (2):**
  - [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/woo-verzoek|Woo-verzoek]] — procesobject, GGM-hiaat, 6/6 criteria, art. 4.1 Woo
  - [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/klacht|Klacht]] — procesobject, GGM-hiaat, 6/6 criteria, titel 9.1 Awb
- **GGM-terugmeldingen:** #66 Woo-verzoek (hiaat), #67 Klacht (hiaat, alleen domeinspecifiek "Klacht Leerlingenvervoer" in taakveld 4)
- **Onderwerpoverzicht:** status open → in-behandeling, 1 bronsamenvatting, 9 begrippen, 2 BO's
- **bo_count:** +2

## [2026-06-26] herziening | Informatiesamenleving — zoeksuggesties toegevoegd

- **Status:** afgerond → open (onvoldoende bronnen)
- **Potentiële BO's uitgebreid:** Verwerkingsactiviteit (AVG art. 30) en DPIA toegevoegd naast bestaande drie (Woo-verzoek, Algoritmeregister, Datalek)
- **Zoeksuggesties:** per potentiële BO concrete zoektermen en bronlocaties opgenomen
- **Prioritering:** Woo-verzoek meest kansrijk, Verwerkingsactiviteit tweede (wettelijk verplicht register)

## [2026-06-26] ingest | Europa en Internationaal — alle bronnen niet-relevant

- **Bronnen:** 7 VNG-portaalpagina's (europese-kennisnetwerken, europese-subsidies, gemeentelijk-internationaal-beleid, global-goals-voor-gemeenten, grensoverschrijdende-samenwerking, rubriek-europa-en-internationaal, versterking-lokaal-bestuur-wereldwijd)
- **Beoordeling:** Alle bronnen governance/strategie op VNG-niveau, geen concrete gemeentelijke registraties
- **Resultaat:** 0 bronsamenvattingen, 0 begrippen, 0 BO's. 7 bronnen → Niet-relevant
- **Onderwerpoverzicht:** [[Wiki/Onderwerpoverzichten/europa-en-internationaal|Europa en Internationaal]] aangemaakt (open — onvoldoende bronnen)
- **Signalering:** Europese subsidie(aanvraag) potentieel BO bij rijkere bronnen (EFRO/ESF-projectadministratie, jaarrekening). Zoeksuggesties opgenomen in onderwerpoverzicht.

## [2026-06-26] ingest | Dienstverlening — RGBZ-kernobjecten Zaak en Document

- **Bronnen:** bestaande bronsamenvattingen RGBZ 1.0 en ZTC2 v2.1
- **2 nieuwe BO's:** Zaak (GGM exact, RGBZ-kern) en Document (GGM exact, RGBZ-kern)
- **Onderwerpoverzicht:** Zaak en Document toegevoegd, zaakdossier gecorrigeerd naar ❌ (impliciet concept), informatieobject naar ❌ (abstract supertype)
- **Relaties gefixt:** aanvraag-of-melding en balieafspraak verwijzen nu naar Zaak i.p.v. platte tekst "zaakdossier"
- **Cross-domein link:** Document → Archiefstuk (via overbrenging Archiefwet), informatieobject als abstract archiveringsconcept

## [2026-06-26] ingest | Cultuur — Archiefverordening Wageningen 2019 + Memorie van toelichting Archiefwet 1995

- **Bronnen:** Archiefverordening Wageningen 2019 (lokaleregelgeving.overheid.nl) + Memorie van toelichting Archiefwet 1995 (PDF, 638 regels)
- **Bronsamenvattingen:** archiefverordening-wageningen.md, memorie-van-toelichting-archiefwet.md
- **Geen nieuwe BO's** — beide bronnen bevestigen bestaand BO Archiefstuk
- **BO bijgewerkt:** Archiefstuk — domein uitgebreid naar [Cultuur, Informatiebeheer], duale positionering gedocumenteerd
- **Onderwerpoverzicht:** 8 begrippen toegevoegd (archiefbewaarplaats, archiefruimte, archiefbescheiden, zorgdrager, gemeentearchivaris, overbrenging, vernietigingslijst, substitutie)
- **Signalering:** GGM mist e-depot-concept (digitale archiefbewaarplaats) en archiefruimte (semi-statische opslag vóór overbrenging). MvT adresseert digitale archivering al in 1992.

## [2026-06-25] ingest | Openbare Gezondheid — Kerntaken infectieziektebestrijding

- **Bron:** Adviesrapport De Kerntaken van de Infectieziektebestrijding (GGD GHOR Nederland, september 2022, PDF 509 regels)
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Openbare Gezondheid/kerntaken-infectieziektebestrijding|Kerntaken infectieziektebestrijding]]
- **Begrippen:** 7 nieuwe begrippen in onderwerpoverzicht (1 BO + 6 niet-BO's: infectieziektemelding, BCO, surveillance, outbreak management, vangnetfunctie, risicoprofiel, opschalingsplan)
- **Nieuw BO (1):** [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/infectieziektemelding|Infectieziektemelding]] — procesobject, GGM-hiaat, 6/6 criteria, Wpg meldingsplicht
- **GGM-terugmelding:** #65 — Infectieziektemelding als specialisatie van AanvraagOfMelding; taakveld 7 mist beleidsdomein Volksgezondheid
- **Perspectief:** gemeente is opdrachtgever GGD, niet uitvoerder. Meeste IZB-begrippen zijn GGD-processen, buiten gemeentelijke scope.
- **bo_count:** +1

## [2026-06-25] ingest | Openbare Gezondheid — herziening en BO Gemeentebegrafenis

- **Bronnen:** 6 bronnen (4 VNG-portaalpagina's, Utrechts gezondheidsbeleid, Uitvoeringsprogramma mentale gezondheid). 2 eerder naar Niet-relevant verplaatst.
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Openbare Gezondheid/gezondheidsbeleid-en-preventie|Gezondheidsbeleid en preventie]] bijgewerkt — bronnenlijst aangevuld, BO-conclusie herzien
- **GGM-analyse:** Taakveld 7 bevat alleen Afval; Gemeentebegrafenissen zit onder taakveld 6 (Sociaal Domein). Geen volksgezondheid-specifieke entiteiten in het GGM.
- **Nieuw BO (1):** [[Wiki/Bedrijfsobjecten/6-sociaal-domein/gemeentebegrafenissen/gemeentebegrafenis|Gemeentebegrafenis]] — 6/6 criteria, GGM exact match, art. 21 Wet op de lijkbezorging
- **Onderwerpoverzicht:** [[Wiki/Onderwerpoverzichten/openbare-gezondheid|Openbare Gezondheid]] bijgewerkt — status open (onvoldoende bronnen), 9 begrippen, 1 BO. Ontbrekende bronnen gesignaleerd (begraafplaatsbeheer, infectieziektebestrijding, milieugezondheid, hygiënetoezicht, lijkschouw).
- **bo_count:** +1

## [2026-06-25] ingest | Informatiesamenleving — alle bronnen niet-relevant

- **Bronnen:** 14 VNG-portaalpagina's (ai-en-algoritmen, archieven, data-en-samenleving, digital-decade, digitale-autonomie, digitale-identiteit, digitale-veiligheid-en-privacy, federatief-datastelsel, generieke-digitale-infrastructuur-gdi, innovatie-en-trends, regie-op-de-digitale-samenleving, rubriek-informatiesamenleving, standaarden, wet-open-overheid)
- **Beoordeling:** Alle bronnen zijn governance/strategie op VNG-niveau, geen concrete gemeentelijke registraties of objecttypen
- **Resultaat:** 0 bronsamenvattingen, 0 begrippen, 0 BO's. 14 bronnen → Niet-relevant
- **Onderwerpoverzicht:** [[Wiki/Onderwerpoverzichten/informatiesamenleving|Informatiesamenleving]] aangemaakt (afgerond)
- **Signalering:** Woo-verzoek, Algoritmeregister en Datalek potentieel BO bij rijkere bronnen

## [2026-06-25] ingest | Basisregistraties — Gegevenscatalogus NHR 3.0.4
- **Bron:** Gegevenscatalogus Handelsregister v3.0.4 (KvK / Ministerie van EZK), Handelsregisterwet 2007, Handelsregisterbesluit 2008
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Standaarden/catalogus-nhr|Gegevenscatalogus NHR 3.0.4]]
- **Begrippen:** 7 nieuwe begrippen in onderwerpoverzicht [[Wiki/Onderwerpoverzichten/basisregistraties|Basisregistraties]] (3 BO's + 4 niet-BO's: Onderneming, Rechtspersoon, Handelsnaam, SBI-code, UBO, Functionaris, Faillissement)
- **Nieuwe BO's (3):** [[Wiki/Bedrijfsobjecten/99-kern/nhr/maatschappelijke-activiteit|Maatschappelijke Activiteit]], [[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon|Niet-Natuurlijk Persoon]], [[Wiki/Bedrijfsobjecten/99-kern/nhr/vestiging|Vestiging]]
- **GGM-matching:** 3 exact match op RSGB Model Kern (MaatschappelijkeActiviteit, NietNatuurlijkPersoon, Vestiging). Geen GGM-hiaten.
- **bo_count:** 161 → 164

## [2026-06-25] ingest | Basisregistraties — Catalogus BRK 2020
- **Bron:** Catalogus Basisregistratie Kadaster versie 1.0 (Het Kadaster, 10 december 2020, PDF 35 pagina's)
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Standaarden/catalogus-brk|Catalogus BRK 2020]]
- **Begrippen:** 14 nieuwe begrippen in onderwerpoverzicht [[Wiki/Onderwerpoverzichten/basisregistraties|Basisregistraties]] (8 BO's + 6 niet-BO's)
- **Nieuwe BO's (8):** [[Wiki/Bedrijfsobjecten/99-kern/brk/kadastraal-perceel|Kadastraal Perceel]], [[Wiki/Bedrijfsobjecten/99-kern/brk/appartementsrecht|Appartementsrecht]], [[Wiki/Bedrijfsobjecten/99-kern/brk/zakelijk-recht|Zakelijk Recht]], [[Wiki/Bedrijfsobjecten/99-kern/brk/tenaamstelling|Tenaamstelling]], [[Wiki/Bedrijfsobjecten/99-kern/brk/zekerheidsrecht|Zekerheidsrecht]], [[Wiki/Bedrijfsobjecten/99-kern/brk/publiekrechtelijke-beperking|Publiekrechtelijke Beperking]], [[Wiki/Bedrijfsobjecten/99-kern/brk/stuk|Stuk]], [[Wiki/Bedrijfsobjecten/99-kern/brk/stukdeel|Stukdeel]]
- **GGM-matching:** 5 exact match op RSGBPlus (KadastraalPerceel, Appartementsrecht, ZakelijkRecht, Tenaamstelling, Zekerheidsrecht), 3 GGM-hiaten (Publiekrechtelijke Beperking, Stuk, Stukdeel)
- **Terugmeldingen:** #62 (Publiekrechtelijke Beperking hiaat), #63 (Stuk hiaat), #64 (Stukdeel hiaat)
- **bo_count:** 153 → 161

## [2026-06-25] ingest | Basisregistraties — Logisch Ontwerp BRP 2025.Q1
- **Bron:** Logisch Ontwerp BRP Versie 2025.Q1 (RvIG/BZK, 1 januari 2025, PDF 765 pagina's)
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Standaarden/logisch-ontwerp-brp-2025q1|Logisch Ontwerp BRP 2025.Q1]]
- **Begrippen:** 10 nieuwe begrippen in onderwerpoverzicht [[Wiki/Onderwerpoverzichten/basisregistraties|Basisregistraties]] (3 BO's + 2 subtypes + 5 niet-BO's)
- **Nieuwe BO's (3):** [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon|Ingeschreven Persoon]], [[Wiki/Bedrijfsobjecten/99-kern/brp/huwelijk|Huwelijk]], [[Wiki/Bedrijfsobjecten/99-kern/brp/reisdocument|Reisdocument]]
- **GGM-matching:** alle 3 exact match op RSGBPlus-entiteiten (Ingezetene, SluitingOfAangaanHuwelijkOfGeregistreerdPartnerschap, Reisdocument)
- **GGM-componenten bij Ingeschreven Persoon:** 9 detailentiteiten (nationaliteit, geboorte, overlijden, migratie, verblijfadres, verblijfstitel, verstrekkingsbeperking, naamgebruik, samengesteldenaam)
- **Niet-BO's:** Nationaliteit, Verblijfstitel, Gezagsverhouding, Kiesrecht, Overlijden (allen eigenschap/status van persoon)
- **Terugmelding:** #61 (definitie Reisdocument dekt niet ID-kaart)
- **bo_count:** 150 → 153

## [2026-06-25] coverage | GGM-dekkingsanalyse bijgewerkt
- **Script:** `coverage_analysis.py` — volledige analyse alle beleidsdomeinen
- **Resultaat:** 954 objecttype-entiteiten, 150 BO's, 758 niet beoordeeld
- **Output:** [[Wiki/Analyses/ggm-dekking|GGM-dekkingsanalyse]]

## [2026-06-25] GGM-duplicaten — BAG/RSGBPlus conventie en doorvoering
- **Conventie vastgelegd:**
  - Template: `ggm_duplicaat_entiteiten` frontmatter-veld + `## GGM-duplicaten` body-sectie
  - Skill write-bo: stap 4b voor duplicaat-detectie, classificatie (duplicaat vs homoniem), primaire GUID-keuze
  - Skill lint: checks op duplicaat-frontmatter en -body consistentie
  - Terugmeldingen: nieuwe typen `duplicaat` (samenvoeg-advies) en `homoniem` (hernoemadvies)
- **Doorgevoerd voor 10 BAG-BO's:** Pand, Verblijfsobject, Woonplaats, Openbare Ruimte, Nummeraanduiding, Standplaats (BAG), Ligplaats, Gemeente, Wijk, Buurt — alle met RSGBPlus-duplicaat; Standplaats ook met Musea-homoniem
- **Terugmeldingen:** #59 (structureel BAG/RSGBPlus duplicaat, 10 entiteiten) en #60 (homoniem Standplaats BAG vs Musea)

## [2026-06-25] ingest | Basisregistraties — Catalogus BAG 2018
- **Bron:** Catalogus BAG 2018 (Ministerie van BZK, 29 maart 2018)
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bag-2018|Catalogus BAG 2018]]
- **Begrippen:** 13 begrippen in nieuw onderwerpoverzicht [[Wiki/Onderwerpoverzichten/basisregistraties|Basisregistraties]]
- **Nieuwe BO's (8):** [[Wiki/Bedrijfsobjecten/99-kern/bag/pand|Pand]], [[Wiki/Bedrijfsobjecten/99-kern/bag/verblijfsobject|Verblijfsobject]], [[Wiki/Bedrijfsobjecten/99-kern/bag/woonplaats|Woonplaats]], [[Wiki/Bedrijfsobjecten/99-kern/bag/openbare-ruimte|Openbare Ruimte]], [[Wiki/Bedrijfsobjecten/99-kern/bag/nummeraanduiding|Nummeraanduiding]], [[Wiki/Bedrijfsobjecten/99-kern/bag/standplaats|Standplaats (BAG)]], [[Wiki/Bedrijfsobjecten/99-kern/bag/gemeente|Gemeente]], [[Wiki/Bedrijfsobjecten/99-kern/bag/wijk|Wijk]], [[Wiki/Bedrijfsobjecten/99-kern/bag/buurt|Buurt]]
- **Bestaande BO's aangepast:**
  - Ligplaats: onderwerp uitgebreid met Basisregistraties/BAG, bronverwijzing toegevoegd
  - Standplaats (Economie) → hernoemd naar [[Wiki/Bedrijfsobjecten/3-economie/economie/marktstandplaats|Marktstandplaats]]: GGM-match gecorrigeerd (was foutief gematcht op BAG Standplaats), grondslag gewijzigd naar procesobject
- **Wiki-links bijgewerkt:** warenmarkt, bronsamenvattingen Economie, onderwerpoverzicht Economie
- **GGM-dekking:** alle 9 BO's exact match op GGM BAG-beleidsdomein (13 entiteiten); Marktstandplaats is nieuw geïdentificeerd GGM-hiaat

## [2026-06-25] ingest | Bestuur — Implementatiehandleiding Model Participatieverordening 2024
- **Bron:** Implementatiehandleiding VNG Model Participatieverordening 2024 (VNG, december 2024, PDF)
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Bestuur/implementatiehandleiding-model-participatieverordening-2024|Implementatiehandleiding Model Participatieverordening 2024]]
- **Begrippen:** 7 nieuwe begrippen toegevoegd aan onderwerpoverzicht (participatieverordening, inwonersparticipatie, overheidsparticipatie, uitdaagrecht, participatieplan, inspraak, maatschappelijke partij)
- **BO's:** geen nieuwe BO's — alle begrippen zijn processen, procedures, governance of externe actoren
- **Conclusie:** bron beschrijft governance en procesregels voor gemeentelijke participatie; verrijkt context voor bestaand domein Bestuur

## [2026-06-25] coverage | GGM-dekkingsanalyse bijgewerkt
- **Script:** `coverage_analysis.py` — 954 objecttype-entiteiten, 44 beleidsdomeinen
- **142 BO's**, 9 generalisaties, 18 subtypes, 13 componenten, 5 begrippentabel niet-BO's
- **767 entiteiten niet beoordeeld**
- **19 beleidsdomeinen zonder bronnen** (o.a. Griffie, ICT, Inkoop, Subsidies, Vastgoed, meerdere Inkomen-subdomeinen)

## [2026-06-25] ingest | Werk en Inkomen — handreiking Participatiewet, 2 nieuwe BO's
- **Bron:** Handreiking Explicitering budgetten Participatiewet en Wsw (Berenschot, april 2025, in opdracht Cedris/Divosa/VNG/SZW) — PDF geconverteerd, 1019 regels
- **2 nieuwe BO's:**
  - Loonkostensubsidie (GGM exact, Werk) — tegemoetkoming aan werkgever voor verschil loonwaarde en WML; historische budgetverdeling, €7.355 per eenheid in gemeentefonds
  - Re-integratievoorziening (GGM exact, Werk, 12 attributen) — voorziening/dienst voor vergroten arbeidskansen werkzoekende; scholing, werkervaring, bemiddeling
- **Onderwerpoverzicht uitgebreid:** 15 → 19 begrippen, 2 → 4 BO's
- **GGM-terugmelding:** Loonkostensubsidie heeft slechts 1 attribuut (PercentageLoonwaardeWML); in praktijk worden meer gegevens geregistreerd
- **Eerste dekking** voor GGM-beleidsdomein Werk (33 entiteiten, nu 2 BO's)
- **bo_count:** 140 → 142

## [2026-06-25] ingest | Asiel en Integratie — handreiking financieel ontzorgen, onderwerpoverzicht aangemaakt
- **Bron:** Divosa — Handreiking Financieel ontzorgen en financiële zelfredzaamheid (feb. 2024, update juli 2025), gecrawld via crawl4ai
- **Geen nieuwe BO's:** alle begrippen vallen onder bestaande BO's (Asielstatushouder, PIP, Brede Intake, etc.) of bestaande GGM-entiteiten (Leenbijstand, Inkomensvoorziening)
- **Nieuw onderwerpoverzicht:** `Wiki/Onderwerpoverzichten/asiel-en-integratie.md` — 38 begrippen, 15 BO's, 7 verwerkte bronnen
- **Bronsamenvatting:** `Wiki/Bronsamenvattingen/Asiel en Integratie/divosa-handreiking-financieel-ontzorgen.md`
- **Observatie:** financieel ontzorgen is proces (vastgelegd in PIP en Inkomensvoorziening), geen zelfstandig BO. Inrichtingskrediet = Leenbijstand (GGM). Budgetbeheer = uitvoeringswijze Schuldhulptraject.

## [2026-06-25] ingest | Schulden en Armoede — vroegsignalering verrijkt, 1 nieuw BO
- **Bron:** Divosa — Vroegsignaleringsaanpak gemeenten onder de loep (sept. 2024), landelijk onderzoek 167 gemeenten
- **1 nieuw BO:** Contactpoging (GGM exact, Vroegsignalering) — gepromoveerd van GGM-component naar zelfstandig BO op basis van empirische onderbouwing (meest bepalende factor voor bereik, eigen attributen en levenscyclus)
- **3 bestaande BO's verrijkt:** Vroegsignaal, Vroegsignaalzaak, Signaalpartner — nieuwe bronsamenvatting toegevoegd
- **6 nieuwe begrippen** in onderwerpoverzicht: contactpoging (✅), hulpacceptatie, drempelbedrag, laatsignaal, BRP-koppeling, CAK-lijst, bereikpercentage
- **bo_count:** 139 → 140

## [2026-06-25] ingest | Werk en Inkomen — afgerond, 2 BO's
- **7 VNG-portaalpagina's** → Niet-relevant (arbeidsmarktbeleid, inkomensondersteuning-alleenverdieners, migratie-en-werk, participatiewet-in-balans, rubriek, toezicht-en-handhaving, wsw)
- Domein afgerond: 1 bronsamenvatting, 7 niet-relevant, 15 begrippen, 2 BO's

## [2026-06-25] ingest | Werk en Inkomen — eerste bron, 2 nieuwe BO's
- **Bron:** Factsheet Bijzondere Bijstand (Divosa/BMC/Stimulansz, mei 2024) — 4 bronbestanden, 1 bronsamenvatting
- **Nieuw onderwerp:** Werk en Inkomen — eerste onderwerpoverzicht met 15 begrippen
- **2 nieuwe BO's:**
  - Inkomensvoorziening (GGM exact, Model Inkomen) — overkoepelend concept voor structurele en tijdelijke inkomensregelingen (bijstandsuitkering, bijzondere bijstand, energietoeslag, TONK); 10 subtypes
  - Draagkracht (GGM exact, Sociaal Domein Generiek) — berekend vermogen van inwoner om zelf in kosten te voorzien; bepalend voor recht op bijzondere bijstand
- **GGM-terugmeldingen:** #56-58 (Inkomensvoorziening definitie, Draagkracht definitie, Periodiek dienst Bijz. bijstand redundant)
- **Eerste dekking** voor GGM-beleidsdomeinen Inkomen/Diensten, Model Inkomen, Normafwijking, Reden aanvraag (stonden allen op "zonder bronnen")
- **bo_count:** 137 → 139

## [2026-06-25] coverage | Herberekening na VTH-ingest
- **137 BO's** (was 135), 771 entiteiten niet beoordeeld (was 773)
- 9 generalisaties, 18 subtypes, 14 componenten, 5 begrippentabel-assessments
- 19 beleidsdomeinen zonder bronnen
- Taakveld 1 VTH: 7 BO-matches (was 6), 6 subtypes beoordeeld

## [2026-06-23] herbeoordeling | Belastingen — subtypes en 2 nieuwe BO's
- **Herbeoordeling onderwerpoverzicht belastingen**: 18 belastingtypen (OZB, hondenbelasting, precario, etc.) geherclassificeerd van "object ❌" naar "subtype ❌" — het zijn subtypes van Heffing, geen losse classificaties
- **2 nieuwe BO's:**
  - Heffinggrondslag (GGM exact, 1 VV) — tariefregel in verordening; koppelt Heffingsverordening aan Heffing
  - WOZ-deelobject (GGM exact, RSGBPlus) — element van WOZ-object voor waarde-onderbouwing
- **Verrijkte bestaande BO's:**
  - Heffing: uitgebreide Subtypes-sectie met alle 18 belastingtypen in 4 categorieën + relatie Heffinggrondslag
  - Heffingsverordening: Subtypes-sectie uitgebreid van 2 naar 14 verordening-subtypes + relatie Heffinggrondslag
  - WOZ-object: relatie naar WOZ-deelobject toegevoegd
- **Onderwerpoverzicht:** heffingsmaatstaf en tarief geherclassificeerd als attributen van Heffinggrondslag
- **bo_count:** 9 → 11

## [2026-06-23] coverage | Herberekening na Omgevingswet-ingest
- **135 BO's**, 773 entiteiten niet beoordeeld (was 782)
- Taakveld 1 VTH: 6 BO-matches (was 2), 6 subtypes beoordeeld
- Onderwerpoverzicht Omgevingswet nu gelinkt in coverage

## [2026-06-23] ingest | Omgevingswet — eerste bron, 4 nieuwe BO's
- **Bron:** Uitvoeringsbeleid VTH Delft 2024-2028 (58 pagina's, gemeente Delft)
- **Nieuw onderwerp:** Omgevingswet — onderwerpoverzicht aangemaakt met 14 begrippen
- **4 nieuwe BO's:**
  - VTH-zaak (GGM VTHzaak, exact) — centraal dossier voor vergunningverlening, toezicht en handhaving
  - Inspectie (GGM Inspectie, functioneel) — toezichtscontrole; ⚠️ GGM-definitie te smal (boezemkade)
  - Bevinding (GGM Bevinding, exact) — uitkomst van inspectie met risico en ernst
  - Handhavingsbesluit (procesobject, GGM-hiaat) — formeel besluit bij overtreding
- **Verrijkte bestaande BO's:**
  - Vergunningen en ontheffingen: omgevingsvergunning-subtype verrijkt
  - Aanvraag of melding: subtypes-sectie toegevoegd (bouwmelding Wkb, handhavingsverzoek, VTH-melding, e.a.)
  - Heffingsverordening: subtype legesverordening toegevoegd
- **Terugmeldingen GGM:** Inspectie-definitie te domeinspecifiek; Handhavingsbesluit ontbreekt
- **Status:** 9 bronnen nog te verwerken in dit onderwerp

## [2026-06-23] Economie — 5 GGM-entiteiten beoordeeld, coverage-script uitgebreid
- **5 GGM-entiteiten taakveld 3** formeel beoordeeld als geen BO: Contact, Hotelbezoek, Verkooppunt, Werkgelegenheid, Winkelvloeroppervlak
- **Begrippentabel uitgebreid:** 4 nieuwe entries (Contact, Verkooppunt, Werkgelegenheid, Winkelvloeroppervlak; Hotelbezoek stond er al)
- **Coverage-script verbeterd:** `coverage_analysis.py` detecteert nu ook begrippentabel-beoordelingen (BO?=❌, GGM=ja) als "beoordeeld, geen BO"
- **Taakveld 3 Economie:** van 1/6 naar 6/6 entiteiten beoordeeld
- **Totaal niet beoordeeld:** 787 → 782

## [2026-06-23] ingest | Financien — afgerond (10 BO's, 4 bronsamenvattingen)
- **6 bronnen beoordeeld:** 4 raadgever-bronnen (eerder samengevat), 2 VNG-portaalpagina's
- **2 bronnen naar Niet-relevant:** begroting-en-verantwoording (portaalpagina, gedekt door raadgevers), gemeentefonds-en-btw-compensatiefonds (portaalpagina, gedekt door raadgever-inkomstenbronnen)
- **Onderwerpoverzicht bijgewerkt:** bronverwijzingen gecorrigeerd naar wiki-links, niet-relevante bronnen toegevoegd, cross-domein sectie uitgebreid, status → afgerond
- **Geen nieuwe BO's** — 10 bestaande BO's uit GGM-beleidsdomein Financien (taakveld 9) bevestigd via bronnen
- **20 begrippen** in onderwerpoverzicht: 10 BO, 10 niet-BO (instrumenten, kengetallen, thema's)

## [2026-06-23] ingest | Bestuur — Partijsubsidie (1 BO, 2 bronsamenvattingen)
- **4 bronnen opgehaald:** VNG Model Subsidieregeling decentrale politieke partijen (nieuwspagina, ledenbrief PDF, modelverordening DOCX, implementatiehandleiding DOCX)
- **2 bronnen naar Niet-relevant:** nieuwspagina (dun, samenvatting), ledenbrief (dupliceert verordening)
- **2 bronsamenvattingen:** model-subsidieregeling-politieke-partijen, implementatiehandleiding-subsidieregeling-politieke-partijen
- **1 nieuw BO:** [[Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/politiek/partijsubsidie|Partijsubsidie]] — procesobject, geen GGM-entiteit in taakveld 0
- **GGM-hiaat genoteerd:** politieke partijen niet gemodelleerd onder taakveld 0; Raadslid.fractie is enige referentie

## [2026-06-23] coverage | GGM-dekkingsanalyse geregenereerd
- [[Wiki/Analyses/ggm-dekking|ggm-dekking]] opnieuw gegenereerd via `coverage_analysis.py`
- 954 objecttype-entiteiten in 44 beleidsdomeinen, 132 BO's vastgelegd, 787 niet beoordeeld
- 19 beleidsdomeinen zonder bronnen (incl. Griffie, ICT, Inkoop, Subsidies, Vastgoed, Werk, div. Inkomen-subdomeinen)

## [2026-06-23] ingest | Schulden en Armoede — 9 BO's, 2 bronsamenvattingen
- **5 bronnen beoordeeld:** 1 zeer rijk (beleidsplan Den Haag), 2 dunne VNG-pagina's (gebundeld), 1 stub, 1 niet-relevant (hersteloperatie kinderopvangtoeslag → Niet-relevant/)
- **2 bronsamenvattingen** aangemaakt: beleidsplan-schuldhulpverlening-den-haag-2024-2028, vng-schulden-en-armoede
- **9 BO-pagina's** aangemaakt in Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/:
  - Schuldhulpverlening (7): Schuldhulptraject, Schuld, Schuldregeling, Schuldeiser (actor), Moratorium, WSNP-traject
  - Vroegsignalering (3): Vroegsignaal, Vroegsignaalzaak, Signaalpartner (actor)
- **28 begrippen** beoordeeld in onderwerpoverzicht (9 BO, 19 niet-BO)
- **GGM-dekking:** 33 entiteiten in 2 sub-domeinen (Schuldhulpverlening 27, Vroegsignalering 6). 9 BO, 12 GGM-componenten op Schuldhulptraject/Vroegsignaalzaak, 12 context/classificatie.
- **Nieuw:** GGM-componenten patroon — procesfasen (Aanmelding, Intake, Stabilisatie, etc.) als ## GGM-componenten sectie op BO-pagina, niet als apart BO
- **Tooling:** coverage_analysis.py uitgebreid met subtype- en componentdetectie (↓ subtype van X, ◆ onderdeel van X); assess-bo skill: actoren zijn nu BO-kandidaat; generate_ggm_wiki.py nieuw script + /generate-ggm skill

## [2026-06-23] coverage | volledige GGM-dekkingsanalyse v2
- **Gegenereerd:** Centrale dekkingspagina [[Wiki/Analyses/ggm-dekking|ggm-dekking]] per taakveld
- **Wijzigingen t.o.v. v1:**
  - Filter `stereotype == 'Objecttype'` i.p.v. `gemma_type == 'business-object'` → 954 entiteiten (was 437)
  - Taakveld-hiërarchie dynamisch uit GGM-packages: sub-taakvelden (Erfgoed, Inkomen, Schulden) genest onder hun parent
  - Weggefilterde UML-types (Enumeratie: 388, Class zonder stereotype: 22) getoond in statistieken
  - Generalisatie-detectie: parent entities als "Geen bedrijfsobject (generalisatie van ...)"
  - Entiteiten alfabetisch gesorteerd
- **Statistieken:**
  - Totaal GGM-entiteiten: 1364 (waarvan 954 Objecttype in tabellen)
  - Bedrijfsobjecten vastgelegd: 123 (13%)
  - Generalisaties: 9
  - Niet beoordeeld: 822 (86%)
- **Skill update:** `/coverage` aangepast voor Objecttype-filter, package-hiërarchie, UML-type statistieken

## [2026-06-23] Refactor: GGM-dekking naar centrale analysepagina
- **Reden:** GGM-beleidsdomeinen en wiki-domeinen lopen niet 1-op-1. Centrale dekkingspagina maakt per beleidsdomein zichtbaar welke bronnen beschikbaar zijn.
- **Wijzigingen:**
  - Nieuwe pagina: [[Wiki/Analyses/ggm-dekking|ggm-dekking]] — centrale dekkingstabel met 48 beleidsdomeinen, 922 GGM-entiteiten, bronnenaantal per domein
  - Verwijderd: GGM-entiteitendekking + GGM-dekkingsanalyse secties uit alle 24 domeinoverzichten
  - Herschreven: `/coverage` skill — nu met bronnenaantal per beleidsdomein
  - Bijgewerkt: `templates/onderwerpoverzicht.md` — geen GGM-dekkingssecties meer
  - Bijgewerkt: `/ingest` skill — verwijderd GGM-dekkingsstap (coverage is aparte actie)
  - Bijgewerkt: `/domain-status` skill — verwijzing naar centrale pagina
  - Bijgewerkt: `CLAUDE.md` — werkwijze-beschrijving, coverage-beschrijving
- **Statistieken centraal overzicht:**
  - 922 GGM-entiteiten: 122 BO (13%), 173 niet-BO (19%), 627 niet-beoordeeld (68%)
  - Volledig gedekt: Mobiliteit, Parkeren, Terug-en-invordering, Inburgering
  - Hiaten: Dierenwelzijn, Energie/Klimaat (geen beleidsdomeinen in GGM), Welstand (VTH nog niet verwerkt), BOR detail-niveaus

## [2026-06-22] ingest | Maatschappelijke Ondersteuning — domein afgerond, 9 BO's
- **16 bronnen beoordeeld:** 8 relevant, 8 naar Niet-relevant (portaalpagina's, procesbeschrijvingen)
- **2 nieuwe bronnen opgehaald:** beleidsnota-jeugd-utrecht (PDF, gemeente Utrecht 2025-2034), beleidsregels-jeugdhulp-oost-gelre (verordening, gemeente Oost Gelre 2025)
- **8 bronsamenvattingen** aangemaakt: 6 dunne VNG-pagina's + 2 rijke beleidsdocumenten
- **9 BO-pagina's** aangemaakt:
  - Generiek Jeugd en Wmo (5): Beschikking, Voorziening, Toewijzing, Levering, PGB-Toekenning
  - Sociaal Domein Generiek (1): Client
  - Jeugdbescherming en reclassering (1): Zorgmelding
  - Sociale Teams (1): SociaalTeamDossier
  - Dak- en thuislozen (1): Dakloosheid
- **25 begrippen** beoordeeld in domeinoverzicht (9 BO, 16 niet-BO)
- **GGM-dekking:** 97 entiteiten in 5 beleidsdomeinen; kernketen goed gedekt, hiaten bij kinderbeschermingsmaatregelen en jeugdhulpvormen als expliciete entiteiten

## [2026-06-22] ingest | Energie en Klimaat — domein afgerond, 3 BO's
- **2 bronnen naar Niet-relevant:** beleid-klimaatverandering (portaalpagina, gedekt door Visie Klimaatadaptatie), utrecht-klimaatneutraal (landingspagina, gedekt door Ontwerpvisie Klimaatneutraal)
- **Geen nieuwe BO's of begrippen:** beide bronnen bevatten geen informatie boven de al verwerkte rijkere beleidsdocumenten
- **Domein status:** afgerond — 7 bronsamenvattingen, 2 niet-relevant, 22 begrippen, 3 BO's (Warmtenet, Opwekgebied, Koelteplek)

## [2026-06-22] ingest | Economie — domein afgerond, 8 BO's
- **1 nieuwe bronsamenvatting:** handreiking effectrapportage bij nieuwe bedrijvigheid (VNG, 2024)
- **4 bronnen naar Niet-relevant:** rubriek-economie, breed-mkb-en-innovatie, regionale-economische-samenwerking, vitale-binnensteden-dorpskernen-en-werklocaties (portaalpagina's zonder BO-waarde)
- **2 nieuwe begrippen:** effectrapportage (instrument), arbeidsmigrant (doelgroep) — beide geen BO
- **Geen nieuwe BO's:** handreiking beschrijft beleidsinstrument/proces, geen registreerbare objecten
- **Domein status:** afgerond — 10 bronsamenvattingen, 7 niet-relevant, 34 begrippen, 8 BO's

## [2026-06-22] ingest | Belastingen — domein afgerond, 9 BO's
- **11 nieuwe bronsamenvattingen:** OZB, parkeerbelastingen, precario, reclamebelasting, hondenbelasting, BIZ-bijdrage, retributies, reinigingsheffingen, riool- en waterzorgheffing, toeristische heffingen, beleidsregels DFM
- **14 bronnen naar Niet-relevant:** portaalpagina's, duplicaten, buiten scope (rijksbelastingen)
- **2 nieuwe BO's:** Heffing (belastingaanslag, GGM Heffing 99 Kern) en Heffingsverordening (GGM Heffingsverordening 1 VTH)
- **6 nieuwe begrippen:** roerende-zaakbelasting, watertoeristenbelasting, marktgeld, havengeld, lijkbezorgingsrechten, staanplaatsgeld
- **GGM-dekkingsanalyse** bijgewerkt: Heffing en Heffingsverordening waren reeds in GGM aanwezig (eerder als hiaat genoteerd)
- **Domein status:** afgerond — 22 bronnen verwerkt, 46 begrippen, 9 BO's

## [2026-06-22] ingest | Arbeidszaken — 12 BO's vanuit bedrijfsvoeringsperspectief
- **Nieuwe bron:** handreiking-flexibele-arbeidsinzet.pdf (VNG/Capra, feb 2024) — juridische handreiking detachering, contractvormen, inhuur
- **Herbeoordeling:** domein opnieuw beoordeeld vanuit bedrijfsvoeringsperspectief; GGM HR-domein (31 entiteiten, taakveld 9) was eerder over het hoofd gezien
- **12 nieuwe BO's** in Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/:
  - Formatie: Formatieplaats, Functie
  - Werving: Vacature, Sollicitatie
  - Dienstverband: Dienstverband (4 subtypes), Werknemer
  - Uitvoering: Verlof, Verzuim, Declaratie, Beoordeling (3 subtypes gesprekscyclus), Disciplinaire Maatregel
  - Samenwerking: Detacheringsovereenkomst (GGM-hiaat #52)
- **GGM-dekking:** 31 entiteiten beoordeeld: 11 BO, 20 niet-BO, 1 hiaat, 1 definitiecorrectie (#53: Beoordeling)
- **Domeinoverzicht** volledig herschreven: van 0 naar 12 BO's, begrippentabel van 11 naar 23 begrippen
- **12 bronsamenvattingen** (9 eerder + 1 nieuw + 2 bestaand)

## [2026-06-22] ingest | Arbeidszaken — 9 resterende bronnen samengevat
- **9 bronsamenvattingen** aangemaakt: rubriek, arbeidsmarktkrapte, arbeidsmigranten, arbeidsvoorwaarden, financiële arbeidsvoorwaarden, integriteit, P&O-beleid, rechtspositie politieke ambtsdragers, werk voor arbeidsbeperkten

## [2026-06-22] update | Onderwijs — openstaande punten opgelost
- **1 nieuw BO:** Kinderopvangvoorziening (procesobject, GGM-hiaat #51) — met subtypes KDV, BSO, gastouderopvang
- **School bijgewerkt:** MFA als 6e subtype toegevoegd; relatie naar Binnenlocatie (gymzaal, cross-domein taakveld 5)
- **Domeinoverzicht** uitgebreid naar 31 begrippen, 11 BO's
- **Bron toegevoegd:** soorten-kinderopvang.md (Rijksoverheid)
- **GGM-terugmelding** #51: Kinderopvangvoorziening ontbreekt in GGM

## [2026-06-22] ingest | Onderwijs (10 nieuwe BO's, 10 bronnen)
- **Bronnen opgehaald:** utrecht.nl/onderwijshuisvesting + 6 PDF's (beleidsnota, UVP, wijkprofielen, adviezen, voortgangsrapportage, leerlingenprognose) + 7 bestaande VNG-bronnen
- **4 bronnen niet-relevant:** rubriek-onderwijs, wijkprofielen, voortgangsrapportage, leerlingenprognose (statistiek/operationeel)
- **8 bronsamenvattingen** aangemaakt in Wiki/Bronsamenvattingen/onderwijs/
- **10 nieuwe BO's:**
  - Onderwijs (5): School (subtypes: PO, VO, SO/SBO/VSO, buurtschool, kindcentrum), Leerling, Inschrijving, Uitschrijving, Ouder Of Verzorger
  - Leerplicht en Leerlingenvervoer (5): Verzuimmelding, Vrijstelling, Procesverbaal Onderwijs, Aanvraag Leerlingenvervoer, Beschikking Leerlingenvervoer
- **Domeinoverzicht** Wiki/Domeinen/onderwijs.md aangemaakt (27 begrippen, 10 BO's)
- **GGM-dekking:** taakveld 4 volledig beoordeeld (27 entiteiten: 10 BO, 17 niet-BO). Geen GGM-hiaten; alle BO's hebben exact GGM-match.
- **Observatie:** GGM modelleert geen entiteiten voor onderwijshuisvesting (schoolgebouw, gymzaal, MFA). Deze vallen buiten GGM-scope taakveld 4 maar zijn prominent in beleidsbronnen.

## [2026-06-22] nieuw BO | Vergunningen en ontheffingen — domeinoverstijgend parent BO
- **1 nieuw BO:** [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/vergunningen-en-ontheffingen|Vergunningen en ontheffingen]] (procesobject, GGM-hiaat #50)
  - Domeinoverstijgend parent BO voor alle gemeentelijke vergunningen en ontheffingen
  - Specialisaties: Evenementenvergunning, Parkeervergunning, Ontheffing (milieuzone)
  - Subtypes (geen apart BO): Standplaatsvergunning, Horecavergunning, Ligplaatsvergunning, Exploitatievergunning (vaarverkeer), Omgevingsvergunning
- **3 BO's bijgewerkt** met generalisatie-relatie naar parent:
  - Evenementenvergunning — generalisatie + body geactualiseerd (ter-discussie verwijderd)
  - Parkeervergunning — generalisatie-relatie toegevoegd
  - Ontheffing (milieuzone) — generalisatie + body geactualiseerd
- **Evenement** — aantekening over generiek vergunnings-BO geactualiseerd
- **GGM-terugmeldingen** — nieuw item #50 (structuur: ontbrekend generiek vergunnings-/ontheffingsconcept), item #44 gelinkt

## [2026-06-21] ingest | Wonen — Woonboten (1 nieuw BO, 1 BO verrijkt, 3 bronnen)
- **Bronnen opgehaald:** omgevingsvisie.utrecht.nl/thematisch-beleid/woonboten + 2 PDF's
  - Woonbotenbeleid september 2007 (hoofdbron, 30 p.)
  - Behouden van historische schepen in Utrecht (december 2015, 12 p.)
  - Overzichtspagina woonboten (webpagina, samenvatting)
- **3 bronsamenvattingen** aangemaakt in Wiki/Bronsamenvattingen/Wonen/
- **1 nieuw BO:**
  - Woonboot (GGM Vaartuig, sterk) — met 4 subtypes: woonark, varend schip, historisch schip, schark
- **1 BO verrijkt:**
  - Ligplaats — was procesobject/GGM-hiaat, nu ggm-entiteit (GGM BAG Ligplaats, exact). Bronnen en relaties aangevuld met woonbotenbeleid. Terugmelding #47 opgelost.
- **Domeinoverzicht** Wiki/Domeinen/wonen.md uitgebreid (32 begrippen, 5 BO's)
- **Observatie:** 334 woonboten in Utrecht (stabiel bestand). Ligplaatsvergunningenstelsel via Havenverordening/Havenatlas. Historische schepen (≥50 jaar) beschermd in drie zones: Keulsekade, Vechtdijk, Oosterkade.

## [2026-06-21] ingest | Wonen (3 nieuwe BO's, 7 bronnen)
- **Bronnen opgehaald:** omgevingsvisie.utrecht.nl/thematisch-beleid/wonen + 6 PDF's en 3 regelgeving-pagina's
  - Beleidsnota Wonen in Utrecht 2025-2030 (hoofdbron, 107 p.)
  - Huisvestingsverordening gemeente Utrecht (lokaleregelgeving.overheid.nl)
  - Nadere regel Huisvestingsverordening (lokaleregelgeving.overheid.nl)
  - Beleidsregel Huisvestingsverordening (lokaleregelgeving.overheid.nl)
  - Actieplan betaalbare koopwoningen 2021 (bestuurlijkeinformatie.nl)
  - Actieplan Middenhuur 2017 (bestuurlijkeinformatie.nl)
  - Werkwijze extra woningen toevoegen aan gebouw (bestuurlijkeinformatie.nl)
  - 4 bronnen → Niet-relevant (overzichtspagina's en addenda opgenomen in beleidsnota)
- **7 bronsamenvattingen** aangemaakt in Wiki/Bronsamenvattingen/Wonen/
- **3 nieuwe BO's:**
  - Woning (GGM Gebouw, sterk) — met 4 subtypes: sociale huurwoning, middenhuurwoning (GGM-hiaat), betaalbare koopwoning, studentenwoning
  - Woningbouwplan (GGM Plan, exact)
  - Urgentverklaring (governance-object, GGM-hiaat) — 7 subtypes per urgentiecategorie
- **Domeinoverzicht** Wiki/Domeinen/wonen.md aangemaakt (22 begrippen, 3 BO's)
- **GGM-hiaten:** Middenhuurwoning (subtype Gebouw), Urgentverklaring (nieuw objecttype)
- **Observatie:** GGM Bouwen en Wonen (7 entiteiten) dekt alleen woningbouw, niet toewijzing/verdeling. Vergunningen (huisvesting, omzetting, splitsing, woningvorming) zijn als instrumenten vastgelegd maar niet als BO; bij VTH-ingest opnieuw te beoordelen.

## [2026-06-21] ingest | Welstand (2 nieuwe BO's, 2 bronnen)
- **Bronnen opgehaald:** omgevingsvisie.utrecht.nl/thematisch-beleid/welstand + 2 PDF's
  - Welstandsnota De Utrechtse aanpak (Deel A: beleidskader, typologieën, beleidsniveaus, criteria, begrippenlijst)
  - Welstandscriteria en richtlijnen (Deel B: toetsingscriteria per bouwwerktype)
  - 2 summiere webpagina's → Niet-relevant (gedekt door PDF-bronnen)
- **2 bronsamenvattingen** aangemaakt in Wiki/Bronsamenvattingen/Welstand/
- **2 nieuwe BO's:**
  - Welstandsadvies (procesobject, GGM-hiaat) → Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/
  - Beschermde Status (GGM exact, domein Erfgoed) → Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/
- **Domeinoverzicht** Wiki/Domeinen/welstand.md aangemaakt (10 begrippen, 2 BO's)
- **Observatie:** welstandsdomein is primair beleidskader; de meeste concepten zijn classificaties of regels. Beschermde Status verhuisd naar Erfgoed.

## [2026-06-21] ingest | Milieu — Water en riolering (10 nieuwe BO's, 3 bronnen)
- **Bronnen opgehaald:** omgevingsvisie.utrecht.nl/thematisch-beleid/water + 3 PDF's via bestuurlijkeinformatie.nl
  - Visie Water en Riolering Utrecht (strategisch beleidskader, horizon 2050)
  - Programma Water en Riolering 2025-2029 (uitvoeringsprogramma met budgetten)
  - Beleidsnota Stadswater (gebruik vaarwegen en buitenzwemwater, horizon 2040)
  - Overzichtspagina water.md → Niet-relevant (gedekt door bovenstaande)
- **3 bronsamenvattingen** aangemaakt in Wiki/Bronsamenvattingen/milieu/
- **10 nieuwe BO's** aangemaakt in Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/:
  - GGM exact (7): Gemaal, Kolk, Overstortconstructie, Bergingsbassin, Waterobject, Rioleringsgebied, Put
  - GGM-hiaat (3): Buitenzwemplek, Ligplaats, Rioolheffing
- **1 subtype** toegevoegd aan bestaand BO Kunstwerk: Sluis (GGM-hiaat)
- **Put** als BO met 3 subtypes: Drainageput, Filterput, Infiltratieput
- **Rioleringsgebied** met subtype Bemalingsgebied
- **Buitenzwemplek** met relatie naar Zwembad (Sport) — zelfde behoefte, ander objecttype
- **Domeinoverzicht milieu** uitgebreid met 4e subdomein "Water en riolering" + begrippentabel (20 begrippen)
- **GGM-terugmeldingen** uitgebreid: #46-49 (Buitenzwemplek, Ligplaats, Rioolheffing, Sluis)
- Counts: bronnen 7→10, begrippen 42→62, BO's 23→33

## [2026-06-21] re-ingest | Mobiliteit — Mobiliteitsplan 2040 (1 nieuw BO, regels bijgewerkt)
- **Aanleiding:** heringest wegens gewijzigde assess-bo regels (data-object classificatie, instrumenten als BO-kandidaten).
- Bron opgehaald via /fetch: omgevingsvisie.utrecht.nl/thematisch-beleid/verkeer-en-mobiliteit. Overzichtspagina niet-relevant (gedekt door bestaande PDF).
- Mobiliteitsplan 2040 PDF opnieuw geconverteerd en frontmatter toegevoegd.
- **Domeinoverzicht bijgewerkt:**
  - Data-object kolom toegevoegd aan alle 8 secties van de begrippentabel (stap 9 assess-bo).
  - 3 instrumenten herbeoordeeld (Kwaliteitsnet, Wiel met Spaken, MaaS) — alle drie blijven ❌ onder nieuwe regels (falen op meervoud/levenscyclus).
  - 2 nieuwe begrippen: Voetgangersgebied (✅ BO), Compartimenteringszone (❌).
- **1 nieuw BO:** [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/voetgangersgebied|Voetgangersgebied]] (6/6 criteria, governance-object, GGM-hiaat). Aangewezen gebied waar voetganger hoofdgebruiker is (binnenstad, USP, LRC).
- **1 GGM-terugmelding:** Voetgangersgebied (#36) — vergelijkbaar met Zero-emissiezone qua opzet.
- Bronsamenvatting aangevuld met Voetgangersgebied als kernbegrip.
- Domein Mobiliteit: 29 BO's, 43 begrippen, 12 bronnen.

## [2026-06-21] ingest | Sport en Bewegen (7 BO's, 2 bronsamenvattingen, 1 GGM-hiaat)
- Bronnen opgehaald via /fetch: omgevingsvisie.utrecht.nl/thematisch-beleid/beleid-voor-sport-en-bewegen + 3 PDF's (beleidsnota 2025-2032, raadsbrief, uitvoeringsprogramma 2025-2026).
- PDF's geconverteerd naar markdown met convert_pdf.py.
- 2 bronnen niet-relevant verklaard: webpagina-samenvatting en raadsbrief (geen eigen informatie).
- 2 bronsamenvattingen: [[Wiki/Bronsamenvattingen/Sport en Bewegen/beleidsnota-sport-en-bewegen-2025-2032|Beleidsnota Sport en Bewegen 2025-2032]], [[Wiki/Bronsamenvattingen/Sport en Bewegen/uitvoeringsprogramma-sport-en-bewegen-2025|Uitvoeringsprogramma Sport en Bewegen 2025-2026]].
- **7 BO's aangemaakt** (GGM beleidsdomein Sport, taakveld 5):
  - **Sportlocatie** (6/6, GGM exact) — abstracte generalisatie
  - **Sportpark** (6/6, GGM exact) — specialisatie Sportlocatie
  - **Binnenlocatie** (6/6, GGM exact) — specialisatie Sportlocatie, subtypes sporthal/gymzaal
  - **Veld** (6/6, GGM exact) — sportveld, capaciteitsberekeningen per sporttype
  - **Zwembad** (6/6, GGM-hiaat) — gemeentelijke zwemvoorziening
  - **Sportvereniging** (6/6, GGM exact) — actor, goedgekeurd door team
  - **Sportmateriaal** (6/6, GGM exact)
- 5 niet-BO begrippen: sport- en beweegaanbieder, sportaccommodatie, beweegvriendelijke openbare ruimte, urban sports, positieve sportcultuur.
- Nieuw domeinoverzicht: [[sport-en-bewegen|Sport En Bewegen]].
- **1 GGM-terugmelding:** Zwembad ontbreekt in GGM beleidsdomein Sport.
- GGM-dekking Sport: 6/13 entiteiten → BO, 5 niet-BO (4× Proxyconnector + Belijning), 2 meetwaarden (Bezetting, Onderhoudskosten).

## [2026-06-21] ingest | Visie Speelruimte Utrecht (1 nieuw BO, 1 bronsamenvatting, 1 BO verrijkt)
- Bron opgehaald via /fetch: omgevingsvisie.utrecht.nl/thematisch-beleid/speelruimte + PDF "Spelen in je eigen buurt" (48 p., maart 2022).
- PDF geconverteerd naar markdown met convert_pdf.py, opgeslagen in `Sources/Onderwerpen/Ruimte Wonen en Mobiliteit/converted_pdf/`.
- Webpagina verplaatst naar Niet-relevant (volledig gedekt door PDF).
- Bronsamenvatting: [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/visie-speelruimte-utrecht|Spelen in je eigen buurt — Ontwerpvisie Speelruimte Utrecht]].
- 1 nieuw BO: **Speelterrein** (6/6 criteria, exact GGM-match FunctioneelGebied). Subtypes: buurtplek, blokplek, speelhoekje, stedelijke sportplek.
- 1 BO verrijkt: **Speeltoestel** — bron en relatie naar Speelterrein toegevoegd.
- 6 nieuwe begrippen in domeinoverzicht BOR: speelterrein (BO), speelbuurt, buurtplek, blokplek, speelruimtenorm, speelruimtescan.
- Aandachtspunt: overlap subtype "Speelplek" bij Maatschappelijke Voorziening met nieuw BO Speelterrein.
- Domein BOR: 9 BO's, 32 begrippen, 8 bronnen.

## [2026-06-21] ingest | Beleidsnota Werklocaties 2035 (1 BO, 1 bronsamenvatting)
- Bron opgehaald via /fetch: omgevingsvisie.utrecht.nl/plekken-voor-werk + PDF Beleidsnota Werklocaties 2035 (100+ p., 3 juni 2025).
- PDF geconverteerd naar markdown met convert_pdf.py, opgeslagen in `Sources/Onderwerpen/Economie/converted_pdf/`.
- 1 bronsamenvatting aangemaakt: beleidsnota-werklocaties-2035.
- **1 nieuw BO aangemaakt:**
  - **Werklocatie** — procesobject (GGM-hiaat). Aangewezen geografisch werkgebied met profiel. 5 subtypes: bedrijventerrein, kantoorlocatie, winkelgebied, innovatielocatie, wijkeconomie. Utrecht telt 31 werklocaties + 40 winkelgebieden. 6/6 criteria.
- 8 niet-BO begrippen toegevoegd aan begrippentabel: bedrijventerrein, kantoorlocatie, innovatielocatie, wijkeconomie, milieucategorie, retailhoofdstructuur, functiemenging, commerciële voorziening, stadslogistiek, circulaire bedrijvigheid.
- Winkelgebied herclassificeerd van "te generiek" naar "subtype van werklocatie".
- GGM-hiaat genoteerd: geen entiteit voor werklocatie als geografisch werkgebied; Vestiging (RSGB) dekt alleen individuele bedrijfslocaties.
- Domeinoverzicht Economie bijgewerkt: 9 BO's, 30 begrippen, 9 bronnen.

## [2026-06-21] ingest | Parkeerbeleid Utrecht (2 BO's, 8 bronsamenvattingen)
- 10 bronnen opgehaald via /fetch: Omgevingsvisie Utrecht parkeerbeleid (webpagina + 7 PDF's + 2 beleidsregels lokaleregelgeving.overheid.nl). 2 bronnen (Parkeervisie, Uitvoeringsprogramma) niet bereikbaar (iBabs 500 error).
- 8 bronsamenvattingen aangemaakt: beleidsregel-parkeernormen-fiets-2021, beleidsregel-parkeernormen-auto-2021, module-parkeernormen, uitwerking-parkeerhubs, rapportage-routekaart-parkeerhubs, uitwerking-fietsparkeren, uitwerking-parkeren-openbare-ruimte, uitwerking-toegankelijkheid.
- **2 nieuwe BO's aangemaakt:**
  - **Gehandicaptenparkeerkaart (GPK)** — procesobject (GGM-hiaat). Europees document, gemeente geeft uit op basis medisch advies. Subtypes: bestuurder/passagier/combi/instelling. 6/6 criteria.
  - **Gehandicaptenparkeerplaats** — procesobject (GGM partieel: Parkeervlak.doelgroep). Specialisatie van Parkeervlak met eigen beleidsregel, processen, sensoren. Subtypes: algemeen/individueel. 6/6 criteria. ⚠️ ter discussie: zelfstandig BO vs. subtype.
- 11 niet-BO begrippen toegevoegd aan begrippentabel: parkeernorm, deelautoplek, bereikbaarheidsfonds, mobiliteitsbeheerplan, fietsdepot, fietsparkeerverbodzone, betaald parkeergebied, mobiliteitslabel, maatwerklocatie.
- Bestaande parkeer-BO's verrijkt met bronverwijzingen uit nieuwe bronnen.
- GGM-terugmeldingen: GPK ontbreekt als entiteit; gehandicaptenparkeerplaats niet als apart type.
- Domeinoverzicht bijgewerkt: 28 BO's (was 26), 41 begrippen (was 30), 12 bronnen (was 2).
- Aanvulling: Parkeervisie (38 p.) en Uitvoeringsprogramma betaald parkeren (24 p., nov 2025) alsnog opgehaald na constructie van correcte iBabs download-URL's. 2 extra bronsamenvattingen aangemaakt. Geen nieuwe BO's (inhoud bevestigt bestaande begrippen).

## [2026-06-21] ingest | Beheer Openbare Ruimte — kwaliteit en beheer (5 BO's, 4 bronsamenvattingen)
- 4 bronnen opgehaald via /fetch: Nota Beheer OR (2021, 64 p. PDF), Kadernota KOR (2016, 49 p. PDF), overzichtspagina Omgevingsvisie, BInG-pagina utrecht.nl.
- 4 bronsamenvattingen aangemaakt: nota-beheer-openbare-ruimte, kadernota-kwaliteit-openbare-ruimte, kwaliteit-openbare-ruimte, openbare-ruimte-bing.
- 5 nieuwe BO's: Verhardingsobject (levensduur 40j, €35,7M achterstallig), Kunstwerk (50-70j, €7,6M achterstallig, subtypes Brug/Viaduct/Kademuur), Verlichtingsobject (25j), Speeltoestel (15j, 4x/jaar inspectie), Verkeerslicht (10j). Alle 6/6 criteria, exact GGM-match.
- 12 niet-BO begrippen toegevoegd aan begrippentabel: kwaliteitsniveau, BInG-toets, CROW-beeldkwaliteit, ontwikkelend beheer, straatmeubilair, bebording.
- Domeinoverzicht bijgewerkt: 8 BO's totaal (was 3), 26 begrippen (was 15), 7 bronnen (was 3). GGM-dekking: 8/200 beoordeeld, 192 niet beoordeeld (water/riolering/kabels nog geen beleidsbron).

## [2026-06-21] ingest | Sociaal Domein breed (0 BO's, 0 bronsamenvattingen)
- 11 onverwerkte VNG-rubrieken bronnen geïnventariseerd: alle zijn dunne portaalpagina's over beleid, processen en programma's zonder BO-kandidaten.
- Alle 11 verplaatst naar Niet-relevant/: rubriek-sociaal-domein-breed, aanpak-basisvaardigheden, iedereen-doet-mee, isd-informatievoorziening-sociaal-domein, multidisciplinair-handhaven, persoonsgebonden-budget, platform-sociaal-domein, project-toegang, richtinggevend-kader-convenant-en-verkenningsinstrument-toegang, wmo-2015-en-jeugdwet-toezicht-en-handhaving.
- Domein Sociaal Domein heeft nu 1 verwerkte bron (koersdocument) en 0 onverwerkte. Voor verdere verdieping zijn inhoudelijke beleidsdocumenten nodig (sportnota, Wmo-beleidsplan, cultuurvisie).

## [2026-06-21] ingest | Maatschappelijke voorzieningen (1 BO, 1 bronsamenvatting)
- Bron: Leefbare stad en maatschappelijke voorzieningen (Gemeente Utrecht, koersdocument maart 2020, ~870 regels). Opgehaald via /fetch als PDF + webpagina; webpagina naar Niet-relevant (overlapt met koersdocument).
- 1 bronsamenvatting aangemaakt: leefbare-stad-en-maatschappelijke-voorzieningen
- **1 nieuw BO aangemaakt:**
  - **Maatschappelijke voorziening** — ggm-afgeleid (Sportlocatie, School, Vastgoedobject). Overkoepelend concept voor plekken met maatschappelijk doel. 16 subtypes (buurtcentrum, buurtkamer, jongerenhuiskamer, gezondheidscentrum, sporthal, sportpark, zwembad, beheerde speeltuin, speelplek, wijkcultuurhuis, school, volkstuinpark, scoutingaccommodatie, dagbestedingslocatie, gezinshuis, maatschappelijke opvang).
- GGM-terugmelding #44: overkoepelend concept maatschappelijke voorziening ontbreekt; welzijns-, zorg- en cultuursubtypen hebben geen GGM-entiteit.
- Assess-bo skill aangepast: beslisregel stap 4 stond categorisch toe dat abstract niveau geen BO wordt bij herkenbare specialisaties — nu mag abstract niveau ook BO worden als het zelf de 6 criteria haalt.

## [2026-06-21] ingest | Luchtkwaliteit (7 BO's, 1 bronsamenvatting)
- Bron: Beleidsnota Luchtkwaliteit – Gezonde lucht voor iedereen 2025-2030 (Gemeente Utrecht, sept. 2024, 1267 regels). Opgehaald via /fetch als PDF + webpagina; webpagina naar Niet-relevant (overlapt volledig met beleidsnota).
- 1 bronsamenvatting aangemaakt: beleidsnota-luchtkwaliteit-2025
- **7 nieuwe BO's aangemaakt (alle GGM-hiaten):**
  - **Milieuzone** — procesobject. Afgebakend gebied met emissieklasse-eisen. Subtype: nul-emissiezone.
  - **Vuurwerkvrije zone** — procesobject. 150 zones, overgegaan naar gemeentebreed verbod.
  - **Luchtkwaliteitsmeetpunt** — procesobject. 64 gemeentelijke + 3 RIVM-meetlocaties.
  - **Rookvrije zone** — procesobject. Bushaltes, speelplekken, sportlocaties, USP.
  - **Ontheffing (milieuzone)** — procesobject. Individuele uitzondering op zone-regels.
  - **Walstroompunt** — procesobject. Ca. 50 fysieke aansluitpunten walstroom.
  - **Sloopregeling** — ⚠️ instrument, ter discussie. Subsidieregeling bij milieuzone-aanscherping.
- Domeinoverzicht milieu uitgebreid met subdomein "Luchtkwaliteit" (14 begrippen, 7 BO's).
- GGM-terugmeldingen: mist beleidsdomein luchtkwaliteit (taakveld 7), mist generiek zone-concept, mist generiek ontheffingsconcept.

## [2026-06-20] ingest | Klimaatverandering (1 BO, 3 bronsamenvattingen)
- Bronnen: 5 bestanden opgehaald via /fetch (omgevingsvisie.utrecht.nl/thematisch-beleid/beleid-voor-klimaatverandering + 3 PDF's via iBabs + 1 subpagina). 2 summiere webpagina's niet apart samengevat (overzichtspagina's).
- 3 bronsamenvattingen aangemaakt: visie-klimaatadaptatie-utrecht, ontwerpvisie-klimaatneutraal, raadsbrief-klimaatneutraal
- **1 nieuw BO aangemaakt:**
  - **Koelteplek** — procesobject, GGM-hiaat. Groene verblijfsplek ≥200 m², doelstelling binnen 200m loopafstand.
- Bestaande BO's in andere domeinen bevestigd vanuit klimaatbronnen: zero-emissiezone (mobiliteit), laadpaal (mobiliteit), bodemenergiesysteem (milieu)
- Domeinoverzicht uitgebreid met 10 nieuwe begrippen (klimaatadaptatie-thema's) en cross-domein verwijzingen
- WKO-installatie als subtype van bodemenergiesysteem genoteerd; wadi geparkeerd voor domein openbare ruimte

## [2026-06-20] ingest | Horeca, hotels en short stay (5 BO's, 1 GGM-match)
- Bronnen: 7 bestanden opgehaald via /fetch (omgevingsvisie.utrecht.nl/thematisch-beleid/horeca + 1 PDF + 5 gelinkte HTML-pagina's). 2 dunne iBabs-stubs naar Niet-relevant. Fetch-skill bijgewerkt: haalt nu ook HTML-links 1 level diep op.
- 5 bronsamenvattingen aangemaakt: horecabeleid-utrecht, actualisatie-marktruimte-hotelnota, beleidsregels-terrassen-utrecht, beleidsregel-hotels-utrecht, beleidsregels-short-stay-utrecht
- **5 nieuwe BO's aangemaakt:**
  - **Hotel** — GGM exact (Hotel, taakveld 3). Subtypes: concepthotel, doelgroephotel, minihotel
  - **Horecabedrijf** — GGM partieel (Vestiging RSGB). Subtype: horecavergunning
  - **Terras** — procesobject, GGM-hiaat. Terugmelding: registratieobject openbare ruimte
  - **Short Stay Accommodatie** — procesobject, GGM-hiaat. Capaciteitsgrenzen 1.080 eenheden
  - **Bed-and-breakfast** — procesobject, GGM-hiaat. Max 4 kamers, vergelijkbaar met Hotel
- Domeinoverzicht economie.md bijgewerkt: 8 begrippen + 5 BO's + 4 GGM-hiaten toegevoegd
- CLAUDE.md bijgewerkt: regel "Subtypes altijd vastleggen" toegevoegd bij BO-criteria

## [2026-06-20] ingest | Afval en circulaire economie (10 BO's, 4 GGM-match)
- Bronnen: 4 bestanden opgehaald via /fetch (omgevingsvisie.utrecht.nl + 3 PDF's: Grondstoffennota 2020, Visie Utrecht Circulair 2050, Beleidsnota Utrecht Circulair 2030). Portaalpagina naar Niet-relevant.
- 3 bronsamenvattingen aangemaakt: grondstoffennota-utrecht-2020.md, visie-utrecht-circulair-2050.md, beleidsnota-utrecht-circulair-2030.md
- GGM-beleidsdomein Afval (16 entiteiten) volledig beoordeeld: 4 BO, 12 niet-BO (te granulair/operationeel)
- **10 nieuwe BO's aangemaakt:**
  - **Container** — GGM exact, 3 subtypes (ondergronds, kliko, citybin)
  - **Grondstofstroom** — GGM sterk (Fractie), terugmelding: GGM-definitie te generiek
  - **Milieustraat** — GGM exact
  - **Afvalstoffenheffing** — GGM partieel (Prijsafspraak), cross-domain Belastingen
  - **Verwerkingscontract** — procesobject, GGM-hiaat
  - **Inzamelcontract** — procesobject, GGM-hiaat
  - **Upcyclecentrum** — procesobject, GGM-hiaat (nieuw concept circulaire economie)
  - **Grondstoffendepot** — procesobject, GGM-hiaat
  - **Materiaalpasspoort** — ⚠️ ter discussie (instrument)
  - **Afvalstoffenverordening** — ⚠️ ter discussie (governance)
- 4 begrippen niet-BO: HNI (proces), nascheiding (proces), circulaire economie (concept), sorteeranalyse (activiteit)
- Domeinoverzicht milieu.md uitgebreid met subdomein Afval en circulaire economie (28 begrippen, 16 BO's totaal)
- VNG-bron afval-en-circulaire-economie.md nog niet verwerkt (aanvullende landelijke context)

## [2026-06-20] ingest | Groenbeleid → Beheer Openbare Ruimte (2 BO's)
- Bronnen: 6 bestanden opgehaald via /fetch (omgevingsvisie.utrecht.nl + 5 PDF's), 2 hoog-relevant behouden, 4 naar Niet-relevant/
- 2 bronsamenvattingen aangemaakt: groenstructuurplan-utrecht-2007.md, actualisatie-groenstructuurplan-2017-2030.md (onder Wiki/Bronsamenvattingen/Milieu/)
- Bronnen zijn opgeslagen onder Sources/Onderwerpen/Milieu/ maar leveren BO's in domein Beheer Openbare Ruimte (GGM taakveld 8)
- **2 nieuwe BO's aangemaakt:**
  - **Groenobject** — GGM-match exact (Groenobject, IMBOR), 6/6 BO-criteria
  - **Faunapassage** — GGM-match sterk (Ecoduct), 6/6 BO-criteria, terugmelding: GGM Ecoduct is beperkter dan gemeentelijk begrip faunapassage
- 7 begrippen niet-BO: groenstructuur (structuur), visiekaart (instrument), groencompensatie (proces), beschermde soort (classificatie), wijkgroenplan (instrument)
- Domeinoverzicht beheer-openbare-ruimte.md bijgewerkt: 3 BO's, 15 begrippen
- Domeinoverzicht milieu.md bijgewerkt: cross-referentie naar BOR-domein

## [2026-06-20] ingest | Mobiliteit — nieuw domein (15 BO's, alle GGM-hiaten)
- Bronnen: 3 documenten opgehaald via /fetch (omgevingsvisie.utrecht.nl + 2 PDF's: Mobiliteitsplan 2040, Kwaliteitsnet Goederenvervoer 2007)
- 1 bron niet-relevant: webpagina goederenvervoer is te dun (3 alinea's) → verplaatst naar Niet-relevant/
- 2 bronsamenvattingen aangemaakt: mobiliteitsplan-2040.md (hoofdbron, 174p), kwaliteitsnet-goederenvervoer-2007.md (routestructuur)
- Nieuw domeinoverzicht aangemaakt: Wiki/Domeinen/mobiliteit.md (30 begrippen, 15 BO's)
- **13 nieuwe BO's aangemaakt** (alle procesobjecten/governance-objecten, GGM-hiaten) + **13 GGM-verificatie BO's** (9 parkeren, 4 mobiliteit):
  - Fiets: **Hoofdfietsroute**
  - OV: **OV-knooppunt**, **OV-lijn**, **Halte**
  - Multimodaal: **P+R-locatie**, **Mobiliteitshub**, **Laadpaal**
  - Goederenvervoer: **Logistieke Route**, **Laad- en Losplaats**, **Stadsdistributiepunt**, **Zero-emissiezone**, **Overslagpunt**, **Bouwlogistiek Centrum**
- **GGM-verificatie BO's aangemaakt:**
  - Parkeren: **Parkeerzone**, **Parkeergarage**, **Parkeervergunning**, **Parkeerrecht**, **Parkeervlak**, **Parkeerscan**, **Voertuig**, **Naheffing**, **MulderFeit** (alle exact match)
  - Mobiliteit: **Verkeersbesluit**, **Stremming**, **Verkeerstelling**, **Strooiroute** (alle exact match)
- 4 GGM-entiteiten niet-BO: Belprovider, Productgroep, Productsoort, Straatsectie (te operationeel/administratief)
- Structureel GGM-hiaat: functionele mobiliteitslaag (routes, knooppunten, haltes, hubs, zones) ontbreekt volledig in GGM
- Index en log bijgewerkt

## [2026-06-20] ingest | Openbare Gezondheid — domein afgerond (0 BO's)
- Bronnen: 8 documenten (4 VNG-onderwerpenpagina's, 2 gemeente Utrecht incl. PDF uitvoeringsprogramma mentale gezondheid 2025-2027)
- 2 bronnen naar Niet-relevant/: rubriek-openbare-gezondheid (1 zin), startpagina-aan-de-slag (methodologie)
- 1 bronsamenvatting aangemaakt: Wiki/Bronsamenvattingen/Openbare Gezondheid/gezondheidsbeleid-en-preventie.md (bundelt 6 bronnen)
- Nieuw domeinoverzicht aangemaakt: Wiki/Domeinen/openbare-gezondheid.md (8 begrippen, 0 BO's)
- **Geen BO's** — domein bestaat uit thema's (preventie, mentale gezondheid), instrumenten (GALA, IZA, preventieakkoord), actoren (GGD, JGZ) en activiteiten (monitoring, screening)
- Begraafplaats genoteerd als potentieel BO bij uitbreiding domein Beheer Openbare Ruimte (IMBOR kent entiteit)
- Zelfde patroon als Arbeidszaken: governance/programmatisch domein zonder registreerbare objecten
- Index en log bijgewerkt

## [2026-06-20] ingest | Geluid — actieplan toegevoegd (geen nieuwe BO's)
- Bron: Actieplan Geluid Utrecht 2018-2023 (Gemeente Utrecht, operationeel uitvoeringsprogramma bij beleidsnota)
- 1 bronsamenvatting aangemaakt: Wiki/Bronsamenvattingen/geluid/actieplan-geluid-utrecht.md
- Domeinoverzicht bijgewerkt: bronnen_count 1 → 2
- **Geen nieuwe BO's** — actieplan verdiept bestaande begrippen (Stil gebied, Geluidscherm, Geluidbron) maar introduceert geen nieuwe BO-kandidaten
- Verrijkingen: Stil gebied (drie schaalniveaus, koesteren/verbeteren/uitbreiden), Geluidscherm (binnenstedelijk onwenselijk), Geluidbron (wegverkeer dominant, asfalttypen)
- Niet-BO begrippen bevestigd: plandrempel (parameter), knelpuntlocatie (berekende status), geluidsanering (proces), geluidreducerend asfalt (eigenschap)
- Index en log bijgewerkt

## [2026-06-20] ingest | Gevaarlijke stoffen — 3 nieuwe BO's (alle partieel GGM-match)
- Bronnen: 2 documenten opgehaald via /fetch (omgevingsvisie.utrecht.nl + PDF beleidsnota via utrecht.bestuurlijkeinformatie.nl)
- 1 bron niet-relevant: webpagina is subset van beleidsnota → verplaatst naar Niet-relevant/
- 1 bronsamenvatting aangemaakt: Wiki/Bronsamenvattingen/gevaarlijke-stoffen/beleidsnota-omgevingsveiligheid.md
- Nieuw domeinoverzicht aangemaakt: Wiki/Domeinen/gevaarlijke-stoffen.md (9 begrippen, 3 BO's)
- **3 BO's aangemaakt:**
  - **Risicobron** (ggm-entiteit) — bedrijf, buisleiding of transportroute met gevaarlijke stoffen. GGM-match: Activiteit (Omgevingswet), partieel.
  - **Aandachtsgebied** (ggm-entiteit) — ruimtelijk gebied rond risicobron voor veiligheidsafweging. GGM-match: Gebiedsaanwijzing, partieel.
  - **Voorschriftengebied** (ggm-entiteit) — aangewezen gebied met aanvullende bouweisen. GGM-match: Gebiedsaanwijzing, partieel.
- 6 niet-BO begrippen: plaatsgebonden risico (norm), groepsrisico (norm), oriëntatiewaarde (norm), (beperkt) kwetsbare gebouwen (classificatie), zeer kwetsbare gebouwen (classificatie), basisnet (landelijk instrument)
- GGM-dekking: geen specifiek beleidsdomein voor omgevingsveiligheid; alle matches op generiek Omgevingswet-package
- Nieuw iBabs-downloadpatroon ontdekt: /Document/View/{id} voor /Reports/Document/ URLs → memory bijgewerkt

## [2026-06-20] ingest | Geluid — 5 nieuwe BO's (1 GGM-match, 4 hiaten)
- Bronnen: 2 documenten opgehaald via /fetch (omgevingsvisie.utrecht.nl + PDF beleidsnota via utrecht.bestuurlijkeinformatie.nl)
- 1 bron niet-relevant: webpagina is subset van beleidsnota → verplaatst naar Niet-relevant/
- 1 bronsamenvatting aangemaakt: Wiki/Bronsamenvattingen/geluid/beleidsnota-geluid-en-trillingen.md
- Nieuw domeinoverzicht aangemaakt: Wiki/Domeinen/geluid.md (9 begrippen, 5 BO's)
- **5 BO's aangemaakt:**
  - **Geluidbron** (procesobject) — object dat geluid veroorzaakt, ingedeeld naar bronsoort. GGM-hiaat.
  - **Geluidgevoelig gebouw** (procesobject) — gebouw waarvoor geluidnormen gelden. GGM-hiaat.
  - **Stil gebied** (procesobject) — rustig gebied dat de gemeente beschermt. GGM-hiaat.
  - **Geluidzone** (procesobject) — zone rond industrieterrein met cumulatieve normen. GGM-hiaat.
  - **Geluidscherm** (ggm-entiteit) — fysieke afscherming langs weg/spoor. GGM-match: Geluidsscherm (IMBOR, Beheer Openbare Ruimte), matchsterkte exact.
- 4 niet-BO begrippen: geluidontheffing (subtype vergunning), geluidluwe gevel (eigenschap), geluidkartering (activiteit), actieplan geluid (governance-instrument)
- GGM-dekking: geen beleidsdomein Geluid; Geluidsscherm staat in IMBOR/Beheer Openbare Ruimte
- Index en log bijgewerkt

## [2026-06-20] ingest | Evenementen — 3 nieuwe BO's (1 GGM-match, 2 hiaten)
- Bronnen: 2 documenten (Beleidsnota Locatiebeleid evenementen 2024-2030 PDF + overzichtspagina omgevingsvisie.utrecht.nl)
- Bronbestanden opgehaald via /fetch incl. PDF-conversie naar Sources/evenementen/
- 2 bronsamenvattingen aangemaakt in Wiki/Bronsamenvattingen/Evenementen/
- Nieuw domeinoverzicht aangemaakt: Wiki/Domeinen/evenementen.md (9 begrippen, 3 BO's)
- **3 BO's aangemaakt:**
  - **Evenement** (ggm-entiteit) — georganiseerde activiteit met publiek in de openbare ruimte. GGM-match: OpenbareActiviteit (VTH, taakveld 1), matchsterkte partieel (definitie te breed, geen relaties, dunne attributen).
  - **Evenementenlocatie** (procesobject) — aangewezen fysieke locatie met locatieprofiel (kaders voor dagen, omvang, geluid, rust). GGM-hiaat.
  - **Evenementenvergunning** (procesobject) — toestemming om een evenement te organiseren. GGM-hiaat. ⚠️ Op termijn nodig: generiek Vergunning-BO (GGM kent vergunningen alleen domeinspecifiek).
- 6 niet-BO begrippen: locatieprofiel (instrument), reserveringskalender (instrument), beoordelingscriteria (regel), stads- en volksfeest (classificatie), rustperiode (regel), winterbeperking (regel)
- GGM-dekking: geen beleidsdomein Evenementen; OpenbareActiviteit staat geïsoleerd in VTH zonder relaties of diagrammen
- GGM-terugmeldingen: #18 (OpenbareActiviteit definitie te breed), #19 (Evenementenlocatie hiaat), #20 (Evenementenvergunning hiaat + generiek vergunningsconcept ontbreekt)
- Index en log bijgewerkt

## [2026-06-20] ingest | Cultuur/Erfgoed — 1 nieuw BO (GGM-hiaat)
- Bronnen: 4 documenten opgehaald via /fetch (omgevingsvisie.utrecht.nl/thematisch-beleid/erfgoed + 3 PDF's)
- 1 bron niet-relevant: lijst beeldbepalende panden (adressenlijst) → verplaatst naar Niet-relevant/
- 3 bronsamenvattingen aangemaakt in Wiki/Bronsamenvattingen/Cultuur/ (visie-religieus-erfgoed-2025, erfgoedbeleid-utrecht, bijlagen-visie-religieus-erfgoed)
- Domeinoverzicht Wiki/Domeinen/cultuur.md bijgewerkt: 6 nieuwe begrippen (orgel, luidklok, ensemble, kerkgebouw, herbestemmingsprofiel, waardestelling, carillon), totaal nu 33 begrippen, 7 BO's
- **1 BO aangemaakt** (procesobject, GGM-hiaat):
  - **Orgel** — rijks- of gemeentelijk monumentaal muziekinstrument met eigen beschermingsstatus en levenscyclus. Roerend erfgoed, apart geïnventariseerd. 6/6 criteria.
- 6 niet-BO begrippen: luidklok (onderdeel monument), ensemble (geen eigen bestaan), kerkgebouw (type monument), herbestemmingsprofiel (instrument), waardestelling (instrument), carillon (specifiek klokkenspel)
- GGM-terugmelding: Orgel ontbreekt als entiteit in beleidsdomein Monumenten
- **Specialisaties-patroon ingevoerd**: `gemma_subtypes` als frontmatter-veld voor BO's met herkende subtypes die geen apart BO zijn. Monument BO verrijkt met 7 subtypes (kerkgebouw, beschermd stadsgezicht, synagoge, klooster, woonhuis, verdedigingswerk, openbare ruimte). Template, CLAUDE.md en exportscript bijgewerkt.
- Index en log bijgewerkt

## [2026-06-20] ingest | Energie en Klimaat — 2 nieuwe BO's (alle GGM-hiaten)
- Bronnen: 4 documenten (Energiebeleid Utrecht omgevingsvisie + 3 VNG-onderwerpenpagina's)
- Bronbestand opgehaald via /fetch: energiebeleid-utrecht.md (omgevingsvisie.utrecht.nl)
- Verplaatst van Sources/energie/ naar Sources/Onderwerpen/Energie en Klimaat/ (juiste projectlocatie)
- 4 bronsamenvattingen aangemaakt in Wiki/Bronsamenvattingen/Energie en Klimaat/
- Nieuw domeinoverzicht aangemaakt: Wiki/Domeinen/energie-en-klimaat.md (12 begrippen, 2 BO's)
- **2 BO's aangemaakt** (beide procesobjecten, geen GGM-grondslag):
  - **Warmtenet** — infrastructuur voor levering van warmte aan gebouwen. Gemeente heeft governance via SOK met Eneco en wettelijke bevoegdheden (Wcw). 6/6 criteria.
  - **Opwekgebied** — aangewezen gebied voor grootschalige opwek duurzame energie (zon/wind). Aanwijzing via beleidsnota Opwekgebieden 2024-2030, verankering in omgevingsplan. 6/6 criteria.
- 10 niet-BO begrippen: warmteprogramma (⚠️ instrument, ter discussie), RES (regionaal), energietransitie (thema), energieloket (kanaal), klimaatpanel (participatie), netcongestie (situatie), energielabel (classificatie), buurtaanpak aardgasvrij (aanpak), warmtebron (te granulair), zonneveld (type van opwekgebied)
- GGM-dekking: taakveld 7 kent alleen beleidsdomein Afval; energie/klimaat ontbreekt volledig. Zelfde patroon als Milieu en Dierenwelzijn.
- GGM-terugmeldingen: #15 (beleidsdomein Energie ontbreekt), #16 (Warmtenet hiaat), #17 (Opwekgebied hiaat)
- CLAUDE.md aangescherpt: anti-patronen toegevoegd bij BO-criteria ("eigendom", "gemeente registreert niet" zijn geen afwijsgronden)
- Feedback-memory versterkt met expliciete anti-patronen
- Index en log bijgewerkt

## [2026-06-20] ingest | Dierenwelzijn — 4 nieuwe BO's (alle GGM-hiaten)
- Bron: Nota Dierenwelzijn (Gemeente Utrecht, december 2019, 26 p., PDF via omgevingsvisie.utrecht.nl)
- Webpaginasamenvatting verplaatst naar Niet-relevant/ (gedekt door de nota)
- 1 bronsamenvatting aangemaakt in Wiki/Bronsamenvattingen/Dierenwelzijn/
- Nieuw domeinoverzicht aangemaakt: Wiki/Domeinen/dierenwelzijn.md (10 begrippen, 4 BO's)
- **4 BO's aangemaakt** (alle procesobjecten, geen GGM-grondslag):
  - **Hulpbehoevend dier** — wild of gehouden dier waarvoor de gemeente wettelijk opvang organiseert (BW 5:8 lid 3)
  - **Kinderboerderij** — openbaar toegankelijke boerderij met educatieve functie, gemeentelijk eigendom (Steedes)
  - **Dierenweide** — locatie met dieren, beperkte openingstijden, particulier initiatief met subsidierelatie (11 stuks)
  - **Visrecht** — recht om te vissen in gemeentelijke wateren, verhuurd via Visserijwet (1963)
- 6 niet-BO begrippen: soortenmanagementplan (⚠️ instrument, ter discussie), Utrechtse soortenlijst (geen meervoud), diervriendelijk bouwen (thema), faunabeheer (proces), plaagdierbestrijding (proces), dierenwelzijnsbeleid (thema)
- GGM-dekking: taakveld 7 kent alleen beleidsdomein Afval; dierenwelzijn ontbreekt volledig. Zelfde patroon als Milieu.
- Index en log bijgewerkt

## [2026-06-20] ingest | Economie — detailhandel — 2 nieuwe BO's
- Bronnen: Ontwikkelingskader Detailhandel 2012 + Detailhandel Utrecht 2015 (Gemeente Utrecht, PDF's via omgevingsvisie.utrecht.nl)
- Webpaginasamenvatting verplaatst naar Niet-relevant/ (te dun voor BO-kandidaten)
- 2 bronsamenvattingen aangemaakt in Wiki/Bronsamenvattingen/Economie/
- **2 BO's aangemaakt:**
  - **Standplaats** (ggm-entiteit) — APV-gereguleerde verkooplocatie in openbare ruimte. GGM-match: Standplaats (Musea, taakveld 5), matchsterkte sterk. Terugmelding: domeinplaatsing Musea is betwistbaar, zou onder Economie moeten.
  - **Warenmarkt** (procesobject) — periodieke georganiseerde verkoop, Marktverordening-gereguleerd. GGM-hiaat.
- 5 niet-BO begrippen: winkelgebied (concept), ambulante handel (categorie), detailhandelsvestiging (te generiek), branchering (instrument), leegstand (status)
- Domeinoverzicht Economie bijgewerkt: 9 → 14 begrippen, 1 → 3 BO's
- GGM-terugmeldingen uitgebreid: #13 (Standplaats scope) en #14 (Warenmarkt hiaat)
- Index en log bijgewerkt

## [2026-06-20] ingest | Beheer Openbare Ruimte — bomenbeleid — 1 nieuw BO
- Bron: Bomenbeleid Utrecht (Gemeente Utrecht, 2009/2018, 42 pagina's PDF)
- Bronbestand opgehaald via /fetch incl. PDF-conversie naar Sources/Onderwerpen/Milieu/
- Overzichtspagina verplaatst naar Niet-relevant/ (redundant met volledig document)
- 1 bronsamenvatting aangemaakt in Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/
- Nieuw domeinoverzicht aangemaakt: Wiki/Domeinen/beheer-openbare-ruimte.md (8 begrippen, 1 BO)
- **1 BO aangemaakt** — exacte GGM-match:
  - **Boom** (ggm-entiteit) — individueel geregistreerd houtachtig gewas, 43 GGM-attributen (IMBOR)
- 7 niet-BO begrippen: monumentale boom (classificatie), bomenstructuur (structuur), bomenparagraaf (instrument), kapvergunning (instrument), herplantplicht (regel), groeiplaats (eigenschap), VTA-inspectie (proces)
- GGM-dekking: beleidsdomein Beheer Openbare Ruimte bevat 200 entiteiten; 1 beoordeeld (Boom=BO), 199 niet beoordeeld (geen beleidsbron voor overige subdomeinen)
- Index en log bijgewerkt

## [2026-06-20] ingest | Milieu — bodem, grondwater en ondergrond — 6 nieuwe BO's (alle GGM-hiaten)
- Bronnen: 3 documenten gemeente Utrecht (beleidspagina + Gebiedsplan grondwaterbeheer 2016 + Nota Bodembeheer 2017-2027)
- Bronbestanden opgehaald via /fetch incl. PDF-conversie naar Sources/Onderwerpen/Milieu/
- 3 bronsamenvattingen aangemaakt in Wiki/Bronsamenvattingen/Milieu/
- Nieuw domeinoverzicht aangemaakt: Wiki/Domeinen/milieu.md (14 begrippen, 6 BO's)
- **6 BO's aangemaakt** — alle GGM-hiaten (geen beleidsdomein Bodem/Milieu in GGM):
  - **Bodemkwaliteitskaart** (governance-object) — wettelijk instrument per Besluit kwaliteit leefomgeving
  - **Bodemverontreiniging** (procesobject) — geregistreerde verontreinigingslocatie
  - **Saneringsplan** (procesobject) — plan voor aanpak verontreiniging
  - **Grondwatermeetpunt** (procesobject) — fysiek meetpunt in monitoringsnetwerk
  - **Grondverzet** (procesobject) — registratie grondverplaatsing, meldingsplicht
  - **Bodemenergiesysteem** (procesobject) — WKO-installatie, vergunningsplichtig
- GGM-dekking: taakveld 7 heeft alleen beleidsdomein Afval (14 entiteiten, niet beoordeeld). Het hele bodem/grondwater/milieu-domein ontbreekt in het GGM — significant structureel hiaat.
- Index en log bijgewerkt

## [2026-06-19] ingest | Erfgoednota Utrecht — 3 nieuwe BO's archeologie + monument verrijkt
- Bron: Erfgoednota 'Utrechts erfgoed verbindt mensen en tijden' (Gemeente Utrecht, oktober 2021)
- Clipping verplaatst naar Sources/Onderwerpen/Cultuur/erfgoednota-utrecht-2021.md
- Bronsamenvatting aangemaakt: Wiki/Bronsamenvattingen/Cultuur/erfgoednota-utrecht.md
- **17 GGM-archeologie-entiteiten volledig beoordeeld** (waren 100% onbeoordeeld):
  - 3 BO's aangemaakt — grondslag: ggm-entiteit
    - **Archeologische vindplaats** (= GGM Vindplaats, matchsterkte sterk) — locatie met archeologische waarde, gemeente is bevoegd gezag
    - **Archeologische vondst** (= GGM Vondst + Artefact geaggregeerd, matchsterkte exact) — overblijfsel beheerd in gemeentelijk depot
    - **Archeologisch onderzoek** (= GGM Project, matchsterkte sterk) — onderzoeksproject door/namens gemeente
  - 14 niet-BO's: Archeologiebesluit (processtap), Artefact (detail Vondst), Artefactsoort (classificatie), Put/Vlak/Spoor/Vulling/boring (opgravingsdetails), Doos/Magazijnlocatie/Magazijnplaatsing/Stelling (depotlogistiek), Kaart/locatie (documentatie)
- Bestaand BO **Monument** verrijkt: erfgoednota als extra bron, verduurzaming als bedrijfsproces
- Begrip "archeologische vindplaats" herbeoordeeld: was niet-BO ("niet primair gemeentelijk") → nu BO (gemeente is bevoegd gezag, heeft eigen beleidskaart)
- 8 nieuwe begrippen toegevoegd aan domeinoverzicht Cultuur (werelderfgoed, beschermd stadsgezicht, cultuurhistorische waardenkaart, archeologische beleidskaart, erfgoedverordening, erfgoed effectrapportage, groen/blauw erfgoed, immaterieel erfgoed)
- GGM-dekking Cultuur verbeterd: 69% onbeoordeeld → 43% onbeoordeeld
- Domein Cultuur status: afgerond → in opbouw (Musea en Generiek Erfgoed nog open)
- Index en log bijgewerkt

## [2026-06-19] ingest | Dienstverlening — 3 BO's + 6 bronsamenvattingen
- Bronnen: 6 VNG-onderwerpenpagina's (hand-out overheidsbrede dienstverlening, startscan, rubriek, online dienstverlening, digitale toegankelijkheid, inkoop-en-aanbesteden) + GGM beleidsdomein Model Dienstverlening (16 entiteiten)
- Directory: Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/
- 3 BO's aangemaakt — grondslag: ggm-entiteit
  - **Aanvraag of melding** (= GGM AanvraagOfMelding, Model Dienstverlening) — startpunt dienstverlening, matchsterkte sterk
  - **Balieafspraak** (= GGM Balieafspraak, Model Dienstverlening) — geplande afspraak klantcontact, matchsterkte exact
  - **Product of dienst** (= GGM ProductOfDienst, Model Dienstverlening) — gemeentelijk aanbod, matchsterkte sterk
- Generalisatiekeuze AanvraagOfMelding: BO op generiek niveau, 11 specialisaties (MOR, WMO/Jeugd, VTH, etc.) horen bij hun eigen domein
- 9 GGM-entiteiten beoordeeld als niet-BO (attributen, statuswaarden, configuratie, classificaties)
- 2 twijfelgevallen gedocumenteerd: Klantbeoordeling (kwaliteitsmetric), Telefoontje (te granulair)
- 6 bronsamenvattingen aangemaakt in Wiki/Bronsamenvattingen/Dienstverlening/
- Domeinoverzicht bijgewerkt: 14 begrippen, 7 BO's, GGM-dekkingsanalyse uitgebreid
- Terugmeldingen: 2 definitieverbeteringen (AanvraagOfMelding en ProductOfDienst hebben systeemreferenties als definitie)
- VNG-bronnen bevestigen werkwijze/organisatiemodel (overheidsbrede dienstverlening, IDO's, professionallijnen) — geen nieuwe data-objecten
- Index en log bijgewerkt

## [2026-06-19] ingest | Cultuur — 3 BO's aangemaakt
- Bronnen: 5 VNG-onderwerpenpagina's (kunst-en-cultuur, propositie-cultuur, architectuur-en-erfgoed, bibliotheekwerk, toelichting-ringenmodel)
- Directory: Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/ en musea/
- 3 BO's aangemaakt — grondslag: ggm-entiteit (alle exact match)
  - **Monument** (= GGM Beschermde Status, beleidsdomein Monumenten) — beschermd onroerend erfgoed
  - **Archiefstuk** (beleidsdomein Archief) — gearchiveerde informatie, gemeentearchief
  - **Museumobject** (beleidsdomein Musea) — object met cultuurhistorische waarde in museale collectie
- 5 bronsamenvattingen aangemaakt in Wiki/Bronsamenvattingen/Cultuur/
- Domeinoverzicht aangemaakt met status: afgerond (18 begrippen, 3 BO's)
- GGM-dekkingsanalyse: Erfgoed (44 ent.) en Musea (32 ent.) goed gedekt; cultuurbeleid structureel buiten GGM (governance)
- Geen terugmeldingen richting GGM
- Index en log bijgewerkt

## [2026-06-19] reconsider | Bestuur — GGM-hiaten hergeclassificeerd
- Feedback: GGM-scope is dataobjecten (wat gemeenten registreren), niet processen (hoe werk verloopt)
- **Herclassificatie:**
  - **Verkiezing** en **Referendum**: Processen, niet dataobjecten → **geen terugmelding** naar GGM (structureel uit scope)
  - **Stembureau**: Registratieobject (fysieke locaties met capaciteit) → **wel terugmelding** (dataobject, pakt in GGM-scope)
  - **Gemeenschappelijke Regeling**: Juridische entiteit met registreerbare eigenschappen → **wel terugmelding** (dataobject, pakt in GGM-scope)
- BO-pagina's bijgewerkt met uitleg waarom sommige processen zijn (en dus niet in GGM-scope)
- [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]] bijgewerkt: 4 items → 2 items (alleen Stembureau en GR als potentiële hiaten)

## [2026-06-19] ingest | Bestuur — 4 BO's aangemaakt
- Bronnen: 9 VNG-onderwerpenpagina's (rubriek + 8 onderwerpen)
- Directory: Wiki/Bedrijfsobjecten/0-bestuur-politiek-en-ondersteuning/politiek/
- 4 BO's aangemaakt — grondslag: procesobject/governance-object (geen GGM-grondslag)
  - **Verkiezing** (procesobject) — periodieke vervangingskeuze ambtsdragers; 6/6 criteria
  - **Referendum** (procesobject) — volksstemming; 6/6 criteria
  - **Stembureau** (procesobject, maar dataobject-karakter) — fysieke locatie stemming; 6/6 criteria
  - **Gemeenschappelijke Regeling** (governance-object, maar dataobject-karakter) — Wgr-samenwerkingsconstructie; 6/6 criteria
- 9 bronsamenvattingen aangemaakt in Wiki/Bronsamenvattingen/Bestuur/
- Domeinoverzicht aangemaakt met status: afgerond (na herclassificatie)
- Index en log bijgewerkt

## [2026-06-19] lint & fixes | Wiki lint-issues opgelost
- **Wees-BO's:** domeinoverzicht Terug-en-invordering aangemaakt voor 7 BO's (aflossing, aflossingsplan, afschrijving, interventie, kwijtschelding, restitutie, vordering)
- **Herleidbaarheid:** MAP.md voorzien van bronnen-veld (Asiel en Integratie/vng-inburgering)
- **Enum-validatie:** bestuursovereenkomst.md archimate_type gecorrigeerd (contract → business-object)
- Index bijgewerkt met Terug-en-invordering domeinoverzicht

## [2026-06-19] bedrijfsobjecten | Asiel en Integratie — 15 BO's aangemaakt
- Directory: Wiki/Bedrijfsobjecten/Asiel-en-Integratie/
- 13 BO's met grondslag ggm-entiteit (GGM beleidsdomein Inburgering, taakveld 6): Asielstatushouder, Gezinsmigrant, Brede Intake, PIP, Inburgeringstraject, Leerroute, Inburgeringsplicht, Examen, Inburgeringsaanbod, Inburgeringstermijn, MAP, PVT, Voorbereiding op Inburgering
- 1 procesobject zonder GGM: Opvanglocatie (asielopvang structureel niet gemodelleerd in GGM)
- 1 governance-object zonder GGM: Bestuursovereenkomst (contract, overeenkomst gemeente-COA)
- Alle 13 GGM-matches: matchsterkte exact
- GGM-entiteiten geaggregeerd in BO's: B1-route en Z-route → classificatie van Leerroute; Examenonderdeel → detail van Examen; Ontheffing en Vrijstelling → status van Inburgeringsplicht; Aanvraag verlenging → processtap van Inburgeringstermijn
- Index bijgewerkt met sectie Asiel en Integratie

## [2026-06-19] ingest | Arbeidszaken — CvA-bronnen toegevoegd
- Bronnen: College voor Arbeidszaken.md, cva-beleidsplan_2023-2026.md (verplaatst uit opgeheven folder Bedrijfsvoering)
- 2 bronsamenvattingen aangemaakt in Wiki/Bronsamenvattingen/Arbeidszaken/
- Conclusie ongewijzigd: 0 BO's, bronnen bevestigen governance/instrument-karakter domein
- Domeinoverzicht bijgewerkt: bronnen_count 9 → 11

## [2026-06-19] ingest | Arbeidszaken — domein afgerond (0 BO's)
- Bronnen: 9 VNG-onderwerpenpagina's (rubriek + 8 onderwerpen)
- Conclusie: geen BO's — domein betreft gemeente als werkgever, structureel buiten GGM-scope
- Alle bronnen zijn instrumenten (cao, gedragscode, rechtspositieregeling) en thema's (arbeidsmarktkrapte, integriteitsbeleid)
- Geen begrippenpagina's aangemaakt (geen BO-kandidaten)
- Domeinoverzicht aangemaakt met status: afgerond

## [2026-06-18] ingest | RGBZ 1.0 en ZTC2 v2.1 — domein Dienstverlening
- Bronnen: RGBZ 1.0 (KING, 2010), GEMMA ZTC2 Informatiemodel v2.1 (KING, 2014)
- Clippings verplaatst van Clippings/ naar Sources/Standaarden/
- Begrippen geëxtraheerd (5): zaakgericht werken (thema/operationeel), zaaktypecatalogus (object/operationeel), informatieobject (object/operationeel), zaakdossier (object/operationeel), resultaattype (object/operationeel)
- Pagina's aangemaakt: 5 begrippen, 2 bronsamenvattingen, 1 domeinoverzicht (Dienstverlening)
- Pagina's bijgewerkt: ggm-dekkingspatroon (Dienstverlening-sectie toegevoegd), gemma-bedrijfsobjecten-en-ggm (kruisverwijzingen)
- GGM-relatie: taakveld 10 Dienstverlening bestaat, nog geen GGM-bronbestand; taakveld 99 Kern/RGBZPlus dekt runtime (25 entiteiten) maar niet ZTC2-configuratielaag
- Structureel hiaat: CATALOGUS, RESULTAATTYPE, EIGENSCHAP, ROLTYPE, ZAAKOBJECTTYPE ontbreken in GGM

## [2026-06-18] ingest | Introductie RGBZ (vng-realisatie.github.io)
- Bron: Introductie RGBZ (VNG Realisatie), verplaatst naar Sources/Standaarden/introductie-rgbz.md
- Samengevoegd met bestaande RGBZ-bronsamenvatting
- Meerwaarde: RGBZ 2.0 (concept, nooit vastgesteld) → ZGW API's (officieel); berichtenarchitectuur (StUF-ZKN, Zaak- en Documentservices, ZGW API's)
- Pagina's bijgewerkt: rgbz-informatiemodel (sectie Status en evolutie + Berichtenarchitectuur), zaakgericht-werken (berichtenstandaarden), dienstverlening (evolutie-sectie + openstaande vraag actualiteit RGBZPlus)

## [2026-06-18] ingest | 3 Raadgever-bronnen belastingendomein
- Bronnen: raadgever-gemeentelijke-belastingen, raadgever-kostenonderbouwing-lokale-heffingen, raadgever-woz
- Clippings verplaatst van Clippings/ naar Sources/Onderwerpen/Belastingen/
- Raadgever Riool- en waterzorgheffing overgeslagen: duplicaat van bestaand bronbestand
- Begrippen geëxtraheerd (6): woz-waarde, woz-beschikking, onroerende-zaak, waarderingskamer, kruissubsidiering, kostenonderbouwing
- Bestaande begrippen bijgewerkt met nieuwe bronverwijzing: belastingmix, kostendekkend-tarief, kwijtschelding
- Pagina's aangemaakt: 6 begrippen, 3 bronsamenvattingen
- Pagina's bijgewerkt: domeinoverzicht belastingen, index

## [2026-06-18] ingest | 4 Raadgever-bronnen financiëndomein (NIEUW)
- Bronnen: raadgever-inkomstenbronnen-gemeenten, raadgever-gemeentebegroting-en-jaarrekening, raadgever-financiele-verordening, raadgever-financiele-conditie-gemeente
- Clippings verplaatst van Clippings/ naar Sources/Onderwerpen/Financien/ (nieuwe map)
- Begrippen geëxtraheerd (10): gemeentefonds, algemene uitkering, specifieke uitkering, begrotingscyclus, budgetrecht, financiele verordening, kadernota, solvabiliteitsratio, netto schuldquote, onbenutte belastingcapaciteit
- Pagina's aangemaakt: 10 begrippen, 4 bronsamenvattingen, 1 domeinoverzicht (Financien)
- Koppeling met bestaande bedrijfsobjecten: Begroting, Taakveld, Doelstelling, Product, Kostenplaats, Activa
- Stub domeinoverzicht gemeentelijke-belasting.md verwijderd (duplicaat van belastingen.md)

## [2026-06-18] ingest | 1 Raadgever-bron bedrijfsvoering (NIEUW)
- Bron: raadgever-inkoop-en-aanbesteden
- Clipping verplaatst van Clippings/ naar Sources/Onderwerpen/Bedrijfsvoering/ (nieuwe map)
- Begrippen geëxtraheerd (3): gemeentelijke inkoop, aanbesteding, mvoi
- Pagina's aangemaakt: 3 begrippen, 1 bronsamenvatting, 1 domeinoverzicht (Bedrijfsvoering)
- Koppeling met bestaande bedrijfsobjecten: Inkooporder, Factuur, Werkorder

## [2026-06-18] bronnen | RSGB en VNG Informatiemodellen
- Sources/Standaarden gelezen: RSGB 2.02 Deel I, Wat is een Informatiemodel
- Bronsamenvatting aangemaakt: Wiki/Bronsamenvattingen/Standaarden/rsgb-en-informatiemodellen.md
- Analyse ggm-oorsprong-en-meerwaarde.md gecorrigeerd: GGM niet alleen uit databases maar uit drie lagen bronnen (informatiemodellen basisregistraties, RSGB als integratiemodel, domeinmodellen uit bestaande systemen)
- RSGB beschrijft wat de gemeente met basisregistraties uitwisselt; gemeente registreert intern meer in de bronregistraties

## [2026-06-18] bronnen | GEMMA-referentiearchitectuur
- 8 pagina's geraadpleegd op gemmaonline.nl: Bedrijfsobjecten, GEMMA en het GGM, Procesarchitectuur kennismodel, Bedrijfsfuncties, Bedrijfsarchitectuur, Visie op zaakgericht werken, Procesarchitectuur relatie met zaakgericht werken, Samenhang PDC/UPL/ZTC/verwerkingsregister
- Geconsolideerd bronbestand aangemaakt: Sources/GEMMA/gemma-bedrijfsobjecten-en-ggm.md
- Bronsamenvatting aangemaakt: Wiki/Bronsamenvattingen/GEMMA/gemma-bedrijfsobjecten-en-ggm.md
- Kernbevindingen: (1) GEMMA leidt 507 bedrijfsobjecten af uit GGM-dataobjecten, (2) zaak is al een procesobject in GEMMA maar niet gegeneraliseerd naar het bedrijfsobjectenmodel, (3) GEMMA noemt zelf uitbreiding bedrijfsarchitectuur als verbetervoorstel
- Analyse ggm-oorsprong-en-meerwaarde.md uitgebreid met sectie over zaakgericht werken als bestaand verbindingsmechanisme
- Geen begrippen geëxtraheerd — deze bronnen zijn architectuurkader, geen beleidsdocumenten

## [2026-06-18] analyse | Van data-inventarisatie naar bedrijfsarchitectuur
- Nieuwe analyse: GGM-oorsprong (bottom-up MI), oprekking naar transactioneel, consequenties voor GEMMA
- GEMMA-bronnen geraadpleegd: Bedrijfsobjecten, Procesarchitectuur kennismodel, Bedrijfsfuncties, GEMMA en het GGM
- Kernbevinding: GEMMA leidt bedrijfsobjecten af uit GGM → bottom-up beperking werkt door in referentiearchitectuur
- GEMMA heeft 507 bedrijfsobjecten, alle GGM-afgeleid — procesobjecten en governance-objecten ontbreken structureel
- Meerwaarde: aanvulling met procesobjecten/governance-objecten maakt GEMMA-procesarchitectuur concreter en transactioneel toepasbaar
- Opbouwend geformuleerd: bevestigt waarde GGM, toont complementaire aanvulling

## [2026-06-18] conventie | Begripstype voorspelt GGM-match + BO-grondslag
- CLAUDE.md aangepast: begripstype is primaire voorspeller voor GGM-match, niet abstractieniveau
- Tabel toegevoegd: begripstype → verwachte GGM-match (object=vaak, instrument/actor/thema=zelden/nooit)
- Bedrijfsobject-frontmatter uitgebreid met `grondslag` veld: ggm-entiteit, ggm-afgeleid, procesobject, governance-object
- Afleidingsregels aangepast: eerst grondslag bepalen, dan pas afleiden
- Alle 19 bestaande BO's bijgewerkt met `grondslag: ggm-entiteit`
- Aanleiding: structureel patroon uit [[Wiki/Analyses/ggm-dekkingspatroon|ggm-dekkingspatroon]] — GGM dekt data, niet processen/governance

## [2026-06-18] analyse | GGM-dekkingspatroon
- Nieuwe analyse: structureel patroon over vier domeinen (Belastingen, Financiën, Economie, Bedrijfsvoering)
- Kernbevinding: GGM dekt data-objecten (basisregistraties, boekhoudkundig) maar niet processen, governance of beleidsinstrumenten
- Grens loopt niet tussen abstractieniveaus maar tussen data (staat van systemen) en dynamiek (gedrag van de organisatie)
- Consequentie: bedrijfsarchitectuur moet procesmodellen, governance en actoren zelf opbouwen uit beleidsbronnen
- Verwachting: patroon zal zich herhalen bij nieuwe domeinen (Schuldhulpverlening, Cultuur, Dienstverlening)

## [2026-06-18] bedrijfsobjecten | WOZ-object en WOZ-waarde
- 2 bedrijfsobjecten aangemaakt in Wiki/Bedrijfsobjecten/Belastingen/
- WOZ-object: 1:1 match met GGM WOZ-object (RSGBPlus, taakveld 99 Kern)
- WOZ-waarde: 1:1 match met GGM WOZ-Waarde (RSGBPlus); omvat beschikkingsaspect (statusBeschikking)
- WOZ-beschikking niet als apart BO: in GGM attribuut van WOZ-Waarde, op bedrijfsniveau niet onderscheidbaar
- Begrippen woz-waarde en onroerende-zaak bijgewerkt met GGM-referenties

## [2026-06-18] analyse | GGM-hiaten uitgebreid met Financiën-domein
- Hiatenanalyse uitgebreid met 10 Financiën-begrippen zonder GGM-match
- Structureel patroon geïdentificeerd: GGM dekt objecten (boekhoudkundig, basisregistratie) maar niet processen (begrotingscyclus, heffingsproces) of governance (verordeningen, budgetrecht)
- Kengetallen (solvabiliteit, schuldquote, belastingcapaciteit) zijn afleidbaar uit bestaande GGM-objecten, niet als entiteiten nodig
- WOZ-bedrijfsobjecten bevestigen: basisregistratie-kant goed gedekt, heffingsketen ontbreekt

## [2026-06-18] batch-verwerking | 10 clippings (8 verwerkt, 2 overgeslagen)
- Verwerkt: 3 Belastingen, 4 Financiën, 1 Bedrijfsvoering
- Overgeslagen: Raadgever Riool- en waterzorgheffing (duplicaat), Over de adviescommissies en colleges (buiten gemeentelijk perspectief)
- Totaal aangemaakt: 19 begrippen, 8 bronsamenvattingen, 2 domeinoverzichten
- Twee nieuwe domeinen: Financiën, Bedrijfsvoering

## [2026-06-17] setup | GGM als bronmateriaal geladen
- Bron: Sources/Gemeentelijk Gegevensmodel XMI2.1.xml
- GGM-bronpagina's aangemaakt in Sources/GGM/: structuur-ggm, financien (24 entiteiten), terug-en-invordering (29), sport-cultuur-en-recreatie (83), schulden (33)
- Alle definities letterlijk uit het GGM v2.5.1 XMI-bestand, geen synthese
- GGM-pagina's zijn bronmateriaal (Sources), geen wiki-pagina's

## [2026-06-17] analyse | GGM-hiaten belastingendomein
- Overzicht aangemaakt van ontbrekende concepten in het GGM voor het belastingendomein
- 6 begrippen zonder GGM-entiteit, 6 kandidaat-entiteiten geïdentificeerd
- Structureel hiaat beschreven: heffingsproces valt tussen RSGB, Financien en Terug- en invordering
- Status: in opbouw, wordt aangevuld bij verwerking volgende bronnen

## [2026-06-17] ingest | Belastingtypen
- Bron: Sources/Onderwerpen/Belastingen/Belastingtypen.md
- Begrippen geëxtraheerd: gemeentelijke belasting, algemene belasting, bestemmingsbelasting, retributie, leges, algemene middelen
- Pagina's aangemaakt: 6 begrippen, 1 bronsamenvatting, 1 domeinoverzicht
- Hiaat gesignaleerd: GGM kent geen belastingtypologie als entiteiten of enumeratie

## [2026-06-17] bedrijfsobjecten | eerste set uit GGM
- 17 bedrijfsobjecten aangemaakt, afgeleid van GGM-entiteiten
- Financien (10): Begroting, Taakveld, Doelstelling, Product, Kostenplaats, Factuur, Inkooporder, Debiteur, Activa, Werkorder
- Terug-en-invordering (7): Vordering, Aflossingsplan, Aflossing, Kwijtschelding, Afschrijving, Restitutie, Interventie
- Debiteur combineert twee GGM-definities (Financien + T&I) in één bedrijfsobject
- Kwijtschelding noteert contextverschil: GGM = sociaal domein, belastingdomein = Invorderingswet
- 36 GGM-entiteiten uitgesloten: te granulair (Begrotingregel, Vorderingscomponent, etc.), te technisch (Batch, Batchregel), of specialisaties (Boetevordering, Rentevordering, etc.)
- Format per bedrijfsobject: naam, definitie (= GGM, afwijkend indien nodig), beleidsdomein, bedrijfsprocessen, bedrijfsfuncties

## [2026-06-17] ingest | 7 bronnen belastingendomein
- Bronnen: Belastinggebied, Belastingpolitiek, Belastingverordening, Bevoegdhedenverdeling, Invordering en kwijtschelding, Kostendekkende tarieven, Wettelijke grenzen
- Begrippen geëxtraheerd: belastinggebied, belastingverordening, belastingplichtige, heffingsambtenaar, invorderingsambtenaar, belastingmix, belastingaanslag, heffingsmaatstaf, kostendekkend tarief, kwijtschelding, woonlasten
- Pagina's aangemaakt: 11 begrippen, 7 bronsamenvattingen
- Pagina's bijgewerkt: gemeentelijke-belasting, bestemmingsbelasting, retributie, domeinoverzicht belastingen
- GGM-hiatenanalyse uitgebreid: 17 begrippen zonder (volledige) GGM-entiteit, procesmodel gereconstrueerd, overlap met Terug-en-invordering geanalyseerd
- Enige GGM-match: kwijtschelding → GGM "Kwijtschelding" (Terug-en-invordering), maar in context sociaal domein

## [2026-06-17] analyse | VNG-rubrieken mapping op GGM
- Alle 26 VNG-rubrieken (vng.nl/rubrieken) opgehaald met beschrijvingen en onderwerpen
- Mapping aangemaakt naar GGM-taakvelden (0-10, 99) en beleidsdomeinen
- Dekking: 14 rubrieken goed gedekt, 7 deels gedekt, 4 met hiaat, 1 zonder dekking
- Belangrijkste hiaten: Belastingen, Energietransitie, Openbare gezondheid, Recht, Risicobeheer
- Europa en internationaal valt geheel buiten GGM-scope
- Observatie: sociaal domein het breedst vertegenwoordigd (5 rubrieken → 13 beleidsdomeinen); taakveld 7 het smalst (alleen Afval)

## [2026-06-17] setup | GGM taakveld 3 Economie als bronmateriaal
- GGM-bronpagina aangemaakt: Sources/GGM/economie.md
- 6 entiteiten zonder definities: Contact, Hotel, Hotelbezoek, Verkooppunt, Werkgelegenheid, Winkelvloeroppervlak
- Observatie: zeer smal model, gericht op hotel/retail-statistieken rond Vestiging (RSGB)
- Groot hiaat t.o.v. breedte taakveld-definitie ("economische ontwikkeling, bedrijvigheid en innovatie")

## [2026-06-17] conventie | Begripstypen en abstractieniveaus
- CLAUDE.md uitgebreid met twee nieuwe dimensies voor begrippen: begripstype en abstractieniveau
- Begripstypen: waarde, doel, thema, instrument, actor, doelgroep, object
- Abstractieniveaus: normatief, strategisch, tactisch, operationeel
- Aanleiding: VNG-beleidsdocumenten spreken fundamenteel andere taal dan GGM — onderscheid moet structureel zichtbaar zijn
- Frontmatter begrippenpagina's uitgebreid met velden begripstype en abstractieniveau

## [2026-06-17] ingest | Economie speerpunten VNG
- Bron: Sources/Onderwerpen/Economie/Economie speerpunten VNG.md
- Begrippen geëxtraheerd (9): brede welvaart (waarde/normatief), vestigingsklimaat (doel/strategisch), ondernemersdienstverlening (thema/tactisch), regeldruk (thema/tactisch), economische ruimte (thema/tactisch), arbeidsmarkt (thema/strategisch), human capital (thema/strategisch), midden- en kleinbedrijf (doelgroep/tactisch), werklocatie (object/operationeel)
- Pagina's aangemaakt: 9 begrippen, 1 bronsamenvatting, 1 domeinoverzicht
- GGM-matching: 0 directe matches, 3 gedeeltelijke (Werkgelegenheid, Winkelvloeroppervlak, Vestiging RSGB)
- Groot hiaat: GGM taakveld 3 dekt slechts statistisch fragment van het beleidsveld

## [2026-06-17] revisie | GGM-hiaten belastingendomein
- Hiatenanalyse herzien met begripstype/abstractieniveau-indeling
- Begrippen gegroepeerd per niveau: 1 strategisch, 9 tactisch, 7 operationeel
- Kernpunt: operationeel hiaat (heffingsproces) is het eigenlijke probleem; dat strategische begrippen geen GGM-match hebben is logisch
- Kandidaat-entiteiten getypeerd naar begripstype (object, doelgroep, actor)
- Onderscheid aangebracht tussen GGM-kandidaten (operationeel) en architectuurkader (tactisch)

## [2026-06-17] ingest | Inburgering en Asielopvang — 2 bronnen
- Bronnen: Asielopvangwijzer (COA portaal), COA Dienstverleningsgids (januari 2026)
- Begrippen geëxtraheerd (11): asielopvang, opvanglocatie, spreidingswet, duurzame gemeentelijke opvang, bestuursovereenkomst, statushouder, alleenstaande minderjarige vreemdeling, inburgering, voorinburgering, meedoenbalie, kansrijke koppeling, inhuisregistratie
- Pagina's aangemaakt: 11 begrippen, 2 bronsamenvattingen, 1 domeinoverzicht
- Scope: gemeentelijk perspectief — wat de gemeente ziet en doet in de asielketen
- COA/IND/DT&V/AVIM benoemd als ketenpartners, niet als eigen begrip uitgewerkt
- GGM-referentie: beleidsdomein Inburgering (35 entiteiten, taakveld 6) beschikbaar maar nog niet gemapped
- GGM-hiaat: asielopvangfase is niet gemodelleerd in het GGM
- Handreiking effectrapportage bij nieuwe bedrijvigheid verplaatst van Sources/Inburgering naar Sources/Economie (betreft arbeidsmigranten, niet inburgering)
- Conventie toegevoegd aan CLAUDE.md: gemeentelijk perspectief als scope voor alle compilaties
