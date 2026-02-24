#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

nopat = int(input("Anna Arpakuutioiden määrä: ")) #noppien määrä

import random

silmaluvut = [] #lista johon noppien silmä luvut kasataan

for i in range(nopat):
    silma = random.randint(1,6) #arpoo nopan silmälukeman
    silmaluvut.append(silma)

summa = sum(silmaluvut) #listan silmalukujen summa
print(summa)
print(len(silmaluvut))
"""
vanha = 0
for luku in range(1,7):
    if luku != vanha:
        print("Luku", luku, "on listassa", silmaluvut.count(luku), "kertaa.")
    vanha = luku
"""