class Auto:
    def __init__(self, registernumber, topspeed):
        self.register_number = registernumber
        self.top_speed = topspeed
        self.speed = 0
        self.trip = 0

# Pääohjelma
auto = Auto("ABC-123", 142)
print("Rekisteritunnus:", auto.register_number)
print("Huippunopeus:", auto.top_speed, "km/h")
print("Tämänhetkinen nopeus:", auto.speed, "km/h")
print("Kuljettu matka:", auto.trip, "km")

