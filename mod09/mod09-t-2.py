# mod09 t, 2

class Car:
    def __init__(self, registernumber, topspeed):
        self.register_number = registernumber
        self.top_speed = topspeed
        self.speed = 0
        self.trip = 0

    def accelerate(self, speed_change):
        self.trip += speed_change
        if self.trip > self.top_speed:
            self.trip = self.top_speed
        elif self.speed < 0:
            self.speed = 0


# Pääohjelma
auto = Car("ABC-123", 142)
print("Register Number:", auto.register_number)
print("Top Speed:", auto.top_speed, "km/h")
print("Present Speed:", auto.speed, "km/h")
print("Trip travelled:", auto.trip, "km")

# Nopeuden muutokset
auto.accelerate(30)
print("Speed after +30 km/h acceleration:", auto.speed, "km/h")
auto.accelerate(70)
print("Speed after +70 km/h acceleration:", auto.speed, "km/h")
auto.accelerate(50)
print("Speed after +50 km/h acceleration:", auto.speed, "km/h")

# Hätäjarrutus
auto.accelerate(-200)
print("Speed after emergency brake:", auto.speed, "km/h")