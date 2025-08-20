#20.8. tuntiesimerkkejä

"""
monirivinen kommentti (merkkijono, string)
voidaan myös sijoittaa muuttujaan
"""""
import math

nimi = input("Anna nimesi: ") # palauttaa merkkijonon (str)
ika = 20 #kokonaisluku (int)
ika_ensi_vuonna = ika + 1 # int

str_ika_ensi_vuonna = str(ika_ensi_vuonna) # -> "21"


tervehdys = "Moi " + nimi + " " + str_ika_ensi_vuonna
1+2 # 3

print(tervehdys)


# Simppeli laskukone

# luetaan käyttäjältä kaksi luku (str), jotka muunnetaan samantien liukuluvuiksi ja sijoitetaan muuttujiin

luku1 = float(input("anna ensimmäinen luku: ")) # esim. "10" -> 10.0
luku2 = float(input("anna toka luku: ")) # esim. "20" -> 20.0

# Lasketaan tulos numeerisilla arvoilla
# tulos = int(luku1) 0 int(luku2) # kokonaisluvuilla
tulos_yhteenlasku = luku1 + luku2 # liukuluvuilla
tulos_vahennyslasku = luku1 - luku2
tulos_jakolasku = luku1 / luku2
kokonaisosa = luku1 // luku2
jakojaannos = luku1 % luku2
tulos_kertolasku = luku1 * luku2
tulos_potenssiin_korotus = luku1 ** luku2


#tulos= 1+2 # 3 (kovakoodattu arvo test)


print("Yhteenlaskutoimituksen tulos: " + str(tulos_yhteenlasku))
print("Vähennyslaskun tulos: " + str(tulos_vahennyslasku))
# tulosteeen muotoilu f-stringillä (kannattaa)
#print(Kertolaskun tulos: " + str(tulos_kertolasku)")
print(f"Jakolaskun tulos: {luku1 / luku2:.2f}, jossa kokonaisosa on "
      f"{kokonaisosa}, desimaaliosa {tulos_jakolasku - kokonaisosa} ja "
      f"jakojaannos {jakojaannos}")
# TODO: tulosta loput tulokset

# ympyrän ala: pi * r^2: 3.149 * r^2
# piin arvo math-kirjastosta (import-lause tiedoston alussa tarvitaan (rivillä 7))
print(math.pi)



