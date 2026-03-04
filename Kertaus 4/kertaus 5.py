

while True:
    toimitus = input("Mitä haluat laskea (+, -, *, /), muu komento lopettaa ohjelman: ")

    if toimitus == "+":
        luku1 = int(input("Anna ensimmäinen luku: "))
        luku2 = int(input("Anna toinen luku: "))
        summa = luku1 + luku2
        print(luku1, " + ", luku2, " = ", summa)
    elif toimitus == "-":
        luku1 = int(input("Anna ensimmäinen luku: "))
        luku2 = int(input("Anna toinen luku: "))
        erotus = luku1 - luku2
        print(luku1, " - ", luku2, " = ", erotus)
    elif toimitus == "*":
        luku1 = int(input("Anna ensimmäinen luku: "))
        luku2 = int(input("Anna toinen luku: "))
        tulo = luku1 * luku2
        print(luku1, " * ", luku2, " = ", tulo)
    elif toimitus == "/":
        luku1 = int(input("Anna ensimmäinen luku: "))
        luku2 = int(input("Anna toinen luku: "))
        jako = luku1 / luku2
        print(luku1, " / ", luku2, " = ", jako)
    elif toimitus == "" or "/" or "*" or "-" or "+":
        break