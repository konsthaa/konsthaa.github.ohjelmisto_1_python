# mod12 esimerkki (ulkoisen rajapinnan käyttö).
import json
import requests

hakusana = input("Anna hakusana: ")

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyyntö = "https://api.tvmaze.com/search/shows?q=" + hakusana
vastaus = requests.get(pyyntö).json()

# Tämä on lähinnä koko vastauksen muotoilua varten:
print(json.dumps(vastaus, indent=2))


sanakirja = vastaus[0]
print(sanakirja["show"]["genres"][0])


# lista[0][0]
# sanakirja["show"]["name"]
