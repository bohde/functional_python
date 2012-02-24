# As a simple demo of pure functional programming, 
# let's do some math using only functions

# We encode numbers so that a number `n`
# is the following function, lambda f: lambda x: f^n(x),
# where f is a function, and x is some value

# `zero` would apply f to x zero times, so would just return x
zero = lambda f: lambda x: x

# And `one` would apply f to x one time, so would return f(x)
one = lambda f: lambda x: f(x)

# In order to decode a given number, n, 
# we need to provide f, and x.
# f needs to be the transistion function between two numbers,
# the addition of 1, and x needs to be the results of zero applications
# of f, which is 0
unchurch = lambda n: n(lambda m: m + 1)(0)

# Let's do some sanity testing
assert unchurch(zero) == 0
assert unchurch(one) == 1

# To get the next number, the "successor", 
# we just call `f` one more time around the encoded value
succ = lambda n: lambda f: lambda x: f(n(f)(x))

# We're going to manipulate these, so let's make a 
# helper function to determine equality
def equals(x, y):
    assert unchurch(x) == unchurch(y)

equals(succ(zero), one)

# Let's define some more constants for easier reading
two = succ(one)
three = succ(two)
four = succ(three)
five = succ(four)
six = succ(five)

# Given that f is the transition function, 
# m + n would be the m applications of f to n
plus = lambda m: lambda n: lambda f: lambda x: m(f)(n(f)(x))

equals(plus(two)(three), five)

# Multiplication of m * n would be would be m applications of 
# n applications of f
mult = lambda m: lambda n: lambda f: lambda x: m(n(f))(x)

equals(mult(two)(three), six)

# Exponenets of m^n would be the multiplication of m applied n times. 
exp = lambda m: lambda n: n(mult(m))(one)

equals(exp(two)(two), four)
