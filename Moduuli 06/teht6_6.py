#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
#Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
#Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
#kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
#Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math

def neliohinta(halkaisija, hinta):
    ala = math.pi*((halkaisija/2)/100)**2 # pizzan ala neliömetreissä
  #  print(ala)
    nh = hinta/ala #hinta per neliömetri
    return nh

pizza1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): ")) #pizzan 1 halkaisija
pizza1hinta= float(input("Anna ensimmäisen pizzan hinta: ")) #pizzan 1 hinta

pizza2 = float(input("Anna toisen pizzan halkaisija (cm): "))  #pizza 2 halkaisija
pizza2hinta= float(input("Anna toisen pizzan hinta: "))  # pizza2 hinta

pizza1nh = neliohinta(pizza1, pizza1hinta) #laskee neliöhinnat pizzoille
pizza2nh = neliohinta(pizza2, pizza2hinta)

#print(pizza1nh, pizza2nh)

print(f"Ensimmäisen pizzan neliöhinta on {pizza1nh:.2f} euroa ja toisen pizzan {pizza2nh:.2f} euroa.")

if (pizza1nh < pizza2nh):
    print("Ensimmäinen pizza antaa paremman vastineen rahalle")

else:
    print("Toinen pizza antaa paremman vastineen rahalle")


