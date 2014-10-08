import math

#LIMIT = 10**15
LIMIT = 4
MOD_VAL = 10**9

def mod(k):
    return k % MOD_VAL

def sumSquaresMod(n):
    return (n * (n + 1) * (2 * n + 1)) / 6

def SIGMA():
    split_count = long(math.sqrt(LIMIT))
    split_count = long(max([split_count / 3, 1]))
    split_at = long(LIMIT / (split_count + 1))

    total = 0
    for i in xrange(1, LIMIT+1):
        count = mod(LIMIT / i)
        term = mod(i * i)
        term = mod(term * count)
        total = mod(term + total)

    for i in xrange(split_count, 0, -1):
        start = int(LIMIT / (i + 1))
        end = int(LIMIT / i)

        print(start, end)
        sumSquares = sumSquaresMod(end) - sumSquaresMod(start)
        total = mod(total + i * sumSquares)

    return total

if __name__ == "__main__":
    global LIMIT
    for i in xrange(1, 7):
        LIMIT = i
        print(SIGMA())

