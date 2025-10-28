# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
# Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat.
# Tee aliluokkiin metodi tulosta_tiedot, joka tulostaa kyseisen julkaisun kaikki tiedot.
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.


class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}")
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumaara}")
        print("-" * 30)

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.nimi = nimi
        self.paatoimittaja = paatoimittaja

    if __init__ == "__main__":
        lehti = Lehti("Aku Ankka", "Aki Hyyppä")
        kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

        lehti.tulosta_tiedot()
        kirja.tulosta_tiedot()

        # ** EI VALMIS, TEE KOTONA LOPPUUN**


