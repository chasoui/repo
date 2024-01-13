#ik heb de opdracht wat aangepast zodat het wat overzichtelijker is
# ( hoop ik )
#"edit" staat voor aangepassingen in oude line code van originele programma
#"add" staat voor eenTOEVOEGING van een nieuwe line t.o.v. nieuwe prog.
 
def sumEx1():
    #add: de variabele moest som wel eerst gedefinieerd worden
    som = 0
    for i in range(1,101):
        #Edit: ^ is een bitwise operator, men moest ** gebruikeN
        som = som + (-1)**i / i 
    print(som)

def sumEx2():
    #add: de variabele moest som wel eerst gedefinieerd worden 
    som = 0
    for i in range(1,101):
        #Edit: ^ is een bitwise operator, men moest ** gebruikeN
        som = som + (-1)**i/i
        print(som)

print(" 1e for loop: ")
sumEx1()
print(" 2e for loop: ")
sumEx2()
### het verschil tussen de 2 loops is dat bij de eerste for loop,
### de print statement buiten de functie wordt opgeroepen, 
### en ons ALLEEN het uitgerekende eindantwoord som geeft.
###
### Bij de tweede for loop wordt de print functie wel 100 keer 
### opgeroepen, omdat deze print functie in de for loop zelf zit
### waarover dan ook 100 keer geitereerd wordt. Dus in dit geval 
### krijgt men ook alle " tussen antwoorden" gegeven, i.e., het ant-
### woord van elke rekenstap.