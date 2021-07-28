numbers = [3, 8, 7, 9, 6, 1, 12, 5, 14, 2, 19, 16, 18, 11, 10, 15, 13, 17, 20]

numbers.sort()

for (index, value) in enumerate(numbers):
	try:
		if (numbers[index+1] - value) != 1:
			numbers.insert(index+1, value+1)
	except IndexError:
		break

print(numbers)