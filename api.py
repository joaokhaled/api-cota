import os
from api2 import *
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def teste():
	return jsonify([{"dolar": f'{k[1].text}', 'dolar-australiano': f'{k2[1].text}', 'dolar-canadense': f'{k3[1].text}', 'dolar-neozelandes': f'{k4[1].text}', 'euro': f'{k5[1].text}', 'iene': f'{k6[1].text}', 'libra': f'{k7[1].text}', 'ouro': f'{k8[1].text}', 'peso-argentino': f'{k9[1].text}', 'peso-chileno': f'{k0[1].text}', 'peso-uruguaio': f'{ka[1].text}', 'won-coreano': f'{kb[1].text}', 'yuan': f'{kc[1].text}'}])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)