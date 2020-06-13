import os
from scrapy import *
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def api():
	return jsonify(
					[
						{
							'moedas':
								{
								'dolar': f'{k[1].text}', 
					 			'dolar-au': f'{k2[1].text}', 
					 			'dolar-cad': f'{k3[1].text}', 
					 			'dolar-nzd': f'{k4[1].text}', 
					 			'eur': f'{k5[1].text}', 
					 			'iene': f'{k6[1].text}', 
					 			'libra': f'{k7[1].text}', 
					 			'ouro': f'{k8[1].text}', 
					 			'peso-arg': f'{k9[1].text}', 
					 			'peso-chi': f'{k0[1].text}', 
					 			'peso-uru': f'{ka[1].text}', 
					 			'won-sul coreano': f'{kb[1].text}', 
					 			'yuan': f'{kc[1].text}'
					 			},
					 		'update': ’upd'
						 }						 						 		
					] 
				)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
