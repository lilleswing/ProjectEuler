from itertools import izip

__author__ = 'leswing'
import copy

black = 3 - 1  # Seed with single black element
white = 1


class Group:
    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        return self.data == other.data

    def __hash__(self):
        return hash(self.data)

    def __repr__(self):
        return str(self.data)

    def add(self, data):
        new_data = tuple(x + y for x, y in izip(data, self.data))
        return Group(new_data)


class GroupCollection:
    def __init__(self, groups=list()):
        self.groups = frozenset(groups)

    def expand(self, data):
        """ Return a Set of GroupCollection objects that were expanded with data
        """
        retval = set()
        group_list = list(self.groups)
        for i in xrange(len(group_list)):
            before = group_list[:i]
            after = group_list[i + 1:]
            this = group_list[i]
            this = [this.add(data)]
            t_collection = GroupCollection(before + after + this)
            retval.add(t_collection)
        retval.add(GroupCollection(group_list + [Group(data)]))
        return retval

    def __hash__(self):
        return hash(self.groups)

    def __eq__(self, other):
        return self.groups == other.groups

    def __repr__(self):
        return str(self.groups)


def dp_step(previous, data):
    retval = set()
    for collection in previous:
        retval.update(collection.expand(data))
    return retval


def p181():
    previous = set()
    groupCollection = GroupCollection([Group((1, 0))])
    previous.add(groupCollection)
    for i in xrange(black):
        next_set = dp_step(previous, (1, 0))
        previous = next_set
        print("%s,%s" % (i, len(previous)))
    for i in xrange(white):
        next_set = dp_step(previous, (0, 1))
        previous = next_set
    print(previous)
    print(len(previous))


if __name__ == "__main__":
    p181()
