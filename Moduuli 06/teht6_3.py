#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa
#paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
#Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
#kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#Yksi gallona on 3,785 litraa.

def muunnos(gallonat):
    litrat = gallonat * 3.785
    return litrat

gallonat = int(input("Anna gallonat, negatiivinen luku lopettaa kyselyn: "))

while True:

    if gallonat >= 0:
        print(muunnos(gallonat))
        gallonat =int(input("Anna gallonat: "))
    else:
        break

#print(muunnos(gallonat))