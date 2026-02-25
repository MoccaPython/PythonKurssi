#Ohjelma tarkistaa onko annettu vuosiluku karkausvuosi

vuosi = int(input("Anna vuosiluku, niin tarkistan onko se karkaus vuosi! "))

if vuosi >= 0:
    if vuosi % 400 == 0 and vuosi % 100 == 0:
        print("Vuosi", vuosi, "on karkausvuosi")
    elif vuosi % 100 == 0:
        print(vuosi, "ei ole karkausvuosi!")
    elif vuosi % 4 == 0:
        print(vuosi, "on karkausvuosi!")
    else:
        print("Vuosi", vuosi, "ei ole karkausvuosi!")

else:
    print("Kelvoton vuosiluku!")


"""
if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print("Vuosi on karkausvuosi!")
else:
print("Vuosi ei ole karkausvuosi!")
"""