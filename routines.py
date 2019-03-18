#!/usr/bin/env python3

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