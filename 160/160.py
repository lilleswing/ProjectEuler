__author__ = 'leswing'

top = 10**12
up_to = 100000  # n % up_to is 5 digits long at max


# handle powers of 10 first
mod_val = 1
twos = 0
fives = 0

for i in xrange(2, top+1):
    if i % 10000 == 0:
        print(i)
    while i % 2 == 0:
        i /= 2
        twos += 1
    while i % 5 == 0:
        i /= 5
        fives += 1
    i %= up_to
    mod_val = (mod_val * i) % up_to

two_pow = pow(2, twos-fives, up_to)
mod_val = (mod_val * two_pow) % up_to

print mod_val
