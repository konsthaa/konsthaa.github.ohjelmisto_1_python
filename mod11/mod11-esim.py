# periytyminen (**KATSO MUISTIINPANOT GITHUBISSA**)

# self-viittaus tekee oliolle ominaisuuden, joka jää muistiin.

class Elain:
    def __init__(self, nimi, syntymävuosi):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi

    def tulosta_tiedot(self):               # metodi
      print(f"{self.nimi} on kissa, joka on syntynyt vuonna {self.syntymävuosi}")

    def puhu(self, kerrat, ääni="---"):
        for i in range(kerrat):
            print(ääni)



class Koira(Elain):
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.haukahdus = haukahdus
        super().__init__(nimi, syntymävuosi)

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)
    # ylikirjoitetaan elaimen puhu() -metodi ja kutsutaan sieltä luokan omaa
    def puhu(self, kerrat, ääni="---"):
        self.hauku(kerrat)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"{self.nimi} on koira")

class Kissa(Elain):
    def __init__(self, nimi, vuosi):
        super().__init__(nimi, vuosi)

    def puhu(self, kerrat, ääni="---"):
        super().puhu(kerrat, "Miumiu")


elaimet = []
elaimet.append(Koira("Ruffe", 2020))
elaimet.append(Kissa("Mila", 2018))
elaimet.append(Elain("Tipu", 2024))
for elain in elaimet:
    elain.tulosta_tiedot()
    elain.puhu(2)


koira = Koira("Ruffe", 2020)
koira.hauku(2)
kissa = Kissa("Mila", 2018)
print(f"{kissa.nimi}: syntymävuosi {kissa.syntymävuosi}")
kissa.tulosta_tiedot()
koira.tulosta_tiedot()