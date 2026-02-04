#suorakulmion alan ja piirin laskenta

Kanta_str = input("Anna Suorkulmion kanta: ")
Kanta = float(Kanta_str)
Korkeus_str = input("Anna Suorakulmion korkeus: ")
Korkeus = float(Korkeus_str)
Area = Kanta * Korkeus
Circuit = Kanta * 2 + Korkeus * 2
print("Suorakulmion ala on " + str(Area) + " ja piiri on " + str(Circuit))
