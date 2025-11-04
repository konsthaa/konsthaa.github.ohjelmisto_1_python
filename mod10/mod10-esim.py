# Assosiaatio

# **KTS. OPETTAJAN MUISTIINPANOT, SIELLÄ TEHTY OIKEIN**

# Rakenteen suunnittelu


#esimerkki githubista:
class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)
        return

# luodaan pysyvä assosiaatiosuhde Hoito ja Koira-luokkien välillä:
# Koirat tallennetaan luokan ominaisuutena olevaan koiralistaan

class yritys:
    def __init__(self, yritys, osoite):
        self.nimi = yritys
        self.osoite = osoite
        self.hoitolat = []

    def lisaa_hoitola(self):
        self.hoitolat.append(hoitola1)

    def tulosta_hoitola(self):
        for h in self.hoitolat:
            print(h.nimi)

    def anna_joululahja(self):
        print("Yritys antaa joululahjan jokaiselle koiralle.")
        for h in self.hoitolat:
            print(f"Annetaan lahjoja {h.nimi} koirille.")
            for koira in h.koirat:
                print(f"{koira.nimi} saa lahjaksi luun.")
                koira.hauku(1)

        # käytetään metodeja

        for hoitola in self.hoitolat:
            print("Yritys antaa toisen luun")
            hoitola.tervehdi_koiria()



class Hoitola:
    def __init__(self, nimi):
        self.nimi = nimi
        self.koirat = []


    # metodi, jonka parametrina annetaan viittaus Koira-olioon:
    # **Assosiaatiosuhde on voimassa vain metodikutsun ajan**
    def koira_sisään(self, koira):
        print(koira)
        print(f"Lisätään kohta koira {koira.nimi} sisään hoitolaan")
        self.koirat.append(koira)
        return

    def koira_ulos(self, koira):
        print(koira)
        self.koirat.remove(koira)
        print(f"Heippa {koira.nimi} ja hyvää kotimatkaa!")
        return


    def printtaa_koirat(self):
        print(f"Hoitolassa {self.nimi} on seuraavat koirat:")
        for koira in self.koirat:
            print(koira.nimi)

    def tervehdi_koiria(self, kerrat):
        print("Tervehditään koiria ja jokainen koira haukkuu: ")
        for koira in self.koirat:
            koira.hauku(1)


# Pääohjelma
# 4 eri koiraa
koira1 = Koira("Nita", 2018, "WuufWuuf")
koira2 = Koira("Androi", 2019, "HauHau")
koira3 = Koira("Hermann", 2020, "Räyh")
koira4 = Koira("Alona", 2013, "WäyWäy")

yritys= yritys("Hauhau.ry", "Osoite vanhavuorenkatu")
yritys.lisaa_hoitola("hoitola1")
yritys.lisaa_hoitola("hoitola2")

yritys.tulosta_hoitolat
hoitolat = ["hoitola1", "hoitola2"]
print(koira1.nimi)
koira1.hauku(3)


# Lisätään koira koirahoitolaan
# Koira1 Onnentassuun
hoitola1 = Hoitola("Onnentassu")
hoitola1.koira_sisään(koira1)
hoitola1.koira_sisään(koira2)


hoitola2 = Hoitola("Pikkukoirat")
hoitola2.koira_sisään(koira3)
hoitola2.koira_sisään(koira4)


hoitola1.printtaa_koirat()
hoitola2.printtaa_koirat()

# Tervehdi koiria:
hoitola1.tervehdi_koiria(3)

# Poistetaan koira hoitolasta:
hoitola1.koira_ulos(koira1)

yritys.anna_joululahja()
