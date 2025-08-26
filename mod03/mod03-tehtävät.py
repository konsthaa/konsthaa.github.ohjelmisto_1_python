import random
from random import randint
# python ohjelmistoteema 3 tehtävät:

# tehtävä 1:
    # Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
    # Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
    # montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
    # Kuha on alamittainen, jos sen pituus on alle 37 cm.

#kysytään ensin kuhan mitta.

kuhan_mitta = float(input("Anna kuhan mitta: "))
if kuhan_mitta<37:
    print("Alamittainen! Heitä takaisin!")
    print(f'{37-kuhan_mitta} cm vajaa täysimittainen ')

else:
    print("Täysimittainen! Vie kotiisi!")
    print(f'{kuhan_mitta-37} cm yli vaaditun mitan ')




# tehtävä 2:
# Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C)
# ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
# Tehtävässä on käytettävä if/elif/else-toistorakennetta.

# LUX on parvekkeellinen hytti yläkannella.
# A on ikkunallinen hytti autokannen yläpuolella.
# B on ikkunaton hytti autokannen yläpuolella.
# C on ikkunaton hytti autokannen alapuolella.
# Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.

hyttiluokka = input("Hyttiluokka: ")
if hyttiluokka == "LUX" :
    print("Lux on parvelleellinen hytti yläkannella.")
elif hyttiluokka == "A" :
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B" :
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C" :
    print("C on ikkunaton hytti autokannen alapuolella.")

else:
    print("Virheellinen hyttiluokka!")


# Tehtävä 3

# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

Sukupuoli = input("Sukupuoli: ")
Hemoglobiiniarvo = float(input("Hemoglobiiniarvo (g/l): "))
if Sukupuoli == "Nainen" and Hemoglobiiniarvo<117:
    print("Alhainen hemoglobiini!")
if Sukupuoli == "Nainen" and Hemoglobiiniarvo>117<175:
    print("Normaali hemoglobiini!")
if Sukupuoli == "Nainen" and Hemoglobiiniarvo>175:
    print("Korkea hemoglobiini!")

if Sukupuoli == "Mies" and Hemoglobiiniarvo<134:
    print("Alhainen hemoglobiini!")
if Sukupuoli == "Mies" and Hemoglobiiniarvo>134<195:
    print("Normaali hemoglobiini!")
if Sukupuoli == "Mies" and Hemoglobiiniarvo>195:
    print("Korkea hemoglobiini!")

#Tehtävä 4:
#Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
#Vuosi on karkausvuosi, jos se on jaollinen neljällä.
#Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

Vuosiluku = int(input("Vuosiluku: "))


if Vuosiluku % 4 == 0:
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausivuosi")

