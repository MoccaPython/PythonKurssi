#Ohjelma tarkistaa onko annettu vuosiluku karkausvuosi

vuosi = int(input("Anna vuosiluku, niin tarkistan onko se karkaus vuosi!"))

if vuosi >= 0:
    if vuosi % 400 == 0 or vuosi % 4 == 0:
        print("Vuosi", vuosi, "on karkausvuosi")
    else:
        print("Vuosi", vuosi, "ei ole karkausvuosi")

else:
    print("Kelvoton vuosiluku!")