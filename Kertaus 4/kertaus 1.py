nimi = input("Kerro nimesi: ")

if nimi == "Matti":
    print("Kiitos, seuraava!")

else:
    annokset = int(input("Montako annosta? "))
    summa = annokset * 5.90
    print("Kokonaishinta on ", summa)
    print("Seuraava, kiitos!")