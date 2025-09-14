# Tehtävä 2
# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin "uusi nimi" tai "aiemmin syötetty" nimi sen mukaan,
# syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
# Käytä joukkotietorakennetta nimien tallentamiseen.

nimi_joukko = set()
while True:
    nimi = input("Anna nimi (tyhjä lopettaa): ")
    if nimi == "":
        break
    if nimi in nimi_joukko:
        print("Aiemmin syötetty")
    else:
        print("Uusi nimi")
        nimi_joukko.add(nimi)


    print("Syötetyt nimet:")
    for nimi in nimi_joukko:
        print(nimi)