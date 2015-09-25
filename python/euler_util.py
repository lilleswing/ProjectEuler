from math import ceil


def sieve(size):
    l = [1] * size
    k = 4
    l[0] = 0
    l[1] = 0
    while (k < size):
        l[k] = 0
        k += 2
    k = 3
    while k < size:
        m = 2
        while k * m < size:
            l[k * m] = 0
            m += 1
        k += 2
    l2 = list()
    for i in xrange(0, size):
        if l[i] == 1:
            l2.append(i)
    return l2


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def factor(n):
    l = list()
    while n % 2 == 0:
        n = n / 2
        l.append(2)
    i = 3
    while n != 1:
        while n % i == 0:
            n = n / i
            l.append(i)
        i += 2
    return l


def numdivisors(n):
    l = factor(n)
    d = dict()
    for i in l:
        if i not in d:
            d[i] = 0
        d[i] = d[i] + 1
    prod = 1
    return reduce(lambda x, y: (d[y] + 1) * x, d.keys(), 1)
    #for key in d.keys():
    #    prod = prod * (d[key]+1)
    #return prod


def properdivisors(n):
    l = list()
    k = 1
    top = ceil(n ** 0.5)
    while k < top:
        if n % k == 0:
            l.append(k)
            l.append(n / k)
        k += 1
    return list(set(l))


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True
