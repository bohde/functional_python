
# Let's examine a simple imperative script
def imperative(xs):
    results = []
    for x in xs:
        if x > 7: 
            break
        if x < 2:
            result = 4 * x
            results.append(result)
    return results

# Let's test it
assert imperative(range(10)) == [0, 4]


# Let's look at a simple functional version
from itertools import takewhile
def functional(xs):
    return map(lambda x: 4 * x,
               filter(lambda x: x < 2,
                      takewhile(lambda x: x < 7, xs)))

assert functional(range(10)) == [0, 4]


# That seems too Christmas tree like for me. 
# Can we make flatter?

def compose_two(g, f):
    """Function composition for two functions, e.g. compose_two(f, g)(x) = f(g(x))"""
    return lambda *args, **kwargs: g(f(*args, **kwargs))

assert compose_two(lambda x: x * 2,
                   lambda y: y + 4)(1) == 10

def compose(*funcs):
    """Compose an arbitrary number of functions passed as args"""
    return reduce(compose_two, funcs)

from functools import partial
composition_style = compose(
    partial(map, lambda x: 4 * x),
    partial(filter, lambda x: x < 2),
    partial(takewhile, lambda x: x < 7))

assert composition_style(range(10)) == [0, 4]


# Still seems like too much boiler plate.
# Can we abstract this out? 

from itertools import starmap
def point_free(*partial_funcs):
    return compose(*starmap(partial, partial_funcs))

point_free_style = point_free(
    (map, lambda x: 4 * x),
    (filter, lambda x: x < 2),
    (takewhile, lambda x: x < 7))

assert point_free_style(range(10)) == [0, 4]


# It's a bit difficult to read the logic in reverse order, can we fix that? 

def rcompose(*funcs):
    """Compose an arbitrary number of functions passed as args, but in reverse order"""
    return reduce(compose_two, reversed(funcs))

def rpoint_free(*partial_funcs):
    return rcompose(*starmap(partial, partial_funcs))

rpoint_free_style = rpoint_free(
    (takewhile, lambda x: x < 7),
    (filter, lambda x: x < 2),
    (map, lambda x: 4 * x))

assert rpoint_free_style(range(10)) == [0, 4]
