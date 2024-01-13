####################################################################################
# Naam: S Chaoui, 14674920                                                        #
# Titel: Opdracht 8, vak 'Programmeren en Expermimenter' aan de UvA.              #
# Datum : 2024 Januari 11                                                         #
####################################################################################

""" DOEL:
Schrijf een programma dat alle paren van bevriende getallen
onder een door de gebruiker ingetoetste bovengrens berekent.
INfo: Twee natuurlijke getallen m en n heten bevriend als de som van de delers van m 
gelijk is aan n en de som van de delers van n gelijk is aan m. 
"""

import math


def delers(n):#functie die voor getal n een lijst van delers van n geeft.
    div = [1] # 1 is altijd een deler
    for i in range(2, int(math.sqrt(n))+1): # hoeven alleen tot sqrt(getal) te checken, zie uitleg logboek
        if n % i == 0:
            div.append(int(n/i))
            div.append(i)
    return div 

def som(l): # functie die de gegeven lijst van  delers sommeert
    ans = 0
    for _, i in enumerate(l):
        ans +=  i
    return ans 


gecheckt = [1]
vrienden = []
grens = 15000 # int(input(" Vul bovengrens in:"))

for m in range(1,grens+1):
    if m in gecheckt:
        continue # gaat naar volgende iter want m is al gecheckt op vriendschap
    elif m not in gecheckt:
        n = som(delers(m)) #we stellen n gelijk aan som(delers(m)), alleen nodig voor som(delers(n))    
        pm = som(delers(n)) # met deze " placeholder m" gaan we verglijken met " echte m "
        ppm = som(delers(pm))
        if n == m: #Nodige line omdat in de opdracht niet specifiek is aangegevn of m=n mag.
            continue
        elif m == pm: #Vb: m=220, dan n = 284 . Nu, zij pm = som(delers(284)) = 220. Er geldt nu m = pm
            vrienden.append([m,n])
            gecheckt.append(m)
            gecheckt.append(n)
        elif m != pm: #als dit paar niet bevriend is, voeg toe aan gecheckt om herhalingen te vermijden
            gecheckt.append(pm)
#ik had geen zin bovenstaande in functie nog te zetten
"""
svd(m)=n. pm=som(delers(n)). Stel je construeerd een n volgens n = svd(m). Dan moet gelden dat
svd(n)= pm == m voor vriendschap. Zij n = svd(m). Construeer pm := svd(n). Stel er geldt pm = m; succes.
Stel er geldt pm !=m; dan pm = a voor een a.
"""
def flauwemooimaak():
    print("bovengrens = ", grens)
    print("lijst van bevriende getallen m en n onder ", grens)
    print(" m\t n")
    for paar in vrienden:
        print(f"{paar[0]}\t{paar[1]}")

flauwemooimaak()


    

""" LOGBOEK
dag 1 - 17:03 -  Om te bepalen of getallen m,n, bevriende getallen zijn, moeten 
    wij eerst een programma schrijven die de delers van deze getallen m&n vinden.
    Dan lijkt het mij nadig deze getallen te onthouden en later optellen.
    Voor het delerprogramma hoeven wij "alleen" maar getallen tot n/2 te checken,
    want alles groter dan n/2 kan geenn deler zijn van n zelf. Maar computers zijn
    tegenwoordig efficient voor zulke kleine getallen dus wij gaan niet heel erg 
    nadenken over efficientie in deze zin. 
    programma gaat dus als volgt: bereken delers getallen 2-> sla deze op
    in een lijst ( ) -> check of SVD gelijk is aan getal < 15k -> check of delers 
    van SVD gelijk is aan het getal waaruit de SVD ontstaat - > zo wel, succes. Zo 
    niet, sla dit getallenpaar op -> Bij volgende iteratie wordt gecheckt of dit 
    getal m al voorkomt in de lijst, en dus hoeft deze niet gecheckt te worden. 
    We zullen dit testen met m=220 en n=300 met een bovengrens van 300.
dag 2 15:54 - Gister niks echt gecodeerd behalve een simpele functie voor vinden 
    van delers. Maar er is opgemerkt dat delers zich in " paren " kenbar maken,
    d.w.z., als n=20 en een deler d = 5, dan is ook n / d = 20 / 5  = 4 een deler 
    van n. Verder is 1 altijd een deler dus die is al in de lijst gezet, lijst ordening
    maakt overigens niet uit voor dit probleem, index is onnodig. 
    17:04 - Succesvol een deler en som functie gemaakt. Bezig met de check functie die 
    kijkt of de getallen gelijk zijn. Ik wil als dit niet zo is deze opslaan in een lijst
    en bij de volgenxde iteratie checken ofde svd = som(l1) gelijk is aan de som van de delers van de 
    som van de delers, ofwel of svd = som(delers(som(l1))) = svdvsvd. Als dit zo is, succes. 
    Als dit niet zo is, slaan we zowel svd, svdvsvd als op en wordt dus bij volgende iteratie
    gecheckt of deze niet al is gewesst, dus " if svd in gecheckt ". HEt lukt mij niet om
    in 1x een functie zoals deze te bedenken, dus ik verdeel het nogmaals in stappen:
    start: for- loop geeft getal m
    -> 2 opties: Of m in gecheckt; next iter. Of niet in gecheckt; cont.
    -> svd(m) wordt gemaakt en nieuwe n = svd(m). 
    -> bereken pm:= svd(n) (= svd(svd(k)) mais s'en cache)
    -> Logica check of pm = m :
    -> 2 opties: Als pm=m, dan zijn ze maatjes: succes. Als pm != m, dan, getal opslaan.
    -> na het opslaan van pm,m, voor getal m+1 wordt bekeken of m+1 in gecheckt: 
    -> 2 opties: of m+1 zit in gecheckt; niks doen. Of m+1 zit niet in gecheckt: svd(m+1) wordt gemaakt en gecheckt ->
    -> 2 opties: of svd(m+1) in gecheckt; niks doen. Of svd(m+1) niet in gecheckt; loop " compleet "
    -> nu weer berekenstap net zoals berekening van pm. 
18:17 - Ik heb het bovenstaande process gecodeerd en het werkt! heel fijn behalve dat er dubbels
    voorkomen in de lijst van vrienden. Een getal kan blijkbaar ook bevriend zijn met zichzelf. Dit is
    slecht in de opdracht dgedefinieerd.
    Dus om die te verwijderen heb ik nog een extra logica statement gemaakt om dit te vermijden. 
    18:46 - I call it a day. Nog eventjes text opmaak geschreven en paar comments geadd.
        het programma werkt dus ik noem het een succes. Ik sla 1761 = 15000 - len(gecheckt) over wat ik wel
        nice vind.
"""