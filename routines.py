#!/usr/bin/env python3

import numpy as np  # only for arrays


def switch(a, b):
    ''' switch the values of a and b '''
    return b, a


def magnitude(a):
    ''' get the magnitude of a number '''
    if a < 0:
        a *= -1

    return a


def sign(a):
    ''' get the sign of a number (-1, 0, or 1) '''
    return (a>0) - (a<0)


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


def find_closest(points, value):
    '''
    Find the index and nearest value in an array
    
    Example
    -------
    points = [1, 5, 10, 2, 8]
    value = 2.3
    print(find_closest(points, value))
    # (3, 2)
    # 2 is the value closest to 2.3 and is at index 3
        
    Parameters
    ----------
    points : list-like
        list of values to search
    value : float
        value to find in points
    
    Returns
    -------
    (index, closet_val) : (int, float)
        The index and closest value found in the array
    '''
    
    index = np.argmin(np.abs(np.array(points) - value))
    closest_val = points[index]
    
    return (index, closest_val)
