from math import sqrt

#print (sqrt(9))

numero = int(input("Anna numero: "))

while True:
    if numero > 0 and numero <= 100:
        print(sqrt(numero))
        numero = int(input("Anna numero: "))
    elif numero == 0:
        break
    elif numero < 0:
        print("Virheellinen numero")
        numero = int(input("Anna numero: "))
