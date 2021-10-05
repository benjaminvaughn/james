from logging import debug
from flask import Flask, json, request, render_template, jsonify


import requests as r

from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/graph', methods = ['POST'])
def graphjs():
    print(dict(request.values))
    coin = dict(request.values)['coin']
    print(coin) # send the request of that coin to coingecko
    # now simply return prices and dates back to the front end
    return jsonify({'prices': prices, 'dates': dates})

app.run(debug=True)