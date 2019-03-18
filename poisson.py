#!/usr/bin/env python3

import numpy as np  # only for exp()


def poisson(mu, k):
    '''
    Calculate the value k for a Poisson distribution with mean mu.
        
    Parameters
    ----------
    mu : positive float
        The mean of the distribution
    k : positive int
        The number of times an event occurs
    '''
    if mu < 0:
        raise ValueError('Negative value passed for mu')
    if k < 0:
        return 0 
    
    # TODO is it possible to calculate the factorial without a loop?
    k_fact = 1
    for value in range(1, k+1):
        k_fact *= value 
    
    return (mu**k * np.exp(-mu)) / k_fact


if __name__=='__main__':

    for mu, k in [(1, 0), (5, 10), (3, 20), (2.6, 40)]:
        print('P(%s, %s) = %.6f' %(mu, k, poisson(mu, k)))