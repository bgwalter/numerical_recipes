#!/usr/bin/env python3

import numpy as np

from RNG import random
import integration as integ
import derivation as deriv


class GalaxyProfile:

    def __init__(self, Nsat=100, a=None, b=None, c=None):
        '''
        Create a number density profile of satellite galaxies in a 
        dark matter halo:

            n(x) = A <Nsat> (x/b)^(a-3) exp[-(x/b)^c]

        where x is the radius relative to the virial radius x = r/r_vir

        If the free parameters a, b, and c are not provided, random values are 
        assigned.

        Parameters
        ----------
        Nsat : int (optional)
            The number of galaxies
        a : float (optional)
            Controls the small-scale slope
        b : float (optional)
            Controls the transition scale
        c : float (optional)
            Controls the steepness of the exponential dropoff     
        '''
        self.a = a if a is not None else random.rand_range(1.1, 2.5)
        self.b = b if b is not None else random.rand_range(0.5, 2)
        self.c = c if c is not None else random.rand_range(1.5, 4)
        
        self.Nsat = Nsat
        self.A = self.normalize()
        
        
    def normalize(self, Nsat=None):
        '''
        Find the normalization factor A such that 
        
            4 pi \int_0^5 n(x) x^2 = <Nsat>
        '''
        if Nsat is None:
            Nsat = self.Nsat
            
        self.A = self.Nsat / integ.spherical_integration(self.dist, 1e-4, 5)
        return self.A
    
    
    def dist(self, x):
        ''' unormalized distriubtion '''
        return (x/self.b)**(self.a-3) * np.exp(-(x/self.b)**self.c)
    
    def logdist(self, x):
        ''' log of the unormalized distribution '''
        return np.log10(self.dist(x))
        
    def n(self, x):
        ''' the normalized number density profile '''
        return self.dist(x) * self.A
    
    def logn(self, x):
        ''' the log of the normalized number density profile '''
        return self.logdist(x) * self.A

    def dn(self, x):
        ''' the derivative of the profile at radius x '''
        return deriv.central(self.n, x)

    def probability(self, x):
        ''' 
        the probability distribution
       
            p(x) dx = 4 pi x^2 n(x) dx 
        '''
        return 4 * np.pi * x**2 * self.n(x) / self.Nsat

    
    def __str__(self):
        return 'Nsat=%s     a = %.4f     b = %.4f     c = %.4f    A = %.4f' \
                %(self.Nsat, self.a, self.b, self.c, self.A)
