#!/usr/bin/env python3

'''
Usage: At beginning of program, add the line:

    from RNG import random
    
This will create an instance of the RNG using the current unix time as
a starting seed. Generating a random number is then as easy as calling

    random.rand()
    
'''
import time


class RNG:
    
    def __init__(self, seed=1):
        ''' 
        Random Number Generator 
        '''
        if seed <= 0:
            raise ValueError('Starting seed must be greater than 0')
            
        self.seed = int(seed)
        self.state = int(seed)
    
    
    def rand(self):
        '''
        Generate a random value between 0 and 1 using a combination of a 
        multiplicative linear congruential generator and a 64-bit XOR-shift.
        
        Values for the multipliers taken from Press et al. (2007)
        '''

        # MLCG
        a = 3935559000370003845
        c = 2691343689449507681
        m = 2**64-1
        
        self.state = (a * self.state + c) % m
    
        # XOR shift
        self.state ^= (self.state >> 21) & m
        self.state ^= (self.state << 35) & m
        self.state ^= (self.state >> 4)  & m
    
        return self.state / m 
    
    
    def rand_range(self, lower, upper):
        '''
        Generate a random number within a range
        
        Method found from:
        https://www.geeksforgeeks.org/generating-random-number-range-c/
        '''
        return (self.rand() % (upper - lower + 1)) + lower
        

# use current unix time as a seed
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
