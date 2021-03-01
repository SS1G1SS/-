import multiprocessing
import urllib.request
import json
import time

with open("crypto.txt") as f:
    data = json.load(f)
    result = data

resultbtc = result['BTC']
resultdash = result['DASH']
resulteth = result['ETH']

url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=ETH,DASH,BTC&tsyms=BTC,EUR&api_key=9a96785fb79da776270b5ffc9e989d9092bbe24d23472e107301cec5ff8a82f3"
data = urllib.request.urlopen(url)
html = data.read()
html = html.decode()
o = json.loads(html)
btcv = o['BTC']['EUR']
dashv = o['DASH']['EUR']
ethv = o['ETH']['EUR']
fresbtc = btcv * resultbtc
fresdash = dashv * resultdash
freseth = ethv * resulteth

print ("Ο χρήστης",result['Name'],"εχει",fresbtc,"€ σε BITCOIN",freseth,"€ σε ETHEREUM",fresdash,"€ σε DASH")
time.sleep(5)
