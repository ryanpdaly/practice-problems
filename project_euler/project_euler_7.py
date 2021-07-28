'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import math

N = 100001

n_init = 3 * (10**5)

sieve = []

def append_sieve(j):
    temp = [True] * j

    return(temp)

sieve = sieve + append_sieve(n_init)

for i in range(2, math.sqrt()):
    if sieve[i] == True:
        for j in range(0, len(sieve))
            test = i**2 + j*i
            if test > len(sieve):
                break
            else:
                sieve[test] == False
