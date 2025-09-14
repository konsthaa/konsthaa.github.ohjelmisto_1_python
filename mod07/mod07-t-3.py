# tehtävä 3
# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä,
#  haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
# (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

lkentta = {}

while True:
    toiminto = input("Valitse (syötä/uusi/haku/lopeta): ")

    if toiminto == "lopeta":
        break
    elif toiminto == "uusi":
        icao = input("Anna ICAO-koodi: ").upper()
        nimi = input("Anna kentän nimi: ")
        lkentta[icao] = nimi
        print("Kenttä lisätty!")
    elif toiminto == "haku":
        icao = input("Anna ICAO-koodi: ").upper()
        if icao in lkentta:
            print(f"Kentän nimi: {lkentta[icao]}")
        else:
            print("Kenttää ei löydy.")
    else:
        print("Tuntematon toiminto. Käytä syöttöä, hakua tai lopeta.")
