# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

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


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissia(self, hissi_numero, kohde_kerros):
        if hissi_numero < 1 or hissi_numero > len(self.hissit):
            print(f"Virhe: Hissiä numero {hissi_numero} ei ole talossa!")
            return

        print(f"Ajetaan hissiä {hissi_numero} kerrokseen {kohde_kerros}...")
        self.hissit[hissi_numero - 1].siirry_kerrokseen(kohde_kerros)


# Pääohjelman testaus
if __name__ == "__main__":
    # Luodaan talo kerroksilla 1-10 ja jossa on kolme hissiä
    talo = Talo(1, 10, 3)

    print("Talo luotu 3 hissillä. Kaikki hissit aloittavat kerroksesta 1.")
    print()

    # Ajetaan hissiä 1 kerrokseen 5
    talo.aja_hissia(1, 5)
    print()

    # Ajetaan hissiä 2 kerrokseen 8
    talo.aja_hissia(2, 8)
    print()

    # Ajetaan hissiä 3 kerrokseen 3
    talo.aja_hissia(3, 3)
    print()

    # Ajetaan hissiä 1 takaisin kerrokseen 1
    talo.aja_hissia(1, 1)
    print()

    # Virheellinen hissi. esimerkiksi hissi nro. 4
    talo.aja_hissia(4, 5)