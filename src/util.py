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

def is_in_bounds(elem_sz, pos, cont_sz):
    """Determine if a rectangle is completely inside another rectangle.

    elem_sz ((int,int)): The (w,h) dimensions of the inner rectangle.
    pos ((int,int)): The (x,y) coords of the inner rectangle.
    cont_sz ((int,int)): The (w,h) dimensions of the outer rectangle (container).
    """
    (elem_w,elem_h) = elem_sz
    (x,y) = pos
    (cont_w,cont_h) = cont_sz
    # Make sure it's not too high or too far left.
    if x < 0 or y < 0: return False
    # Make sure it's not too low or too far right.
    if x > (cont_w - elem_w) or y > (cont_h - elem_h): return False
    return True
