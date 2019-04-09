#!/usr/bin/env python3

import numpy as np

import nur.routines as rt


def poisson(mu, k):
    '''
    Calculate the value k for a Poisson distribution with mean mu.
        
    Parameters
    ----------
    mu : unsigned np.float64
        The mean of the distribution
    k : np.int64
        The number of times an event occurs (should be >0)
    '''
    if mu < 0:
        raise ValueError('Negative value passed for mu')
    if k < 0:
        return 0 

    mu = np.float64(mu)
    k = np.int64(k)
    
    return (mu**k * np.exp(-mu)) / rt.prod(range(1, k+1))
