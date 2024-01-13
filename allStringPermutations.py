# Les 2 0pdracht 5van het vak "programmeren en experimenteren" v/d UvA
# Geschreven door s Chaoui, 9 January 2024 met Visual Studio Code. 

""" doel:
1. Schrijf een Python programma dat via geneste herhalingen de cijfers in 123 permuteert.
2. Schrijf nu ook zo'n programma voor de permutaties van 1234. 
""" 

num = '1234'

for i, _ in enumerate(num): # for-loop die itereerd over eerste cijfer van getal-permutaties
    begin = num[i]
    shuf =  num[:i] + num[i+1:] # de cijfers die we gaan permuteren en plakken aan begin getal
    for j, _ in enumerate(shuf): #loop die de rest cijfers shuffelt, j is de index en _ 
        print(begin+shuf[j:]+shuf[:j]) # de string wordt eigenlijk opgebroken in 2 delen en wordt andersom
                                        # aan elkaar geplakt




"""Logboek
1. men weet dat er n! permutaties zijn voor een getal met n cijfers, dus
    importereert men het math pakket met afkorting "mm" voor de factoriaal functie.
2. We weten dat er geitereerd moet worden over de lengte n!, dus maken wij een for-loop
    met die lengte.
3. we definieren de te permuteren getallen als een string zodat we deze 
    later kunnen slicen en " plakken "
4. we testen eerst een kleine functie met range enkel 2 om een gevoel te krijgen voor
    hoe we de string moeten slicen m.b.t. het itereren tussen het slicen door. Daarmee
    kunnen we kijken hoe bij elke iteratiestap de string wordt gesliced.
5. het werkte met range 2, maar wat er eigenlijk gebeur is dat men num[0] vasthoudt, 
    en bij de volgende iteratie zou men willen dat num[1] vastgehouden wordt als eerste cijfer 
    van het getal. dus moeten we ook itereren over de 3 mogelijke startwaardes voor het eerste.
    Dit lijkt het handigst door nog een for-loop te definieren van range 3 ( ofwel de lengte
    van de string, gegeven door len(num),  merk op dit telt van 0 tot len(num)-1 ). 
6. Dit plan gaat nergens heen, ofwel ik heb een beter plan: ik hoef aleen een deel van de
    eene kant te slicen en de andere kant er achteraan plakken. 
7. na de code zo gemaakte te hebben besef ik mij dat dit eigenlijk niet werkt want dit 
    schuift welliswaar alleen de getallen op en geeft mij allen permutaties, maar 
    zo verkrijg ik niet de wenste volgorde hiervan. Dus een nieuwe aanpak is nodig.

8. We weten dat we het eerste cijfer vast moeten houden, dus laten we dat sowieso definieren.
9. dan lijkt het alsof de getallen wel verschuiven, maar dat het begincijfer verborgen is
    en bij de verschuiving verdwijnt:.

Dag 2, ik ga opnieuw aan de opgave beginnen. Wij gaan het probleem als volgt aanpakken.
1X:XX - Merk op dat het begin getal steeds hetzelfde blijft per 2 permutaties, misschien is een for-loop
            voor dit process handig. We testen eerst met het getal 1 als eerste cijfer. Dan gaan we de 
            cijfers van de rest van de string slicen om vervolgens te permuteren en plakken aan het begingetal.
15.58 - Het slicen is gelukt. Nu moeten wij een manier vinden om deze overige getallen te husselen. 
        Dit zal in een tweede for-loop moeten gebeuren. Overigens wisselen we de string num af en toe van 
            '123' naar '1234' om het gedrag te inspecteren ,met '1234' is het 
            gedrag namelijk duidelijker ( gedrag = " wat er gebeurdt met getallen ")
16.17 - ik ben erachter gekomen dat je ook direct de characters uit de string kan pakken, dus ik hoef
            bij dit onderdeel niet te werken met indexes. Kijken naaar de gegeven volgorde lijkt
            het alsof men een horizontale verschuiving maakt. Dus gaan we het probleem zo aanpakken, en laten 
            wij het plakken terzijde.
16.41 - Zo'n 15 min geleden is het mij gelukt, door toch indexes te gebruiken haha.
         Eigenlijk met slicen is dit best makkelijk te doen. 
        Het werkt schijnbaar voor 123 en 1234 dus ik ben content
"""
