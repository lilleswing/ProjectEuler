count = 0
limit = 100000000
x = 1
y = 1
while x + y < limit:
    x, y = 3 * x + 4 *y, 2 * x + 3 * y
    count += limit / (x + y)
print("%d pythagorean triangles" % count)
