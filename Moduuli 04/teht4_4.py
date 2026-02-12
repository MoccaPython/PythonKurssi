#kone arpoo luvun 1-10 ja käyttäjän täytyy arvata se
import random
arvottu = random.randint(1,10)
#print(arvottu)
arvaus = int(input("Arvaa numero 1-10! "))

while arvottu != arvaus:
    if arvottu < arvaus:
        print("Liian suuri arvaus!")
    elif arvottu > arvaus:
        print("Liian pieni arvaus!")
    arvaus = int(input("Arvaa numero 1-10! "))
print("Oikein!")
