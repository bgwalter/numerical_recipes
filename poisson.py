#!/usr/bin/env python3

# Brendon Walter (s2078864)
# 2019 March 15
# Numerical Recipes in Astrophysics

import numpy as np  # only for exp()

from routines import factorial


def poisson(l, k):
    '''
    Calculate the value k for a Poisson distribution with mean l
    
        P(k) = l^k e^{-l} / k!
        
    Parameters
    ----------
    l : positive float
        The mean of the distribution
    k : positive int
        The number of times an event occurs
    '''
    if l < 0:
        raise ValueError('Negative value passed for lambda')
    if k < 0:
        return 0 
    
    return (l**k * np.exp(-l)) / factorial(k)


if __name__=='__main__':

    for l, k in [(1, 0), (5, 10), (3, 20), (2.6, 40)]:
        print('P(%s, %s) = %.6f' %(l, k, poisson(l, k)))