# tehtävä 1
# Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.
#from mod03.noppapeli import app_running
import random



#i = 1
#while i <= 1000:
    #if i % 3 == 0:
        #print(f"i={i}")
    #i += 1

# tehtävä 2
# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa.
# 1 tuuma = 2,54 cm

#tuumat = float(input("Anna tuumien määrä (negatiivinen luku lopettaa): "))
#while tuumat >= 0:
    #sentit = tuumat * 2.54
    #print(f"{tuumat} tuumaa = {sentit:.2f} cm")
    #tuumat = float(input("Anna tuumat (negatiivinen luku lopettaa): "))
#print("Ohjelma lopetettu.")



# tehtävä 3
# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

#numerot = []
#app_running = True
#while app_running:
    #luku = input("Anna luku (enter lopettaa): ")
    #if luku == "":
        #print("Error, tyhjä merkkijono")
        #app_running = False
    #numerot.append(luku)
#if numerot:
    #print(f"pienin luku {min(numerot)}:")
    #print(f"suurin luku {max(numerot)}:")
#else:
    #print("Loppu")


# tehtävä 4
# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

#numerot = random.randint(1,10) #arvotaan satunnainen numero (1-10).

#while True:
    #luku = int(input("Anna luku (1-10): "))   # pelaaja arvaa (1-10)

    #if luku > numerot:
        #print("Liian suuri arvaus!")
    #elif luku < numerot:
        print("Liian pieni arvaus!")
    else:
        print("Oikein!")
        break
#teht 6

# kaikkien pisteiden määrä N
#N = 10
# ympyrän sisään osuvien pisteiden lkm n
#n = 0
#i = 0
#while i < N:
    #i = i + 1
    # arvotaan satunnainen piste koordinaatistoon
    #x = random.uniform(-1, 1)
    #y = random.uniform(-1, 1)
    #print(f"Arvottu piste: {x}, {y}")
    # TODO: testaa, toteutuuko piste epäyhtälön x^2+y^2 < 1
    # jos ehtgo on totta, kasvata n-laskurin arvoa

#TODO: laske ja tulosta piin likiarvo käyttäen kaavaa: pi\approx4n/N etsi oikea kaava.
