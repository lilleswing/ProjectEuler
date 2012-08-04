a = 0
b = 0
for i in xrange(1,101):
    a += i*i
    b += i
b = b*b
print b-a
