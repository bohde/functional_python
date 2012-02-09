from functools import wraps
from itertools import takewhile


class Combinators(object):
    def __init__(self, value):
        self._value = value


    def K(self, f, *args, **kwargs):
        """The Kestrel combinator, invokes a method, and returns the original value"""
        if callable(f):
            f(self._value, *args, **kwargs)
        else:
            getattr(self._value, f)(*args, **kwargs)
        return self._value
    

    def T(self, function, *args, **kwargs):
        """The Thrush combinator, makes a function call look like a method"""
        return function(self._value, *args, **kwargs)


    def R(self, function, *args, **kwargs):
        """The Robin combinator, like the thrust, except appends to the end of the argument list"""
        return function(*(args + (self._value,)), **kwargs)


    def chain(self):
        return ChainedCombinators(self._value)


class ChainedCombinators(object):
    def __init__(self, value):
        self._value = value

        
    def K(self, f, *args, **kwargs):
        """The Kestrel combinator, invokes a method, and returns the original value"""
        if callable(f):
            f(self._value, *args, **kwargs)
        else:
            getattr(self._value, f)(*args, **kwargs)
        return self
    

    def T(self, function, *args, **kwargs):
        """The Thrush combinator, makes a function call look like a method"""
        return self.__class__(function(self._value, *args, **kwargs))


    def R(self, function, *args, **kwargs):
        """The Robin combinator, like the thrust, except appends to the end of the argument list."""
        return self.__class__(function(*(args + (self._value,)), **kwargs))


    def value(self):
        return self._value


def bw(value):
    return Combinators(value)


def fluent_combinator_style(xs):
    return bw(xs).chain()\
                 .R(takewhile, lambda x: x < 7)\
                 .R(filter, lambda x: x < 2)\
                 .R(map, lambda x: 4 * x)\
                 .value()
    
assert fluent_combinator_style(range(10)) == [0, 4]


