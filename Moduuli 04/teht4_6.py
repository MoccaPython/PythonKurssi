#piin likiaron laskeminen

import random
import math

print("Lasketaan piin likiarvo yksikköympyrän avulla!")
N = int(input("Montako pistettä arvotaan? "))
loopit = 0
circle = 0

while loopit < N:
    ax = random.randint(-10000, 10000)  # jaetaan nämä 10000 saadaan tarkemmin väli -1, 1
    ay = random.randint(-10000, 10000)

    x = ax / 10000
    y = ay / 10000


    if x**2+y**2 < 1:
        circle = circle + 1

    loopit = loopit + 1

pii = 4 * circle / N
print("Piin laskennallinen likiarvo on: ", pii)
print("Piin todellinen likiarvo on: ", math.pi)
