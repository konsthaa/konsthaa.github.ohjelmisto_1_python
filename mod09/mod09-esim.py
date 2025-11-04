# Katso pycharm opettajan esimerkki tarvittaessa, löytyy githubista.

# KONSEPTI: Luokka, Olio, Alustaja;

# Luokka (class):

class Koira:     # konstruktori (alustaja) -metodi   **OPETTELE LUOKAN MÄÄRITTELY**
    count = 0
    def __init__(self, name, weight):
        print(f"uusi koiraolio {name} luotu.")   # nimi tallennetaan olion ominaisuudeksi self-viittauksen avulla.
        self.name = name
        self.weight = weight
        Koira.count = Koira.count + 1

    def hauku(self, toWhom, times):               # metodi (luokan toiminto (verrattavissa funktioon))
        print(f"{self.name} haukkuu {toWhom}")
        for i in range(times):
            if self.weight < 10:
                print("WufWuf!")
            else:
                print("Hau Hau!")


# Olio (object):
koira1 = Koira("Rekku", 4) #olion nimi (name) on Rekku ja paino (weight) 4 kg

# muuttujat, jotta päästään olioon käsiksi.

koira2 = Koira("Ruffe", 28) # --=--

koira1.hauku("Matille", 2) #olion nimi (name) on Matille ja kerrat (times), jota haukutaan 2

koira2.hauku("Jussille", 5) # --=--
#koira3 = koira1

koira1.name = "Rekku"
print(koira2.name)
koira2.name = "Beethoven"
#print(koira1.name)
#print(koira2.name)
#print(koira3.name)


