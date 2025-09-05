# tehtävä 2
# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

tyhjamjono = []

while True:
    syote = input("Syötä luku (tyhjä merkkijono lopettaa): ")
    if syote == "":
        break
    try:
        luku = float(syote)
        tyhjamjono.append(luku)
    except ValueError:
        print("Syötä kelvollinen luku!")

if len(tyhjamjono) == 0:
    print("Ei syötettyjä lukuja.")
else:
    tyhjamjono.sort(reverse=True)
    print("Viisi suurinta lukua:")
    for i in range(min(5, len(tyhjamjono))):
        print(tyhjamjono[i])