#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

import nur.routines as rt
from nur.RNG import RNG

random = RNG(11)
print('Random seed is', random.seed)


def write(path, text):
    ''' for easy printing and writing into a file '''
    print('\t%s' %text)
    with open(path, 'w') as f:
        f.write(str(text))

start = time.time()

''' 1 a)
Write a function that returns P_λ(k). When your code is run, output P_λ(k) to 
at least six significant digits for these values: (λ, k) = (1, 0), (5, 10), 
(3, 21) and (2.6, 40).
'''
print('1 a) poisson')

from nur.poisson import poisson

s = ''
for mu, k in [(1, 0), (5, 10), (3, 21), (2.6, 40)]:
    s += 'P(%s, %s) = %.6f\t' %(mu, k, poisson(mu, k))

write('output/1a_poisson.txt', s)


''' 1 b)
Write a random number generator that returns a random floating-point number 
between 0 and 1. At minimum, use some combination of an (M)LCG and a 64-bit XOR-
shift. We’ll test its quality: like in the tutorial, have your code plot 
sequential random numbers against each other in a scatter plot (xi+1 vs xi) for 
the first 1000 numbers generated. Additionally, have your code generate 
1,000,000 random numbers and plot the result of binning these in 20 bins 0.05 
wide. Change your RNG parameters if necessary.
'''
print('1 b) RNG')

rand = [random.rand() for _ in range(int(1e6+1))]
x, y = rand[:-1], rand[1:]

# scatter plot
plt.figure(figsize=(4,4))
plt.scatter(x[:1000], y[:1000], alpha=.5, marker='.')
plt.savefig('output/1b_RNG-scatter.png')
plt.clf()

# 2d histogram
plt.figure(figsize=(5,4))
im = plt.hist2d(x, y, bins=20, cmap='Blues')
plt.colorbar(im[3])
plt.savefig('output/1b_RNG-hist2d.png')
plt.clf()


''' 2 a) 
Have your code randomly generate three numbers 1.1 < a < 2.5, 0.5 < b < 2 
and 1.5 < c < 4. Write a numerical integrator to solve for A given those three 
parameters, taking <Nsat> = 100. Output the numbers a, b, c and A.
'''
print('2 a) Setting up galaxy profile') 

from nur.gal_profile import GalaxyProfile

dist = GalaxyProfile()
write('output/2a.txt', dist.__str__())


''' 2 b)
Make a log-log plot of and plot single points for n(10^−4), n(10^−2 ), 
n(10^−1), n(1) and n(5) with an axis range from x = 10^−4 to xmax = 5. 
Interpolate the values in between based on just these points – make sure to 
argue in the comments of your code why you chose to interpolate in a certain 
way.
'''
print('2 b) interpolation')

import nur.interpolation as interp

xmin, xmax = 1e-4, 5

# true values for x and y
truex = np.linspace(xmin, xmax, 100)
logtruex = np.log10(truex)
logtruey = dist.logn(truex)

# the data points
datax = np.array([1e-4, 1e-2, 1e-1, 1, 5])
logdatax = np.log10(datax)
logdatay = dist.logn(datax)

# the x points to be interpolated
xinterp = np.linspace(xmin, xmax, 100)
logxinterp = np.log10(xinterp)

# interpolation via two different methods
loglinear = interp.linear(logdatax, logdatay, logxinterp)
logpoly = interp.polynomial(logdatax, logdatay, logxinterp)

# plot results
plt.plot(logtruex, logtruey, lw=5, alpha=.3, label='true')
plt.scatter(logdatax, logdatay, c='k', marker='x', label='data')

plt.plot(logxinterp, loglinear, lw=2, linestyle='dashed', label='linear')
plt.plot(logxinterp, logpoly, lw=2, linestyle='dotted', label='polynomial')

plt.xlabel('$\log_{10}(x)$')
plt.ylabel('$\log n(x)$')

plt.legend(loc='lower left')
plt.savefig('output/2b_interpolation.png')
plt.clf()


''' 2 c)
Numerically calculate dn(x)/dx at x = b. Output the value found alongside the 
analytical result, both to at least 12 significant digits. Choose your 
algorithm such as to get them as close as possible.
'''
print('2 c) derivative')

write('output/2c_derivative.txt', dist.dn(dist.b))
#TODO analytical derivation


''' 2 d)
Now we want to generate 3D satellite positions such that they statistically 
follow the satellite profile in equation (2); that is, the probability 
distribution of the (relative) radii x ∈ [0, xmax) should be p(x) dx = n(x)4πx2 
dx/<Nsat> (with the same a, b and c as before). Use one of the methods 
discussed in class to sample this distribution. Additionally, for each galaxy 
generate random angles φ and θ such that the resulting positions are 
(statistically) uniformly distributed as a function of direction. Output the 
positions (r, φ, θ) for 100 such satellites.
'''
print('2 d) generating 3D positions')

import nur.sampling as samp

# sample along r
r = samp.rejection(dist.probability, 100, xrange=(xmin, xmax), yrange=(0, 4)).T

plt.plot(truex, dist.probability(truex),  lw=5, alpha=.8)
plt.scatter(r[0], r[1], marker='.')

plt.xlabel('x')
plt.ylabel('P(x)')

plt.savefig('output/2d_r-samples.png')
plt.clf()


# sample theta and phi
angles = samp.spherical(100).T
theta, phi = angles[0], angles[1]

# generate a table of (r ,theta, phi) for 100 galaxies
galaxies = np.array([r[0], theta, phi])
galaxies = pd.DataFrame(galaxies.T, columns=['r', 'theta', 'phi'])
galaxies.to_csv('output/2d_galaxies.csv', sep='\t')


''' 2 e)
Repeat (d) for 1000 haloes each containing 100 satellites. Make another log-log 
plot showing N (x) = n(x)4πx2 over the same range as before, but now over-plot 
a histogram showing the average number of satellites in each bin. Use 20 
logarithmically-spaced bins between x = 10−4 and xmax and don’t forget to 
divide each bin by its width. Do your generated galaxies match this distribution?
'''
print('2 e) generating 1000 haloes')

# define the function N to be used here in 2 e) and f)
N = lambda x: dist.probability(x)*dist.Nsat

# sample 1000 haloes
Nsat = 100
Nhalo = 1000
halos = np.ndarray((Nhalo, 3, Nsat))

for h in range(Nhalo):
    r = samp.rejection(dist.probability, Nsat, 
                       xrange=(xmin, xmax), yrange=(0, 4)).T
    theta, phi = samp.spherical(Nsat).T
    galaxies = np.array([r[0], theta, phi])
    halos[h, :, :] = galaxies


# create a table of histograms for each of the 1000 halos
nbins = 20
bins = np.log10(np.logspace(np.log10(xmin), np.log10(xmax), nbins+1))

halo_hist = np.ndarray((Nhalo, nbins))
for h, halo in enumerate(halos):
    logr = np.log10(halo[0])
    halo_hist[h, :]  = np.histogram(logr, bins)[0]


# plot the function and histogram
plt.plot(np.log10(truex), N(truex), lw=5, alpha=.8)
plt.bar(bins[:-1], rt.mean(halo_hist), .2, alpha=.5, color='C1')

plt.yscale('log')
plt.ylim([1e-3, 1e4])

plt.xlabel('$\log_{10}(x)$')
plt.ylabel('$N(x)$')

plt.savefig('output/2e_average-r.png')
plt.clf()


''' 2 f)
Write a root-finding algorithm to find the solution(s) to N(x) = y/2 in the 
same x-range, where y is the maximum of N(x). Use the same parameter values as 
before. Output the root(s).
'''
print('2 f) minimization and root finding')

import nur.minimization as minim
import nur.root_finding as rf

# find the function maximum
Nmaxx = minim.golden(lambda x: -N(x), .1, 1)
Nmaxy = N(Nmaxx)

# plot the location of N(y/2) and y/2
plt.plot(truex, N(truex), lw=5, alpha=.8, label='true')
plt.axvline(Nmaxx, c='k', linestyle='dashed', lw=2)
plt.axhline(Nmaxy/2, c='k', linestyle='dotted', lw=2)

plt.xlabel('x')
plt.ylabel('N(x)')

plt.savefig('output/2f_max.png')
plt.clf()


# find N(x) = y/2
Nshift = lambda x: N(x)-Nmaxy/2
r1 = rf.bisect(Nshift, 1e-4, Nmaxx)
r2 = rf.bisect(Nshift, Nmaxx, 5)

write('output/2f_roots.txt', 'r1: %s\tr2 %s' %(r1, r2))

# plot location of the roots
plt.plot(truex, N(truex), lw=5, alpha=.8, label='true')
plt.axhline(Nmaxy/2, c='k', linestyle='dotted', lw=2)

plt.axvline(r1, c='k', linestyle='dashed', lw=2)
plt.axvline(r2, c='k', linestyle='dashed', lw=2)

plt.xlabel('x')
plt.ylabel('N(x)')

plt.savefig('output/2f_roots.png')
plt.clf()


''' 2 g)
Take the radial bin from (e) containing the largest number of galaxies. Using 
sorting, calculate the median, 16th and 84th percentile for this bin and output 
these values. Next, make a histogram of the number of galaxies in this radial 
bin in each halo (so 1000 values), each bin of this histogram should have a 
width of 1. Plot this histogram, and over-plot the Poisson distribution (using 
your code from 1(a)) with λ equal to the mean number of galaxies in this radial 
bin.
'''
print('2 g) sorting, poisson')

import nur.sorting as sort

# find the maximum bin
max_bin = np.argmax(rt.mean(halo_hist))
ngals = halo_hist[:, max_bin]

# sort galaxies in the radial bin
sort.quick_sort(ngals)

# find median and percentiles
median = rt.median(ngals)
p16, p84 = rt.percentile(ngals, 0.16), rt.percentile(ngals, 0.84)

write('output/2g_median-percentiles.txt', 
      'Median: %s\t16th Percentile: %s\t84th Percentile: %s' \
      %(median, p16, p84))


# plot poisson distribution and histogram
x = np.arange(ngals[0]-5, ngals[-1]+5)
plt.plot(x, [poisson(rt.median(ngals), k) for k in x], lw=5, alpha=.8)

ngals_hist, ngals_bins = np.histogram(ngals, bins=x)
plt.bar(ngals_bins[:-1], ngals_hist/len(ngals), alpha=.5, color='C1')

# plot median and percentile lines
plt.axvline(rt.median(ngals), c='k', lw=2, linestyle='dashed', label='median')
plt.axvline(rt.percentile(ngals, .16), c='k', lw=2, linestyle='dotted', label='16th')
plt.axvline(rt.percentile(ngals, .84), c='k', lw=2, linestyle='dotted', label='84th')

plt.xlabel('Number of galaxies')

plt.savefig('output/2g_ngal.png')
plt.clf()


''' 2 h)
The normalization factor A depends on all three parameters. Calculate A at 0.1 
wide intervals in the ranges of a, b and c given above (including the 
boundaries). You should get a table containing 6240 values. Choose an 
interpolation scheme and write a 3D interpolator for A as a function of the 
three parameters based on these calculated values.
'''
print('2 h) finding values for A')

from scipy.interpolate import RegularGridInterpolator

step_size = 0.1
a_range = np.arange(1.1, 2.5+step_size, step_size)
b_range = np.arange(0.5, 2+step_size, step_size)
c_range = np.arange(1.5, 4+step_size, step_size)

A_table = np.ndarray((len(a_range), len(b_range), len(c_range)))

try:
    A_table = np.load('output/A_table.npy')
except FileNotFoundError:
    print("!!! THIS SHOULDN'T HAVE TO RUN BECAUSE IT TAKES 2 HOURS !!!")
    step_size = 0.1
    a_range = np.arange(1.1, 2.5+step_size, step_size)
    b_range = np.arange(0.5, 2+step_size, step_size)
    c_range = np.arange(1.5, 4+step_size, step_size)

    A_table = np.ndarray((len(a_range), len(b_range), len(c_range)))
    for i, a in enumerate(a_range):
        print(i)
        for j, b in enumerate(b_range):
            for k, c in enumerate(c_range):
                A_table[i, j, k] = GalaxyProfile(a=a, b=b, c=c).A
              
    np.save('output/A_table', A_table)

fn = RegularGridInterpolator((a_range, b_range, c_range), A_table)
write('output/2f_3dinterp.txt', str(fn([[2, 1, 3], [1.5, 1.5, 2]])))


''' 3
Now we are going to turn things around. Download these files:
    https://home.strw.leidenuniv.nl/~daalen/files/satgals_m11.txt
    https://home.strw.leidenuniv.nl/~daalen/files/satgals_m12.txt
    https://home.strw.leidenuniv.nl/~daalen/files/satgals_m13.txt
    https://home.strw.leidenuniv.nl/~daalen/files/satgals_m14.txt
    https://home.strw.leidenuniv.nl/~daalen/files/satgals_m15.txt

Each file contains haloes in a certain mass bin with variable numbers of 
satellites. Write down the log-likelihood corresponding to a set of random 
realizations of the satellite profile in equation (2) with some unknown <Nsat>. 
Retain only the terms with a (residual) dependence on a, b and/or c (including 
A = A(a, b, c)).
'''
print('3 parsing data files')

haloes = {}
for mass in [11, 12, 13, 14, 15]:
    data = []
    with open('data/satgals_m%s.txt' %mass, 'r') as f:
        for line in f.readlines()[4:]:
            if line.startswith('#'): continue
            data.append(line)

    for i, val in enumerate(data):
        data[i] = np.array(val.strip().split(), dtype='float')

    data = np.array(data)

    m = 'm%s' %mass
    haloes[m] = {}
    haloes[m]['r'] = data[:,0]
    haloes[m]['theta'] = data[:,1]
    haloes[m]['phi'] = data[:,2]


plt.hist([haloes['m11']['r'], haloes['m12']['r'], haloes['m13']['r'], haloes['m14']['r'], haloes['m15']['r']],
        histtype='step', lw=2, alpha=.5, label=['m11', 'm12', 'm13', 'm14', 'm15'], density=True, bins=20)

plt.legend()
plt.savefig('output/3_hist.png')
plt.clf()


print('\n\nTOTAL TIME: %.2f seconds\n\n' %(time.time() - start))
