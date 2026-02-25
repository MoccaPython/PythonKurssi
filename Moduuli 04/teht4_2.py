#Muunnetaan tuumat senteiksi!
inch = input("Anna tuumamäärä: ")

tuuma = float(inch)

while (tuuma >= 0):
    #if tuuma >= 0:
        print(tuuma * 2.54)
        tuuma = float(input("Anna tuumamäärä: "))
else:
    print("Ohjelma lopetettu")