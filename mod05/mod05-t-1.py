# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

import random

arpakuutiot = int(input("arpakuutioiden määrä: "))
arpakuution_numero = random.randint(1, 6)
silmalukujen_summa = arpakuutiot * arpakuution_numero

for arpakuution_numero in arpakuutiot:
    print(sum(silmalukujen_summa))
