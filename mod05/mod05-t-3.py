# tehtävä 3
# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

def on_alkuluku(luku):
    if luku < 2:
        return False
    for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            return False
    return True

try:
    luku = int(input("Syötä kokonaisluku: "))
    if on_alkuluku(luku):
        print(f"{luku} on alkuluku.")
    else:
        print(f"{luku} ei ole alkuluku.")
except ValueError:
    print("Syötä kokonaisluku!")