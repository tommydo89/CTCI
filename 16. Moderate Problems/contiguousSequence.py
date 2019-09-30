# You are given an array of integers (both positive and negative). Find the
# contiguous sequence with the largest sum. Return the sum. 

#iterate through the array and sum the values. If a sum is negative, start back at 0

def contiguousSequence(arr):
	highest = 0
	curr_sum = 0
	# as long as the sum of all the previous numbers are positive, we will want to add them
	for num in arr:
		curr_sum += num
		if curr_sum > highest:
			highest = curr_sum
		elif curr_sum < 0:
			curr_sum = 0
	return highest