# The discriminant of the recurrence has to be a perfect square
# 5*k**2 + 14*k + 1 - b **2 = 0
# http://www.alpertron.com.ar/JQUAD.HTM

starts = [
        (0, -1),
        (0, 1),
        (-3, -2),
        (-3, 2),
        (-4, -5),
        (-4, 5),
        (2, -7),
        (2, 7)
        ]

sols = set()
for start in starts:
    k = start[0]
    b = start[1]
    for i in xrange(0, 30):
        if k > 0:
            sols.add(k)
        k, b = -9 * k - 4 * b - 14, -20 * k - 9 * b - 28

sol_list = sorted(list(sols))
print(sum(sol_list[0:30]))
