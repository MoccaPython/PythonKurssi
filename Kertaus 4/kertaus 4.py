tarina = []
edellinen = ""
while True:
    sana = input("Anna sana lisättäväksi tarinaan: ")
    if sana != "loppu":


        if sana == edellinen:
            break
    else:
        break
    tarina.append(sana)
    edellinen = sana
for nimi in tarina:
    print(nimi, end=" ")



    #    print(tarina, end="")
     #   break