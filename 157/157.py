__author__ = 'leswing'

N = 1
ns = [10 ** x for x in xrange(1, N + 1)]
print(ns)
count = 0
for a in xrange(0, 10000):
    for b in xrange(1, a):
        plus = a + b
        mul = a * b
        for n in ns:
            my_plus = plus * n
            if mul % my_plus == 0:
                count += 1

print(count)
