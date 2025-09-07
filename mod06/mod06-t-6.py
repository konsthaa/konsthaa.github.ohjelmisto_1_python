# Tehtävä 6
# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
  # kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

def laske_yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2
    pinta_ala = math.pi * sade ** 2
    return hinta / (pinta_ala / 10000)  # Muunnetaan cm² -> m² ja jaetaan hinta

#Pääohjelma
halkaisija1 = float(input("Syötä ensimmäisen pizzan halkaisija (cm): "))
hinta1 = float(input("Syötä ensimmäisen pizzan hinta (€): "))
halkaisija2 = float(input("Syötä toisen pizzan halkaisija (cm): "))
hinta2 = float(input("Syötä toisen pizzan hinta (€): "))

yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)

print(f"Ensimmäisen pizzan yksikköhinta: {yksikkohinta1:.2f} €/m²")
print(f"Toisen pizzan yksikköhinta: {yksikkohinta2:.2f} €/m²")

if yksikkohinta1 < yksikkohinta2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif yksikkohinta2 < yksikkohinta1:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Molemmat pizzat antavat saman vastineen rahalle.")