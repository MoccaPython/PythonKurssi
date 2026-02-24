#ikä = int(input("Anna ikä: "))
#if 15<=ikä<18:
#    paino = float(input("Anna paino (kg): "))
#if (ikä>=18 or ikä>=15 and paino>=55):
#    print("Lääkkeen käyttö on sallittua.")
""""
komento = input ("Anna komento: ")
while komento!="lopeta":
    print ("Suoritan toiminnon: " + komento)
    komento = input("Anna komento: ")
print ("Toiminnot lopetettu.")
"""
"""
while True:
    korkeus = int(input("Korkeus: "))
    leveys = int(input("Leveys: "))
    if korkeus <= 0 or leveys <= 0:
        # negatiiviset arvot eivät kelpaa
        continue
    for y in range(korkeus):
        for x in range(leveys):
            # end = "" tarkoittaa, että ei tulosteta loppuun rivinvaihtoa
            print(end="*")
        # tässä taas tulostetaan pelkkä rivinvaihto
        print()
    vastaus = input("Haluatko jatkaa (k/e)? ")
    if vastaus == "e":
        break
"""
"""
nimet = []

etunimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while etunimi != "":
    nimet.append(etunimi)
    etunimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")

for nimi in nimet:
    print (f"Moi, {nimi}!")
"""
luku = int(input("Anna luku: "))

viimeinen = abs(luku) % 10

print("Viimeinen numero on:", viimeinen)