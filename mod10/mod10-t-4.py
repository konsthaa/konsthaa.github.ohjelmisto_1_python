# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi,
# pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja,
# joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi.

# Luokassa on seuraavat metodit:

# tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet
# eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.

# tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
# kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän.
# Muussa tapauksessa palautetaan False.

# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
# Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia,
# jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
# Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen,
# kun kilpailu on päättynyt.


import random

class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.speed += change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0

    def drive(self, hours):
        self.distance += self.speed * hours


class Race:
    def __init__(self, name, distance_km, cars):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars  # auto-olioja

    def hour_passes(self):
        for car in self.cars:
            # Random nopeudenmuutos -10 ja +15 km/h välillä
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)  # Ajetaan tunti

    def print_status(self):
        print(f"\n{'Reg':<12} {'Max Speed':<14} {'Speed':<10} {'Distance (km)':<12}")
        print("-" * 50)
        for car in self.cars:
            print(f"{car.reg_number:<12} {car.max_speed:<14} {car.speed:<10} {car.distance:<12}")

    def race_over(self):
        for car in self.cars:
            if car.distance >= self.distance_km:
                return True
        return False


# Pääohjelma
if __name__ == "__main__":
    # Luodaan 10 autoa
    cars = []
    for i in range(1, 11):
        reg = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        cars.append(Car(reg, max_speed))

    # Create the race
    race = Race("Great Scrapyard Race", 8000, cars)

    print(f"Welcome to the race: {race.name}")
    print(f"Race distance: {race.distance_km} km")
    print("The race begins!\n")

    hour = 0
    while not race.race_over():
        race.hour_passes()
        hour += 1

        # Tulostetaan tilanne joka 10:nen tunnin välein
        if hour % 10 == 0:
            print(f"\n--- STATUS AFTER {hour} HOURS ---")
            race.print_status()

    # Lopputulema
    print(f"\n--- RACE FINISHED AFTER {hour} HOURS ---")
    race.print_status()

    # Voittaja
    winner = max(race.cars, key=lambda c: c.distance)
    print(f"\nWINNER: {winner.reg_number} – {winner.distance} km!")