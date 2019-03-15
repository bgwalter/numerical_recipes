#!/usr/bin/env python3

# Brendon Walter (s2078864)
# 2019 March 15

# Numerical Recipes in Astrophysics

import numpy as np  # only for arrays and exp()!


def prod(array):
    '''
    Calculate the product of a list
    
        prod = x_i * x_{i+1} * ... * x_{N}
    '''
    total = 1
    for value in array:
        total *= value
        
    return total


def factorial(k):
    '''
    Calculate the factorial
    
        k! = k * (k-1) * ... * 1
    '''
    return prod(np.arange(1, k+1))


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
    
    return (l**k * np.exp(-l)) / factorial(k)


if __name__ == '__main__':
    
    # check prod() and factorial()
    assert(factorial(5) == 120)
    
    # check poisson()
    assert(round(poisson(1, 0), 3) == 0.368)
    assert(round(poisson(1, 6), 4) == 0.0005)