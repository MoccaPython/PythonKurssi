tuntipalkka = float(input("Tuntipalkka: "))
tehdyt = float(input("Tehdyt tunnit: "))
paiva = input("Viikonpäivä: ").upper()

if paiva == "SUNNUNTAI":
    palkka = tehdyt * tuntipalkka * 2
    print("Päiväpalkka: ", palkka, " euroa")

else:
    palkka = tehdyt * tuntipalkka
    print("Päiväpalkka: ", palkka, " euroa")