#!/usr/bin/env python3

'''
Usage: At beginning of program, add the line:

    from nur.RNG import random
    
This will create an instance of the RNG using the current unix time as the 
starting seed. Generating a random number is then as easy as calling

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

    def __getattr__(self):
        return getattr(self.instance)

            
    def rand(self):
        '''
        Generate a random value between 0 and 1 using a combination of a 
        multiplicative linear congruential generator and a 64-bit XOR-shift.
        
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

    
if __name__ == '__main__':

    import matplotlib.pyplot as plt

    
    print('Seed is %s' %random.seed)
    
    rand = [random.rand() for _ in range(int(1e6+1))]
    x, y = rand[:-1], rand[1:]

    plt.figure(figsize=(4,4))
    plt.scatter(x[:1000], y[:1000], alpha=.5, marker='.')
    plt.savefig('output/RNG_scatter.png')

    
    plt.figure(figsize=(5,4))
    im = plt.hist2d(x, y, bins=20, cmap='Blues')
    plt.colorbar(im[3])
    plt.savefig('output/RNG_hist2d.png')
