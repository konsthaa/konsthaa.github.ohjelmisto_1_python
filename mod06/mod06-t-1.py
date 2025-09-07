# Tehtävä 1
# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def heita_noppaa():
    return random.randint(1, 6)

while True:
    tulos = heita_noppaa()
    print(tulos)
    if tulos == 6:
        break