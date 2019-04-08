#!/usr/bin/env python3

import numpy as np  # only for arrays


def switch(a, b):
    '''
    Switch the values of a and b
    
    Ex:
        a=1; b=2
        a, b = switch(a, b)
        print(a) # 2
        print(b) # 1
    '''
    return b, a


def mean(array):
    '''
    Calculate the mean of a 1D array
    '''
    return sum(array) / len(array)


def median(array):
    '''
    Calculate the median of a 1D array

    Note: the array should be sorted
    '''
    return percentile(array, .5)


def percentile(array, k):
    '''
    Find the `k`th percentile of a 1D array.

    Note: the array should be sorted
    '''
    assert(k>=0 and k<=1)
    index = len(array)*k
    if index % 1 == 0.:         # if not a whole number
        index = int(index)+1    # round up to the nearest whole number
        return array[index]

    return mean([array[index], array[index+1]])


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
