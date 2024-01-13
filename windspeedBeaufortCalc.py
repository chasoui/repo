# Les 1/2 Opdracht 3, 5 en 8 van het vak "programmeren en experimenteren" v/d UvA
# Geschreven door s Chaoui, 9 January 2024 met Visual Studio Code. 


# %%# Opdracht 3.1
"""
Doelen: 
    1. Schrijf een Python programma dat bij gegeven temperatuur en
    gemiddelde windsnelheid de gevoelstemperatuur uitrekent. 
    2. Pas de code aan zodat de windsnelheid volgens de schaal van 
    Beaufort wordt gesprecifieerd d.m.v. een gegeven omrekenformule.
"""

def gevoelTemp():
    #w = (7/0.836)**(2/3) ( herleid uit gegeven verglijking voor w)
    #t = 5
    w = float(input("Geef windsnelheid: "))
    t = float(input("Geef temperatuurin graden Celcius "))
    G = 13.12 + 0.6215*t + (0.4867*t -13.96 )*(w**(0.16))
    print(G)

gevoelTemp()

""" Logboek:
    1. rekenfunctie makkelijk gemaakt met gegeven invoer voor wind en 
    temp, hiermee is doel 1 bereikt.    
"""

# %%# Opdracht 3.2
def gevoelTemp():
    B = (7/0.836)**(2/3) ( herleid uit gegeven verglijking voor w)
    #t = 5
    # Bovenstaande is voor snelle test

    #B = float(input("Geef windsnelheid m.b.t. schaal van Beaufort: "))
    t = float(input("Geef temperatuurin graden Celcius "))
    w = 0.836 * B * sqrt(B)
    G = 13.12 + 0.6215*t + (0.4867*t -13.96 )*(w**(0.16))
    print(G)

gevoelTemp()
 """ LOGBOEK:
    2. We moeten de code aanpassen zoals in doel 2 wordt gespecif-
iceerd wordt, dus we voegen de gegeven code in in onze huidige functie.
    3. sqrt uit math pakket geimporteerd voor de wortelfunctie
    4. functie omgebouwt zodat het nu invoer krijgt voor B en t,
gebruik t= 5 en B = (7/0.826)**(2/3) voor G =~ 0.5
    5. De functie werkt voldoende en geeft schijnbaar juiste antwoorden,
hiermee is doel 2 bereikt.
    Beschouwing: ik heb geleerd goed op te letten bij het gebruiken
    van operator en het herdefinieren van deze. 7/10.
    Vraag: Ik merke op dat 0.6215 = 5/8 en 0.16 = 4/25, is het beter
om deze in decimalen te laten of wel als breuk. Mijn programmeer gut 
feeling zegt in breuk als het gaat om rationele en decimaal voor irrationeel mits mogelijk.
"""
# %%
