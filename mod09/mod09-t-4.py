# mod09 t, 4
import random

class Car:
    def __init__(self, registernumber, topspeed):
        self.registernumber = registernumber
        self.top_speed = topspeed
        self.speed = 0
        self.trip = 0

    def accelerate(self, speed_change):
        self.speed += speed_change
        if self.speed > self.top_speed:
            self.speed = self.top_speed
        elif self.speed < 0:
            self.speed = 0

    def go(self, hours):
        self.trip += self.speed * hours


# Pääohjelma
cars = []
for i in range(1, 11):
    top_speed = random.randint(100, 200)
    car = Car(f"CPR-{i}", top_speed)
    cars.append(car)

# Kilpailu
while all(car.trip < 10000 for car in cars):
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.go(1)

# Tulostetaan tulokset taulukkona
print("\n{:<10} {:<15} {:<15} {:<15}".format("Register", "Top Speed", "Speed", "Trip"))
print("-" * 55)
for car in cars:
    print("{:<10} {:<15} {:<15} {:<15}".format(
        car.registernumber,
        f"{car.top_speed} km/h",
        f"{car.speed} km/h",
        f"{car.trip} km"
    ))