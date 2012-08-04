fib = [0]*90
sum = [0]*90
lim = 1
def recur(n,sum,fib):
	if(n <=2):
		return sum[n]
	else:
		for i in xrange(0,90):
			if(fib[i] <= n):
				t=i
		return sum[t]+n-fib[t]+recur(n-fib[t],sum,fib)
for i in xrange(0,17):
	lim = lim * 10
fib[0] = 0
fib[1] = 1
fib[2] = 2
sum[0] = 0
sum[1] = 1
sum[2] = 2
for i in xrange(3,90):
	fib[i] = fib[i-1]+fib[i-2]
	sum[i] = sum[i-1]+sum[i-2]+fib[i-2]-1

print recur(lim-1,sum, fib)
