# Richtlijnen tegen dubbele vastlegging

Kernregel: **elk gegeven heeft precies één vindplaats**; elke andere plek verwijst.

| Gegeven | Enige vindplaats |
|---|---|
| Brontekst | het bronbestand in `Sources/` (immutabel) |
| Samenvatting en passages van een bron | de source-pagina |
| Groepering en relevante termen van een domein | de topic-pagina |
| Analyse, motivatie, voorstel en status van een begrip | de kandidaatpagina |
| Definitief element (naam, definitie, relaties, beheerd) | het GEMMA ArchiMate-model |

## Richtlijnen

1. **De wiki bevat nooit definitieve elementdefinities.** Alles op een kandidaatpagina is een voorstel; na goedkeuring en export is GEMMA leidend. Wijzigt GEMMA een definitie, dan wordt de kandidaatpagina niet mee-onderhouden (levenscyclus na export is een open punt — zie [open-punten.md](open-punten.md)).
2. **Status staat alleen in de frontmatter van de kandidaatpagina.** Overzichten (`voortgang.md`) worden gegenereerd en zijn weggooibaar; een handmatig bijgehouden index bestaat niet.
3. **Source-pagina's citeren selectief.** Relevante passages letterlijk als blockquote, met plaatsaanduiding — geen tweede kopie van de bron, en geen ArchiMate-analyse: die hoort op de kandidaatpagina.
4. **Topic-pagina's verwijzen, herhalen niet.** Een topic linkt naar bronnen en registreert welke extracties zijn uitgevoerd; het herhaalt geen samenvattingen en geen kandidaat-analyse. Welke kandidaten bij een onderwerp horen is afleidbaar uit de kandidaat-frontmatter en staat in het gegenereerde voortgangsoverzicht.
5. **Eén kandidaatpagina per begrip**, ook bij meerdere ArchiMate-typen en meerdere onderwerpen. Synoniemen zijn een lijst op die ene pagina, geen tweede pagina. Type-extractie controleert altijd eerst de bestaande kandidatenmap.
6. **Analyse en definitieve architectuur gescheiden houden.** De export draagt alleen de machine-leesbare kern over (zie [exportmodel.md](exportmodel.md)); motivatie, typeanalyse en afgevallen alternatieven blijven in de wiki. Omgekeerd wordt GEMMA-inhoud niet in de wiki gespiegeld.
7. **Afgeleide bestanden** (`voortgang.md`, `export/`) worden nooit handmatig bewerkt — ze zijn altijd reproduceerbaar uit de pagina's.
