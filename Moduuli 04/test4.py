#luku = 1
#while luku<1000:
 #   if luku % 3 == 0:
  #      print (luku)
   # luku = luku + 1

# Tänne ei koskaan päästä:
#print("Valmista tuli.")



import random

# Kysytään käyttäjältä arvottavien pisteiden määrä
N = int(input("Anna arvottavien pisteiden määrä: "))

ympyran_sisalla = 0
laskuri = 0

while laskuri < N:
    # Arvotaan piste neliöstä [-1,1] x [-1,1]
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # Tarkistetaan, onko piste yksikköympyrän sisällä
    if x ** 2 + y ** 2 < 1:
        ympyran_sisalla += 1

    laskuri += 1

# Lasketaan piin likiarvo
pi_likiarvo = 4 * ympyran_sisalla / N

print(f"Piin likiarvo on: {pi_likiarvo}")
