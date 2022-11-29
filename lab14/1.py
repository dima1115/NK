import requests
import json
yco = requests.get("https://news.ycombinator.com/newest")
cnn = requests.get("https://edition.cnn.com/")
bbc = requests.get("https://www.bbc.com/news/world")
x = open("tf.txt", "r")
tf = x.read()
tf = tf.replace(',', '').split()
spis_yco= []
spis_cnn=[]
spis_bbc=[]
spis_yco.append(' news.ycombinator')
if yco.status_code==200:
    n=0
    while len(tf)>n:
        if yco.text.count(tf[n])>0:
            spis_yco.append(tf[n])
            spis_yco.append( yco.text.count(tf[n]))
        n=n+1
spis_cnn.append(' CNN')
if cnn.status_code==200:
    n=0
    while len(tf)>n:
        if cnn.text.count(tf[n])>0:
            spis_cnn.append(tf[n])
            spis_cnn.append( cnn.text.count(tf[n]))
        n=n+1
spis_bbc.append(' BBC')
if bbc.status_code==200:
    n=0
    while len(tf)>n:
        if bbc.text.count(tf[n])>0:
            spis_bbc.append(tf[n])
            spis_bbc.append(bbc.text.count(tf[n]))
        n=n+1
cspis=[]
cspis.append(spis_cnn)
cspis.append(spis_yco)
cspis.append(spis_bbc)
with open('ksinfo.json', 'w') as f:
   json.dump(cspis, f)