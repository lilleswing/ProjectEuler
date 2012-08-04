size = 21
l = list()
for i in xrange(0,size+1):
    l.append([0]*(size+1))

l[0][1] = 1
for i in xrange(1,size+1):
    for j in xrange(1,size+1):
        l[i][j] = l[i-1][j] + l[i][j-1]

#for i in l:
#    print i
print l[21][21]
