'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math

n = 600851475143

def factorize(n):
    while True:
        p = int(smallest_factor(n))

        if p < n:
            n = n//p
        else:
            return(n)
    

def smallest_factor(m):
    for i in range(2, m+1):
        if m%i == 0:
            return(i)

print(factorize(n))


