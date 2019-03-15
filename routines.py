#!/usr/bin/env python3

# Brendon Walter (s2078864)
# 2019 March 15
# Numerical Recipes in Astrophysics

import numpy as np  # only for arrays


def mean(array):
    '''
    Calculate the mean of a 1D array
    '''
    return sum(array) / len(array)


def std(array):
    '''
    Calculate the standard deviation of a 1D array
    '''
    array = np.asarray(array)
    numer = sum((array - mean(array))**2)
    denom = len(array)
    
    return (numer / denom)**.5


def prod(array):
    '''
    Calculate the product of an array
    
        prod = x_i * x_{i+1} * ... * x_{N}
        
    TODO is there a way to do this without a for loop?
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
    return prod(range(1, k+1))


def corr_coef(x, y):
    '''
    Pearson correlation coefficient
    
        r_{xy} = (mean(xy) - mean(x)*mean(y)) / (std(x)*std(y))
        
    Parameters
    ----------
    x, y : list-like
        Correlation is found between these two lists. Should be the 
        same length.
        
    Returns
    -------
    r : float from -1 to 1
        The correlation between the inputs. -1 or 1 implies perfect
        correlation, while 0 implies no correlation.
    '''
    numer = mean(x*y) - mean(x)*mean(y)
    denom = std(x) * std(y)
    
    return numer/denom