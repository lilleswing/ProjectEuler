this = 2
last = 1
sum = 0
even = 1
while(this < 4000000):
	if(even == 0):
		sum += this
	last,this = this,this+last
	even = (even+1)%2
print sum
