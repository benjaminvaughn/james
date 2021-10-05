import datetime
from requests import Request, Session
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from bs4 import BeautifulSoup
url = ['https://www.livecoinwatch.com/price/Tether-USDT', 'https://www.livecoinwatch.com/price/Cardano-ADA', 'https://www.livecoinwatch.com/price/Bitcoin-BTC', 'https://www.livecoinwatch.com/price/Dogecoin-DOGE', 'https://www.livecoinwatch.com/price/Radicle-RAD']
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}


for i in url:
    r = requests.get(url=i, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.select('html body#body.dark-page div#__next div.position-relative div.content-hack.content-hack-n-header main.main.main-inner div.d-flex.flex-column-reverse div.mb30.mb-mob-20 div.container div.rounded-box.typical-box.border.px-main.coin-section section div.coin-tools div.center-between.w-100.coin-row div.official-name div.cion-item.coin-price-large span.price')
    print(price[0].text)

r = requests.get(url="https://www.investing.com/crypto/cardano/historical-data", headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup)
prices = []

print(soup.select("td"))

for i in soup.select("td"):
    if "green" in str(i) or "red" in str(i) and "%" not in str(i):
        if '%' not in str(i):
            prices.append(i.text)

print(prices)
print(len(prices))
base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(0, 31)]
print(len(date_list))