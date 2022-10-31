import csv
i=0
b=0
c=[]
s=[]
with open("f.csv", newline = '') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=";")
    for row in reader:
        while float(row['t']) > i:
            i = float(row['t'])
            c= (row['d'])
        while float(row['t']) < b:
            b = float(row['t'])
            s= (row['d'])
        print('День', row['d'], 'Температура', row['t'])
    print('День з найбільшою температурою', c)
    print('День з найменшою температурою', s)





