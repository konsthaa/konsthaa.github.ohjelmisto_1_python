import random

#noppaesim. 3-materiaalista. (muokattu)
pelikerrat = 0
heittojen_lkm = 0
app_running = True
while app_running:
    noppa1 = noppa2 = heitot = 0
    while noppa1 != 6 or noppa2 != 6:
        noppa1 = random.randint(1, 6)
        noppa2 = random.randint(1, 6)
        heitot = heitot + 1
    print(f"Kahteen kutoseen tarvittiin {heitot:d} heittoa.")
    pelikerrat = pelikerrat + 1
    heittojen_lkm = heittojen_lkm + heitot
    komento = input("Pelataanko uudestaan (k/e)? ")
    if komento != "k":
        app_running = False
print(f"Kaksi kutosta saatiin keskimäärin {heittojen_lkm/pelikerrat} heitolla.")