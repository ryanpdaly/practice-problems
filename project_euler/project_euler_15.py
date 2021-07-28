'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''
import math

def main(grid_size):
	X = grid_size[0]
	Y = grid_size[1]
	
	# The number of permutations in either direction is given by (N)!, meaning the total number of possible moves is ((X)+(Y))!
	# But we must account for the fact that a move itself is not unique, only the order of the combination
	# Then we must divide by possible number N! in both directions
	# Meaining our net permutations is given by: (X+Y)! /(X!*Y!)

	combos = int(math.factorial((X)+(Y)) / (math.factorial(X)*math.factorial(Y)))
	return(combos)

print(main((20,20)))