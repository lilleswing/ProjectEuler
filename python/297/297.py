size = 10**6

def countOne(arr):
	count = 0
	for x in arr:
		if(x==1):
			count += 1

	return count

def getIt(answers, loc):
	answer = [0] * len(answers[0])
	for x in xrange(loc,-1,-1):
		twin = loc-x
		bitPat1 = answers[x]
		bitPat2 = answers[twin]
		finished = True
		for i in xrange(len(bitPat1)):
			if(bitPat1[i] == 1 and bitPat2[i] == 1):
				finished = False
			answer[i] = bitPat1[i] & bitPat2[i]
		if(finished):
			answers[loc] = answer
			return 1
	return -1
			
				
def fillFib(size):
	l = []
	a = 1
	b = 2
	l.append(a)
	while(b < size):
		a,b = b, a+b
		l.append(a)
	return l

l = fillFib(size)
answers = []
for x in xrange(0,size):
	answers.append([0]*len(l))

for x in xrange(0,len(l)):
	answers[l[x]][x] = 1

print "All Set Up"
for x in xrange(1,size):
	if(getIt(answers,x)==-1):
		print "FAIL MOM"
print "All Done"
count = 0
for x in xrange(1,size): 
	count += countOne(answers[x])
print count
