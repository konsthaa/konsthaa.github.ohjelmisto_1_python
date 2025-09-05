# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

import random

arpakuutiot = input("arpakuutioiden määrä: ")
summa = 0
for i in range(int(arpakuutiot)):
    heitto = random.randint(1,6)
    print(f"arpakuutio {i + 1}: {heitto}")
    summa += heitto
print(f"silmälukujen summa: {summa}")
