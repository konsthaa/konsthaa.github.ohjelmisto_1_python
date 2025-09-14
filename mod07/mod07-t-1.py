# tehtävä 1
# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

kevät = [3, 4, 5]
kesä = [6, 7, 8]
syksy = [9, 10, 11]
talvi = [12, 1, 2]

kysymys = int(input("Anna kuukauden numero: "))
if kysymys in kevät:
    print("kevät")
if kysymys in kesä:
    print("kesä")
if kysymys in syksy:
    print("syksy")
if kysymys in talvi:
    print("talvi")


# TESTAA OMASSA HARJOITUSKOE; LÖYTYY ETUSIVULTA!!!!!


