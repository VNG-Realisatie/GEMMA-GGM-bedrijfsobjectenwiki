# Bedrijfsobjecten (BO)

Regels die één skill uitvoert staan in die skill: `/assess-element` (6 criteria, abstract niveau, GGM-hiaten), `/write-element` (duplicaten/homoniemen, definities), `/audit-duplicaten`, `/ingest` (bronselectie, GGM-dekking). Hieronder alleen skill-overstijgende regels.

## Anti-patronen registr*
- [BO4] De 6 BO-criteria zijn de ENIGE toets (`/assess-element` Stap 7). NOOIT "registr*" (registreerbaar, registreren, registratieobject) gebruiken als filter, criterium of motivatie bij BO-beoordeling, begrippentabellen, GGM-hiaat-beoordelingen of inleidende analyses. Ook niet impliciet of als synoniem. UITZONDERING: de typering van data-objecten in `/assess-element` Stap 9–10; die bepaalt NOOIT BO-status.
- [BO5] Vervang: "registreerbaar object" → "zelfstandig object"; "wat gemeenten registreren" → "wat de gemeente herkent als zelfstandig ding"; "geen registratieobject" → afwijzen via de 6 criteria.
- [BO6] Irrelevant als afwijsgrond: "eigendom ligt bij X", "systeembeheer", "regie, niet registratie", "extern systeem".

## BO-naam bij GGM-generalisatie
Scope: BO matcht een GGM-entiteit via generalisatie/specialisatie, matchsterkte "sterk"/"partieel", GGM-entiteit is breder.
- [BO11] STANDAARD: BO-naam blijft het gemeentelijke beleidsbegrip. NIET hernoemen naar de abstractere GGM-entiteitnaam.
- [BO12] Leg de afwijking vast in de bestaande `## GGM-bron`/matchsterkte-toelichting. NOOIT in `## Naamkeuze` (uitsluitend voor homoniem-disambiguatie; zie `templates/element.md`, `/write-element` Stap 4c).
- [BO13] UITZONDERING (zeldzaam, per geval): hernoemen naar de GGM-naam ALLEEN ALS de term geen eigen identiteit heeft: er is in de gemeentelijke bronnen geen ander gebruik van de GGM-entiteit dan deze ene toepassing én de term is geen zelfstandig gedragen beleidsbegrip.
- [BO14] Toets voor [BO13]: zou een domeinexpert dit begrip ooit anders noemen, of gebruiken voor iets anders dan deze ene GGM-toepassing? ALS ja → niet hernoemen.
- [BO15] Bij hernoeming wordt de specifieke term binnen de hernoemde BO een Subtype (geen eigen pagina) OF een Specialisatie (eigen pagina; ALLEEN ALS de term zelf de 6 criteria haalt).
- [BO16] NOOIT in bulk doorvoeren op basis van één eerder akkoord. Bij twijfel of meerdere vergelijkbare gevallen: expliciet per geval voorleggen. Een generiek "ja, overal" is geen akkoord voor bulk.
- [BO17] Bij hernoeming of nieuwe generieke pagina: ALLE wiki-links bijwerken: bare `[[Naam]]`-links in Bronsamenvattingen, `bo_relaties` in andere BO's, onderwerpoverzicht-rijen, `Wiki/index.md`.
- [BO18] Daarna `entiteitendekking.py --all` regenereren en controleren volgens `/entiteitendekking` Stap 1 (controle na de run).

## Wiki-velden
- [BO29] Veldnamen: `bo_definitie`, `bo_toelichting`, `bo_relaties`, `bo_synoniemen` (andere namen voor hetzelfde concept), `bo_homoniemen` (andere concepten met dezelfde GGM-naam). `bo_subtypes`: zie [BO29c]. `bedrijfsprocessen` en `bedrijfsfuncties` behouden hun naam. Prefix `bo_` = wiki-eigen BO-model; `ggm_*` = GGM-bron; `ggm_gemma_*` = GGM-GEMMA-referentie. De export leest de `bo_`-velden.
- [BO29a] `gemma_*`-waarden komen uit het GGM (dat een `gemma.csv` importeert). In `ggm_parsed.json` staan ze als `gemma_tags`; in BO-frontmatter als `ggm_gemma_*`.
- [BO29b] NOOIT `gemma_*`/`ggm_gemma_*` vullen vanuit wiki-beoordeling; wiki-eigen inhoud gaat naar `bo_*`.
- [BO29c] `bo_subtypes` is in gebruik (NIET deprecated): per item `naam`, `omschrijving`, `ggm_entiteit`, `ggm_guid`, `ggm_attribuut`. `tools/entiteitendekking.py` leest de items met `ggm_attribuut: generalisatie` voor de dekking van GGM-specialisaties; lint, export en enrichment gebruiken het ook. NIET verwijderen.

## Notes
- Precedent [BO13]: Woonboot → Vaartuig hernoemd (2026-07-09; Woonboot is de enige toepassing van GGM-entiteit Vaartuig). NIET hernoemd: Evenement, Woning, Rioolleiding (zelfstandige beleidsbegrippen). Rioolleiding = twee pagina's: Leiding (generieke GGM-match) + Rioolleiding (Specialisatie met generalisatie-relatie terug).
