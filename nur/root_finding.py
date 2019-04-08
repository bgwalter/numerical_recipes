#!/usr/bin/env python3

import nur.routines as rt


def bisect(f, a, b, eps=1e-4, maxiter=50):
    '''
    Find the root via bisection

    Parameters
    ----------
    f : function
        The function for which the roots are found
    a : float
        x value to the left of the root
    b : float
        y value to the right of the float
    eps : float (default: 1e-4)
        Stop once the difference between `a` and `b` becomes smaller than
        this value
    maxiter : int (default: 50)
        Stop after this many iterations if the method fails to converge
        fast enough

    Returns
    -------
    c : float
        The location on the x axis where f(x) = 0
    '''

    # ensure there is a root between a and b
    assert(f(a)*f(b) < 0)

    # ensure a is less than b
    assert(a != b)
    if a > b:
        a, b = rt.switch(a, b)

    delta = abs(b-a)

    i = 0
    while (delta > eps) and i<=maxiter:

        # calculate midpoint between a and b
        c = a + delta/2

        if f(a)*f(c) < 0: 
            b = c  # root is between a and c
        elif f(b)*f(c) < 0:
            a = c  # root is between b and c

        # update delta to the new values of a and b
        delta = abs(b-a)

        i += 1

    return c
