# Tehtävä 2
# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def heita_noppaa(tahkoja):
    return random.randint(1, tahkoja)

max_silmaluku = int(input("Mikä on nopan maksimisilmäluku?"))
while True:
    tulos = heita_noppaa(max_silmaluku)
    print(tulos)
    if tulos == max_silmaluku:
        break