# Adapter: chat-tools (ChatGPT, Gemini, Open WebUI)

Chat-tools hebben geen directe bestandstoegang; je geeft context mee als systeeminstructie, projectkennis of bijlage.

## Eenmalig instellen

1. Maak een project/GPT/gem aan (ChatGPT Projects, Gemini Gems, Open WebUI workspace).
2. Zet [../AGENTS.md](../AGENTS.md) in de systeeminstructie (custom instructions).
3. Upload de `context/`-bestanden als projectkennis; voeg voor schrijftaken ook de relevante `templates/` toe.

Open WebUI: maak een "knowledge collection" van `Opzet/` en koppel die aan een custom model met AGENTS.md als systeemprompt.

## Per taak

1. Open het promptbestand in [../prompts/](../prompts/) en vul de `{{parameters}}` in.
2. Plak de ingevulde prompt in de chat.
3. Voeg de bestanden onder **Benodigde context** toe als bijlage (bijv. het onderwerpoverzicht en de bron), plus de bestanden waarop de taak moet werken.
4. Resultaten (nieuwe of gewijzigde pagina's) kopieer je zelf terug naar de wiki — chat-tools schrijven niet in je bestanden. Vermeld dat in de log-entry.

## Beperkingen

- Taken die scripts draaien ([entiteitendekking](../prompts/entiteitendekking.md), [generate-ggm](../prompts/generate-ggm.md), [export-ggm](../prompts/export-ggm.md), [convert-pdf](../prompts/convert-pdf.md)) vereisen een omgeving met shell-toegang — draai het script zelf lokaal en geef de output aan de chat.
- Grote sweeps (lint, audits over de hele wiki) passen niet in één chatcontext; beperk de scope per gesprek tot één onderwerp.
