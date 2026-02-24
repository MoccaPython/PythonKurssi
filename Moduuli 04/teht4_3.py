#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon
#lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luku_str = input("Anna luku!\nTyhjä lopettaa kyselyn \n")


luku = int(luku_str)
suurin = luku
pienin = luku

while True:
    luku_str = input("Anna luku! ")
    if luku_str == "":
        break
    luku = int(luku_str)
    luku = int(luku_str)
    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku
print(f"Suurin antamasi luku on {suurin}, pienin antamasi luku on {pienin}")