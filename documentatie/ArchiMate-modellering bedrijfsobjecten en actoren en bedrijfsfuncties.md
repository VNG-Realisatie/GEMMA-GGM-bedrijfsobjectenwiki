### Hoofddoel: bedrijfsobjectmodel

* [Verified] Business Object model bevat uitsluitend informatieobjecten
* [Verified] Business Objects representeren data, documenten, registraties, concepten
* [Inferred] Dit model is onafhankelijk van actorstructuur en processtructuur

### Kernstructuur bedrijfsobjecten

* Business Object
* Object-typen / groeperingen (domeinstructuur)
* Relaties tussen objecten (structuur, afhankelijkheden)
* Eventueel: levenscyclusstatus (conceptueel, niet procesmatig)

### Nevendoel 1: actoren en rollen vastleggen

* [Verified] Actoren en rollen horen in Business Layer (structureel model)
* Actor (organisatie, persoon, systeem)
* Business Role (verantwoordelijkheid)
* Business Collaboration (optioneel)

### Koppeling actoren ↔ bedrijfsobjecten

* [Verified] Geen directe relatie Actor ↔ Business Object
* Koppeling via gedrag:

  * Business Process of Business Function
* Relaties:

  * Actor → Role (Assignment)
  * Role → Process/Function (Assignment)
  * Process/Function → Business Object (Access)

### Nevendoel 2: koppeling met bedrijfsfunctiemodel

* [Verified] Business Function model is een structurele decompositie van activiteiten
* [Verified] Business Objects worden gebruikt en geproduceerd door functies
* Doel: verrijken bestaand functiemodel met informatiestructuur

### Integratiepatroon

* Business Function → gebruikt/produceert → Business Object
* Business Function → gerealiseerd door → Service (optioneel)
* Actor → vervult Role → uitvoert Function/Process

### Nevendoel 3: producten en diensten (contextlaag)

* [Verified] Product = bundel van Services + Business Objects + contractcontext
* [Verified] Service = extern zichtbaar gedrag
* Business Object = inhoud van levering (bijv. document, dossier)

### Relatiemodel (samenvatting)

* Actor → Role → Function/Process → Business Object
* Function → Service → Product
* Product → bundelt Services + Business Objects

### Belangrijk ontwerpprincipe

* [Inferred] Bedrijfsobjectmodel is leidend en onafhankelijk
* [Inferred] Actoren en functies zijn “gebruikerslaag”
* [Inferred] Producten en services zijn “externe waardelaag”
* [Inferred] Processen/functies zijn “gedragslaag” die alles verbindt

### Resultaatstructuur (praktisch)

* Laag 1: Bedrijfsobjecten (kernmodel)
* Laag 2: Functies (bestaand uitbreiden)
* Laag 3: Actoren en rollen (verantwoordelijkheid)
* Laag 4: Services en producten (extern perspectief)

### Conclusie

* Bedrijfsobjectmodel blijft centraal en zelfstandig
* Actoren en rollen worden via functies/processen gekoppeld
* Functiemodel is verbindende laag tussen objecten en organisatie
* Producten en diensten vormen externe verpakking bovenop objecten en functies
