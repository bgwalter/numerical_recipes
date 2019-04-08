#!/usr/bin/env python3

import numpy as np

from RNG import random
import integration as integ


class GalaxyProfile:
    
    def __init__(self, Nsat=100, a=None, b=None, c=None):
        self.a = a if a is not None else random.rand_range(1.1, 2.5)
        self.b = b if b is not None else random.rand_range(0.5, 2)
        self.c = c if c is not None else random.rand_range(1.5, 4)
        
        self.Nsat = Nsat
        self.A = self.normalize()
        
        
    def normalize(self, Nsat=None):
        '''
        Find the normalization factor A such that 
        
            4 \pi \int_0^5 n(x) x^2 = <Nsat>
        '''
        if Nsat is None:
            Nsat = self.Nsat
            
        self.A = self.Nsat / integ.spherical_integration(self.dist, 1e-4, 5)
        return self.A
    
    
    def dist(self, x):
        return (x/self.b)**(self.a-3) * np.exp(-(x/self.b)**self.c)
    
    
    def log_dist(self, x):
        return np.log10(self.dist(x))
        
        
    def n(self, x):
        return self.dist(x) * self.A
    
    
    def logn(self, x):
        return self.log_dist(x) * self.A
    
    
    def __str__(self):
        s = 'Profile of satellite galaxies:\n' + \
            'Parameters:\n' + \
            '\ta = %.4f\tb = %.4f\tc = %.4f\tA = %.4f' \
            %(self.a, self.b, self.c, self.A)
        return s
