#!/usr/bin/env python3

import numpy as np

from nur.RNG import random


def rejection(f, n, xrange=(0,1), yrange=(0,1)):
    '''
    Rejection sampling
    
    Parameters
    ----------
    f : function
        The function being sampled
    n : int
        The number of samples to draw
    xrange : (float, float) (default: (0,1))
        The range of x values to sample from
    yrange : (float, float) (default: (0,1))
        The range of y values to sample from
    
    Returns
    -------
    values : array (N, 2)
        An array with the (x, y) sampled pairs. The length
        N <= n is the number of samples in which y < f(x)
    '''
    
    values = []
    
    while len(values) < n:
        x = random.rand_range(xrange[0], xrange[1])
        y = random.rand_range(yrange[0], yrange[1])
        
        if y < f(x):
            values.append((x,y))
            
    return np.array(values)


def spherical(n):
    '''
    Sample values randomly from the surface of a sphere
    '''
    
    values = []
    
    for _ in range(n):
        theta = 2 * np.pi * random.rand()
        phi = np.arccos(1 - 2*random.rand())
        values.append((theta, phi))
    
    return np.array(values)
