# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
# Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen,
# jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import json
import requests


API_key = "d04592ec87c010011d63707ecda8ab59"
city_name = input("Enter City name: ")
#lon = input("Enter Longitude: ")
#lat = input("Enter Latitude: ")
# Pyynnön malli: https://openweathermap.org/api
lang = "FI"
pyyntö = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={API_key}"

try:
    vastaus = requests.get(pyyntö)
    print("Status code", vastaus.status_code)
    if vastaus.status_code==200:
        data = vastaus.json()
        print(json.dumps(data, indent=2))
        eka = data[0]
        print(eka)
        lat, lon = eka["lat"], eka["lon"]
        print(f"Kaupungin {city_name} leveysaste on {lat} ja pituusaste on {lon}")
        print(f"Sää kohteessa {city_name}: {data['weather'][0]['description']}")
except requests.exceptions.RequestException as e:
    print(e)
    print ("Hakua ei voitu suorittaa.")