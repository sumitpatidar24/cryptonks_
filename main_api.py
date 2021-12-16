import requests, time
from createdb import db
from emailsend import sm

data = db()
sendm = sm()

count = 0
bought_price = 45221277
while(count<10):
    response = requests.get("https://api.wazirx.com//api/v2/tickers")
    btc = response.json()['btcinr']
    data.insert(float(btc['last']), float(btc['low']), float(btc['high']))
    gl = round((float(btc['last'])-float(bought_price))/bought_price,2)*100
    msg = """\
        Subject: Bitcoin price up/low.

        Current price of bitcoin is- {}
        The gain/loss is- {}%.""".format(float(btc['last']), gl)
    if(float(btc['last'])>bought_price):
        sendm.send_mail(msg)
    count+=1
    print("done")
    time.sleep(10)
  


