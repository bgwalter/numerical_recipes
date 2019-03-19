#!/usr/bin/env python3

from RNG import random

print('Random seed is', random.seed)


# 2. a)

a = random.randint(1.1, 2.5)
b = random.randint(0.5, 2)
c = random.randint(1.5, 4)

Nsat = 100
A = 1  # TODO

gal_profile = lambda x: A*Nsat * (x/b)**(a-3) * np.exp(-(x/b)**c)
