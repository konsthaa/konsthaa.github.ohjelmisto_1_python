# Tehtävä 4
# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def laske_summa(luvut):
    return sum(luvut)

# Testaus
testilista = [1, 2, 3, 4, 5]
tulos = laske_summa(testilista)
print(f"Listan summa on: {tulos}")
