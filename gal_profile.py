#!/usr/bin/env python3

from RNG import random


class GalaxyProfile:
    
    def __init__(self, Nsat=100, a=None, b=None, c=None):
        self.a = a if a is not None else random.randint(1.1, 2.5)
        self.b = b if b is not None else random.randint(0.5, 2)
        self.c = c if c is not None else random.randint(1.5, 4)
        
        self.Nsat = Nsat
        self.A = 1  # TODO
        
        
    def n(self, x):
        norm = self.A * self.Nsat
        dist = (x/self.b)**(self.a-3) * np.exp(-(x/self.b)**self.c)
        return norm*dist
    
    
    def n_log(self, x):
        pass