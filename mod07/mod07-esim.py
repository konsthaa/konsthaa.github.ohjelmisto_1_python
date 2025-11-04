import random

# mod07 tuntiesimerkit:

#monikko, joukko ja sanakirja

# MONIKKO:

# monikko, eli (tuple) on "kuin lista, jota ei voi muokata"

lista = [1, 2, 3, 4, 5, 6]
print(lista)

monikko = (1, 2, 3, 4, 5, 6)
print(monikko)

monikko2 = 1, 2, 3, 4, 5, 6 # toimii myös ilman kaarisulkeita, ohjelma lisää ne automaattisesti.
print(monikko2)

#monikko voi sisältää erilaista tietoa
monikko3 = (1, 2, "Konsta", (3, 4), 88)
print(monikko3)

# luetaan listan eka alkio:
print(lista[0])

#printataan monikon eka alkio:
print(monikko[0])

# Toisin kuiin lista, monikko on kuitenkin muuttumaton:
# siihen ei voi lisätä alkioita eikä siitä voi poistaa alkoita monikon luonnin jälkeen.

#muokataan listaa:
lista[0] = 0
print("muokattu lista", lista)

#lisätään listaan:
lista.append(7)

# monikko[0] = 0, tämä ei toimi monikolla, koska monikko on muokkaamaton.

# monikosta voi hakea indeksin avulla alkion arvon
luku = monikko[3]
print("Hain tämän monikosta:", luku)


#Monikkoa on tarkoituksenmukaista käyttää tuilanteissa, joissa alkioden jono on luonteeltaan staattinen: tiedetään, että
#muutoksille ei ole tarvetta ohjelman suorituksen aikana.


'''
viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
viikonpäivä = viikonpäivät[järjestysnumero-1]
print (f"{järjestysnumero}. viikonpäivä on {viikonpäivä}.")
'''

# Monikon läpikäynti kuten listan:
sanat = ("eka", "toka", "kolmas", "neljäs", "viides")

for sana in sanat:
    print(sana)
    if sana == "kolmas":
        print("Sana KOLMAS löytyi!!!")

if "viides" in sanat:
    print("Sana VIIDES löytyi!!!")


# Moniko arvojen purku muuttujiin

hedelmät = ("Lime", "Sitruuna", "Ananas")
(eka, toka, kolmas) = hedelmät
# (eka, toka, kolmas) = ("Lime", "Sitruuna", "Ananas")   <-- toimii samalla tavalla kuin ylempi.
print (f"Hedelmiä ovat {eka}, {toka} ja {kolmas}.")
print("Monikko purettu muuttujiin, tässä eka:", eka)

# Monikon voi antaa funktiolle parametrina

def tulosta_monikko(hedelmät):
    for h in hedelmät:
        print(h)

tulosta_monikko(hedelmät)

# Monikko funktion paluuarvona

def heitä():
    eka = random.randint(1, 6)
    toka = random.randint(1, 6)
    print(f"nopista tuli: {eka} ja {toka}")
heitä()


# Yksinkertaistetaan random

def heitä2():
    # tässä luodaan tuple (monikko), joka puretaan muuttujiin:
    # eka, toka = random.randint(1, 6), random.randint(1, 6)
    eka, toka = random.randint(1, 6), random.randint(1, 6)
    print(f"nopista tuli: {eka} ja {toka}")
heitä2()

# Monikko myös paluuarvona

def heitä3():
    eka, toka = random.randint(1, 6), random.randint(1, 6)
    return eka, toka
noppa1, noppa2 = heitä3()
print("Funktiosta heitä3 palautui arvot:", noppa1, noppa2)

print("-----------------------------------------------------")
print("JOUKKO\n")

# Joukko eli set {}

# Joukko (set) on järjestämätön tietorakenne, eli sen alkiot voivat olla missä tahansa järjestyksessä
# alkioihin ei voi myöskään viitata indeksillä.
# toisin kuin listassa tai monikossa, sama alkio voi esiintyä joukossa vain kertaalleen.



# joukko merkataan aaltosulkeilla
joukko = {1,2,3,4,5,6}
print(joukko)

llista = [1,2,3,4,5,6,6,]
monikko = (1,2,3,4,5,6,6)
print(f"Numero 6 EI voi esiintyä joukossa useasti")
jjoukko = {1,2,3,4,5,6,6}
print(jjoukko)

#yllä oleva ei sinsänsä tuota virhettä, kuten ei add-metodi
jjoukko.add(6)  # tämä ei aiheuta virhettä, mutta ei lisää uuttaa numeroa 6.
jjoukko.add(7)  # toimii, koska lisättävä numero ei ole alkuperäisessä jjoukossa.
print(jjoukko)
jjoukko.remove(1)
print(jjoukko)

pelit = {"Monopoli", "Shakki", "Cluedo", "Muuttuva labyrintti", "Hotel"}
print(pelit)
pelit.add("Cluedo")
print(pelit)

# alkioiden iteroiminen läpi for/in rakenteella
# indeksiin ei voi tosiaan tässä viitata

for p in pelit:
    print(p)

if "Cluedo" in pelit:
    print(f"Cluedo löytyy pelit-listasta :D ")


print("---------------------------")

# tyhjän listan luominen
autolista = []
autolista.append("Audi")
print(autolista)
print(type(autolista))


# tyhjä joukko luodaan edellä esitetystä poiketen set-funktion avulla
autojoukko = set()
autojoukko.add("Mersu")
print(autojoukko)
print(type(autojoukko))

# jos yrität luoda tyhjää joukkoa {} -sulkeilla, tästä tuleekin sanakirja
autosanakirja = {}
print(type(autosanakirja))

print("SANAKIRJA\n")

# Sanakirja (dictionary) on Pythonin käytetyimpiä tietorakenteita.
# Sanakirjaan voidaan tallentaa avain-arvopareja.

# kun sanakirja alustetaan, annetaan avain-arvopari seuraavasti: AVAIN : ARVO
# peräkkäiset avain-arvoparit erotellaan pilkulla

oppilaat = {"Aapeli": 25,          #voidaan luettavuuden takia laittaa useammalle riville, muista {} loppuun.
            "Bertta": 56,
            "Cecilia": 32,
            "Daniel": 23,
            "Emma": 25}
print(oppilaat)

# mitä ovat tietueet (items)
print(oppilaat.items())


# mitä ovat avaimet (keys) sanakirjassa
print(oppilaat.keys())

# mitä ovat arvot (values) sanakirjassa
print(oppilaat.values())


# käydään läpi sanakirja nyt for / in rakenteella
# kierrosmuuttuja eli tässä tapauksessa o saa arvokseen kunkin sanakirjassa esiintyvän AVAIMEN (key).
for o in oppilaat:
    print(o)

avain = "Aapeli"
oppilaat[avain]
print("Etsitään avaimella Aapeli hänen ikä", oppilaat[avain])
#print(oppilaat["Aapeli"]) toimii myös nimeä etsimällä.
print(f"Danielin ikä: {oppilaat["Daniel"]}")

for o in oppilaat:
    print(f"Oppilaan nimi on {o} ja IKÄ on {oppilaat[o]}")

# hae haluttu ikä if/in rakennetta käyttäen
# pyydä käyttäjältä nimi ja haetaan se sanakirjasta
nimi = input("Anna nimi, jota etsin sanakirjasta: ")
if nimi in oppilaat:
    ikä = oppilaat[nimi] # haetaan avaimella arvo
    print(f"Nimi {nimi} löytyi!!!")
    print(f"Hänen ikä on {ikä}")
else:
    print(f"Nimeä {nimi} ei löydy sanakirjasta!")

yhteystiedot = {
    "Aapeli": {
        "puh" : "050824712",
        "Osoite" : "Allinkuja 2"},#voidaan luettavuuden takia laittaa useammalle riville, muista {} loppuun.

        "Bertta": {
            "puh" : "050432556",
            "Osoite" : "Linnuntie 5"},

        "Cecilia": {
            "puh" : "050432568",
            "Osoite" : "Rapakuja 2"},

        "Daniel": {
            "puh" : "050432579",
            "Osoite" : "Tullihaukankuja 8"}}

print(f"Aapelin puhelinnumero: {yhteystiedot["Aapeli"][puh]}")
