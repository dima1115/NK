import random
class KARD():

    def __init__(self):
        self.kk=24
        self.sk=['9.1', '9.2', '9.3', '9.4', '10.1', '10.2', '10.3', '10.4', 'v1',  'v2', 'v3', 'v4', 'd1', 'd2', 'd3', 'd4', 'k1', 'k2', 'k3', 'k4', 't1', 't2', 't3', 't4']

    def mix(self):
        sk=self.sk
        random.shuffle(sk)
        return sk

    def rem(self, r):
        self.sk.remove(r)
        print(r)

c = KARD()
N=float(input('N '))
l=0
g=1
k=int(c.kk/N)
while c.kk>l:
    print('Карти', g, 'гравця', c.sk[l:l+k])
    g=g+1
    l=l+k
