## [2026-09-23] ingest | Openbare Gezondheid — Wet op de lijkbezorging: 5 nieuwe BO's + 1 rol

- **Aanleiding:** vervolg op de backlog-notitie "Domein open" (`ToDo/ingest-backlog.md`, Openbare Gezondheid) — begraafplaatsbeheer en lijkschouw stonden gesignaleerd als onvoldoende gedekte deelonderwerpen. De bestaande bron `wet-op-de-lijkbezorging.md` bleek een dunne VNG-samenvatting (één alinea); de volledige wettekst (BWBR0005009, wetten.overheid.nl, versie 2025-07-01) is opgehaald als aanvullende bron `wet-op-de-lijkbezorging-wettekst.md`.
- **GGM-controle vooraf:** geen enkele GGM-entiteit voor begraafplaats/graf/crematorium/lijkschouw gevonden in `ggm_parsed.json`. De eerdere aanname in het onderwerpoverzicht dat begraafplaats "hoort bij Beheer Openbare Ruimte (IMBOR)" bleek onjuist — dat onderwerpoverzicht bevat geen enkele vermelding. Onbezet GGM-hiaat, met de gebruiker afgestemd vóór uitwerking (alle 6 kandidaten in één ronde).
- **5 nieuwe BO's** (`Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/`), alle GGM-hiaat:
  - [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/begraafplaats|Begraafplaats]] — met subtypes Gemeentelijke/Bijzondere begraafplaats (uitwisselbaar qua proces, verschil zit in eigenaarschap)
  - [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/grafrecht|Grafrecht]] — uitsluitend recht op een particulier graf; expliciet géén registergoed (art. 28 lid 1 Wlb), dus bewust geen relatie naar het bestaande BO Zakelijk Recht (BRK)
  - [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/crematorium|Crematorium]] — analoog aan Begraafplaats (gemeentelijk/bijzonder)
  - [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/lijkschouw|Lijkschouw]] — resultaatdocument (verklaring van overlijden / verslag aan OvJ), zelfde patroon als het bestaande BO Infectieziektemelding
  - [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/verlof-tot-begraving-of-crematie|Verlof tot begraving of crematie]] — na overleg met de gebruiker bewust GEEN specialisatie van het bestaande generieke BO Vergunningen en ontheffingen: geen discretionaire beoordeling, kosteloos en nagenoeg automatisch afgegeven
- **1 nieuwe rol:** [[Wiki/Rollen/gemeentelijk-lijkschouwer|Gemeentelijk lijkschouwer]] — na overleg met de gebruiker bewust GEEN aparte BO-pagina (analoog aan het BOA-precedent: individuele registratiegegevens vallen onder HR/arbeidszaken)
- **Bestaand BO verrijkt:** [[Wiki/Bedrijfsobjecten/6-sociaal-domein/gemeentebegrafenissen/gemeentebegrafenis|Gemeentebegrafenis]] — relaties naar Begraafplaats/Crematorium toegevoegd, beschrijving uitgebreid met art. 20-22 Wlb (waarschuwingsplicht, begraving vs. crematie, kostenverhaal, identificatie onbekend lijk)
- **5 nieuwe GGM-terugmeldingen:** #119 t/m #123 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]]
- **Bijgewerkt:** `Wiki/Onderwerpoverzichten/openbare-gezondheid.md` (begrippentabel +9 begrippen, bronnen_count/begrippen_count/bo_count), `Wiki/index.md`, `ToDo/ingest-backlog.md`. Domein blijft `open`: milieugezondheid en hygiënetoezicht nog te verwerken.

## [2026-09-23] ingest | Risicobeheer volledig afgerond: frauderisicoanalyse, fraudeonderzoek, Risicobeheerfonds onderzocht

- **Aanleiding:** laatste open domein afronden — Risicobeheerfonds en frauderisicobibliotheek stonden gesignaleerd als te dun voor BO-beoordeling.
- **Risicobeheerfonds** — het VNG-initiatief nader onderzocht: een collectieve opstal-/gebouwenverzekering (start 2026), voor de helft eigendom van de deelnemende gemeenten en voor de helft van de VNG, na vergunning onder DNB-toezicht (Solvency II). Te dun gedocumenteerd voor een eigen BO of actor-pagina (geen toetredingsprocedure of deelnemersovereenkomst-detail beschikbaar) — de polis zelf is qua aard een gewone opstal-/inventarisverzekering, dus als voorbeeld toegevoegd aan het bestaande BO [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/verzekering|Verzekering]], geen nieuw element.
- **Frauderisicobibliotheek** — de RPO-bibliotheek zelf bleef een dunne landelijke referentielijst, maar het doorzoeken leverde een veel rijkere gemeentelijke bron op: het Fraudebeleid en de Frauderisicoanalyse van Gemeente Brummen (CVDR699229, collegebesluit 16 mei 2023) — een concreet, operationeel document met een tabel van 60+ fraudegevoelige processen, een fraudedriehoek-beoordelingskader (Gelegenheid × Druk × Rationalisatie) en een compleet 8-stappen handelingsprotocol bij een vermoeden van fraude.
- **2 nieuwe BO's**, beide GGM-hiaat, fysiek ondergebracht bij de bestaande BBV-familie in Financien:
  - [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/frauderisicoanalyse|Frauderisicoanalyse]] — het jaarlijkse document (inventarisatie + kans×impactanalyse), onderdeel van de rechtmatigheidsverantwoording van het college sinds 2023; vergelijkbaar governance-patroon als het bestaande BO Weerstandsvermogen en risicobeheersing.
  - [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/fraudeonderzoek|Fraudeonderzoek]] — het onderzoeksproces bij een concreet vermoeden (5/6 criteria, geen eigen wettelijke grondslag); vergelijkbaar patroon als het bestaande BO Bibob-toets.
- **Afbakening bevestigd:** het GGM kent alleen `WoonfraudeAanvraagOfMelding` (extern gerichte woonfraude, taakveld 1) — een ander concept dan de hier vastgelegde interne, bestuurs-/ambtenarengerichte fraude.
- **2 nieuwe GGM-terugmeldingen:** #126 (Frauderisicoanalyse), #127 (Fraudeonderzoek) in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
- **Domein Risicobeheer nu volledig afgerond** (status `afgerond`): 3 bronsamenvattingen, 7 begrippen, 5 BO's. Hiermee zijn alle backlog-domeinen uit `ToDo/ingest-backlog.md` afgerond.
- **Bijgewerkt:** `Wiki/Onderwerpoverzichten/risicobeheer.md`, `Wiki/index.md`, `ToDo/ingest-backlog.md`.

## [2026-09-23] ingest | Openbare Orde en Veiligheid volledig afgerond: coffeeshop, Zorg- en Veiligheidshuis, model-APV-vergunningplichten

- **Aanleiding:** de drie laatste open punten uit het domein afronden: Coffeeshop en Zorg- en Veiligheidshuis (bron te dun gesignaleerd in eerdere ronde), model-APV-vergunningplichten (overlap met bestaande vergunning-BO's nog te onderzoeken).
- **Coffeeshop** — Coffeeshopbeleid 2024 (Gemeente Vijfheerenlanden, CVDR730395) opgehaald, een rijke gemeentelijke beleidsbron. 1 nieuw BO: [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/openbare-orde-en-veiligheid/gedoogverklaring|Gedoogverklaring]] (art. 13b Opiumwet, GGM-hiaat) — bewust geen specialisatie van [[Vergunningen en ontheffingen]], want geen discretionaire beoordeling en eigen wettelijke grondslag. De bijbehorende exploitatievergunning blijft gedekt door het al bestaande subtype Horecavergunning.
- **Zorg- en Veiligheidshuis** — Landelijk Kader Veiligheidshuizen (Ministerie van Veiligheid en Justitie, 2013, 42 pagina's) opgehaald en geconverteerd. 1 nieuwe actor: [[Wiki/Actoren/zorg-en-veiligheidshuis|Zorg- en Veiligheidshuis]] (netwerksamenwerkingsverband, precedent GGD/Sociaal ontwikkelbedrijf — geen BO voor de organisatie zelf). Bij het doorlezen bleek er meer in de bron te zitten dan het oorspronkelijke signaal verwachtte: een concreet procesobject met eigen levenscyclus (screening/triage → behandeling → integraal plan van aanpak). Met de gebruiker afgestemd vóór vastlegging → 1 nieuw BO: [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/openbare-orde-en-veiligheid/casus-veiligheidshuis|Casus (Veiligheidshuis)]] (5/6 criteria — geen eigen wettelijke grondslag, alleen bestuurlijk landelijk kader; GGM-hiaat). Naam "Casus" bewust overgenomen uit de brontaal (niet "Persoonsgerichte Aanpak/PGA", die term komt in déze bron niet voor).
- **Model-APV-vergunningplichten** — autoverhuur, glazenwassers, spyshops en woningverhuur/-bemiddeling (uit de eerder ge-ingeste Handreiking APV en ondermijning) bleken qua vorm identiek aan de al bestaande subtypes (Standplaatsvergunning, Horecavergunning e.a.): als 4 nieuwe subtypes toegevoegd aan [[Vergunningen en ontheffingen]], geen hiaat en geen aparte bron nodig. Evenementen en exploitatie openbare inrichting waren al gedekt.
- **2 nieuwe GGM-terugmeldingen:** #124 (Gedoogverklaring), #125 (Casus Veiligheidshuis) in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
- **Domein Openbare Orde en Veiligheid nu volledig afgerond** (status `afgerond`): 7 bronsamenvattingen, 12 begrippen, 7 BO's, 2 actoren, 1 rol. Eén punt blijft bewust "ter discussie" voor een toekomstige ronde: of Alcoholoverlastgebied, Veiligheidsrisicogebied en Gebiedsaanwijzing (Omgevingswet) onder een overkoepelend generiek concept moeten.
- **Bijgewerkt:** `Wiki/Onderwerpoverzichten/openbare-orde-en-veiligheid.md`, `Wiki/index.md`, `ToDo/ingest-backlog.md`, `Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/vergunningen-en-ontheffingen.md` (4 nieuwe subtypes).

## [2026-09-23] analyse | Europa en Internationaal afgesloten: geen apart BO voor Europese subsidie

- **Aanleiding:** openstaand punt uit de backlog ("Domein open: potentiële BO's bij rijkere bronnen: Europese subsidie(aanvraag)"). Op verzoek van de gebruiker gericht gezocht naar een rijkere, gemeentelijk-perspectief bron.
- **Drie kandidaatbronnen beoordeeld en afgewezen** (niet opgehaald als Source, want te dun of niet gemeentelijk):
  - EU-fondsenwijzer (europadecentraal.nl) — navigatieportaal, geen procesbegrippen.
  - Regeling Europese EZK- en LNV-subsidies 2021 (REES 2021, wetten.overheid.nl/BWBR0045685) — rijke wettekst (deelbetaling, subsidiabele kosten, penvoerder) maar doelgroep is bedrijven/landbouwers/kennisinstellingen, niet gemeenten.
  - Subsidieregeling cofinanciering EFRO 2022-2027 Zuid-Holland / Kansen voor West (CVDR686362) — governance-verband omvat wel de G4-gemeenten als partner, maar de regeling zelf is beperkt concreet (details per openstelling) en noemt gemeenten niet expliciet als doelgroep.
- **Conclusie:** Europese subsidie(aanvraag) is geen zelfstandig BO maar een potentiële specialisatie van het bestaande BO [[Wiki/Bedrijfsobjecten/9-interne-organisatie/subsidies/subsidie|Subsidie]] (subsidierecht-domein). Domein Europa en Internationaal daarmee afgerond op 0 BO's.
- **Bijgewerkt:** `Wiki/Onderwerpoverzichten/europa-en-internationaal.md` (status → afgerond, conclusie + geraadpleegde bronnen vastgelegd), `ToDo/ingest-backlog.md`, `Wiki/index.md`.

## [2026-09-23] ingest | Basisregistraties — RSGBPlus batch 2: 8 nieuwe BO's, domein Basisregistraties volledig afgerond

- **Aanleiding:** vervolg op batch 1 (zie vorige log-entry). Alle ~28 resterende RSGB Deel II-objecttypen (buiten de al gedekte basisregistraties en de batch 1-generalisaties) beoordeeld tegen GGM (`ggm_parsed.json`) en brontekst. Vooraf besproken met de gebruiker in twee rondes (6 sterke kandidaten in één keer akkoord; 2 relatie-objecttypen — Ouder-kind-relatie en Huishoudenrelatie — apart, op verzoek van de gebruiker omdat de RSGB-namen "als informatiemodel klonken i.p.v. BO").
- **8 nieuwe BO's:**
  - [[Wiki/Bedrijfsobjecten/99-kern/brp/natuurlijk-persoon|Natuurlijk Persoon]] (GGM exact) — sluit de asymmetrie met de al bestaande [[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon|Niet-Natuurlijk Persoon]]; tweede specialisatie van Rechtspersoon.
  - [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/huishouden|Huishouden]] (GGM exact, duplicaat met Sociaal Domein Generiek — RSGBPlus als primair gekozen, terugmelding toegevoegd).
  - [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/huishoudenlid|Huishoudenlid]] (ggm-afgeleid) — RSGB heet dit "Huishoudenrelatie"; herdoopt na twee ronden naamzoektocht (RSGB-brondefinitie "positie die de persoon binnen het huishouden inneemt" → eerst "Huishoudenpositie" voorgesteld, gebruiker koos uiteindelijk "Huishoudenlid" als natuurlijker begrip).
  - [[Wiki/Bedrijfsobjecten/99-kern/brp/ouderschap|Ouderschap]] (ggm-afgeleid, uit attributen ouder1/ouder2/gezinsrelatie op IngeschrevenPersoon) — RSGB heet dit "Ouder-kind-relatie"; herdoopt naar de term die het al ge-ingeste Logisch Ontwerp BRP zelf consequent gebruikt ("vaststelling/ontkenning ouderschap"), analoog aan hoe [[Wiki/Bedrijfsobjecten/99-kern/brp/huwelijk|Huwelijk]] eerder al als herkenbare naam i.p.v. de lange GGM-naam is gekozen.
  - [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/overig-gebouwd-object|Overig Gebouwd Object]] en [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/overig-terrein|Overig Terrein]] (beide GGM exact) — ontbrekende derde/vierde specialisaties naast Verblijfsobject resp. Standplaats/Ligplaats.
  - [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/woz-belang|WOZ-belang]] (GGM exact, beleidsdomein Vastgoed) — koppelt WOZ-object aan Rechtspersoon; bestaande "ingekorte" relatie op `woz-object.md` (via Debiteur) aangevuld met de directe relatie.
  - [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/gemeentelijke-openbare-ruimte|Gemeentelijke Openbare Ruimte]] (ggm-afgeleid, géén GGM-entiteit) — ander abstractieniveau dan de bestaande BAG-Openbare Ruimte (geo-object over meerdere woonplaatsen i.p.v. benaming binnen één woonplaats); als mogelijk hiaat teruggemeld.
- **~19 begrippen beoordeeld als géén BO** (referentietabellen zoals Aard recht verkort/Aard verkregen recht/Academische titel/Kadastrale gemeente/Reisdocumentsoort — RSGB noemt deze zelf "tabel-objecttype"; koppelobjecten zonder eigen gegevens zoals Functionaris — bron: "kan niet zelfstandig bestaan" — en Overige/Adresseerbaar object aanduiding; abstracte generalisaties Kadastrale Onroerende Zaak/Inrichtingselement; en begrippen die al gedekt zijn door bestaande BO's/rijen: Ander (Niet-)Natuurlijk Persoon als subtype, Ingeschreven Niet-Natuurlijk Persoon (dekt door bestaande Niet-Natuurlijk Persoon), Kadastrale/Zakelijk Recht Aantekening (dekt door bestaande generieke "Aantekening"-rij BRK), Ingezetene/Niet-ingezetene/Nationaliteit/Verblijfstitel (bleken al in de BRP-sectie beoordeeld).
- **Cross-referenties bijgewerkt:** `niet-natuurlijk-persoon.md` (link naar Natuurlijk Persoon, subtype Ander Niet-Natuurlijk Persoon toegevoegd), `rechtspersoon.md` (specialisatie-tabel en relaties uitgebreid met Natuurlijk Persoon), `woz-object.md` (directe WOZ-belang-relatie toegevoegd naast de bestaande ingekorte Debiteur-relatie), `sportpark.md`/`veld.md` (platte-tekstverwijzing "OverigBenoemdTerrein" omgezet naar wiki-link naar Overig Terrein).
- **Domein Basisregistraties nu volledig afgerond** (status `afgerond`): alle 8 GGM-gemodelleerde basisregistraties verwerkt, 48 BO's totaal.
- **Bijgewerkt:** `ToDo/ingest-backlog.md`, `Wiki/Onderwerpoverzichten/basisregistraties.md` (volledige RSGBPlus-begrippentabel, tellingen, status), `Wiki/index.md`, `Wiki/Analyses/ggm-terugmeldingen.md` (Huishouden-duplicaat, Gemeentelijke Openbare Ruimte-hiaat).

## [2026-09-23] ingest | Basisregistraties — RSGBPlus batch 1: bron gevonden (RSGB Deel II), 1 nieuw BO (Rechtspersoon)

- **Aanleiding:** het enige bewust opengelaten resthiaat van het domein Basisregistraties (`ToDo/ingest-backlog.md`, "RSGBPlus overig") was zonder bekende bron. Gebruiker gaf de aanwijzing dat RSGB een subset van de landelijke basisregistratie-informatiemodellen bevat — dat wees naar het RSGB-referentiemodel zelf als bron voor de RSGBPlus-detailentiteiten, in plaats van naar een externe RSGBPlus-specifieke catalogus.
- **Bron gevonden en opgehaald:** RSGB 2.02 Deel II: Specificaties (VNG Realisatie/KING, `https://vng-realisatie.github.io/RSGB/documenten/RSG_Basisgegevens_2.02_deel_II_(in_gebruik).pdf`, 134 pagina's, zelfde versie als het al ge-ingeste Deel I) → `Sources/Standaarden/RSG_Basisgegevens_2.02_deel_II_(in_gebruik).md`. Bevat de gegevenscatalogus (62 objecttypen) waar Deel I alleen het referentiemodel op hoofdlijnen beschrijft.
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/Standaarden/rsgb-deel-ii-specificaties|RSGB 2.02 Deel II: Specificaties]].
- **Gefaseerde aanpak afgesproken** (~24 objecttypen al gedekt via bestaande basisregistratie-BO's, ~6 generalisaties, ~26 overige detailentiteiten). Batch 1 (generalisaties) nu verwerkt:
  - **Rechtspersoon** — nieuw BO, [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/rechtspersoon|Rechtspersoon]]. GGM exact (abstract, RSGBPlus), generalisatiewortel voor ~20 domeinrollen (Eigenaar, Huurder, Pachter, Debiteur, Schuldeiser, Signaalpartner, Leverancier, Gemachtigde, e.a.). **Herziet een eerdere beslissing:** bij de NHR-ingest (2026-06-25, zie [[Wiki/Bedrijfsobjecten/99-kern/nhr/niet-natuurlijk-persoon|Niet-Natuurlijk Persoon]]) was Rechtspersoon beoordeeld als "te abstract voor een BO"; na expliciete heroverweging (relatie-rijkdom en herkenbaarheid wegen zwaarder) alsnog vastgelegd.
  - **Benoemd Object, Gebouwd Object, Benoemd Terrein, Adresseerbaar Object, Subject** — beoordeeld en bewust *geen* BO (te abstract/geen eigen bestaan, resp. geen eigen GGM-entiteit voor Subject); vastgelegd in de begrippentabel met reden.
  - **Natuurlijk Persoon** — nog geen BO-pagina, gepland voor batch 2.
- **Cross-referenties bijgewerkt:** `niet-natuurlijk-persoon.md` (relatie + body-tekst herzien, contradictie met nieuwe Rechtspersoon-pagina opgelost), `schuldeiser.md`, `signaalpartner.md`, `leverancier.md`, `vastgoedcontract.md` (platte-tekstverwijzingen naar "Rechtspersoon" omgezet naar wiki-link; `vastgoedcontract.md` kreeg ook een ontbrekende `bo_relaties`-regel).
- **Nog te doen (batch 2):** ~26 overige detailentiteiten/referentietabellen uit RSGB Deel II (Huishouden, Ingezetene, Kadastrale Gemeente, Land, Nationaliteit, Overig Gebouwd Object, Overig Terrein, WOZ-belang, e.a.) plus Natuurlijk Persoon. `entiteitendekking 99-kern` bewust nog niet geregenereerd — pas zinvol na afronding van het hele domein.
- **Bijgewerkt:** `ToDo/ingest-backlog.md`, `Wiki/Onderwerpoverzichten/basisregistraties.md` (nieuwe RSGBPlus-sectie, status `in-behandeling`, tellingen), `Wiki/index.md` (§Domeinen, §Bedrijfsobjecten, §Bronsamenvattingen).

## [2026-09-23] ingest | Risicobeheer (nieuw domein): 4 dunne bronnen + 2 zelf opgehaalde rijkere bronnen, 3 BO's

- **Aanleiding:** eerstvolgende onverwerkte sectie in de ingest-backlog. Net als Openbare Orde en Veiligheid bevatte deze 4 VNG-portaalpagina's (Risicobeheerfonds, Risico Platform Overheden, EVO/Verzekeringslab, rubriekpagina) zonder concrete objecten, netwerk-/strategieniveau.
- **Op verzoek van de gebruiker** ("zoek eerst betere bronnen") 2 primaire bronnen zelf opgezocht en opgehaald: een gemeentelijke Nota Weerstandsvermogen en Risicobeheersing (Waadhoeke, lokaleregelgeving.overheid.nl) en een gemeentelijk Verzekeringsbeleid (Eindhoven 2022, lokaleregelgeving.overheid.nl). De onderliggende wettekst art. 11 BBV bleek al aanwezig in de eerder ge-ingeste bron `besluit-begroting-en-verantwoording` (Financien-domein) en is hergebruikt i.p.v. opnieuw opgehaald.
- **3 nieuwe BO's**, alle governance-object/procesobject zonder GGM-match, fysiek in `Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/` naast de bestaande BBV-familie: **Weerstandsvermogen en risicobeheersing** (art. 212 Gemeentewet + art. 11 BBV, met de nota/paragraaf-tweeledigheid als toelichting), **Risico** (individuele risico-inventarisatiepost, subtypes afgedekt/niet-afgedekt) en **Verzekering** (7 subtypen polissen uit de Eindhoven-bron). Reserve en Financiële Voorziening kregen een nieuwe relatie naar Risico; Jaarrekening kreeg een relatie naar Weerstandsvermogen en risicobeheersing; Financien-onderwerpoverzicht kreeg een cross-referentienotitie (BO's geteld bij Risicobeheer, niet dubbel bij Financien).
- **Alle 4 oorspronkelijke bronnen → Niet-relevant.** Risicobeheerfonds en de frauderisicobibliotheek gesignaleerd maar niet uitgewerkt (te dun; Risicobeheerfonds leest als toepassing van het bestaande BO Verbonden Partij) — als openstaande vraag vastgelegd.
- **Nieuw onderwerpoverzicht aangemaakt:** `Wiki/Onderwerpoverzichten/risicobeheer.md`.
- **Bijgewerkt:** `ToDo/ingest-backlog.md`, `Wiki/Analyses/ggm-terugmeldingen.md` (#114-116), `Wiki/Onderwerpoverzichten/financien.md` (cross-referentie), `Wiki/index.md` (§Domeinen, §Bedrijfsobjecten, §Bronsamenvattingen).

## [2026-09-23] ingest | Openbare Orde en Veiligheid (nieuw domein): 10 dunne bronnen + 4 zelf opgehaalde rijkere bronnen, 5 BO's, 1 actor, 1 rol

- **Aanleiding:** eerstvolgende onverwerkte sectie in de ingest-backlog (na correctie van 2 stale afgeronde secties, Milieu en Onderwijs, die nog als open stonden). Backlog bevatte 10 VNG-portaalpagina's (16-31 regels elk), zonder concrete objecten — behalve één signaal: BOA had een exacte GGM-match (beleidsdomein "1 Veiligheid en Vergunningen").
- **Op verzoek van de gebruiker** ("zoek betere bronnen") 4 primaire bronnen zelf opgezocht en opgehaald: Wet Bibob (wetten.overheid.nl), volledige Alcoholwet (wetten.overheid.nl), Regeling domeinlijsten BOA (wetten.overheid.nl), VNG Handreiking APV en ondermijning (PDF, eerste download was afgekapt — 2,8 van 3,3 MB — opnieuw gedownload). Voor de Gemeentewet-artikelen (151b, 174, 174a, 174b) bleek een eerder ge-ingest volledig wettekst-bestand al te bestaan onder Bestuur, direct herbruikt i.p.v. opnieuw op te halen.
- **7 nieuwe elementen**, elk na expliciet overleg over structurele keuzes: rol **BOA** (GGM exact), actor **Landelijk Bureau Bibob** (precedent Ombudsman/ACOI), BO **Bibob-toets** (met Bibob-advies als specialisatie van het bestaande BO [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/advies|Advies]], net als eerder Welstandsadvies), BO **Preventie- en handhavingsplan alcohol** (art. 43a Alcoholwet), BO **Alcoholoverlastgebied** (art. 25f Alcoholwet) en BO **Veiligheidsrisicogebied** (art. 151b/174b Gemeentewet) — beide bewust los gehouden van het bestaande BO Gebiedsaanwijzing (ander juridisch kader/registratiesysteem, IMOW vs. Alcoholwet/Gemeentewet) — en BO **Sluitingsbesluit** (art. 174/174a Gemeentewet, art. 13b Opiumwet) — bewust los gehouden van Handhavingsbesluit (andere bevoegde actor: burgemeester i.p.v. college).
- **9 van de 10 oorspronkelijke bronnen → Niet-relevant**; `gemeentelijke-handhaving-boas.md` behield een eigen (korte) bronsamenvatting omdat die al als bron bij BOA werd geciteerd. Coffeeshop en Zorg- en Veiligheidshuis gesignaleerd maar niet uitgewerkt (bron te dun); als openstaande vraag/zoeksuggestie vastgelegd.
- **Nieuw onderwerpoverzicht aangemaakt** (bestond nog niet): `Wiki/Onderwerpoverzichten/openbare-orde-en-veiligheid.md`.
- **Bijgewerkt:** `ToDo/ingest-backlog.md` (Milieu/Onderwijs met terugwerkende kracht afgevinkt; Openbare Orde en Veiligheid + 4 aanvullende bronnen afgevinkt), `Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/advies.md` (Bibob-toets-relatie), `Wiki/Analyses/ggm-terugmeldingen.md` (#109-113), `Wiki/index.md` (§Domeinen, §Bedrijfsobjecten, §Actoren, §Rollen, §Bronsamenvattingen).

## [2026-09-23] ingest | informatiebeheer: 4 Woo-bronnen bleken verkeerd geplaatst, verhuisd naar Informatiesamenleving; 2 nieuwe BO's, 1 actor

- **Aanleiding:** `/ingest informatiebeheer` trof 4 onverwerkte bronnen aan over Woo-actieve openbaarmaking. Bij het lezen bleek `handreiking-woo-gemeentelijke-praktijk.md` een exact duplicaat (alleen frontmatter verschilde) van een bron die al eerder — onder onderwerp Informatiesamenleving — was verwerkt, inclusief de BO's Woo-verzoek en Klacht en de rol Woo-contactpersoon.
- **Herindeling:** de gebruiker bevestigde dat alle 4 bronnen inhoudelijk bij Informatiesamenleving horen, niet bij informatiebeheer (dat gaat over archivering: Document → Informatieobject → Archiefstuk). Het duplicaat is verwijderd uit `Sources/`; de 3 overige bronnen (wettekst art. 3.1-3.5, de 17-categorieën-bijlage, de RDDI-projectpagina) zijn verplaatst naar `Sources/Onderwerpen/Informatiesamenleving/` (RDDI-pagina direct naar `Niet-relevant/`, want procesinformatie zonder concrete objecten).
- **Nieuwe bronsamenvattingen:** wet-open-overheid-actieve-openbaarmaking, 17-categorieen-actief-openbaarmaken-woo.
- **Nieuwe elementen, na overleg met de gebruiker per kandidaat:** BO **Meerjarenplan** (art. 6.2 Woo, governance-object, GGM-hiaat), actor **ACOI** (precedent: Ombudsman — onafhankelijk wettelijk orgaan met klachtbehandelingstaak), BO **Advies** (generiek procesobject, GGM-hiaat). Bij Advies: het bestaande BO [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/welstandsadvies|Welstandsadvies]] stond zonder generalisatierelatie op zichzelf — met akkoord van de gebruiker retroactief gekoppeld als specialisatie van Advies.
- **Afgewezen na heroverweging:** Onderzoeksrapport (geen bestaande specialisatie, dunne levenscyclus, smalle Woo-afbakening) en Jaarplan/Jaarverslag (al gedekt als BBV-Jaarstukken via `bo_subtypes` op het bestaande BO Jaarrekening, tegenhanger van Begroting).
- **Bijgewerkt:** `Wiki/Onderwerpoverzichten/informatiesamenleving.md` (frontmatter-tellingen, begrippentabel, bronnenlijst, Niet-relevant-lijst, Beoordeling), `Wiki/Onderwerpoverzichten/informatiebeheer.md` (notitie over de verhuizing), `Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/welstandsadvies.md` (generalisatie-relatie), `Wiki/Analyses/ggm-terugmeldingen.md` (#107-108), `Wiki/index.md` (§Domeinen, §Bedrijfsobjecten ×2, §Actoren, §Bronsamenvattingen).

## [2026-09-23] fix | Subsidie-specialisaties alsnog gekoppeld: Partijsubsidie, Loonkostensubsidie, Sloopregeling kregen nooit een structurele relatie naar Subsidie

- **Aanleiding:** bij het afronden van milieu (Sloopregeling ter discussie) besloten dat Sloopregeling een eigen BO-pagina blijft i.p.v. subtype van Subsidie, analoog aan het bestaande precedent Partijsubsidie/Loonkostensubsidie. Gebruiker vroeg door: dat precedent bleek puur beargumenteerd vanuit "geen generalisatierelatie in de GGM-XMI" — maar `subsidie.md` had voor geen van de drie specifieke subsidievormen ook maar een structurele `bo_relaties`-link, alleen prozavermelding. Het ontbreken van een GGM-relatie sluit een wiki-niveau Specialisatie-relatie niet uit (zelfde redenering als eerder toegepast bij Zwembad → Sportlocatie, ook zonder GGM-entiteit).
- **Gecontroleerd of Partijsubsidie/Loonkostensubsidie/Sloopregeling in hetzelfde GGM-beleidsdomein als Subsidie zitten:** nee — Loonkostensubsidie zit zelfs in een heel ander taakveld (Werk, taakveld 6, eigen GGM-entiteit) dan Subsidie (Subsidies, taakveld 9); Partijsubsidie en Sloopregeling hebben geen GGM-entiteit. Besluit: verschillend taakveld/beleidsdomein is een GGM-organisatieprincipe, geen blokkade voor een bedrijfsmatige relatie.
- **Doorgevoerd:** generalisatie-relatie (richting `naar-dit-BO`) toegevoegd op alle 3 kindpagina's; `subsidie.md` kreeg een nieuwe `## Specialisaties`-sectie met alle 3 en de reciproke `van-dit-BO`-relaties.
- **Bijgewerkt:** `subsidie.md`, `partijsubsidie.md`, `loonkostensubsidie.md`, `sloopregeling.md` (frontmatter `bo_relaties` + body Relaties-tabellen).

## [2026-09-23] ingest | milieu afgerond: 3 ter-discussie-BO's opgelost, 4 bronnen niet-relevant, 1 bron gevlagd, bronnenlijst-bug gecorrigeerd

- **Aanleiding:** domein had 5 onverwerkte VNG-rubriekbronnen (bekend, al gedocumenteerd) én 3 BO's expliciet gemarkeerd ⚠️ "ter discussie"/"voorgelegd aan team" (Materiaalpasspoort, Afvalstoffenverordening, Sloopregeling) — een bewuste deferral in de brontekst zelf, dus voorgelegd aan de gebruiker in plaats van zelf besloten.
- **Bronnen:** `rubriek-milieu.md`, `luchtkwaliteit.md`, `zeer-zorgwekkende-stoffen.md`, `afval-en-circulaire-economie.md` (dunne VNG-portaalpagina's, inhoudelijk overlappend met de al verwerkte rijkere Utrechtse bronnen) → verplaatst naar `Sources/Onderwerpen/Milieu/Niet-relevant/`. `asbest.md` bevat wél een zwak signaal (meldingsplicht bij asbestverwijdering) maar is te dun voor een BO — blijft staan, gedocumenteerd als openstaande vraag i.p.v. stilzwijgend weggezet.
- **Materiaalpasspoort** (5/6) en **Afvalstoffenverordening** (5/6): beide bevestigd als BO. Afvalstoffenverordening volgt hetzelfde patroon als het bestaande BO Heffingsverordening (verordening als juridische grondslag naast de operationele heffing). **Bijvangst:** de "Bronnen"-sectie van Afvalstoffenverordening bevatte 10 duidelijk onjuiste, gekopieerde verwijzingen (bodem/grondwater/luchtkwaliteit/water-bronnen die inhoudelijk niets met afval te maken hebben) — gecorrigeerd naar de daadwerkelijk relevante bron (`grondstoffennota-utrecht-2020`).
- **Sloopregeling** (6/6): eerst overwogen als subtype in te voegen in het generieke GGM Model Subsidies (Subsidie/Subsidieaanvraag/Subsidiebeschikking, net gebouwd bij de Recht-ingest), maar dat bleek in directe tegenspraak met een expliciet precedent op `subsidie.md` zelf: specifieke subsidievormen (Partijsubsidie, Loonkostensubsidie) krijgen daar bewust een eigen BO-pagina, "geen generalisatierelatie in de XMI". Onderzocht of een tussenlaag naar doelgroep (burgers/ondernemers vs. instellingen) zou passen: Loonkostensubsidie bleek werkgever-gericht met een eigen GGM-entiteit in een ander beleidsdomein, Partijsubsidie institutioneel — geen van beide deelt genoeg structuur met het burger-gerichte, GGM-loze Sloopregeling om nu een nieuwe laag te rechtvaardigen op basis van één instantie. Besluit: Sloopregeling blijft eigen BO, zelfde patroon als de twee precedenten.
- **Bijgewerkt:** `materiaalpasspoort.md`, `afvalstoffenverordening.md`, `sloopregeling.md` (⚠️-markers verwijderd, besluit gedocumenteerd), `subsidie.md` (Sloopregeling toegevoegd aan het precedent-voorbeeld), `Wiki/Onderwerpoverzichten/milieu.md` (begrippentabel, "Nog te verwerken"/"Openstaande vragen" opgeschoond, conclusie, `status` in-behandeling→afgerond), `Wiki/index.md` (§Domeinen, BO-telling 33→36 gecorrigeerd).

## [2026-09-23] fix | mobiliteit, omgevingswet, werk-en-inkomen afgerond

- **mobiliteit:** `mobiliteit.md` (VNG-rubriekpagina, portaaloverzicht zonder concrete objecten) nog niet beoordeeld — verplaatst naar `Sources/Onderwerpen/mobiliteit/Niet-relevant/`. Van de 3 open vragen bleek "P+R vs. Parkeergarage" stale: de relatie stond al op beide BO-pagina's. Overige 2 (Deelvoertuig, Bouwlogistiek Centrum) zijn vooruitgeschoven onderzoekspunten.
- **omgevingswet:** homoniem Activiteit (Omgevingswet) ↔ Activiteit (Musea) was al gedisambigueerd in `bo_homoniemen` op de BO-pagina maar ontbrak in het centrale overzicht — teruggemeld als #106. Overige 4 punten (2 definitie-kwaliteitsissues, 7 resterende GGM-detailentiteiten, Programma als toekomstige kandidaat) zijn vooruitkijkende notities.
- **werk-en-inkomen:** geen inhoudelijke wijziging, alleen stale `bronnen_count` (3→6, correct is aantal in "Verwerkte bronnen") en status gecorrigeerd. Beide open vragen expliciet vooruitgeschoven wegens ontbrekende rijkere bronnen.
- **Bijgewerkt:** `Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/omgevingswet/activiteit.md` (terugmelding-verwijzing), `Wiki/Analyses/ggm-terugmeldingen.md` (#106), 3× `Wiki/Onderwerpoverzichten/*.md` (status, conclusie), `Wiki/index.md` (§Domeinen ×3).

## [2026-09-23] ingest | onderwijs afgerond: 3 bronnen alsnog verwerkt (1 nieuw subtype, 2 niet-relevant)

- **Aanleiding:** domein claimde "geen openstaande vragen" maar `Sources/Onderwerpen/Onderwijs/` bevatte 3 nog niet verwerkte bronnen die niet in "Nog te verwerken bronnen" stonden vermeld.
- **`soorten-kinderopvang.md`** (Rijksoverheid) verwerkt: bronsamenvatting gemaakt, levert "Tussenschoolse opvang" als 4e subtype van [[Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/kinderopvangvoorziening|Kinderopvangvoorziening]] (naast KDV, BSO, Gastouderopvang) — enige subtype zonder recht op kinderopvangtoeslag.
- **`onderwijshuisvesting.md`** (VNG-rubriek, portaalpagina zonder concrete objecten) en **`utrecht-onderwijshuisvesting.md`** (gemeentelijke webpagina, feitelijk overlappend met de al verwerkte, rijkere Beleidsnota Onderwijshuisvesting Utrecht 2026-2041 — zelfde leerlingenprognose, opheffingsnorm, multifunctioneel-gebruik-thema's) → verplaatst naar `Sources/Onderwerpen/Onderwijs/Niet-relevant/`.
- **Bijgewerkt:** `Wiki/Bedrijfsobjecten/4-onderwijs/onderwijs/kinderopvangvoorziening.md` (subtype toegevoegd aan frontmatter en body), `Wiki/Onderwerpoverzichten/onderwijs.md` (`bronnen_count` 10→11, "Nog te verwerken" sectie met de 3 bronnen aangevuld, conclusie, `status` in-behandeling→afgerond), `Wiki/index.md` (§Domeinen — ook stale BO-telling 10→11 gecorrigeerd, §Onderwijs-bronsamenvattingen, kinderopvangvoorziening-subtype).

## [2026-09-23] fix | sport-en-bewegen afgerond: Zwembad-positionering opgelost via Sportpark/Binnenlocatie-precedent

- **Aanleiding:** domein had 1 open modelvraag: is Zwembad een specialisatie van Sportlocatie of een zelfstandig objecttype? Zwembad's eigen pagina beschreef zichzelf al als "vergelijkbaar met Binnenlocatie en Sportpark qua rol in het sportdomein" zonder de vraag af te maken.
- **Opgelost:** Zwembad vastgelegd als derde specialisatie van Sportlocatie — zelfde generalisatie-patroon als de twee al bestaande specialisaties (Sportpark, Binnenlocatie), geen aanwijsbaar structureel verschil gevonden dat een zelfstandig objecttype zou rechtvaardigen.
- **Bijgewerkt:** `zwembad.md` (generalisatie-relatie naar Sportlocatie toegevoegd, terugmelding aangescherpt), `sportlocatie.md` (Zwembad toegevoegd aan Specialisaties-tabel en bo_relaties), `Wiki/Onderwerpoverzichten/sport-en-bewegen.md` (open vraag opgelost, conclusie, `status` in-behandeling→afgerond), `Wiki/index.md` (§Domeinen).

## [2026-09-23] fix | sociaal-domein afgerond: geen wijzigingen nodig, alleen status gecorrigeerd

- **Aanleiding:** domein had 1 bron volledig verwerkt (16 subtypes onder 1 overkoepelend BO), 11 dunne bronnen terecht als niet-relevant weggezet, geen blokkerende open vragen. De 4 gesuggereerde toekomstige bronnen (sportnota, Wmo-beleidsplan, cultuurvisie, onderwijsagenda) hebben geen concrete URL — geen fetch-actie mogelijk, blijft vooruitkijkende suggestie.
- **Bijgewerkt:** `Wiki/Onderwerpoverzichten/sociaal-domein.md` (`status` in-behandeling→afgerond, conclusie), `Wiki/index.md` (§Domeinen).

## [2026-09-23] fix | geluid afgerond: 3 ontbrekende GGM-terugmeldingen alsnog ingediend

- **Aanleiding:** domein had 5 BO's en 2 bronnen volledig verwerkt, maar "Openstaande vragen" liet een onafgemaakte analyse zien: 4 BO's (Geluidbron, Geluidgevoelig gebouw, Stil gebied, Geluidzone) waren op hun eigen pagina al gemarkeerd "potentieel hiaat, nader te beoordelen" zonder dat de beoordeling ooit werd afgemaakt — terwijl de begrippentabel zelf al `Data-object: ja` had vastgesteld voor alle 4, wat volgens `/write-element` Stap 10 een terugmelding als hiaat impliceert.
- **Afgerond volgens de regel:** Geluidbron, Geluidgevoelig gebouw en Stil gebied teruggemeld als #103–105. Geluidzone bleek al gedekt door de bestaande structurele terugmelding #43 (ontbrekend generiek Zone-concept, samen met milieuzones/rookvrije zones/vuurwerkvrije zones) — pagina verwijst er nu naar in plaats van een eigen "nader te beoordelen".
- **Bijgewerkt:** 4 BO-pagina's (Terugmelding GGM-sectie), `Wiki/Analyses/ggm-terugmeldingen.md` (#103–105), `Wiki/Onderwerpoverzichten/geluid.md` (openstaande vraag opgelost, conclusie, `status` in-behandeling→afgerond), `Wiki/index.md` (§Domeinen).

## [2026-09-23] fix | Wonen afgerond: Standplaats (BAG) alsnog cross-gelinkt, dode woonboot-link gerepareerd

- **Aanleiding:** systematische sync-check (script, cross_tag `onderwerp:`-veld tegen begrippentabel-links) over alle resterende "in-behandeling"-domeinen naar aanleiding van de dienstverlening-bevinding hierboven.
- **Gevonden:** [[Wiki/Bedrijfsobjecten/99-kern/bag/standplaats|Standplaats (BAG)]] is cross-getagd `onderwerp: [Basisregistraties, BAG, Wonen]` maar stond niet in de wonen-begrippentabel, terwijl het qua patroon identiek is aan [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/ligplaats|Ligplaats]] (dezelfde cross-tag-constructie), dat wél al stond. Toegevoegd.
- **Los gevonden en gerepareerd:** `Wiki/index.md` §Wonen — Woonboten verwees naar het niet-bestaande pad `vth/woonboot`; de pagina heet sinds de eerdere Woonboot→Vaartuig-hernoeming (precedent [BO6], 2026-07-09) `vth/vaartuig`. Link gecorrigeerd, Ligplaats en Standplaats (BAG) als cross-referenties toegevoegd voor consistentie met wonen.md.
- **Overige 10 "in-behandeling"-domeinen (geluid, informatiebeheer, informatiesamenleving, milieu, mobiliteit, omgevingswet, onderwijs, sociaal-domein, sport-en-bewegen, werk-en-inkomen) gecontroleerd met hetzelfde script: geen sync-gaps gevonden** — alle BO-bestanden met een matchend `onderwerp:`-veld staan al correct gelinkt in hun eigen onderwerpoverzicht.
- **Bijgewerkt:** `Wiki/Onderwerpoverzichten/wonen.md` (nieuwe rij, `bo_count` 5→6, `begrippen_count` 31→32, `bronnen_count` 9→10 correctie, `status` in-behandeling→afgerond, "Nog te verwerken" opgeschoond, conclusie), `Wiki/index.md` (§Domeinen, §Wonen — Woonboten link gefixt).

## [2026-09-23] fix | Dienstverlening afgerond: sync-gap gedicht, 3 bestaande BO's alsnog opgenomen in begrippentabel

- **Aanleiding:** bij het afronden van de "in-behandeling"-domeinen bleek de map `Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/` 22 BO-bestanden te bevatten terwijl de onderwerpoverzicht-tabel er maar 13 noemde (`bo_count: 13`).
- **Analyse:** 8 van de 9 ontbrekende bestanden (algoritmeregister, datalek, dpia, grondrechteneffectbeoordeling, verwerkersovereenkomst, verwerkingsactiviteit, informatieobject) horen inhoudelijk bij Informatiesamenleving resp. Informatiebeheer (`onderwerp:`-veld) en staan daar al correct in de eigen begrippentabel — terecht niet dubbel opgenomen. 3 hoorden wél (mede) bij dit domein en ontbraken hier volledig: [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/vergunningen-en-ontheffingen|Vergunningen en ontheffingen]] (`onderwerp: [dienstverlening]`, nooit opgenomen), [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/woo-verzoek|Woo-verzoek]] en [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/klacht|Klacht]] (beide cross-getagd `[informatiesamenleving, dienstverlening]`).
- **Openstaande vragen:** 3 vooruitkijkende onderzoeksnotities (ZTC2/RGBZ-standaardevolutie, toekomstige klantbeoordelingsbronnen) — geen blokkerende BO-classificatievraag, blijven gedocumenteerd.
- **Bijgewerkt:** `Wiki/Onderwerpoverzichten/dienstverlening.md` (3 nieuwe rijen in beide tabellen, `bo_count` 13→16, `begrippen_count` 27→30, `status` in-behandeling→afgerond, conclusie), `Wiki/index.md` (§Domeinen, kleine opschoning dubbele regel in §Dienstverlening).

## [2026-09-23] ingest | Basisregistraties afgerond: BGT-gegevenscatalogus verwerkt, 13 nieuwe BO's, 1 homoniem + 2 duplicaten gemeld

- **Aanleiding:** domein basisregistraties had een gedocumenteerde hiaat: BGT (Basisregistratie Grootschalige Topografie) had nog geen bronbestand. Gebruiker gekozen: BGT ophalen (RSGBPlus-overige-entiteiten blijft openstaand, geen geschikte bron bekend).
- **Bron opgehaald:** `Sources/Standaarden/catalogus-bgt-1.2.md` (Geonovum, Gegevenscatalogus BGT 1.2, via `curl`), bronsamenvatting `Wiki/Bronsamenvattingen/Standaarden/catalogus-bgt-1.2.md`.
- **18 objecttypen beoordeeld**, 14 BO's (13 nieuw, Pand al bestaand via BAG):
  - **11 nieuw in `Wiki/Bedrijfsobjecten/99-kern/bgt/`:** Wegdeel, OndersteunendWegdeel, Spoorbaan, OnbegroeidTerreindeel, BegroeidTerreindeel, Waterdeel, OndersteunendWaterdeel, OverigBouwwerk, Overbruggingsdeel, Tunneldeel, Kunstwerkdeel — alle exacte RSGBPlus-matches.
  - **2 nieuw in `Wiki/Bedrijfsobjecten/.../beheer-openbare-ruimte/`:** Scheiding en Functioneel gebied — GGM-duplicaten tussen RSGBPlus (BGT) en Beheer Openbare Ruimte (IMBOR) met identieke definitie, geen van beide had al een BO-pagina. Gebruiker gekozen: Beheer Openbare Ruimte als primair beleidsdomein (beheercontext). Functioneel gebied bleek de al langer impliciete GGM-generalisatie-parent van het bestaande BO [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/speelterrein|Speelterrein]] (voorheen ongelinkte platte tekst "FunctioneelGebied (GGM)"); die relatie nu naar een echte wiki-link omgezet.
  - **4 geen BO** (abstract of geen zelfstandige bedrijfsbetekenis): IMGeo-Object, OverigeConstructie (beide abstract), OpenbareRuimteLabel (cartografisch label van bestaande BO Openbare Ruimte), Plaatsbepalingspunt (meettechnisch kwaliteitsobject).
- **Homoniem (gebruiker gekozen):** GGM-naam "Spoor" bestaat ook in Archeologie ("blijk van eerdere aanwezigheid", nog niet ge-ingest) — RSGBPlus-kant vastgelegd als **Spoorbaan** i.p.v. "Spoor", gedisambigueerd via `## Naamkeuze`. Gemeld als #102 (signaal, Archeologie-kant volgt later).
- **Terugmeldingen #100/#101 (duplicaat):** Scheiding en Functioneel gebied.
- **Bijgewerkt:** `Wiki/Onderwerpoverzichten/basisregistraties.md` (nieuwe §BGT in begrippentabel, `bo_count` 26→39, `begrippen_count` 57→75, `bronnen_count` 6→8, `status` in-behandeling→afgerond, openstaande vragen opgelost, conclusie toegevoegd), `Wiki/Onderwerpoverzichten/beheer-openbare-ruimte.md` (2 nieuwe begrippen, `bo_count` 9→11, `begrippen_count` 37→39, blijft `in-behandeling` — 192 onbeoordeelde entiteiten resteren, ongerelateerd aan deze toevoeging), `Wiki/index.md` (§Domeinen ×2, nieuwe §Basisregistraties — BGT, 2 nieuwe rijen Beheer Openbare Ruimte, nieuwe bronsamenvatting-rij).

## [2026-09-23] fix | Arbeidszaken: status gecorrigeerd naar afgerond, geen inhoudelijke wijzigingen

- **Aanleiding:** gebruiker liet de "in-behandeling"-domeinen één voor één afronden. Alle 12 bronnen in `Sources/Onderwerpen/Arbeidszaken/` hebben al een bronsamenvatting, alle 12 BO-kandidaten hebben al een BO-pagina, geen "ter discussie"/open-vraag-markeringen aangetroffen, en het overzicht had al een uitgewerkte Conclusie-sectie. Alleen het statusveld liep achter.
- **Bijgewerkt:** `Wiki/Onderwerpoverzichten/arbeidszaken.md` (`in behandeling` → `afgerond`), `Wiki/index.md` (§Domeinen).

## [2026-09-23] ingest | Dierenwelzijn afgerond: soortenmanagementplan herbeoordeeld en vastgelegd als BO (5e BO), GGM-hiaat gemeld

- **Aanleiding:** gebruiker liet de "in-behandeling"-domeinen één voor één afronden. Dierenwelzijn had 1/1 bronnen al verwerkt, maar één open vraag blokkeerde afronding: soortenmanagementplan stond in `Wiki/Onderwerpoverzichten/dierenwelzijn.md` als "instrument, 6/6 criteria maar type=instrument → ter discussie", terwijl dezelfde log (eerdere ingest-run) het juist als niet-BO had geclassificeerd — tegenstrijdige, niet onderbouwde documentatie, geen van beide met een zichtbare per-criterium toetsing.
- **Herbeoordeeld** op de 6 BO-criteria (zie [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/dierenwelzijn/soortenmanagementplan|Soortenmanagementplan]]): 6/6, op basis van `2019-nota-dierenwelzijn.md` én `Sources/Onderwerpen/Beheer Openbare Ruimte/factsheet-informatiebronnen-natuur-groen.md` (soortenmanagementplan ook provinciebreed gebruikt als vergunningsbasis bij na-isolatieprojecten, niet alleen het Utrechtse MGP-plan). Uitkomst voorgelegd aan en bevestigd door gebruiker.
- **BO aangemaakt:** `Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/dierenwelzijn/soortenmanagementplan.md`, grondslag `governance-object`, geen GGM-match.
- **GGM-hiaat gemeld:** #99 in `Wiki/Analyses/ggm-terugmeldingen.md` — GGM kent geen entiteit voor een natuurbeschermings-/soortenmanagementinstrument.
- **Bijgewerkt:** `Wiki/Onderwerpoverzichten/dierenwelzijn.md` (begrippentabel, `bo_count` 4→5, `status` in-behandeling→afgerond, openstaande vraag opgelost, conclusie toegevoegd), `Wiki/index.md` (§Domeinen, §Bedrijfsobjecten/Dierenwelzijn).

## [2026-09-23] fix | Onderwerp Asiel en Integratie: stale backlog-checkboxes en status gecorrigeerd, geen nieuwe bronnen

- **Aanleiding:** `/ingest Asiel en Integratie` aangeroepen. Stap 1 (bronnen identificeren) liet zien dat alle 7 bronnen in `Sources/Onderwerpen/Asiel en Integratie/` + de 2 bronnen in `Sources/Onderwerpen/Inburgering en Asielopvang/` (waarheen 2 ervan bij de eerdere reorganisatie waren verplaatst, zie eerdere log-entry over de 37-bestanden-move) al een bronsamenvatting hadden en al in de begrippentabel van `Wiki/Onderwerpoverzichten/asiel-en-integratie.md` waren verwerkt ("Nog te verwerken bronnen: (geen)"). Geen nieuwe bron om te verwerken.
- **`ToDo/ingest-backlog.md` was niet bijgewerkt** na die eerdere ingest-rondes: 6 van de 7 bronnen stonden nog als `[ ]` terwijl ze allang waren verwerkt. Alle 7 afgevinkt met verwijzing naar hun bronsamenvatting; sectie gemarkeerd als afgerond.
- **Status gecorrigeerd:** `Wiki/Onderwerpoverzichten/asiel-en-integratie.md` (`in-behandeling` → `afgerond`) en `Wiki/index.md` (§Domeinen) — het domein was inhoudelijk al compleet (17 BO's, 43 begrippen, 88% GGM-dekking, 0 BO-hiaten, vastgesteld in een eerdere GGM-vergelijkingsanalyse, zie log-entry [2026-06-28]), alleen de statusvelden liepen achter. **Opgemerkt maar niet opgelost:** die eerdere entry verwijst naar `Wiki/Analyses/ggm-vergelijking/ggm-vergelijking-asiel-en-integratie`, een bestand dat niet (meer) bestaat — buiten scope van deze correctie, gebruiker attenderen.
- Geen wijzigingen aan bronsamenvattingen, BO-pagina's of de begrippentabel zelf — puur een synchronisatie van boekhouding met de al bestaande, juiste inhoud.

## [2026-09-23] ingest | Onderwerp Recht afgerond: 3 nieuwe BO's (Subsidie-domein), GGM-hiaat opgelost

- **Bronnen:** 9 VNG-rubriekpagina's in `Sources/Onderwerpen/Recht/` verwerkt. 5 te dun bevonden (geen concrete objecten/attributen, puur portaal/navigatie) en verplaatst naar `Sources/Onderwerpen/Recht/Niet-relevant/`: `algemene-wet-bestuursrecht-awb`, `algemene-plaatselijke-verordening-apv`, `modelverordeningen`, `rubriek-recht`, `portal-overheidsprivaatrecht`. 4 bronsamenvattingen aangemaakt in `Wiki/Bronsamenvattingen/Recht/`: `subsidierecht`, `overeenkomsten`, `overheidsaansprakelijkheid`, `gemeentewet`.
- **Nieuw beleidsdomein Subsidies (GGM taakveld 9 Interne Organisatie) opgepakt:** `subsidierecht.md` bevestigde een al gesignaleerde hiaat (`Wiki/Analyses/entiteitendekking/9-interne-organisatie`: "Subsidies opvallend zonder BO ondanks schijndekking"). 3 BO's aangemaakt in `Wiki/Bedrijfsobjecten/9-interne-organisatie/subsidies/`, alle met exacte GGM-match: **Subsidie**, **Subsidieaanvraag**, **Subsidiebeschikking** (6/6 criteria elk). GGM-entiteiten Subsidieprogramma, Subsidiecomponent en de enumeratie Subsidieniveau bewust niet vastgelegd — geen brongrond in deze dunne bron; gesignaleerd voor een toekomstige rijkere subsidierecht-bron.
- **Homoniem-signaal gedocumenteerd (geen actie):** GGM-naam "Beschikking" komt ook voor in de beleidsdomeinen Generiek Jeugd en Wmo en Diensten; Subsidiebeschikking is een aparte, eigen GGM-entiteit zonder generalisatierelatie — geen naamcollisie omdat de BO-naam al disambiguerend is.
- **Overeenkomsten/Overheidsaansprakelijkheid/Gemeentewet:** 0 nieuwe BO's. Overeenkomst-concepten zijn al gedekt per contractsoort ([[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/contract|Contract]] e.a.); GIBIT is al rijk geïngest onder onderwerp Informatiesystemen; overheidsaansprakelijkheid betreft juridische toetsingscriteria, geen registreerbare objecten; de Gemeentewet-rubriekpagina is inhoudelijk een dunnere versie van de al eerder verwerkte volledige wettekst (`Wiki/Bronsamenvattingen/Bestuur/gemeentewet-wettekst`, met Raadsstuk/Vergadering/Stemming) — het genoemde "recht om vragen te stellen aan het college" bleek daar al vastgelegd als subtype **Raadsvraag** van Raadsstuk.
- **Bijgewerkt:** `Wiki/Onderwerpoverzichten/recht.md` (nieuw, status afgerond), `Wiki/index.md` (§Domeinen, nieuwe §Subsidies onder Bedrijfsobjecten, nieuwe §Recht onder Bronsamenvattingen), `Bedrijfsarchitectuur/ToDo/ingest-backlog.md` (Recht-sectie afgevinkt).

## [2026-09-23] fix | 4 misgeplaatste erfgoed-bronsamenvattingen verplaatst van `Bronsamenvattingen/Cultuur/` naar `Bronsamenvattingen/erfgoed/`

- **Aanleiding:** gebruiker signaleerde dat `Sources/Onderwerpen/erfgoed/` meer documenten (8) bevat dan `Wiki/Bronsamenvattingen/erfgoed/` samenvattingen (4). Analyse: de bronsamenvattingen bestonden wél, maar waren tijdens de gebundelde Cultuur/erfgoed-ingest onder `onderwerp`/`domein` "Cultuur" weggeschreven i.p.v. "erfgoed", terwijl hun bronbestanden alleen in `Sources/Onderwerpen/erfgoed/` staan.
- **Verplaatst (`git mv`):** `archiefverordening-wageningen.md`, `memorie-van-toelichting-archiefwet.md`, `visie-religieus-erfgoed-2025.md`, `bijlagen-visie-religieus-erfgoed.md` → `Wiki/Bronsamenvattingen/erfgoed/`.
- **Frontmatter gecorrigeerd:** veldnaam `domein:` → `onderwerp:` (template-conform) op de 2 visie-bestanden; `onderwerp: [Cultuur, Informatiebeheer]` → `[erfgoed, Informatiebeheer]` op de 2 archiefwet-bestanden.
- **Bronformaat gecorrigeerd:** de 4 al aanwezige erfgoed-bronsamenvattingen (`erfgoedwet.md`, `gr-regionaal-archief-rivierenland.md`, `besluit-informatiebeheer-gr-cure.md`, `beleidsplan-westfries-archief.md`) hadden een platte-tekst `## Bronnen`-regel i.p.v. `[[Sources/...]]`-wiki-link — dit was de reden dat `tools/lint_checks.py` alle 6 relevante erfgoed-bronnen als "orphan" meldde (regex matcht alleen `[[Sources/...]]`). Omgezet naar wiki-link.
- **Alle referrers bijgewerkt** (14 regels in 9 bestanden): `Wiki/index.md`, `Wiki/Onderwerpoverzichten/cultuur.md`, 4 BO-pagina's (`archiefstuk.md`, `orgel.md`, `monument.md`, `document.md`, `informatieobject.md`), `Wiki/Bronsamenvattingen/Cultuur/erfgoedbeleid-utrecht.md`.
- **`Wiki/index.md` aangevuld:** de 4 al langer bestaande erfgoed-bronsamenvattingen (`archiefverordening-wageningen`, `memorie-van-toelichting-archiefwet`, `erfgoedwet`, `gr-regionaal-archief-rivierenland`, `besluit-informatiebeheer-gr-cure`, `beleidsplan-westfries-archief`) stonden er nooit in — toegevoegd onder §Domeinen/Cultuur.
- **Niet opgelost (buiten scope PR1):** `visie-religieus-erfgoed-2025.md` en `bijlagen-visie-religieus-erfgoed.md` bestaan als identieke bronbestanden in zowel `Sources/Onderwerpen/Cultuur/` als `Sources/Onderwerpen/erfgoed/` (duplicatie ontstaan tijdens de gebundelde ingest). `Sources/` is read-only ([PR1]) — niet opgeschoond. De Cultuur-kopieën zijn nu de "orphan" kant in lint (voorheen de erfgoed-kopieën); gebruiker moet beslissen welke kopie canoniek is.
- **Bredere check + gefixt:** dezelfde map-naam-mismatch (case-only, inhoudelijk niet fout maar rommelig) gevonden bij 5 andere onderwerpen: `Wiki/Bronsamenvattingen/onderwijs` → `Onderwijs`, `Dierenwelzijn` → `dierenwelzijn`, `Evenementen` → `evenementen`, `Informatiebeheer` → `informatiebeheer`, `Informatiesystemen` → `informatiesystemen` (map hernoemd naar de `Sources/Onderwerpen`-schrijfwijze, 48 referrer-bestanden bijgewerkt). Bewust NIET aangepast: `onderwerp:`/`domein:`-veldwaarden in de frontmatter van bestanden in deze mappen (aparte, kleinere inconsistentie, buiten scope van deze mapnaam-fix).
- **Lint uitgebreid** (`tools/lint_checks.py`, met goedkeuring): 2 nieuwe checks in het wiki-brede blok van `main()`:
  - `check_plain_text_source_refs()` → "Sources-referentie in ## Bronnen niet als wiki-link": signaleert toekomstige platte-tekst `Sources/Onderwerpen/...`-vermeldingen (zonder `[[ ]]`) in een bronsamenvatting — dit was de directe oorzaak dat 4 al-correct-geplaatste erfgoed-bronsamenvattingen toch als "orphan source" werden gemeld.
  - `check_topic_folder_casing()` → "Sources/Onderwerpen- vs Bronsamenvattingen-map: hoofdletter-mismatch": signaleert precies dit soort case-only mapnaam-drift. Bewust NIET een botte "map ≠ Sources-map"-check: ~35 bestaande, bewuste onderwerp-herindelingen (zie `ToDo/ingest-backlog.md`, bv. "Ruimte Wonen en Mobiliteit" → `mobiliteit`/`Wonen`/`Welstand`/`Beheer Openbare Ruimte`) zouden dan als valse bevindingen verschijnen.
  - `.claude/commands/lint.md` §Stap 1-dekkingslijst bijgewerkt met beide checks.
- **Bronduplicaten verwijderd (expliciete uitzondering op [PR1], op verzoek gebruiker):** 4 identieke bronbestand-paren gevonden (md5-vergelijking over heel `Sources/Onderwerpen/`), ontstaan tijdens de gebundelde Cultuur/erfgoed-ingest. Per paar de niet-gerefereerde kopie verwijderd, canonieke kopie behouden:
  - `visie-religieus-erfgoed-2025.md`: `Cultuur/`-kopie verwijderd, `erfgoed/`-kopie behouden (bronsamenvatting wijst hiernaar).
  - `bijlagen-visie-religieus-erfgoed.md`: idem.
  - `Niet-relevant/lijst-beeldbepalende-panden.md`: `Cultuur/Niet-relevant/`-kopie verwijderd, `erfgoed/Niet-relevant/`-kopie behouden (hoort bij erfgoed's eigen ingest-batch, zie `ToDo/ingest-backlog.md` regel 81).
  - `Niet-relevant/erfgoedbeleid-utrecht.md`: `erfgoed/Niet-relevant/`-kopie verwijderd, `Cultuur/`-kopie (top-level, wél relevant, heeft eigen bronsamenvatting) behouden.
  - Vooraf geverifieerd dat geen enkele wiki-pagina naar de te verwijderen kopieën linkte.
- **Sources/ heringedeeld naar de bronsamenvatting-indeling (2e ronde, expliciete uitzondering op [PR1], op verzoek gebruiker):** de ~35 gerapporteerde map-mismatches (bronsamenvatting-map ≠ Sources-map) bleken bij exacte resolutie 37 individuele bronbestanden, verspreid over 12 doelmappen. Alle bewust bewaard onder hun oorspronkelijke VNG-onderwerpnaam terwijl de bijbehorende bronsamenvatting allang naar een fijnmaziger onderwerp was verplaatst — precies dezelfde bug als de erfgoed-fix, nu structureel voor alle bewuste herindelingen. Aanpak:
  1. Script gebouwd dat voor elke bronsamenvatting de `[[Sources/Onderwerpen/{topic}/...]]`-referenties uitleest en vergelijkt met de eigen map; 37 unieke bronpaden gevonden, 0 conflicten (geen bron door twee verschillende doelmappen gerefereerd).
  2. 37 bronbestanden + 12 bijbehorende PDF-sidecars (in `converted_pdf/`) verplaatst met `git mv`: `Ruimte Wonen en Mobiliteit/` → `mobiliteit/` (12), `Wonen/` (10), `Welstand/` (2), `Beheer Openbare Ruimte/` (7); `Milieu/` → `Beheer Openbare Ruimte/` (2); `goederenvervoer/` → `mobiliteit/` (2, incl. pdf); `Asiel en Integratie/` → `Inburgering en Asielopvang/` (2); `Recht/` → `Bestuur/` (1, gemeentewet-wettekst); `Dienstverlening/` → `Standaarden/` (1, ztc2-begeleidend-document).
  3. Alle referenties naar de oude paden wiki-breed vervangen (39 bestanden, incl. historische `Wiki/log.md`-entries die naar deze paden verwezen).
  4. Oorspronkelijke VNG-onderwerpmappen (`Ruimte Wonen en Mobiliteit/`, `goederenvervoer/`, `Recht/`, `Asiel en Integratie/`, `Dienstverlening/`, `Milieu/`) blijven bestaan met hun resterende, nog niet aan een fijnmaziger onderwerp toegewezen of `Niet-relevant/`-bronnen — dit is geen opschoning van die mappen, alleen van de 37 bestanden die al wél via een bronsamenvatting aan een ander onderwerp waren toegewezen.
  - **Verificatie:** `python3 tools/lint_checks.py` — 0 dode Sources-links, 0 hoofdletter-mismatches, 0 platte-tekst Sources-referenties, geen resterende verwijzing naar een van de 37 oude paden (script-gecontroleerd over heel `Wiki/`), totaal 1511 bevindingen (ongewijzigd t.o.v. voor de reorganisatie — geen regressie, geen nieuwe orphans).
- **`Ruimte Wonen en Mobiliteit/` en `goederenvervoer/` volledig verwijderd** (op verzoek gebruiker, na bevestiging dat dit — anders dan `Recht/`, `Asiel en Integratie/`, `Dienstverlening/`, `Milieu/` — de enige 2 mappen zijn die volledig afgehandeld zijn zonder nog niet-verwerkt brongmateriaal). Voor het verwijderen alle resterende inhoud herverdeeld:
  - **Duplicaat verwijderd:** `converted_pdf/mobiliteitsplan-2040.md`+`.pdf` bleek een tweede, identieke fetch van dezelfde PDF (md5-gelijk) als de al eerder verplaatste `mobiliteit/converted_pdf/mobiliteitsplan-2040.md` — orphan-kopie verwijderd, canonieke (gerefereerde) kopie behouden.
  - **28 bestanden herverdeeld** naar `Niet-relevant/` en `converted_pdf/` van `mobiliteit/`, `Wonen/`, `Welstand/` en `Beheer Openbare Ruimte/` — inhoudelijk geclassificeerd op basis van titel/onderwerp (bv. `welstandsbeleid.md`/`welstandsnota-utrecht.md` → `Welstand/Niet-relevant/`; `bouwen-en-wonen.md`/`ruimtelijke-ordening.md`/`bouwregelgeving.md` → `Wonen/Niet-relevant/`; `klimaatadaptatie-en-water.md`/`landelijk-gebied.md`/`speelruimtebeleid-utrecht.md` → `Beheer Openbare Ruimte/Niet-relevant/`; `parkeerbeleid-utrecht.md`/`rubriek-ruimte-wonen-en-mobiliteit.md`/`beleid-goederenvervoer-utrecht.md` (uit `goederenvervoer/`) → `mobiliteit/Niet-relevant/`). PDF-sidecars uit `converted_pdf/` meeverplaatst naar de `converted_pdf/`-map van het nieuwe onderwerp, ook als het bijbehorende `.md`-bestand in `Niet-relevant/` landde (zelfde patroon als bij de eerdere 37-bestanden-move).
  - `mobiliteit.md` (top-level, nooit getrieerd VNG-rubriekpagina, ongerefereerd) ongewijzigd qua status verplaatst naar `mobiliteit/mobiliteit.md`.
  - Losse classificatiekeuzes zijn editorial (geen bronsamenvatting om op te varen, want Niet-relevant) — bij twijfel later eenvoudig te herzien via `git mv`.
  - Beide brondmappen waren na deze stap leeg en zijn verwijderd; geverifieerd dat nergens in `Wiki/` nog naar het oude pad wordt gelinkt (1 historische, beschrijvende vermelding in een oude `log.md`-entry bewust ongemoeid gelaten — feitelijk juist op het moment van schrijven).
  - **Verificatie:** `python3 tools/lint_checks.py` — 0 dode links, 0 hoofdletter-mismatches, totaal 1510 (1 minder dan hiervoor door de verwijderde duplicaat-orphan).

## [2026-09-23] bo | Herbeoordeling 6 `/audit-actoren track 1`-BO's: relaties toegevoegd, analyse-bron verwijderd

- **Aanleiding:** gebruiker corrigeerde de vorige triage-entry — een verwijzing naar `Wiki/Analyses/entiteitendekking/...` in `## Bronnen` is geen bron (kan een trigger zijn om een bron te zoeken, maar zelf geen brondocument). Ik had deze regel laten staan naast de nieuw gekoppelde bron in 6 BO's (Opdrachtgever, Opdrachtnemer, Raadslid, Collegelid, Aanwezige Deelnemer, Contactpersoon).
- **Analyse-regel verwijderd** uit alle 6 pagina's — elk heeft nu uitsluitend een echte bronsamenvatting in `## Bronnen`.
- **Erkend:** het toevoegen van een bron aan een al bestaande, `/audit-actoren`-afgeleide BO-pagina was geen volledige `/ingest`/`/element-pipeline`-doorloop — alleen een bronverwijzing. Op verzoek alsnog een herbeoordeling gedaan: GGM-relaties opgezocht in `ggm_parsed.json` per GUID en verwerkt in `bo_relaties`-frontmatter + nieuwe `## Relaties`-secties:
  - Opdrachtgever ↔ Doelstelling/Product, Opdrachtnemer ↔ Kostenplaats/Product (Financiën-taakveld, wederkerigheid met BW art. 400-413 toegelicht in proza, GGM modelleert dit niet als eigen relatie tussen Opdrachtgever/Opdrachtnemer zelf).
  - Raadslid ↔ Aanwezige Deelnemer/Raadscommissie/Indiener; Collegelid ↔ Aanwezige Deelnemer/Indiener; Aanwezige Deelnemer ↔ Vergadering/Raadslid/Collegelid (Griffie-domein, wederzijds op alle 3 pagina's vastgelegd).
  - Contactpersoon: relatie naar Schuldhulporganisatie gedocumenteerd als open punt (geen wiki-pagina, niet aangemaakt in deze sessie).
- **Bijvangst — 2 al langer bestaande, ongeregistreerde bevindingen alsnog vastgelegd terwijl deze pagina's toch open stonden:**
  - Contactpersoon had al een `ggm_duplicaat_entiteiten`-vermelding (Schuldhulpverlening vs. Vroegsignalering) zonder de vereiste `## GGM-duplicaten`-sectie en zonder terugmelding — sectie toegevoegd, geregistreerd als #97 in [[Wiki/Analyses/ggm-terugmeldingen]].
  - Informatieobject had al een uitgewerkte `### Terugmelding GGM`-paragraaf (GGM-hiaat tussen Document en Archiefstuk) die nooit als formele regel was geregistreerd — toegevoegd als #98.
- **Bewust niet gedaan:** generalisatie Raadslid/Collegelid → Ingezetene en relatie Aanwezige Deelnemer → NatuurlijkPersoon (beide zonder eigen wiki-pagina) alleen als open punt genoteerd in de body — geen nieuwe elementen aangemaakt (dat is een aparte `/assess-element`-beoordeling, buiten scope van deze herbeoordeling).
- **Verificatie:** YAML-parse OK op alle 6 + de 2 bijvangst-pagina's; `python3 tools/lint_checks.py` 1519 → 1516 (2 nieuw geïntroduceerde "wiki-link zonder alias"-bevindingen uit eigen toevoegingen meteen zelf gecorrigeerd, geen regressie).

## [2026-09-23] fix | Triage van de 2 nieuwe lint-checks: 28 bevindingen naar 0

- **Aanleiding:** vervolg op de vorige entry van vandaag — de twee nieuwe checks (`check_traceability_naar_bron`, `check_bronsamenvatting_verwerkt`) leverden bij hun eerste run 18 resp. 10 bevindingen op. Gebruiker vroeg om deze te triageren i.p.v. ongetriageerd te laten staan.
- **Formatteringsfouten hersteld (geen inhoudelijke wijziging):** `Wiki/Bronsamenvattingen/Inkoop/inkoop-en-aanbestedingsbeleid.md` gebruikte platte tekst i.p.v. `[[wiki-link]]` in `## Bronnen` (loste 7 bevindingen op); 3 bronbestanden in `Wiki/Bronsamenvattingen/Milieu/` hadden een foutieve naam met spatie+"1" (`beleidsnota-stadswater 1.md` e.d.) — hernoemd naar de correcte VR1-conforme naam, alle 6 verwijzende bestanden + `Wiki/index.md` bijgewerkt (loste 3+3 bevindingen op); `kinderopvangvoorziening` stond wel in `onderwijs.md` maar zonder wiki-link — hersteld.
- **Ontbrekende tabelrijen toegevoegd (BO bestond al, nooit in begrippentabel gezet):** Aanwezige Deelnemer (`bestuur.md`), Opdrachtgever + Opdrachtnemer (`financien.md`), Contactpersoon (`schulden-en-armoede.md`) — telkens in het bestaande rol/BO-tegenhanger-patroon (vgl. Raadslid/Collegelid in `bestuur.md`).
- **Ontbrekend onderwerpoverzicht aangemaakt:** `Wiki/Onderwerpoverzichten/informatiebeheer.md` bestond nog helemaal niet, terwijl er al 3 BO's (Document, Informatieobject, Archiefstuk), 3 rollen (Archiefvormer, Archivaris, Archiefinspecteur) en 1 bronsamenvatting (Overheidsinformatiemodel) met `onderwerp: [Informatiebeheer]` bestonden. Aangemaakt volgens `templates/onderwerpoverzicht.md`, opgenomen in `Wiki/index.md` §Domeinen.
- **6 BO's uit `/audit-actoren track 1` zonder beleidsbron:** hun `## Bronnen`-sectie linkte alleen naar een entiteitendekking-rapport (GGM-signaal, geen bron). Voor Raadslid (art. 7-15), Collegelid (art. 34-41b) en Aanwezige Deelnemer (art. 17-24, vergadering) bleek de al aanwezige bronsamenvatting `Wiki/Bronsamenvattingen/Bestuur/gemeentewet-wettekst.md` de juiste, nooit gekoppelde bron. Voor Contactpersoon bleek RGBZ 1.0 (`Wiki/Bronsamenvattingen/Standaarden/rgbz-informatiemodel.md`) — geverifieerd met een citaat uit `Sources/Standaarden/rgbz-1.0.md` dat Contactpersoon expliciet als rol met naam/functie/telefoon/e-mail definieert — de juiste bron.
- **Nieuwe bron opgehaald voor Opdrachtgever/Opdrachtnemer:** geen bestaande bron dekte deze BW-contractrollen. Via `/fetch`-werkwijze (curl, wetten.overheid.nl) `Sources/Onderwerpen/Financien/bw7-titel7-afdeling1-opdracht.md` opgehaald — BW Boek 7, Titel 7, Afdeling 1 (art. 400-413), bewust afgebakend tot alleen deze afdeling (niet heel Titel 7, dat ook geneeskundige behandeling/reisovereenkomst/arbeidsbemiddeling bevat — buiten scope). Nieuwe bronsamenvatting `Wiki/Bronsamenvattingen/Financien/bw7-opdracht.md` aangemaakt, gekoppeld aan beide BO's en aan `financien.md`.
- **3 Werk en Inkomen-bronsamenvattingen** (waaronder `participatiewet.md` zelf) en **2 Bestuur-bronsamenvattingen** (subsidieregeling politieke partijen) + **1 Standaarden-bronsamenvatting** (RSGB, hoort bij `basisregistraties.md`) waren al lang verwerkt maar nooit aan de bronnenlijst van het bijbehorende onderwerpoverzicht toegevoegd — toegevoegd.
- **Verificatie:** `python3 tools/lint_checks.py --json` — beide nieuwe checks op 0 bevindingen (was 18 en 10), Python-syntaxcheck OK.
- **Bijgewerkt:** `Bedrijfsarchitectuur/ToDo/Structuur en herleidbaarheid.md` (punt 6 en 7 van "opgelost" naar "opgelost én getriageerd", vervolgwerk-tabel bijgewerkt).

## [2026-09-23] structuur | Bedrijfsfunctie/-proces als nieuw elementtype + 2 nieuwe lint-checks (openstaande punten `ToDo/Structuur en herleidbaarheid.md`)

- **Aanleiding:** de 4 openstaande punten uit `Bedrijfsarchitectuur/ToDo/Structuur en herleidbaarheid.md` (na een eerdere status-analyse van dat bestand) via interview met de gebruiker besloten en geïmplementeerd.
- **Besluit 1 (geen actie):** geen expliciete n:n-mappingtabel onderwerp ↔ taakveld/beleidsdomein — bewust impliciet gelaten.
- **Besluit 2 (nieuw elementtype):** `bedrijfsfuncties`/`bedrijfsprocessen` worden volwaardige elementen met eigen pagina, zoals BO/actor/rol: locatie onder taakveld/beleidsdomein (`Wiki/Bedrijfsfuncties/`/`Wiki/Bedrijfsprocessen/`), bron ad hoc (net als BO's), zelfde `/assess-element`+`/write-element`-flow. Gebouwd: nieuwe naslagpagina [[Wiki/GEMMA/functies-en-processen|Bedrijfsfuncties en bedrijfsprocessen]] (definities + 6 diagnostische vragen per type, analoog aan [[Wiki/GEMMA/actoren-en-rollen|Actoren en rollen]]); `templates/element.md` (locaties, `archimate_type: business-function|business-process`, veld-frontmatter van vrije tekst naar verplichte wiki-link); `/assess-element` (begripstypen + Stap 2c); `/write-element` (nieuwe Stap 12); `CLAUDE.md` (§3, §7, [BO12]); `tools/lint_checks.py` (nieuwe mappen in `BO_DIRS`/`VALID_ARCHIMATE_TYPE`/wrong_folder, plus `check_functies_processen_links()`: vrije-tekst- en dode-linkdetectie + wees-pagina's).
- **Besluit 3 (nieuwe check):** `check_bronsamenvatting_verwerkt()` toegevoegd — signaleert bronsamenvattingen die in geen enkel onderwerpoverzicht worden genoemd (analoog aan de bestaande wees-BO-check). Eerste run: 10 bevindingen.
- **Besluit 4 (nieuwe check):** `check_traceability_naar_bron()` toegevoegd — één samengestelde end-to-end signaal per BO ("geen pad naar brondocument"), i.p.v. drie los te combineren deelchecks. Eerste run: 18 bevindingen.
- **Verificatie:** `python3 -c "import ast; ast.parse(...)"` OK, `python3 tools/lint_checks.py --json` draait zonder crash (1554 totaal, inclusief de nieuwe categorieën).
- **Bewust niet (nu) gedaan:** de 1296 bestaande `bedrijfsprocessen`/`bedrijfsfuncties`-vermeldingen die de nieuwe lint-check als "vrije tekst i.p.v. wiki-link" markeert, zijn migratie-achterstand — bewust niet in bulk omgezet, elke migratie vereist een eigen `/assess-element`-beoordeling. `tools/entiteitendekking.py` blijft ongewijzigd (matcht nog niet tegen bedrijfsfunctie/-procespagina's) — buiten scope van dit besluit.
- **Bijgewerkt:** `Wiki/index.md` (nieuwe secties Bedrijfsfuncties/Bedrijfsprocessen, vooralsnog leeg), `ToDo/Structuur en herleidbaarheid.md` (alle 4 punten van open naar opgelost/besloten, met vervolgwerk-tabel).

## [2026-09-19] bo | Beperking heroverwogen — ten onrechte afgewezen begrip alsnog BO (Generiek Jeugd en Wmo)

- **Aanleiding:** gebruiker vroeg om verklaring van de rij `Beperking → beschrijft Beschikking, detail, "Eigenschap van beoordeling, niet zelfstandig BO"` in `Wiki/Analyses/entiteitendekking/6-sociaal-domein.md`. Herkomst getraceerd: gecureerde ❌-afwijzing uit `Wiki/Onderwerpoverzichten/maatschappelijke-ondersteuning.md` (2026-06-27), zonder expliciete criteria-score — in tegenstelling tot buurregels die wel een concrete structurele reden geven.
- **Herbeoordeling (`/assess-element`):** GGM-data (attributen `duur, categorie, commentaar, wet`; relaties naar Beperkingscategorie, Beperkingscore en optioneel — 0..1 — naar Beschikking, "is gebaseerd op") en Wmo 2015 art. 2.3.5 lid 3 ("het college beslist tot verstrekking [...] ter compensatie van de beperkingen [...] die de cliënt ondervindt") getoetst aan de 6 BO-criteria: 6/6, ruim boven de drempel van 5. De 0..1-relatie naar Beschikking (niet 1..1) bevestigt eigen bestaan: een beperking kan al zijn vastgesteld tijdens het onderzoek (art. 2.3.2), vóór er een beschikking is.
- **Vastgelegd (`/write-element`):** nieuwe BO-pagina `Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beperking.md`, grondslag `ggm-entiteit`, matchsterkte exact. `## GGM-componenten` voor Beperkingscategorie en Beperkingscore (geen aparte BO's). Onderwerpoverzicht `maatschappelijke-ondersteuning.md` bijgewerkt (❌→✅, bo_count 15→16, verwerkingsdatum ververst).
- **Entiteitendekking herberekend:** `entiteitendekking.py --all` + `entiteitendekking_sync_bo.py` gedraaid. Beperkingscategorie, Beperkingscore en Beperkingscoresoort routeren nu correct via het nieuwe BO Beperking i.p.v. via Beschikking (kortere, juistere graph-afstand). Totaaloverzicht-aggregaat ongewijzigd (724/877 gedekt) — Beperking was al indirect meegeteld als "ondersteunend", telt nu als directe match; alleen de onderverdeling verschuift. Taakveld 6 BO-matches 61→62.
- **BO-frontmatter-sync:** chirurgisch 2 pagina's bijgewerkt (`beperking.md` nieuw `analyse_ggm_dekking`, `beschikking.md` 3 regels minder — Beperking/Beperkingscategorie/Beperkingscore niet langer als indirecte dekking vermeld), 242 ongewijzigd.
- **Verificatie:** `python3 tools/lint_checks.py` 230 → 230 (ongewijzigd), YAML-parse OK.
- **Reflectie:** dit is het tweede geval (na de `bo_subtypes`-lintcheck gisteren) waarin een eerdere, niet meer onderbouwde beslissing bij toeval aan het licht kwam via een entiteitendekking-rapportrij. Geen aanleiding voor een systematische heraudit van alle vroege (pre-2026-07) ❌-rijen zonder criteria-score — wel iets om alert op te blijven bij toekomstige lint/dekkingsvragen.

## [2026-09-18] fix | Verouderde `bo_subtypes`-lintcheck verwijderd (37 valse positieven)

- **Aanleiding:** laatste openstaand punt — `tools/lint_checks.py`'s `check_subtypes()` was nooit bijgewerkt na de deprecatie van het `bo_subtypes`-veld (subtypes staan sinds die wijziging alleen nog in de `## Subtypes`-body-sectie, zie `templates/element.md`). De check ging nog uit van het oude tweevoudige patroon en vlagde elke pagina met een gevulde sectie maar lege frontmatter als "mismatch" — precies het nu-correcte patroon voor elke sinds de deprecatie geschreven BO (waaronder `Inkomensvoorziening` en de vandaag aangemaakte `Vermogenscomponent`/`Maatregel`).
- **Fix:** de `elif not subtypes and section is not None`-tak (en de bijbehorende `body_no_fm`-return-waarde en rapportregel) uit `check_subtypes()` verwijderd. De twee overige, nog wel geldige checks (`bo_subtypes` gevuld zonder body-sectie; frontmatter/body-namen die niet overeenkomen wanneer beide gevuld zijn) blijven intact.
- **Verificatie:** lint-totaal 267 → 230 (exact de verwachte 37 minder), Python-syntaxcheck OK, het ene overblijvende (legitieme, niet aan vandaag gerelateerde) resultaat in die categorie (`vergunningen-en-ontheffingen.md`, frontmatter gevuld zónder body-sectie — het omgekeerde, nog wel een echte bevinding) blijft correct staan.

## [2026-09-18] analyse | Entiteitendekking ververst na Participatiewet-ingest (laatste openstaande punt)

- **Aanleiding:** laatste van de 4 openstaande punten uit de Participatiewet-ingest — de nieuwe BO's (Normafwijking, Maatregel, Boete, Vermogenscomponent) hadden een lege `analyse_ggm_dekking`, en `Werkzoekende` noemde Ontheffing nog als indirect gedekt "detail" terwijl dat inmiddels een eigen BO is.
- **Stap 1 — misstap en herstel:** eerste run met `--taakveld 6` overschreef `totaaloverzicht.md` zodat alleen taakveld 6 nog in de tabel stond — de andere 11 taakvelden waren verdwenen. Hersteld door `--all` te draaien (regenereert alle 12 taakveldrapporten + het totaaloverzicht consistent); geverifieerd dat de overige 11 taakveld-bestanden alleen een `datum:`-bump kregen (op 4-onderwijs.md na, die nu correct de Vrijstelling↔Leerplichtvrijstelling-homoniem toont — bijvangst van een eerdere fix in deze sessie).
- **Stap 2 — 3 nieuwe `ter discussie`-conflicten opgelost:** de nieuwe `Vermogenscomponent`-BO introduceerde ambiguïteit voor `Profiel`, `Inkomstenverhouding` en `Reden aanvraag` (GGM biedt geen sterk signaal welke van Client/Vermogenscomponent de juiste route is). Alle drie inhoudelijk beoordeeld aan de hand van de GGM-definities (bijv. "Inkomstenverhoudingen worden geadministreerd in het profiel van de klant") en toegewezen aan **Client** via `bo_via_kandidaten` — gaat over profiel/inkomen van de persoon, niet over een vermogensbestanddeel. 8 resterende, niet aan dit werk gerelateerde `ter discussie`-items (Inburgering, Inkomen/Vordering-cluster, Schulden) bewust laten staan — buiten scope van deze refresh.
- **Stap 5 — BO-frontmatter sync:** `entiteitendekking_sync_bo.py` gedraaid (niet dry-run), 121 BO-pagina's chirurgisch bijgewerkt (alleen het `analyse_ggm_dekking`-veld), 122 ongewijzigd. Steekproef bevestigt dat alleen dat veld is geraakt.
- **Bijgewerkt:** `Wiki/index.md` (verse cijfers voor totaaloverzicht en taakveld 6, vermelding nieuwe beleidsdomeinen Normafwijking/Vermogen).
- **Bewust niet gedaan:** de `## Beoordeling`-sectie van `6-sociaal-domein.md` bevat nog steeds de ongewijzigde `<!-- REVIEW -->`-placeholder (kale cijfers, geen inhoudelijke interpretatie) — dit bleek al zo te zijn sinds de vorige run (2026-07-09), geen regressie van vandaag. Volledige inhoudelijke beoordeling van alle 10 beleidsdomeinen in taakveld 6 is een aparte, grotere klus dan deze refresh.
- **Verificatie:** lint 267 bevindingen (ongewijzigd), YAML-parse OK op alle aangepaste bestanden.

## [2026-09-18] bo | Art. 48-51 en 57 Participatiewet beoordeeld — geen nieuwe BO's, Inkomensvoorziening verrijkt met sectie Verstrekkingsvorm

- **Aanleiding:** twee openstaande punten uit de Participatiewet-ingest: art. 48-51 (Geldlening en borgtocht, Schuldenlast, Eigen woning, Duurzame gebruiksgoederen) waren nooit volledig gelezen (alleen titels via de hoofdstuk-index), en art. 57 (Noodzakelijke betalingen en bijstand in natura) was wel gelezen maar nooit los beoordeeld naast de eerder afgewezen `Ontzorgen` (art. 56a).
- **Bevinding:** beide horen bij dezelfde dimensie — *hoe* een inkomensvoorziening wordt uitgekeerd, niet *welke* regeling het is. Dit is al een bestaand GGM-attribuut op Inkomensvoorziening (`verstrekkingsvorm`), geen aparte entiteit. BO-criteria toegepast: geen eigen identificatie of levenscyclus los van de onderliggende voorziening (zelfde conclusie als eerder bij Ontzorgen) — dus geen nieuwe BO's voor "Geldlening" of "Bijstand in natura".
- **Vastgelegd:** nieuwe sectie `## Verstrekkingsvorm` op `Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening.md`, met de wettelijke voorwaarden per vorm (om niet = hoofdregel art. 48 lid 1; geldlening/borgtocht bij de 4 gronden van art. 48 lid 2, saneringskrediet art. 49, eigen-woning-vermogen art. 50, duurzame gebruiksgoederen art. 51; in natura/rechtstreekse betaling art. 57, met expliciete kruisverwijzing naar de eerder afgewezen Ontzorgen-variant). `bo_toelichting` en Bronnen-citaat bijgewerkt; bronsamenvatting `participatiewet.md` aangevuld in de "beoordeeld en afgewezen"-lijst.
- **Verificatie:** YAML-parse OK, lint 267 bevindingen (ongewijzigd).

## [2026-09-18] fix | "Structureel buiten GGM-scope"-framing gecorrigeerd (5 pagina's) + nieuwe regel tegen verwijzingen naar technische bestanden

- **Aanleiding:** de vorige fix (dode links naar verwijderde Analyses-pagina's) loste ik op door te verwijzen naar CLAUDE.md/`templates/element.md`. Gebruiker corrigeerde dit op twee punten: (1) BO-pagina's mogen niet naar technische/proces-bestanden verwijzen, en (2) de onderliggende bewering zelf ("dit valt buiten de scope van het GGM per definitie" / "structureel hiaat") is te absoluut — juister is dat procesobjecten/governance-objecten in het GGM niet compleet gedekt zijn, geen categorische uitsluiting.
- **Belangrijk onderscheid (expliciet bevestigd door gebruiker):** dit geldt alleen voor het **generieke** patroon ("GGM doet nooit processen/governance, dus geen match") zonder domeinspecifieke onderbouwing. Inhoudelijk onderbouwde constateringen met een concrete, specifieke reden (bijv. `opvanglocatie.md`: "het beleidsdomein Inburgering begint pas bij de inburgeringsplicht, de opvangfase daarvoor valt buiten scope") blijven **ongewijzigd** — die zijn goed, geen generiek excuus.
- **Gecorrigeerd (5 pagina's, na handmatige beoordeling van 15 kandidaten):** `sla.md`, `voetgangersgebied.md`, `zero-emissiezone.md`, `welstandsadvies.md`, `afvalstoffenverordening.md` — telkens "structureel buiten de GGM-scope (het GGM modelleert data, niet governance/processen)" vervangen door "... zijn in het GGM niet compleet gedekt", zonder de rest van de (vaak wel goede) redenering aan te tasten.
- **Bewust ongewijzigd gelaten (10 kandidaten uit dezelfde grep, na inhoudelijke beoordeling):** `opvanglocatie.md`, `bodemverontreiniging.md`, `bodemkwaliteitskaart.md`, `partijsubsidie.md`, `gemeenschappelijke-regeling.md`, `werklocatie.md`, `materiaalpasspoort.md`, `hulpbehoevend-dier.md`, `vergunningen-en-ontheffingen.md`, `software.md` — elk gebruikt "structureel" in een specifieke, onderbouwde context (concreet ontbrekend beleidsdomein, specifieke wetsverwijzing, brontaal-citaat, of een andere betekenis van "structureel" die niets met GGM-scope te maken heeft).
- **Ook opnieuw gecorrigeerd (eerder vandaag per abuis fout gefixt):** `bestuursovereenkomst.md`, `verkiezing.md`, `referendum.md`, `gemma-bedrijfsobjecten-en-ggm.md`, `Wiki/Vragen/ggm-oorsprong-en-meerwaarde.md` (2x), `templates/element.md`'s Grondslag-tabel — de CLAUDE.md/templates-verwijzingen die ik er zonet aan toevoegde zijn eruit gehaald; de bewering zelf herschreven naar "niet compleet gedekt" i.p.v. "buiten scope"/"structureel"/"per definitie".
- **Nieuwe regel (CLAUDE.md §7, punt 4):** wiki-content verwijst nooit naar `CLAUDE.md`, `templates/`, `tools/` of skills — die documenteren het proces, niet de inhoud, en zijn geen stabiel citaat-anker (sectienummers/bestanden verschuiven). Inclusief de vuistregel: generieke taal als "structureel buiten scope" of "per definitie" zonder domeinspecifieke onderbouwing is een signaal dat de bewering herschreven moet worden met de concrete reden. Ook toegevoegd aan `templates/element.md`, sectie Linkconventie body.
- **Verificatie:** `python3 tools/lint_checks.py` 266 → 267 → 266 (netto ongewijzigd; tussentijdse alias-mankementen in eigen log-tekst meteen zelf gecorrigeerd).
- **Vervolg (buiten `Wiki/Bedrijfsobjecten/` gezocht):** dezelfde generieke formulering bleek ook te staan in `Wiki/Bronsamenvattingen/Arbeidszaken/cva-beleidsplan-2023-2026.md`, `.../college-voor-arbeidszaken.md`, `Wiki/Onderwerpoverzichten/cultuur.md` en `.../inburgering-en-asielopvang.md` (de laatste bevatte zelfs een interne tegenspraak: "valt structureel buiten het GGM" náást "dit is een hiaatbevinding" in dezelfde zin). Alle vier gecorrigeerd naar "niet compleet gedekt" resp. de contradictie verwijderd.

## [2026-09-18] fix | Dode links naar 3 verwijderde Analyses-pagina's opgeruimd (regressie uit gisteren)

- **Aanleiding:** bij het opzoeken van `[[Wiki/Analyses/ggm-dekkingspatroon]]` (zie vorige log-entry) bleek de pagina niet ontbrekend maar **verwijderd**: git bevestigt dat `ggm-dekkingspatroon.md` (146 regels), `ggm-hiaten-belastingendomein.md` (242 regels) en `vng-rubrieken-mapping.md` (441 regels) alle drie zijn weggevallen in de "cleanup"-commit `df096d8` (Mark Backer, 2026-09-17), samen met een grote batch overduidelijk overbodige bestanden (verouderde CSV-exports, een 16k-regel JSON-cache, losse clippings). De drie Analyses-pagina's lijken hierin te zijn meegesleept, niet doelbewust individueel verwijderd.
- **Gebruikersvraag:** of de inhoud van `ggm-dekkingspatroon` (het patroon "GGM dekt data, niet processen/governance") als regel in de skills verwerkt moest worden. Bevinding: dat was al zo — CLAUDE.md §1/§6 en `templates/element.md`'s Grondslag-sectie bevatten de operationele regel al onafhankelijk van de verwijderde pagina (vandaag zelf toegepast bij het aanmaken van `Voorschot`/`Verhaal` als procesobject). De verwijderde pagina was uitsluitend bewijsvoering (tabel per domein), geen bron van een regel die nu ontbreekt.
- **Besluit gebruiker:** pagina's niet herstellen; de ~9 dode verwijzingen omleiden naar de bestaande regel in CLAUDE.md/templates in plaats van naar een nieuwe/herstelde pagina.
- **Opgeruimd (9 verwijzingen, 8 bestanden):** `bestuursovereenkomst.md`, `verkiezing.md`, `referendum.md`, `gemma-bedrijfsobjecten-en-ggm.md`, `templates/element.md` (2x) omgeleid naar "CLAUDE.md §6 en templates/element.md, sectie Grondslag"; `ggm-oorsprong-en-meerwaarde.md` (2x, waarvan één als Bronnen-lijst-item verwijderd met toelichting) en `taakveld.md` (waar de specifieke bewijsclaim geen vervangende bron had, dus de link losgelaten met behoud van de zin). Bijvangst: `taakveld.md` bevatte ook een losstaande dode link `[[GGM-indeling]]` (nooit bestaan onder die naam) — gecorrigeerd naar `[[Wiki/GGM/structuur-ggm|structuur-ggm]]`.
- **Verificatie:** `python3 tools/lint_checks.py` 267 → 266 bevindingen (de ene daling is de wiki-link-alias die ik in mijn eigen vorige log-entry miste); geen van de negen fixes voegde een nieuwe dode link toe (elk doelbestand met `ls`/`find` geverifieerd vóór gebruik).
- **Niet gedaan:** de drie verwijderde pagina's zelf niet hersteld (bewuste keuze gebruiker) en niet verder onderzocht of er nog meer bestanden in dezelfde commit onbedoeld zijn meegesleept buiten `Wiki/Analyses/` — als dat vermoeden er is, apart onderzoeken.

## [2026-09-18] ingest | Participatiewet — 6 nieuwe BO's, 2 nieuwe GGM-beleidsdomeinen ontgonnen, 7 bestaande BO's verrijkt

- **Aanleiding:** vervolg op het eerder opgehaalde bronbestand `participatiewet-bwbr0015703.md` (zie vorige log-entry) — volledige `/ingest` op verzoek van de gebruiker, scope "volledige wet in één keer" na overleg over een signalering per hoofdstuk-cluster.
- **Bronsamenvatting:** `Wiki/Bronsamenvattingen/Werk en Inkomen/participatiewet.md` aangemaakt — dekt alle 8 hoofdstukken (174 artikelen), met expliciete clustering in gedekt/nieuw/subtype/afgewezen.
- **7 bestaande BO's verrijkt met de wet als (aanvullende) bron:** Werkzoekende, Loonkostensubsidie, Re-integratievoorziening, Trajectplan, Instrument, Inkomensvoorziening, Draagkracht, plus de volledige Terug-en-invordering-cluster (Vordering, Aflossingsplan, Aflossing, Kwijtschelding, Afschrijving, Restitutie, Interventie) — `Vordering`'s eigen definitie noemde de bijstandscontext al expliciet, art. 58-60c Participatiewet is nu de wettelijke grondslag.
- **Naamgevingsvondst:** "plan van aanpak" (art. 44a, art. 9a lid 7-9) bleek hetzelfde concept als het bestaande SGR-begrip Trajectplan — toegevoegd als `bo_synoniemen`, geen nieuw BO.
- **6 nieuwe BO's, twee tot dusver onontgonnen GGM-beleidsdomeinen:**
  - **Normafwijking, Maatregel, Boete** (`Wiki/Bedrijfsobjecten/6-sociaal-domein/normafwijking/`, nieuwe map) — eerste BO's uit GGM-beleidsdomein **Normafwijking**. De GGM-overervingshiërarchie (`Wiki/GGM/6-sociaal-domein/normafwijking.md`) bleek cruciaal: Maatregel is het abstracte generalisatie-niveau, Boete een specialisatie (bewust apart gemodelleerd t.b.v. risicoprofilering, ook als de onderliggende vordering niet meer bestaat), Normafwijking de voorafgaande constatering+verwijtbaarheidsbeoordeling. `Afwijkende maatregel`/`Maatregel op uitkering` zijn dunne parametrische GGM-entiteiten zonder eigen identificatie — als Subtypes bij Maatregel gedocumenteerd, geen aparte BO's.
  - **Vermogenscomponent** (`sociaal-domein-generiek/`) — eerste BO uit GGM-subdomein **Vermogen**. GGM: abstract, generaliseert naar Bankrekening/Hypotheek/Motorvoertuig/Onroerend goed (als Subtypes gedocumenteerd, niet uitgewerkt — bredere Sociaal Domein Generiek-concepten, buiten scope van deze ingest).
  - **Voorschot, Verhaal** (`model-inkomen/`, procesobject) — beide GGM-hiaten (#95, #96). Verhaal is expliciet onderscheiden van het bestaande GGM-begrip Onderhoudsplicht (niet-BO, civielrechtelijke relatie, zie bronsamenvatting BW Boek 1 Titel 17): Verhaal is het gemeentelijke besluit dat een bestaande onderhoudsplicht verzilvert, geen nieuwe civielrechtelijke relatie.
- **Beoordeeld en afgewezen (❌, toegevoegd aan begrippentabel):** Ontzorgen (art. 56a — te smalle doelgroep, geen eigen levenscyclus los van de bijstandsverlening zelf), Bijstandsnorm/Kostendelersnorm (art. 19a-22a — rekenregel/attribuut van Inkomensvoorziening, geen zelfstandig object).
- **Terugmeldingen:** #95 (Voorschot, hiaat), #96 (Verhaal, hiaat) toegevoegd aan `Wiki/Analyses/ggm-terugmeldingen.md`.
- **Bijgewerkt:** `Wiki/Onderwerpoverzichten/werk-en-inkomen.md` (10 nieuwe/gewijzigde rijen), `Wiki/index.md` (7 nieuwe BO-vermeldingen + bronsamenvatting), `ToDo/ingest-backlog.md`.
- **Verificatie:** `python3 tools/lint_checks.py` vóór en na vergeleken — totaal 265 → 266 bevindingen; het ene verschil is een pre-existente, verouderde lint-regel (`bo_subtypes`-veld is gedeprecieerd sinds de templates-update, maar de check is daar nog niet op aangepast — treft ook 37 al bestaande pagina's, waaronder Inkomensvoorziening zelf). Geen Wees-BO's, geen ontbrekende aliassen, geen kapotte relaties.
- **Bewust niet gedaan:** Hoofdstuk 1 (definities), Hoofdstuk 7 (financiering Rijk-gemeente, al ❌BO), Hoofdstuk 7a/7b/7c (overgangsrecht, aflopende regelingen) en Hoofdstuk 8 (slotbepalingen) leverden geen BO-kandidaten op — besproken en bevestigd met de gebruiker vóór aanvang van het schrijfwerk.
- **Zijdelingse observatie (niet opgelost, buiten scope):** de wiki-link `[[Wiki/Analyses/ggm-dekkingspatroon|ggm-dekkingspatroon]]` wordt vanuit minstens 8 bestaande pagina's aangehaald maar de pagina zelf bestaat niet meer in `Wiki/Analyses/`. Git bevestigt dat `ggm-dekkingspatroon.md` (146 regels) is verwijderd in de "cleanup"-commit van 2026-09-17 (`df096d8`), zonder de verwijzingen ernaar op te ruimen — een regressie, geen ontbrekende aanmaak. Niet door de huidige `/lint`-regels gedetecteerd (die controleren alleen dode Sources-links).

## [2026-09-18] bron | Participatiewet opgehaald ter onderbouwing van Ontheffing (Werk)

- **Aanleiding:** `Ontheffing (Werk)` had geen beleidsbron naast het GGM; `## Bronnen` was gemarkeerd met 🔍 Verificatie nodig voor de aanvraag-/herzieningsprocedure.
- **Opgehaald via curl** (niet WebFetch — wetten.overheid.nl-tekst mag niet geparafraseerd worden, zie eerdere afspraak): `https://wetten.overheid.nl/BWBR0015703/2026-01-01` (Participatiewet, volledige wettekst, 174 artikelen). Opgeslagen als `Sources/Onderwerpen/Werk en Inkomen/participatiewet-bwbr0015703.md`.
- **Relevante vondst:** art. 9 lid 2 (algemene ontheffing bij dringende redenen, incl. zorgtaken) en art. 9a (aparte, eenmalige ontheffing voor alleenstaande ouder met kind tot vijf jaar, met zesmaandelijks heronderzoek) bevestigen de GGM-definitie inhoudelijk en onderbouwen nu `bo_toelichting` en de `## Bronnen`-sectie van `werk/ontheffing.md` met letterlijke citaten.
- **Bewust niet gedaan:** geen volledige `/ingest` van de Participatiewet (bronsamenvatting, onderwerpoverzicht-uitbreiding) — dat is een grotere stap die eerst met de gebruiker besproken moet worden (CLAUDE.md §"Bespreek eerst, schrijf dan"). Alleen de brontekst is opgehaald en direct geciteerd, gericht op deze ene verificatievraag. Opengezet als item in `ToDo/ingest-backlog.md` onder Werk en Inkomen.

## [2026-09-18] bo | Ontheffing (Werk) aangemaakt — resterend punt uit vorige lint-run opgelost

- **Aanleiding:** vorige log-entry signaleerde dat `inburgering/ontheffing.md`'s `bo_homoniemen`-item naar `werk/ontheffing.md` een dode link was — die pagina bestond nog niet.
- **Beoordeling (`/assess-element`):** GGM-entiteit Ontheffing in beleidsdomein Werk (GUID `EAID_8EE515EA...`), 15 attributen (aanvraag, besluit, motivatie, ingangs-/einddatum, herziening) wijzen op een volwaardige entiteit met eigen levenscyclus, niet slechts het "detail"-attribuut van Werkzoekende waarvoor `werkzoekende.md`'s `analyse_ggm_dekking` het momenteel aanmerkt. Score 6/6, GGM-match exact, autonoom afgehandeld (voldoet aan alle drie autonomiecriteria uit stap 11).
- **Bevestigd echt homoniem, geen duplicaat:** `ggm_parsed.json` bevat exact 2 entiteiten met naam "Ontheffing" — Werk (`EAID_8EE515EA...`) en Inburgering (`EAID_3F5932BD...`), met wezenlijk andere definities (arbeidsverplichtingen Participatiewet vs. inburgeringsplicht Wi2021).
- **Aangemaakt:** `Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/ontheffing.md`. Naamgeving volgt het precedent van de Inburgering-tegenhanger: `naam: Ontheffing` blijft ongewijzigd, disambiguatie via de domeinmap (`werk/` vs. `inburgering/`), "(Werk)"/"(Inburgering)" alleen als linktekst.
- **Bewust niet gedaan:** `werkzoekende.md`'s `analyse_ggm_dekking` (noemt Ontheffing nog als indirect gedekt detail) niet handmatig aangepast — dat veld is scriptgegenereerd door `entiteitendekking_sync_bo.py` en wordt bij de eerstvolgende `/entiteitendekking`-run vanzelf bijgewerkt nu Ontheffing een eigen `ggm_guid`-dekkende BO-pagina heeft. Evenmin een reciproke relatie in `werkzoekende.md`'s `bo_relaties` toegevoegd — de Inburgering-kant kent dat patroon ook niet (`inburgeringsplicht.md` verwijst niet terug naar `ontheffing.md`), dus asymmetrische relaties zijn hier precedent, niet een omissie.
- **Bronnen:** geen aparte Participatiewet-bronsamenvatting in `Sources/Onderwerpen/Werk en Inkomen/` beschikbaar voor dit specifieke besluit (wet-suwi noemt een andersoortige ontheffing, art. 8 lid 3 BBA 1945 — niet hetzelfde concept, dus niet als bron gebruikt). Definitie komt daarom uitsluitend uit het GGM (matchsterkte exact); gemarkeerd met 🔍 Verificatie nodig in de Bronnen-sectie.
- **Terugmelding:** #94 toegevoegd aan `Wiki/Analyses/ggm-terugmeldingen.md` (type `homoniem`), met kruisverwijzing naar de bestaande structurele hiaten #44 en #50 (ontbrekend generiek Ontheffing-supertype).
- **Bijgewerkt:** `Wiki/Onderwerpoverzichten/werk-en-inkomen.md` (nieuwe rij), `Wiki/index.md` (nieuwe pagina).

## [2026-09-18] fix | Dode homoniem-link vrijstelling ↔ leerplichtvrijstelling hersteld

- **Bevinding:** `inburgering/vrijstelling.md`'s `bo_homoniemen`-item linkte naar `.../leerplicht-en-leerlingenvervoer/vrijstelling` — die pagina bestaat niet. Bleek een verkeerde bestandsnaam: de echte pagina heet `leerplichtvrijstelling.md`.
- **Bevestiging vóór fix:** de GUID's kruisen exact — `inburgering/vrijstelling.md`'s eigen `ggm_guid` (`EAID_B8584CD2...`) staat als homoniem-guid in `leerplichtvrijstelling.md`, en omgekeerd (`EAID_C31D4A7E...`). Dit zijn dus elkaars bedoelde tegenhangers, geen toeval.
- **Fix:** link in `inburgering/vrijstelling.md` gecorrigeerd naar `leerplichtvrijstelling`; `leerplichtvrijstelling.md`'s homoniem-item kreeg het ontbrekende `bedrijfsobject`-veld terug (naar `inburgering/vrijstelling.md`). Lost tegelijk de "mist bedrijfsobject"- én de "eenzijdig"-bevinding voor dit paar op.
- **Resterend (nog niet gefixt, zie vorige log-entry):** `inburgering/ontheffing.md` linkt naar een `werk/ontheffing.md` die nergens bestaat — `Wiki/Onderwerpoverzichten/milieu.md` noemt "Ontheffing Werk" wel expliciet als bestaande domeinvariant zonder eigen BO-pagina. Dit is een ontbrekende BO-aanmaak (`/assess-element`), geen lint-fix.

## [2026-09-18] fix | Stap 0 en Stap 4c in write-element.md samengevoegd (overlap opgelost)

- **Aanleiding:** de gisteren toegevoegde Stap 0 (wiki-naamcollisie) en de bestaande Stap 4c (GGM-homoniem-naamkeuze) beschreven dezelfde disambiguatie-mechaniek (suggestiestrategieën, `## Naamkeuze`) twee keer — alleen de trigger verschilde.
- **Fix:** samengevoegd tot één Stap 0 ("Naamgeving en disambiguatie") met twee triggers (wiki-collisie, ongeacht grondslag; GGM-homoniem via stap 4b, alleen bij `grondslag: ggm-entiteit`) en de GGM-specifieke restregels (ggm_entiteit behouden, niet naar bo_synoniemen) als aparte paragraaf. Stap 4c vervallen; verwijzingen in stap 4/4b/8 aangepast. Stap-nummering ongewijzigd (4b bleef 4b, geen gat).

## [2026-09-18] fix | Regel verduidelijkt: `bo_homoniemen` is een GGM-naamcollisie, geen wiki-BO-naamcollisie — 2 misclassificaties gecorrigeerd, 1 per abuis meegetrokken en teruggedraaid

- **Vraag gebruiker:** klopt de redenering dat `bo_homoniemen` alleen relevant is voor de onderliggende GGM-entiteiten, niet voor de (per definitie ondubbelzinnige) wiki-BO-naam zelf?
- **Bevestigd, met bewijs uit de data:** een échte homoniem (bijv. het net herstelde `vrijstelling`↔`leerplichtvrijstelling`-paar) heeft aan **beide** kanten een eigen `ggm_entiteit` met dezelfde naam en verschillende GUID. Bij controle bleken `financiele-voorziening.md` en `gebruiksrecht.md` (beide `grondslag: procesobject`, geen eigen `ggm_entiteit`) geen GGM-naamcollisie te representeren — er bestaat geen tweede GGM-entiteit met hun naam in een ander domein. Hun `bo_homoniemen`-item was dus verkeerd gecategoriseerd; de uitleg stond al (en blijft) in hun bestaande `## Naamkeuze`-sectie. Frontmatter geleegd naar `[]`.
- **Regel expliciet gemaakt:** nieuwe "Stap 0: Naam vaststellen" in `write-element.md` (naamgeving/disambiguatie geldt voor élk BO, ongeacht grondslag — dat is iets anders dan een GGM-homoniem) en een aanscherping van stap 4b ("alleen van toepassing bij `grondslag: ggm-entiteit`"). `templates/element.md`'s veldcommentaar bij `bo_homoniemen` verwijst nu naar deze stap.
- **Fout gemaakt en zelf teruggedraaid:** `vacature.md`↔`vacature-arbeidsmarkt.md` leek op het eerste gezicht dezelfde situatie (target heeft `grondslag: procesobject`), en is per abuis ook geleegd. Bij controle van `Wiki/Analyses/ggm-terugmeldingen.md` bleek terugmelding **#87** dit expliciet als `homoniem` te classificeren, met hernoemadvies "Vacature (HR)" vs. "Vacature (arbeidsmarkt)" — een bewuste, eerder vastgelegde beoordeling, geen omissie. Dit is een derde categorie die de huidige regel niet dekt: een GGM-naamcollisie-risico dat is vastgelegd vóórdat de tweede GGM-entiteit officieel bestaat (de Werk-kant is zelf een GGM-hiaat). Wijziging teruggedraaid (`git checkout`); item blijft staan zoals het was, inclusief de bestaande onvolledigheid (`ggm_entiteit`/`ggm_guid` blijven leeg, terecht niet in te vullen zolang het hiaat openstaat).
- **Les:** vóór een `bo_homoniemen`-item als misclassificatie behandelen, altijd eerst `ggm-terugmeldingen.md` raadplegen op een expliciete `homoniem`-classificatie — een lege `ggm_entiteit`/`ggm_guid` kan een bewuste hiaat-gebonden registratie zijn, niet per se een fout.

## [2026-09-17] feature | 4e `--fix`-categorie (bo_homoniemen ggm-backfill); 3 van 4 "mechanische" stap-2-categorieën bleken dat niet

- **Aanleiding:** na stap 2 (modelbeoordeling) leken 4 categorieën pure data-omissies: `bo_relaties` mist kardinaliteit (23), `ggm_duplicaat_entiteiten`/sectie-mismatch (13), `bo_homoniemen` mist veld (7), `bo_homoniemen` eenzijdig (4). Bij het daadwerkelijk scripten bleek die aanname te optimistisch.
- **Wél mechanisch, nu gescript (`fix_homoniemen_ggm_backfill`):** 2 van de 7 `bo_homoniemen`-items misten alleen `ggm_guid` terwijl `bedrijfsobject` al naar een bestaande pagina wees die zelf wél `ggm_entiteit`/`ggm_guid` had — die twee velden zijn 1-op-1 over te nemen. Gefixt: `financiele-voorziening.md`, `gebruiksrecht.md`.
- **Niet mechanisch, ondanks eerdere aanname:**
  - **`bo_relaties` kardinaliteit (23)** — geen bron om uit te lenen; een mens moet "0..1" vs "0..\*" kiezen.
  - **`bo_homoniemen` mist `bedrijfsobject` (5 resterend van de 7)** — geverifieerd tegen alle `ggm_guid`'s in de wiki: 3 van de 4 gecontroleerde gevallen (arbeidsfunctie, put, storing-ict) hebben nog geen eigen BO-pagina om naar te linken; het 4e geval (leerplichtvrijstelling) heeft wél een kandidaat-target maar die zit al in een aangrenzend homoniemen-cluster (er bestaat al een apart `vrijstelling`-homoniempaar tussen inburgering en onderwijs) — blind linken zou kunnen botsen met een bestaande, andere disambiguatiekeuze. Vereist een mens.
  - **`bo_homoniemen` eenzijdig (4)** — de bronpagina heeft vaak zelf geen `ggm_entiteit`/`ggm_guid` (bijv. `financiele-voorziening.md` heeft zelf geen GGM-grondslag), dus er is niets om terug te spiegelen naar de tegenpartij.
  - **`## GGM-duplicaten`-sectie genereren (13)** — alle 14 bestaande, correct gesynchroniseerde secties in de wiki bevatten een "primair vs. duplicaat"-redenering (vaak gebaseerd op diagram-aantallen) én een verwijzing naar een regel in `ggm-terugmeldingen.md`. Er is geen "kaal" precedent. Een kaal gegenereerde sectie zonder die twee elementen zou de bestaande conventie doorbreken, dus niet gedaan.
- **Correctie op eerdere aanname:** in het vorige rapport aan de gebruiker waren deze 4 categorieën allemaal als "puur data-omissie, mechanisch te vullen" bestempeld. Dat klopte alleen voor 2 van de ~9 individuele gevallen die daadwerkelijk zijn nagelopen. `lint.md` is bijgewerkt met een expliciete uitleg waarom de rest niet scriptbaar is, zodat dit niet nogmaals als "simpel" wordt aangenomen.
- **Verificatie:** dry-run vóór toepassing, YAML re-parse na afloop (0 nieuwe fouten), git diff bevestigt exact 2 bestanden × 1 regel gewijzigd.

## [2026-09-17] feature | `lint_checks.py --fix` toegevoegd; `lint.md` ingekort (geen historie meer in de skill)

- **`--fix`-vlag** op `tools/lint_checks.py`: past de drie mechanisch veilige categorieën uit de vorige entry direct toe (Bronnen-alias strippen, dode Sources-links oplossen bij eenduidige kandidaat, `ggm_duplicaat_entiteiten`-schema upgraden) i.p.v. de eenmalige scratchpad-scripts van eerder vandaag. Elke fix-functie verifieert zijn eigen schrijfactie (GUID-set voor/na identiek, alleen schrijven bij exact één kandidaatbestand) vóór commit.
- **Los getest** met een geïsoleerde fixture (niet tegen de echte wiki, die nu al schoon is): alle drie fix-functies correct bevonden, inclusief YAML re-parse na de duplicaten-schema-upgrade.
- **`.claude/commands/lint.md` herschreven**: incident-narratief (Haiku-hallucinatie, datums, log-verwijzingen) eruit — de skill beschrijft nu alleen wat hij doet, niet waarom hij zo gebouwd is. Die geschiedenis staat in deze log, niet in de skill.

## [2026-09-17] feature | `/lint` gesplitst in deterministisch script + modelbeoordeling, 3 nieuwe buggroepen gevonden en gefixt

- **Aanleiding:** vervolg op de lint-hallucinatie-analyse hieronder. Gebruiker vroeg om herhaalbare scripts te bouwen voor wat mogelijk is, met één `/lint`-commando dat eerst het script draait en dan pas een LLM-check.
- **Nieuw:** `tools/lint_checks.py` — dekt het grootste deel van de telbare/structurele bullets uit `lint.md` (Bronnen-secties, frontmatter-compleetheid/enum/ggm_guid-validatie, bo_relaties-structuur, subtypes/duplicaten/homoniemen-schema en -consistentie, wees-BO's, Begrippen/-verbod, wiki-link-aliassen, dubbele bestandsnamen, onderwerpoverzicht-tabellen). Elke check is getest tegen een handmatig geverifieerde steekproef vóór opname (zie hieronder) — dat is precies de stap die bij de Haiku-run ontbrak.
- **`.claude/commands/lint.md` herschreven**: stap 1 = script (geen model nodig, exacte telling), stap 2 = Haiku-beoordeling van wat het script alleen kan signaleren maar niet kan beoordelen (registr*-context, bo_relaties-omissie vs. bewust, wees-BO terecht of niet). Checks die nog niet gescript zijn (generalisatie/specialisatie-symmetrie, ggm-dekking.md-volledigheid, terugmeldingen-consistentie, naamkeuze) staan expliciet benoemd als openstaand — zie [[project_lint-skill-reparatie]].
- **Tijdens het bouwen 3 nieuwe, echte buggroepen gevonden die noch de Haiku-run, noch de eerdere handmatige steekproef had opgemerkt:**
  1. **19 dode `[[Sources/...]]`-links** in bronsamenvattingen: 14× verwezen naar het niet-bestaande pad `Sources/Onderwerpen%20VNG/...` (moet `Sources/Onderwerpen/...` zijn — vermoedelijk een oude mapnaam die nooit is bijgewerkt in bestaande links), 5× ontbrak het `Onderwerpen/`-segment volledig of stond het in de verkeerde case (`Sources/milieu/...` i.p.v. `Sources/Onderwerpen/Milieu/...`). Alle 19 gecorrigeerd naar het echte bestandspad.
  2. **10 BO's met verouderd `ggm_duplicaat_entiteiten`-schema**: een platte lijst GUID-strings (`- "EAID_..."`) i.p.v. het dict-schema (`entiteit`/`guid`/`beleidsdomein`/`taakveld`) dat de rest van de wiki gebruikt en dat `lint.md` als vereist beschrijft. Opgewaardeerd via opzoeking in `ggm_parsed.json`; `afwijkende_attributen` blanco gelaten (niet automatisch te bepalen). Verificatie: GUID-set vóór en na moest identiek zijn per bestand, anders abort — 10/10 geslaagd.
  3. **Kardinaliteit-check verfijnd**: 46 van de 69 aanvankelijke "mist kardinaliteit"-treffers bleken systematisch `type: generalisatie`-relaties, waar kardinaliteit semantisch niet van toepassing is (is-a-relatie, geen associatie). Script uitgezonderd voor dat type; de resterende 23 (bij `type: associatie`) zijn een echte bevinding, nu aan de gebruiker voorgelegd i.p.v. blind gemeld.
- **Andere verificatie-correcties tijdens bouwen:** "wees-BO"-check aanvankelijk 72 (inclusief Actoren/Rollen, die terecht niet in onderwerpoverzichten voorkomen — eigen namespace, zie [[project_element-schema]]) → beperkt tot `Wiki/Bedrijfsobjecten/`, geeft 6 echte gevallen; "source zonder bronsamenvatting" aanvankelijk 202 (waarvan 134 in `Niet-relevant/`-submappen, een bestaande — zij het nooit gedocumenteerde — conventie voor bewust afgewezen bronnen) → uitgesloten van de telling, blijft 49 over (waarvan de 19 dode links een deel verklaren; rest is echte achterstand, zie `ToDo/ingest-backlog.md`).
- **Niet gefixt (vereist inhoudelijke keuze, niet mechanisch):** 34 BO's met `## Subtypes`-sectie zonder frontmatter-tegenhanger, 33 `bo_relaties.bedrijfsobject`-waarden die geen wiki-link zijn (deels bewust — relatie naar concept zonder eigen BO-pagina), 7 onvolledige `bo_homoniemen`-items, 4 eenzijdige homoniem-verwijzingen, 40 registr*-kandidaten (ruwe grep, vereist per-geval contextbeoordeling).
- **Verificatie:** alle YAML opnieuw geparsed (0 nieuwe fouten; 1 pre-existing fout in `Wiki/GGM/8-volkshuisvesting-leefomgeving/beheer-openbare-ruimte.md`, bevestigd ongewijzigd via `git diff` — buiten scope, gegenereerd bestand). `entiteitendekking.py --all` niet opnieuw gedraaid deze sessie (geen `ggm_guid`/`ggm_entiteit`-wijzigingen die de matching raken, alleen `ggm_duplicaat_entiteiten`-schema en losse links).

## [2026-09-17] fix | Lint-run: Haiku-bevindingen grotendeels ontkracht, 2 echte issues gefixt

- **Aanleiding:** `/lint` (hele wiki) uitgevoerd op Haiku conform skill-voorschrift. Rapport claimde o.a. 344× `domein:` i.p.v. `onderwerp:` als #1-prioriteit, 381 wees-BO's, 1.123 wiki-links zonder alias, 399 sources zonder bronsamenvatting.
- **Verificatie met eigen greps/scripts (zie [[feedback_lint-haiku-verificatie]]) toonde alle vier volledig fictief of sterk overschat:** 0 bestanden gebruiken `domein:` (422 gebruiken al correct `onderwerp:`); echte wees-BO-telling is 2, niet 381; echte alias-schending is 46 (grotendeels in `Wiki/log.md` zelf), niet 1.123; source/bronsamenvatting-matching van de agent brak op paden met spaties.
- **Twee bevindingen wél bevestigd en gefixt:**
  1. 43 `## Bronnen`-secties met onterechte alias (`[[pad|alias]]` i.p.v. `[[pad]]`) — nieuw eenmalig script (niet in `tools/`, want body-content, geen frontmatter) stript de alias binnen Bronnen-secties wiki-breed.
  2. 13 bestanden met stijlfout `""`/`''` i.p.v. blanco in **geneste** velden (`ggm_entiteit`/`ggm_guid`/`ggm_attribuut` onder `bo_subtypes`-items, `afwijkende_attributen` onder `bo_homoniemen`-items) — `migrate_frontmatter_style.py` dekte dit nog niet (alleen top-level velden + `bo_relaties.bedrijfsobject`/`kardinaliteit`). Script uitgebreid met generieke `NESTED_EMPTY_FIELDS`-set zodat dit voortaan wiki-breed wordt meegenomen.
- **Bewust niet gefixt:** `Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/storing-ict.md` heeft een `bo_homoniemen`-item met lege `bedrijfsobject: ""` — dat is een inhoudelijk gat (welke BO is de homoniem-tegenpartij?), geen stijlfout; blanco maken lost niets op.
- **Niet-geverifieerde categorieën** (GGM-duplicaten-secties, subtypes/specialisaties-symmetrie, homoniemen-consistentie, ggm-dekking.md-volledigheid) blijven open — Haiku's tellingen daarover zijn niet te vertrouwen zonder eigen deterministische check.
- **Root cause & lint-skill-fix:** zie [[feedback_lint-haiku-verificatie]] — Haiku's read-only "analyse" bleek op tellings-/aanwezigheidschecks stelselmatig te hallucineren i.p.v. daadwerkelijk elk bestand te doorzoeken. `lint.md` moet checks met een objectief telbaar antwoord (aanwezig/afwezig, aantal) laten uitvoeren via `grep`/een script, niet als vrije-tekst-analyse door het model — narratieve beoordeling (contradicties, verouderde claims, inhoudelijke tegenstrijdigheden) blijft wel bij het model.

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
- **Bronsamenvatting:** [[Wiki/Bronsamenvattingen/informatiebeheer/overheidsinformatiemodel|Overheidsinformatiemodel]]
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

- **Bron:** [[Sources/Onderwerpen/Standaarden/ztc2-begeleidend-document|ZTC2 Begeleidend document v2.1]] (KING, 2014) — gedownload en geconverteerd via convert_pdf
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
- **8 bronsamenvattingen** aangemaakt in Wiki/Bronsamenvattingen/Onderwijs/
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
- 2 bronsamenvattingen aangemaakt in Wiki/Bronsamenvattingen/evenementen/
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
- 1 bronsamenvatting aangemaakt in Wiki/Bronsamenvattingen/dierenwelzijn/
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
