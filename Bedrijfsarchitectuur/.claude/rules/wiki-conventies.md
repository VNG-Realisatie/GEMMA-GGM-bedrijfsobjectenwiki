# Wiki-conventies

## Links
- [WC1] ALTIJD `[[wiki-links]]` voor verwijzingen naar wiki-pagina's en BO's in `Wiki/`-bestanden. NOOIT platte tekst.
- [WC2] Toepassing:
  - `Wiki/Bronsamenvattingen/`: links naar BO's, andere bronsamenvattingen, analyses.
  - `Wiki/Bedrijfsobjecten/`: links naar bronsamenvattingen (veld `bronnen`), gerelateerde BO's (sectie `relaties`), analyses.
  - `Wiki/Onderwerpoverzichten/`: links naar BO's (begrippentabel), bronsamenvattingen ("Verwerkte bronnen").
  - `index.md`, `log.md`: alle verwijzingen zijn wiki-links.
- [WC3] UITZONDERING: frontmatter-velden die naar Sources wijzen (bv. `bron:` in een bronsamenvatting) → markdown-link `[text](path)`. In `Sources/` zelf: [SRC8].

## Scope
- [WC4] ALTIJD gemeentelijk perspectief als scope: wat de gemeente ziet, doet, registreert en beslist.
- [WC5] Ketenpartners (COA, IND, DT&V, UWV e.d.) en externe actoren/processen: ALLEEN als context of afbakening ("buiten scope") noemen. NOOIT een eigen begrips- of BO-pagina; NOOIT hun interne processen uitwerken. Geldt voor alle domeinen.
- [WC6] Een domein dat geen BO's oplevert → afsluiten met een conclusie waarom. Ingest sluit een domein ALTIJD af, ook bij 0 BO's.

## Inhoud van wiki-pagina's
- [WC7] NOOIT vanuit wiki-content (BO-pagina's, begrippen, analyses, bronsamenvattingen) verwijzen naar of citeren uit `CLAUDE.md`, `templates/`, `tools/` of skills (`.claude/commands/`). Onderbouwing staat op eigen kracht in de inhoud.
- [WC8] NOOIT absolute taal ("structureel buiten scope", "per definitie", "GGM modelleert nooit X") zonder domeinspecifieke onderbouwing.
- [WC9] ALS een generieke "GGM doet dit niet"-bewering geen specifieke reden heeft → herformuleer naar "in het GGM niet compleet gedekt". Specifieke reden = ontbrekend beleidsdomein, specifieke wetsverwijzing of attribuutvergelijking.
- [WC10] ALS een bewering een concrete, specifieke reden geeft (bv. "dit beleidsdomein begint pas bij X", "GGM heeft wel BAG-locaties maar niet dit type locatie") → NIET aanpassen, ook niet als het woord "structureel" erin staat.
- [WC11] Bij opschoning van deze framing: per geval beoordelen. NOOIT blind alle "structureel"/"buiten scope" vervangen.

## `/lint`
- [WC15] `/lint` draait bewust op Haiku.
- [WC16] ALTIJD gemelde bevindingen zelf verifiëren (grep/Read/eigen script) vóór ze in het eindrapport komen, voor élke categorie, ook telbare/structurele claims.
- [WC17] NOOIT een getal of "aanwezig/afwezig"-claim vertrouwen zonder eigen deterministische verificatie (grep/Python-script over de volledige set). Een steekproef van 2–3 voorbeelden volstaat NIET voor aggregaat-tellingen. Bij conflict met [WC16] geldt [WC17] voor tellingen en aanwezigheid; een steekproef volstaat alleen voor semantische bevindingen.
- [WC18] Structureel/telbare checks (veldnaam-gebruik, sectie-aanwezigheid, link-tellingen, orphan-detectie) → script `tools/lint_checks.py`. NIET aan het model delegeren.

## Verificatie na regeneratie en subagent-runs
- [WC19] Na elke `entiteitendekking.py --all`: ALTIJD `git status --short` en `git diff --stat` controleren; toets elk gewijzigd bestand aan de eigen bewerkingslijst. NIET alleen de samenvattingstellingen bekijken.
- [WC20] ALS een wijziging onverklaard is (bv. `type:`-velden die terugveranderen naar `bedrijfsobject`; wijzigingen in `Wiki/GGM/`-bestanden) → `git diff` op dat bestand VÓÓR verder werken. NOOIT afdoen als regressie of toeval op basis van dekkingspercentages.
- [WC21] `Wiki/GGM/` NOOIT handmatig bewerken (gegenereerd). Wijzig ALLEEN door te regenereren via `/generate-ggm`. Herstel een ongewenste externe wijziging met `git checkout -- <bestand>`.
- [WC22] Checklist na elke subagent-run (zie [W4]):
  1. `Wiki/Analyses/ggm-terugmeldingen.md`: nieuwe hiaten/correcties uit de BO-pagina's toegevoegd?
  2. `Wiki/index.md`: alle nieuwe BO's en bronsamenvattingen opgenomen?
  3. `Wiki/log.md`: entry klopt met werkelijke aantallen?
  4. `Wiki/Onderwerpoverzichten/{onderwerp}.md`: `bo_count` en `begrippen_count` actueel?
  5. Forward references in BO-pagina's: verwijzen ze naar bestaande bestanden?

## Notes
- Vermoedelijke oorzaak van [WC20]-gevallen: externe editor (VS Code) slaat verouderde buffer van open tab op. Precedent 2026-07-09: `raadsstuk.md` teruggezet naar `type: bedrijfsobject`.
- `templates/element.md` verwijst naar [WC7].
- Precedent [WC9]: GGM-beleidsdomein Normafwijking (Participatiewet-ingest, 2026-09-18) modelleert Maatregel en Boete; dit weerlegde "GGM modelleert nooit processen/governance".
- Precedent [WC17]: lint-run 2026-09-17 meldde 344 (werkelijk 0), 381 (werkelijk 2), 1.123 (werkelijk 46).
