prod = 1
count = 0
for i in xrange(1,101):
    prod *= i

while(prod != 0):
    count += prod % 10
    prod = prod / 10

print count
