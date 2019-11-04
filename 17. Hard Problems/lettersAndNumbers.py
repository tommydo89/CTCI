#  Given an array filled with letters and numbers, find the longest subarray with
# an equal number of letters and numbers.

# brute force 
# def lettersAndNumbers(arr):
# 	start = 0
# 	end = 0
# 	max_length = 0
# 	# iterate through every sub array
# 	for start_index in range(0, len(arr)):
# 		letter_ct = 0
# 		number_ct = 0
# 		length = 0 
# 		for index in range(start_index, len(arr)):
# 			if isinstance(arr[index], int):
# 				number_ct += 1
# 			else:
# 				letter_ct += 1
# 			length += 1
# 			if letter_ct == number_ct and length > max_length:
# 				start = start_index
# 				end = index
# 				max_length = length
# 	return arr[start:end+1]

# optimized


# if we append an equal subarray to any array that is not equal, then the difference between numbers and letters will be equal at the end of the first
# array and at the end of the equal subarray
# Example:     a  a | 1  a  1  a
# number_ct:   0  0 | 1  1  2  2
# letter_ct:   1  2 | 2  3  3  4
# difference: -1 -2 |-1 -2 -1 -2
def lettersAndNumbers(arr):
	differences = {} # maps each difference to the first index where it occurred
	letter_ct = 0
	number_ct = 0
	max_length = 0
	start = 0 # start of the result sub-array
	end = 0 # end of the result sub-array
	for index in range(0, len(arr)):
		if isinstance(arr[index], int):
			number_ct += 1
		else:
			letter_ct += 1
		if number_ct == letter_ct: # longest possible subarray that is possible at the current iteration
			start = 0
			end = index
		else: # check if the current difference has occurred
			difference = number_ct - letter_ct
			if difference not in differences:
				differences[difference] = index
			else:
				length = index - differences[difference]
				if length > max_length:
					max_length = length
					start = differences[difference] + 1
					end = index + 1
	return arr[start:end]

