# audit-definities

**Doel:** `bo_definitie` en `bo_toelichting` van bestaande BO's controleren tegen de definitieregels, en fouten na rapportage herstellen.
**Aanbevolen model:** standaard
**Parameters:** {{scope}} — onderwerp, beleidsdomein, of leeg (= alle BO's). Optioneel.
**Benodigde context:** [../context/schrijfregels.md](../context/schrijfregels.md), de BO-pagina's in scope, hun bronsamenvattingen, `Sources/GGM-repository/ggm_parsed.json`.
**Verwachte uitvoer:** per BO een regel (naam, scenario, status OK/Fout/Waarschuwing, bevinding), gegroepeerd op status, met totalen; daarna herstel per BO na akkoord.

## Prompt

Controleer en herstel de definities van bestaande BO's. Scope: {{scope}}

1. **Verzamel** alle BO-pagina's in scope en lees per BO de frontmatter.
2. **Controleer per BO:**

   **a. GGM-vergelijking** (bij grondslag ggm-entiteit of ggm-afgeleid) — vergelijk `bo_definitie` met `ggm_definitie` en met de bronnen (via de `## Bronnen`-sectie):

   | Scenario | Herkenning | Oordeel |
   |---|---|---|
   | GGM overgenomen | `bo_definitie` ≈ `ggm_definitie` | OK als GGM qua strekking klopt met de bronnen |
   | GGM aangepast zonder reden | wijkt af, maar GGM klopt wél met de bronnen | Fout: GGM had overgenomen moeten worden |
   | GGM terecht afgeweken | wijkt af, GGM klopt niet, body heeft **BO-definitie**-sectie | OK |
   | Afgeweken zonder documentatie | wijkt af, geen **BO-definitie**-sectie | Fout |
   | GGM onvolledig | definitie = GGM, maar bronnen bevatten meer dan `bo_toelichting` | Waarschuwing: `bo_toelichting` overwegen |

   **b. Vormcontrole** — bij voorkeur één zin ≤ 160 tekens (langer alleen als letterlijk overgenomen); kort en leesbaar (geen jargon of ingewikkelde bijzinnen); veld niet leeg; geen "gelijk aan GGM"-placeholder.

   **c. Broncontrole** (bij grondslag procesobject of governance-object) — is `bo_definitie` herleidbaar naar de gelinkte bronsamenvattingen? Bevat een bron een letterlijke definitie, dan had die overgenomen moeten worden.

   **d. `bo_toelichting`** — veld aanwezig (mag leeg); inhoud gebaseerd op bronnen, niets vrij verzonnen.

3. **Rapporteer** per BO: naam (link), scenario, status, korte bevinding. Groepeer: fouten → waarschuwingen → OK. Toon totalen.
4. **Herstel** na akkoord: pas per BO `bo_definitie`/`bo_toelichting` aan volgens de definitieregels in [../context/schrijfregels.md](../context/schrijfregels.md) (bronnen en GGM-definitie lezen, de drie scenario's doorlopen, resultaat terugschrijven). Toon per BO wat is gewijzigd.

## Voorbeeld

> Controleer en herstel de definities van bestaande BO's. Scope: beheer-openbare-ruimte
