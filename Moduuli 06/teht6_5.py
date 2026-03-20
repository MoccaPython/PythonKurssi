#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
#Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi,
#että siitä on karsittu pois kaikki parittomat luvut. Kirjoita testausta varten pääohjelma, jossa luot listan,
#kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

def pariton(listaus):
    for luku in listaus:
        if luku % 2 != 0:
            listaus.remove(luku)
    return listaus#[luku for luku in listaus if luku % 2 == 0]

luku_str = input("Luodaan kokonaislukulista. Anna kokonaisluku (tyhjä lopettaa funktion): ")

lista = []
while luku_str != "":
    luku = int(luku_str)
    lista.append(luku)
    luku_str = input("Anna kokonaisluku: ")

alkulista = lista.copy()
pariton(lista)
print("Alkuperäinen lista: ", alkulista)
print("Parittomien lista: ", lista)