import time 
import json
import math
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
from random import choice

n = 99933038

''' Choice of the prime coefficients. 
We preemptively saved into a file a list of all prime numbers smaller than the size of the bloom filter in order to avoid generating them many times, since it is an expensive operation. Then we randomly chose coefficients of different extent to be sure of covering the whole extension of the filter with the hashes of the passwords. 
'''
def coefficients():
    with open('primes.json') as pr:
        primes = json.load(pr)
    primes_split = [*np.array_split(list(primes), 20)]
    c1, c2 = [], []
    for i in range(20):
        c1.append(choice(primes_split[i]))
        c2.append(choice(primes_split[i]))
    return c1, c2

                  
''' Hash functions used in the implementation of the bloom filter. 
Given a 20-characters string s = (s_0,...,s_19) and two sets of coefficients c1 and c2, the following function returns two different hash values of s  computed as the sum modulo n of a_i*s_i for all i = 0,...,19. 
'''
def hash_functions(s, c1, c2, m):
    sum_string1, sum_string2 = 0, 0
    for i in range(20):
        sum_string1 = (sum_string1 + c1[i]*ord(s[i]))
        sum_string2 = (sum_string2 + c2[i]*ord(s[i])) 
    return sum_string1 % m , sum_string2 % m
                  
            
# Functions that update the bloom filter with a new password                
def bloom_filter_update(password, c1, c2, B, m):
    a, b = hash_functions(password, c1, c2, m)
    B[a], B[b] = 1, 1                 


# Function that returns if the a given password is in filter or not (although if the returned value is True, that new_pass can still be a false negative)
                  
def BloomFilter(c1, c2, m):
    start = time.time()
    counter = 0          
    with open("passwords2.txt") as p1:
        for new_pass in p1:
            if len(new_pass.strip())==20:
                i1, i2 = hash_functions(new_pass, c1, c2, m)
                if B[i1]=='1' and B[i2]=='1':
                    counter += 1     
    end = time.time()
    tot_time = end-start
    return counter, tot_time, B

# The two following functions are used to plot the error rate of false positive against the dimension of the bloom filter

def p(m, k):
    p = pow(1 - math.exp(-k / (m/ n)), k)
    return p

def plot_error_size():
    m = 957864004
    x = [m]
    k = [1,2,3,4,6,8]
    for i in range(1,20):
        x.append(math.ceil(m/i))
    col = ['r', 'orange', 'y', 'g', 'blue', 'purple']
    plt.figure(figsize=(10,8))
    for i in range(6):
        y = [p(m, k[i]) for m in x]
        plt.plot(x, y, label = 'k = %d'%k[i], color = col[i])
    plt.scatter(159644033, p(159644033, 2), s=250, c= 'darkred', marker='*')
    plt.title('Error rate of false positive in ralation with the size of the bloom filter', fontsize="x-large")
    plt.legend(loc='right', shadow=True, fontsize="x-large")
    plt.xlabel('m : size of the bloom filter (bits)', fontsize = 'large')
    plt.ylabel('p (error rate of false positives)', fontsize = 'large')
    plt.ticklabel_format(axis='x', style='sci', scilimits=(0,9), useMathText=True)
    plt.show()
