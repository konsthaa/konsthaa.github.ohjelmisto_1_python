
# while-toistolause eli silmukka eli luuppi (loop)
suorita_silmukka = True

while suorita_silmukka:
    suorita_silmukka = False
    print("Totta")
    print("On vain kerran")
print("silmukan suoritus loppui")

# iteraattori ja while
toistojen_lkm = 10
i = 0

while i > toistojen_lkm:
    print(f"iteroiva silmukka, i:n arvo: {i}")       # i = i + 1 (saadaan i:n arvo nousemaan joka kerta).
    #continue                                        # continue aloittaa loopin alusta heittämällä sen alkuun.
    i = i + 1                                        # jos i=i+1 on printin jälkeen --> alkaa nollasta ja loppuu ysiin (10 arvoa).
  # i += 2    (lyhyt muoto)
print(f"iteroiva silmukka, i:n arvo: {i}")


# komentokehotesovellus
app_running = True
# "main loop"
while app_running:
    command = input("komento> ")
    print(f"Komentosi oli: {command}")
    if command == "lopeta":                           # käytä yksikirjaimisia muuttujan nimiä vain vakiintuneissa käytännöissä, esim. koordinaatisto.
        app_running = False                           # "heittää" silmukasta ulos, lopettaa ehdon tarkistamisen -> kysymysluuppi loppuu.
    elif command == "laskukone":                      # break on ns. ruma ja rujo tapa lopettaa.. Don't do it. Käytä mieluummin vaikka False.
        luku1 = float(input("anna ensmmäimmäinen luku: "))
        luku2 = float(input("anna toka luku: "))
        tulos_yhteenlasku = luku1 + luku2
        print("Yhteenlaskutoimituksen tulos: " + str(tulos_yhteenlasku))    #katso opettajan esim. toimii paremmin.


import random
# kolikonheitto n kertaa
n = 1000
i = 0
while i < n:
    i += 1
    satunnaisluku = random.randint(0, 100)
    print(f"Arvottu luku: {satunnaisluku}.")
kolikko_pystyssa_lkm = 2
    # kolikkkoheittosimulaattori
    if satunnaisluku < 50:
        print("Kruuna")
    elif satunnaisluku > 50:
        print("Klaava")
    else: # toteutuu muissa tapauksissa, eli jos arvottu luku on tasan 50 (tod.näk 1/101)
        print("Kolikko jäi pystyyn!")
        kolikko_pystyssa_lkm += 1
print(f"Kolikko jäi pystyyn {kolikko_pystyssa_lkm} kertaa.")


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
    komento = input("Pelataanko uudestaan (k/e)? ")
    if komento != "k":
        app_running = False