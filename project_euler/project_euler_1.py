summed = 0

for n in range(0, 1000):
    if n%3 == 0:
        #divisible.append(n)
        summed = summed + n
    elif n%5 == 0:
        #divisible.append(n)
        summed = summed + n

print(summed)
