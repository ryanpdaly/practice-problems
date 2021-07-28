'''
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?
'''

import functools
import math

n = 20
numbers = []
for i in range(1, n+1):
    numbers.append(i)

def least_common(numbers):
    def lcm(a, b):
        return((a*b) // GCD(a,b))

    return(functools.reduce(lcm, numbers, 1))

def GCD(a, b):
    if b == 0:
        return(a)
    else:
        return(GCD(b,a%b))

print(least_common(numbers))
