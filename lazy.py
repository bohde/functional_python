import operator as op
import itertools as it
from functools import partial

class Wrapper(object):
    def __init__(self, data):
        self.data = data

    def __lt__(self, other):
        print 'comparing', self.data, other.data
        return self.data < other.data


def partition(predicate, iterable):
    pack = partial(it.imap, lambda i: (predicate(i), i))

    new_pred = op.itemgetter(0)
    unpack = partial(it.imap, op.itemgetter(1))

    packed = pack(iterable)
    first, second = it.tee(packed)

    passing = it.ifilter(new_pred, first)
    failing = it.ifilterfalse(new_pred, second)

    return map(unpack, (passing, failing))


def isorted(xs):
    xs = iter(xs)
    pivot = next(xs)

    below, above = partition(lambda y: y < pivot, i)

    for x in isorted(below):
        yield x

    yield pivot

    for x in isorted(above):
        yield x


def imin(xs):
    return next(isorted(xs))


def insmallest(n, xs):
    return it.islice(isorted(xs), 0, n)
