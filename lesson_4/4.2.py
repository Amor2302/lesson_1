import requests
import json
import pprint
import datetime as dt

def currency_rates():

    URL = 'https://www.cbr-xml-daily.ru/daily_json.js'

    response = requests.get(URL)
    dict_json = json.loads(response.text)
    start = dt.datetime.utcnow() + dt.timedelta(hours=3)
    res = f" {start.strftime('%d %b %Y')} {dict_json['Valute']['EUR']['Value']}"
    print(res)

currency_rates()


