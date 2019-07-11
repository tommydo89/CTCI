# In an array of integers, a "peak" is an element which is greater than or equal to
# the adjacent integers and a "valley" is an element which is less than or equal to the adjacent integers. For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys. Given an array
# of integers, sort the array into an alternating sequence of peaks and valleys.
# EXAMPLE
# Input: {5, 3, 1, 2, 3}
# Output: {5, 1, 3, 2, 3} 

def peaksAndValleys(array):
	array.sort(reverse = True)
	start = 0
	end = len(array) - 1
	result = []
	while start <= end:
		if start == end:
			result.append(array[start])
		else:
			result.append(array[start])
			result.append(array[end])
		start += 1
		end -= 1
	return result

