
Issue indelingen
- rubrieken onderwerpen taakvelden domeinen en beleidsdomeinen
- indelingen die elkaar op niet eenduidige wijze overlappen en aanvullen
- harde mapping nodig voor herhaalbaarheid
- mapping op ggm-indeling nodig voor terugmelden

issue ggm bron
- bron is json
- ggm samenvatting in wiki
	- ggm structuur -> ggm-indeling top down. index beleidsdomeinen
	- ggm-entiteiten -> pagina per beleidsdomein

frontmatter
- `bedrijfsfuncties`/`bedrijfsprocessen` zijn vrije lijsten zonder eigen pagina's → niet herleidbaar/geen consistentie.

onderwerpen
- ook beleidsthema's, rubrieken, domeinen.
- wat is gedeelde naam voor gemeentelijke indeling



ggm terugmeldingen
- volgen ggm beleidsdomeinen

ggm-dekking
- match van beleidsdomeinen op onderwerpen gaat via de BO en GGM-entiteiten
	- bottom up bepalen wat beleidsdomein is voor een bedrijfsobjecten
		- aantal data-objecten met match, deze eerst, geeft context voor matchen beleidsdomeinen
		- aantal data-objecten zonder match, dan beleidsdomein afleiden op inhoud en melden als hiaat
		- aantal bedrijfsobjecten dat niet geregistreerd wordt, afleiden. Geen hiaat, wel tellen
	- er zijn waarschijnlijk ook onderwerpen waar geen ggm-beleidsdomein voor bestaat
- per beleidsdomein dekking
	- aantal BO met data-object=ja en ggm-match
	- aantal BO met data-object=ja zonder ggm-match -> ggm-hiaat
	- aantal BO met data-object=nee en ggm-match -> zou niet moeten voorkomen
	- aantal BO met data-object=nee zonder ggm-match -> BO buiten scope van GGM



