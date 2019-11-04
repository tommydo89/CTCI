#  Given an array filled with letters and numbers, find the longest subarray with
# an equal number of letters and numbers.

# brute force 
def lettersAndNumbers(arr):
	start = 0
	end = 0
	max_length = 0
	# iterate through every sub array
	for start_index in range(0, len(arr)):
		letter_ct = 0
		number_ct = 0
		length = 0 
		for index in range(start_index, len(arr)):
			if isinstance(arr[index], int):
				number_ct += 1
			else:
				letter_ct += 1
			length += 1
			if letter_ct == number_ct and length > max_length:
				start = start_index
				end = index
				max_length = length
	return arr[start:end+1]