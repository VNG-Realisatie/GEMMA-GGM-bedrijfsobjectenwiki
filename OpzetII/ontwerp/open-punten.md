# Open punten

Vier punten die dit ontwerp bewust benoemt maar niet oplost (besluiten uit [../overdracht.md](../overdracht.md)). Een LLM die onder deze opzet werkt en een open punt raakt: benoemen en voorleggen, niet zelf oplossen.

## 1. Rol van het GGM

De verhouding tot het GGM (Gemeentelijk Gegevensmodel) — entiteitmatching, dekkingsanalyse, terugmeldingen aan het GGM-team — vormt een groot deel van de oude werkwijze maar is in dit ontwerp buiten scope. Open is waar GGM-matching en -terugmelding in het nieuwe procesmodel passen; denkbare aanhaakpunten zijn stap 4 (GGM als extra bron bij de bronanalyse) of stap 5 (GGM-match als onderdeel van de typeanalyse van een Business Object), maar dat is een later ontwerpbesluit.

## 2. Migratie van bestaande content

De bestaande wiki (±319 BO-pagina's, 218 bronsamenvattingen, 34 onderwerpoverzichten onder `Bedrijfsarchitectuur/Wiki/`) blijft onder de oude werkwijze. Wát er te migreren valt, indicatief: bronsamenvattingen laten zich mappen op source-pagina's, onderwerpoverzichten op topic-pagina's, en elementpagina's bevatten het materiaal voor kandidaatpagina's (criteria-toetsing, definitie, relaties, bronnen) — maar met een wezenlijk verschil in levenscyclus: bestaande elementpagina's zijn permanente registratie, kandidaatpagina's niet. Of en hoe er gemigreerd wordt is een apart, later besluit.

## 3. Exportmodel ↔ bestaande CSV-pijplijn

Er bestaat al een CSV-exportpad richting GEMMA: `Bedrijfsarchitectuur/tools/export_ggm_csv.py` genereert 5 CSV's naar `Bedrijfsarchitectuur/exports/` voor de GGM-GEMMA-uitwisseling (catalogus: [../../Opzet/tools/README.md](../../Opzet/tools/README.md)). Open is of de export uit [exportmodel.md](exportmodel.md) daarop aansluit (zelfde kolomindeling/afnemer) of het vervangt. Het exportmodel is bewust als logisch contract beschreven, zodat het bestandsformaat later op de afnemer kan worden afgestemd.

## 4. Levenscyclus na goedkeuring en export

"Geen dubbele vastlegging" vereist een besluit over wat er met een kandidaatpagina gebeurt ná export naar GEMMA: bevriezen (alleen-lezen laten staan als onderbouwingsarchief), archiveren (verplaatsen naar een archiefmap) of reduceren tot verwijzing (alleen frontmatter + link naar het GEMMA-element). Dit ontwerp legt vast dát de pagina een `export:`-markering krijgt en niet met GEMMA mee-onderhouden wordt; de vervolgstap is een open besluit.
