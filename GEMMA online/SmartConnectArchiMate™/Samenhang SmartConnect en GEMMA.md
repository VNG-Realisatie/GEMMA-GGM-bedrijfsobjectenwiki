# Samenhang SmartConnectArchiMate™ en GEMMA

Overzicht van de 30 sjablonen/pagina's in `Categorie:SmartConnectArchiMate™` (ArchiXL, closed source,
read-only), hoe ze samenhangen, en waar GEMMA al dan niet ingrijpt met een eigen versie. Gebaseerd op het lezen van
alle 30 lokaal gespiegelde bestanden in deze map, niet op officiële ArchiXL-ontwikkelaarsdocumentatie —
die bestaat niet binnen deze categorie (zie "Bijzonderheden" onderaan).

## 1. Twee invocatiemechanismen, en dus twee manieren om in te grijpen

**A. Objectdetailpagina's — automatische Custom-detectie door ArchiMedes zelf (PHP, onzichtbaar in wikitekst)**

Voor elk ArchiMate-objecttype (Element, Relationship, View, Viewconnection, Viewnode, Model,
Organization, Organizationitem, PropertyDef, Viewpoint) genereert ArchiMedes bij import een wikipagina.
Bij het *renderen* van die pagina transcludeert de closed-source extensie zelf — buiten de zichtbare
wikitekst om — een vaste sjabloonketen op naam, en geeft daarbij alle objecteigenschappen mee als
benoemde parameters. Onderdeel van die keten is `Sjabloon:DisplayArchiMate<Type>`; **bestaat er een
`Sjabloon:DisplayArchiMate<Type>Custom`, dan gebruikt ArchiMedes die in plaats van het standaardsjabloon.**

Geen van de 30 standaardsjablonen bevat zelf een `{{#ifexist:...Custom|...}}`-constructie — de keuze
gebeurt dus buiten wikitekst, in de PHP-code van de extensie. Dit is precies de reden dat je alleen een
nieuwe pagina `Sjabloon:DisplayArchiMate<Type>Custom` hoeft aan te maken om in te grijpen: er hoeft
nergens een verwijzing naar te worden gelegd, ArchiMedes vindt hem vanzelf.

**B. Hulpsjablonen — expliciete aanroep vanuit wikitekst (GEMMA bepaalt zelf welke naam)**

Kleinere bouwstenen (`FormatRelationshipName`, `FormatViewconnection`, `FormatViewnode`,
`CreateDisplayBox`, `DisplayArchiMateDiagram`, `DisplayArchiMateAnalysis`, `DisplayArchiMateModelsOverview`,
...) worden niet automatisch gekozen, maar expliciet aangeroepen — hetzij rechtstreeks (`{{FormatRelationshipName|...}}`),
hetzij via een SMW-`#ask`-query met `template=FormatRelationshipName`. Hier bestaat geen
Custom-detectiemechanisme; GEMMA "overrides" dit type sjabloon alleen door in haar *eigen* aanroepende
code een andere naam te gebruiken (zie `FormatRelationshipNameCustom`, hieronder).

**C. Mainspace-overzichtspagina's — gewone wikipagina's, geen detectiemechanisme**

`DisplayArchiMateModels`, `DisplayArchiMateElements`, `DisplayArchiMateRelationships`,
`DisplayArchiMateGlossary`, `DisplayArchiMateViewDetails`, `DisplayArchiMateAnalysis` (mainspace) zijn
gewone content-pagina's die ArchiXL vult met `#ask`-queries en URL-parameters (`?elementtype=`, `?model=`,
...). Ze horen niet bij een los object en worden dus ook niet via de Custom-conventie overruled. Wil
GEMMA hier iets anders, dan is directe bewerking (met het overschrijf-risico bij een upgrade) of een eigen
alternatieve pagina de enige weg — vermoedelijk waarom GEMMA in plaats daarvan een geheel eigen
navigatieset heeft gebouwd (`Sjabloon:ToonDomein/*`, `Sjabloon:ToonViewGEMMA`,
`Sjabloon:ToonBeleidsdomeinen`, ...) in plaats van deze pagina's te overrulen.

## 2. Tabel: alle 30 sjablonen/pagina's

| Sjabloon/pagina | Categorie | Wat het is/doet | GEMMA-override | Mechanisme |
|---|---|---|---|---|
| [Sjabloon:DisplayArchiMateElement](Sjabloon%3ADisplayArchiMateElement) | A · objecttype | Detailpagina van een ArchiMate-element: type, label, documentatie, custom properties, views, relaties, contextdiagram | ✅ `DisplayArchiMateElementCustom` | Auto (naamconventie) |
| [Sjabloon:DisplayArchiMateRelationship](Sjabloon%3ADisplayArchiMateRelationship) | A · objecttype | Detailpagina van een relatie: bron/doel, type, custom properties, views, contextdiagram met bron/doel gemarkeerd | ❌ nog standaard | Auto (naamconventie) |
| [Sjabloon:DisplayArchiMateView](Sjabloon%3ADisplayArchiMateView) | A · objecttype | Detailpagina van een view: de view zelf + dynamisch paneel, viewpoint, elementen/relaties op de view | ✅ `DisplayArchiMateViewCustom` | Auto (naamconventie) |
| [Sjabloon:DisplayArchiMateViewconnection](Sjabloon%3ADisplayArchiMateViewconnection) | A · objecttype | Detailpagina van een verbindingslijn in een view: bron/doel-viewnode, welke relatie hij representeert, grafische kenmerken | ❌ nog standaard | Auto (naamconventie) |
| [Sjabloon:DisplayArchiMateViewnode](Sjabloon%3ADisplayArchiMateViewnode) | A · objecttype | Detailpagina van een vorm in een view: positie/afmeting, welk element hij representeert, aansluitende viewconnections | ❌ nog standaard | Auto (naamconventie) |
| [Sjabloon:DisplayArchiMateModel](Sjabloon%3ADisplayArchiMateModel) | A · objecttype | Detailpagina van een geïmporteerd model: metadata, elementen/relaties per laag/categorie, organisaties, viewpoints, views | ❌ nog standaard | Auto (naamconventie) |
| [Sjabloon:DisplayArchiMateOrganization](Sjabloon%3ADisplayArchiMateOrganization) | A · objecttype | Detailpagina van een (root-)organisatiestructuur: boomweergave van alle items | ❌ nog standaard | Auto (naamconventie) |
| [Sjabloon:DisplayArchiMateOrganizationitem](Sjabloon%3ADisplayArchiMateOrganizationitem) | A · objecttype | Detailpagina van één knoop in een organisatiestructuur: subboom vanaf dat item | ❌ nog standaard | Auto (naamconventie) |
| [Sjabloon:DisplayArchiMatePropertyDef](Sjabloon%3ADisplayArchiMatePropertyDef) | A · objecttype | Detailpagina van een custom-property-definitie: type, meest gebruikte waarden, welke objecten hem gebruiken | ❌ nog standaard | Auto (naamconventie) |
| [Sjabloon:DisplayArchiMateViewpoint](Sjabloon%3ADisplayArchiMateViewpoint) | A · objecttype | Detailpagina van een viewpoint: doel, inhoud, toegestane element-/relatietypen, concerns, modeling notes | ❌ nog standaard | Auto (naamconventie) |
| [Sjabloon:FormatRelationshipName](Sjabloon%3AFormatRelationshipName) | B · hulpsjabloon | Formatteert "Bron => Doel (relatietype)" voor gebruik in lijsten/tabellen | ✅ `FormatRelationshipNameCustom` | Expliciete aanroep |
| [Sjabloon:FormatViewconnection](Sjabloon%3AFormatViewconnection) | B · hulpsjabloon | Rij-renderer voor `#ask`-lijsten van viewconnections (gebruikt in Viewnode- en ViewDetails-pagina's) | ❌ nog standaard | Expliciete aanroep |
| [Sjabloon:FormatViewnode](Sjabloon%3AFormatViewnode) | B · hulpsjabloon | Rij-renderer voor `#ask`-lijsten van viewnodes (gebruikt in ViewDetails-pagina) | ❌ nog standaard | Expliciete aanroep |
| [Sjabloon:CreateDisplayBox](Sjabloon%3ACreateDisplayBox) | B · hulpsjabloon | Generieke in-/uitklapbare box met titel + inhoud (evt. 2 kolommen + icoon); dé bouwsteen die vrijwel elk ander sjabloon gebruikt | ❌ (GEMMA gebruikt hem rechtstreeks) | Expliciete aanroep |
| [Sjabloon:DisplayArchiMateDiagram](Sjabloon%3ADisplayArchiMateDiagram) | B · hulpsjabloon | Toont een view + dynamisch-eigenschappenpaneel, herbruikbaar op willekeurige wikipagina's | ❌ nog standaard (GEMMA heeft een eigen `ToonViewGEMMA` ernaast, geen override) | Expliciete aanroep |
| [Sjabloon:DisplayArchiMateDiagramUrl](Sjabloon%3ADisplayArchiMateDiagramUrl) | B · hulpsjabloon | Toont alleen een downloadlink naar een view | ❌ nog standaard | Expliciete aanroep |
| [Sjabloon:DisplayArchiMateDynamicView](Sjabloon%3ADisplayArchiMateDynamicView) | B · hulpsjabloon | Variant van DisplayArchiMateDiagram met meer weergave-opties (paneel/frame verbergen) | ❌ nog standaard | Expliciete aanroep |
| [Sjabloon:DisplayArchiMateAnalysis](Sjabloon%3ADisplayArchiMateAnalysis) | B · hulpsjabloon | Dunne wrapper om de closed-source `#performArchiMateAnalysis`-functie | ❌ nog standaard | Expliciete aanroep |
| [Sjabloon:DisplayArchiMateModelsOverview](Sjabloon%3ADisplayArchiMateModelsOverview) | B · hulpsjabloon | Rij-renderer (positionele parameters) voor de modellenlijst op `DisplayArchiMateModels` | ❌ nog standaard | Expliciete aanroep (`template=` in `#ask`) |
| [DisplayArchiMateModels](DisplayArchiMateModels) | C · overzichtspagina | Vertrekpunt: lijst van alle geïmporteerde modellen (mainspace) | ❌ | Alleen directe bewerking |
| [DisplayArchiMateElements](DisplayArchiMateElements) | C · overzichtspagina | Lijst van elementen van één type binnen één model, via `?elementtype=&model=` (mainspace) | ❌ (GEMMA heeft eigen `ToonDomein/*`-navigatie) | Alleen directe bewerking |
| [DisplayArchiMateRelationships](DisplayArchiMateRelationships) | C · overzichtspagina | Zelfde als Elements, maar voor relaties (mainspace) | ❌ | Alleen directe bewerking |
| [DisplayArchiMateGlossary](DisplayArchiMateGlossary) | C · overzichtspagina | Volledige ArchiMate-begrippenlijst met icoon en definitie per laag/relatietype (mainspace) | ❌ (GEMMA-koppeling via `Overzicht ArchiMate definities`, zie hieronder) | Alleen directe bewerking |
| [DisplayArchiMateViewDetails](DisplayArchiMateViewDetails) | C · overzichtspagina | Technische details van een view: alle viewnodes/viewconnections met coördinaten (mainspace) | ❌ | Alleen directe bewerking |
| [DisplayArchiMateAnalysis](DisplayArchiMateAnalysis) | C · overzichtspagina | Resultaatpagina van een analyse: resultaat, paneel, toelichting (mainspace) | ❌ | Alleen directe bewerking |
| [DisplayArchiMateViews](DisplayArchiMateViews) | C · overzichtspagina | `{{:DisplayArchiMateElements}}` — letterlijk hetzelfde als Elements, want een lijst van views is ook maar een categorielijst | n.v.t. | — |
| [DisplayArchiMatePropertyDefs](DisplayArchiMatePropertyDefs) | C · overzichtspagina | Idem: `{{:DisplayArchiMateElements}}` | n.v.t. | — |
| [Overzicht ArchiMate definities](Overzicht%20ArchiMate%20definities) | D · GEMMA-pagina | GEMMA-eigen pagina die uitleg geeft en vervolgens `DisplayArchiMateGlossary` transcludeert | — (is zelf al een GEMMA-pagina) | — |
| [SmartConnectArchiMateHelp en](SmartConnectArchiMateHelp%20en) | D · documentatie | Gebruikershandleiding van de extensie (Engels) | n.v.t. | — |
| [SmartConnectArchiMateHelp nl](SmartConnectArchiMateHelp%20nl) | D · documentatie | Zelfde, in het Nederlands — bevat géén ontwikkelaarsdocumentatie over het Custom-mechanisme | n.v.t. | — |

## 3. Hoe zelf een nieuwe `...Custom` bouwen (categorie A)

1. Maak `Sjabloon:DisplayArchiMate<Type>Custom` aan (bv. `Sjabloon:DisplayArchiMateRelationshipCustom`).
   ArchiMedes pikt hem vanzelf op zodra de pagina bestaat; er hoeft nergens een verwijzing gelegd te
   worden.
2. Begin met de magic words en het kruimelpad, zoals elk standaardsjabloon doet:
   `__NOCACHE____NOTOC____NOEDITSECTION__` en `{{#displayArchiMateBreadcrumbs:...}}`.
3. Zet zelf de categorieën (`[[Category:ArchiMate{{{ArchiMateVersion|2.1}}}]]` e.d.) — dat gebeurt niet
   automatisch meer zodra je het standaardsjabloon vervangt.
4. Bouw de weergave met [Sjabloon:CreateDisplayBox](Sjabloon%3ACreateDisplayBox) als bouwsteen, zoals het
   standaardsjabloon dat ook doet.
5. Voor de generieke CustomProperties-eigenschappen: het standaardsjabloon gebruikt een `#arraymap`-lus
   met parameter-indirectie (`{{{{{ucfirst:xqx}}|}}}`) die zowel `#set` (vastleggen) als de tabelrij
   (tonen) in één keer doet, inclusief taalvarianten (`<Property>Languages`, `<Property>_<taalcode>`).
   GEMMA's eigen aanpak (zie `Sjabloon:DisplayArchiMateCustom/_index`) splitst dit bewust: vastleggen hoort in de Epilogue, tonen in
   het Display-sjabloon — en laat de taalvarianten-afhandeling vooralsnog achterwege (bekend hiaat).
6. Test zonder ArchiMedes door het sjabloon op een testpagina met expliciete parameters aan te roepen —
   ArchiMedes zelf geeft nooit een `page=`-parameter mee, dus bouw een fallback zoals de bestaande
   GEMMA-Custom-sjablonen doen (`{{#ifeq:{{NAMESPACENUMBER}}|10|<vast testobject>|{{FULLPAGENAME}}}}`).

Kandidaten voor een nieuwe Custom, in volgorde van vermoedelijke impact: **Relationship** (analoog aan
Element, waarschijnlijk de meest gebruikte na Element/View), daarna **Model** (het vertrekpunt-detailscherm
per architectuurmodel) en **Viewpoint**. Viewconnection/Viewnode/Organization/Organizationitem/PropertyDef
zijn techischer en minder vaak direct bezocht.

## 4. Bijzonderheden

* **Het Custom-mechanisme staat nergens gedocumenteerd binnen deze 30 pagina's.** Beide
  `SmartConnectArchiMateHelp`-pagina's (de officiële ArchiXL-handleiding) beschrijven uitsluitend
  eindgebruikersfunctionaliteit (importeren, exporteren, navigeren, dynamische views, queries,
  configuratie-instellingen) — geen woord over dat `...Custom`-sjablonen automatisch worden opgepikt. Die
  kennis is puur af te leiden uit gedrag (afwezigheid van `#ifexist`-logica in de standaardsjablonen zelf)
  en is door het GEMMA-team zelf gereconstrueerd — zie het "gemeten, niet aangenomen"-voorbehoud in
  `Sjabloon:DisplayArchiMateCustom/_index`.
* **Elk standaardsjabloon doet tonen én vastleggen in één blok** (de CustomProperties-`#arraymap`-lus met
  `#set`). GEMMA's eigen architectuur splitst dat bewust (zie `Sjabloon:SmartCoreEpilogue`) —
  maar wie een nieuwe Custom bouwt door het standaardsjabloon simpelweg te kopiëren, erft die vermenging
  automatisch weer terug, tenzij er bewust van wordt afgeweken.
* **Taalvarianten worden door de standaardsjablonen wél afgehandeld** (`<Property>Languages`,
  `<Property>_<taalcode>` met NL-fallback op vrijwel elk veld), **door GEMMA's eigen sjablonen niet.** Dit
  bevestigt vanuit de ArchiXL-broncode het al bekende hiaat.
* **`DisplayArchiMateViews` en `DisplayArchiMatePropertyDefs` zijn geen aparte implementaties**, maar
  transcluderen kaal `DisplayArchiMateElements` — werkt omdat "lijst van categorie X binnen model Y" voor
  beide typen identiek is aan de Elements-lijst.
* **`Sjabloon:DisplayArchiMateModelsOverview` sluit af met een kapotte tag**: `<includeonly>` in plaats van
  `</includeonly>`, letterlijk zo overgenomen in de lokale kopie (geen correctie, is nu eenmaal wat er op
  de wiki staat).
* **De `...EpilogueCustom`/`...Custom`-uitbreidingspunten binnen GEMMA's eigen sjablonen geven zelf geen
  parameters door** (zie eerdere sessie-bevinding bij `SmartCoreEpilogue`) — dat is een GEMMA-eigen
  patroon, niet iets wat van ArchiXL is overgenomen; de ArchiXL-standaardsjablonen kennen dat mechanisme
  niet, zij hébben immers geen eigen Custom-uitbreidingspunt nodig.
* **Elke standaardpagina draagt het auteursrecht-/overschrijfwaarschuwing** ("Any changes to this page will
  be overwritten by module upgrades") — inclusief de mainspace-overzichtspagina's (categorie C), die geen
  Custom-detectiemechanisme hebben. Direct bewerken van die pagina's is dus net zo riskant als bij de
  Sjabloon-pagina's, alleen zonder de escape via een naamconventie.
