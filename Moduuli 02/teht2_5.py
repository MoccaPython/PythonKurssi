#leiviskät, naulat ja luodit kg:ksi
print("Anna leiviskät:")
Leiviska = float(input())
print("Anna naulat:")
Naula = float(input())
print ("Anna luodit:")
Luoti = float(input())
KG = (Leiviska * 20 * 32 * 0.0133) + (Naula * 32 * 0.0133) + (Luoti * 0.0133)
Desimaalit = (KG - int(KG)) * 1000
print("Massa nykymitoissa:\n" + str(int(KG)) + f" kilogrammaa ja {Desimaalit:6.2f} grammaa.")
