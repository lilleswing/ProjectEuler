from pybrain.utilities import memoize

__author__ = 'leswing'


@memoize
def p181(b, w, min_b, min_w):
    if b == 0 and w == 0:
        return 1

    if min_w > w:
        min_w = 0
        min_b += 1

    if min_b > b or w < 0:
        return 0

    if min_b > b / 2:
        return 1

    res = 0

    b1 = min_b
    if b1 == 0 and min_w == 0:
        min_w = 1

    for w1 in range(min_w, w + 1):
        res += p181(b - b1, w - w1, b1, w1)

    for b1 in range(min_b + 1, b / 2 + 1):
        for w1 in range(0, w + 1):
            res += p181(b - b1, w - w1, b1, w1)

    return res + 1


print p181(40, 60, 0, 0)
