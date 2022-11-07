import random
def ch(x):
    lx = len(x)
    z = 0
    y = ''
    r = 'abcdefghijklmnopqrstuvwxyz'
    while lx > z:
        m = x[z] + random.choice(r)
        y = y + m
        z = z + 1
    print(y)
def unch(x):
    lx = len(x)
    z = 0
    z1 = z + 1
    y = ''
    while lx > z:
        m = x[z]
        z = z + 2
        y = y + m
    print(y)