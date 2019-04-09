#!/usr/bin/env python3

'''
Usage: At beginning of program, add the line:

    from nur.RNG import random
    
This will create an instance of the RNG using the current unix time as 
the starting seed. Generating a random number is then as easy as calling

    random.rand()

To define your own seed, use

    from nur.RNG import RNG
    random = RNG(seed)
    random.rand()
'''

import time


class Singleton:
    '''
    Implementation of singleton class comes from Alex Martelli's 'Borg':
    http://www.aleax.it/Python/5ep.html
    '''
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state




class RNG(Singleton):

    def __init__(self, seed=1):
        ''' Random Number Generator '''
        Singleton.__init__(self)

        if seed <= 0:
            raise ValueError('Starting seed must be greater than 0')
        
        self.seed = int(seed)
        self.state = int(seed)
        self.max = (2**64)-1   # maximum value (64 bits)


    def rand(self):
        '''
        Generate a random value between 0 and 1 using a combination 
        of a multiplicative linear congruential generator and a 
        64-bit XOR-shift.
        
        Values for the multipliers taken from Press et al. (2007)
        '''

        # MLCG
        a = 3935559000370003845
        c = 2691343689449507681
        
        self.state = (a * self.state + c) % self.max
    
        # XOR shift
        self.state ^= (self.state >> 21) & self.max
        self.state ^= (self.state << 35) & self.max
        self.state ^= (self.state >> 4)  & self.max
    
        return self.state / self.max
    
    
    def rand_range(self, lower, upper):
        '''
        Generate a random number within a range
        
        '''
        return lower + (random.rand() * (upper-lower))
    

# random seed from current unix time
random = RNG(time.time())
