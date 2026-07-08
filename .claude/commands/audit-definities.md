Controleer en herstel definities van bestaande BO's: $ARGUMENTS

Input: onderwerp (alle BO's in dat onderwerp), beleidsdomein, of leeg (= alle BO's).

Controleert `bo_definitie` en `bo_toelichting` tegen de definitieregels uit `/write-element` stap 5.

## Stap 1: BO's verzamelen

Verzamel alle BO-pagina's in scope. Lees per BO het frontmatter.

## Stap 2: Per BO controleren

### 2a. GGM-vergelijking (bij grondslag `ggm-entiteit` of `ggm-afgeleid`)

Vergelijk `bo_definitie` met `ggm_definitie` en de bronnen in `Wiki/Bronsamenvattingen/` (via de `## Bronnen`-sectie van het BO).

Classificeer het scenario:

| Scenario | Herkenning | Verwacht resultaat |
|---|---|---|
| **GGM overgenomen** | `bo_definitie` is (nagenoeg) gelijk aan `ggm_definitie` | OK als GGM qua strekking klopt met bronnen |
| **GGM aangepast zonder reden** | `bo_definitie` wijkt af van `ggm_definitie`, maar GGM klopt wél met bronnen | Fout: GGM-definitie had overgenomen moeten worden |
| **GGM terecht afgeweken** | `bo_definitie` wijkt af, GGM klopt niet met bronnen, body bevat **BO-definitie** sectie | OK |
| **GGM afgeweken zonder documentatie** | `bo_definitie` wijkt af, maar geen **BO-definitie** body-sectie | Fout: afwijking niet gedocumenteerd |
| **GGM onvolledig** | `bo_definitie` = GGM, maar aanvulling ontbreekt in `bo_toelichting` terwijl bronnen meer info bevatten | Waarschuwing: overweeg `bo_toelichting` |

### 2b. Vormcontrole

| Check | Criterium | Fout als |
|---|---|---|
| Lengte | Bij voorkeur ≤160 tekens, langer mag alleen als letterlijk uit GGM of bron | >160 tekens én niet letterlijk overgenomen |
| Zinnen | Bij voorkeur 1 zin | Meerdere zinnen én niet letterlijk overgenomen |
| Leesbaarheid | Kort, helder, goed leesbaar | Technisch jargon, ingewikkelde bijzinnen |
| Veld aanwezig | `bo_definitie` mag niet leeg zijn | Leeg veld |
| Geen "gelijk aan GGM" | `bo_definitie` moet een zelfstandige tekst zijn | Bevat "gelijk aan GGM" of vergelijkbare verwijzing |

### 2c. Broncontrole (bij grondslag `procesobject` of `governance-object`)

Zonder GGM-match: controleer of `bo_definitie` herleidbaar is naar de gelinkte bronsamenvattingen. Als een bron een letterlijke definitie bevat, had die overgenomen moeten worden.

### 2d. bo_toelichting

| Check | Criterium |
|---|---|
| Veld bestaat | `bo_toelichting` in frontmatter (mag leeg zijn) |
| Inhoud gebaseerd op bronnen | Geen vrij verzonnen uitleg of voorbeelden |

## Stap 3: Rapportage

Geef per BO een regel met:
- BO-naam (wiki-link)
- Scenario (GGM overgenomen / GGM aangepast / etc.)
- Status: OK / Fout / Waarschuwing
- Bevinding (kort)

Groepeer op status: eerst fouten, dan waarschuwingen, dan OK.

Toon samenvattende tellingen: totaal gecontroleerd, fouten, waarschuwingen, OK.

## Stap 4: Herstel

Na rapportage: bied aan om de fouten te herstellen. Pas per BO `bo_definitie` en `bo_toelichting` opnieuw af volgens de regels in `/write-element` stap 5 (paragraaf **Wiki-velden**). Lees de bronsamenvattingen en GGM-definitie, doorloop de drie scenario's, en schrijf het resultaat terug.

Voer herstel per BO uit en toon wat is gewijzigd.
