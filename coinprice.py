try:
    import urequests as requests
except ImportError:
    import requests

def get_json(name):
    url = "https://api.coinmarketcap.com/v1/ticker/{}/?convert=USD&limit=1".format(name)
    r = requests.get(url)
    json = r.json()
    #print(r)
    #print(r.content)
    #print(r.text)
    #print(r.content)
    #print(r.json())
    
    # It's mandatory to close response objects as soon as you finished
    # working with them. On MicroPython platforms without full-fledged
    # OS, not doing so may lead to resource leaks and malfunction.
    r.close()
    return process_json(json[0])


def process_json(json):
    json['price_usd'] = float(json['price_usd'])
    json['percent_change_1h'] = float(json['percent_change_1h'])
    json['percent_change_24h'] = float(json['percent_change_24h'])
    json['percent_change_7d'] = float(json['percent_change_7d'])
    return json