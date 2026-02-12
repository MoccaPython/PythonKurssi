#käyttäjätunnuksen ja salasanan kysyminen. viiden arvauksen jälkeen peli poikki
#KT: phyton ss: rules

user = input("Anna käyttäjätunnus: ")
password = input("Anna salasana: ")
kyselyt = 1

k = "phyton"
s = "rules"

if user == k and password == s:
    print("Tervetuloa")

else:
    while kyselyt < 5:
        user = input("Anna käyttäjätunnus: ")
        password = input("Anna salasana: ")

        if user == k and password == s:
            print("Tervetuloa")
            break
        kyselyt = kyselyt + 1
        if kyselyt == 5:
            print("Pääsy evätty!")