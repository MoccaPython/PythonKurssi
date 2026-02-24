#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
#(käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
#Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin.
#käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.
kaupungit = []
print("Ohjelma pyytää viiden eri kaupungin nimen.")
#kaupungit.append(input("Anna kaupunki: "))
for kaupunki in range(5):
    kaupunki = input("Anna kaupunki: ")
 #   if kaupunki == "":
  #      break
    kaupungit.append(kaupunki)
#print(kaupungit)

for kaupunki in kaupungit:
    print(kaupunki)