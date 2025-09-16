#tehtävä 2
#Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
#Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector
from mysql.connector import cursor

# Otetaan tietokantayhteys
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="OrnataLog26",
    port=3306,  #3306 on oletusarvo, ei tarvitse kirjoittaa
    database="flight_game",
    autocommit=True
)

# funktio, joka hakee lentokentät maakoodin perusteella, lukumäärät tyypeittäin.
print("Give a country code and I will show how many airports of each type the specified country has.")
def start():
    maakoodi = input("Anna maakoodi: ")
    sql = f"SELECT type, count(*) as määrä FROM airport where iso_country='{maakoodi}' GROUP BY type"



    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

    if cursor.rowcount > 0 :
        print(f"Tässä maassa on {cursor.rowcount} eri tyyppistä kenttää.")
        for rivi in result:
            print(f"{rivi[1]} lentokenttää joiden tyyppi: {rivi[0]}")
    else:
        print("Tällä maakoodilla ei ole maata.")
        start()
start()