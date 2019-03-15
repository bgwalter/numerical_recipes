#!/usr/bin/env python3

# Brendon Walter (s2078864)
# 2019 March 15
# Numerical Recipes in Astrophysics

import numpy as np
import matplotlib.pyplot as plt

from scipy import stats

import routines


class RNG:
    
    def __init__(self, seed=1):
        ''' 
        Random Number Generator 
        '''
        if seed <= 0:
            raise ValueError('Starting seed must be greater than 0')
            
        self.seed = seed
        self.state = seed
    
    
    def rand(self):
        '''
        Generate a random value between 0 and 1 using a combination of 
        a multiplicative linear congruential generator:
        
            x_{j+1} = a * x_{j} + c (mod m)
        
        and a 64-bit XOR-shift:
        
            x_{j+1} = x_{j} ^ (x_{j} >> a1)
            x_{j+1} = x_{j} ^ (x_{j} << a2)
            x_{j+1} = x_{j} ^ (x_{j} >> a3)
            
        Values for the multipliers taken from Press et al (2007)
        '''
        
        x = self.state

        # MLCG
        a = 3935559000370003845
        c = 2691343689449507681
        m = 2**64
        
        x = (a * x + c) % m
    
        # XOR shift
        x ^= (x >> 21)
        x ^= (x << 35)
        x ^= (x >> 4)
    
        self.state = x
    
        return self.state / 6.34e29 # TODO why this value?
    
    def rand_range(self, lower, upper):
        # https://www.geeksforgeeks.org/generating-random-number-range-c/
        return (self.rand() % (upper - lower + 1)) + lower
        
    
if __name__ == '__main__':

    rng = RNG(42)
    
    print('Seed is %s' %rng.seed)
    
    x = np.array([rng.rand() for _ in range(1000000)])
    y = np.array([rng.rand() for _ in range(1000000)])
    

    plt.figure(figsize=(4,4))
    
    plt.scatter(x[:1000], y[:1000], alpha=.5, marker='.')
    
    plt.title('r = %.4f' %routines.corr_coef(x, y))

    plt.show()
    
    
    plt.figure(figsize=(5,4))
    
    im = plt.hist2d(x, y, bins=20)
    plt.colorbar(im[3])
    
    plt.title('r = %.4f' %routines.corr_coef(x, y))

    plt.show()
