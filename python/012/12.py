import euler_util

i = 2
div = 1
t = 1
while(div < 500):
    t += i
    i += 1
    div = euler_util.numdivisors(t)

print t
