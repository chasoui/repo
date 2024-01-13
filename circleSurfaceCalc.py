# Les 1 Opdracht 2 van het vak "programmeren en experimenteren" v/d UvA
# Geschreven door s Chaoui, 9 January 2024

"""
python r = input('staal r = ') oppervlakte = (float(r)**2) * 3,141592653589793 
print('oppervlakte = ', oppervlakte)
DOEL: 
1. Verbeter programma 
2.  leg uit waarom dit programma incorrect resulaat geeft
"""

r = input('staal r = ') 
oppervlakte = (float(r)**2) * 3.141592653589793
print('oppervlakte = ', oppervlakte)


"""
doel 1: Check, zie bovenstaand verbeterd programma
doel 2: " Log "
    1. " python " van line 3 weggehaald want dit geeft niks aan.
    2. het definieren van "r" en "oppervlakte " aparte lines gegeven
    3. opgemerkt dat er een comma staat in plaats van punt bij het
uittypen van Pi tot enkele decimalen en dit erna veranderd.  
    4. Na al dit toegepast te hebben werkt het programma
    Beschouwing: Dit programma had enkele syntax fouten zoals te zien 
in mijn logboek, maar ook een semantische fout met het verwisselen
van punt en comma. Dit is een typische fout die kan voorkomen. Verder
niks opgemerkt aan het programma. DEcimalen van pi niet gecheckt klopt
vast wel, iets wat ik volgende keer wel gelijk moet kunnen doen.
"""