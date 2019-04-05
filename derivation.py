#!/usr/bin/env python3

import numpy as np



def central(f, x, dx=1e-6):
    ''' 
    derivation via the central differences formula 
    
    TODO: error estimation (eps = h^2 f'")
    '''
    return (f(x+dx) - f(x-dx))/(2*dx)


def ridders(f, x, dx=1e-6):
    ''' 
    derivation with Ridder's method 
    
    TODO: do this
    '''
    
    pass