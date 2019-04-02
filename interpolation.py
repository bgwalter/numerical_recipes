#!/usr/bin/env

import numpy as np
import routines as rt


def bisect(points, value):
    '''
    Use the bisection algorithm to find the closest points
    to a given value
    
    Parameters
    ----------
    points : list-like (1D)
        The list of the points from which you are interpolating
    value : float
        The point that you want interpolated
        
    Returns
    -------
    (left, right) : (float, float)
        The points closest to the interpolated point
    '''
    
    points = np.sort(points)
    n = len(points)
    
    left = points[:int(n/2)]
    right = points[int(n/2):]
    
    if value < left[0] or value > right[-1]:
        raise Exception('Value falls outside of given range')
    
    elif value < left[-1]: return bisect(left, value)
    elif value > right[0]: return bisect(right, value)
    else: return (left[-1], right[0])


def linear(x, y, xinterp):
    '''
    Linear interpolation
    
    Parameters
    ----------
    x, y : float, float
        The known data points in x and y
    xinterp : list (1D)
        The list of x values to be interpolated
    
    Returns
    -------
    yinterp : list (1D)
        An array holding the values of the interpolated y 
        values for each xinterp passed to the function
    '''
    
    x, y = np.array(x), np.array(y)
    xinterp = np.sort(xinterp)
    yinterp = []
    
    for xval in xinterp:
        
        #find the neighboring points
        xlow, xhigh = bisect(x, xval)
        
        # get the index of the neighboring points
        ilow =  rt.find_closest(x, xlow)[0]
        ihigh = rt.find_closest(x, xhigh)[0]
        
        # get y values of the neighboring points
        ylow, yhigh = y[ilow], y[ihigh]
    
        slope = (yhigh - ylow) / (xhigh - xlow)
        
        yinterp.append(slope * (xval - xhigh) + yhigh)
        
    return np.array(yinterp)


def polynomial(x, y, xinterp):
    '''
    Polynomial interpolation via Neville's algorithm

    Parameters
    ----------
    x, y : float, float
        The known data points in x and y
    xinterp : list (1D)
        The list of x values to be interpolated

    Returns
    -------
    yinterp : list (1D)
        An array holding the values of the interpolated y
        values for each xinterp passed to the function
    '''
    M = len(x)
    yinterp = []
    for xval in xinterp:
        P = np.zeros((M, M))
        P[:, 0] = y
        for i in range(1, M):
            for j in range(1, i+1):

                A = (xval - x[i-j]) * P[i,   j-1]
                B = (xval - x[i])   * P[i-1, j-1]
                C = (x[i] - x[i-j])

                P[i,j] = (A - B) / C

        yinterp.append(P[-1,-1])

    return yinterp
