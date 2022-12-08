import pandas as pd
import json
with open('data.txt', 'r') as f:
    lines = f.readlines()
    for i in range(int(2)):
        lines[i] = (lines[i].rstrip()).split(' ')[:int(4)]
    lines=lines[:int(2)]  #вот это криво, конечно
c=[]
for line in lines:
    c.append(line)
m1=pd.Series(sum(c, []))#переводимо двухвимірний масив в одновимірний
m2=list(set(m1))#cортируюмо масив
print(m2)
with open("end.json", "w") as file:
    json.dump(m2, file)