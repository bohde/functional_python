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
        return next(self.filter(*args, **kwargs))


    def all(self, *args, **kwargs):
        to_check = self.filter(*args, **kwargs) if len(args) else self
        return self.T(all)
        

    def any(self, *args, **kwargs):
        to_check = self.filter(*args, **kwargs) if len(args) else self
        return self.T(any)


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
    

class ChainedIt(ChainedCombinators, It):
    pass
