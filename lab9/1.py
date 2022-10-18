import math
T=(9,12,8,2)
C=(6,3,9,2)
x=len(T)
c=0
m=0
while c<x:
    s=math.sqrt(math.pow((T[m]-C[m]),2)+math.pow((T[m+1]-C[m+1]),2))
    print(s)
    m=m+2
    c=c+2
