#!/usr/bin/env python3

# Brendon Walter (s2078864)
# 2019 March 15
# Numerical Recipes in Astrophysics

import matplotlib.pyplot as plt


class RNG:
    
    ''' Use a combination of (M)LCG and 64-bit XOR shift'''
    
    def __init__(self, seed=1):
        self.seed = seed
        self._prev = seed
    
    
    def randint(self):
        '''
        Generate a random integer
        '''
        pass
    
    
    def rand(self):
        '''
        Generate a random number between 0 and 1
        '''
        pass
    
    
    def _test_scatter(self, n=1000):

        plt.scatter([self.rand() for _ in range(n),
                     self.rand() for _ in range(n)])
        
        plt.show()
        
        
    def _test_his2d(self, bins=20, width=0.05):
        
        plt.hist2d([self.rand() for _ in range(n),
                    self.rand() for _ in range(n)],
                    bins=bins, rwdith=width)
        
        plt.show()
        