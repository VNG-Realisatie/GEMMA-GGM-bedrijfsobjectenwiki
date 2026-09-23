---
type: element
naam: Gemeentebegrafenis
onderwerp: [openbare gezondheid]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Gemeentebegrafenis
ggm_guid: EAID_F2DBE01F_7535_4f26_9DF2_081EF8632F36
ggm_uml_type: Class
ggm_beleidsdomein: Gemeentebegrafenissen
ggm_taakveld: "6 Sociaal Domein"
ggm_diagram: [Gemeente Begrafenissen]
ggm_diagram_ids: [EAID_949AE9E2_95EB_4063_B7C5_E81971D410B3]
ggm_definitie: "Teraardebestelling onder verantwoordelijjkheid van de gemeente."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam: Gemeentebegrafenis
ggm_gemma_guid: "a0f96391-4935-4c7a-be2b-2fa1b00da57f"
ggm_gemma_definitie: "Teraardebestelling onder verantwoordelijjkheid van de gemeente."
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-a0f96391-4935-4c7a-be2b-2fa1b00da57f"
ggm_gemma_bron:
ggm_gemma_alternate_name:

ggm_duplicaat_entiteiten: []

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Gemeentebegrafenis** als directe tegenhanger.
bo_definitie: "Uitvaart die de gemeente verzorgt wanneer niemand anders in de lijkbezorging voorziet, op grond van artikel 21 van de Wet op de lijkbezorging."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[NatuurlijkPersoon]]"
    richting: van-dit-BO
    kardinaliteit: "0..1 → 1..1"
    beschrijving: "De overledene voor wie de gemeente de begrafenis verzorgt"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/begraafplaats|Begraafplaats]]"
    richting: van-dit-BO
    kardinaliteit: "0..* → 1"
    beschrijving: "De gemeentebegrafenis vindt in de regel plaats op een (gemeentelijke) begraafplaats, tenzij de overledene tot crematie of ontleding is bestemd"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/crematorium|Crematorium]]"
    richting: van-dit-BO
    kardinaliteit: "0..* → 0..1"
    beschrijving: "Alternatief voor begraving, als de overledene daartoe is bestemd (art. 21 Wlb)"
bedrijfsprocessen: [lijkbezorging, kostenverhaal gemeentebegrafenis]
bedrijfsfuncties: [volksgezondheid, burgerzaken]
---

## BO-criteria toetsing

| # | Criterium | Toepassing |
|---|---|---|
| 1 | Betekenis binnen onderwerp | Wettelijke taak gemeente op grond van Wet op de lijkbezorging |
| 2 | Herkenbaar voor domeinexperts | Bekend bij burgerzaken en volksgezondheid |
| 3 | Eigen bestaan | Elke gemeentebegrafenis is een zelfstandig geval |
| 4 | Meervoud | Meerdere per jaar per gemeente |
| 5 | Eigen levenscyclus | Melding → opdracht → uitvoering → kostenverhaal → afgedaan |
| 6 | Relaties | Overledene (NatuurlijkPersoon), melder, begraafplaats |

Score: 6/6.

## Beschrijving

Wanneer niemand voorziet in de lijkbezorging van een overledene, is de gemeente op grond van artikel 21 van de Wet op de lijkbezorging verplicht hierin te voorzien. De burgemeester wordt hierop geattendeerd doordat degene die het lijk onder zijn berusting heeft, uiterlijk op de derde dag na het overlijden waarschuwt (art. 20). De gemeente draagt zorg voor de uitvaart — in de regel begraving; crematie is alleen mogelijk als de overledene zijn lijk daartoe uitdrukkelijk heeft bestemd (art. 21 lid 1) — houdt de kosten bij en verhaalt deze waar mogelijk op de nalatenschap, onderhoudsplichtige bloed-/aanverwanten of de werkgever (art. 22). Bij een lijk met onbekende identiteit kan de burgemeester, uitsluitend ten behoeve van identificatie en opsporing van vermiste personen, lichaamsmateriaal laten afnemen (art. 21 lid 3-4).

## GGM-bron

> "Teraardebestelling onder verantwoordelijjkheid van de gemeente."
> — GGM-entiteit: Gemeentebegrafenis (beleidsdomein Gemeentebegrafenissen, taakveld 6 Sociaal Domein)

**Attributen:** melder, begrafeniskosten, gemeentelijkeKosten, verhaaldBedrag, datumBegrafenis, datumAfgedaan, datumGemeld, inkoopordernummer, doodsoorzaak, achtergrondMelding, urenGemeente, datumRuimingGraf

**Matchsterkte:** exact — 1:1 mapping op GGM-entiteit.

Het GGM plaatst deze entiteit onder taakveld 6 (Sociaal Domein). Inhoudelijk hoort lijkbezorging bij volksgezondheid (Wet op de lijkbezorging, Wet publieke gezondheid). Dit is een classificatieverschil in het GGM, geen inhoudelijke afwijking.

## BO-definitie

De GGM-definitie wijkt inhoudelijk af van het gemeentelijke gebruik van dit begrip. De BO-definitie is gebaseerd op de bronnen.

## Relaties

| Gerelateerd object | Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| NatuurlijkPersoon | heeft (overledene) | → | 0..1 → 1..1 | GGM |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/begraafplaats\|Begraafplaats]] | vindt plaats op | → | 0..* → 1 | Art. 21 Wlb |
| [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/openbare-gezondheid/lijkbezorging/crematorium\|Crematorium]] | alternatief | → | 0..* → 0..1 | Art. 21 Wlb |

## Bedrijfsprocessen

- **Lijkbezorging** — melding ontvangen, opdracht geven aan uitvaartondernemer, uitvoering
- **Kostenverhaal** — kosten verhalen op nalatenschap of nabestaanden

## Bronnen

- [[Wiki/Bronsamenvattingen/Openbare Gezondheid/gezondheidsbeleid-en-preventie]]
- [[Wiki/Bronsamenvattingen/Openbare Gezondheid/wet-op-de-lijkbezorging-wettekst]]
