# write-element

**Doel:** een reeds beoordeeld element (bedrijfsobject, actor of rol) vastleggen: grondslag, GGM-match, frontmatter, relaties, pagina en terugmeldingen. Doet zelf géén criteria-toetsing.
**Aanbevolen model:** standaard
**Parameters:** {{element}} — elementnaam (beoordeeld via de prompt `assess-element`), of "onderwerp X" voor alle goedgekeurde elementen van dat onderwerp. Verplicht.
**Benodigde context:** [../context/schrijfregels.md](../context/schrijfregels.md), [../templates/element.md](../templates/element.md), `Sources/GGM/` en `Sources/GGM-repository/ggm_parsed.json`, de bronsamenvattingen van het onderwerp.
**Verwachte uitvoer:** een volledige elementpagina op de juiste locatie, eventuele terugmeldingen, bijgewerkte index/log en onderwerpoverzicht.

## Prompt

Leg vast als element: {{element}}

**Route:** bedrijfsobjecten (business-object/contract/product) volgen stap 1-10; actoren en rollen volgen stap 11. Bij het twee-pagina-patroon (begrip is actor/rol én BO): maak beide pagina's en koppel ze via `element_tegenhangers`.

**Stap 1: Grondslag bepalen** (cascade): directe GGM-entiteit → `ggm-entiteit`; afleidbaar uit GGM-objecten → `ggm-afgeleid`; artefact uit een gemeentelijk proces → `procesobject`; juridisch/beleidsmatig kader → `governance-object`. Het ontbreken van GGM-grondslag is voor proces- en governance-objecten structureel: het GGM modelleert data, geen processen of governance.

**Stap 2: GGM-match zoeken** in `Sources/GGM/`: naam-match (exact of synoniem), definitie-match (vergelijkbare scope), domein-match (zelfde beleidsdomein/taakveld).

**Stap 3: Matchsterkte beoordelen:**

| Matchsterkte | Betekenis | Actie |
|---|---|---|
| exact | Zelfde concept, definitie klopt | Overnemen, definitie uit GGM |
| sterk | Zelfde concept, definitie/scope wijkt licht af | Overnemen, afwijking documenteren en terugmelden |
| partieel | GGM dekt een deel, of BO is aggregatie van meerdere entiteiten | Overnemen met toelichting, terugmelding overwegen |
| zwak | Verwant maar wezenlijk andere scope | Relatie noteren, niet als grondslag gebruiken |

**Stap 4: Mapping-regels.** Voorkeur 1-op-1. Aggregatie toegestaan als het GGM te granulair is (noteer welke entiteiten zijn samengevoegd). Zelfde naam + zelfde concept in meerdere beleidsdomeinen = duplicaat: één BO, thematisch passende GUID primair, rest in `ggm_duplicaat_entiteiten`, terugmelden als `duplicaat`. Zelfde naam + ander concept = homoniem: disambiguerende naam kiezen (stap 4c), terugmelden als `homoniem`.

**Stap 4b: GGM-duplicaten detecteren.** Zoek in `ggm_parsed.json` alle entiteiten met dezelfde naam. Classificeer elk voorkomen (duplicaat of homoniem). Kies de primaire GUID (thematisch passend beleidsdomein) — leg de keuze voor aan de gebruiker. Vergelijk attributen en beschrijf verschillen. Vul frontmatter: `ggm_guid` (primair), `ggm_duplicaat_entiteiten` (duplicaten, geen homoniemen), `bo_synoniemen` (andere namen voor hetzelfde concept), `bo_homoniemen` (per homoniem: `bedrijfsobject`, `ggm_entiteit`, `ggm_guid`, `ggm_beleidsdomein`, `toelichting`). Terugmeldingen naar `Wiki/Analyses/ggm-terugmeldingen.md`.

**Stap 4c: Homoniem-naamkeuze.** Stel 2-3 disambiguerende namen voor (domein-prefix, samengesteld woord, of functionele naam) en leg de keuze voor aan de gebruiker. Regels: geen haakjes in de naam (dus niet de alternate-name-conventie "Inschrijving (Onderwijs)"); de GGM-naam blijft in `ggm_entiteit`, de gekozen naam wordt `naam` en `ggm_gemma_naam`; documenteer in de body-sectie `## Naamkeuze`; de oude naam is géén synoniem (die staat in `bo_homoniemen`).

**Stap 5: GGM-velden ophalen** uit `Sources/GGM-repository/ggm_parsed.json` (bij een nieuwe release eerst de parser draaien, zie [../tools/README.md](../tools/README.md)). Vul het volledige frontmatter-schema van [../templates/element.md](../templates/element.md): de `ggm_*`-velden uit het XMI, de `ggm_gemma_*`-referentievelden uit de GEMMA-tags, en de wiki-velden. Voor `bo_definitie` en `bo_toelichting`: volg de definitieregels in [../context/schrijfregels.md](../context/schrijfregels.md). Disambiguatie: krijgt het BO een andere naam dan de GGM-entiteit, dan `naam` = gekozen naam, `ggm_entiteit` = originele GGM-naam (herleidbaarheid), `ggm_gemma_naam` = exportnaam.

**Stap 6: Hiërarchie vastleggen.** Drie patronen (zie template voor de formats):
- **Generalisatie** (opwaarts, alle niveaus eigen BO): `## Generalisatie`-sectie met de keten, gedeelde kenmerken en het onderscheid van dit niveau; relaties in `bo_relaties`.
- **Specialisaties** (neerwaarts, children wél apart BO): `## Specialisaties`-tabel; `generalisatie`-relaties met `richting: van-dit-BO`, en bij elk child terug met `richting: naar-dit-BO`.
- **Subtypes** (neerwaarts, children géén apart BO): identificeer uit beleidsbronnen (aparte typen met eigen kenmerken), GGM-type-attributen (`type`, `typePlus`, `materiaal` e.d. — attribuutwaarden zijn een implementatiekeuze, geen reden subtypes weg te laten) en GGM-generalisatierelaties. `## Subtypes`-lijst in de body; afwijkingen tussen beleids- en GGM-hiërarchie toelichten.

**Stap 7: Relaties afleiden** van GGM-associaties, vereenvoudigd naar bedrijfsniveau: overnemen (herkenbaar in de praktijk), inkorten (via tussenentiteit die geen BO wordt), samenvoegen (op bedrijfsniveau niet onderscheidbaar), weglaten (puur technisch), toevoegen (bestaat op bedrijfsniveau maar niet in GGM — hiaat-relatie).

**Stap 8: Pagina aanmaken** in `Wiki/Bedrijfsobjecten/{taakveld}/{beleidsdomein}/` (folderstructuur volgt de GGM-indeling), met frontmatter en body-secties volgens het template: criteria-toetsing, beschrijving, hiërarchiesecties (waar van toepassing), GGM-bron (bij GGM-grondslag; letterlijke definitie als blockquote met matchsterkte), naamkeuze/GGM-duplicaten (waar van toepassing), BO-definitie (alleen bij afwijking), relaties, bedrijfsprocessen, bedrijfsfuncties, bronnen, terugmelding.

**Stap 9: Terugmeldingen.** Bij afwijkingen of hiaten een regel toevoegen aan `Wiki/Analyses/ggm-terugmeldingen.md` (typen: hiaat | definitie | structuur | scope | duplicaat | homoniem; status: open). Geen match + data-object = ja → potentieel GGM-hiaat.

**Stap 10: Zonder GGM-grondslag** blijven de `ggm_*`- en `ggm_gemma_*`-velden leeg. Voeg de passende body-sectie toe: **Procesbron** (bij procesobject) of **Juridische bron** (bij governance-object), telkens met een link naar de bronsamenvatting.

**Stap 11: Actor- en rolpagina's.** Locatie: `Wiki/Actoren/{naam}.md` (`archimate_type: business-actor`) of `Wiki/Rollen/{naam}.md` (`business-role`) — beide platte mappen; onderwerp/taakveld staat in de frontmatter. Zelfde frontmatter-schema (`type: element`); GGM-velden leeg zonder match. Doorloop stap 2-5 voor de GGM-match; rollen zonder match zijn vaak governance-hiaten (terugmelding overwegen). Lichtere body: beschrijving, criteria-toetsing, rollen (bij actor) of vervuld-door (bij rol), relaties, bronnen, GGM-bron (bij match). Twee-pagina-patroon: haalt het begrip óók de 6 BO-criteria, maak daarnaast de BO-pagina; koppel via `element_tegenhangers` op beide pagina's plus een cross-linkzin in de body; beide pagina's mogen dezelfde `ggm_guid` dragen, elk met een eigen definitie vanuit het eigen perspectief.

**Nazorg:** `Wiki/index.md`, `Wiki/log.md` en het onderwerpoverzicht bijwerken.

## Voorbeeld

> Leg vast als element: WOZ-object (onderwerp belastingen, beoordeeld: 6/6 criteria, GGM-match exact)
