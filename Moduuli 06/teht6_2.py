#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
#Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
#Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
#joka kysytään käyttäjältä ohjelman suorituksen alussa.
import random

def noppa(silmat):
    silmaluku = random.randint(1,silmat)
#    print ("sa", silmaluku)
    return silmaluku

heitot = 0

noppa1 = int(input("Anna nopan silmien määrä: "))

while True:
    i_str = noppa(noppa1)
    i = int(i_str)

    if i != noppa1:
        heitot += 1
        print(i)
    else:
        print(i)
        heitot += 1
        print("Heittoja tarvittin", heitot, ", jotta tuli ", noppa1)
        break