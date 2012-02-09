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

    def reject(self, f, *args, **kwargs):
        return self.filter(lambda n: not(f(n)), *args, **kwargs)


    def find(self, *args, **kwargs):
        return next(self.filter(*args, **kwargs))


    def all(self, *args, **kwargs):
        if len(args):
            return all(self.filter(*args, **kwargs))
        return all(self._value)
        

    def any(self, *args, **kwargs):
        if len(args):
            return any(self.filter(*args, **kwargs))
        return any(self._value)
        

    def invoke(self,*args, **kwargs):
        return (i.K(*args, **kwargs) for i in self.map(It))

    
    def chain(self):
        return ChainedIt(self._value)
    

class ChainedIt(ChainedCombinators, It):
    pass
