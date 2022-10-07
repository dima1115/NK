import math
a = int(input('Задайте a'))
b = int(input('Задайте b'))
h = int(input('Задайте h'))
x=a


for i in range(100):
    f = 1 / (math.pow(x, 2) + 1) + math.pow(x, 2)
    x=x+h
    print('x =', x, 'f=',f)
    if x>b:
        break