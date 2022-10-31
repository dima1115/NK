import json

i=0
b=0
c=[]
s=[]
with open('j.json', 'r', encoding='utf-8') as f:
    text = json.load(f)


for txt in text['info']:
    while i<txt['capacity']/txt['price']:
        i=txt['capacity']/txt['price']
        c=txt['name']
for txt in text['info']:
    while i>txt['capacity']/txt['price']:
        i=txt['capacity']/txt['price']
        s=txt['name']
print(c)
print(s)
