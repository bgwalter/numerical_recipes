#!/usr/bin/env python3

import numpy as np

import routines as rt


def golden(f, a, b, eps=1e-8):
    '''
    Find the minimum of a function using golden function search

    This algorithm was taken from wikipedia
    https://en.wikipedia.org/wiki/Golden-section_search#Algorithm

    (sorry if that's not allowed - I really don't know how I can change this so
    it's not just the exact same algorithm)
    '''

    # ensure that f(b) < f(a)
    assert(a != b)
    if f(a) < f(b):
        a, b = rt.switch(a, b)

    # find two new points between c and d
    golden_ratio = 1.618
    c = b - (b-a) / golden_ratio
    d = a + (b-a) / golden_ratio

    # iteratively tighten the bracket around the function minimum
    while abs(c-d) > eps:
        if f(c) > f(d):
            b = d
        else:
            a = c

        c = b - (b-a) / golden_ratio
        d = a - (b-a) / golden_ratio

    # minimum is in the middle of the bracket
    return (b+a)/2
