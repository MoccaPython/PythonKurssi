#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
#Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

#Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

luku = int(input("Anna luku: "))
lista = []
"""
if luku == 2 or luku == 1 or luku == 3:
    print(f"Luku {luku} on alkuluku!")
"""
#else:
for i in range(1, luku+1):
    if luku % i == 0:
        lista.append(i)
        #if len(lista) >= 3:  #keskeyttää ajon kun löytyy ensimmäinen jakaja kuin 1 ja luku itse
         #   break

if len(lista)>2:
    print(f"Luku {luku} ei ole alkuluku!")
    print(f"luvulla on ", len(lista), "jakajaa!")  # jos halutaan saada selville luvun jakajat ja niiden määrä
    print(lista)

else:
    print(f"Luku {luku} on alkuluku!")
    #print(lista)
