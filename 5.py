import euler_util
lcm = 1
for i in xrange(1,21):
    lcm = (lcm*i)/(euler_util.gcd(lcm,i))

print lcm
