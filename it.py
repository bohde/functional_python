import itertools
from combinators import Combinators, ChainedCombinators

def apply(comb, func):
    def inner(self, *args, **kwargs):
        return getattr(self, comb)(func, *args, **kwargs)
    return inner


class It(Combinators):
    map = apply('R', itertools.imap)
    filter = apply('R', itertools.ifilter)
    reduce = apply('R', reduce)

    flatten = apply('T', itertools.chain.from_iterable)
    flatten_string = apply('T', ''.join)

    def reject(self, f, *args, **kwargs):
        return self.filter(lambda n: not(f(n)), *args, **kwargs)


    def find(self, *args, **kwargs):
        return next(iter(self.filter(*args, **kwargs)))


    all = apply('T', all)
    any = apply('T', any)

    def include(self, val):
        return val in self._value
        

    def invoke(self, *args, **kwargs):
        return self.map(lambda i: It(i).K(*args, **kwargs))


    def pluck(self, attr):
        return self.map(lambda i: It(i).T(getattr, attr))

    
    max = apply('T', max)
    min = apply('T', min)

    sort = apply('T', sorted)

    __len__ = apply('T', len)

    list = apply('T', list)
    set = apply('T', set)

    def chain(self):
        return ChainedIt(self._value)

    def __iter__(self):
        return iter(self._value)


def lift(attrname):
    def wrapped(self, *args, **kwargs):
        return ChainedIt(getattr(super(ChainedIt, self), attrname)(*args, **kwargs))
    return wrapped
        

class ChainedIt(ChainedCombinators, It):
    find = lift('find')
    include = lift('include')
    
    def __iter__(self):
        return iter(self.value())

