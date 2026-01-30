#leiviskät, naulat ja luodit kg:ksi
print("Anna leiviskät:")
Leiviska = float(input())
print("Anna Naulat:")
Naula = float(input())
print ("Anna luodit:")
Luoti = float(input())
KG = (Leiviska * 20 * 32 * 0.0133) + (Naula * 32 * 0.0133) + (Luoti * 0.0133)


#print("Massa nykymitoissa:")


print (f"kilot: {KG:4d}")