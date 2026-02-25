"""
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

"""

def on_alkuluku(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Pyydetään käyttäjältä välin rajat
alku = int(input("Anna välin alku: "))
loppu = int(input("Anna välin loppu: "))

print(f"Alkuluvut välillä {alku}–{loppu}:")

for luku in range(alku, loppu + 1):
    if on_alkuluku(luku):
        print(luku)