# You have an array with all the numbers from 1 to N, where N is at most 32,000. The
# array may have duplicate entries and you do not know what N is. With only 4 kilobytes of memory
# available, how would you print all duplicate elements in the array? 

def findDuplicates(array):
	max_N = 32000
	bit_vector = bytearray(32000//8 + 1)
	for number in array:
		byte_index = number // 8
		bit_index = number % 8
		if bit_vector[byte_index] & (1 << bit_index) != 0: # if true, that means the current number is a duplicate
			print(number)
		else: # set bit flag to 1 to indicate that we have seen this number
			bit_vector[byte_index] |= (1 << bit_index)
