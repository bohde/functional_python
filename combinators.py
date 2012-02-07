from functools import wraps
from itertools import takewhile


class Combinators(object):
    def __init__(self, value):
        self._value = value


    def K(self, f, *args):
        """The Kestrel combinator, invokes a method, and returns the original value"""
        if callable(f):
            f(self._value, *args)
        else:
            getatttr(self._value, function_name)(*args)
        return self._value
    

    def T(self, function, *args):
        """The Thrush combinator, makes a function call look like a method"""
        return function(self._value, *args)


    def R(self, function, *args):
        """The Robin combinator, like the thrust, except appends to the end of the argument list"""
        return function(*(args + (self._value,)))


    def chain(self):
        return ChainedCombinators(self._value)


class ChainedCombinators(object):
    def __init__(self, value):
        self._value = value

        
    def K(self, f, *args):
        """The Kestrel combinator, invokes a method, and returns the original value"""
        if callable(f):
            f(self._value, *args)
        else:
            getatttr(self._value, function_name)(*args)
        return self
    

    def T(self, function, *args):
        """The Thrush combinator, makes a function call look like a method"""
        return ChainedCombinators(function(self._value, *args))


    def R(self, function, *args):
        """The Robin combinator, like the thrust, except appends to the end of the argument list."""
        return ChainedCombinators(function(*(args + (self._value,))))


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


