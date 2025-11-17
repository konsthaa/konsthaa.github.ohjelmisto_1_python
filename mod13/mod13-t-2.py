

# Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin JSON-muodossa.
# Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
# Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
# Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

from flask import Flask, jsonify

app = Flask(__name__)

# Lentokenttätietokanta (simuloitu opintojakson tietokannan pohjalta)
# Avain: ICAO-koodi, Arvo: (Nimi, Kunta)
lentokentat = {
    "EFHK": ("Helsinki Vantaa Airport", "Helsinki"),
    "EFKT": ("Kittilä Airport", "Kittilä"),
    "EFRO": ("Rovaniemi Airport", "Rovaniemi"),
    "EFJO": ("Joensuu Airport", "Joensuu"),
    "EFMA": ("Mikkeli Airport", "Mikkeli"),
}


@app.route('/kenttä/<icao>', methods=['GET'])
def hae_kentta(icao):
    """
    GET-pyyntö: http://127.0.0.1:3000/kenttä/EFHK
    Palauttaa: {"ICAO": "EFHK", "Name": "Helsinki Vantaa Airport", "Municipality": "Helsinki"}
    """
    if icao.upper() in lentokentat:
        nimi, kunta = lentokentat[icao.upper()]
        return jsonify({
            "ICAO": icao.upper(),
            "Name": nimi,
            "Municipality": kunta
        })
    else:
        return jsonify({"error": "Lentokenttää ei löytynyt"}), 404


if __name__ == '__main__':
    app.run(port=3000, debug=True)