#luku = 1
#while luku<1000:
 #   if luku % 3 == 0:
  #      print (luku)
   # luku = luku + 1

# Tänne ei koskaan päästä:
#print("Valmista tuli.")

luku = int(input("Anna luku? "))

if luku < 0:
    print("luvun itseisarvo on", luku*-1)
else:
    print("luvun itseisarvo on", luku)

