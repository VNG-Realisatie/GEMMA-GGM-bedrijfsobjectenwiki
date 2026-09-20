# Bedrijfsobjecten (BO)

## BO-beoordeling
- [BO1] De 6 BO-criteria zijn de ENIGE toets: betekenis, herkenbaarheid, eigen bestaan, meervoud, levenscyclus, relaties.
- [BO2] ALS ≥5 van de 6 ja → BO.
- [BO3] Beslisvraag: herkent de gemeente dit als een zelfstandig ding waar beleid op gemaakt wordt?
- [BO4] NOOIT "registr*" (registreerbaar, registreren, registratieobject) gebruiken als filter, criterium of motivatie bij BO-beoordeling, begrippentabellen, GGM-hiaat-beoordelingen of inleidende analyses. Ook niet impliciet of als synoniem. UITZONDERING: de typering in [BO36]–[BO39]; die bepaalt NOOIT BO-status.
- [BO5] Vervang: "registreerbaar object" → "zelfstandig object"; "wat gemeenten registreren" → "wat de gemeente herkent als zelfstandig ding"; "geen registratieobject" → afwijzen via de 6 criteria.
- [BO6] Irrelevant als afwijsgrond: "eigendom ligt bij X", "regie, niet registratie", "extern systeem".
- [BO7] Bronbeoordeling (ingest stap 3): NOOIT een bron afwijzen omdat die niet beschrijft wat gemeenten registreren. Toets ALLEEN of de bron objecten bevat die de 6 criteria halen. Governance-/strategiedocumenten noemen concrete objecten (applicatie, dataproduct, overeenkomst) die BO-kandidaat kunnen zijn.
- [BO8] Generalisatie/specialisatie: toets het abstracte niveau (bv. "Maatschappelijke voorziening") aan de 6 criteria. NOOIT categorisch uitsluiten, ook niet als specialisaties herkenbaar zijn en eigen processen hebben.
- [BO9] ALS het abstracte niveau de criteria haalt → BO met opsomming van subtypes. Twee uitkomsten: (a) abstract haalt niet → alleen specialisaties worden BO; (b) abstract en specialisaties halen allen → allen worden BO.
- [BO10] [BO4]–[BO6] gelden ook bij [BO8].

## BO-naam bij GGM-generalisatie
Scope: BO matcht een GGM-entiteit via generalisatie/specialisatie, matchsterkte "sterk"/"partieel", GGM-entiteit is breder.
- [BO11] STANDAARD: BO-naam blijft het gemeentelijke beleidsbegrip. NIET hernoemen naar de abstractere GGM-entiteitnaam.
- [BO12] Leg de afwijking vast in de bestaande `## GGM-bron`/matchsterkte-toelichting. NOOIT in `## Naamkeuze` (uitsluitend voor homoniem-disambiguatie; zie `templates/element.md`, `/write-element` Stap 4c).
- [BO13] UITZONDERING (zeldzaam, per geval): hernoemen naar de GGM-naam ALLEEN ALS de term geen eigen identiteit heeft: er is in de gemeentelijke bronnen geen ander gebruik van de GGM-entiteit dan deze ene toepassing én de term is geen zelfstandig gedragen beleidsbegrip.
- [BO14] Toets voor [BO13]: zou een domeinexpert dit begrip ooit anders noemen, of gebruiken voor iets anders dan deze ene GGM-toepassing? ALS ja → niet hernoemen.
- [BO15] Bij hernoeming wordt de specifieke term binnen de hernoemde BO een Subtype (geen eigen pagina) OF een Specialisatie (eigen pagina; ALLEEN ALS de term zelf de 6 criteria haalt).
- [BO16] NOOIT in bulk doorvoeren op basis van één eerder akkoord. Bij twijfel of meerdere vergelijkbare gevallen: expliciet per geval voorleggen. Een generiek "ja, overal" is geen akkoord voor bulk.
- [BO17] Bij hernoeming of nieuwe generieke pagina: ALLE wiki-links bijwerken: bare `[[Naam]]`-links in Bronsamenvattingen, `bo_relaties` in andere BO's, onderwerpoverzicht-rijen, `Wiki/index.md`.
- [BO18] Daarna `entiteitendekking.py --all` regenereren en controleren volgens [WC19]–[WC21].

## Duplicaten en homoniemen
- [BO19] Bij ingest en `/write-element`: check `ggm_parsed.json` en bestaande BO's op alle voorkomens van de entiteitnaam (automatische detectie = signaal). Duplicaat of homoniem is een menselijke beslissing.
- [BO20] Duplicaat (zelfde concept, meerdere GGM-GUIDs): ÉÉN BO-bestand per concept; plaatsing per geval beoordelen (geen vaste domeinregel).
- [BO21] Duplicaat: bewaar alle GGM-GUIDs in frontmatter `ggm_duplicaat_entiteiten`.
- [BO22] Duplicaat: cross-links in frontmatter (`bo_synoniemen`) én in een body-sectie.
- [BO23] De GEMMA-export genereert bij een duplicaat één rij per GUID, alle naar hetzelfde concept.
- [BO24] Homoniem (zelfde GGM-naam, ander concept): elk concept krijgt een eigen BO met een betere eigen naam en behoudt de eigen GGM-GUID.
- [BO25] Homoniem: leg 2–3 alternatieve namen aan de gebruiker voor; de gebruiker kiest; leg de gekozen naam vast.
- [BO26] Homoniem: documenteer in frontmatter `bo_homoniemen` (verwijzing naar de andere BO's met dezelfde GGM-naam) én in de body waarom de naam van het GGM afwijkt.
- [BO27] Homoniem: body-sectie `## Naamkeuze` met overwogen namen en motivatie.
- [BO28] Retroactieve correctie ALTIJD via `/audit-duplicaten` (alle BO's doorlopen, matches in `ggm_parsed.json`, voorstel per conflict). NOOIT via eenmalige bulk-actie.

## Wiki-velden
- [BO29] Veldnamen: `bo_definitie`, `bo_toelichting`, `bo_relaties`, `bo_synoniemen` (andere namen voor hetzelfde concept), `bo_homoniemen` (andere concepten met dezelfde GGM-naam). `bo_subtypes` is deprecated. `bedrijfsprocessen` en `bedrijfsfuncties` behouden hun naam. Prefix `bo_` = wiki-eigen BO-model; `ggm_*` = GGM-bron; `ggm_gemma_*` = GGM-GEMMA-referentie. De export leest de `bo_`-velden.
- [BO29a] `gemma_*`-velden bevatten waarden uit het bestaande GEMMA-model, via import/ingest van dat model. Die import is nog NIET uitgevoerd.
- [BO29b] NOOIT `gemma_*`-velden vullen vanuit wiki-beoordeling; wiki-eigen inhoud gaat naar `bo_*`.

## Definities (`bo_definitie`, `bo_toelichting`)
- [BO30] `bo_definitie`: beschrijf wat het ding IS, niet waar het staat (zie [BO4]). 1 zin, max ~160 tekens. Langer ALLEEN ALS letterlijk overgenomen uit GGM of bron.
- [BO31] Gebruik ALLEEN informatie uit de Sources-bestanden van het onderwerp. Bron met definitie → letterlijk overnemen. Bron zonder expliciete definitie → afleiden uit het gebruik van het begrip in de bronnen.
- [BO32] Toets eerst de GGM-definitie aan de bronnen:
  - klopt qua strekking → GGM-definitie letterlijk overnemen; niet aanpassen; brontekst tonen niet nodig;
  - wijkt inhoudelijk af → nieuwe definitie afleiden uit de bronnen en voorleggen ter verificatie met brontekst en bronverwijzing;
  - klopt maar onvolledig → GGM-definitie behouden in `bo_definitie`; aanvulling in `bo_toelichting`.
- [BO33] Eigen definitie ALLEEN bij inhoudelijke afwijking van de bronnen, en verifieerbaar.
- [BO34] `bo_toelichting`: aanvullingen, uitleg en voorbeelden, gebaseerd op bronnen. NOOIT verzinnen.

## GGM-hiaten
- [BO35] Bepaal voor elke BO zonder GGM-grondslag via [BO36]–[BO40] of het een hiaat is.
- [BO36] Classificeer: Dataobject (registreerbare gegevens), Proces (hoe werk verloopt), Governance-instrument (wet/verordening/bevoegdheid).
- [BO37] Dataobject → rapporteer als (potentieel) hiaat. Proces of Governance → NIET rapporteren, TENZIJ een specifiek, aanwijsbaar GGM-beleidsdomein dit deel wél modelleert (precedent: beleidsdomein Normafwijking modelleert Maatregel en Boete).
- [BO38] Motiveer een dataobject-hiaat: waar registreert de gemeente dit, welke attributen zijn relevant, past het in een bestaand (beleids)domein?
- [BO39] Formuleer: `**[Object]** — [Registratieobject] [waarom relevant] [waar zou passen]`.
- [BO40] Wees conservatief: bij twijfel NIET rapporteren. Taal: NOOIT "structureel buiten GGM-scope" of "per definitie uit scope"; ALTIJD "doorgaans niet compleet gedekt" met een concrete, domeinspecifieke reden waar mogelijk (zie [WC8]–[WC11]).

## GGM-dekking bij ingest
- [BO41] NOOIT een BO-beoordeling of beleidsdomein overslaan omdat het GGM daar al entiteiten heeft. Ingest verifieert ook het GGM: klopt het, is het compleet, zit het op het juiste abstractieniveau.
- [BO42] Neem ALLE relevante GGM-beleidsdomeinen op in begrippentabel en BO-beoordeling.
- [BO43] Markeer per GGM-entiteit of de beleidsbron deze bevestigt, nuanceert of aanvult.
- [BO44] BO-pagina voor een GGM-entiteit volgt exact hetzelfde template als een nieuwe BO: volledige 6-punts criteria-lijst, `# Naam`-heading met definitie, beschrijving, relaties met wiki-links. GEEN verkorte body.

## Notes
- Precedent [BO13]: Woonboot → Vaartuig hernoemd (2026-07-09; Woonboot is de enige toepassing van GGM-entiteit Vaartuig). NIET hernoemd: Evenement, Woning, Rioolleiding (zelfstandige beleidsbegrippen). Rioolleiding = twee pagina's: Leiding (generieke GGM-match) + Rioolleiding (Specialisatie met generalisatie-relatie terug).
- Voorbeelden [BO37]: rapporteren — Stembureau, Gemeenschappelijke Regeling. Niet rapporteren — Verkiezing, Referendum (proces), Verordening (governance).
