import random

# Kysytään noppien määrä
maara = int(input("Kuinka monta noppaa heitetään? "))

# Luodaan tyhjä lista tuloksille
nopat = []

# Arvotaan jokaiselle nopalle silmäluku
for i in range(maara):
    silmaluku = random.randint(1, 6)
    nopat.append(silmaluku)

# Tulostetaan lista
print("Noppien silmäluvut:", nopat)