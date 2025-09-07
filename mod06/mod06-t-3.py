# Tehtävä 3
# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
# ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.


def gallona_litroiksi(gallonat):
    return gallonat * 3.785

while True:
    gallona = float(input("Syötä bensiinin määrä gallonoina (negatiivinen luku lopettaa): "))
    if gallona < 0:
        break
    litrat = gallona_litroiksi(gallona)
    print(f"{gallona} gallonaa on {litrat} litraa")