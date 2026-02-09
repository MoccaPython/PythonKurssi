#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sex = input("Oletko biologisesti mies vai nainen? m/n ") #Sukupuoli


if sex == "m" or sex == "M":
    hemo = int(input("Anna hemoglobiini arvosi: "))  # hemoglobiini arvo
    if 134 <= hemo <= 195:
        print("Hieno homma, Hemmo!")
    elif 134 > hemo:
        print("Hemoglobiini alhainen! Syö rautaa tai mene vuoristoon!")
    elif sex == "m" or sex =="M" and 195 < hemo:
        print("Hemoglobiinisi on ylhäällä! Laskeudu merenpinnan tasolle")
elif sex == "n" or sex =="N":
    hemo = int(input("Anna hemoglobiini arvosi: "))  # hemoglobiini arvo
    if 117 <= hemo <= 175:
        print("Hieno homma, Leidi")
    elif sex == "n" or sex =="N" and hemo > 175:
        print("Hemoglobiinisi on ylhäällä! Laskeudu merenpinnan tasolle")
    elif sex == "n" or sex == "N" and 117 > hemo:
        print("Hemoglobiini alhainen! Syö rautaa tai mene vuoristoon!")

else:
    print("En tunnista sukupuoltasi!")