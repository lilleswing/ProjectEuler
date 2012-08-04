def ispal(n):
    return str(n) == str(n)[::-1]

best = 0
for i in xrange(100,1000):
    for j in xrange(100,1000):
        k = i*j
        if(k > best and ispal(k)):
            best = k
print best
