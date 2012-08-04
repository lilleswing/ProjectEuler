n = 2**1000
count = 0
while(n != 0):
    count += n % 10
    n = n / 10
print count
