---
type: domein
naam: Arbeidszaken
status: in behandeling
verwerkingsdatum: 2026-06-22
bronnen_count: 12
begrippen_count: 23
bo_count: 12
---

# Domein: Arbeidszaken

De gemeente als werkgever — personeelsadministratie, dienstverbanden, werving en selectie, gesprekscyclus, verzuim, detachering en de bredere context van arbeidsvoorwaarden, integriteit en arbeidsmarktkrapte.

## Begrippen

### Bedrijfsobjecten (bedrijfsvoering/HR)

|Begrip|Type|Omschrijving|BO?| Data-object |Reden|GGM|
|---|---|---|---|---|---|---|
|[[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/dienstverband\|Dienstverband]]|object|Rechtsbetrekking werkgever-werknemer; subtypes: bepaalde/onbepaalde tijd, project, oproep| ✅ | ja |6/6 — kern personeelsadministratie|exact: Dienstverband|
|[[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/werknemer\|Werknemer]]|object|Contractuele wederpartij van de werkgever| ✅ | ja |6/6 — centraal object, hub naar alle HR-objecten|exact: Werknemer|
|[[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/arbeidsfunctie\|Arbeidsfunctie]]|object|Samenstel van taken en werkzaamheden (HR21)| ✅ | ja |6/6 — structureel element functiehuis|exact: Functie (HR)|
|[[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/formatieplaats\|Formatieplaats]]|object|Vastgestelde formatie in fte per organisatie-eenheid| ✅ | ja |6/6 — basis formatieplan|exact: Formatieplaats|
|[[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/vacature\|Vacature]]|object|Te vullen arbeidsplaats, intern of extern opengesteld| ✅ | ja |6/6 — startpunt wervingsproces|exact: Vacature|
|[[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/sollicitatie\|Sollicitatie]]|object|Verzoek om in een functie te worden aangesteld| ✅ | ja |6/6 — kern wervingsproces|exact: Sollicitatie|
|[[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/verlof\|Verlof]]|object|Goedgekeurde periode van afwezigheid| ✅ | ja |6/6 — eigen levenscyclus aanvraag→opname|exact: Verlof|
|[[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/verzuim\|Verzuim]]|object|Afwezigheid wegens ziekte; Wet Poortwachter| ✅ | ja |6/6 — wettelijk verplichte registratie|exact: Verzuim|
|[[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/declaratie\|Declaratie]]|object|Opgave van te vergoeden kosten| ✅ | ja |6/6 — eigen levenscyclus indiening→uitbetaling|exact: Declaratie (HR)|
|[[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/beoordeling\|Beoordeling]]|object|Oordeel over functioneren; gesprekscyclus (planning, functionering, beoordeling)| ✅ | ja |6/6 — subtypes: plannings-/functionerings-/beoordelingsgesprek|exact: Beoordeling|
|[[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/disciplinaire-maatregel\|Disciplinaire Maatregel]]|object|Formeel besluit bij plichtsverzuim of wangedrag| ✅ | ja |6/6 — eigen levenscyclus geconstateerd→opgelegd|exact: Disciplinaire Maatregel|
|[[Wiki/Bedrijfsobjecten/9-interne-organisatie/hr/detacheringsovereenkomst\|Detacheringsovereenkomst]]|object|Overeenkomst uitlener-inlener bij collegiale uitleen personeel| ✅ | ja |6/6 — eigen partijen, duur, vergoedingsmodel|GGM-hiaat #52|

### Overige begrippen (governance/beleid)

|Begrip|Type|Omschrijving|BO?| Data-object |Reden|GGM|
|---|---|---|---|---|---|---|
|arbeidsmarktkrapte|thema|Aanbod arbeid lager dan vraag| ❌ | nee |Beleidsmatig|nee|
|P&O-beleid|instrument|Beleid personeels- en organisatieontwikkeling| ❌ | nee |Governance|nee|
|arbeidsvoorwaarden|thema|Collectieve regelingen, cao-afspraken| ❌ | nee |Beleidsmatig|nee|
|gedragscode|instrument|Normen voor integriteit en ethisch gedrag| ❌ | nee |Governance|nee|
|integriteitsbeleid|thema|Cultuur en regelgeving rond integriteit| ❌ | nee |Governance|nee|
|rechtspositieregeling|instrument|Regeling rechtspositie politieke ambtsdragers| ❌ | nee |Governance|nee|
|cao-gemeenten|instrument|Collectieve arbeidsovereenkomst lokale overheden| ❌ | nee |Extern instrument|nee|
|arbeidsmigranten|doelgroep|Arbeiders uit het buitenland| ❌ | nee |Doelgroep, registratie via BRP/RNI|nee|
|werk-voor-arbeidsbeperkten|thema|Programma Banenafspraak| ❌ | nee |Programma|nee|
|gemeentelijk werkgever|actor|Gemeente in haar werkgeversrol| ❌ | nee |Rol|nee|
|medewerker|actor|Abstract type waarvan Werknemer erft| ❌ | ja |Abstract in GGM, niet zelfstandig|ja (abstract)|

## Verwerkte bronnen

| Bron | Kerninhoud |
|---|---|
| rubriek-arbeidszaken | Overzicht: krappe arbeidsmarkt, VNG-ondersteuning |
| arbeidsvoorwaarden | Arbeidsomstandigheden, collectieve zorgverzekering, HR21 |
| arbeidsmarktkrapte-aanpak-gemeenten | Programma: arbeidsmarktstrategie, AI, vereenvoudiging |
| financiele-arbeidsvoorwaarden | Pensioen (ABP), APPA-wijziging wethouders |
| integriteit | Gedragscodes, toolkits, Netwerk Weerbaar Bestuur, LKOG |
| po-beleid | Werkboek arbeidsmarkt, diversiteit/inclusie, mobiliteitsrapportage |
| rechtspositie-politieke-ambtsdragers | Regelingen burgemeesters, wethouders, raadsleden |
| werk-voor-arbeidsbeperkten | Banenafspraak, Cao Aan de Slag, Cao SW |
| arbeidsmigranten | Woon-/werkomstandigheden, integrale gemeentelijke aanpak |
| handreiking-flexibele-arbeidsinzet | Juridische handreiking: detachering, contractvormen, inhuur, zzp |
| College voor Arbeidszaken | CvA: werkgeversbelangenbehartiging, cao-overleg |
| cva-beleidsplan-2023-2026 | Beleidsplan 2023-2026: 8 thema's, Wtp-transitie |

## Bronsamenvattingen

- [[Wiki/Bronsamenvattingen/Arbeidszaken/college-voor-arbeidszaken|College voor Arbeidszaken]] — CvA: collectieve werkgeversbelangenbehartiging, cao-overleg, pensioen
- [[Wiki/Bronsamenvattingen/Arbeidszaken/cva-beleidsplan-2023-2026|CvA Beleidsplan 2023-2026]] — Beleidsplan 2023-2026: 8 thema's, arbeidsmarktkrapte-programma, Wtp-transitie
- [[Wiki/Bronsamenvattingen/Arbeidszaken/rubriek-arbeidszaken|Rubriek Arbeidszaken]] — Overzichtspagina VNG-rubriek
- [[Wiki/Bronsamenvattingen/Arbeidszaken/arbeidsmarktkrapte-aanpak-gemeenten|Arbeidsmarktkrapte-aanpak Gemeenten]] — VNG-programma personeelstekorten
- [[Wiki/Bronsamenvattingen/Arbeidszaken/arbeidsmigranten|Arbeidsmigranten]] — Woon-/werkomstandigheden, gemeentelijke aanpak
- [[Wiki/Bronsamenvattingen/Arbeidszaken/arbeidsvoorwaarden|Arbeidsvoorwaarden]] — Arbeidsomstandigheden, zorgverzekering, HR21
- [[Wiki/Bronsamenvattingen/Arbeidszaken/financiele-arbeidsvoorwaarden|Financiële arbeidsvoorwaarden]] — Pensioen ABP, APPA-wijziging, ZPW
- [[Wiki/Bronsamenvattingen/Arbeidszaken/integriteit|Integriteit]] — Gedragscodes, toolkits, Netwerk Weerbaar Bestuur, LKOG
- [[Wiki/Bronsamenvattingen/Arbeidszaken/po-beleid|P&O-beleid]] — Werkboek arbeidsmarkt, diversiteit/inclusie
- [[Wiki/Bronsamenvattingen/Arbeidszaken/rechtspositie-politieke-ambtsdragers|Rechtspositie Politieke Ambtsdragers]] — Regelingen burgemeesters, wethouders, raadsleden
- [[Wiki/Bronsamenvattingen/Arbeidszaken/werk-voor-arbeidsbeperkten|Werk voor arbeidsbeperkten]] — Banenafspraak, Cao Aan de Slag, Cao SW
- [[Wiki/Bronsamenvattingen/Arbeidszaken/handreiking-flexibele-arbeidsinzet|Handreiking flexibele arbeidsinzet]] — Juridische handreiking: detachering, contractvormen, inhuur

## Conclusie

Domein Arbeidszaken heeft twee lagen: (1) een **bedrijfsvoeringslaag** met 12 BO's uit het GGM HR-domein (taakveld 9) die de gemeente als werkgever beheert in haar personeelsadministratie, en (2) een **beleidslaag** met governance-begrippen (cao, gedragscode, integriteitsbeleid) die geen BO's opleveren.

De 12 BO's dekken de volledige HR-levenscyclus: formatie (Formatieplaats, Functie) → werving (Vacature, Sollicitatie) → dienstverband (Dienstverband, Werknemer) → uitvoering (Verlof, Verzuim, Declaratie, Beoordeling, Disciplinaire Maatregel) → samenwerking (Detacheringsovereenkomst).

GGM HR-dekking is goed (11 van 12 BO's exact match). Eén GGM-hiaat: Detacheringsovereenkomst. Eén GGM-correctie: definitie Beoordeling.

## Raakvlakken

- **Werk en Inkomen** — werk-voor-arbeidsbeperkten raakt de Participatiewet en Banenafspraak
- **Bestuur** — rechtspositie politieke ambtsdragers raakt gemeentewet en lokale democratie
- **Asiel en Integratie** — arbeidsmigranten raakt ook migratie-en-werk
- **Financien** — Declaratie en salarisadministratie raken financieel beheer (taakveld 9)
