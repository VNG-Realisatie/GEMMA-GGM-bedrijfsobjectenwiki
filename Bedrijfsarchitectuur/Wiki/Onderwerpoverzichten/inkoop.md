---
type: onderwerp
naam: Inkoop
status: afgerond
verwerkingsdatum: 2026-06-26
bronnen_count: 3
begrippen_count: 17
bo_count: 8
---

# Inkoop

## Beschrijving

Gemeentelijk onderwerp dat de verwerving van goederen, diensten en werken door de gemeente omvat. Gemeenten besteden gezamenlijk jaarlijks meer dan 40 miljard euro in. Het inkoopproces volgt zeven fasen (voortraject, specificeren, selecteren, contracteren, bestellen, bewaken, nazorg) en wordt beheerst door de Aanbestedingswet, de Gids Proportionaliteit en het gemeentelijke inkoop- en aanbestedingsbeleid.

Het GGM modelleert dit als beleidsdomein "Inkoop" onder taakveld 9 (Interne Organisatie) met 20 entiteiten, verdeeld over inkoop (goederen/diensten/werken), inhuur (personeel) en overig.

## Begrippentabel

| Begrip | Type | Omschrijving | BO? | Data-object | Reden | Voorbeelden | GGM |
|---|---|---|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/aanbesteding\|Aanbesteding]] | object | Procedure waarmee de gemeente een opdracht in de markt zet en gunt | ✅ | ja | 6/6 criteria, exact match | Europese aanbesteding wegonderhoud, meervoudige offerteaanvraag ICT | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/contract\|Contract]] | object | Bindende overeenkomst tussen gemeente en leverancier | ✅ | ja | 6/6 criteria, exact match | Raamovereenkomst groenonderhoud, leveringscontract kantoorartikelen | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/leverancier\|Leverancier]] | actor | Niet-natuurlijk persoon die goederen, diensten of werken levert | ✅ | ja | 6/6 criteria, exact match, 2 duplicaten | Aannemingsbedrijf, ICT-leverancier, schoonmaakbedrijf | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/gunning\|Gunning]] | object | Formeel besluit tot toewijzing van een opdracht | ✅ | ja | 6/6 criteria, exact match | Gunning wegonderhoud aan aannemer X | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/offerte\|Offerte]] | object | Aanbod met prijsopgave van een leverancier | ✅ | ja | 6/6 criteria, exact match, 3 duplicaten | Offerte voor kantoorinrichting | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/aanbieding\|Aanbieding]] | object | Formele deelname aan een nationale of Europese aanbesteding | ✅ | ja | 5/6 criteria, exact match, voorheen "Inschrijving" | Aanbieding op Europese aanbesteding afvalverwerking | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/inkooppakket\|Inkooppakket]] | object | Categorisering van werken, diensten en leveringen | ✅ | ja | 5/6 criteria, exact match | Pakket "ICT-hardware", pakket "Groenonderhoud" | ja |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/inkoop/marktconsultatie\|Marktconsultatie]] | object | Voorbereidend onderzoek naar marktmogelijkheden | ✅ | ja | 6/6 criteria, GGM-hiaat | Marktconsultatie duurzaam wegonderhoud | nee |
| Aankondiging | object | Publicatie van aanbesteding op TenderNed | ❌ | ja | GGM-component van Aanbesteding | TenderNed-publicatie | ja |
| Offerteaanvraag | object | Uitvraagdocument gericht aan leveranciers | ❌ | ja | GGM-component van Aanbesteding | Meervoudige offerteaanvraag schoonmaak | ja |
| Startformulier aanbesteden | object | Intern formulier voor initiëren aanbesteding | ❌ | ja | GGM-component van Aanbesteding, intern formulier | — | ja |
| Selectietabel aanbesteding | object | Tabel met drempelbedragen en procedures | ❌ | ja | Configuratiedata, GGM-component van Aanbesteding | — | ja |
| CPV-code | object | EU-classificatiesysteem voor overheidsopdrachten | ❌ | ja | EU-referentietabel, geen gemeentelijk object | CPV 45233120 (wegenbouw) | ja |
| Drempelbedrag | object | Grenswaarde voor keuze aanbestedingsprocedure | ❌ | nee | Eigenschap van selectietabel | €70.000 diensten, €150.000 werken | nee |
| BPKV | thema | Beste prijs-kwaliteitverhouding, gunningscriterium | ❌ | nee | Beoordelingsmethode, geen object | — | nee |
| Social return | thema | Maatschappelijke bijdrage door leverancier | ❌ | nee | Beleidsconcept, geen object | Arbeidsplaatsen voor mensen met afstand tot arbeidsmarkt | nee |
| Maatschappelijk verantwoord inkopen | thema | Inkopen met aandacht voor milieu en sociale aspecten | ❌ | nee | Beleidsconcept, geen object | MVOI-actieplan, 7 thema's | nee |

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/Inkoop/inkoop-en-aanbestedingsbeleid|Gemeentelijk inkoop- en aanbestedingsbeleid]] — gebundelde samenvatting van 3 bronnen (VNG-model, OVER-gemeenten, West-Betuwe)

## Openstaande vragen of hiaten

- **Inkoop vs. inhuur:** het GGM modelleert inhuur als apart subdomein met eigen entiteiten (Aanbesteding Inhuur, FormulierInhuur, Kandidaat). De bronnen beschrijven inhuur als onderdeel van het bredere inkoopdomein. De inhuur-entiteiten zijn als GGM-componenten of specialisaties opgenomen, niet als apart BO.
- **Contract domeindoorsnijdend:** Contract verschijnt op 5 GGM-diagrammen (Inkoop, Sociaal Domein, Financiën, Inhuur). Het is primair een Inkoop-BO maar wordt ook gebruikt in andere domeinen.

## Terugmeldingen richting GGM

4 terugmeldingen (#78-#81) in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]]:
- #78: Leverancier — duplicaat (2 GUIDs)
- #79: Offerte — duplicaat (3 GUIDs)
- #80: Inschrijving — homoniem (Inkoop vs. Onderwijs)
- #81: Marktconsultatie — hiaat (ontbreekt als entiteit)
