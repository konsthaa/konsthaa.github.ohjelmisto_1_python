import math
import random


# Tehtävä 1 Kirjoita ohjelma, joka kysyy nimesi ja sen jälkeen tervehtii sinua omalla nimelläsi.

kayttaja= input('Terve, mikä on nimesi: ')
print('Terve,  ' + kayttaja + '!')



# Tehtävä 2 Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.

ympyran_sade = float(input('Mikä on ympyrän säde?'))
ympyran_pinta_ala = math.pi * ympyran_sade ** 2
print(f'ympyran_pinta-ala on: {ympyran_pinta_ala:.2f}')



# Tehtävä 3 Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
          # Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
          # Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

suorakulmion_kanta = float(input('Mikä on suorakulmion kanta?'))
suorakulmion_korkeus = float(input('Mikä on suorakulmion korkeus?'))

suorakulmion_piiri = print(f'suorakulmion_piiri_on: {2 * suorakulmion_kanta + 2 * suorakulmion_korkeus:2f}')


# Tehtävä 4 Kirjoita ohjelma, joka kysyy kolme kokonaislukua.
        # Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

kokonaisluku1 = int(input('Mikä on ensimmäinen kokonaisluku?'))
kokonaisluku2 = int(input('Mikä on toinen kokonaisluku?'))
kokonaisluku3 = int(input('Mikä on kolmas kokonaisluku?'))

lukujen_summa = print(f'lukujen summa: {kokonaisluku1 + kokonaisluku2 + kokonaisluku3}')

lukujen_tulo = print(f'lukujen tulo: {kokonaisluku1 * kokonaisluku2 * kokonaisluku3: 2f}')

lukujen_keskiarvo = print(f'lukujen keskiarvo: {(kokonaisluku1 + kokonaisluku2 + kokonaisluku3)/3:2f}')



# Tehtävä 5 Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.

#           Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

# Yksi leiviskä on 20 naulaa.
# Yksi naula on 32 luotia.
# Yksi luoti on 13,3 grammaa.

#kysytään arvot keskiaikaisina mittoina

leiviskat = int(input('Anna leivisköjen määrä:'))
naulat = int(input('Anna naulojen määrä:'))
luodit = float(input('Anna luotien määrä:'))

# Muunnetaan kaikki saadut arvot grammoiksi

luodit = (leiviskat * 20 * 32) + (naulat * 32) + luodit
grammat = luodit * 13.3

# Muunnetaan grammat kilogrammoiksi

kilot = int(grammat // 1000)
kilojen_lisagrammat = grammat % 1000

# Kilogrammat ja grammat (lopulliset vastaukset):

print(f'Massa on {kilot} kiloa ja {kilojen_lisagrammat:.2f} grammaa.')



# Tehtävä 6 Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
        # kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
        # nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6

# kolminumeroinen koodi (0, 9):

num10=random.randint(0,9)
num11=random.randint(0,9)
num12=random.randint(0,9)

kolminumeroinen_koodi = str(num10) + str(num11) + str(num12)

print(f'Kolminumeroinen koodisi on: {kolminumeroinen_koodi}') #esim. 965


#nelinumeroinen koodi (1, 6)

num20=random.randint(1,6)
num21=random.randint(1,6)
num22=random.randint(1,6)
num23=random.randint(1,6)

nelinumeroinen_koodi = str(num20) + str(num21) + str(num22) + str(num23)

print(f'Nelinumeroinen koodisi on: {nelinumeroinen_koodi}') #esim. 3542











