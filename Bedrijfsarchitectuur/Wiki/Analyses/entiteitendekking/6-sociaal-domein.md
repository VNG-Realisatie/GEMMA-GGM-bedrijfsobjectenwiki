---
type: analyse
titel: "Entiteitendekking: 6 Sociaal Domein"
datum: 2026-07-07
taakveld: "6 Sociaal Domein"
beleidsdomeinen:
  - Dak- en thuislozen
  - Gemeentebegrafenissen
  - Generiek Jeugd en Wmo
  - Inburgering
  - Inkomen
  - Jeugdbescherming en reclassering
  - Schulden
  - Sociaal Domein Generiek
  - Sociale Teams
  - Werk
totaal_entiteiten: 285
totaal_bo: 59
totaal_matches: 49
totaal_hiaten: 10
---

# Entiteitendekking: 6 Sociaal Domein

## Beoordeling

10 beleidsdomeinen, 285 GGM-entiteiten. Dekking: 246 van 285 (86%) — 49 met BO, 197 ondersteunend, 39 niet gedekt. 10 BO's zonder GGM-entiteit.

*Bijgewerkt 2026-07-07 (ronde 1): herbeoordeling Inkomen/Sociaal Domein Generiek — Bankrekening, Hypotheek, Motorvoertuig en Onroerend goed consistent gerouteerd via Vermogenscomponent → Profiel → Client (2 hiaten opgeheven: Hypotheek en Onroerend goed hadden nog geen route; Bankrekening en Motorvoertuig hadden al een — onjuiste — route, dus geen tellingimpact voor die twee).*

*Bijgewerkt 2026-07-07 (ronde 2): ingest van Boek 1 BW Titel 17 (Levensonderhoud) en Wet studiefinanciering 2000, plus verificatie tegen de GGM-Generalization-relaties in `ggm_parsed.json`. Dit legde een grotere inconsistentie bloot dan verwacht: de hele `Inkomstencomponent`-tak (Primair + Secundair inkomstencomponent en hun subtypen) miste de dekkingsroute die `Vermogenscomponent` al wel had, en twee Primair-subtypen (`Ander inkomen`, `Hobby`) en de complete Secundair-familie (`Dertiende maand`, `Heffingskorting`, `Inkomstenvermindering`, `Vergoeding`, `Vakantiegeld`) waren nooit aan hun bovenliggend type gekoppeld. Ook `Onderhoudsplicht`/`Onderhoudsverhouding` bleken via de GGM-documentatie zelf al een route te hebben ("opgenomen in het profiel van de klant"), analoog aan Inkomstenverhouding. In totaal 17 hiaten opgeheven in Sociaal Domein Generiek. Zie herziene paragrafen hieronder.*

Niet-BO entiteiten: 24× classificatie, 16× component, 189× detail, 3× abstract, 2× proces, 2× rol.

**Generiek Jeugd en Wmo.** De niet-BO entiteiten volgen grotendeels het AOM-patroon (AanvraagOfMelding) dat ook in andere taakvelden voorkomt: `AOMMeldingWmoJeugd` en `AOM_AanvraagWmoJeugd` zijn concrete subtypen van het abstracte `AanvraagOfMelding` en beschrijven de [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding|Aanvraag of melding]]-BO, net als de vergelijkbare AOM-entiteiten in Veiligheid en Vergunningen. `Verzoek om Toewijzing` is een inkomend verzoekbericht via het H10-portal dat leidt tot een Beschikking — geen zelfstandig BO. Voor het overige overheerst detailgegeven rond Beschikking en Voorziening (Beperking, Score, Tarief, Team e.d.), met enkele classificaties (Beperkingscoresoort, Beschikkingsoort, Scoresoort) en één component (Declaratieregel).

**Inburgering.** Vrijwel alle niet-BO entiteiten zijn detailgegevens die een van de 15 BO's beschrijven (Asielstatushouder, Leerroute, Inburgeringstermijn e.d.), zonder classificatie- of componentpatroon van betekenis. Twee entiteiten verdienen aandacht vanwege naamhomoniemen: `Werk` (11 attrs, werkgegeven binnen het inburgeringstraject) is een andere entiteit dan de gelijknamige BO `Werkzoekende` en het beleidsdomein "Werk"; `Taalvaardigheid` (14 attrs) is een toetsgegeven van Asielstatushouder. Ook `Ontheffing` (Inburgering, wél BO) heeft een naamgenoot in het beleidsdomein Werk (zie hieronder) — de Naamoverlap-kolom bij Inburgering verwijst daar al naar.

**Inkomen.** Dit is het beleidsdomein met de meeste "niet gedekt"-gevallen (12 van de 20 ⚠️-markeringen in dit taakveld) en het grootste aantal review-items. Structureel patroon: veel entiteiten zijn subtypen van de abstracte classificatie `Reden aanvraag` / `Reden aanvraag Levensonderhoud` (Gestopt betaald werk, Gestopt of verkocht eigen bedrijf, Gestopte detentie, Gestopte of verlaagde alimentatie, Gestopte uitkering, Vertrek uit asielzoekerscentrum). Hoewel de bovenliggende `Reden aanvraag` terecht als classificatie is getypeerd, blijven deze concrete subtypen zelf op `detail` staan: ze dragen elk 5-14 inhoudelijke bewijsattributen (contractgegevens, KvK-nummer, verkoopbedrag, COA-weekgeld) en zijn dus geen eenvoudige codetabel maar situationele bewijsregistraties. Twee entiteiten zijn wél omgezet naar `classificatie`: `Diensttype` en `Leveringscomponenttype` typeren respectievelijk Dienst en Leveringscomponent (naampatroon -type, functie als normtabel); `Periodiek dienst Bijz. bijstand` is door het GGM zelf als redundant met deze twee gemarkeerd en krijgt hetzelfde type. `Component` is omgezet naar `component`: het is letterlijk een bouwsteen ("is opgebouwd uit") van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening|Inkomensvoorziening]]. **Herbeoordeling 2026-07-07 — concept-duplicatie, geen naamoverlap:** `Component` (12 attrs: *"een afzonderlijk onderdeel of bron van inkomen, zoals loon, winst uit onderneming, uitkering…"*) is inhoudelijk hetzelfde begrip als `Inkomstencomponent` in Sociaal Domein Generiek (9 attrs: *"een persoon kan vanuit diverse bronnen inkomsten krijgen: alimentatie, loon, uitkering of vermogen…"*) en als `Inkomen` in Schulden (6 attrs, component van Leefsituatie in een WSNP-traject). Alle drie beschrijven "de afzonderlijke bronnen waaruit iemands inkomen bestaat" — niet drie verschillende begrippen die toevallig dezelfde naam delen, maar hetzelfde onderliggende concept dat het GGM drie keer los modelleert voor drie uitvoeringscontexten: generiek cliëntprofiel (Sociaal Domein Generiek), berekening van één toegekende Inkomensvoorziening (hier), en de Leefsituatie-berekening binnen een WSNP-traject (Schulden). `Component` blijft via Inkomensvoorziening gedekt, maar wordt nu ook expliciet cross-gelinkt naar Inkomstencomponent als het gedeelde bovenliggende begrip (zie tabel). Dit is een kandidaat voor een toekomstige `/assess-bo`-afweging van een generiek "Inkomstenbron"-begrip, zodra er een bron voor bestaat (zie "Ontbrekende bronnen" hieronder) — vooralsnog blijft het bij drie los gedekte, maar wel gekoppelde, entiteiten.

Ook de `Reden aanvraag Levensonderhoud`-subtypes zelf zijn niet geïsoleerd: `Gestopt betaald werk`, `Gestopt of verkocht eigen bedrijf`, `Gestopte of verlaagde alimentatie`, `Gestopte uitkering` en `Vertrek uit asielzoekerscentrum` zijn inhoudelijk de **beëindiging** van precies de inkomstenbronnen die Sociaal Domein Generiek als `Primair inkomstencomponent`-subtypes modelleert (Betaald werk, Eigen bedrijf, Alimentatie, Uitkering) — twee kanten van dezelfde medaille: een lopend profielonderdeel versus de gebeurtenis die het stopzetten ervan markeert en een aanvraag triggert. Ook dit is nu expliciet cross-gelinkt in de tabel in plaats van als losstaand hiaat behandeld.

Functionele dekking: de "niet gedekt"-rijen laten zien dat het GGM veel meer situationele nuance rond inkomensbeëindiging en -wijziging vastlegt (Boete, Verbroken relatie, Wachten DigiD, Opname instelling) dan er BO's voor bestaan — dit hangt samen met [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening|Inkomensvoorziening]] en de terug-/invorderingsketen maar wordt niet apart gemodelleerd als BO. Voor Boete bestaat overigens wel een (zwakke) bron: Wet SUWI art. 83d-83h regelt de bestuurlijke boete, maar dan in UWV-context, niet gemeente/Participatiewet-specifiek — zie "Ontbrekende bronnen".

**Schulden.** Bijna alle niet-BO entiteiten zijn detailgegevens of procesfasen (Aanmelding, Crisisinterventie, Intake, Nazorg, Stabilisatie, Uitstroom) van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuldhulptraject|Schuldhulptraject]]. Eén herclassificatie: `Inkomen` (6 attrs, met attributen inkomstenbron/inkomenscategorie) is een component van Leefsituatie binnen WSNP-traject — nadrukkelijk niet te verwarren met het gelijknamige beleidsdomein Inkomen of de aparte `Inkomen`/`Inkomstencomponent`-structuur in Sociaal Domein Generiek; drie homoniemen "Inkomen" komen zo in dit taakveld voor.

**Sociaal Domein Generiek.** Dit beleidsdomein heeft de meeste "niet gedekt"-gevallen naast Inkomen. Kernpatroon: `Inkomstencomponent` en `Vermogenscomponent` zijn beide herclassificeerd naar `abstract` — het zijn overkoepelende typen met eigen subtype-hiërarchie (Inkomstencomponent → Primair/Secundair inkomstencomponent; Vermogenscomponent → Bankrekening/Hypotheek/Motorvoertuig/Onroerend goed). De concrete inkomstenbron-varianten `Alimentatie`, `Betaald werk`, `Eigen bedrijf`, `Pensioen`, `Stage` en `Uitkering` zijn alle subtypen van "Primair inkomstencomponent" en zijn consistent herclassificeerd naar `component`: elk is een bouwsteen van het totale inkomen van een persoon, met bronspecifieke attributen. De overige review-items (Incident, Onderhoudsplicht, Sociale Groep, Vrijlating inkomsten, Waardepeiling) blijven `detail`: het zijn inhoudelijke registraties (gebeurtenis, wettelijke verplichting, groep, kortingsregel, taxatie) zonder eigen BO-worthy levenscyclus.

**Herbeoordeling 2026-07-07 — Vermogenscomponent-routering gecorrigeerd.** De vier subtypen van `Vermogenscomponent` (Bankrekening, Hypotheek, Motorvoertuig, Onroerend goed) stonden inconsistent gedekt: Bankrekening verwees ten onrechte naar Aflossing, Motorvoertuig naar de Voertuig-BO (taakveld 2), en Hypotheek/Onroerend goed hadden helemaal geen route. De juiste vraag is niet "bestaat er elders in GEMMA al een registratie van dit voertuig/pand" (dat beantwoordt een andere bedrijfsfunctie — kentekenregistratie/parkeren resp. OZB-heffing, geverifieerd o.a. tegen [[Wiki/Bedrijfsobjecten/99-kern/woz-object|WOZ-object]], dat geen relatie met Client heeft), maar of de cliënt vermogen heeft *in de vorm van* dit item. Alle vier zijn nu consistent gedekt via Vermogenscomponent → Profiel → Client, net als de abstracte Vermogenscomponent zelf. Dit heft 2 hiaten op (Hypotheek, Onroerend goed hadden nog geen route); Bankrekening en Motorvoertuig kregen alleen een correctere route (waren al niet als hiaat geteld).

Dezelfde concept-duplicatie als hierboven bij Inkomen beschreven geldt hier vanuit de andere kant: `Inkomstencomponent` is hetzelfde begrip als Inkomen's `Component` en Schulden' `Inkomen` (zie aldaar voor de onderbouwing met citaten) — drie keer los gemodelleerd, nu expliciet cross-gelinkt in de tabel. En de `Primair inkomstencomponent`-subtypes Alimentatie/Betaald werk/Eigen bedrijf/Uitkering zijn het lopende-profiel-tegenhanger van Inkomen's `Reden aanvraag Levensonderhoud`-subtypes (de beëindiging van dezelfde bron) — ook cross-gelinkt.

**Herbeoordeling 2026-07-07 (ronde 2) — Inkomstencomponent-tak volledig gerouteerd, plus twee ingesten.** Bij het verwerken van Studiefinanciering en Onderhoudsplicht (zie hieronder) is de volledige `Inkomstencomponent`-tak gecontroleerd tegen de daadwerkelijke GGM-Generalization-relaties in `ggm_parsed.json` (niet enkel de eerder beschreven review-items). Bevindingen:

- `Inkomstencomponent` (abstract) en `Secundair inkomstencomponent` misten, in tegenstelling tot hun tegenhangers `Vermogenscomponent` en `Primair inkomstencomponent`, een dekkingsroute — nu beide via Profiel/Inkomstencomponent → Client, symmetrisch met de Vermogenscomponent-fix uit ronde 1.
- De 6 al herclassificeerde `component`-subtypen (Alimentatie, Betaald werk, Eigen bedrijf, Pensioen, Stage, Uitkering) hadden zelf óók nog geen route (stonden op ⚠️ ondanks het juiste type) — nu via Primair inkomstencomponent → Client.
- Twee Primair-subtypen die de eerdere analyse gemist had — `Ander inkomen` en `Hobby` — zijn alsnog herclassificeerd naar `component` met dezelfde route.
- De volledige `Secundair inkomstencomponent`-familie (`Dertiende maand - eindejaarsuitkering`, `Inkomstenvermindering`, `Vergoeding`, `Vakantiegeld`) was nooit aan haar bovenliggend type gekoppeld — nu hersteld. `Heffingskorting` (ook een Secundair-subtype) had al een werkende route via [[Wiki/Bedrijfsobjecten/99-kern/heffing|Heffing]] en is verder ongewijzigd, met alleen een aantekening over de dubbele GGM-herkomst.
- **Studiefinanciering** — herclassificeerd van `detail` naar `component`: GGM-Generalization naar Primair inkomstencomponent bevestigd. Ingest van Wet studiefinanciering 2000 (art. 1.1, 2.1-2.3, 3.1-3.21) bevestigt: DUO/de Minister kent toe, niet de gemeente — zelfde patroon als Uitkering/Pensioen. Cross-gelinkt met Inkomen's `Gestopte studiefinanciering` (dezelfde lopende-vs-beëindiging-relatie als bij Alimentatie/Betaald werk/Eigen bedrijf/Uitkering).
- **Onderhoudsplicht/Onderhoudsverhouding** — blijven `detail` (geen component/BO), maar krijgen alsnog een route: de GGM-documentatie bij Onderhoudsverhouding stelt expliciet dat deze "in het profiel van de klant is opgenomen" — dus via Profiel → Client, net als Inkomstenverhouding. Ingest van Boek 1 BW Titel 17 (art. 392-408: wie tot levensonderhoud gehouden is, draagkracht/behoeftigheid, LBIO-invordering) bevestigt de juridische grondslag. Belangrijk, door de GGM-documentatie zelf aangegeven onderscheid: Onderhoudsplicht/-verhouding registreert de situatie waarin de onderhoudsplichtige **via verhaal aan de gemeente** betaalt; betaalt de onderhoudsplichtige **rechtstreeks aan de onderhoudsgerechtigde (de cliënt)**, dan heet dat `Alimentatie` en loopt het via de Inkomstencomponent-tak. Dit zijn dus geen synoniemen — de eerder overwogen aanname om ze aan Alimentatie te cross-linken bleek bij verificatie onjuist.

Totaal 17 hiaten opgeheven in dit beleidsdomein door deze ronde (bovenop de 2 uit ronde 1).

Functionele dekking: na deze correctie én na ronde 2 (Inkomstencomponent-tak, zie hieronder) blijven Stadspas en Loonbeslag/Beslag op inkomen de resterende "niet gedekt"-rijen zonder route in dit beleidsdomein — deze leggen de vermogens- en inkomenspositie van een cliënt vast zonder dat hier een BO tegenover staat, en zonder dat een simpele dekkingscorrectie volstaat: hiervoor ontbreekt daadwerkelijk een bron (zie "Ontbrekende bronnen" hieronder). Studiefinanciering is inmiddels wél opgelost (zie ronde 2) en blijft impliciet onderdeel van het profiel van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client|Client]], net als de overige inkomstencomponenten.

**Sociale Teams.** Klein en overzichtelijk: vier classificaties (typeringen van Behandeling/Bijzonderheid/Doelstelling/SociaalTeamDossier), twee detailgegevens en twee procesentiteiten (Behandeling, Caseaanmelding) — geen review-items.

**Werk.** Grotendeels detailgegevens die Werkzoekende beschrijven. Eén herclassificatie: `Werkzaamheden anders dan in arbeidsverhouding` is `abstract` (overkoepelend type met subtype `Werkzaamheden als mantelzorger`, die zelf `detail` blijft vanwege de inhoudelijke mantelzorgattributen). Naamhomoniem: `Ontheffing` (Werk, detail, vrijstellingsgegeven van Werkzoekende) is een andere entiteit dan de BO `Ontheffing` bij Inburgering — beide bestaan naast elkaar in het GGM onder dezelfde naam maar met andere betekenis en andere relatie.

**Cross-domein observaties.** Taakveld 6 kent opvallend veel naamoverlap tussen beleidsdomeinen, wat te verklaren is doordat Inburgering, Werk en Inkomen deels dezelfde levensdomeinen (werk, inkomen) vanuit een ander perspectief modelleren: "Werk" bestaat als entiteit bij Inburgering (werkgegeven van een inburgeraar) én als beleidsdomein/BO-cluster Werk (Werkzoekende, Re-integratievoorziening); "Ontheffing" bestaat als BO bij Inburgering én als detailgegeven bij Werk. Deze twee zijn echte homoniemen: functioneel verschillend, geen duplicaten om te consolideren, wel vragen ze bij toekomstige BO-vorming om expliciete disambiguatie in paginanamen en Naamoverlap-kolommen.

"Inkomen" ligt anders. Het bestaat als beleidsdomein (Inkomensvoorziening e.a.), als entiteit `Component` binnen ditzelfde beleidsdomein, als entiteit bij Schulden (`Inkomen`, component van Leefsituatie) én als `Inkomstencomponent`-structuur bij Sociaal Domein Generiek. **Herbeoordeling 2026-07-07:** dit is, anders dan Werk/Ontheffing, géén functioneel-verschillend homoniem maar **drie keer hetzelfde concept** ("de afzonderlijke bronnen waaruit iemands inkomen bestaat" — loon, uitkering, winst uit onderneming, alimentatie, vermogen) los gemodelleerd voor drie uitvoeringscontexten (cliëntprofiel, uitkeringsberekening, WSNP-leefsituatie). Zie de Beoordeling-paragrafen van Inkomen en Sociaal Domein Generiek voor de onderbouwing met citaten; de betrokken tabelrijen zijn nu expliciet cross-gelinkt naar `Inkomstencomponent` als het gedeelde bovenliggende begrip. Consolidatie tot één BO is hier dus, in tegenstelling tot Werk/Ontheffing, wel een reële toekomstige optie — maar vereist eerst een bron voor het onderliggende "Inkomstenbron"-concept (zie "Ontbrekende bronnen").

**Ontbrekende bronnen (herbeoordeling 2026-07-07).** Voor een deel van de "niet gedekt"-rijen in Inkomen en Sociaal Domein Generiek is geen dekkingscorrectie mogelijk zoals bij de vermogensitems hierboven — er ontbreekt daadwerkelijk brongrondslag. Onderscheid tussen twee categorieën, op basis van een inventarisatie van `Sources/`:

- **Geen bron aanwezig (echte hiaten, nieuwe bron nodig):**
  - **Stadspas** — geen enkel brondocument; alleen terloopse vermeldingen in ongerelateerde bronnen.
  - **Loonbeslag / Beslag op inkomen** — de term komt nergens in `Sources/` voor; "beslagvrije voet" wordt slechts terloops genoemd in schulden-gerelateerde bronnen, niet inhoudelijk uitgewerkt.
  - **"Reden aanvraag"-beëindigingsgebeurtenissen** (Gestopt betaald werk, Gestopte uitkering e.d.) — geen bron behandelt aanvraag- of beëindigingsredenen voor inkomensvoorzieningen.
  - **Vermogen/Inkomstencomponent als zelfstandig onderwerp** — er bestaat geen bronsamenvatting of onderwerpoverzicht voor "vermogenstoets" of "inkomstenbronnen" als zodanig (alleen losse vermeldingen binnen bijstand- en belastingbronnen).
  - **Normafwijking** — geen bron.
  
  Aanbeveling: deze onderwerpen vragen een nieuwe bron, bijvoorbeeld een verordening bijzondere bijstand/minimabeleid (voor Stadspas, Reden-aanvraag-redenen) of beleidsregels terug- en invordering (voor Loonbeslag/Beslag op inkomen).

- **Bron aanwezig, hergemind (herbeoordeling 2026-07-07 ronde 1):** `sgr-19-gegevensregister-suwi.md` opnieuw doorgelopen en gedistilleerd in de [[Wiki/Bronsamenvattingen/Werk en Inkomen/wet-suwi-en-sgr|bronsamenvatting]]. Resultaat gemengd:
  - **Hypotheek/Onroerend goed/Motorvoertuig (vermogenstoets)** — de deelmodellen RDW (§4.10) en Kadaster (§4.11) bevestigen expliciet de zakelijke functie (vermogenstoets Participatiewet: voertuiggegevens resp. onroerendezaakgegevens van de cliënt). De onderliggende diagrammen zelf zijn OCR-garbled en leveren geen extra attributen, maar de bevestiging van de zakelijke context is nu vastgelegd — dit was al opgelost via de Vermogenscomponent-route hierboven, deze bron onderbouwt die keuze achteraf.
  - **Onderhoudsplichtige** (SGR-rol) — géén zelfstandig begrip: slechts een rolnaam (SuwiML-tag) voor PERSOON in een adresrelatie, zonder eigen attributen. Dit specifieke document leverde dus niets op — maar zie hieronder: een gerichte nieuwe bron (Boek 1 BW) loste het GGM-begrip `Onderhoudsplicht`/`Onderhoudsverhouding` wél op.
  - **Studiefinanciering** — bij nadere lezing alleen een dossiernaam in het berichtenoverzicht, geen deelmodel. Ook hier: een gerichte nieuwe bron (Wet studiefinanciering 2000) loste het GGM-begrip alsnog op.
  - **Boete** (Participatiewet-context) — Wet SUWI art. 83d-83h regelt de bestuurlijke boete uitvoerig, maar in UWV-context, niet gemeente-specifiek; bruikbaar als vertrekpunt, niet als volledige grondslag. Blijft een hiaat.

- **Opgelost via gerichte nieuwe bronnen (herbeoordeling 2026-07-07 ronde 2):**
  - **Onderhoudsplicht/Onderhoudsverhouding** — [[Wiki/Bronsamenvattingen/Werk en Inkomen/burgerlijk-wetboek-boek-1-titel-17-levensonderhoud|Boek 1 BW Titel 17 (Levensonderhoud, art. 392-408)]] toegevoegd aan `Sources/`. Bevestigt de juridische grondslag (wie tot levensonderhoud gehouden is, draagkracht/behoeftigheid, LBIO-invordering) en maakt het onderscheid met Alimentatie expliciet (zie Sociaal Domein Generiek-paragraaf hierboven). GGM-dekking opgelost via Profiel → Client (geen nieuwe bron nodig gebleken voor de dekking zelf — die bleek al in de GGM-documentatie te staan — maar de wettelijke bron onderbouwt en verklaart het begrip).
  - **Studiefinanciering** — [[Wiki/Bronsamenvattingen/Werk en Inkomen/wet-studiefinanciering-2000|Wet studiefinanciering 2000 (art. 1.1, 2.1-2.3, 3.1-3.21)]] toegevoegd aan `Sources/`. Bevestigt: DUO/de Minister kent toe, gemeente registreert alleen. Herclassificeerd naar `component`-subtype van Primair inkomstencomponent, dekking opgelost.

Resterende bronloze hiaten in dit taakveld: **Stadspas**, **Loonbeslag/Beslag op inkomen**, de **Reden-aanvraag-beëindigingsgebeurtenissen**, **Normafwijking** en **Boete** (Participatiewet-context) — voor deze blijft een nieuwe, gerichte bron nodig (verordening bijzondere bijstand/minimabeleid resp. beleidsregels terug- en invordering).

## Dak- en thuislozen

1 entiteiten, 1 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/6-sociaal-domein/dak-en-thuislozen\|Dakloosheid]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/dak-en-thuislozen/dakloosheid\|Dakloosheid]] ✅ | — |  | Exact match |

## Gemeentebegrafenissen

1 entiteiten, 1 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/6-sociaal-domein/gemeentebegrafenissen\|Gemeentebegrafenis]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/gemeentebegrafenissen/gemeentebegrafenis\|Gemeentebegrafenis]] ✅ | — |  | Exact match |

## Generiek Jeugd en Wmo

27 entiteiten, 6 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Beschikking]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Declaratie]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/zorgdeclaratie\|Zorgdeclaratie]] ✅ | synoniem | [[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/declaratie|Declaratie (HR)]] | BO hernoemd: Zorgdeclaratie |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Levering]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/levering\|Levering]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|PGB-Toekenning]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/pgb-toekenning\|PGB-Toekenning]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Toewijzing]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/toewijzing\|Toewijzing]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Voorziening]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/voorziening\|Voorziening]] ✅ | — |  | Exact match |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Beperkingscoresoort]] | classificatie | via Beperkingscore → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | Typering/referentietabel |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Beschikkingsoort]] | classificatie | typering [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | Typering/referentietabel |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Scoresoort]] | classificatie | via Score → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Typering/referentietabel |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Declaratieregel]] | component | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | Component |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|AOMMeldingWmoJeugd]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | AOM-patroon (subtype van AanvraagOfMelding), analoog aan AOM-varianten in andere domeinen |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|AOM_AanvraagWmoJeugd]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | AOM-patroon (subtype van AanvraagOfMelding), analoog aan AOM-varianten in andere domeinen |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Beperking]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | Eigenschap van beoordeling, niet zelfstandig BO |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Beperkingscategorie]] | detail | via Beperking → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Beperkingscore]] | detail | via Beperking → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Beschikte Voorziening]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | Koppeltabel tussen Beschikking en Voorziening, geen zelfstandig BO |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Budgetuitputting]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/pgb-toekenning\|PGB-Toekenning]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Leefgebied]] | detail | via Score → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Leveringsvorm]] | detail | via Beschikte Voorziening → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Melding Eigen bijdrage]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | Component van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/eigen-bijdrage\|Eigen bijdrage]], geen zelfstandig BO |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Score]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Tarief]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/voorziening\|Voorziening]] | Attribuut van [[Wiki/Bedrijfsobjecten/99-kern/heffinggrondslag\|Heffinggrondslag]] |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Team]] | detail | via Clientbegeleider → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Verplichting Wmo Jeugd]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/inkooporder\|Inkooporder]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Verzoek om Toewijzing]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | Inkomend verzoekbericht (H10-portal) dat leidt tot Beschikking, geen zelfstandig BO |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Voorzieningsoort]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/voorziening\|Voorziening]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/generiek-jeugd-en-wmo\|Zelfredzaamheidmatrix]] | detail | via Leefgebied → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Detailgegeven (weinig attributen) |

## Inburgering

35 entiteiten, 15 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Asielstatushouder]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/asielstatushouder\|Asielstatushouder]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Brede Intake]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/brede-intake\|Brede Intake]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Examen]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/examen\|Examen]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Gezinsmigrant en Overige migrant]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/gezinsmigrant\|Gezinsmigrant]] ✅ | synoniem |  | BO hernoemd: Gezinsmigrant |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|InburgeringsAanbod]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringsaanbod\|Inburgeringsaanbod]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Inburgeringsplicht]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringsplicht\|Inburgeringsplicht]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Inburgeringstermijn]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringstermijn\|Inburgeringstermijn]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Inburgeringstraject]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringstraject\|Inburgeringstraject]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Leerroute]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/leerroute\|Leerroute]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|MAP]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/map\|MAP]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Ontheffing]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/ontheffing\|Ontheffing]] ✅ | — | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/ontheffing|Ontheffing (Werk)]] | Exact match |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|PIP]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/pip\|PIP]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|PVT]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/pvt\|PVT]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Voorbereiding op Inburgering]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/voorbereiding-op-inburgering\|Voorbereiding op Inburgering]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Vrijstelling]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/vrijstelling\|Vrijstelling]] ✅ | — | [[Wiki/Bedrijfsobjecten/4-onderwijs/leerplicht-en-leerlingenvervoer/vrijstelling|Vrijstelling (Leerplicht)]] | Exact match |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Aandachtspunt]] | detail | via Inburgeraar → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringsaanbod\|Inburgeringsaanbod]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Aanvraag verlenging Inburgeringstermijn]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringstermijn\|Inburgeringstermijn]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|B1-route]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/leerroute\|Leerroute]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Diplomawaardering]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/asielstatushouder\|Asielstatushouder]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Educatie]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/asielstatushouder\|Asielstatushouder]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Examenonderdeel]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/examen\|Examen]] | Component van Examen, geen zelfstandige levenscyclus |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Hoofddoel]] | detail | via Inburgeraar → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringsaanbod\|Inburgeringsaanbod]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|ICT-Vaardigheid]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/asielstatushouder\|Asielstatushouder]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Inburgeraar]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringsaanbod\|Inburgeringsaanbod]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Introductiemodule]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/voorbereiding-op-inburgering\|Voorbereiding op Inburgering]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Ontwikkelwens]] | detail | via Inburgeraar → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringsaanbod\|Inburgeringsaanbod]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Subdoel Aandachtspunt]] | detail | via Aandachtspunt → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringsaanbod\|Inburgeringsaanbod]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Subdoel Ontwikkelwens]] | detail | via Ontwikkelwens → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringsaanbod\|Inburgeringsaanbod]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Taalvaardigheid]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/asielstatushouder\|Asielstatushouder]] | Toetsgegeven, geassocieerd met Asielstatushouder |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Training]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/asielstatushouder\|Asielstatushouder]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Verblijfplaats AZC]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/asielstatushouder\|Asielstatushouder]] | Detailgegeven |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Verlengingsgrond]] | detail | via Aanvraag verlenging Inburgeringstermijn → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringstermijn\|Inburgeringstermijn]] | Component van Inburgeringstermijn |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Vreemdeling]] | detail | via NatuurlijkPersoon → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/gemeentebegrafenissen/gemeentebegrafenis\|Gemeentebegrafenis]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Werk]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/asielstatushouder\|Asielstatushouder]] | Werkgegeven binnen inburgeringstraject; naamhomoniem met beleidsdomein/BO Werkzoekende (taakveld Werk) |
| [[Wiki/GGM/6-sociaal-domein/inburgering\|Z-route]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/leerroute\|Leerroute]] | Detailgegeven (geassocieerd met BO) |

## Inkomen

88 entiteiten, 8 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Aflossing]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/aflossing\|Aflossing]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Aflossingsplan]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/aflossingsplan\|Aflossingsplan]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Afschrijving]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/afschrijving\|Afschrijving]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Inkomensvoorziening]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Interventie]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/interventie\|Interventie]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Kwijtschelding]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/kwijtschelding-bo\|Kwijtschelding]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Restitutie]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/restitutie\|Restitutie]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Vordering]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering\|Vordering]] ✅ | — |  | Exact match |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Aanvraagtype]] | classificatie | via Aanvraag → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Typering/referentietabel |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|ComponentSoort]] | classificatie | via Component → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]] | Typering/referentietabel |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Huisvestingsoort]] | classificatie | typering [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]] | Typering/referentietabel |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Reden aanvraag]] | classificatie | via Profiel → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Typering/referentietabel |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Reden aanvraag Levensonderhoud]] | classificatie | referentietabel | Typering/referentietabel |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Reden afwijkende startdatum]] | classificatie | typering [[Wiki/Bedrijfsobjecten/99-kern/bag/wijk\|Wijk]] | Typering/referentietabel |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|RedenBlokkering]] | classificatie | typering [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]] | Typering/referentietabel |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|RedenInstroom]] | classificatie | typering [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]] | Typering/referentietabel |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|RedenUitstroom]] | classificatie | typering [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]] | Typering/referentietabel |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Regelingsoort]] | classificatie | via Regeling → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Typering/referentietabel |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Voorwaardetype]] | classificatie | via Diensttype → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Typering/referentietabel |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Afwijkende maatregel]] | component | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/bag/wijk\|Wijk]] | Component |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Maatregel]] | component | via Normafwijking → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Component |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Maatregel op uitkering]] | component | ⚠️ geen BO bereikbaar | Component |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Onderdeel beschikking]] | component | via Diensttype → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Component |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Regeling]] | component | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Component |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Uitsluitingsgrond]] | component | ⚠️ geen BO bereikbaar | Component |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Aanvraag]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Aflossingsafspraak]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering\|Vordering]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Andere reden afwijkende startdatum]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/bag/wijk\|Wijk]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Andere reden verzoek]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Beschikking]] | detail | via Besluit → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Cross-domein parent, al gedekt door domeinspecifieke BO's |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Besluit]] | detail | via Dienst → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Betaalcomponent]] | detail | via Rechtmaand → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering\|Vordering]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Betalingsblokkade]] | detail | via Dienst → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Boete]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Boetevordering]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering\|Vordering]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Component]] | component | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]] | Component van Inkomensvoorziening, geen zelfstandig BO — zelfde concept als [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Inkomstencomponent]] (Sociaal Domein Generiek), zie herbeoordeling 2026-07-07 |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Conservatoir beslag]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering\|Vordering]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Correctie]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering\|Vordering]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Debiteur]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/aflossingsplan\|Aflossingsplan]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Dienst]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Diensten::Aanvraag]] | detail | via Reden aanvraag → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Diensten::Aanvraag levensonderhoud]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Diensttype]] | classificatie | via Dienst → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Typering/referentietabel (typeert Dienst) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Gestopt betaald werk]] | detail | ⚠️ geen BO bereikbaar | Reden-aanvraagsubtype met inhoudelijke bewijsattributen (contract, salaris), geen classificatiecode — beëindiging van [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Betaald werk]] (Sociaal Domein Generiek), zie herbeoordeling 2026-07-07 |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Gestopt of verkocht eigen bedrijf]] | detail | ⚠️ geen BO bereikbaar | Reden-aanvraagsubtype met inhoudelijke gegevens (KvK-nummer, verkoopbedrag), geen classificatiecode — beëindiging van [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Eigen bedrijf]] (Sociaal Domein Generiek), zie herbeoordeling 2026-07-07 |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Gestopte bijstanduitkering]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Gestopte detentie]] | detail | ⚠️ geen BO bereikbaar | Reden-aanvraagsubtype met inhoudelijke gegevens (duur en einddatum detentie), geen classificatiecode |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Gestopte of verlaagde alimentatie]] | detail | ⚠️ geen BO bereikbaar | Reden-aanvraagsubtype met inhoudelijke gegevens (einddatum, LBIO), geen classificatiecode — beëindiging/verlaging van [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Alimentatie]] (Sociaal Domein Generiek), zie herbeoordeling 2026-07-07 |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Gestopte studiefinanciering]] | detail | ⚠️ geen BO bereikbaar | Reden-aanvraagsubtype — beëindiging van [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Studiefinanciering]] (Sociaal Domein Generiek), zie herbeoordeling 2026-07-07 |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Gestopte uitkering]] | detail | ⚠️ geen BO bereikbaar | Reden-aanvraagsubtype met 12 inhoudelijke attributen, geen classificatiecode — beëindiging van [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Uitkering]] (Sociaal Domein Generiek), zie herbeoordeling 2026-07-07 |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Incassokostenvordering]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering\|Vordering]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Individuele plicht]] | detail | via Dienst → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Ingang bijstandsuitkering]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Inkomensvoorzieningsoort]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Interventieverzoek]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/interventie\|Interventie]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Invorderingsbasis]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/aflossingsplan\|Aflossingsplan]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Krediethypotheek]] | detail | via Debiteur → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/aflossingsplan\|Aflossingsplan]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Krediethypotheekvordering]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering\|Vordering]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Leenbijstand]] | detail | via Debiteur → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/aflossingsplan\|Aflossingsplan]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Leenbijstandvordering]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering\|Vordering]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Levenssituatie::Levenssituatie]] | detail | via Reden aanvraag → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Leveringscomponent]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering\|Vordering]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Leveringscomponenttype]] | classificatie | via Leveringscomponent → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering\|Vordering]] | Typering/referentietabel (normtabel per kostensoort) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Leveringsopdracht]] | detail | via Dienst → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Leveringsspecificatie]] | detail | via Leveringscomponent → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering\|Vordering]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Loonbeslagafspraak]] | detail | via Aflossingsafspraak → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/aflossing\|Aflossing]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Normafwijking]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Opname instelling]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Overleden partner]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Periodiek dienst Bijz. bijstand]] | classificatie | ⚠️ geen BO bereikbaar | Typering/referentietabel; door GGM zelf aangemerkt als redundant met Diensttype/Leveringscomponenttype |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Recht]] | detail | via Besluit → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Vaststelling van aanspraak, geassocieerd met Besluit |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Rechtmaand]] | detail | via Terugvorderingsverzoek → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering\|Vordering]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Referteperiode]] | detail | via Dienst → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Rentevordering]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering\|Vordering]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Terugvorderingsverzoek]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering\|Vordering]] | Verzoekbericht dat een Vordering-traject start, geen zelfstandig BO |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|UitkeringsRun]] | detail | via Component → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Uitstel aflossing]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/aflossingsplan\|Aflossingsplan]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Verbroken relatie]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Vermindering terugvordering]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering\|Vordering]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Verrekening]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering\|Vordering]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Verstrekkingsvorm]] | detail | via Diensttype → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Vertrek uit asielzoekerscentrum]] | detail | ⚠️ geen BO bereikbaar | Reden-aanvraagsubtype met inhoudelijke gegevens (COA-weekgeld), geen classificatiecode |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Verwijtbare vordering]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering\|Vordering]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Voorliggende voorziening]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/voorziening\|Voorziening]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Voorwaarde]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Vorderingscomponent]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering\|Vordering]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Wachten DigiD]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/inkomen\|Wachten beslissing instantie]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |

## Jeugdbescherming en reclassering

4 entiteiten, 1 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/6-sociaal-domein/jeugdbescherming-en-reclassering\|Zorgmelding]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/jeugdbescherming-en-reclassering/zorgmelding\|Zorgmelding]] ✅ | — |  | Exact match |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/6-sociaal-domein/jeugdbescherming-en-reclassering\|Informering]] | detail | via NatuurlijkPersoon → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/gemeentebegrafenissen/gemeentebegrafenis\|Gemeentebegrafenis]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/jeugdbescherming-en-reclassering\|Leefgebied]] | detail | via Zorgelijke Situatie → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/jeugdbescherming-en-reclassering/zorgmelding\|Zorgmelding]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/jeugdbescherming-en-reclassering\|Zorgelijke Situatie]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/jeugdbescherming-en-reclassering/zorgmelding\|Zorgmelding]] | Detailgegeven (geassocieerd met BO) |

## Schulden

32 entiteiten, 10 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/6-sociaal-domein/schulden\|Contactpoging]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/contactpoging\|Contactpoging]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Moratorium]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/moratorium\|Moratorium]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Schuld]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuld\|Schuld]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Schuldeiser]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuldeiser\|Schuldeiser]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Schuldhulptraject]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuldhulptraject\|Schuldhulptraject]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Schuldregeling]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuldregeling\|Schuldregeling]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Signaalpartner]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/signaalpartner\|Signaalpartner]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Vroegsignaal]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/vroegsignaal\|Vroegsignaal]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Vroegsignaalzaak]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/vroegsignaalzaak\|Vroegsignaalzaak]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/schulden\|WSNP-traject]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/wsnp-traject\|WSNP-traject]] ✅ | — |  | Exact match |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/6-sociaal-domein/schulden\|Begeleidingssoort]] | classificatie | via Begeleiding → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuldhulptraject\|Schuldhulptraject]] | Typering/referentietabel |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Oplossingssoort]] | classificatie | via Oplossing → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuldhulptraject\|Schuldhulptraject]] | Typering/referentietabel |
| [[Wiki/GGM/6-sociaal-domein/schulden\|AanleverendeOrganisatie]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Aanmelding]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuldhulptraject\|Schuldhulptraject]] | Procesfase van Schuldhulptraject |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Begeleiding]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuldhulptraject\|Schuldhulptraject]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Contactpersoon]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Crisisinterventie]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuldhulptraject\|Schuldhulptraject]] | Procesfase van Schuldhulptraject |
| [[Wiki/GGM/6-sociaal-domein/schulden\|InformatieEnAdvies]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuldhulptraject\|Schuldhulptraject]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Inkomen]] | component | via Leefsituatie → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/wsnp-traject\|WSNP-traject]] | Component van Leefsituatie (inkomstenbron); niet te verwarren met beleidsdomein Inkomen — zelfde concept als [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Inkomstencomponent]] (Sociaal Domein Generiek) en `Component` (Inkomen), zie herbeoordeling 2026-07-07 |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Intake]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuldhulptraject\|Schuldhulptraject]] | Procesfase van Schuldhulptraject |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Leefsituatie]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/wsnp-traject\|WSNP-traject]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Nazorg]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuldhulptraject\|Schuldhulptraject]] | Procesfase van Schuldhulptraject |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Oplossing]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuldhulptraject\|Schuldhulptraject]] | Onderdeel van Schuldhulptraject, 1:1 met traject |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Partner]] | detail | via NatuurlijkPersoon → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/gemeentebegrafenissen/gemeentebegrafenis\|Gemeentebegrafenis]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/schulden\|PlanVanAanpak]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuldhulptraject\|Schuldhulptraject]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Schuldhulporganisatie]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon\|Niet-Natuurlijk Persoon]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Stabilisatie]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuldhulptraject\|Schuldhulptraject]] | Procesfase van Schuldhulptraject |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Uitstroom]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuldhulptraject\|Schuldhulptraject]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/schulden\|VoorlopigeVoorziening]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/schuldhulptraject\|Schuldhulptraject]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/schulden\|WSNP-verklaring]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Woningbezit]] | detail | via Leefsituatie → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/schulden/wsnp-traject\|WSNP-traject]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/schulden\|Ondernemer]] | rol | n.v.t. | Functie/verantwoordelijkheid |

## Sociaal Domein Generiek

55 entiteiten, 3 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Client]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Draagkracht]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/draagkracht\|Draagkracht]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Eigen bijdrage]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/eigen-bijdrage\|Eigen bijdrage]] ✅ | — |  | Exact match |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Relatiesoort]] | classificatie | via Relatie → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Typering/referentietabel |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Verlaging door maatregel]] | component | ⚠️ geen BO bereikbaar | Component |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|AanvraagStadspas]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Alimentatie]] | component | via Primair inkomstencomponent → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Component (inkomstenbron), subtype van Primair inkomstencomponent (GGM-Generalization geverifieerd) — lopende tegenhanger van [[Wiki/GGM/6-sociaal-domein/inkomen\|Gestopte of verlaagde alimentatie]] (Inkomen), zie herbeoordeling 2026-07-07; route gecorrigeerd 2026-07-07 |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Ander inkomen]] | component | via Primair inkomstencomponent → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Herclassificatie 2026-07-07: component (inkomstenbron), GGM-Generalization naar Primair inkomstencomponent bevestigd (was over het hoofd gezien in eerdere analyse) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Bankrekening]] | component | via Vermogenscomponent → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Component (vermogensbestanddeel), subtype van Vermogenscomponent — route gecorrigeerd 2026-07-07 (was ten onrechte "beschrijft Aflossing") |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Beslag op inkomen]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Betaald werk]] | component | via Primair inkomstencomponent → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Component (inkomstenbron), subtype van Primair inkomstencomponent (GGM-Generalization geverifieerd) — lopende tegenhanger van [[Wiki/GGM/6-sociaal-domein/inkomen\|Gestopt betaald werk]] (Inkomen), zie herbeoordeling 2026-07-07; route gecorrigeerd 2026-07-07 |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Dertiende maand - eindejaarsuitkering]] | component | via Secundair inkomstencomponent → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Herclassificatie 2026-07-07: component (inkomstenbron), GGM-Generalization naar Secundair inkomstencomponent bevestigd (hele Secundair-familie was in eerdere analyse niet aan haar bovenliggend type gekoppeld) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Draagkrachtregime]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/draagkracht\|Draagkracht]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Eigen bedrijf]] | component | via Primair inkomstencomponent → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Component (inkomstenbron), subtype van Primair inkomstencomponent (GGM-Generalization geverifieerd) — lopende tegenhanger van [[Wiki/GGM/6-sociaal-domein/inkomen\|Gestopt of verkocht eigen bedrijf]] (Inkomen), zie herbeoordeling 2026-07-07; route gecorrigeerd 2026-07-07 |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Gerechtelijke uitspraak]] | detail | via Gezagsverhouding → [[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon\|Niet-Natuurlijk Persoon]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Gezagsverhouding]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon\|Niet-Natuurlijk Persoon]] | juridische status |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Heffingskorting]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/99-kern/heffing\|Heffing]] | Detailgegeven (weinig attributen) — GGM modelleert dit óók als Generalization-subtype van Secundair inkomstencomponent (2026-07-07 geverifieerd); dekking via Heffing blijft staan, geen wijziging nodig |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Hobby]] | component | via Primair inkomstencomponent → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Herclassificatie 2026-07-07: component (inkomstenbron), GGM-Generalization naar Primair inkomstencomponent bevestigd (was over het hoofd gezien in eerdere analyse) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Huishouden]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Cross-cutting sociaal domein, eenheid voor beoordeling |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Hypotheek]] | component | via Vermogenscomponent → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Component (vermogensbestanddeel), subtype van Vermogenscomponent — hiaat opgeheven 2026-07-07 |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Incident]] | detail | via Zorgelijke Situatie → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/jeugdbescherming-en-reclassering/zorgmelding\|Zorgmelding]] | Gebeurtenisregistratie, geen zelfstandig BO |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Inkomstencomponent]] | abstract | via Profiel → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Abstract: overkoepelend type met subtypen Primair/Secundair inkomstencomponent — route toegevoegd 2026-07-07, consistent met Vermogenscomponent (dezelfde soort abstracte structuur, al langer via Profiel → Client gedekt) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Inkomstenverhouding]] | detail | via Profiel → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Inkomstenvermindering]] | component | via Secundair inkomstencomponent → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Herclassificatie 2026-07-07: component (inkomstenbron), GGM-Generalization naar Secundair inkomstencomponent bevestigd |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Kostencomponent]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Leverancier]] | detail | via Rechtspersoon → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeervergunning\|Parkeervergunning]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Loonbeslag]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Maaltijdvergoeding]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Motorvoertuig]] | component | via Vermogenscomponent → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Component (vermogensbestanddeel), subtype van Vermogenscomponent — route gecorrigeerd 2026-07-07 (de link naar Voertuig beantwoordde de kentekenregistratie-vraag, niet de vermogensvraag) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Onderhoudsplicht]] | detail | via Onderhoudsverhouding → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Wettelijke verplichting, geassocieerd met Onderhoudsverhouding — route toegevoegd 2026-07-07 (Boek 1 BW Titel 17: wie tot levensonderhoud gehouden is). Nadrukkelijk niet hetzelfde als [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Alimentatie]]: GGM-documentatie bij Onderhoudsverhouding maakt expliciet onderscheid — Onderhoudsplicht/-verhouding wordt vastgelegd als de onderhoudsplichtige ná verhaal aan de gemeente betaalt; betaalt de onderhoudsplichtige rechtstreeks aan de onderhoudsgerechtigde, dan heet dat Alimentatie (inkomstencomponent) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Onderhoudsverhouding]] | detail | via Profiel → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Route toegevoegd 2026-07-07: GGM-documentatie stelt expliciet dat "de onderhoudsplichtverhouding in het profiel van de klant is opgenomen" — zelfde route als Inkomstenverhouding/Inkomstencomponent/Vermogenscomponent. Bron: Boek 1 BW Titel 17 (levensonderhoud, LBIO-invordering) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Onkostenvergoeding]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Onroerend goed]] | component | via Vermogenscomponent → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Component (vermogensbestanddeel), subtype van Vermogenscomponent — hiaat opgeheven 2026-07-07 (WOZ-object beantwoordt de OZB-belastingvraag, niet de vermogensvraag, en is dus geen route) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Pensioen]] | component | via Primair inkomstencomponent → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Component (inkomstenbron), subtype van Primair inkomstencomponent (GGM-Generalization geverifieerd); route gecorrigeerd 2026-07-07 |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Primair inkomstencomponent]] | detail | via Inkomstenverhouding → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Profiel]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Reiskosten naar het werk]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Reiskostenvergoeding]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Relatie]] | detail | via NatuurlijkPersoon → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/gemeentebegrafenissen/gemeentebegrafenis\|Gemeentebegrafenis]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Secundair inkomstencomponent]] | detail | via Inkomstencomponent → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Route toegevoegd 2026-07-07: overkoepelend type voor Dertiende maand/Heffingskorting/Inkomstenvermindering/Vergoeding/Vakantiegeld (GGM-Generalization geverifieerd), zonder eigen aggregatierelatie zoals Primair inkomstencomponent die wel heeft (via Inkomstenverhouding) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Sociale Groep]] | detail | via NatuurlijkPersoon → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/gemeentebegrafenissen/gemeentebegrafenis\|Gemeentebegrafenis]] | Groepsregistratie met weinig attributen, geen zelfstandig BO |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Sociale Relatie]] | detail | via NatuurlijkPersoon → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/gemeentebegrafenissen/gemeentebegrafenis\|Gemeentebegrafenis]] | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Stadspas]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Stage]] | component | via Primair inkomstencomponent → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Component (inkomstenbron), subtype van Primair inkomstencomponent (GGM-Generalization geverifieerd); route gecorrigeerd 2026-07-07 |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Studiefinanciering]] | component | via Primair inkomstencomponent → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Herclassificatie 2026-07-07: component (inkomstenbron), GGM-Generalization naar Primair inkomstencomponent bevestigd — DUO kent toe, niet de gemeente; gemeente registreert dit alleen als inkomstenfeit, zelfde patroon als Uitkering/Pensioen. Lopende tegenhanger van [[Wiki/GGM/6-sociaal-domein/inkomen\|Gestopte studiefinanciering]] (Inkomen). Bron: Wet studiefinanciering 2000 |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Te betalen alimentatie]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Uitkering]] | component | via Primair inkomstencomponent → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Component (inkomstenbron), subtype van Primair inkomstencomponent (GGM-Generalization geverifieerd) — lopende tegenhanger van [[Wiki/GGM/6-sociaal-domein/inkomen\|Gestopte uitkering]] (Inkomen), zie herbeoordeling 2026-07-07; route gecorrigeerd 2026-07-07 |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Vakantiegeld]] | component | via Secundair inkomstencomponent → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Herclassificatie 2026-07-07: component (inkomstenbron), GGM-Generalization naar Secundair inkomstencomponent bevestigd |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Vergoeding]] | component | via Secundair inkomstencomponent → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Herclassificatie 2026-07-07: component (inkomstenbron), GGM-Generalization naar Secundair inkomstencomponent bevestigd |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Vergoeding in natura]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Verlaging door boete]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Vermogenscomponent]] | abstract | via Profiel → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Abstract: overkoepelend type met subtypen Bankrekening/Hypotheek/Motorvoertuig/Onroerend goed |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Vrijlating inkomsten]] | detail | ⚠️ geen BO bereikbaar | Kortingsregel op inkomsten, geen zelfstandig BO |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Waardepeiling]] | detail | via Vermogenscomponent → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Taxatie-/waarderingsregistratie, geassocieerd met Vermogenscomponent |
| [[Wiki/GGM/6-sociaal-domein/sociaal-domein-generiek\|Clientbegeleider]] | rol | n.v.t. | Functie/verantwoordelijkheid |

## Sociale Teams

9 entiteiten, 1 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/6-sociaal-domein/sociale-teams\|SociaalTeamDossier]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociale-teams/sociaalteamdossier\|SociaalTeamDossier]] ✅ | — |  | Exact match |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/6-sociaal-domein/sociale-teams\|Behandelsoort]] | classificatie | via Behandeling → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociale-teams/sociaalteamdossier\|SociaalTeamDossier]] | Typering/referentietabel |
| [[Wiki/GGM/6-sociaal-domein/sociale-teams\|Bijzonderheidsoort]] | classificatie | via Bijzonderheid → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociale-teams/sociaalteamdossier\|SociaalTeamDossier]] | Typering/referentietabel |
| [[Wiki/GGM/6-sociaal-domein/sociale-teams\|Doelstellingsoort]] | classificatie | via Doelstelling → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociale-teams/sociaalteamdossier\|SociaalTeamDossier]] | Typering/referentietabel |
| [[Wiki/GGM/6-sociaal-domein/sociale-teams\|SociaalteamDossiersoort]] | classificatie | typering [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociale-teams/sociaalteamdossier\|SociaalTeamDossier]] | Typering/referentietabel |
| [[Wiki/GGM/6-sociaal-domein/sociale-teams\|Bijzonderheid]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociale-teams/sociaalteamdossier\|SociaalTeamDossier]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/sociale-teams\|Doelstelling]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociale-teams/sociaalteamdossier\|SociaalTeamDossier]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/sociale-teams\|Behandeling]] | proces | n.v.t. | Proces of processtap |
| [[Wiki/GGM/6-sociaal-domein/sociale-teams\|Caseaanmelding]] | proces | n.v.t. | Proces of processtap |

## Werk

33 entiteiten, 3 Entiteiten met BO.

### Entiteiten met BO

| GGM-entiteit | BO | Entiteitstype | Naamoverlap | Beoordeling |
|---|---|---|---|---|
| [[Wiki/GGM/6-sociaal-domein/werk\|Loonkostensubsidie]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/loonkostensubsidie\|Loonkostensubsidie]] ✅ | — |  | Exact match |
| [[Wiki/GGM/6-sociaal-domein/werk\|Reintegratievoorziening]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/re-integratievoorziening\|Re-integratievoorziening]] ✅ | synoniem |  | BO hernoemd: Re-integratievoorziening |
| [[Wiki/GGM/6-sociaal-domein/werk\|Werkzoekende]] | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] ✅ | — |  | Exact match |

### Entiteiten zonder BO

| GGM-entiteit | Entiteitstype | Dekking | Beoordeling |
|---|---|---|---|
| [[Wiki/GGM/6-sociaal-domein/werk\|Arbeidsmarktkwalificaties]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/werk\|Arbeidsperiode]] | detail | via Arbeidsverhouding → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Periodegegeven, geassocieerd met Werkzoekende |
| [[Wiki/GGM/6-sociaal-domein/werk\|Arbeidsverhouding]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/werk\|Arbeidsvermogen]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/werk\|Bemiddelingsactiviteit]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/activiteit\|Activiteit]] | Detailgegeven |
| [[Wiki/GGM/6-sociaal-domein/werk\|Bemiddelingsberoep]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/werk\|Bemiddelingstraject]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/werk\|BeschikbaarVoorArbeid]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Indicatorgegeven, geassocieerd met Werkzoekende |
| [[Wiki/GGM/6-sociaal-domein/werk\|BeschikbaarVoorBemiddeling]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/werk\|DoelReintegratievoorziening]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/werk\|Doelgroep]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/werk\|Doelgroepenregister]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | UWV beheert; gemeente gebruikt als verdeelmaatstaf |
| [[Wiki/GGM/6-sociaal-domein/werk\|Flexibliteit]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/werk\|Mobiliteit]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/werk\|Ontheffing]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Vrijstellingsgegeven van Werkzoekende; naamhomoniem met BO [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/ontheffing\|Ontheffing (Inburgering)]] |
| [[Wiki/GGM/6-sociaal-domein/werk\|Opleiding]] | detail | via Opleidingsniveau → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Opleidingsgegeven, geassocieerd met Werkzoekende |
| [[Wiki/GGM/6-sociaal-domein/werk\|Opleidingsnaam]] | detail | via Opleiding → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Detailgegeven |
| [[Wiki/GGM/6-sociaal-domein/werk\|OpleidingsnaamGecodeerd]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/rioolleiding\|Rioolleiding]] | Detailgegeven |
| [[Wiki/GGM/6-sociaal-domein/werk\|OpleidingsnaamOngecodeerd]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/rioolleiding\|Rioolleiding]] | Detailgegeven |
| [[Wiki/GGM/6-sociaal-domein/werk\|Opleidingsniveau]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/werk\|Rijbewijs /Certificaat]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/werk\|Taalbeheersing]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/werk\|TaalbeheersingNederlands]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/werk\|Vaardigheidsvaststelling]] | detail | ⚠️ geen BO bereikbaar | Detailgegeven (weinig attributen) |
| [[Wiki/GGM/6-sociaal-domein/werk\|Voorkeur]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Wensgegeven, geassocieerd met Werkzoekende |
| [[Wiki/GGM/6-sociaal-domein/werk\|VrijstellingArbeidsplicht]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/werk\|Werkervaring]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Detailgegeven (geassocieerd met BO) |
| [[Wiki/GGM/6-sociaal-domein/werk\|Werkzaamheden als mantelzorger]] | detail | via Werkzaamheden anders dan in arbeidsverhouding → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Subtype van Werkzaamheden anders dan in arbeidsverhouding, met inhoudelijke mantelzorggegevens |
| [[Wiki/GGM/6-sociaal-domein/werk\|Werkzaamheden anders dan in arbeidsverhouding]] | abstract | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Abstract: overkoepelend type met subtype Werkzaamheden als mantelzorger |
| [[Wiki/GGM/6-sociaal-domein/werk\|ZelfredzaamheidScore]] | detail | beschrijft [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/werkzoekende\|Werkzoekende]] | Detailgegeven (geassocieerd met BO) |

## BO's zonder GGM-entiteit

BO's waarvoor geen overeenkomstige GGM-entiteit bestaat. Data-objecten worden als hiaat teruggemeld aan het GGM-team; overige BO's bestaan alleen in GEMMA.

| BO | Data-object | Grondslag | Status |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/bestuursovereenkomst\|Bestuursovereenkomst]] | nee | governance-object | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/hulpverleningsplan\|Hulpverleningsplan]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/instrument\|Instrument]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/jeugdbescherming-en-reclassering/kinderbeschermingsmaatregel\|Kinderbeschermingsmaatregel]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/maatschappelijke-voorzieningen/maatschappelijke-voorziening\|Maatschappelijke voorziening]] | ja | ggm-afgeleid | **Terugmelding** |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/jeugdbescherming-en-reclassering/machtiging-gesloten-jeugdhulp\|Machtiging Gesloten Jeugdhulp]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/opvanglocatie\|Opvanglocatie]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/jeugdbescherming-en-reclassering/pleegcontract\|Pleegcontract]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/trajectplan\|Trajectplan]] | nee | procesobject | **Alleen GEMMA-BO** |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/vacature-arbeidsmarkt\|Vacature (arbeidsmarkt)]] | nee | procesobject | **Alleen GEMMA-BO** |
