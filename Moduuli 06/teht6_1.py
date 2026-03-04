#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
#Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
#Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def noppa():
    silmaluku = random.randint(1,6)
    #print (silmaluku)
    return silmaluku

heitot = 0

while True:
    i = noppa()

    if i != 6:
        heitot += 1
        print(i)
    else:
        print(i)
        heitot += 1
        print("Heittoja tarvittin", heitot, ", jotta tuli kutonen!")
        break