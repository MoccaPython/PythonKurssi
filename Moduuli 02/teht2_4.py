#kolmen kokonaisluvun summa, tulo ja keskiarvo
Luku1_str = (input('Anna ensimmäinen luku:'))
Luku1 = float(Luku1_str)
Luku2_str = input('Anna toinen luku:')
Luku2 = float(Luku2_str)
Luku3_str = input('Anna kolmas luku:')
Luku3 = float(Luku3_str)
Summa = Luku1 + Luku2 + Luku3
Tulo = Luku1 * Luku2 * Luku3
Keskiarvo = Summa / 3
print ("Lukujen " +str(Luku1)+ ", " + str(Luku2) + " ja " + str(Luku3) +
       ".\nSumma: " + str(Summa) + "\nTulo: " + str(Tulo) + "\nKeskiarvo: " + str(Keskiarvo))
