Richt de lokale omgeving in zodat de commands werken op deze machine (Linux of Windows). $ARGUMENTS

Input: geen. Idempotent: veilig om opnieuw te draaien.
Output: korte checklist met per stap OK / aangepast / mislukt.

Stappen:
1. **Python vinden.** Probeer `python3 --version`, dan `python --version`, dan `py --version` (Windows). Gebruik de eerste die werkt als `PY` voor de volgende stappen. Geen Python of versie < 3.10 → meld dit, toon installatie-alternatieven (bv. scoop, winget, officiële installer van python.org, Microsoft Store) en vraag expliciet akkoord aan de gebruiker vóór installatie. Installeer nooit zonder dat akkoord, ook niet stilzwijgend via een package manager.
2. **crawl4ai installeren.** Controleer met `PY -c "import crawl4ai"`. Ontbreekt het: `PY -m pip install crawl4ai`, daarna `crawl4ai-setup` (installeert de browser). Meld bij een fout de uitvoer; probeer niet te omzeilen.
3. **Scripts controleren.** Controleer dat `agent/tools/crawl4ai/SKILL.md` en `agent/tools/crawl4ai/scripts/basic_crawler.py` bestaan (paden relatief aan de repo-root). Ontbreken ze → meld dit; herstel niet zelf uit andere locaties.
4. **Rooktest.** Draai `PY agent/tools/crawl4ai/scripts/basic_crawler.py https://example.com` en controleer dat er markdown terugkomt.
5. **Overige tools.** Controleer `curl --version` (gebruikt door `/fetch`) en `git --version`. Alleen melden, niet installeren.
6. **Commands zichtbaar?** Controleer of `.claude/commands/` in de repo-root bestaat en of de symlink `BAlink` daarin een geldige map is (`ls`). Is het een tekstbestand of dode link (Windows zonder `core.symlinks`) → meld dit en verwijs naar het voorstel om de commands als echte bestanden op te nemen; repareer niet zelf.

Richtlijnen:
- Gebruik altijd `/` in paden en relatieve paden vanaf de repo-root; geen `~`, geen `/home/...`.
- Verander niets buiten de Python-installatie zonder het te melden.
