#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
#Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

luku_str = input("Anna luku: ")

luku = int(luku_str)
luvut = []
luvut.append(luku)
while True:
    luku_str = input("Anna seuraava luku: ")
    if luku_str == "":
        break

    luku = int(luku_str)
    luvut.append(luku)

luvut.sort(reverse=True)
#luvut.reverse()

print(luvut[0:5])
#print(len(luvut))
#print(luvut)