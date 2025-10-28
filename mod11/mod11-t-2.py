# Auto-yliluokka
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0  # nykyinen nopeus
        self.matka = 0   # matkamittari

    def aja(self, tunnit):
        """Ajaa annetun ajan tunneissa nykyisellä nopeudella."""
        self.matka += self.nopeus * tunnit


# Sähköauto-aliluokka
class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti_kwh):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti_kwh


# Polttomoottoriauto-aliluokka
class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki_litraa):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki_litraa


# Pääohjelma
def main():
    # Luodaan autot
    sahkoauto = Sähköauto("ABC-15", 180, 52.5)
    bensaauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    # Asetetaan nopeudet
    sahkoauto.nopeus = 120  # km/h
    bensaauto.nopeus = 140  # km/h

    # Ajetaan 3 tuntia
    sahkoauto.aja(3)
    bensaauto.aja(3)

    # Tulostetaan matkamittarilukemat
    print(f"Sähköauto {sahkoauto.rekisteritunnus}:")
    print(f"  Matka: {sahkoauto.matka} km")

    print(f"Polttomoottoriauto {bensaauto.rekisteritunnus}:")
    print(f"  Matka: {bensaauto.matka} km")


if __name__ == "__main__":
    main()