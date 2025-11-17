from flask import Flask, jsonify

app = Flask(__name__)

def onko_alkuluku(n):
    """Testaa onko luku n alkuluku. Hyödynnetään aiempaa tehokasta toteutusta."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


@app.route('/alkuluku/<int:luku>', methods=['GET'])
def tarkista_alkuluku(luku):
    """
    GET-pyyntö: http://127.0.0.1:3000/alkuluku/31
    Palauttaa: {"Number": 31, "isPrime": true}
    """
    return jsonify({
        "Number": luku,
        "isPrime": onko_alkuluku(luku)
    })


if __name__ == '__main__':
    app.run(port=3000, debug=True)