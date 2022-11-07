def Nr(x,n):
    f = ''
    m = 0
    l = len(x)
    while l > m:
        y = x[m: m+n]
        m = m + n
        f = f+y+' '
    print(f)
def r_two(x):
    m = 0
    l = len(x)
    while l > m:
        y = x[m: m+2]
        m = m + 2
        print(y)