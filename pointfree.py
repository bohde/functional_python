
# Let's examine a simple imperative script
def imperative_style(xs):
    results = []
    for x in xs:
        if x >= 7: 
            break
        if x < 2:
            result = 4 * x
            results.append(result)
    return results

# Let's add a sanity check, since we're going
# to refactor this version
assert imperative_style(range(10)) == [0, 4]

# Whenever I see code like the above `imperative_style`, 
# I mentally file it as point of possible complexity and bugs,
# especially as requirements change and more logic
# is tacked on. 

# As a comparison, let's look at a simple functional version
# First, we're going to need `takewhile` from itertools, 
# which will allow us to build something like the `break` statement
from itertools import takewhile

# And now the functions definition, utilized two
# builtins, `map` and `filter`, as well as `takewhile`
# to break the problem down into logically independent parts
# notice that the conditional in the `takewhile` is inverted
def functional_style(xs):
    return map(lambda x: 4 * x,
               filter(lambda x: x < 2,
                      takewhile(lambda x: x < 7, xs)))

assert functional_style(range(10)) == [0, 4]

# There are less moving parts here,
# but it seems too much like a  Christmas tree for me. 
# Can we make it flatter?

# For this, we're going to need more tools for working with 
# functions. First is compose, which let's us feed the result
# of one function as the argument of another.

# I'm always surprised that Python doesn't have this builtin. 
# In more functional languages this is a basic feature, with
# Haskell making it one character (`.`)
def compose_two(g, f):
    """Function composition for two functions, e.g. compose_two(f, g)(x) == f(g(x))"""
    return lambda *args, **kwargs: g(f(*args, **kwargs))

assert compose_two(lambda x: x * 2,
                   lambda y: y + 4)(1) == 10

def compose(*funcs):
    """Compose an arbitrary number of functions left-to-right passed as args"""
    return reduce(compose_two, funcs)


# With compose, we need one more function, `partial`,
# which can be used to provice only some of a function's
# arguments
from functools import partial
composition_style = compose(
    partial(map, lambda x: 4 * x),
    partial(filter, lambda x: x < 2),
    partial(takewhile, lambda x: x < 7))

assert composition_style(range(10)) == [0, 4]


# There's a quite a bit of boilerplate
# in this definition.
# Can we abstract out a reusable pattern? 
from itertools import starmap
def composed_partials(*partial_funcs):
    return compose(*starmap(partial, partial_funcs))

composed_partials_style = composed_partials(
    (map, lambda x: 4 * x),
    (filter, lambda x: x < 2),
    (takewhile, lambda x: x < 7))

assert composed_partials_style(range(10)) == [0, 4]


# This is less noisy, but it's a bit difficult to
# read the logic in reverse order. Can we change that? 
def pipe(*partial_funcs):
    return composed_partials(*reversed(partial_funcs))


pipe_style = pipe(
    (takewhile, lambda x: x < 7),
    (filter, lambda x: x < 2),
    (map, lambda x: 4 * x))

assert pipe_style(range(10)) == [0, 4]


# This definition is more dataflow oriented, much
# like using pipes in a shell, or Clojure's `->` macro. 


# Looking at the definition for composed_partials and pipe, 
# they follow a similar structure. 
# Can we extract that out? 
def transform_args(func, transformer):
    return lambda *args: func(*transformer(args))

composed_partials = transform_args(compose, partial(starmap, partial))
pipe = transform_args(composed_partials, reversed)

assert composed_partials_style(range(10)) == [0, 4]
assert pipe_style(range(10)) == [0, 4]
