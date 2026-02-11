#luku = 1
#while luku<1000:
 #   if luku % 3 == 0:
  #      print (luku)
   # luku = luku + 1

# Tänne ei koskaan päästä:
#print("Valmista tuli.")

komento = input ("Anna komento: ")
while komento!="lopeta":
    if komento=="MAYDAY":
        break
    print ("Suoritan toiminnon: " + komento)
    komento = input("Anna komento: ")
print ("Toiminnot lopetettu.")