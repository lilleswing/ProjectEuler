def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True


dnp = set()    # set of deceptive non-primes
L = 25
n = 91    # start with first valid n given in the problem description

while len(dnp) < L:
    if not is_prime(n) and pow(10, n-1, 9*n) == 1:
        dnp.add(n)
    n += 2

print "Project Euler 130 Solution =", sum(dnp)
