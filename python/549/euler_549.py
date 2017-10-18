from collections import Counter
import json
import pickle
import math

largest = 10**8
#largest = 100

def get_primes():
    try:
        return json.loads(open('primes.json').read())
    except:
        pass
    primes = [x for x in primes_sieve(largest+1)]
    print("primes sieve complete")
    s = json.dumps(primes)
    with open('primes.json', 'w') as fout:
        fout.write(s)
    return primes

def get_factor_map(factor_map):
    try:
        raise ValueError()
        d = json.loads(open('factors.json').read())
        return {int(k): v for k,v in d.items()}
    except:
        pass
    for i in range(2, largest+1):
        if i % 10000 == 0:
            print(i)
        prime_factors(i, factor_map)
    return factor_map


def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False

def prime_factors(n, factor_map):
    if n in p_set:
        factor_map[n] = n
        return
    for p in primes:
        if n % p == 0:
            factor_map[n] = p
            return

def is_empty(c):
    for elem in c.values():
        if elem > 0:
            return False
    return True

def traverse_factor_map(n):
    fs = []
    while n != 1:
        p = factor_map[n]
        fs.append(p)
        n //= p
    return fs

def s_f(n):
    f = sorted(traverse_factor_map(n), reverse=True)

    factor_set = Counter()
    factor_set.update(f)
    index = 2
    while not is_empty(factor_set):
        f2 = traverse_factor_map(index)
        for elem in f2:
            if elem in factor_set:
                factor_set.subtract([elem])
        index += 1
    return index - 1

def exp_add(n1, n2):
    i = 2
    w = n1 ** i
    while w < n2:
        i += 1
        w = n1 ** i
    if w != n2:
        return 0
    return i - 1

def magic_number(n, exp):
    total = 0;
    mul = 0;
    while (total < exp):
        mul += 1
        total += 1
        x = mul;
        while x % prime == 0:
          total += 1
          x /= prime
    return n * mul


def s_f2(n):
    f = traverse_factor_map(n)
    factor_set = Counter()
    factor_set.update(f)
    l = [magic_number(k,v) for k,v in factor_set.items()]
    return max(l)


#print(magic_number(3,5))
#print(magic_number(5,2))
#print(magic_number(5,1))
primes = get_primes()
p_set = set(primes)
factor_map = {}
factor_map = get_factor_map(factor_map)
print("Done Precomputing")

total = 0
for i in range(2, largest+1):
    if i % 10000 == 0:
        print(i)
    total += s_f2(i)

print(total)
