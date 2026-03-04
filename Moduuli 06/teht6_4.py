#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
#Ohjelma palauttaa listassa olevien lukujen summan.
#Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def lukulista():
    luku_str = input("Anna kokonaisluku (tyhjä lopettaa funktion): ")

    lista = []
    while luku_str != "":
        luku = luku_str
        lista.append(luku)
        luku_str = input("Anna kokonaisluku: ")

    print(lista)
    return

lukulista()



