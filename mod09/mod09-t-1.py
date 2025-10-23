# Mod09 tehtävät, 1

class Car:
    def __init__(self, registernumber, topspeed):
        self.register_number = registernumber
        self.top_speed = topspeed
        self.speed = 0
        self.trip = 0

# Pääohjelma
auto = Car("ABC-123", 142)
print("Register Number:", auto.register_number)
print("Top Speed:", auto.top_speed, "km/h")
print("Speed:", auto.speed, "km/h")
print("Trip:", auto.trip, "km")