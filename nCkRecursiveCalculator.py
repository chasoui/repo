##############################################################################
# Naam: s CHAOUI, 14674920                                                   #
# Titel: Les 7, Opg. 2, vak: 'Programmeren en Expermimenter' aan de UvA.     #
# Start datum : 2024 Januari 13 ---- Einddatum:  2024 Januari 13             #
##############################################################################
"""
doel: Maak een dictionary met sleutels de paren (n,k) en bijbehorende waardes de 
waardes van de binomial coefficienten C(n,k). Bereken C(40,3) en C(100,50). 
"""


#maken eerst een woordenboek.
nCkDict = dict() # { (n, k) : nCk}, nCk als afkorting voor "n choose k" (engels)

#standaardgevallen: eerste en laatste getal in rij is altijd 1
def baseCase(var):
    n, _ = var
    #sleutels met waarde (m,0) en (m,1) maken voor i<=m
    for k in range(0,n+1):
        if k>0:
            nCkDict[(k,0)] = 1 #Eerste getal rij is 1
            nCkDict[(k,k)] = 1 #Laatste getal rij is 1
            nCkDict[(k,1)] = k #Uit symmetrie
            nCkDict[(k,k-1)] = k

def nCk(key): # onthoud key moet een tuple zijn. Paar i,j invoeren moet als (i,j)
    n, k = key
    if key not in nCkDict:
        nCkDict[key] = nCk((n-1,k-1))+nCk((n-1,k))
    return nCkDict[key]

var = (1000,500)
baseCase(var)
nCk(var)
print(var, nCkDict[var])

"""
logboek: 
dag 8471 ( 13 Jan )
15:00 - Ik heb doorgespoeld en ben aan les 7 begonnen. Deze 
    opgave ga ik aanpakken d.m.v. de recursieve definitie van de fibanacci reeks 
    uit les 7 te halen en de 2 verschillende codes te vergelijken, een van de methode
    met dictionaries en het process te reverse engineeren. Eerst paar feiten:
    -   Sleutels: De paren (n,k). De waardes: nCk. {sleutel : waarde}
    -   De fib functie heeft 1 input, nCk functie heeft er 2
    -   we weten dat er symmetrie zit in de driehoek van pascal
    -   Alleen k gaat omhoog, n niet.
    Ik heb het gevoel dat we eerst de sleutels invoeren en dan recursief de waardes
    van nCk moeten gaan berekenen. Fijne is dat we geenn waarden hoeven te hechten 
    aan elke sleutel. We zetten de sleutels in de dict d.m.v. een for-loop
15:21 - Het is niet handig om in 1 keer alle sleutels toe te voegen. Men wilt 
    namelijk " if key not in " gebruiken, maar als alle keys er wel aan in zitten 
    gaat dit lastig. Dus definieren we eerst de gedefinieerde gevallen in onze func.
    De realisatie is tot mij gekomen hoe wij de driehoek van pascal kunenn gebruiken
     ( denk ik ). We definieren de eerste 2 rijen en denken verder. Oke we gaan
     ook de "muren" van de driehoek van pascal definieeren met een for-loop.
16:12 - Het besef dat we achteruit moeten werken is ook geland. Althans:
    Hebben we waarde van nCk? 2 opties:Zo ja; succes. Zo nee, - > 
    Hebben we waarde van (n-1)Ck en (n-1)C(k-1) ? En herhaal bovenste. 
    Dit gaat door tot waarde die bekend zijn bij de 1e en laatste kolom van pascal.
    " We weten waaruit het grootte bestaat maar hebben de bouwstenen niet, breek
    het grootte op tot je bouwstenen ziet die je wel hebt. Dan beginnen met bouwen." 
17:06   - Gelukt om standaard gevallen te implementeren.
        - Nu aan de slag met recursie gedeelte.
        - BEseft dat ik de gehele pyramide kan bouwen en dan met sleutels opvragen:
        ik ga proberen achteruit te werken met while loop die steeds kijkt of we 
        de vorige som al kunnen uitrekenen.
17:45   - Programma werkt, maar was wel gedoe erover na denken terwijl het simpelweg
            de opmaak is van de fibonacci. 
        - Grootste werk was uiteindelijk het nadenken over de aanpak. In het vervolg
            zal ik eerst een goede outline moeten maken voordat ik echt aan het code
            begin. Ik bedoel dit doe ik al, maar in mijn hoofd meestal. Dat kan soms
            verwarrend zijn en dan schrijf ik het toch op. Misschien dus beter om 
            voortaan direct het op te schrijven, het liefst via de IDEA Methode die 
            ik op de TU geleerd had. 
        - programma is best efficient, ik kan vrijwel alles tot grootte 4 decimalen
            snel uitrekenen. Ik denk dat dit beter is want men laat groot deel van 
            de 3hoek buiten beschouwing want dat is niet nodig. 
            (1000,xxx) doet die met gemak.
        - mood: trots enigszins
"""