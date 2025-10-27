#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia
# niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat,
# missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään
# haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.nykyinen = alin_kerros  # Hissi aloittaa aina alimmasta kerroksesta

    def kerros_ylos(self):
        if self.nykyinen < self.ylin:
            self.nykyinen += 1
        print(f"Hissi on nyt kerroksessa {self.nykyinen}")
        return self.nykyinen

    def kerros_alas(self):
        if self.nykyinen > self.alin:
            self.nykyinen -= 1
        print(f"Hissi on nyt kerroksessa {self.nykyinen}")
        return self.nykyinen

    def siirry_kerrokseen(self, kohde):
        if kohde < self.alin or kohde > self.ylin:
            print(f"Virhe: Kerrosta {kohde} ei ole tässä hississä!")
            return

        print(f"Siirrytään kerrokseen {kohde}...")

        if kohde > self.nykyinen:
            while self.nykyinen < kohde:
                self.kerros_ylos()
        elif kohde < self.nykyinen:
            while self.nykyinen > kohde:
                self.kerros_alas()
        else:
            print(f"Hissi on jo kerroksessa {kohde}")


# PÄÄOHJELMA - TESTAUS
if __name__ == "__main__":
    # Luodaan hissi kerroksista 1-10
    h = Hissi(1, 10)

    print("Hissi luotu. Aloituskerros:", h.nykyinen)
    print()

    # Siirrytään kerrokseen 6
    h.siirry_kerrokseen(6)
    print()

    # Palataan takaisin alimpaan kerrokseen (1)
    h.siirry_kerrokseen(1)