# Bedrijfsobjecten

## abstract-bo-niveau

Bij generalisatie/specialisatie-structuren: het abstracte niveau (bijv. "Maatschappelijke voorziening") mag een BO worden als het zelf de 6 BO-criteria haalt, ook wanneer de specialisaties herkenbaar zijn en eigen processen hebben.

**Why:** De assess-bo skill bevatte een regel die het abstracte niveau categorisch uitsloot wanneer specialisaties eigen processen hadden. Dit leidde tot een onjuiste afwijzing van "Maatschappelijke voorziening" als BO. De skill is aangepast (stap 4 beslisregel).

**How to apply:** Beoordeel het abstracte niveau altijd op de 6 criteria. Als het haalt → BO met opsomming van subtypes. Twee situaties: (1) alleen specialisaties worden BO (abstract haalt criteria niet), (2) zowel abstract als specialisaties worden BO (beide halen criteria). Zie [[bo-niet-alleen-registratie]] voor de anti-patronen die ook hier van toepassing zijn.

## bo-naam-ggm-generalisatie

Als een BO-pagina matcht met een GGM-entiteit via een generalisatie/specialisatie-relatie (matchsterkte "sterk"/"partieel", GGM-entiteit is breder), **blijft de BO-naam in principe het gemeentelijke beleidsbegrip** — dit is GEEN reden om de BO te hernoemen naar de (abstractere) GGM-entiteitnaam. De afwijking hoort thuis in de bestaande `## GGM-bron`/matchsterkte-toelichting, niet in een `## Naamkeuze`-sectie (die is uitsluitend voor homoniem-disambiguatie, zie `templates/element.md` en `/write-element` Stap 4c).

**Uitzondering (zeldzaam, per geval te beoordelen):** hernoemen naar de GGM-naam kan wél zinvol zijn wanneer de specifieke term **geen eigen identiteit heeft los van** "de volledige praktijkscope van deze ene GGM-entiteit" — d.w.z. er is geen enkel ander gebruik van de GGM-entiteit in de gemeentelijke bronnen dan deze ene specifieke toepassing, en de term zelf is geen zelfstandig gedragen beleidsbegrip. Bij zo'n hernoeming: de specifieke term wordt een Subtype (geen eigen pagina) of Specialisatie (eigen pagina, als hij zelf de 6 BO-criteria haalt) binnen de hernoemde BO.

**Why:** op 2026-07-09 werd `Wiki/Bedrijfsobjecten/.../vth/woonboot.md` hernoemd naar `vaartuig.md` op expliciet verzoek van de gebruiker ("ik verwacht een BO vaartuig met daarin genoemd de specialisaties") — Woonboot is de enige praktijktoepassing van GGM-entiteit Vaartuig, geen zelfstandig beleidsbegrip los daarvan. Ik generaliseerde dit vervolgens te snel naar 8 andere gevallen (Evenement/OpenbareActiviteit, Woning/Gebouw, Horecabedrijf/Vestiging, Aandachtsgebied+Voorschriftengebied/Gebiedsaanwijzing, Risicobron/Activiteit, Rioolleiding/Leiding, Gezinsmigrant) en begon Evenement te hernoemen naar OpenbareActiviteit. De gebruiker greep in: "evenement moet blijven... woonboot en vaartuig zijn eerder de uitzondering. waarom doe je dit" — Evenement is een zelfstandig, breed gedragen beleidsterm (eigen reserveringskalender, beoordelingscriteria, vergunningenproces) die niemand zou opzoeken onder de GGM-naam. Woning en Rioolleiding bleken bij toetsing hetzelfde: zelfstandige beleidsbegrippen, dus NIET hernoemen. Voor Rioolleiding koos de gebruiker wél een aparte oplossing: 2 pagina's (Leiding = generieke GGM-match, Rioolleiding = eigen Specialisatie-pagina met generalisatie-relatie terug) — dus geen hernoeming van Rioolleiding zelf, wel een nieuwe generieke ouderpagina ernaast.

**How to apply:** bij een BO met matchsterkte "sterk"/"partieel" waar de GGM-entiteit breder is: standaard NIETS wijzigen aan de BO-naam — de bestaande GGM-bron-sectie volstaat. Overweeg een structuurwijziging alleen als getoetst is dat de specifieke term werkelijk geen zelfstandige identiteit heeft (test: zou een domeinexpert dit begrip ooit anders noemen, of gebruiken voor iets anders dan deze ene GGM-toepassing?). Bij twijfel of bij een schaalbare wijziging (meerdere vergelijkbare gevallen tegelijk): niet in bulk doorvoeren op basis van één eerder akkoord — expliciet per geval voorleggen, zeker nadat een generiek "ja, overal" antwoord al eens tot een verkeerde bulk-actie heeft geleid. Bij een wél-gekozen hernoeming of nieuwe generieke pagina: ALLE wiki-links bijwerken (bare `[[Naam]]`-links in Bronsamenvattingen, `bo_relaties` in andere BO's, onderwerpoverzicht-rijen, `Wiki/index.md`), en na afloop `entiteitendekking.py --all` regenereren + `git status` checken op onverwachte bestanden (zie [[feedback_externe-wijzigingen-verifieren]]).

## bo-niet-alleen-registratie

NOOIT het woord "registreerbaar" of "registreren" gebruiken als filter, criterium of motivatie bij BO-beoordeling. Ook niet impliciet via formuleringen als "geen registratieobject", "niet registreerbaar", "wat gemeenten registreren".

**Why:** Herhaaldelijk gecorrigeerd (4+ keer). Het patroon is hardnekkig: zelfs na eerdere correcties duikt "registreerbaar" steeds weer op als impliciete filter — in begrippentabellen, in GGM-hiaat-beoordelingen, en in inleidende analyses. De 6 BO-criteria zijn de ENIGE toets.

**Anti-patronen (NIET gebruiken, ook niet als synoniem):**
- "registreerbaar object" → gebruik "zelfstandig object"
- "wat gemeenten registreren" → gebruik "wat de gemeente herkent als zelfstandig ding"
- "geen registratieobject" → gebruik de 6 criteria om af te wijzen
- "eigendom ligt bij X" → irrelevant
- "regie, niet registratie" → irrelevant
- "extern systeem" → irrelevant

**How to apply:** Bij ELKE BO-beoordeling en begrippentabel: stel ALLEEN de 6 vragen (betekenis, herkenbaarheid, eigen bestaan, meervoud, levenscyclus, relaties). Gebruik het woord "registr*" niet in de motivatie. Als 5+ van de 6 ja zijn → BO. De enige vraag is: herkent de gemeente dit als een zelfstandig ding waar beleid op gemaakt wordt?

**Let ook op bij bronbeoordeling (stap 3 ingest):** beoordeel bronnen niet als "niet relevant omdat ze niet beschrijven wat gemeenten registreren". Governance-/strategiedocumenten benoemen concrete objecten (applicatie, dataproduct, overeenkomst) die BO-kandidaat kunnen zijn. De vraag is niet of de bron over registratie gaat, maar of er objecten in staan die de 6 criteria halen.

## dubbele-namen

## Duplicaten (zelfde concept, meerdere GGM-GUIDs)

- Eén BO-bestand per concept, plaatsing per geval beoordelen (geen vaste regel voor domein)
- Alle GGM-GUIDs bewaren in `ggm_duplicaat_entiteiten` frontmatter
- GEMMA-export genereert meerdere rijen (één per GUID), alle verwijzend naar hetzelfde concept
- Cross-links in frontmatter (`bo_synoniemen` veld) én body-sectie

**Why:** GGM hergebruikt dezelfde entiteit in meerdere beleidsdomeinen met aparte GUIDs. De wiki moet dit consolideren tot één BO maar de GUIDs behouden voor traceerbaarheid en GEMMA-export.

**How to apply:** Bij write-bo en ingest: check ggm_parsed.json op alle voorkomens van de entiteitnaam. Bij match: classificeer als duplicaat of homoniem. Eén BO aanmaken, duplicaat-GUIDs in frontmatter.

## Homoniemen (zelfde GGM-naam, ander concept)

- Elk concept krijgt een eigen BO met een betere, eigen naam
- Meerdere naamsuggesties voorleggen aan gebruiker — gebruiker kiest
- Eigen GGM-GUID behouden per BO
- Documenteer in frontmatter (`bo_homoniemen` veld) en body waarom de naam afwijkt van GGM

**Why:** Dezelfde GGM-entiteitnaam (bijv. "Inschrijving") kan fundamenteel andere concepten aanduiden. Zonder disambiguatie is de wiki verwarrend en is de GEMMA-export onjuist.

**How to apply:** Bij homoniem-detectie: stel 2-3 alternatieve namen voor. Leg de gekozen naam vast. Voeg `bo_homoniemen` frontmatter toe met verwijzing naar de andere BO's met dezelfde GGM-naam.

## Wiki-velden (bo_ prefix)

Het "GEMMA wiki"-blok is hernoemd naar "Wiki-velden" met `bo_` prefix:
- `gemma_definitie` → `bo_definitie`
- `gemma_subtypes` → `bo_subtypes` (deprecated)
- `relaties` → `bo_relaties`
- `bo_synoniemen`: lijst van andere namen voor hetzelfde concept (nieuw)
- `bo_homoniemen`: lijst van andere concepten met dezelfde GGM-naam (nieuw)
- `bedrijfsprocessen` en `bedrijfsfuncties` behouden hun naam

**Why:** De `bo_` prefix maakt duidelijk dat dit het wiki-eigen BO-model is, los van de GGM-bron (`ggm_*`) en de GGM-GEMMA referentie (`ggm_gemma_*`). Bij export worden de `bo_` velden ingelezen in de GEMMA.

Body: `## Naamkeuze` sectie met overwogen namen en motivatie bij homoniem-disambiguatie.

## Detectie

- Automatische detectie bij ingest als signaal (check bestaande BO's + ggm_parsed.json)
- Menselijke beslissing over classificatie (duplicaat vs. homoniem)

## Retroactieve correctie

- Via een `/audit-duplicaten` skill: systematisch alle BO's doorlopen, matches in ggm_parsed.json, voorstel per conflict
- Niet via eenmalige bulk-actie maar via skill die herbruikbaar is

Zie ook: [[ggm-dekking-verificatie]], [[ggm-hiaten-checklist]]

## korte-definities

## gemma_definitie

- Kort, helder, goed leesbaar — bij voorkeur 1 zin, max ~160 tekens.
- Langer mag alleen als de tekst letterlijk uit GGM of bron wordt overgenomen.
- De definitie moet beschrijven wat het ding ís, niet waar het staat. Zie [[bo-niet-alleen-registratie]].

## GGM-definitie vs. eigen definitie

Drie scenario's:
1. **GGM-definitie klopt qua strekking met bronnen** → letterlijk overnemen, niet aanpassen.
2. **GGM-definitie wijkt inhoudelijk af van bronnen** → nieuwe definitie afleiden uit bronnen. Voorleggen ter verificatie met brontekst.
3. **GGM-definitie klopt maar is onvolledig** → GGM-definitie behouden in gemma_definitie, aanvulling in gemma_toelichting.

**Why:** GGM-definities zijn de standaard en moeten niet onnodig afwijken. Alleen bij inhoudelijke afwijking van de bronnen is een eigen definitie gerechtvaardigd, en die moet verifieerbaar zijn.

## Brongebruik

- Gebruik alleen informatie uit de Sources-bestanden van het onderwerp.
- Als een bron een definitie bevat: letterlijk overnemen.
- Als een bron geen expliciete definitie heeft: afleiden uit hoe het begrip in de bronnen wordt gebruikt.
- Bij afwijking van GGM: brontekst tonen ter verificatie. Bij overname van GGM is dat niet nodig.

## gemma_toelichting

- Bevat aanvullingen, uitleg en voorbeelden.
- Ook gebaseerd op bronnen, niet vrij verzonnen.

**How to apply:** Bij het schrijven/beoordelen van BO-frontmatter: eerst GGM-definitie toetsen aan bronnen. Bij match → overnemen. Bij afwijking → eigen definitie met bronverwijzing voorleggen. Aanvullingen altijd naar gemma_toelichting.

## ggm-hiaten-checklist

Voor elke BO zonder GGM-grondslag moet je via deze checklist bepalen of het werkelijk een hiaat is of (nog) geen GGM-dekking heeft.

**Correctie (2026-09-18, zie [[feedback_geen-technische-verwijzingen-wiki]]):** "structureel buiten GGM-scope"/"per definitie uit scope" is een te absolute formulering — het GGM-beleidsdomein Normafwijking modelleert wél een deel van het handhavingsproces (Maatregel, Boete). De juiste framing: procesobjecten/governance-objecten zijn *doorgaans niet compleet gedekt* in het GGM, geen categorische uitsluiting. Dit verandert de conclusie van de checklist niet wezenlijk (nog steeds: wees conservatief, meld proces/governance niet standaard als hiaat) maar wél de *taal* waarin je dat vastlegt — nooit "buiten scope per definitie", wel "niet compleet gedekt" met een concrete, domeinspecifieke reden waar mogelijk.

## Checklist

**Stap 1: Wat is dit BO?**
- Dataobject (registreerbare gegevens)?
- Proces (hoe werk verloopt)?
- Governance-instrument (wet/verordening/bevoegdheid)?

**Stap 2: GGM-dekking check**

| Type | GGM-dekking? | Rapporteren als hiaat? |
|---|---|---|
| Dataobject | Doorgaans wel gedekt | ✅ JA (potentieel hiaat) |
| Proces | Doorgaans niet compleet gedekt | ❌ NEEN, tenzij een specifiek, aanwijsbaar GGM-beleidsdomein dit deel wél modelleert (zie Normafwijking-precedent) |
| Governance | Doorgaans niet compleet gedekt | ❌ NEEN, zelfde voorbehoud |

**Stap 3: Voor dataobjecten: motiveer**
- Waar registreert de gemeente dit?
- Welke attributen zijn relevant?
- Pakt het in bestaand domein/beleidsdomein?

**Stap 4: Formuleer**
> **[Object]** — [Registratieobject] [waarom relevant] [waar zou passen]

**Wees conservatief.** Twijfel = niet rapporteren.

## Voorbeelden

✅ **Rapporteren (dataobject):**
- Stembureau — registreerbare locatie + capaciteit voor stemmingen
- Gemeenschappelijke Regeling — registreerbare juridische entiteit met eigenschappen

❌ **Niet rapporteren (proces/governance):**
- Verkiezing — proces (gemeente registreert uitslagen, niet "verkiezing" zelf)
- Referendum — proces (gemeente voert uit, registreert niet als object)
- Verordening — governance-instrument (regelgeving, niet registratie)

## Waarom dit werkt

Het GGM is een **informatiemodel**: het beschrijft wat informatiesystemen opslaan, niet hoe werk verloopt. Hiaten melden heeft alleen zin als het BO daadwerkelijk in die scope past.

## ggm-dekking-verificatie

Bestaande GGM-dekking is geen reden om BO-beoordeling over te slaan. De ingest is ook een verificatie van het GGM — beleidsbronnen toetsen tegen GGM-entiteiten om te checken of ze kloppen, compleet zijn, en op het juiste abstractieniveau zitten.

**Why:** Het doel van de wiki is niet alleen nieuwe BO's vinden, maar ook bestaande GGM-entiteiten onderbouwen en verifiëren vanuit beleidsperspectief. Overslaan van een heel beleidsdomein (bijv. Parkeren) omdat het GGM daar al entiteiten heeft, mist het verificatiedoel.

**How to apply:** Bij elke ingest alle relevante GGM-beleidsdomeinen meenemen in de begrippentabel en BO-beoordeling, ook als het GGM daar al entiteiten voor heeft. Markeer per GGM-entiteit of de beleidsbron deze bevestigt, nuanceert, of aanvult. BO-pagina's voor GGM-entiteiten volgen exact hetzelfde template als nieuwe BO's: volledige 6-punts criteria-lijst, `# Naam` heading met definitie, beschrijving, relaties met wiki-links. Geen shortcuts of verkorte body. Zie ook [[bo-niet-alleen-registratie]].
