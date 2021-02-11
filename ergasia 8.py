import urllib.request
import json
sinolikoposo = 0
with open('coins.json') as json_file:
    jdata = json.load(json_file)
print(jdata)
for kriptonomisma in jdata:
    print(kriptonomisma)
    print(jdata[kriptonomisma])
    urltocheck = "https://min-api.cryptocompare.com/data/price?fsym=" + kriptonomisma + "&tsyms=EUR"
    print(urltocheck)
    r=urllib.request.urlopen(urltocheck)
    html=r.read()
    html=html.decode()
    data=json.loads(html,strict=False)
    print(data)
    value = data["EUR"]
    print(value)
    sinolikoposo = (value * jdata[kriptonomisma]) + sinolikoposo

print("Sinolo aksias se euro: ", sinolikoposo)