__author__ = 'Dominic Gomez'
__email__ = 'DominicAnthonyGomez@gmail.com'

"""Miscellaneous functions that make life easier."""

import operator

def tupadd(lhs, rhs):
    """Componentwise addition of tuples.

    lhs ((int,int)): The first tuple.
    rhs ((int,int)): The second tuple.

    """
    return tuple(map(operator.add, lhs, rhs))
