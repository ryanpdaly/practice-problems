'''
Write a function that reverses a string. The input string is given as an array of characters s.
Follow up: Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''

def use_builtin(str):
	str.reverse()

def recusion(str):
	# Time Complexity: O(N) to complete O(N/2) swaps
	# Space Complexity: O(N) to keep recursion stack
	def helper(left, right):
		if left < right:
			str[left], str[right] = str[right], str[left]
			helper(left+1, right-1)

	helper(0, len(str)-1)

def two_pointers(str):
	# Time complexity: O(N) to swap N/2 elements
	# Space complexity: O(1)
	left = 0
	right = len(s) -1

	while left < right:
		s[left], s[right] = s[right], s[left]
		left, right = left+1, right-1