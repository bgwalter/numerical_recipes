#!/usr/bin/env python3

import numpy as np


def trapezoid(f, a, b, N=10000000):
    '''
    Integral approximation via the trapezoid rule
    '''
    h = (b-a)/N
    x = np.linspace(a, b, N)
    
    y = (f(a) + f(b))/2
    y += np.sum(f(x))
    
    return h*y


def simpson(f, a, b, N=10000000):
    '''
    Integral approximation via Simpson's rule
    '''
    h = (b-a)/N
    
    x = np.linspace(a, b, N)
    y = f(a) + f(b)
    
    y += np.sum(2*f(x[2::2]))
    y += np.sum(4*f(x[1::2]))
        
    return (h*y)/3


def spherical_integration(f, a, b):
    '''
    Integrate a function over 3 dimensions in spherical coordinates
    
        \int \int \int_V f(r) dV
    
    where dV = r^2 \sin \phi d\phi d\theta
    
    Thus
        
        4 \pi \int_a^b f(r) r^2
    '''
    
    # timing shows that simpson tends to be faster
    return 4 * np.pi * simpson(lambda r: f(r)*r**2, a, b)
    
    
if __name__=='__main__':
    
    # running some tests
    print('Triple integral to approximate the volume of a sphere (R=5):')
    print('\tApprox\t', spherical_integrator(lambda r: 1, 0, 5))
    print('\tReal\t', (4/3) * np.pi * 5**3)
