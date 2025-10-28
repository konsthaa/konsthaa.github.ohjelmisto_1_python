# Auto-yläluokka
class Car:
    def __init__(self, reg_number, top_speed):
        self.reg_number = reg_number
        self.top_speed = top_speed
        self.speed = 0  # nopeus nyt
        self.trip = 0   # matkan pituutta mittaava mittari

    def drive(self, hours):
        # Ajetaan annetun ajan verran tunneissa
        self.trip += self.speed * hours


# Sähköauto-alaluokka
class Electric(Car):
    def __init__(self, reg_number, top_speed, battery_capacity_kwh):
        super().__init__(reg_number, top_speed)
        self.akkukapasiteetti = battery_capacity_kwh


# Polttomoottoriauto-alaluokka
class Combustion(Car):
    def __init__(self, reg_number, top_speed, gastank_litres):
        super().__init__(reg_number, top_speed)
        self.gastank = gastank_litres


# Pääohjelma
def main():
    # Luodaan autot
    electriccar = Electric("ABC-15", 180, 52.5)
    combustioncar = Combustion("ACD-123", 165, 32.3)

    # nopeudet
    electriccar.speed = 120  # km/h
    combustioncar.speed = 140  # km/h

    # Ajetaan 3 tuntia
    electriccar.drive(3)
    combustioncar.drive(3)

    # Tulostetaan matkamittarilukemat
    print(f"Sähköauto {electriccar.reg_number}:")
    print(f"  Matka: {electriccar.trip} km")

    print(f"Polttomoottoriauto {combustioncar.reg_number}:")
    print(f"  Matka: {combustioncar.trip} km")


if __name__ == "__main__":
    main()