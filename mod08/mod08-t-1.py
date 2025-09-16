# Tehtävä 1

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

# funktio, joka hakee lentokentän sen koodin perusteella. Myös sijaintikunnan.

cursor = connection.cursor()
# Kysytään IACO-koodi
ident = input("Anna ICAO-koodi: ").upper()

# Haetaan lentoaseman nimi ja sijaintikunta tietokannasta.
sql = f"SELECT name, municipality FROM airport WHERE ident='{ident}'"
print(sql)
cursor.execute(sql)
#cursor.execute() == str("SELECT name, municipality FROM airport WHERE ident = ?, ident")
#cursor.execute("SELECT name, municipality FROM airport WHERE ident = ?", (ident))
result = cursor.fetchone()
print(result)
# Tulostetetaan tulos



if result:
    airport_name, municipality = result
    print(f"Lentoaseman nimi: {airport_name}")
    print(f"Sijaintikunta: {municipality}")
else:
    print("Lentoasemaa ei löydy tietokannasta.")

# Suljetaan
connection.close()
