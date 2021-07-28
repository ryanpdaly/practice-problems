'''
The sum of the squares of the first ten natural numbers is,

    1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,

    (1+2+...+10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is

3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
'''

def sum_of_squares(numbers):
    result = 0
    for n in numbers:
        result = result + n**2
    return(result)

def square_of_sums(numbers):
    summed = sum(numbers)
    return(summed**2)

def sum_square_diff(n):

    numbers = []
    for i in range(1, n+1):
        numbers.append(i)

    sums = sum_of_squares(numbers)
    square = square_of_sums(numbers)

    return(square-sums)

print(sum_square_diff(100))
