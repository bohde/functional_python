import operator as op
import itertools as it
from functools import partial
from collections import deque

class Wrapper(object):
    def __init__(self, data):
        self.data = data

    def __lt__(self, other):
        print 'comparing', self.data, other.data
        return self.data < other.data


def partition(predicate, iterable):
    passing, failing = deque(), deque()

    def gen(f, mine, other):
        while True:
            if mine:
                yield mine.popleft()
            else:
                newval = next(iterable)
                if f(newval):
                    yield newval
                else:
                    other.append(newval)

    return (
        gen(predicate, passing, failing),
        gen(lambda i: not(predicate(i)), failing, passing)
    )
                    

def isorted(xs):
    xs = iter(xs)
    pivot = next(xs)

    below, above = partition(lambda y: y < pivot, xs)

    for x in isorted(below):
        yield x

    yield pivot

    for x in isorted(above):
        yield x


def imin(xs):
    return next(isorted(xs))


def insmallest(n, xs):
    return it.islice(isorted(xs), 0, n)
