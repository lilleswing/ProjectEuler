primes = []
primes.append(2)
max = 40000000
for x in xrange(3,max,2):
	isPrime = True
	for j in primes:
		if(x%j==0):
			isPrime=False
			break;
	if(isPrime):
		primes.append(x)

for x in primes:
	print x
