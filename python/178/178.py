# solution = 126461847755
pand_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


class Square:
    def __init__(self):
        self.partials = dict()

    def add_square(self, square):
        for partial_key in square.partials.keys():
            if partial_key not in self.partials:
                self.partials[partial_key] = 0
            self.partials[partial_key] += square.partials[partial_key]

    def num_pand(self):
        if pand_tuple in self.partials:
            return self.partials[pand_tuple]
        return 0


def extend_square(sq, val):
    """Create a new square with the same data but all sets
    are extended with val"""
    retval = Square()
    for partial_key in sq.partials.keys():
        partial_key_set = set(partial_key)
        partial_key_set.add(val)
        new_partial_key = tuple(sorted(partial_key_set))
        if new_partial_key not in retval.partials:
            retval.partials[new_partial_key] = 0
        retval.partials[new_partial_key] += sq.partials[partial_key]
    return retval


def dp_step(squares, val):
    retval = Square()
    for square in squares:
        ext = extend_square(square, val)
        retval.add_square(ext)
    return retval


glob_num_digits = 41
dp = list()
for i in xrange(0, 10):
    l = [None] * glob_num_digits
    dp.append(l)

# seed the dp
for i in xrange(0, 10):
    sq = Square()
    if i == 0:  # Can't start a number with 0
        sq.partials[tuple([i])] = 0
    else:
        sq.partials[tuple([i])] = 1
    dp[i][1] = sq

count = 0
for num_digits in xrange(2, glob_num_digits):
    for digit_value in xrange(0, 10):
        components = list()
        under = digit_value - 1
        if under >= 0:
            components.append(dp[under][num_digits - 1])
        over = digit_value + 1
        if over <= 9:
            components.append(dp[over][num_digits - 1])
        dp[digit_value][num_digits] = dp_step(components, digit_value)
        count += dp[digit_value][num_digits].num_pand()

print(count)
