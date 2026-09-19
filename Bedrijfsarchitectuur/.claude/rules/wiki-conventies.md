# Wiki-conventies

## wiki-links-structureel

Alle verwijzingen naar wiki-pagina's en bedrijfsobjecten in Wiki-bestanden moeten `[[wiki-links]]` zijn, nooit platte tekst.

**How to apply:**
- **In Wiki/Bronsamenvattingen/**: links naar BO's, naar andere bronsamenvattingen, naar analyses
- **In Wiki/Bedrijfsobjecten/**: links naar bronsamenvattingen (in `bronnen` veld), links naar gerelateerde BO's (in `relaties` sectie), links naar analyses
- **In Wiki/Domeinen/**: links naar BO's (in begrippentabel), links naar bronsamenvattingen (in "Verwerkte bronnen")
- **In index.md en log.md**: alle verwijzingen zijn wiki-links

Exception: frontmatter-velden die naar sources wijzen (bijv. `bron:` veld in bronsamenvatting) gebruiken markdown-links `[text](path)` omdat sources geen wiki-pagina's zijn.

## gemeentelijk-perspectief

Bij het compileren van bronnen naar wiki-pagina's altijd het gemeentelijk perspectief aanhouden als scope.

**Why:** de wiki is een bedrijfsarchitectuurwiki voor gemeenten. Ketenpartners (COA, IND, DT&V, UWV, etc.) zijn context, niet het onderwerp. De gebruiker wil zien wat de gemeente doet, registreert en beslist — niet de interne processen van andere organisaties.

**How to apply:** begrippen en bedrijfsobjecten worden uitgewerkt voor wat de gemeente ziet. Externe actoren en processen worden benoemd als context/afbakening ("buiten scope") maar krijgen geen eigen begrips- of bedrijfsobjectpagina. Deze regel geldt voor alle domeinen, niet alleen inburgering.

Aanvulling (2026-06-19): "geen resultaat" is ook een resultaat. Een domein dat geen BO's oplevert wordt afgetekend met een conclusie waarom. Ingest tekent een domein altijd af — ook bij 0 BO's. Relevant voor onderhoudscyclus (nieuwe GGM-release, nieuwe bronnen).

## geen-verificatie-bij-publiceren

Sla bij "publiceer"-opdrachten naar redactie.gemmaonline.nl standaard verificatiestappen over — geen
`parse-wikitext`-dry-run om een sjabloon te laten renderen, geen `<categorytree>`-opzoekingen om een
testobject te vinden — tenzij de gebruiker expliciet om verificatie vraagt.

**Why:** die stappen kostten in de praktijk veel meer tokens dan de publicatie zelf. Een
`<categorytree>`-opvraging kan tientallen KB's HTML teruggeven (moet dan naar een bestand worden
weggeschreven), en een `parse-wikitext`-render van een ArchiMate-sjabloon bevat een compleet inline
SVG-diagram. `update-page`/`create-page` sturen bovendien altijd de hele paginabron mee (geen
diff-patching), dus de publicatie zelf is al kostbaar genoeg zonder die extra rondes.

**How to apply:** normale `update-page`/`create-page`-aanroepen (met `latestId` voor conflictdetectie via
`get-page metadata=true`) blijven de standaardroute. Alleen als de gebruiker letterlijk "verifieer" oid.
aangeeft, extra stappen als een live dry-run render of het opzoeken van een representatief testobject
toevoegen. Geldt voor redactie-gemmaonline-toegang / werk binnen `GEMMA online/`.

## lint-haiku-verificatie

Bij `/lint`-runs op de Bedrijfsarchitectuur-wiki (draait bewust op Haiku, zie project-element-schema) altijd een steekproef van de gemelde bevindingen zelf verifiëren (grep/Read/eigen script) vóór ze in het eindrapport komen — dit geldt voor élke categorie, ook pure telbare/structurele claims, niet alleen semantische.

**Why:** bij de lint-run van 2026-07-09 bleken meerdere semantische categorieën vals (archimate_type, registr*-anti-patroon, placeholder-definitie) — zie oorspronkelijke aantekening hieronder. Toen werd aangenomen dat puur telbare/structurele bevindingen (aantal bestanden, sectie-header aanwezig) betrouwbaarder waren. **Die aanname is bij de lint-run van 2026-09-17 ontkracht:** juist de tel-claims waren compleet fictief of enorm overschat — "344 bestanden met `domein:` i.p.v. `onderwerp:`, #1 prioriteit" (werkelijk: 0, veld bestaat niet in de wiki), "381 wees-BO's" (werkelijk: 2), "1.123 wiki-links zonder alias" (werkelijk: 46). Een Haiku-subagent die de hele wiki moet doorzoeken en tellen, hallucineert blijkbaar op schaal i.p.v. daadwerkelijk elk bestand te doorlopen — ook al is de vraag zelf triviaal telbaar. Twee andere bevindingen van dezelfde run (43 aliassen in Bronnen-secties, ~14 lege frontmatter-waarden) kwamen wél nagenoeg exact overeen met eigen verificatie.
Oorspronkelijke aantekening (2026-07-09): "11 BO's met verkeerd archimate_type" (alle 11 bleken correct), "33 registr*-anti-patroon-overtredingen" (geen enkele echte overtreding), "5 BO's met ontbrekende ggm_entiteit/ggm_guid" (alle volledig ingevuld), "koelteplek.md heeft placeholder-definitie" (bevat volwaardige definitie).

**How to apply:** bij een volgende `/lint`-run: (1) laat Haiku draaien zoals voorgeschreven, maar (2) vertrouw geen enkel getal of "aanwezig/afwezig"-claim zonder eigen deterministische verificatie (grep/Python-script over de volledige set) — niet alleen een steekproef van 2-3 voorbeelden, want juist de aggregaat-telling bleek de fout, niet losse voorbeelden. (3) Voor structureel/telbare checks (veldnaam-gebruik, sectie-aanwezigheid, link-tellingen, orphan-detectie) is een grep/script sowieso sneller én betrouwbaarder dan een LLM-narratief — overweeg dit soort checks helemaal niet meer aan het model te delegeren. Het structurele fix is doorgevoerd in `tools/lint_checks.py`.

## externe-wijzigingen-verifieren

Bij het regenereren van `entiteitendekking.py --all`, controleer `git status`/`git diff --stat` op bestanden buiten de eigen bewerkingslijst — niet alleen de samenvattingstellingen in de terminaloutput.

**Why:** op 2026-07-09 verschilde een `--all`-regeneratie onverwacht tussen twee runs (Griffie-taakveld: 9→8 matches) terwijl er geen enkele bewuste wijziging in dat domein was gemaakt. Onderzoek wees uit dat `Wiki/Bedrijfsobjecten/.../griffie/raadsstuk.md` buiten alle uitgevoerde tool-calls om was teruggezet van `type: element` naar het oude `type: bedrijfsobject` (met bijbehorende YAML-herformattering), en `Wiki/GGM/.../griffie.md` (een puur gegenereerd bestand dat nooit handmatig bewerkt hoort te worden) een cosmetische tabel-herformattering had ondergaan. Vermoedelijke oorzaak: een externe editor/extensie (VSCode-omgeving) die een verouderde buffer van een open tab heeft opgeslagen, niet een fout in mijn eigen bewerkingen of subagents. `git checkout -- <bestand>` herstelde beide en de dekking was weer correct.

**How to apply:** na elke `entiteitendekking.py --all`-run, `git status --short` bekijken en elk gewijzigd bestand toetsen aan de eigen bedoelde bewerkingslijst. Onverklaarde wijzigingen (vooral `type:`-velden die terugveranderen, of Wiki/GGM/-bestanden die zouden moeten stilstaan) zijn een signaal om `git diff` op dat specifieke bestand te bekijken vóór verder te gaan — niet alleen de dekkingspercentages als "regressie" of "toeval" afdoen.
