# Listarakenne ja läpinäkyvä toistorakenne (for)

# https://github.com/vesavvo/Python_Ohjelmistoteema/blob/main/05_Listarakenne_ja_for-toistorakenne.md?plain=1

nimi = 'Konsta'
nimi2 = 'Allu'
num1 = 45
num2 = 56

print(f"Hei {nimi} ikäsi on {num1}")

#tyhjä lista
lista = []

# lista voi sisältää muuttujia, numeroita, merkkojonoja jne.
nimet = ["Anna", "Liisa", nimi, nimi2, "Toni", 78, 64]
print(nimet)

# lista voi sisältää toisia listoja
ikälista = [45, 67, 34, [98, 4, 17]]
print(ikälista)

lempinumerot = [67, 90, 64, 36, 23, 21, 10]

print(len(ikälista))
print(len(lempinumerot))


#alkioon viitataan indenksinumerolla, alkaen numerosta 0 (alkio on listan jäsen).
#
print(f"Hei {nimet[0]} ja terve myös {nimet[4]}")

# voidaan myös printata listasta listan sisältä  (3 listan neljäs alkio, 1. alkion 3 sisältä):
print(f"{ikälista[3][1]}")

print("------------------")
# tapoja viitata listan alkoihin:

nimet2 = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary", "Anna", "Ulla", "Pasi"]
print(nimet2[3])  # Olga
print(nimet2[1])  # Ahmed
print(nimet2[1:5]) # alkupiste mukaanlukien ja indeksiin 3 päättyen (päätepiste pois lukien).
print(nimet2[-1])  #tokavika
print(nimet2[2:]) #toisesta eteenpäin
print(nimet2[1:-1]) #ahmedista ullaan
print(nimet2[1:-1:2])
print("-----------------")


# uusi_lista = vanha_lista[alku:loppu:askel]
uusi_lista = nimet2[2:4]
print(nimet2)
print(uusi_lista)


print("------------------------")
# lista jossa 5 kaupunkia
# tulosta niistä kolme ensimmäistä ja viimeinen.

kaupunkilista = ["Helsinki", "Tampere", "Turku", "Kouvola", "Lahti"]

print(kaupunkilista[:3])
print(kaupunkilista[-1])

# Viittaus listan ulkopuolelle aiheuttaa virheen!!!:
# print(kaupunkilista[7])



kaupunkilista.append("Uusi kaupunki")
print(kaupunkilista)
# kaupungit.remove("Iisalmi")  -> Virhe, koska kaupunkia ei löydy.

if "Tampere" in kaupunkilista:
    print(f"Tampere löytyi ja poistetaan listasta!")
    # poistetaan kaupunki
    kaupunkilista.remove("Tampere")
    print(kaupunkilista)


#lisätään Tampere ensimmäiseksi
kaupunkilista.insert(4, "Tampere")
print(kaupunkilista)

# Tutkitaan monesko indeksi:
monesko = kaupunkilista.index("Tampere")
print(monesko)  # --> Tampere on neljäs.

#Voidaan myös lisätä indeksejä jo olemassa olevaan listaan:

lisää_kaupunkeja = ["Sodankylä", "Sipoo", "Kotka"]
kaupunkilista.extend(lisää_kaupunkeja)
print(kaupunkilista)

# Muokataan olemassa olevaa alkiota indeksin avulla
kaupunkilista[7] = "Sipöö"
print(kaupunkilista)

# Voidaan myös lajitella:
hedelmiä = ["appelsiini", "Appelsiini", "Banaani", "Greippi", ]
numerolista = [1300, 2400, 600, 3]

hedelmiä.sort()
print(hedelmiä)

numerolista.sort()   #pienimmästä suurimpaan
print(numerolista)

numerolista.sort(reverse=True)     # suurimmasta pienimpään (väärinpäin)
print(numerolista)


# listarakenteita voidaan tutkia (esim. muuttujatyyppi):
tottavaiei = True
tottavaiei = "Totta"
print(type(tottavaiei))  # kertoo tyypin 'class'

viikonpaivat = ["Maanantai", "Tiistai"]
print(viikonpaivat)

print("-----------------------------")
print("muutamia hyödyllisiä funktioita tulevaisuutta varten")
print("--------------------------------------")

# listoille toimii mm. tämänlaiset funktiot
# len, sum, min, max, count

luvut = [2,4,6,5,2,7,3,2,3,2,7]

print(len(luvut))            #pituus
print(sum(luvut))            #summa
print(min(luvut))            #minimiarvo
print(max(luvut))            #maksimiarvo
print(luvut.count(2))        #kuinka monta lukua 2 listassa on

print("----------------")
print("Miten käydään lista läpi iteroimalla")
print("----------------")


luvut [2]

i = 0
while i < len(luvut):
    #print(i)
    print(luvut[i])
    # i = i + 1
    i += 1


print("----------------")
# käydään lista läpi alkio alkiolta

for luku in luvut:
    print (luku)

print("----------------")

for kirjain in "abcdfg":
    print(kirjain)

print("----------------")

for alkio in [1,2,3,4,5,6]:
    print(alkio)

print("----------------")


# tässä tapauksessa kaupunki on kierrosmuuttuja
for kaupunki in kaupunkilista:
    print(kaupunki)

print("-----------------")

for numero in range(5):
    print(numero)

for n in range(4,80):
    print(n)
print("-----------------")
print("nurinpäin:")

for n in range(50, 0, -2):      #50 = alkupiste, 0 = loppupiste, -2 = väli/frekvenssi
    print(n)

print("-----------------")

# luvut = [2,4,6,5,2,7,2,7]

luvut_listan_pituus = len(luvut)
for n in range(luvut_listan_pituus):
    # print(n) -> tämä on iteraattori
    print(luvut[n])

print("----------------------")
# printataan vain 3
for n in range(3):
    print(kaupunkilista[n])   #tässä tapauksessa printattiin kaupunkilistan kolme ensimmäistä kaupunkia.
