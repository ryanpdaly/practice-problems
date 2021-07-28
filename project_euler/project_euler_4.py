'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

products = []

for i in range(1000, 100, -1):
    for j in range(1000, 100, -1):
        product =  i*j

        rev = int(str(product)[::-1])

        if product == rev:
            products.append(product)

products.sort()

print(products[-1])
