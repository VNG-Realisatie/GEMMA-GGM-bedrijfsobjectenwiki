# Schrijfregels

## Definitieregels (`bo_definitie` en `bo_toelichting`)

Een definitie is **kort, helder en goed leesbaar**: bij voorkeur één zin van maximaal ±160 tekens. Langer mag alleen als de tekst letterlijk uit het GGM of een bron is overgenomen.

Bepaal de definitie zo:

1. **Toets de GGM-definitie aan de bronnen.** Een lege of placeholder-definitie (`~`, `-`, `?`, `TODO`) telt als "geen definitie".
2. **Drie scenario's:**
   - **GGM klopt qua strekking** → GGM-definitie overnemen. Alleen opschonen: taalfouten en HTML-restanten corrigeren; opsommingen en uitweidingen naar `bo_toelichting`. Geen documentatieplicht.
   - **GGM wijkt inhoudelijk af van de bronnen** → eigen definitie op basis van de bronnen (letterlijke brondefinitie overnemen als die er is). Voorstel ter verificatie aan de gebruiker tonen; afwijking documenteren in de body-sectie **BO-definitie**.
   - **GGM klopt maar is onvolledig** → GGM-definitie letterlijk overnemen; de aanvulling in `bo_toelichting`.
3. **Zonder GGM-match** → definitie uit de bronnen afleiden; brondefinitie letterlijk overnemen als die bestaat.
4. **`bo_toelichting`** — uitleg, context en voorbeelden, ook gebaseerd op bronnen (niets vrij verzinnen). Leeg laten als de definitie volstaat.

"Gelijk aan GGM" of een vergelijkbare verwijzing is géén definitie: het veld bevat altijd een zelfstandige tekst.

## Citatie- en verificatieregels

Elke feitelijke claim is traceerbaar naar zijn bron:

1. **Refereer altijd aan bronbestanden** — geen ononderbouwde claims.
2. **Format:** verwijs naar de bronsamenvatting, of citeer direct: `> [citaat] (bron: bestandsnaam)`.
3. **Bij tegenspraak tussen bronnen:** documenteer beide en markeer `⚠️ Tegenspraak` op de pagina.
4. **Zonder bron:** markeer `🔍 Verificatie nodig` en zet het bij de openstaande vragen.
5. **BO-grondslag:** elke BO-pagina heeft een `## Bronnen`-sectie die naar bronsamenvattingen verwijst.
6. **GGM-matching:** onzekere matches markeren als `ter discussie` — niet gokken.

## Herschrijven vs. verplaatsen

Bij het verplaatsen of herstructureren van bestaande wiki-tekst: exact knippen en plakken, niet herschrijven. Herschrijven is alleen aan de orde wanneer daar expliciet om wordt gevraagd of wanneer de definitieregels hierboven het voorschrijven.
