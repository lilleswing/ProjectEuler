for a in xrange(1,1000):
    for b in xrange(a+1,1000):
        c = 1000-a-b
        if(a*a+b*b==c*c):
            print a*b*c
