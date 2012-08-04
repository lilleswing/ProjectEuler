def hail(h,n):
    if(n in h):
        return h[n]
    if(n%2==0):
        t = hail(h,n/2)
    else:
        t = hail(h, n*3+1)
    h[n] = t+1
    return t+1


h= dict()
h[1] = 0
best = 0
for i in xrange(1,1000001):
    t = hail(h,i)
    if(t > best):
        best = t
        print i

