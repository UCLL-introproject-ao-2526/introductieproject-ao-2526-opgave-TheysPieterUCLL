
## 16 oktober 1720

Ik heb de opdracht nog eens nagelezen en alles klaargezet in vs code en de tutorial beginnen lijken. tot nu toe is alles vlot verlopen. de code wordt goed uitgelegd maar ik heb bij enkele punten nog wat extra uitleg gezocht om zeker te zijn dat ik de logica goed begrijp. Het is ook soms moeilijk om te volgen wat alle parameters zijn en doen. verder heb ik ook de code toegevoegd aan mijn project om sneller code na te kunnen kijken. En de video geliked!




## 17 oktober 1600

ik heb verder gewerkt aan het blackjack project. er was een probleem met dat de kaarten niet op het scherm verschenen, na enkele keren terug te gaan zag ik dat in de return van deal_cards de twee variabelen omgedraaid moesten worden. verder was ik de coordinaten van dealer cards vergeten aan te passen.  Ik ben aan het nadenken hoe ik later het spel visueel kan verbeteren/uitbreiden en ik wil ook de 'suits' van de kaarten toevoegen.




## 18 oktober 1110

probleem met de hit-button, uiteindelijk was het probleem dat de variable hand_active op false bleef staan. bij testen van de game bleek er een probleem te zijn vanaf de tweede ronde. na het vergelijken van mijn code met de originele bleek dat ik een van de variabele was vergeten te resetten ( reveal_dealer) waardoor de game bevroor. ik moet iets aandachtiger zijn met het updaten van variabelen, dit is de zoveelste keer dat ik hier tijd aan heb verloren. ik heb de tutorial afgewerkt en het spel werkt naar behoren.






## 19 november 1245

ik heb de code nog eens overlopen om alles nog eens op te frissen en goed te begrijpen hoe alles werkt zodat ik bij het uitbreiden van het spel hopelijk bugs sneller kan oplossen. ik wil het spel om te beginnen visueel verbeteren dus ik heb om te beginnen de grootte van het scherm veranderd en de layout van de knoppen aangepast zodat het hele scherm benut wordt. dit ging al bij al vrij vlot het enige probleem dat ik enkele keren heb gehad was een foutieve of niet optimale x,y waarde ingeven. 






## 20 november 1705

ik heb de 'suits' toegevoegd zodat elke kaart nu bestaat uit twee delen (bvb '2H') de rank en de suit. verder ook de code aangepast zodat alles blijft werken. de voornaamste aanpassingen waren aan calculate_score en draw_cards. Dit verliep vrij vlot. ik ben ook aan het zoeken hoe ik de kaarten kan voorstellen met pixelart ipv de simpele rechthoeken met een getal. Ook een aanpassing gemaakt aan hoe de score berekend wordt naar iets dat mij logischer leek.




## 15 december 1610

ik heb een deel van de code om de kaarten met pixelart voor te stellen. ik heb eerst veel tijd verloren om via trial en error ergens toe te proberen komen maar ik bleef problemen hebben. ik heb dan vanalles opgezocht over wat alle functies juist deden (screen.blit, pygame.draw, pygame.surface, ...) en wat de beste manier is om objecten te tekenen. ik had dit beter eerst gedaan dan had ik eerder gerealiseerd dat ik het gebruik van de functies verwarde.






## 16 december 1615

het voorstellen van de kaarten met pixelart werkt nu. eerst een pixelart symbool voor elke suit laten genereren, elk symbool bestaat uit een combinatie van vormen in de juiste kleur. wel nog veel problemen gehad met de coordinaten voor welk element waar moet komen. ook werken met de instructie list was moeilijk. deze geeft drie parameters terug maar afhankelijk van de shape heeft deze een andere lengte. draw_cards roept render_card aan, render_card roept get_card_pixel_instructions aan en geeft een list terug die render_card gebruikt om de kaart samen te stellen.





## 17 december 1700

verder gewerkt aan de kaarten voor te stellen met pixelart, ik heb de ??? kaart vervangen met pixelart van de achterkant van een kaart. Dit ging vlotter dan de voorkant aangezien dit altijd hetzelfde is. de kaart is een list bestaande uit elementen die elk bestaan uit een string van W en R characters waar W wit is en R rood. daarna het patroon tekenen met enumerate if, else.





## 18 december 1630

ik heb de layout aangepast zodat alles mooi op het scherm past en er geen overlappingen zijn. ik wilde ook de wins van de player voorstellen met pokerchips. voor elke win verschijnt er een chip naast de hand van de player. het aantal chips is gelijk aan het aantal wins min het aantal losses. het tekenen van de chips leek niet zo moeilijk aangezien een ellipse gedefinieerd wordt door een rechthoek. maar om het geheel op een pokerchip te laten lijken was erg moeilijk heb wel wat verbeteringen van chat gbt nodig gehad. ook had ik enkele bugs bij het laten alterneren van de chipsstapel. verder wil ik ook een manier zoeken om het spel meer persoonlijkheid te geven door een soort dialoog toe te voegen. al bij al lang gewerkt aan iets dat ik dacht dat vrij simpel ging zijn.






## 19 december 1720

ik heb een aparte klasse gemaakt voor tekstbubbels die de speler begroet bij het begin en ook de uitkomst van elke ronde vertelt. de code werkt maar is niet optimaal. het geeft op dit moment geen problemen omdat het maar kort gebruikt wordt en alles wordt gereset na elke ronde.

ik had ook het idee om een pokerchip te laten "vallen" op het moment dat het spel begint. maar ik zie nu in dat de manier waarop ik nu een chip op het scherm teken niet geschikt is om dit te doen. het is nu een  functie die gewoon een x en y coordinaat neemt. ik ga hier een aparte klasse van moeten maken.





## 20 december 1330

ik ben begonnen aan het maken van een aparte classe voor de chips zoals voor de tekstbubbels er zitten nog enkele bugs in maar het doet iets. minder vooruitgang gemaakt dan ik had gehoopt.






## 21 december 1405

ik heb enkele bugs verbeterd in de chip classe. eerst werden niet alle elementen correct getekend door een probleem met de surface van de chip, sommige elementen werden direct op het scherm getekend en niet op de surface van de chip. dit had ik eerder moeten zien.daarna de posite en de snelheid van de chip aangepast zodat de chip op de juiste locatie belandt en het niet te lang duurt. ook nog een aanpassing gemaakt zodat de schaduw enkel getekend wordt als de chip niet beweegt.





## 25 december 1745

Na de chip classe nog meermaals veranderd te hebben werkt nu alles. ik heb een move_to functie toegevoegd zodat de positie van de chip meermaals aangepast kan worden. de update functie doet de chip dan effectief bewegen. ik gebruik nu een vector om de chip te laten bewegen wat beter is dan de chip trapsgewijs over het scherm te laten schuiven. ik heb ook nog enkele problemen gehad met het implementeren van de chip classe in de gameloop. het probleem was uiteindelijk dat de timing fout was en dat sommige parameters meermaals van waarde veranderden wat maakte dat de chips gewoon verdwenen. veel tijd verloren door dubbel werk te doen, ik had de chip classe en de functionaliteit beter moeten uitdenken voor ik eraan begon.




## 26 december 1610

alle code nog eens doorlopen en oude, overbodige code verwijderd. Nu ik de code nog eens heb bekeken zijn er veel dingen die ik nog zou willen aanpassen omdat ik nu meer weet en kan dan toen ik aan het project begon. veel dingen zijn niet optimaal of kunnen in bepaalde situaties op een niet bedoelde manier reageren. Ik heb echter geen tijd meer om ze aan te passen zonder over de 20 uur te gaan.


## reactie op feedback over project

op dit moment (1/1/2026) heb ik nog geen feedback ontvangen