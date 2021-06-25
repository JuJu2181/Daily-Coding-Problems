"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""
# cons will always return a pair from a and b
def cons(a,b):
    # here pair takes an input function and then it will apply the given function to the pair
    def pair(f):
        return f(a,b)
    return pair 

def car(pair):
    return pair(lambda a,b:a)

def cdr(pair):
    return pair(lambda a,b:b)

print(cons(3,4)(lambda a,b:a))
print(car(cons(4,5)))
print(cdr(cons(4,5)))