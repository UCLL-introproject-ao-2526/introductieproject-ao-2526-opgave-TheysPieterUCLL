
16 october 15:00 – 17:20
ik heb de opdracht nog eens nagelezen en alles klaargeze in vs code en de tutorial beginnen lijken. tot nu toe gaat alles vlot. de code wordt goet uitgelegd maar ik heb bij enkele punten nog wat extra uitleg gevraagd aan chatgbt om zeker te zijn dat ik de logica begrijp. enkel weten wat elke parameter doet is soms moeilijk te volgen. verder heb ik ook de code toegevoegd aan mijn project om sneller te kunnen nakijken en de video geliked!

17 october 13:00 - 16:00
ik heb verder gwerkt aan de blackjack project. er was een probleem met dat de kaarten niet op het scherm verschenen, na enkele keren terug te gaan zag ik dat in de return van deal_cards de twee variabele moesten omgedraaid worden. verder was ik de coordinaten van dealer cards vergeten aan te passen.  Ik ben na aan het denken hoe ik later het spel visueel kan uitbrijden en 'suite' toevoegen.

18 october 8:20 - 10:10
probleem met hit me button, uitijndelijk was het probleem dat de variable hand_active op false bleef staan. bij testen van de game bleek er een probleem te zijn vanaf de twede ronde. na het vergelijken van mijn code met de originele bleek dat ik een van de variabele was vergeten te resetten ( reveal_dealer) waardoor de game bevroor. ik heb de tutorial afgewerkt en het spel werkt.



19 nov 11:00 - 12:45
ik heb de code nog eens overlopen om goed te begrijpen hoe alles werkt zodat al ik bij het uitbrijden van het spel problemen tegenkom ik sneller de oorzaak kan terugvinden. ik wil het spel om te beginnen visueel verbeteren dus ik heb om te beginnen het scherm verandert en de layout van de knoppen aangepast zodat het hele scherm benut wordt. dit ging al bij al vrij vlot het enige probleem dat ik enkele keren heb gehad was een foutieve of niet optimale x,y waarde ingeven. 



nov 18 14:45 - 17:05
verder ben ik ook begonnen met het toevoegen van de "suits" van de kaarten. vergde wel enkele aanpassingen aangezijn elk element in de hand list nu twee waarden heeft en dus telkens gesplitst moet worden om bijvoorbeeld de score te berekenen.
verder werken aan het toevoegen van de suits. de grootste verandering is in calculate_score, dit was niet zo moeilijk aangezien ik gewoon het rank and suit deel moest splitsen de restblijft hetzelfde. ok aangepast hoe de score berekend wordt naar iets dat mij logiser leek. 
daarna zoeken hoe ik de kaarten kan voortellen met pixel art. 


dec 15
13:00 - 14:05
ik heb enkele videos gekeken op youtube hoe ik ditb zou kunnen doen. en opgezocht hoe het tekenen in pygame juist werkt
de beste manier zou zijn door eerst een surface te maken, daarna hier alle elementen op te tekenen en daarna het surface object te displayen met blit met de juiste coordinaten. een instructie functie zecht hoe de kaart te maken, render functie stelt dan de kaart samen.


dec 16 14:30 - 16:15
 eerst een pixel art symbool voor elke suit laten genereren door chat gbt, elk symbool bestaat uit een combinatie van vormen in de juiste kleur. 
 veel problemen gehad met de coordinaten voor wat waar moet komen. ook werken met de instructie list was moeilijk. deze geeft drie parameters terug daar afhankelijk van de shape heeft param een andere lengte. maar  vrij weinig vooruitgang gemaakt.


dec 17
15:00 - 17:00
verder werken aan de kaarten voor te stellen met pixel art, ik wil ook de ??? kaart vervangen met de achterkant van een kaart. de achterkan van de kaart word maar een keer gebruikt dus hiervoor gebruik ik een pattern list bestaande uit elementen die elk bestaan uit een string van W en R characters waar W whit is en R red. daarna het patroon tekenen met enumerate if, else. dit ging vlotter dan de voorkant van de kaarten te maken.

dec 18
15:15 - 16:30
layout aangepast zodat alles mooi op het scherm past en er geen overlappingen zijn. ik wil ook de wins van de player voorstellen met chips. voor elke win verschijnd er een chip naast de hand van de player. het aantal chips is gelijk aan het aantal wins min het aantal losses. Na er lang aan gewerkt te hebben maar wijnig vooruitgang. het tekenen van de chips leek niet zo moeilijk aangezien en elips gedifigneerdt wordt door een rechthoek


maar om het geheel op een poker chip te doen lijken was erg moelijk. heb wel wat verbeteringen van chat gbt nodig gehad. ook even moeten zoeken hoe ik de stapel kon doen alterneren. verder wil ik ook een manier zoeken om het spel meer persoonlijkhijd te geven door een soort dialoog toe te voegen.



dec 19
15:30 - 17:20
ik heb een apparte classe gemaakt voor text bubbels, deze worden aangeroepen in de game verschijnen op het scherm en verdwijnen dan weer. de code werkt maar is echt niet optimaal. het geeft op dit moment geen problemen omdat het maar kort gebruikt wordt en alles wordt gereset na elke ronde.ik had ook het idee om een pokerchip te laten "vallen" op het moment dat het spel begint. maar ik zie nu in dat de manier waarop ik nu een chip op het scherm teken niet geschikt is op dit te doen. het is nu een  functie die gewoon een x en y coordinaat neemt. ik ga hier een apparte classe van moeten maken.


dc 20
11:30 - 13:30
lang gewerkt op chip een eigen class te make, nog niet perfect maar het doet iets. het heeft ook even geduurt om de chip te doen bewegen. moet er nog verder aan werken maar de chip van begin locatie naar eind locatie te doen bewegen lukt wel.


dec 21
12:45 - 14:05
debuggen van de chip class en verder veerbeteren. eerst werden niet alle elementen van de chip getekent door een probleem met de chip surface. daarna de posite en de snelhijd van de chip aangepast zodt de chip op de juiste locatie beland en het niet te lang duurt. ook nog een aanpassing gemaakt zodat de schaduw enkel getekent wordt al de chip niet beweecht.

dec 22
16:20 - 17:30
de oude draw chip functies overal vervangen door de nieuwe classe. ik had eerst enkele problemen bij het aanpassen va de code maar de meeste dingen werken nu. ik heb ook het winnen van chips aangepast zodat deze ook bewegen. ik ze nu wel in dat ik de classe van chip beter anders had kunnen maken, nu wordt de begin en eindpositie vastgelegt bij het maken van de chip, het update beweecht de chip dan. het was beter geweest als de update functie de eindcooordinaten als parameters nam zodat een chip meermaals verplaatst kan worden.

dec 23
16:10 - 17:30
aanpassen van chip class zodat de update funcie meer flexibel wordt en een chip meermaals verplaats kan worden. ik wil ook de update functie aanpassen zodat de chip ook in de x as kan verplaatst worden. er lijken 2 manieren hiervoor te bestaan, x en y appart laten bewegen of werken met vectoren. ik wil de vectoren gebruiken, gellukkig heb ik veel wiskunde gehad. de code werkt voor het grootste deel

dec 24
9:20 10:30
toch nog veel problemen gehad met de chips te doen bewegen. als de speler verliest moet er een chip van de stapel verweidert worden door de positie te updaten maar dit blijft problemen geven. ik zie niet goed wat het probleem in maar het heeft iets te maken met timing en parameters die niet correct worden aangepast. wijnig vooruitgang kunnen maken

dec 25
11:30 - 14:00
na de chip classe nogmaals aangepast te hebben en de update functie aan te passen, werkt alles zoals gewenst. ik heb een move_to functie toegevoegd die te target positie van de chip aanpast. de update functie laat dat de chip dan bewegen. als ik meer tijd had gehad zou ik de kaarten ook een eigen klasse hebben gemaakt zodat deze ook kunnen bewegen. verder heb ik de code nog wat opgekuist en oude onnodige code verwijdert.

