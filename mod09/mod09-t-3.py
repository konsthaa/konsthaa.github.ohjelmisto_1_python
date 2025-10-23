#mod 09 t 3

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
car = Car("CPR-865", 142)
print("Register Number:", car.registernumber)
print("Top Speed:", car.top_speed, "km/h")
print("Speed", car.speed, "km/h")
print("Trip:", car.trip, "km")

# Nopeuden muutokset
car.accelerate(30)
print("Speed after +30 km/h acceleration:", car.speed, "km/h")
car.accelerate(70)
print("Speed after +70 km/h acceleration:", car.speed, "km/h")
car.accelerate(50)
print("Speed after +50 km/h acceleration:", car.speed, "km/h")

# Hätäjarrutus
car.accelerate(-200)
print("Speed after (-200 km/h) emergency brake:", car.speed, "km/h")

# Esim. kulje-metodi:
car.accelerate(60)  # kiihdytetään nopeuteen 60 km/h
car.go(1.5)  # Ajetaan 1.5 tuntia
print("Trip after 1.5 hour drive (speed 60 km/h):", car.trip, "km")