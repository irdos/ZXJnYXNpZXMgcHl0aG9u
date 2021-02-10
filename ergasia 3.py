import urllib.request
import json
import calendar
import datetime

now = datetime.datetime.now()
xronosminas = now.strftime("%y-%m")


minas = now.strftime("%m")
xronos = now.strftime("%Y")
mera = now.strftime("%d")

i = 1 
statlist = [0] * 80

while i <= int(mera):
    
    if len(str(i)) == 1:
        kataskeuimera = "0" + str(i)
    else:   
        kataskeuimera = str(i)
    kataskeui = xronos + "-" + minas + "-" + kataskeuimera
    urltocheck = "https://api.opap.gr/draws/v3.0/1100/draw-date/" + kataskeui +"/" + kataskeui + "/draw-id"
    
    r=urllib.request.urlopen(urltocheck)
    html=r.read()
    html=html.decode()
    data=json.loads(html,strict=False)
    k = data[0]
    print(k)
    urltocheck2 = "https://api.opap.gr/draws/v3.0/1100/" + str(k)
    r2=urllib.request.urlopen(urltocheck2)
    html2=r2.read()
    html2=html2.decode()
    data2=json.loads(html2,strict=False)
    k2 = data2["winningNumbers"]["list"]
    
    print(k2)
    for j in range(len(k2)):
        o = k2[j]                                                                    
        statlist[o - 1] += 1
        j += 1

    
    i +=1
for i in range(len(statlist)):
    print("To noumero: ", i + 1," bgike ", statlist[i], " fores.")

