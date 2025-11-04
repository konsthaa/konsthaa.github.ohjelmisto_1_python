import random
from random import randint

# valintarakenne-esimerkkejä (mod3)


#onko_totta = False
#onko_totta= 3 == 3      # yksittäinen "=" on aina sijoitusoperaattori. Käytä siis "==".


satunnaisluku = random.randint(0,100)
#print(f"Arvottu luku: {satunnaisluku}")

# kolikkkoheittosimulaattori
if satunnaisluku < 50:
    print("Kruuna")
    print("Kuuluu samaan koodilohkoon")
elif satunnaisluku > 50:
    print("Klaava")
else: # toteutuu muissa tapauksissa, eli jos arvottu luku on tasan 50 (tod.näk 1/101)
    print("Kolikko jäi pystyyn!")

print("Suoritus if-lauseen jälkeen jatkuu tästä.")

# dummy-kirjautuminen

tunnus = "konstah"
oikea_salasana = "salakala"
input_tunnus = input("Käyttäjätunnus: ")
input_salasana = input("Anna salasana: ")

if input_salasana == oikea_salasana and input_tunnus == tunnus:
        print("Tervetuloa!")
        kehote = input("Mitäs haluat tehdä? ")
        if kehote == "Tervehtiä":
            print("No morjens!")
        else:
            print("En ymmärtänyt kehotetta")
else:
    print("Väärä salasana")


print("Ohjelma suljettu. Heippa!")
